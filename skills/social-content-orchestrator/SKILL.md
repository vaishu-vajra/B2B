---
name: social-content-orchestrator
description: Coordinates Vajra Global's four-stage LinkedIn workflow from brief qualification through post quality review. Starts Context Assembler once for the four stage packages and pauses for one full-calendar approval before drafting.
---

# Social Content Orchestrator

Use the project-local skill instructions and the required prior outputs from the API workflow input map. Keep one workflow run ID and use the run's designated context-package and output folders. Save only the actual outputs of each skill.

## Run order

1. Run Context Assembler once with an explicit contract for this four-stage workflow. Request only the packages for Brief Qualifier, Content Planner, Post Writer, and Post Quality Analyst. Verify that each package is a separate Markdown file for the same run. Keep each original package as the record of what was available at assembly.
2. Run Brief Qualifier with its own package and save its report. Continue to planning only after a READY or LIMITED verdict.
3. Run Content Planner with its own package and the saved same-run Brief Qualifier result. Save the complete calendar and its item briefs. Pause for one explicit human approval covering that exact full calendar version.
4. Run Post Writer with its own package, the qualified brief, the approved calendar and all item briefs, and the recorded whole-calendar approval. Save the complete draft batch.
5. Run Post Quality Analyst with its own package, the qualified brief, the approved calendar and item briefs, and the complete matching draft batch. Attach permitted historical caption matches selected using the actual drafts. Save the QA report for every item.

## Handoffs and resuming

Before running a stage, verify its required upstream outputs and approval apply to the same run and versions. Review the assembly-time gaps against the inputs now available. A package marked BLOCKED solely because a required previous output had yet to be generated can be used once that dependency and every other required input is satisfied. Keep the original package and add later inputs to the receiving skill's handoff. Pause on any unresolved blocker and name the required input or decision.

On resume, start with the first incomplete stage and reuse the saved packages and valid completed outputs for this run. Do not rerun Context Assembler between stages. If shared inputs materially change, start a new workflow run and obtain any approvals required for the new versions.
