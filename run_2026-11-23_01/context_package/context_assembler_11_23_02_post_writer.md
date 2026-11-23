# Run Context Package

## Run header
- Client: Vajra Global
- Project: LinkedIn Marketing
- Channel: LinkedIn company page
- Period: 2026-11-23–2026-12-10
- Run ID: `run_2026-11-23_01`
- Stage: Post Writer
- Assembled on: 2026-11-23, Asia/Kolkata

## Stage contract
- Required inputs: Current period brief; approved voice and writing rules; audience definition; supplied claims and relevant offering status; quality rubric; full current calendar version with explicit human approval covering every row; complete item brief for every row; qualified brief handoff; current context package.
- Helpful inputs: Approved pillars and hashtag bank; selected historical LinkedIn captions for style and text-overlap comparison; relevant feedback; proposed slots.
- Freshness rules: Use current period inputs. Historical captions remain valid for style and overlap checks using their supplied dates. For this text-only pilot, visual assets and alt text are out of scope.

## Selected evidence
| Source/record and version | Evidence IDs and relevant fact | Status and permission/scope | Freshness result | Permitted wording/excerpt |
|---|---|---|---|---|
| `knowledge layer/knowledge_index.md` v0.8 | Maps `brand.md`, `operations.md`, and `learning.md`; identifies internal pilot approval and source caveats. | Approved for internal pilot use per 2026-11-10 user instruction. | Updated 2026-11-23; usable for this run. | Use descriptive source names and retain relevant caveats. |
| `knowledge layer/brand.md` v0.5 | Voice, writing rules, audience personas, pilot themes, approved pilot hashtag bank. | Approved for internal pilot context; source facts not independently verified. | Updated 2026-11-18; usable. | Strategic, insightful, practical, confident without boastfulness, human and accessible. Concise paragraphs; meaningful hook; one relevant CTA. Up to three relevant tags from `#AIMarketing`, `#MarketingOperations`, `#WorkflowDesign`. |
| `knowledge layer/operations.md` v0.4 | LinkedIn text-post standards and pilot roles. | Approved for internal pilot context. | Updated 2026-11-18; usable. | 60–150 words excluding hashtags; short paragraphs; one core idea and one CTA; maximum 3,000 characters including hashtags. |
| `knowledge layer/learning.md` v0.7 | K8.3 rubric: brand voice, clarity, accuracy, CTA; 1–5 scale. Historical baseline: 63 posts, April–October 2026, mean 489.3 and median 381 impressions. | Approved for internal pilot reference. | Historical data retain their period; age does not lower readiness. | Use rubric dimensions and scale; skip pass target. Baseline only if relevant; impressions is the sole KPI. |
| `knowledge layer/claims.md` v0.3 | Current pilot supplied-claim handling. | Approved for internal pilot use. Claims supplied in current materials are final inputs; concerns go to human final-copy approval. | Updated 2026-11-18; usable. | No separate claim evidence or approval gate. Preserve scope; do not invent or expand claims. |
| `context/period_brief.md` — `VG-LI-2026-11-P1` | Six text-only LinkedIn posts; sole KPI is organic impressions; target approximately 5,700; baseline as recorded in `learning.md`; audience and CTAs supplied. | Current working period brief per user instruction. | Active dates 2026-11-23–2026-12-10; start date is the run date. | Use the active brief’s target and supplied objectives, audience, messages, and CTAs. |
| `brief_qualifier_11_23_01.md` | READY handoff; confirms brief and dates; explicitly says no specific calendar version approval was supplied in that handoff. | Current run prior output. | Dated 2026-11-23. | Planning may proceed; approval is still required before drafting. |
| `content_planner_11_23_02.md` | Six calendar rows and six item briefs; calendar approval marked Pending. | Current run prior output. | Dated 2026-11-23. Items 1 and 2 draft dates (Nov 18 and Nov 21) have elapsed; item 1 planned copy-approval date (Nov 21) has elapsed. | The six rows and briefs are available as the proposed calendar version, not as an approved version. |
| `calendar_approval_2026-11-20.md` | Approval applies to the entire calendar presented in the 20 November workflow run, with earlier publication dates. | Explicitly approved, but only for that earlier exact version. | Does not cover the changed 23 November calendar version. | No approval wording can be carried over to the current version. |

