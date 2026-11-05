---
name: brief-qualifier
description: Qualify a client or project brief for social content planning. Use when checking whether a brief is complete, consistent with approved knowledge, and ready to hand into planning; identify gaps and ask focused questions instead of guessing.
---

# Brief Qualifier

## Purpose

Review a supplied social-content brief before planning begins. Return a clear readiness verdict, evidence-based gaps and conflicts, and only the follow-up questions needed to resolve them.

This skill qualifies the brief. It does not create a content calendar or posts, approve client knowledge, calculate the client's Knowledge Readiness Score (KRS), change source files, or publish content.

## Inputs

### Required

- The brief to qualify.
- Client and project identity.
- Channel and planning period, either stated in the brief or supplied as run inputs.
- The applicable context package, including its verdict, required/optional items, approved knowledge records, record versions, freshness results, and any known conflicts.

If the brief or its identity is missing, do not infer it from unrelated files. Return a Blocked verdict and request the missing input.

### Helpful when applicable

- The period calendar or event register, including confirmed events and blackout dates.
- Earlier approved stage outputs or decisions relevant to this brief.
- A brief qualification checklist supplied by the project owner.

## Source and knowledge handling

- Treat the brief and supplied context as the evidence for this run. Identify the source for each material finding (brief section, record ID/version, or supplied calendar entry).
- Use only approved, current, permitted knowledge records as established by the context package.
- Preserve labels such as provisional, candidate, disputed, expired, or unverified. Never present them as approved facts or use them to resolve a conflict.
- A client-specific rule belongs in approved knowledge or the brief, not in this skill.
- If run without an assembler during a pilot, use the knowledge index to locate only the sections relevant to brief qualification. Check each section's status and review date; apply permission and freshness rules. If a critical rule or its status cannot be established, state that limitation or block where it prevents a safe qualification. Do not treat raw files, conversation archives, or evaluation materials as approved knowledge.
- Never infer a target, date, audience, permission, launch status, or approval decision. Do not silently reconcile differing sources. Ask the responsible person to decide.

## Qualification procedure

1. **Identify the brief.** Record client, project, channel, planning period, and brief version/date when supplied. Call out any missing or inconsistent identity details.
2. **Read the context verdict first.** If the context package is Blocked, do not qualify the brief as ready. Return the blocking gaps and owners given by the package. If Limited, continue only within its stated limitations and carry each relevant limitation into the report.
3. **Check the brief's planning essentials.** For each applicable item below, record what the brief says, its source, and whether it is complete, missing, provisional, or conflicting:
   - business/content objective and desired outcome;
   - target audience and, when relevant, geography;
   - planning period and relevant dates;
   - content focus or approved pillars;
   - CTA priorities or destination;
   - scope, cadence or formats when these affect planning;
   - exclusions, confidentiality limits, or other content restrictions;
   - metrics and targets, distinguishing approved targets from historical measures or recommendations;
   - approval requirement and the handoff needed before publication.
4. **Check against approved knowledge and calendar inputs.** Compare relevant statements with the context package and period calendar. Flag missing mandatory information, stale or unauthorized knowledge, conflicting records, unconfirmed events, blackout dates, and dependencies that affect the requested period.
5. **Separate gaps by impact.** Use the stage contract or project checklist when supplied to determine what blocks. A missing critical objective, audience, period, permission, or approval condition should block when it makes the requested planning unsafe or materially indeterminate. Missing helpful detail may be Limited if the work can proceed without making it up. Do not invent a requirement or mark an item mandatory unless the supplied contract or brief establishes that.
6. **Ask focused questions.** Ask one question per unresolved decision where practical. Include the reason and the source conflict or missing field. Name an owner only when a source identifies one; otherwise write “Owner not specified.”
7. **Return the report.** Do not edit the brief or knowledge files. State what can proceed, what must wait, and any proposed knowledge update for human review. Never approve your own findings.

## Readiness verdict

- **READY** — All required brief fields and applicable context inputs are present, current, permitted, and non-conflicting. No material limitation prevents handoff to the next planning step.
- **LIMITED** — The brief can move forward with one or more non-blocking gaps or limitations clearly disclosed. Do not fill them with assumptions.
- **BLOCKED** — A required input is missing, stale, unauthorized, or materially conflicting, or the context package is Blocked. State exactly what must be resolved before planning proceeds.

Use the context package's verdict where one is supplied; do not override it. This verdict is for this brief/run only. It is not the client's KRS band or overall knowledge-layer approval.

## Output format

Return the following Markdown structure. Use “Not provided” or “Not established” rather than leaving ambiguous blanks. Omit a table row only when it is clearly not applicable and state why.

```markdown
# Brief Qualification

## 1. Brief details
- Client:
- Project:  
- Channel:
- Planning period:
- Brief version/date:

## 2. Readiness
- Verdict: READY / LIMITED / BLOCKED
- Reason:
- Context-package verdict and limitations:

## 3. Information checked
| Requirement | Brief says | Source / record ID and version | Finding |
|---|---|---|---|

## 4. Missing information
| Missing detail | Why it matters | Blocking? | Owner |
|---|---|---|---|

## 5. Conflicts or stale/unapproved inputs
| Issue | Sources involved | What needs confirmation | Owner |
|---|---|---|---|

## 6. Questions to resolve
1. ...

## 7. Provisional items and limitations
- ...

## 8. Handoff
- Can proceed:
- Must wait for:
- Possible knowledge or brief update for human review:
```

In “Information checked,” cite only sources actually supplied. In “Possible knowledge or brief update,” describe a proposed change; do not write it into a knowledge file or mark it approved.
