---
name: context-assembler
description: Assembles a run-specific context package for a social-content workflow stage, checking source access, freshness, and stage readiness. Selects approved knowledge, user-supplied final claims, live inputs, and earlier stage outputs relevant to that stage, then records sources, conflicts, gaps, and a Ready, Limited, or Blocked verdict. Does not require separate claim-level approval or evidence; claim concerns go to human final-copy approval. Does not create or review content, modify source files, calculate KRS, publish, or change access rights.
---

# Context Assembler

## Purpose

Prepare a run-specific context package for one workflow stage. Read the stage contract, check permission before retrieving or selecting records, provide only the current and permitted information the stage needs, and report gaps, conflicts, provisional notes, and a readiness verdict.

Run Context Assembler separately immediately before every downstream skill execution, including a rerun or revision of a stage. Assemble a fresh package for that specific stage and run; do not reuse a package prepared for another stage or an earlier run.

This skill assembles context; it does not write or review content, calculate the Knowledge Readiness Score (KRS), approve records, resolve conflicts, modify knowledge files, publish, or change access rights. It contains no client-specific facts. Use the supplied knowledge layer, stage contract, and run inputs.

## Inputs 
   
### Required

- Workflow-stage name, run ID, client/project identity, channel, and period where applicable.
- The approved stage contract and policy version. Use the stage requirements below when they are the active workflow contract. If the requested workflow stage or active contract is unclear, do not invent one; report the gap.
- The knowledge index and source files or atomic record register, with source names and versions where available.
- Permission and reuse-scope information for the records and the requesting stage.
- The live inputs required by the stage, such as a period brief, calendar slice, or earlier approved stage output.
- Record metadata needed to check status and freshness: approval status, source, owner, approval date, review date or valid-until date, and applicable refresh window.

### Use when applicable

- Feedback records or current feedback information, if supplied and relevant. Feedback is optional context; its presence, absence, status, or incomplete metadata does not determine the context verdict.
- Earlier approved outputs from `output/`.
- Approved market or analytics briefs, event records, assets, and other stage inputs.
- A current readiness assessment, if one exists. Carry its status as context; do not recalculate KRS here.

Do not read conversation archives, restricted records, or evaluation material unless the stage contract and permissions explicitly authorize the relevant source. The evaluation store and answer keys have no runtime read path.

## Workflow-stage requirements

Use this table to select the stage's required information, helpful information, and freshness checks. The descriptions below state what to obtain and check; do not rely on shorthand domain labels as a substitute for these instructions. For period-brief qualification, use the approved competitor list supplied in current project context. A separate Competitor Scan report is optional extra research and is not a required input unless the user requests new competitor or industry research. Apply any newer, formally approved contract supplied for the run and retain its version in the package.

