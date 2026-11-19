# Run Context Package

## Run header
- Client: Vajra Global
- Project: LinkedIn content pilot
- Channel: LinkedIn company page; exact page URL/stable identity not provided
- Period: Pilot period 11–20 November 2026; Item 1 schedule date 18 November 2026 is assumed
- Run ID: PV-2026-11-13-01
- Stage: Publish and Verify
- Stage-contract version: Current project Publish and Verify instructions; no separate version supplied
- Policy version: SHARED SKILL OUTPUT RULES.md; no formal version supplied
- Assembled on: 13 November 2026

## Stage contract
- Required inputs: Exact final copy and version; approval confirmation for that exact copy; item reference/topic/pillar/format; LinkedIn company page identity; confirmed publication date, time and timezone; calendar constraints/dependencies; named authorized publisher and verified page access.
- Helpful inputs: Prior QA report and current calendar context.
- Freshness rules: Confirm page identity, publisher permissions, calendar and approval at release. Do not publish or report verification without checking a live post.

## Selected records
| Source or record name | Version | Information needed by the stage | Status | Permission/scope | Freshness check | Permitted wording or relevant excerpt |
|---|---|---|---|---|---|---|
| Content Planner | CP-2026-11-13-04 | Item 1 reference, topic, pillar, format, scheduled slot and item state | Plan approved; Item 1 approved for drafting | Internal workflow | 13 Nov 2026 | Item 1: AI & Innovation; text-only; 18 Nov 2026 assumed; no time supplied |
| Post Writer draft | PW-2026-11-13-03 | Exact text and hashtags | Draft ready for review | Internal workflow | 13 Nov 2026 | Exact text in corresponding output; no direct publication action taken |
| Post Quality Analyst | PQA-2026-11-13-02 | Independent QA result | PASS | Internal review | 13 Nov 2026 | Text-only copy passed current checks |
| User approval in conversation | Prior user message: “i approve the final post” | Human approval state | Approval stated in conversation; local record does not identify exact copy version approved | Pilot approval authority per operations | Approval date/version binding not recorded in local run artifacts | Do not assume it applies to a later text change; current fresh draft copy text matches prior saved draft text, but explicit version binding is not recorded |
| Operations and calendar constraints | v0.3 | Publisher, approver, page access rules, timezone and calendar constraints | Approved for internal pilot use; access verification outstanding | Internal workflow; actual account permissions not granted by this record | Current supplied version | X is pilot approver; Y is backup approver and assigned publisher; actual page identity and account rights still require confirmation; timezone IST subject to confirmation |
| Period Brief VG-LI-2026-11-P1 | Updated 12 Nov 2026 | Pilot period and scope | Confirmed working brief | Internal workflow | Current period | 11–20 Nov 2026, six text-only posts |
| Calendar and post schedule | Content Planner 11_13_04 | Date/time, dependencies, blackouts | Date assumption only; time absent | Internal planning | Current plan | No blackout dates assumed; 18 Nov date not confirmed/scheduled |

## Run inputs and prior approved outputs
| Input/output | Version or date | Source | Stage relevance |
|---|---|---|---|
| Current draft | PW-2026-11-13-03 | output/post_writer_11_13_03.md | Exact copy to compare with any approved version |
| Independent QA | PQA-2026-11-13-02 | output/post_quality_analyst_11_13_02.md | Confirms copy review result; not a publishing action |
| Calendar/item brief | CP-2026-11-13-04 | output/content_planner_11_13_04.md | Item details and assumed schedule date |

## Provisional notes
| Note | Source and version | Why provisional | Not-for-claims reminder |
|---|---|---|---|
| 18 November 2026 publication date | Content Planner 11_13_04 | Explicitly assumed, not reconciled or scheduled | Do not describe as confirmed publication |
| User final-copy approval | Prior conversation | User approval exists, but its exact output-version binding is not recorded locally | Do not state that a specific version is approved unless confirmed against exact text |
| Publisher Y | Operations v0.3 | Role assignment exists; company-page access is unverified | Do not infer permission from role assignment |

## Gaps and conflicts
| Missing/disputed item | Sources/records involved | Owner | Blocking? | What is needed |
|---|---|---|---|---|
| LinkedIn company page URL and stable identity | Operations v0.3; current run inputs | Owner not specified | Yes | Identify the correct company page |
| Publisher Y's current page access | Operations v0.3 | Y is assigned publisher; permission owner not specified | Yes | Confirm publishing access through approved account process; do not provide credentials in chat |
| Confirmed date, time and timezone | Planner 11_13_04; operations v0.3 | Calendar owner Pranathy; named role | Yes | Confirm calendar slot and IST/global timezone applicability |
| Approval linked to exact copy version | Conversation approval; Post Writer 11_13_03 | Approver X assigned in operations; direct approval was from user | Yes | Record approval against exact final copy version |

## Verdict
- Result: BLOCKED
- Reason: Required page identity, verified publisher access, confirmed publication time/timezone, and exact version-bound approval are not established in the supplied project records. Context rules require the downstream Publish and Verify stage not to proceed while these are missing.
- Permitted next action: Resolve the listed release inputs, then assemble a new Publish and Verify context package.
- Limitations: No publication attempt or live-post verification is supported by this context.

## Run record
- Records and versions checked: Content Planner CP-2026-11-13-04; Post Writer PW-2026-11-13-03; Post Quality Analyst PQA-2026-11-13-02; Period Brief VG-LI-2026-11-P1; operations v0.3; user approval message in current conversation.
- Sources withheld due to permission/status: No credentials or private account information accessed.
- Escalations or questions: Required release details listed above; no login secrets requested.