## Run inputs and prior approved outputs
| Run input or prior output | Exact file/version | Sections or fields supplied | Relevance/status |
|---|---|---|---|
| Period brief | `context/period_brief.md`, `VG-LI-2026-11-P1` | Whole brief | Current brief for drafting scope, messages, dates, and CTAs. |
| Brief qualification | `output/brief_qualifier_11_23_01.md` | Qualification verdict, key details, issues, next step | READY; notes no approval for a specific calendar was supplied. |
| Calendar and item briefs | `output/content_planner_11_23_02.md` | Full six-row calendar and all six item briefs | Calendar approval Pending; several planned deadlines elapsed. |
| Earlier calendar approval | `context/calendar_approval_2026-11-20.md` | Earlier approved version and its dates | Not approval of the current calendar version. |
| Knowledge index and brand | `knowledge layer/knowledge_index.md` v0.8; `knowledge layer/brand.md` v0.5 | Index and relevant brand sections | Supplies voice, rules, audience, themes, and hashtags. |
| Operations and learning | `knowledge layer/operations.md` v0.4; `knowledge layer/learning.md` v0.7 | Text-post rules, roles, rubric, compact learning core | Supplies standards and rubric. |
| Claims | `knowledge layer/claims.md` v0.3 | Current pilot claim-handling rule and supplied claim records | Available for supplied claims; no need for a proof-point register. |
| Historical captions and feedback excerpts | API-selected excerpts from `learning_posts.csv` and `learning_feedback.csv` | Not provided in the supplied run evidence | Caption comparison coverage and relevant feedback excerpts are unavailable. Caption coverage is a limitation only; it does not override the calendar-approval blocker. Feedback is optional. |

## Material provisional notes
| Note | Source | Why provisional | Effect on this stage |
|---|---|---|---|
| Current six-post calendar | `content_planner_11_23_02.md` | Planner marks approval Pending; 20 November approval names an earlier exact version. | Cannot draft against it until the entire current version is explicitly approved. |

## Gaps and conflicts
| Missing/disputed item | Sources involved | Owner | Blocking? | What is needed |
|---|---|---|---|---|
| Explicit human approval of the entire current six-post calendar version and all its rows | `content_planner_11_23_02.md` marks approval Pending; `calendar_approval_2026-11-20.md` covers only the earlier version | Pilot approver X or backup Y, as assigned in `operations.md` | Yes | Explicit approval of the exact current calendar version before Post Writer drafts. |
| Elapsed planned dates in the proposed calendar | `content_planner_11_23_02.md`; run date 2026-11-23 | Owner not specified | Not independently a context blocker; dates need resolution for execution | Resolve the elapsed draft deadlines for items 1 and 2 and item 1’s planned copy-approval date; retain the supplied dates unless the calendar owner updates the schedule. |
| Selected historical caption excerpts | Required stage map references API-selected excerpts; none are included in the supplied evidence | Owner not specified | No; limited overlap/style comparison does not lower readiness | Provide excerpts if a fuller text-overlap and style comparison is desired. |

## Verdict
- Result: BLOCKED
- Reason: The Post Writer contract requires explicit approval of the entire current calendar version. The supplied approval applies only to the earlier 20 November version, while the current planner output marks approval Pending.
- Permitted next action: Obtain explicit approval for the exact current calendar version, resolving the elapsed planned dates as needed; then assemble fresh context for Post Writer.
- Material limitations: Historical caption excerpts were not supplied, so no excerpt-based overlap comparison can be made. This does not change the blocking verdict.
