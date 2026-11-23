# Run Context Package

## Run header
- Client: Vajra Global
- Project: Vajra Global Social Content Delivery
- Channel: LinkedIn company page
- Period: 2026-11-23 to 2026-12-10; six text-only posts
- Run ID: run_2026-11-23_02
- Stage: Post Quality Analyst
- Assembled on: 2026-11-23, Asia/Kolkata

## Stage contract
- Required inputs: Same-run qualified brief, current full calendar and item briefs, complete matching draft batch, approved voice/writing rules, supplied claims, audience context and rubric.
- Helpful inputs: Selected historical feedback and caption matches based on actual draft keywords.
- Freshness rules: Historical captions remain tied to their Published dates. Compare actual drafts to permitted caption matches at QA execution; feedback status does not determine QA readiness.

## Selected evidence
| Source/record and version | Evidence IDs and relevant fact | Status and permission/scope | Freshness result | Permitted wording/excerpt |
|---|---|---|---|---|
| `knowledge layer/brand.md`, v0.5 | Tone: strategic, insightful, practical, confident without boastfulness, human; accessible and conversational. Concise paragraphs, meaningful hooks, avoid excessive jargon and generic AI phrasing. | Approved for internal pilot context. | Review cycle 6–12 months/on change; no explicit expiry supplied. | Use to assess copy voice and clarity. |
| `knowledge layer/operations.md`, v0.4 | Pilot text standards: 60–150 body words excluding hashtags, short paragraphs, one core idea, one CTA, up to three relevant approved tags; 3,000-character maximum. | Approved pilot standards. | Limit source checked 2026-11-11 per record. | Apply to submitted post text only. |
| `knowledge layer/brand.md`, v0.5 | Approved hashtags: `#AIMarketing`, `#MarketingOperations`, `#WorkflowDesign`. | User-approved pilot bank, 2026-11-11. | Pilot scope. | Only relevant tags from this bank, up to three. |
| `knowledge layer/learning.md`, v0.7 | Rubric 1–5 anchors supplied for brand voice, clarity, accuracy and CTA (1 poor, 3 acceptable, 5 excellent). Strategic relevance, audience relevance, originality, visual quality and evidence quality are listed but anchors are not supplied. | Approved internal pilot reference. | Current supplied rubric. | Score anchored dimensions; mark unanchored dimensions not assessed rather than inventing anchors. |
| `context/period_brief.md`, VG-LI-2026-11-P1 | Six text-only posts; audience roles and goals; supplied claims final for pilot; accuracy/disclosure/permission concerns routed to human final-copy approval. | Confirmed working brief. | Current period. | Review claims faithfully; no separate evidence gate. |
| `knowledge layer/learning.md`, v0.7 | Compact historical feedback register F1–F13; examples ask for added context, less generic tone, spacing similar topics and relevant CTA. | Optional historical context; incomplete metadata; not formal rules absent approval. Detailed feedback selection empty. | Historical, not current open feedback. | Treat as context, not formal rules. |
| `knowledge layer/learning_posts.csv`, selected excerpt input | Writer selection contains shortened captions dated 2026-04-01–2026-10-26. | Internal style/overlap source; QA’s own actual-draft matches not yet selected. | Published dates supplied. | At QA execution, caller supplies relevant caption matches chosen from actual draft keywords. Do not use writer excerpt set as a substitute for actual-draft matching. |

## Run inputs and prior approved outputs
| Run input or prior output | Exact file/version | Sections or fields supplied | Relevance/status |
|---|---|---|---|
| Same-run Brief Qualifier result | Not provided | Readiness and handoff | **Pending**; attach for this exact run. |
| Same-run Content Planner output | Not provided | Full calendar and item briefs | **Pending**. |
| Same-run Post Writer output | Not provided | Full draft batch and exact copy | **Pending**; QA must match every draft to its calendar item. |
| Historical caption matches selected from actual draft keywords | `knowledge layer/learning_posts.csv` | Not selected yet | **Pending at QA execution**; caller supplies QA-specific matches once drafts exist. |
| Detailed feedback selection | `knowledge layer/learning_feedback.csv`, selected input empty | No rows supplied | Optional; use compact learning.md feedback register. |
| Earlier calendar approval | `context/calendar_approval_2026-11-20.md` | Prior calendar only | Context only; does not approve current calendar version. |

## Material provisional notes
| Note | Source | Why provisional | Effect on this stage |
|---|---|---|---|
| Historical feedback entries have incomplete reviewer/decision metadata. | `knowledge layer/learning.md`, v0.7 | Records preserve comments but do not establish formal rules or current status. | Optional context only; does not lower verdict. |
| Caption excerpts are shortened and the QA-specific matching selection awaits actual drafts. | `knowledge layer/learning_posts.csv`; run inputs | QA matching depends on actual draft keywords; no drafts yet. | Attach matches at execution and state coverage. Partial match coverage alone need not block or require revision. |

## Gaps and conflicts
| Missing/disputed item | Sources involved | Owner | Blocking? | What is needed |
|---|---|---|---|---|
| Same-run qualified brief, full current calendar/item briefs, and complete matching draft batch are unavailable. | Required prior outputs | Brief Qualifier, Content Planner and Post Writer stages | Yes | Attach all three same-run outputs and verify each draft maps to its calendar row. |
| QA-specific historical caption matches cannot yet be selected. | `knowledge layer/learning_posts.csv`; draft batch not available | Caller/QA stage | Pending execution dependency | Select permitted caption matches using actual draft keywords when the batch is attached; do not use arbitrary matches. |
| Explicit current-calendar approval is not supplied. | `context/calendar_approval_2026-11-20.md`; current run | X or Y | No for QA context; required upstream context | Attach current whole-calendar approval with the planner output; the November 20 approval covers only the earlier calendar. |

## Verdict
- Result: BLOCKED
- Reason: The required same-run brief, complete calendar/item briefs and complete matching draft batch are pending.
- Permitted next action: When those outputs arrive, attach them, obtain QA-specific historical caption matches from actual draft keywords, then review every matching item independently.
- Material limitations: Detailed feedback excerpts are unavailable; use only the compact historical feedback register. Caption comparison is pending, not assessed at assembly. Text-only scope excludes creative assets.