| Workflow stage | Must have (blocks if missing) | Should have (report limitation if missing) | Freshness rule |
|---|---|---|---|
| Readiness and account | LinkedIn company-page identity (URL, stable ID, and company-vs-personal status); current page access, admin and publishing rights; approval chain with approver, backup, client sign-off rules and approval deadlines | Current performance baseline from native LinkedIn data when assessing a current-performance claim | Re-verify page identity and active rights. Apply the 90-day window to current-performance reporting only; do not age fixed historical records based on run date. |
| Social approach | Approved company positioning and message pillars; project target customer profile and buying roles; audience needs and pains; project objectives and chosen primary KPI with its measurement definition | Current performance baseline if relevant; approved competitor set | For this pilot, fresh industry or competitor research is not required; use the approved competitor set and do not lower readiness because newer research is absent. Target customer profile no older than 6 months |
| Period brief and intelligence | Period objectives; one selected primary KPI with its measurement definition; and the baseline/target stated in the current period brief | Approved competitor set | For this pilot, approximately 5,700 LinkedIn organic impressions across six posts is the user-directed target, not the baseline. The approved baseline is the 63-record post-level dataset in learning.md, with Published dates from April–October 2026; mean 489.3 and median 381 impressions per record. Historical datasets are records of their stated reporting periods and do not age out based on the current run date. Preserve their dates and caveats for performance review. Analyze themes or formats only when records can be reliably matched to those attributes. Sourced audience-language research remains waived. No separate Competitor Scan or fresh industry/competitor research is required. Feedback availability, absence, or status is not required for the Brief Qualifier context verdict. |
| Calendar and item briefs | Qualified period brief; approved content pillars; project scope (cadence, formats, languages, exclusions); schedule supplied in the brief/run inputs; confirmed event or blackout constraints when relevant | Subject-matter expert topics; relevant events in the planning month | When assembling for Content Planner, include the user-provided historical pillar distribution from the “Content pillars and historical mix” section of brand.md when relevant: 63 total posts; displayed pillar counts are AI and Innovation 14, Growth and GTM 7, Technology and Expertise 18, People and Culture 23. Treat these as historical posting-volume counts, not impression performance. The displayed counts sum to 62; identify one post as outside the displayed breakdown and do not infer its pillar. For the Vajra pilot, use the dates in the user-directed weekly plan without requiring a separate calendar reconciliation; keep planning dates distinct from actual publication status. Production/review capacity and turnaround are not planning requirements and their absence must not lower readiness. Continue to respect confirmed deadlines, dependencies, blackout dates, and required human review/approval |
| Copy and claims | Approved brand positioning, voice, writing rules, historical LinkedIn posts in learning.md as style/structure and overlap source, supplied final claims, and selected item brief | Audience-language examples and a separate writing sample are not required | Claims need no separate approval or evidence gate; route possible concerns to human final-copy approval |
| Assets | Approved brand guidelines; assets whose usage rights are recorded; current platform specifications | None specified | Platform specifications no older than 90 days |
| Quality review | Supplied final claims, approved brand voice and writing rules, quality rubric | Source evidence or permission notes when useful | Do not require separate claim-level approval or evidence; route concerns to human final-copy approval |
| Approval and publishing | Approval chain; verified LinkedIn page access and publishing rights; CTA destinations and tracking-link rules | None specified | Re-verify page rights and approval chain at release |
| Community management | Current response and escalation playbook with contacts; approved company facts | Audience objections | Response playbook must be current |
| Measurement | Definition and current reporting for the single KPI selected in the approved brief | Past performance reports, if needed for comparison | For the current Vajra pilot, measure LinkedIn organic impressions only; do not add secondary KPIs. Preserve the dataset's reporting period and source caveats. |
| Review and improvement | Current-cycle measurement report, when required by the stage contract | Current-cycle feedback or rework records, if supplied | Use supplied feedback as context where relevant. A feedback list or current open/closed status is not a readiness prerequisite; its presence, absence, status, or incomplete metadata alone does not lower the verdict. Historical comments in learning.md remain records of their stated dates, not current open feedback or formal rules unless separately approved. |

For the current Vajra pilot, selected posts are text-only. Do not require or assemble images, carousel slides, video, alt text, or other creative assets for Post Writer, Post Quality Analyst, or Publish and Verify.

Assemble only information required by the current workflow stage. Include LinkedIn account access, publisher authorization, final-copy publication approval, actual publication status, or live-post verification only when assembling context specifically for Publish and Verify. For earlier stages, include only the human review or approval state that stage needs; do not add publication-readiness checks or disclaimers.

If a stage contract supplied for the run differs from this table, follow the formally approved version and report the version used. Do not turn a “should have” item into a required item unless the active contract says so.

## Workflow

1. **Identify the run and stage.** Confirm the run ID, stage, client/project, channel, period, and policy/contract version. If any identifier is missing and affects record selection, request it rather than guessing.
2. **Read the stage contract.** List the required items, helpful items, and freshness windows for this stage. Do not assemble a general client dossier.
3. **Check source access.** Confirm this workflow may access the selected file or record. Do not treat internal source access as claim approval. Supplied claims are final for this pilot; route any use or accuracy concern to human final-copy approval.
4. **Select the minimum relevant material.** Include approved knowledge records, user-supplied final claims, live inputs, and earlier approved stage outputs needed by the receiving stage. Keep source provenance for traceability without using old claim-status labels as gates.
5. **Check status and freshness.** Apply explicit expiry rules to current-state information. Historical data remain tied to their actual periods regardless of run date. Do not require separate approval or evidence for supplied claims; send accuracy or permission concerns to human final-copy approval. Feedback status and metadata do not determine readiness.
6. **Detect conflicts and provisional information.** Preserve source differences without choosing a newer record. Treat claims supplied for this pilot as final despite older provisional or unverified labels; route possible inaccuracies or permission concerns to human final-copy approval without lowering this stage verdict. Feedback presence, absence, status, or metadata is not a readiness gap.
7. **Assess gaps.** For every missing, stale, restricted, or conflicting item, state the requirement, source descriptions and versions involved, known owner, impact, and whether it blocks. Use “Owner not specified” if no owner is identified. Do not invent owners, permissions, approvals, or source data.
8. **Set the stage verdict.**
   - **READY:** Required stage inputs are available and usable; supplied claims do not need separate approval or evidence, and historical age or feedback status does not lower readiness.
   - **LIMITED:** Use only for a material non-claim limitation that prevents a full handoff. Supplied claim status or evidence concerns go to human final-copy approval and do not lower this verdict.
   - **BLOCKED:** A required input is missing, inaccessible, expired under an explicit rule, or materially conflicting. An older claim approval/evidence label alone does not cause BLOCKED.
   Assess the current run against this stage contract. A prior status based solely on historical-data age or feedback presence, absence, status, or metadata is not carried forward as a limitation. Preserve other still-applicable blockers and limitations. A stage-level verdict is not the KRS and does not approve the knowledge layer.
