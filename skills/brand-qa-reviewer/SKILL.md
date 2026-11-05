---
name: brand-qa-reviewer
description: Review a supplied LinkedIn post and its creative materials against approved company facts, permissions, brand guidance, and the quality rubric. Use when the user wants a review and issue report, not drafting, approval, or publishing.
---

# Brand QA Reviewer

## Purpose

Review a submitted LinkedIn post package against the supplied brief and approved knowledge. Identify factual, permission, brand, and quality issues; explain where each issue occurs and what should change. Return a review report for a human to resolve.

This skill reviews only the materials supplied for the run. It does not create a calendar, rewrite the full post unless specifically asked for suggested corrections, approve content, or publish to LinkedIn. It contains no client-specific facts; obtain them from the supplied brief and approved context.

## Required knowledge and context

Use knowledge section IDs from the context package. Do not rely on hard-coded client file paths.

**Must have:**

- K1.2 — approved voice and tone guidance.
- K1.4 — approved do's and don'ts.
- K1.5 — claims, permitted wording, evidence, and reuse permissions.
- K2.4 — target audience/persona relevant to the post.
- K8.3 — applicable quality rubric.
- The period brief and the selected item brief or calendar row.

The context package should identify selected records and versions, permission/freshness checks, gaps, conflicts, and its Ready/Limited/Blocked verdict. For a pilot run without an assembler, use the supplied knowledge index to locate the relevant sections, then check their status, permissions, and review dates before applying the same verdict rules. Do not treat a missing context package as an error in that pilot mode when the index and necessary records are supplied.

If required guidance or the submission itself is missing, do not invent a rule or assume the missing material passes. Report what is missing and whether review is blocked or limited.

## Inputs

### Required

- Client, project, and LinkedIn channel identity.
- The exact post copy submitted for review.
- The period brief and selected item brief or calendar row (or IDs with access to them).
- A context package with its verdict; or, in pilot mode without an assembler, the knowledge index and relevant knowledge sections.

### Helpful

- Attached creative materials, including image text, carousel slides, video captions, and alt text, if they are part of the submitted post.
- Claim IDs or evidence references already attached to the draft.
- Reviewer notes, requested changes, and the previous QA report if this is a revision.
- Release package/version IDs and the versions of the brief and knowledge records used.
- Applicable disclosure policy and any extra channel-specific requirements.

Review every supplied public-facing element. If a creative element is expected but not supplied, identify that scope gap; do not claim to have reviewed it.

## Workflow

1. **Check the verdict before reviewing.**
   - **BLOCKED:** Do not perform a pass/fail content review. Return the blocking gaps and their owners as supplied.
   - **LIMITED:** Review only the parts that can be assessed safely; make the limits explicit and do not give an overall pass if a material area cannot be checked.
   - **READY:** Continue with the supplied approved context.
   Use the supplied verdict; do not override it. In pilot mode, derive the verdict from the required sections' status, permission, and freshness information. If those checks cannot be completed, disclose the limitation or stop if it affects a required check.
2. **Confirm the review scope.** Record the post/item identifier, copy version, included creative assets, and brief/context versions where provided. Compare the submitted content with the selected calendar row and item brief: objective, audience, message/angle, CTA, format, and slot. Report deviations; do not silently change the brief.
3. **Check factual claims and permissions.** Identify each factual claim about the company, its services, clients, results, people, credentials, awards, partners, products, or guarantees. Match it to an approved K1.5 record and permitted wording, evidence, reuse permission, and disclosure requirements. Flag claims that are missing, overstated, outdated, outside permission scope, or in conflict. Do not treat a public website page as approval to reuse its claims unless the supplied approved record permits that use.
4. **Check brand and audience fit.** Compare the copy and supplied creative text with K1.2, K1.4, K2.4, and any applicable approved visual guidance. Check clarity, tone, relevance, CTA, and accessibility requirements only where the relevant guidance or rubric defines them. Do not invent brand rules.
5. **Score against K8.3.** Use the supplied rubric and its scoring anchors. Report each applicable dimension, score, and rationale. If the rubric is missing or lacks an anchor for a dimension, mark it Not assessed; do not create replacement thresholds.
6. **Record findings.** For every issue, identify its severity, exact location, applicable rule or knowledge record ID/version, reason, and recommended action. Suggested replacement wording may be provided for clarity, but must not introduce new factual claims or alter the approved message without support.
7. **Set the QA result.** Return **PASS** only when no unresolved critical or material issues remain and all required checks were assessable. Return **REVISE** when the draft or assets contain fixable issues. Return **BLOCKED** when a required source, permission, brief, or context check is missing or conflicting such that a reliable review cannot be completed. A Limited context verdict cannot receive PASS for the overall result.
8. **Check release readiness separately.** Record whether any critical findings remain and whether the release package's referenced versions match the reviewed versions. Mark version matching Not verified if IDs/versions are missing. Human approval is still required; a QA result is not approval to publish.
9. **Keep evaluation material out of ordinary review.** Do not load or reveal K9/K10 evaluation answer keys, seeded test cases, or expected answers during a normal content review. Store evaluation outputs separately when an explicitly authorized evaluation process is run.

## Review rules

- Judge claims only against the approved records and permissions supplied for this run. Do not infer permission from a public URL, a logo appearing online, or the mere existence of a case study.
- Do not resolve conflicting records by choosing the newest one. Surface the conflict and block the affected check if needed.
- Treat provisional, unapproved, expired, or restricted records according to their stated status and scope; never present them as approved facts.
- Check all supplied public-facing text, including text embedded in images and slides. Do not claim to have assessed visuals that were not supplied or are unreadable.
- Do not infer that LinkedIn account permissions have been granted or changed. This skill does not manage access or publish content.
- Keep findings specific and actionable. Separate critical issues that prevent safe use from lower-severity improvements, using the rubric's definitions when supplied.
- Do not mark a draft approved, scheduled, or published.

## Output format

Return this Markdown structure. Use `Not provided`, `Not assessed`, or `Not verified` where appropriate; do not leave blanks that could be mistaken for confirmation.

```markdown
# LinkedIn Brand and Content QA Review

## Item reviewed
- Client/project/channel:
- Calendar item or brief ID:
- Copy/version reviewed:
- Creative materials reviewed:
- Brief/context/knowledge versions:

## QA result
- Result: PASS / REVISE / BLOCKED
- Context verdict: READY / LIMITED / BLOCKED
- Summary:

## Findings
| Severity | Location | Rule or knowledge record (ID/version) | Issue and reason | Recommended action |
|---|---|---|---|---|

## Claim and permission check
| Claim or asset | Approved source and permission | Result | Notes |
|---|---|---|---|

## Quality scores
| Rubric dimension | Score | Rationale |
|---|---:|---|

## Suggested corrections
- ...

## Release-readiness check
- Open critical findings:
- Reviewed versions match release package: Yes / No / Not verified
- Human approval required: Yes

## Questions or limitations
- ...
```

If the verdict is BLOCKED, return the blockers, supplied owners, and questions; do not report unsupported pass/fail judgments for unchecked content. If the verdict is LIMITED, clearly identify which sections were reviewed and which could not be assessed.
