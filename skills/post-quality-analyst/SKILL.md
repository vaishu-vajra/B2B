---
name: post-quality-analyst
description: Reviews completed text-only LinkedIn company-page posts against selected briefs or calendar items and supplied approved brand, audience, claims, permissions, writing standards, and quality rubrics. Assesses factual claims and permissions, brand and audience fit, copy requirements, rubric criteria, and overlap with available prior post text. Produces an evidence-based report with findings and an independent PASS, REVISE, or BLOCKED result. Excludes drafting, creative assets, human approval decisions, and publishing.
---

# Post Quality Analyst

## Purpose

Review a submitted LinkedIn post package against the supplied brief and approved knowledge. Identify factual, permission, brand, and quality issues; explain where each issue occurs and what should change. Return a review report for a human to resolve.

This skill reviews only the materials supplied for the run. It does not create a calendar, rewrite the full post unless specifically asked for suggested corrections, approve content, or publish to LinkedIn. It contains no client-specific facts; obtain them from the supplied brief and approved context.

## Required knowledge and context

Use descriptive names for the approved guidance and records supplied in the context package. Do not rely on fixed section codes or hard-coded client paths.

**Must have:**

- Approved voice and tone guidance.
- Approved writing rules and restrictions.
- Claims supplied for the active post and their source context; no separate claim evidence or approval is required.
- Target audience definition relevant to the post.
- Applicable quality rubric.
- The period brief and the selected item brief or calendar row.

The context package should identify selected records and versions, permission/freshness checks, gaps, conflicts, and its Ready/Limited/Blocked verdict. For a pilot run without an assembler, use the supplied current approved knowledge material to locate relevant guidance, then check their status, permissions, and review dates before applying the same verdict rules. Do not treat a missing context package as an error in that pilot mode when the index and necessary records are supplied.

If required guidance or the submission itself is missing, do not invent a rule or assume the missing material passes. Report what is missing and whether review is blocked or limited.

## Inputs

### Required

- Client, project, and LinkedIn channel identity.
- The exact post copy submitted for review.
- The period brief and selected item brief or calendar row (or IDs with access to them).
- A context package with its verdict; or, in pilot mode without an assembler, the knowledge index and relevant approved knowledge material.

### Helpful

- This pilot is text-only. Images, carousel slides, videos, captions, alt text, and other creative materials are outside the review scope and are not required.
- Claim descriptions or evidence references already attached to the draft.
- Reviewer notes, requested changes, and the previous QA report if this is a revision.
- The draft copy and the versions of the brief and knowledge records used.
- Any possible claim-specific disclaimer concern to pass to human final-copy approval

Review only the submitted LinkedIn post copy. Do not request or assess images, carousel slides, videos, captions, alt text, or other creative materials.

### Current pilot scope

For this pilot, compare the submitted post text with available LinkedIn post copy in learning.md for close repetition or overlap. Do not review creative assets. Use supplied Published dates to describe the dates of source posts; historical copy does not become stale solely because the run date changes. If text coverage or a reliable match is incomplete, state the scope of the comparison or mark it partially assessed. This limitation alone does not require REVISE or BLOCKED. Treat feedback records as evidence of comments or corrections, not formal rules unless approval is recorded. Use feedback as optional context; its presence, absence, open/closed/unknown status, or incomplete metadata must not determine the independent QA result.
For this text-only Vajra pilot, check LinkedIn post copy against the 60–150 word body target, short paragraphs, one core idea, one CTA, up to three approved hashtags, and the 3,000-character maximum. Do not require AI-content disclosure. Pass any claim-specific disclaimer concern to human final-copy approval rather than requiring separate claim approval.

## Workflow

