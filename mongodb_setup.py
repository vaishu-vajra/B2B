"""Initialize the shared social content database and optionally seed Group 1."""

import argparse
import hashlib
import os
from datetime import datetime, timezone
from pathlib import Path

from pymongo import ASCENDING, DESCENDING, MongoClient, ReturnDocument
from pymongo.errors import CollectionInvalid, PyMongoError


CORE_INDEXES = {
    "clients": [("client_key", [("slug", ASCENDING)], True)],
    "projects": [
        ("project_key", [("clientId", ASCENDING), ("slug", ASCENDING)], True),
    ],
    "knowledgeVersions": [
        ("knowledge_version", [("clientId", ASCENDING), ("recordKey", ASCENDING), ("version", ASCENDING)], True),
        ("knowledge_scope", [("clientId", ASCENDING), ("projectId", ASCENDING), ("status", ASCENDING)], False),
    ],
    "briefs": [
        ("project_briefs", [("clientId", ASCENDING), ("projectId", ASCENDING), ("createdAt", DESCENDING)], False),
    ],
    "runs": [
        ("brief_runs", [("clientId", ASCENDING), ("briefId", ASCENDING), ("startedAt", DESCENDING)], False),
    ],
    "stageExecutions": [
        ("stage_attempt", [("clientId", ASCENDING), ("runId", ASCENDING), ("stageKey", ASCENDING), ("attempt", ASCENDING)], True),
    ],
    "contentItems": [
        ("content_queue", [("clientId", ASCENDING), ("projectId", ASCENDING), ("status", ASCENDING), ("plannedFor", ASCENDING)], False),
    ],
    "draftVersions": [
        ("draft_version", [("clientId", ASCENDING), ("contentItemId", ASCENDING), ("version", ASCENDING)], True),
    ],
    "reviewDecisions": [
        ("draft_reviews", [("clientId", ASCENDING), ("draftVersionId", ASCENDING), ("reviewedAt", DESCENDING)], False),
    ],
}

DELIVERY_INDEXES = {
    "publications": [
        ("publishing_job", [("clientId", ASCENDING), ("jobKey", ASCENDING)], True),
        ("due_publications", [("status", ASCENDING), ("scheduledAt", ASCENDING)], False),
    ],
    "performanceSnapshots": [
        ("publication_metrics", [("clientId", ASCENDING), ("publicationId", ASCENDING), ("capturedAt", DESCENDING)], False),
    ],
}

KNOWLEDGE_TYPES = {
    "brand.md": "brand",
    "claims.md": "claims",
    "market.md": "market",
    "learning.md": "learning",
    "operations.md": "operations",
}


def initialize(database, include_delivery):
    indexes = CORE_INDEXES | (DELIVERY_INDEXES if include_delivery else {})
    for collection_name, definitions in indexes.items():
        try:
            database.create_collection(collection_name, check_exists=False)
        except CollectionInvalid:
            # MongoDB may report an existing namespace on a repeat setup.
            if collection_name not in database.list_collection_names():
                raise
        except PyMongoError as error:
            if getattr(error, "code", None) != 48:
                raise
        for name, keys, unique in definitions:
            database[collection_name].create_index(keys, name=name, unique=unique)
    return len(indexes)


def seed_pilot(database, knowledge_dir):
    sources = {
        filename: (knowledge_dir / filename).read_text(encoding="utf-8-sig")
        for filename in KNOWLEDGE_TYPES
    }
    now = datetime.now(timezone.utc)
    client = database.clients.find_one_and_update(
        {"slug": "vajra-global"},
        {"$setOnInsert": {"name": "Vajra Global", "status": "active", "createdAt": now}},
        upsert=True,
        return_document=ReturnDocument.AFTER,
    )
    project = database.projects.find_one_and_update(
        {"clientId": client["_id"], "slug": "linkedin-content-pilot"},
        {"$setOnInsert": {
            "name": "LinkedIn Content Pilot",
            "channels": ["linkedin"],
            "status": "active",
            "createdAt": now,
        }},
        upsert=True,
        return_document=ReturnDocument.AFTER,
    )
    for filename, markdown in sources.items():
        record_type = KNOWLEDGE_TYPES[filename]
        source_hash = hashlib.sha256(markdown.encode("utf-8")).hexdigest()
        database.knowledgeVersions.update_one(
            {
                "clientId": client["_id"],
                "recordKey": record_type,
                "version": f"import-{source_hash}",
            },
            {"$setOnInsert": {
                "projectId": project["_id"] if record_type == "operations" else None,
                "type": record_type,
                "status": "draft",
                "data": {"markdown": markdown},
                "sourceRefs": [{"filename": filename, "sha256": source_hash}],
                "createdAt": now,
            }},
            upsert=True,
        )
    print(f"Seeded {client['name']} and {project['name']} with {len(sources)} draft knowledge sources.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--knowledge-dir", type=Path, help="Opt in to importing the pilot Markdown sources.")
    parser.add_argument("--include-delivery", action="store_true", help="Also create publishing and metrics collections.")
    args = parser.parse_args()
    uri = os.environ.get("MONGODB_URI", "").strip()
    database_name = os.environ.get("MONGODB_DB", "social_content_dev").strip()
    if not uri or not database_name:
        parser.exit(1, "Set MONGODB_URI and a non-empty MONGODB_DB (defaults to social_content_dev).\n")
    try:
        with MongoClient(uri, serverSelectionTimeoutMS=5000) as client:
            client.admin.command("ping")
            database = client[database_name]
            count = initialize(database, args.include_delivery)
            print(f"Initialized {count} collections in {database_name}.")
            if args.knowledge_dir is not None:
                seed_pilot(database, args.knowledge_dir)
    except FileNotFoundError as error:
        parser.exit(1, f"Knowledge source missing: {error.filename}\n")
    except (PyMongoError, ValueError) as error:
        parser.exit(1, f"MongoDB setup failed ({type(error).__name__}). Check the connection and database permissions.\n")


if __name__ == "__main__":
    main()
