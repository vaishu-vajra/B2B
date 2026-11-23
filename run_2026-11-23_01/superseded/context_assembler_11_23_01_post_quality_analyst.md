# Run Context Package

## Run header
- Client: Vajra Global
- Project: LinkedIn content pilot
- Channel: LinkedIn company page
- Period: 23 November–10 December 2026
- Run ID: Not provided
- Stage: Post Quality Analyst
- Assembled on: 23 November 2026, Asia/Kolkata

## Stage contract
- Required inputs: Current period brief; approved voice and writing rules; audience definition; quality rubric; full Content Planner calendar and item briefs; full Post Writer draft batch matched to calendar items; context package verdict.
- Helpful inputs: Relevant supplied claims and the API-selected historical post and feedback excerpts.
- Freshness rules: Historical captions are overlap references and do not become stale based on run date. Feedback is optional context and its status does not determine readiness. Text-only review; creative assets are not required.

## Selected evidence
| Source/record and version | Evidence IDs and relevant fact | Status and permission/scope | Freshness result | Permitted wording/excerpt |
|---|---|---|---|---|
| `context/period_brief.md`, VG-LI-2026-11-P1 | Six text-only LinkedIn posts; 23 Nov–10 Dec 2026; audience includes B2B marketing, business, technology, revenue and operations leaders; primary KPI is organic impressions; target ≈5,700; baseline 63 posts from Apr–Oct 2026, mean 489.3 and median 381. | Confirmed working brief; supplied claims are final for this pilot. | Current period brief. | Use supplied brief claims and item-specific directions as provided; route accuracy or disclosure concerns to human final-copy approval. |
| `knowledge layer/brand.md`, v0.5 | Voice: strategic, insightful, practical, confident without boastfulness, human, accessible. Short paragraphs, useful hooks, selective emojis and relevant hashtags; avoid jargon, exaggerated claims and generic AI phrases. Audience personas include marketing, business, technology, revenue and operations leaders. Pilot hashtag bank: #AIMarketing, #MarketingOperations, #WorkflowDesign. | Approved for internal pilot context; supplied claims final for this pilot. | Last updated 18 Nov 2026; usable for this review. | Apply supplied voice, writing guidance, audience descriptions and approved hashtag bank. |
| `knowledge layer/operations.md`, v0.4 | Text body target 60–150 words excluding hashtags; one central idea and primary CTA; short paragraphs; up to three relevant tags from the approved bank; 3,000-character maximum. | Approved for internal pilot context. | Last updated 18 Nov 2026; usable for this review. | Apply these supplied text-post standards. |
| `knowledge layer/learning.md`, v0.7 | K8.3 rubric: 1–5 for brand voice, clarity, accuracy and CTA; anchors: 1 poor, 3 acceptable, 5 excellent. Strategic relevance, audience relevance, originality, visual quality and evidence quality have no supplied anchors. | Approved for internal pilot reference. | Updated 19 Nov 2026; usable for this review. | Score anchored dimensions; mark unanchored dimensions Not assessed. Visual quality is outside text-only scope. |
| `knowledge layer/claims.md`, v0.3 | Supplied-claim rule: no separate claim evidence or approval required; preserve supplied claims and route potential accuracy, contradiction, disclosure or permission concerns to final-copy approval. | Approved for internal pilot context. | Updated 18 Nov 2026; applicable to this pilot. | Preserve supplied claim wording; do not expand it. |
| `knowledge layer/learning.md`, v0.7 | Historical performance baseline: 63 organic posts published Apr–Oct 2026; mean 489.3 and median 381 impressions. | Approved internal reference. | Historical reporting period retained; age does not lower readiness. | Metrics are context only; do not infer topic performance without reliable matching. |

## Run inputs and prior approved outputs
| Run input or prior output | Exact file/version | Sections or fields supplied | Relevance/status |
|---|---|---|---|
| Brief Qualification | `D:\SOCIAL CONTENT DELIVERY\run_2026-11-23_01\output\brief_qualifier_11_23_01.md` | Full supplied result | READY; identifies active window and notes that this calendar version has no approval supplied. |
| Content Planner | `D:\SOCIAL CONTENT DELIVERY\run_2026-11-23_01\output\content_planner_11_23_01.md` | Full calendar and item briefs | Six items and corresponding briefs supplied. Calendar approval is Pending. Item 1 draft and final-copy approval deadlines (18 and 21 Nov) precede the 23 Nov run date. |
| Calendar approval | `context\calendar_approval_2026-11-20.md` | Approval for the 20 Nov calendar version | Applies only to the earlier version and its dates/topics; does not approve the current 23 Nov calendar version. |
| Post Writer draft batch | Required mapped output for this run | Not supplied | Missing. No exact drafts or writer checks are available to review. |
| Historical post excerpts | API-selected excerpts from `knowledge layer/learning_posts.csv` | Not supplied in run evidence | Missing for overlap comparison; overlap coverage cannot be established. |
| Feedback excerpts | API-selected excerpts from `knowledge layer/learning_feedback.csv` | Not supplied in run evidence | Optional; absence does not affect readiness. |
| Knowledge index | `knowledge layer/knowledge_index.md`, v0.8 | Full supplied index | Identifies relevant approved internal records and versions. |
| Competitor observations | Attached verified public observations | No observations supplied | No competitor research is required for this QA stage. |

## Material provisional notes
| Note | Source | Why provisional | Effect on this stage |
|---|---|---|---|
| Calendar approval for the current six-item version is Pending; the 20 Nov approval covers an earlier exact version. | Current Content Planner output; `context\calendar_approval_2026-11-20.md` | Approval scope does not extend to the current version. | Carry as approval context; do not treat the earlier approval as applying to this calendar. |
| Item 1’s draft and planned final-copy approval deadlines have passed as of 23 Nov 2026. | Current Content Planner output | The stated dates are 18 Nov and 21 Nov. | Material scheduling finding for human handling; does not replace independent copy QA. |
| Historical caption overlap comparison cannot be performed from supplied excerpts. | Run evidence inventory | Selected CSV excerpts were not supplied. | Coverage limitation, but not independently a blocker under the QA contract. |

## Gaps and conflicts
| Missing/disputed item | Sources involved | Owner | Blocking? | What is needed |
|---|---|---|---|---|
| Full Post Writer draft batch with exact copy and relevant checks, matched to all six calendar items | Current Content Planner output is supplied; required Post Writer output is explicitly missing | Owner not specified | Yes | Supply the complete current-run Post Writer batch. The analyst must not proceed without the submission to review. |
| Explicit approval of the exact current calendar version | Current Content Planner says Pending; 20 Nov approval applies to an earlier version | X or Y per operations pilot assignments | No for assembling QA context; approval must remain accurately identified | Record approval for the current complete version if it is obtained. Do not infer approval from the earlier version. |
| Selected historical caption excerpts | Required stage map calls for API-selected excerpts; none included in supplied evidence | Owner not specified | No, if copy review is otherwise possible | Supply excerpts for overlap comparison or report that comparison as unavailable. |

## Verdict
- Result: BLOCKED
- Reason: The required full Post Writer draft batch is absent, so there is no submitted copy to match to the six calendar items or assess.
- Permitted next action: Supply the complete current-run draft batch. Then assemble fresh QA-stage context before invoking Post Quality Analyst.
- Material limitations: Current calendar approval is Pending and the earlier approval applies only to the earlier exact version. Item 1’s draft and final-copy approval deadlines precede the run date. Historical caption excerpts were not supplied, limiting overlap review.