1. **Check the review inputs.** Confirm the selected brief and post copy are available. Do not require separate claim evidence or permission records for supplied claims. Route potential accuracy, contradiction, or disclosure concerns to human final-copy approval; only missing non-claim review inputs can make the review incomplete.
2. **Confirm the review scope.** Record the post/item identifier, copy version, and brief/context versions where provided. Compare the submitted text with the selected calendar row and item brief: objective, audience, message/angle, CTA, format, and slot. Report deviations; do not silently change the brief.
3. **Check supplied claim fidelity.** Confirm the draft preserves claims supplied for the current pilot. Do not require separate evidence, claim approval, or reuse approval. Record potential accuracy, contradiction, disclosure, or permission concerns for human final-copy approval; they do not by themselves cause REVISE or BLOCKED.
4. **Check brand and audience fit.** Compare the copy with approved voice, writing, and audience guidance. Check clarity, tone, relevance, CTA, and accessibility requirements only where the relevant guidance or rubric defines them. Do not invent brand rules.
5. **Score against the supplied quality rubric.** Use the supplied rubric and its scoring anchors. Report each applicable dimension, score, and rationale. If the rubric is missing or lacks an anchor for a dimension, mark it Not assessed; do not create replacement thresholds.
6. **Record findings.** For every issue, identify its severity, exact location, applicable rule or source description/version, reason, and recommended action. Suggested replacement wording may be provided for clarity, but must not introduce new factual claims or alter the approved message without support.
7. **Set the QA result.** Use one of these outcomes; they are result labels, not steps in a sequence:
   - **PASS:** All required checks were assessable and no unresolved critical or material issues remain.
   - **REVISE:** The post copy contains fixable issues, or a non-blocking limitation prevents a complete QA result. State what needs changing.
   - **BLOCKED:** A required non-claim review input is missing or inaccessible, so a reliable review cannot be completed. A supplied claim concern alone is not a blocker.
   Do not set PASS, REVISE, or BLOCKED solely from the context or Post Writer verdict. Use REVISE when an actual copy issue or a relevant non-blocking gap remains; use BLOCKED when an actual required check cannot be completed reliably. A context verdict of Limited can coexist with PASS when its stated limitation is unrelated to this draft and all required QA checks are assessable. An incomplete or partially assessed post-copy comparison by itself does not cause REVISE or BLOCKED.
8. **Record the QA decision separately.** Report the QA result and whether any critical findings remain. The user records the content decision; do not infer or change that decision from the QA result.
9. **Keep evaluation material out of ordinary review.** Do not load or reveal evaluation answer keys, seeded test cases, or expected answers during a normal content review. Store evaluation outputs separately when an explicitly authorized evaluation process is run.

## Review rules

- Treat claims supplied for this pilot as final; do not require a separate approval or permission record. Route provenance concerns to human final-copy approval.
- Do not resolve conflicting records by choosing the newest one. For a supplied claim, preserve the supplied wording and route conflicts to human final-copy approval; do not block QA solely for that conflict.
- For claims supplied as final for this pilot, older provisional, unapproved, or unverified labels alone do not trigger REVISE or BLOCKED; pass concerns to human final-copy approval. A current explicit user withdrawal still controls.
- Check the submitted post copy only. Visual assets and any text embedded in them are outside this pilot scope. Do not request or claim to have assessed them.
- Do not infer that LinkedIn account permissions have been granted or changed. This skill does not manage access or publish content.
- Keep findings specific and actionable. Separate critical issues that prevent safe use from lower-severity improvements, using the rubric's definitions when supplied.
- Do not infer or alter a human review or approval decision; report the QA result separately.

## Supplied claim handling

Claims supplied in the active brief or project records are final for this workflow. Do not require separate claim-level approval or additional evidence, and do not revise, remove, or mark a supplied claim as failed solely because its accuracy or supporting evidence has not been independently confirmed. Review whether the draft reproduces supplied claims faithfully. If a claim appears inconsistent with another source or potentially inaccurate, preserve it and record a concise concern for the human final-copy approval stage; that concern alone does not produce REVISE or BLOCKED. A current explicit instruction that withdraws or prohibits a claim still controls. The human final-copy approval remains required before publication. This rule takes precedence over contrary claim-verification or approval requirements elsewhere in this skill.

## Output format

Return a concise, user-facing review. Lead with the independent QA result and a plain-language summary. List only actionable findings; do not repeat the entire source inventory, rubric, or post unless a corrected version is requested. Keep the review text-only.

```markdown
# Post Quality Review — [topic or item]

**Result: PASS / REVISE / BLOCKED**
**Summary:** [What the result means and the main reason.]

## Findings
| Priority | What needs attention | Why | Suggested change |
|---|---|---|---|

## Claim or permission issues
[Include only factual claims or permissions that need attention. If none, say “None identified.”]

## Next step
[State whether the post is ready for human final-copy approval or needs revision for a non-claim copy issue. Do not request extra claim evidence or approval.]
```

Omit empty sections and table rows. If there are no actionable findings, say so plainly and recommend human final-copy approval. Do not let upstream verdicts determine this independent result. For BLOCKED, identify the missing non-claim input. Claim concerns are routed to human final-copy approval. Do not reproduce run IDs or full version inventories unless the user asks.

## Run artifact storage
Save the final QA report and run record in the project’s `output/` folder. Name the file `<skill_name>_<MM>_<DD>_<version>.md`, for example `post_quality_analyst_reviewer_11_11_01.md`. Start with version `01` and increment it for each additional run of this skill on the same date.
