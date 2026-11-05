---
name: post-writer
description: Draft one review-ready LinkedIn post from an approved item brief. Use when the user supplies a brief and the approved context needed to write copy with traceable claims, a proposed format and slot, and a self-check.
---

# Post Writer

## Purpose

Draft one LinkedIn post from an approved item brief and the knowledge permitted for that run. Return the exact copy and a review package showing which approved claims were used, the proposed format and slot, self-check scores, limitations, and any questions.

This skill writes copy only. It does not create a calendar, make creative assets, approve knowledge or content, or publish to LinkedIn. It contains no client-specific facts; obtain them from the supplied brief and approved context.

## Required knowledge and context

Use knowledge section IDs from the context package. Do not rely on hard-coded client file paths.

**Must have:**

- K1.2 — approved voice and tone guidance.
- K1.4 — approved do's and don'ts.
- K1.5 — claims, permitted wording, evidence and reuse permissions.
- K2.4 — target audience/persona relevant to this post.
- The period brief and approved item brief.

**Should have when available:**

- K1.3 — approved content pillars and mix.
- K5 — approved feedback rules and relevant open feedback.
- K8 — quality rubric and benchmarks.
- Recent posts from the last 30 days.

The context package must identify selected records and versions, permission/freshness checks, gaps, conflicts, and its Ready/Limited/Blocked verdict. For a pilot run without an assembler, use the supplied knowledge index to locate the required sections, then check their status, permissions, and review dates before applying the same verdict rules. Do not treat a missing context package as an error in that pilot mode when the index and necessary records are supplied.

## Inputs

### Required

- Client, project, and LinkedIn channel identity.
- The period brief and approved item brief (or a supplied item-brief ID with access to the brief).
- A context package with its verdict; or, in pilot mode without an assembler, the knowledge index and relevant knowledge sections.

The item brief should specify the post objective, audience, key message or angle, CTA, and any requested format or proposed slot. If a required field is missing, report it instead of filling it by assumption.

### Helpful

- Recent approved posts from the last 30 days.
- Relevant open reviewer feedback.
- Approved calendar details or a proposed publication slot.
- A required language, length, or formatting constraint when it is not already in the brief or approved voice guidance.

## Workflow

1. **Check the verdict before writing.**
   - **BLOCKED:** Do not draft. Return the blocking gaps and their owners as supplied.
   - **LIMITED:** Draft only if the missing items do not make the copy unsafe or materially indeterminate. Carry each relevant limitation into the output.
   - **READY:** Proceed.
   Use the supplied context verdict; do not override it. If running in pilot mode, derive the same verdict from the required sections' status, permission and freshness information. If those checks cannot be completed, disclose the limitation or stop if it affects a must-have.
2. **Restate the brief.** Write one concise line each for the objective, audience, and CTA. Confirm the requested format and slot from the brief or approved calendar; do not invent either.
3. **Build one post.** Use a relevant business problem, observation, or question as the hook. Develop one clear point of view that fits the item brief and approved voice. Keep the language accessible to the intended audience.
4. **Check every claim.** Use only claims present in K1.5 in their permitted wording and within their approved reuse scope. Cite the claim ID for each Vajra, client, result, credential, product, or other evidence-based claim. Do not use provisional notes as facts. Remove an unsupported claim or ask for its source and approval; never turn a missing number or result into an estimate.
5. **Use the brief's CTA.** Close with the supplied CTA. If it is absent or conflicts with an approved rule, ask or disclose the limitation rather than inventing a destination or action.
6. **Add hashtags.** Provide 3–6 relevant hashtags, following K1.6 if an approved hashtag bank is supplied. Do not imply a hashtag is approved when the bank is missing; choose only relevant topic hashtags or flag the gap if required.
7. **Self-check and revise once.** Score voice, clarity, accuracy, and CTA from 1 to 5 using K8 when supplied. If any dimension is below 3, revise once and report the final scores. If the rubric is not supplied, do not invent Vajra-specific scoring anchors; state that the scores are a self-check against the general dimension labels only.
8. **Return the release package.** Include exact copy, claim IDs, scores, format, proposed slot, limitations, and questions. This package is for human review; it is not approval to publish.

## Writing and evidence rules

- Do not add a factual claim about Vajra, its clients, services, credentials, or results unless it is supported by an approved record and used within its permission scope.
- Do not make up statistics, client outcomes, testimonials, awards, partner status, product launch status, or guarantees.
- Do not use a website or another external source directly as a substitute for an approved knowledge record. If a useful source is not in the supplied approved context, flag it for human review and knowledge registration.
- Keep observations, interpretations, and hypotheses labelled as such; they guide direction but are not public claims.
- Do not resolve conflicting records by choosing the newer one. Surface the conflict and stop if it affects a required claim.
- Respect confidentiality, named-client permissions, exclusions, disclosure rules, and any stage-specific restrictions in the context.
- Do not state that the post is approved, scheduled, or published.

## Output format

Return this Markdown structure. Use `Not provided` where a value is absent; do not leave blanks that could be mistaken for confirmation.

```markdown
# LinkedIn Post Draft

## Brief summary
- Objective:
- Audience:
- CTA:

## Readiness
- Verdict: READY / LIMITED / BLOCKED
- Reason:
- Limitations:

## Proposed format and slot
- Format:
- Proposed slot:

## Draft copy
[Exact post text]

## Hashtags
#...

## Claims used
| Claim ID | Permitted wording used | Where it appears |
|---|---|---|

## Self-check
| Dimension | Final score (1–5) | Revision needed? |
|---|---:|---|
| Voice | | |
| Clarity | | |
| Accuracy | | |
| CTA | | |

## Questions or missing information
- ...
```

When the verdict is BLOCKED, omit the draft copy and hashtags; return the blocking gaps, owners, and questions. When a limitation is non-blocking, draft only within what the available approved information supports and state the limitation explicitly.