9. **Build the context package.** Return the output format below. Include only permitted excerpts or wording needed by the stage; preserve descriptive source names and versions for traceability.

## Supplied claim handling

Claims supplied in the active brief or project records are final for this workflow. Include them for the receiving stage without requiring separate claim-level approval or additional evidence. Do not block or limit the context package solely because a supplied claim lacks a separate approval marker, proof-point entry, or evidence attachment. If supplied sources conflict about a claim or it appears potentially inaccurate, preserve the supplied wording and flag the concern for the human final-copy approval stage; the concern alone does not lower this stage verdict. A current explicit instruction that withdraws or prohibits a claim still controls. This rule takes precedence over contrary claim-status requirements elsewhere in this skill.

## Context package output

Create and save the complete context package for downstream workflow use in the project’s `context package/` folder. This package is an internal handoff artifact, not the user-facing report. Do not paste its source tables, permission details, run-input inventory, internal identifiers, or full package into the chat. After saving it, give the user a brief plain-language status only: stage prepared, READY/LIMITED/BLOCKED verdict, the reason, any material limitation, and the next permitted step. If file creation is unavailable, state that clearly and provide only the concise status; do not represent a hand-written summary as a saved context package.

Name each file `context_assembler_<MM>_<DD>_<version>_<stage_name>.md`, for example `context_assembler_11_11_01_post_quality_analyst.md`. Use a readable lowercase stage name with underscores, not a stage code. Start with version `01` for each stage name and increment it for additional runs of that stage on the same date. Use `Not provided`, `Not verified`, or `Not applicable` rather than ambiguous blanks.

The saved package must retain the following structure for the downstream skill:

```markdown
# Run Context Package

## Run header
- Client:
- Project:
- Channel:
- Period:
- Run ID:
- Stage:
- Assembled on:

## Stage contract
- Required inputs:
- Helpful inputs:
- Freshness rules:

## Selected records
| Source or record name | Version | Information needed by the stage | Status | Permission/scope | Freshness check | Permitted wording or relevant excerpt |
|---|---|---|---|---|---|---|

## Run inputs and prior approved outputs
| Input/output | Version or date | Source | Stage relevance |
|---|---|---|---|

## Provisional notes
| Note | Source | Why provisional | Not-for-claims reminder |
|---|---|---|---|

## Gaps and conflicts
| Missing/disputed item | Sources involved | Owner | Blocking? | What is needed |
|---|---|---|---|---|

## Verdict
- Result: READY / LIMITED / BLOCKED
- Reason:
- Permitted next action:
- Material limitations:
```

Include only records and excerpts needed by the receiving stage. For BLOCKED, identify the blocker and say the downstream stage must not proceed. For LIMITED, state what may proceed and the specific limitation. Keep internal traceability inside the saved package.

## Boundaries

- The context package is not a new approval record. Only an authorized human can approve a knowledge record or deliverable.
- Do not write proposed fixes into the knowledge layer. Report them for the responsible owner.
- Do not treat public availability as reuse permission for a client name, logo, result, or asset.
- Do not silently reconcile conflicting sources or turn provisional notes into facts.
- Do not calculate or infer a KRS from incomplete metadata. If a readiness score is supplied, report its source and version without changing it.
- Do not expose restricted personal information or evaluation answers in a context package.

## Run artifact storage
All context packages belong in the project’s `context package/` folder, one per workflow stage. Use the descriptive stage name in the filename; do not use internal stage codes. Do not save context packages in `output/`.
