# Run Context Package

## Run header
- Client: Vajra Global
- Project: LinkedIn content pilot
- Channel: LinkedIn company page
- Period: 23 November–10 December 2026
- Run ID: `run_2026-11-23_01`
- Stage: Post Writer
- Assembled on: 23 November 2026, Asia/Kolkata

## Stage contract
- Required inputs: Active period brief; approved voice and writing rules; supplied final claims and relevant audience; applicable rubric; explicit human approval of the entire current calendar version; all calendar rows and complete item briefs; a context package.
- Helpful inputs: Approved content pillars and hashtag guidance; selected historical LinkedIn caption and feedback excerpts; relevant feedback and proposed slots.
- Freshness rules: Historical captions use their supplied publication dates and do not expire solely due to age. Claims supplied for this pilot need no separate evidence or approval; concerns go to human final-copy approval.

## Selected evidence
| Source/record and version | Evidence IDs and relevant fact | Status and permission/scope | Freshness result | Permitted wording/excerpt |
|---|---|---|---|---|
| `knowledge layer/brand.md` v0.5 | Voice, writing rules, audience, pillars, approved pilot hashtag bank | Approved for internal pilot use per 2026-11-10 user instruction; approver name/role not supplied | Current for the supplied pilot context | Strategic, insightful, practical, confident and human; concise paragraphs, useful hooks, accessible language, one relevant CTA. Use up to three relevant tags from `#AIMarketing`, `#MarketingOperations`, `#WorkflowDesign`. |
| `knowledge layer/operations.md` v0.4 | LinkedIn text-post standards and pilot roles | Approved for internal pilot use per 2026-11-10 user instruction | Current for supplied pilot context | Body target 60–150 words excluding hashtags; short paragraphs; one central idea and CTA; maximum 3,000 characters including hashtags. |
| `knowledge layer/learning.md` v0.7 | K8.3 rubric: brand voice, clarity, accuracy, CTA; 1–5 scale | Approved for internal pilot reference | Current rubric supplied; pilot instructions say skip pass target | Score each supplied dimension on the 1–5 scale; no pass/fail judgment. |
| `knowledge layer/claims.md` v0.3; active brief | Supplied claims are final for this pilot; no separate claim evidence or approval required | Supplied claims may be used as written; route accuracy, contradiction, disclosure or permission concerns to final-copy approval | Applies to this pilot | Do not expand claims beyond supplied scope. |
| Active brief `context/period_brief.md`, VG-LI-2026-11-P1 | Primary KPI is LinkedIn organic impressions; target approximately 5,700 across six posts; baseline 63 posts published April–October 2026, mean 489.3 and median 381 | Confirmed working brief per user instruction | Current period: 23 November–10 December 2026 | Text-only pilot; English; audiences include marketing, business, technology, revenue and operations leaders. Exclude the practical-experience statement. |
| `knowledge layer/knowledge_index.md` v0.8 | Mapped knowledge status and internal-use approval | Approved for internal pilot context per 2026-11-10 user instruction | Last updated 2026-11-23 | Use only stage-relevant records listed above. |

## Run inputs and prior approved outputs
| Run input or prior output | Exact file/version | Sections or fields supplied | Relevance/status |
|---|---|---|---|
| Period brief | `context/period_brief.md`, VG-LI-2026-11-P1 | Full brief, objectives, audience, claims policy, period, six-post count, KPI | Active brief; publishing range starts on run date. |
| Brief Qualifier | `output/brief_qualifier_11_23_01.md` | Qualification verdict and handoff | READY; identifies the active period and notes that the earlier calendar approval does not cover a specific current calendar. |
| Content Planner | `output/content_planner_11_23_01.md` | Full six-row calendar and item briefs | Calendar approval marked Pending. Briefs supplied for all six rows. |
| Earlier calendar approval | `context/calendar_approval_2026-11-20.md` | Approval for six-post calendar dated 20 November, publishing range 20 November–10 December | Applies only to that earlier exact version; does not approve the current 23 November–10 December calendar. |
| Historical copy and feedback excerpts | API-selected excerpts from `knowledge layer/learning_posts.csv` and `knowledge layer/learning_feedback.csv` | No excerpts supplied in this run’s evidence | Missing from handoff; selected-copy overlap comparison cannot be performed. This alone does not block drafting readiness under the Post Writer contract. |

## Material provisional notes
| Note | Source | Why provisional | Effect on this stage |
|---|---|---|---|
| Current calendar approval is pending. | `output/content_planner_11_23_01.md` | No explicit human approval supplied for this exact calendar version and all its rows. The 20 November approval covers a different calendar version. | Blocks the full drafting batch. |
| Item 1 timing is already partly past. | Current calendar in `output/content_planner_11_23_01.md`; run date 23 November 2026, Asia/Kolkata | Item 1 draft due 18 November and planned final-copy approval due 21 November; publication is 23 November. | Calendar scheduling issue to resolve before drafting this version. |
| Historical caption excerpts are absent. | Stage-mapped CSV excerpts not supplied | No API-selected caption excerpts were included in the supplied run evidence. | Overlap check unavailable; not independently a drafting blocker. |

## Gaps and conflicts
| Missing/disputed item | Sources involved | Owner | Blocking? | What is needed |
|---|---|---|---|---|
| Explicit approval of the entire current six-post calendar version and every row/item brief | Current planner output marks approval Pending; 2026-11-20 approval is for the earlier exact calendar | Approver: X, with Y as backup, per `knowledge layer/operations.md`; named identities not supplied | Yes | Explicit human approval covering the current exact calendar version and all six rows and briefs. |
| Item 1 schedule has elapsed draft and final-copy approval deadlines | Current calendar; run date 23 November 2026, Asia/Kolkata | Calendar owner: Pranathy, as recorded in `knowledge layer/operations.md` | Yes for proceeding with this calendar as supplied | Replan or otherwise resolve the dates, then obtain approval for the resulting exact calendar version. Item 1 draft due 18 November and approval due 21 November precede the run date; publication is set for 23 November. |
| Selected historical copy and feedback excerpts not provided | Required stage-map excerpts from `learning_posts.csv` and `learning_feedback.csv` | Owner not specified | No | Provide excerpts if available for style, overlap and relevant feedback context. |

## Verdict
- Result: BLOCKED
- Reason: The current calendar version lacks explicit approval covering the whole calendar and every item brief. The earlier approval applies only to the earlier exact version. Item 1’s draft and planned final-copy approval deadlines also precede the run date.
- Permitted next action: Do not invoke Post Writer. Resolve Item 1 timing, then obtain explicit approval of the resulting complete calendar version before running Context Assembler again for Post Writer.
- Material limitations: Historical caption and feedback excerpts were not supplied, so a text-overlap comparison is unavailable. This omission does not change the verdict.
