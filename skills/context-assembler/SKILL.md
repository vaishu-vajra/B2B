---
name: context-assembler
description: Assembles social-content workflow context in one run, saving a separate package for Brief Qualifier, Content Planner, Post Writer, Post Quality Analyst, and Competitor Scan. Each package contains the relevant source material, its readiness at assembly, and the upstream outputs or approvals needed at execution. Also supports explicitly requested standalone stages.
---

# Context Assembler

## Purpose

Prepare a run-specific context package for each receiving skill. Check permission before retrieving or selecting records, include the current and permitted information the recipient needs, and report the gaps, conflicts, provisional notes, and readiness for that stage.

This skill assembles context; it does not write or review content, calculate the Knowledge Readiness Score (KRS), approve records, resolve conflicts, modify knowledge files, publish, or change access rights. It contains no client-specific facts. Use the supplied knowledge layer, stage contract, and run inputs.

## Workflow execution

For the five-skill workflow, run Context Assembler once at the start. Read the shared run inputs and the union of the five stages' mapped sources once. Apply the stage contracts independently and save exactly five separate Markdown context packages for the same run ID, one for each recipient. Include the source content each stage needs and its provenance. Share only the sources and excerpts relevant to each recipient. If the request explicitly selects one standalone stage, assemble one package for that stage.

| Receiving skill | Include at assembly | Attach or check when the skill runs |
|---|---|---|
| Brief Qualifier | Active period brief, objective, audience, KPI definition, target, baseline, dates, and relevant project rules. | Confirm the publishing start date is valid for the run. |
| Content Planner | Planning window, post count, scope, pillars, constraints, and relevant performance context. Include calculated slots when supplied. | Attach the same-run Brief Qualifier result. Require a READY or LIMITED qualification and a valid planning window. |
| Post Writer | Text-post standards, brand voice, supplied claims and selected historical writing and feedback excerpts. | Attach the qualified brief, current calendar with every item brief, and explicit human approval of that exact full calendar version. Draft only when the entire current calendar is approved and its item briefs are complete. |
| Post Quality Analyst | Text-review standards, rubric, brand voice, supplied claims and relevant historical feedback. | Attach the same-run qualified brief, current approved calendar and item briefs, and the complete matching draft batch. Retrieve the permitted historical caption matches using the actual drafts at this point. Verify each draft maps to its calendar item before review. |
| Competitor Scan | Approved competitor set, relevant market and brand context, and research scope. Include an explicitly supplied prior scan only when relevant. | Run independently of the other four skills. Gather current public evidence within the research scope during the scan. |

For the five-skill workflow, the workflow caller or receiving skill attaches the named same-run outputs, records and permitted excerpts to its own package at execution and checks the remaining required inputs. Do not invoke Context Assembler again between those stages or to resume an incomplete stage with the same source inputs. Record missing upstream results or approvals as pending dependencies in the package. If required for execution, they make the stage BLOCKED at assembly. This verdict describes the inputs available at assembly. After the dependencies arrive, the caller or receiving skill checks and records execution readiness independently, preserving the saved package and any unresolved blockers. If shared inputs change materially, prepare a new workflow run with five fresh packages.

## Project stage input map
For this project, `api_pipeline/workflow_inputs.json` defines the whole knowledge files and prior stage outputs supplied for each receiving stage. For each package, select only the sources listed for its receiving stage. Prior outputs must be explicitly named for this run; never select a file by guessing which output is latest or substitute another run. Record required prior outputs that are absent and name the stage or approver that will supply them. A supplied prior output may contain only selected Markdown sections; omitted sections are not evidence that information is absent from its source. The stage map requires the compact `learning.md` core for every workflow stage. For each in-scope content stage, make every available reviewer comment accessible from the supplied feedback rows, learning.md register, or current run inputs. Preserve each comment and ID regardless of approval, age, status, or missing metadata. Count IDs repeated across sources once. Include the permitted writer caption and final-copy excerpts, and the available QA original and final excerpts. The caller attaches caption matches that require the actual drafts at QA execution. Content Planner may receive only dates and opening lines from posts published in the last 60 days. Use structured rows for feedback comments and selected excerpts for historical post copy. Preserve the approximately 3,000-token target for CSV-derived context by shortening supporting copy when needed, while keeping reviewer comments intact.

## Inputs 
   
### Required

