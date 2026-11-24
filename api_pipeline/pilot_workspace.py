"""Persistence for the loopback-only B2B pilot UI."""

from datetime import datetime, timezone
from hashlib import sha256
from ipaddress import ip_address
import json

from fastapi import HTTPException, Request
from pydantic import BaseModel, Field
from pymongo import ReturnDocument
from pymongo.errors import PyMongoError


PILOT = "vajra-preview"
GROUPS = {"clients", "briefs", "runs", "uploads", "records", "posts", "approvals", "audit"}
MAX_BYTES = 6 * 1024 * 1024
STAGES = {
    "qualificationResult": {"context": "context-brief", "qualification": "brief-qualifier"},
    "planningResult": {"context": "context-plan", "planner": "content-planner"},
    "draftingResult": {"context": "context-draft", "writer": "post-writer",
                       "qaContext": "context-qa", "qa": "post-quality-analyst"},
}


class WorkspaceUpdate(BaseModel):
    revision: int = Field(ge=0)
    state: dict[str, list[dict]]


def _local(request):
    try:
        loopback = ip_address(request.client.host).is_loopback if request.client else False
    except ValueError:
        loopback = False
    if not loopback or request.headers.get("x-b2b-pilot") != "1":
        raise HTTPException(403, "Pilot workspace is available only from the local UI.")


def _digest(value):
    raw = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return sha256(raw.encode()).hexdigest()


def _validate(state):
    if set(state) - GROUPS:
        raise HTTPException(422, "Unsupported pilot workspace fields.")
    if len(json.dumps(state, ensure_ascii=False).encode()) > MAX_BYTES:
        raise HTTPException(413, "Pilot workspace exceeds 6 MB.")
    for group, rows in state.items():
        seen = set()
        for row in rows:
            key = row.get("id")
            if not isinstance(key, str) or not key or key in seen:
                raise HTTPException(422, "Pilot rows must have unique string IDs.")
            seen.add(key)
            if group == "clients" and key != PILOT:
                raise HTTPException(422, "This pilot workspace is scoped to Vajra Global.")
            if group != "clients" and row.get("clientId") != PILOT:
                raise HTTPException(422, "Pilot rows must belong to Vajra Global.")
    brief_ids = {row["id"] for row in state.get("briefs", [])}
    run_ids = {row["id"] for row in state.get("runs", [])}
    for run in state.get("runs", []):
        if not isinstance(run.get("briefId"), str) or run["briefId"] not in brief_ids:
            raise HTTPException(422, "A run must reference a saved brief.")
    for group in ("posts", "approvals"):
        for row in state.get(group, []):
            if not isinstance(row.get("runId"), str) or row["runId"] not in run_ids:
                raise HTTPException(422, "A post or approval must reference a saved run.")
    for post in state.get("posts", []):
        if post.get("status") not in {"Needs revision", "Awaiting approval", "Held", "Rejected", "Changes requested"}:
            raise HTTPException(422, "Publishing decisions are unavailable in this pilot.")
        if type(post.get("version")) is not int or post["version"] < 1 or not isinstance(post.get("copy"), str):
            raise HTTPException(422, "A post requires copy and a positive draft version.")
        if not isinstance(post.get("decisions", []), list) or any(
            not isinstance(decision, dict) or not isinstance(decision.get("decidedAt"), str)
            for decision in post.get("decisions", [])
        ):
            raise HTTPException(422, "Invalid post decisions.")


def _upsert(collection, identity, fields, session):
    return collection.find_one_and_update(
        identity, {"$set": fields, "$setOnInsert": {"createdAt": datetime.now(timezone.utc)}},
        upsert=True, return_document=ReturnDocument.AFTER, session=session,
    )["_id"]