- Receiving stage names (or one explicitly requested standalone stage), run ID, client/project identity, channel, and period where applicable.
- The approved stage contract and policy version. Use the stage requirements below when they are the active workflow contract. If the requested workflow stage or active contract is unclear, do not invent one; report the gap.
- The mapped source files or atomic record register, with source names and versions where available. Include the knowledge index for stages that require it. For Content Planner, use the mapped files' own metadata for status, scope, and freshness checks.
- Permission and reuse-scope information for the records and the requesting stage.
- The live inputs available at assembly, such as the active period brief. Record required earlier stage results, calendar approval, and other execution inputs that are still pending.
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
| Calendar and item briefs | Qualified period brief; approved content pillars; project scope (cadence, formats, languages, exclusions); publishing start date, end date and post count supplied in the brief/run inputs; confirmed event or blackout constraints when relevant | Subject-matter expert topics; relevant events in the planning month | When assembling for Content Planner, include the user-provided historical pillar distribution from the “Content pillars and historical mix” section of brand.md when relevant: 63 total posts; displayed pillar counts are AI and Innovation 14, Growth and GTM 7, Technology and Expertise 18, People and Culture 23. Treat these as historical posting-volume counts, not impression performance. The displayed counts sum to 62; identify one post as outside the displayed breakdown and do not infer its pillar. For the Vajra pilot, pass the publishing start date, end date and post count to Brief Qualifier and Content Planner. When supplied, pass the API-calculated proposed slots to Content Planner. Use the publishing start and end dates as the single active period for the brief and calendar. For Brief Qualifier and Content Planner, block a publishing range whose start date is before today in India time and request a new range. Flag other actual date conflicts. Production/review capacity and turnaround are not planning requirements and their absence must not lower readiness. Continue to respect confirmed deadlines, dependencies, blackout dates, and required human review/approval |
| Copy and claims | Approved brand positioning, voice, writing rules, selected historical LinkedIn post excerpts from `learning_posts.csv` as style/structure and overlap source, supplied final claims, and selected item brief | Audience-language examples and a separate writing sample are not required | Claims need no separate approval or evidence gate; route possible concerns to human final-copy approval |
| Assets | Approved brand guidelines; assets whose usage rights are recorded; current platform specifications | None specified | Platform specifications no older than 90 days |
| Quality review | Supplied final claims, approved brand voice and writing rules, quality rubric | Source evidence or permission notes when useful | Do not require separate claim-level approval or evidence; route concerns to human final-copy approval |
| Approval and publishing | Approval chain; verified LinkedIn page access and publishing rights; CTA destinations and tracking-link rules | None specified | Re-verify page rights and approval chain at release |
| Community management | Current response and escalation playbook with contacts; approved company facts | Audience objections | Response playbook must be current |
| Measurement | Definition and current reporting for the single KPI selected in the approved brief | Past performance reports, if needed for comparison | For the current Vajra pilot, measure LinkedIn organic impressions only; do not add secondary KPIs. Preserve the dataset's reporting period and source caveats. |
| Review and improvement | Current-cycle measurement report, when required by the stage contract | Current-cycle feedback or rework records, if supplied | Use supplied feedback as context where relevant. A feedback list or current open/closed status is not a readiness prerequisite; its presence, absence, status, or incomplete metadata alone does not lower the verdict. The compact historical feedback summary in `learning.md` and detailed rows in `learning_feedback.csv` remain records of their stated dates, and can be used immediately as editorial context. Formal rule changes still require the designated approver. |

For the current Vajra pilot, selected posts are text-only. Do not require or assemble images, carousel slides, video, alt text, or other creative assets for Post Writer, Post Quality Analyst, or Publish and Verify.

For each package, assemble only information required by its receiving stage and identify later inputs under the run inputs or gaps sections. For Post Writer, preserve explicit human approval of the current calendar version alongside every calendar row and item brief. Approval must cover every post on that version. Report missing, pending, partial, or outdated approval or missing item briefs as a blocker for the entire drafting batch. For batch QA, hand off the full draft batch and all corresponding calendar rows and briefs, with calendar approval as context. For publishing, hand off the selected item and its matching QA result. Include LinkedIn account access, publisher authorization, final-copy publication approval, actual publication status, or live-post verification only when assembling context specifically for Publish and Verify. For earlier stages, include only the human review or approval state that stage needs. Keep traceability concise: record each relevant source name/version once, include only evidence IDs and excerpts used by this stage, and state permission or freshness only when it affects the handoff. Do not repeat general policy reminders or source descriptions already defined in this skill.

If a stage contract supplied for the run differs from this table, follow the formally approved version and report the version used. Do not turn a “should have” item into a required item unless the active contract says so.

## Workflow