def _project_rows(db, scope, current, previous, session):
    def changed(group):
        old = {row["id"]: row for row in previous.get(group, [])}
        return (row for row in current.get(group, []) if old.get(row["id"]) != row)

    for row in changed("briefs"):
        identity = {**scope, "previewId": row["id"]}
        db.briefs.update_one(
            identity,
            {"$setOnInsert": {"currentVersion": 1, "versions": [{"version": 1, **{
                k: row.get(k) for k in ("fields", "period", "postCount", "name", "issues", "validated")
            }}], "createdAt": datetime.now(timezone.utc)}},
            upsert=True, session=session,
        )
    for row in changed("records"):
        record = {**scope, "recordKey": "preview:" + row["id"], "version": _digest(row)}
        db.knowledgeVersions.update_one(
            record, {"$setOnInsert": {"status": str(row.get("state", "Captured")).lower(),
                                      "data": row, "createdAt": datetime.now(timezone.utc)}},
            upsert=True, session=session,
        )
    for row in changed("runs"):
        brief = db.briefs.find_one({**scope, "previewId": row["briefId"]}, {"_id": 1}, session=session)
        run_id = _upsert(db.runs, {**scope, "previewId": row["id"]}, {
            "briefId": brief["_id"], "briefVersion": 1,
            **{key: row.get(key) for key in ("status", "period", "startedAt", "knowledgeVersion", "openFeedback")},
        }, session)
        for group, keys in STAGES.items():
            for key, stage in keys.items():
                result = (row.get(group) or {}).get(key)
                if not isinstance(result, dict):
                    continue
                identity = {**scope, "runId": run_id, "stageKey": stage}
                signature = _digest(result)
                if db.stageExecutions.find_one({**identity, "resultHash": signature}, {"_id": 1}, session=session):
                    continue
                latest = db.stageExecutions.find_one(identity, sort=[("attempt", -1)], session=session)
                db.stageExecutions.insert_one({
                    **identity, "resultHash": signature, "attempt": 1 + (latest["attempt"] if latest else 0),
                    "status": "completed", "output": result, "createdAt": datetime.now(timezone.utc),
                }, session=session)
        decision = row.get("gate1")
        if isinstance(decision, dict):
            plan = (row.get("planningResult") or {}).get("planner")
            if not isinstance(plan, dict) or plan.get("verdict") not in {"READY", "LIMITED"} or \
                    decision.get("decision") not in {"Approved", "Rejected"}:
                raise HTTPException(422, "A Gate 1 decision requires a reviewable plan.")
            db.reviewDecisions.update_one(
                {**scope, "runId": run_id, "gate": 1, "decisionHash": _digest([plan, decision])},
                {"$setOnInsert": {"planHash": _digest(plan), "previewOnly": True,
                                  **{key: decision.get(key) for key in ("decision", "reason", "decidedAt")}}},
                upsert=True, session=session,
            )
    for row in changed("posts"):
        run = db.runs.find_one({**scope, "previewId": row["runId"]}, {"_id": 1}, session=session)
        post_id = _upsert(db.contentItems, {**scope, "previewId": row["id"]}, {
            "runId": run["_id"],
            **{key: row.get(key) for key in ("title", "status", "qaStatus", "scheduledAt", "comments")},
        }, session)
        version = row.get("version", 1)
        draft = db.draftVersions.find_one_and_update(
            {**scope, "contentItemId": post_id, "version": version},
            {"$setOnInsert": {"copy": row.get("copy", ""), "createdAt": datetime.now(timezone.utc)}},
            upsert=True, return_document=ReturnDocument.AFTER, session=session,
        )
        if draft["copy"] != row.get("copy", ""):
            raise HTTPException(409, "Edited copy requires a new draft version.")
        db.contentItems.update_one({"_id": post_id}, {"$set": {"currentDraftId": draft["_id"]}}, session=session)
        for decision in row.get("decisions", []):
            reviewed = db.draftVersions.find_one(
                {**scope, "contentItemId": post_id, "version": decision.get("version")},
                {"_id": 1}, session=session,
            )
            if reviewed is None or decision.get("decision") not in {"Held", "Rejected", "Changes requested"}:
                raise HTTPException(422, "Invalid pilot decision or draft version.")
            db.reviewDecisions.update_one(
                {**scope, "gate": 2, "decisionHash": _digest([row["id"], decision])},
                {"$setOnInsert": {"runId": run["_id"], "draftVersionId": reviewed["_id"], "previewOnly": True,
                                  "decision": decision["decision"], "reason": decision.get("reason"),
                                  "decidedAt": decision["decidedAt"]}},
                upsert=True, session=session,
            )


def register_pilot_workspace(app, get_database, get_scope):
    def context(request):
        _local(request)
        db = get_database()
        if db is None:
            raise HTTPException(503, "Set MONGODB_URI in the FastAPI terminal.")
        scope = get_scope(db)
        if scope is None:
            raise HTTPException(503, "Seed the Vajra Global pilot in Atlas first.")
        return db, scope

    @app.get("/api/pilot/workspace")
    def load_workspace(request: Request):
        try:
            db, scope = context(request)
            project = db.projects.find_one({"_id": scope["projectId"], "clientId": scope["clientId"]},
                                           {"pilotWorkspace": 1})
            return project.get("pilotWorkspace", {"revision": 0, "state": {}})
        except PyMongoError:
            raise HTTPException(503, "MongoDB workspace could not be loaded.") from None

    @app.put("/api/pilot/workspace")
    def save_workspace(payload: WorkspaceUpdate, request: Request):
        _validate(payload.state)
        try:
            db, scope = context(request)
            identity = {"_id": scope["projectId"], "clientId": scope["clientId"]}
            with db.client.start_session() as session:
                with session.start_transaction():
                    project = db.projects.find_one(identity, {"pilotWorkspace": 1}, session=session)
                    previous = project.get("pilotWorkspace", {"revision": 0, "state": {}})
                    if previous["revision"] != payload.revision:
                        raise HTTPException(409, "The workspace changed in another tab. Reload to continue.")
                    revision = payload.revision + 1
                    db.projects.update_one(identity, {"$set": {
                        "pilotWorkspace": {"revision": revision, "state": payload.state},
                    }}, session=session)
                    _project_rows(db, scope, payload.state, previous["state"], session)
            return {"revision": revision}
        except PyMongoError as error:
            if error.has_error_label("TransientTransactionError"):
                raise HTTPException(409, "The workspace changed during save. Reload to continue.") from None
            raise HTTPException(503, "MongoDB could not confirm the workspace save.") from None