1. **Identify the run and recipients.** Confirm the run ID, workflow or standalone stage, client/project, channel, period, and policy or contract version. If an identifier is missing and affects record selection, request it.
2. **Read the stage contracts.** Determine what each recipient needs, what is helpful, and which freshness windows apply. Use the same source read for every package that needs that source.
3. **Check source access.** Confirm this workflow may access the selected file or record. Do not treat internal source access as claim approval. Supplied claims are final for this pilot; route any use or accuracy concern to human final-copy approval.
4. **Select the minimum relevant material.** Include approved knowledge records, user-supplied final claims, live inputs, and earlier approved stage outputs needed by the receiving stage. Keep source provenance for traceability without using old claim-status labels as gates.
5. **Check status and freshness.** Apply explicit expiry rules to current-state information. Historical data remain tied to their actual periods regardless of run date. Do not require separate approval or evidence for supplied claims; send accuracy or permission concerns to human final-copy approval. Feedback status and metadata do not determine readiness.
6. **Detect conflicts and provisional information.** Preserve source differences without choosing a newer record. Treat claims supplied for this pilot as final despite older provisional or unverified labels; route possible inaccuracies or permission concerns to human final-copy approval without lowering this stage verdict. Feedback presence, absence, status, or metadata is not a readiness gap.
7. **Assess gaps for each recipient.** Record each missing, stale, restricted, or conflicting item, affected sources, known owner, impact, and whether it blocks. For pending dependencies, identify what must be attached and who or which stage supplies it. Use “Owner not specified” if no owner is identified.
8. **Set the stage verdict.**
   - **READY:** Required stage inputs are available and usable; supplied claims do not need separate approval or evidence, and historical age or feedback status does not lower readiness.
   - **LIMITED:** Use only for a material non-claim limitation that prevents a full handoff. Supplied claim status or evidence concerns go to human final-copy approval and do not lower this verdict.
   - **BLOCKED:** A required input is missing, inaccessible, expired under an explicit rule, or materially conflicting. An older claim approval/evidence label alone does not cause BLOCKED.
   Assess the current run against this stage contract. A prior status based solely on historical-data age or feedback presence, absence, status, or metadata is not carried forward as a limitation. Preserve other still-applicable blockers and limitations. A stage-level verdict is not the KRS and does not approve the knowledge layer.
9. **Build and verify the context packages.** Use the format below separately for each recipient and preserve source names and versions. For the five-skill workflow, verify all five stage names and the shared run ID before finishing.

## Supplied claim handling

Claims supplied in the active brief or project records are final for this workflow. Include them for the receiving stage without requiring separate claim-level approval or additional evidence. Do not block or limit the context package solely because a supplied claim lacks a separate approval marker, proof-point entry, or evidence attachment. If supplied sources conflict about a claim or it appears potentially inaccurate, preserve the supplied wording and flag the concern for the human final-copy approval stage; the concern alone does not lower this stage verdict. A current explicit instruction that withdraws or prohibits a claim still controls. This rule takes precedence over contrary claim-status requirements elsewhere in this skill.

## Context package output

For the five-skill workflow, save all five complete context packages in the run's designated context-package folder. For a standalone stage, save its one complete package in the same way. Keep internal source tables, reuse permissions, and the full packages in the saved files. After saving, list the files and give the READY, LIMITED, or BLOCKED status at assembly for each stage, with the material reason and next permitted step. If file creation is unavailable, report that limitation and provide a concise status without representing it as a saved package.

Name each file `context_assembler_<MM>_<DD>_<version>_<stage_name>.md`, for example `context_assembler_11_11_01_post_quality_analyst.md`. Use a readable lowercase stage name with underscores, not a stage code. Start with version `01` for each stage name and increment it for additional runs of that stage on the same date. Use `Not provided`, `Not verified`, or `Not applicable` rather than ambiguous blanks.

The saved package must retain this structure for the downstream skill while keeping each section concise. Omit empty sections and table rows. Do not repeat generic rules from this skill in the package. Use a permission note only when a source's actual reuse scope affects the receiving stage; keep source names, versions, evidence IDs and permitted wording where they are needed for traceability.

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

## Selected evidence
| Source/record and version | Evidence IDs and relevant fact | Status and permission/scope | Freshness result | Permitted wording/excerpt |
|---|---|---|---|---|

## Run inputs and prior approved outputs
| Run input or prior output | Exact file/version | Sections or fields supplied | Relevance/status |
|---|---|---|---|

## Material provisional notes
| Note | Source | Why provisional | Effect on this stage |
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

Include only records and excerpts needed by the receiving stage. For BLOCKED, identify what the receiving stage must obtain or resolve before proceeding. For LIMITED, state what may proceed and the specific limitation. Keep internal traceability inside the saved package.

## Boundaries

- The context package is not a new approval record. Only an authorized human can approve a knowledge record or deliverable.
- Do not write proposed fixes into the knowledge layer. Report them for the responsible owner.
- Do not treat public availability as reuse permission for a client name, logo, result, or asset.
- Do not silently reconcile conflicting sources or turn provisional notes into facts.
- Do not calculate or infer a KRS from incomplete metadata. If a readiness score is supplied, report its source and version without changing it.
- Do not expose restricted personal information or evaluation answers in a context package.

## Run artifact storage
Use the run's designated context-package folder when supplied. Otherwise save in the project-root `context package/` folder. Use the descriptive stage name in the filename. Keep context packages separate from skill results in `output/`.

