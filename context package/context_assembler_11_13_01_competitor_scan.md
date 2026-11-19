# Run Context Package

## Run header
- Client: Vajra Global
- Project: LinkedIn content workflow
- Channel: LinkedIn and public web sources for competitor intelligence
- Period: Research snapshot as of 13 November 2026; rolling comparison window 14 October–13 November 2026
- Run ID: Not provided
- Stage: Competitor Scan
- Stage-contract version: Current Context Assembler and Competitor Scan instructions; formal version not supplied
- Policy version: Current Vajra pilot content guidance
- Assembled on: 13 November 2026

## Stage contract
- Required inputs: Current stage context and readiness; approved market records and competitor list; approved brand records; approved claims, evidence and permission rules; previous scan when available; research window and observation requirements.
- Helpful inputs: Public company websites, public LinkedIn pages, dated case studies, credible industry sources, and previous scan references.
- Freshness rules: Market records are refreshed monthly; market v0.2 was updated 10 Nov 2026. Recheck any observation older than 30 days against current public sources or omit it. Record a defined period for any posting-frequency figure. Use only public sources; identify relative timestamps and incomplete feeds. Competitor statements are not Vajra-approved evidence.

## Selected records
| Source or record name | Version | Information needed by the stage | Status | Permission/scope | Freshness check | Permitted wording or relevant excerpt |
|---|---|---|---|---|---|---|
| Market intelligence — Vajra Global | v0.2, updated 10 Nov 2026 | Approved competitor set, competitor fields, research questions and public-source constraints | Approved for internal pilot use per user direction dated 10 Nov; approver name/role not supplied | Competitor set approved for research only; no permission to copy competitor content or treat their claims as Vajra evidence | Within monthly review cycle | Approved set: Social Beat, Schbang and Performics India. Do not call them the three closest competitors without separate evidence. Required fields include official identity/URLs, markets, services, audiences, positioning, content themes/formats, observed frequency over a defined period, dated public proof and source URLs. |
| Brand and company profile — Vajra Global | v0.3, updated 11 Nov 2026 | Internal capabilities/positioning for clearly labelled hypotheses | Approved for internal pilot context per user direction dated 10 Nov; item-level source caveats remain | Internal use; source wording is not automatically approved for public claims | Within stated 6–12 month review cycle | Internal positioning describes connecting strategy, technology, creativity and execution, and an AI-native growth/marketing partner direction. Treat as source-described positioning; confirm public wording before use. |
| Claims, evidence and permissions | v0.2, updated 10 Nov 2026 | Evidence and permission needed before converting a hypothesis to a Vajra claim | Approved for internal pilot context; item-level caveats remain | Public use requires claim-specific evidence, wording and permissions; client/results require explicit reuse permission | Apply claim-specific status/expiry; no competitor statement can satisfy this requirement | No unsupported superiority claims. A public competitor claim or metric is not evidence for Vajra. Any Vajra capability or outcome claim needs approved wording, evidence, scope and permissions. |
| Knowledge index | v0.4, updated 12 Nov 2026 | Source status and refresh details | Approved for internal pilot context per user direction dated 10 Nov | Internal pilot | Current | Market v0.2 is the approved competitor source; public-source observations remain attributed and unverified for reuse. |
| Prior Competitor Scan | `competitor_scan_11_11_01.md`, researched 11 Nov 2026 | Change comparison and prior observation check | Prior scan status LIMITED; context was READY | Internal intelligence comparison | Two days old; within the 30-day recheck window, but current public sources still rechecked | Prior window 12 Oct–11 Nov 2026. It covered Social Beat's PRISM update, Schbang's October roundup, Performics India's “25th Hour” AI-agent post, and a Dun & Bradstreet survey release. It could not compare to an older scan. |

## Run inputs and prior approved outputs
| Input/output | Version or date | Source | Stage relevance |
|---|---|---|---|
| User request | 13 Nov 2026 | Current run instruction | Explicitly requests optional Competitor Scan. |
| Approved competitor set | Market v0.2; approval recorded 10 Nov 2026 | `knowledge layer/market.md` | Defines the three names to research; approval covers selection, not the truth of public statements. |
| Prior scan | 11 Nov 2026 | `output/competitor_scan_11_11_01.md` | Provides the immediately preceding findings and comparison point. |
| Brand positioning and capabilities | Brand v0.3; 11 Nov 2026 | `knowledge layer/brand.md` | Permits only carefully caveated, internal hypotheses; no public claim is approved by this scan. |
| Claims and permission rules | Claims v0.2; 10 Nov 2026 | `knowledge layer/claims.md` | Defines evidence and permission required before any hypothesis becomes a Vajra public claim. |

## Provisional notes
| Note | Source and version | Why provisional | Not-for-claims reminder |
|---|---|---|---|
| Social Beat, Schbang and Performics India are the approved competitor set for this pilot. | Market v0.2 | User approval confirms research selection only; it does not establish a relative ranking or validate competitor claims. | Do not call them the “closest” competitors or use their content/metrics as Vajra evidence. |
| The rolling research comparison window is 14 Oct–13 Nov 2026. | Current run date and Competitor Scan 30-day freshness rule | A date window was set for this scan; it does not imply complete LinkedIn feed coverage. | State limits on frequency counts and relative timestamps. |
| The AI-native growth/marketing positioning is source-described in brand v0.3. | Brand v0.3 | The record says public wording needs confirmation. | Keep hypotheses general until approved public claim wording and evidence exist. |

## Gaps and conflicts
| Missing/disputed item | Sources/records involved | Owner | Blocking? | What is needed |
|---|---|---|---|---|
| Exact LinkedIn posting frequency and complete dated feeds may not be publicly verifiable. | Approved market schema; public competitor LinkedIn pages; prior scan | Research lead (named owner not supplied) | No | Report visible examples, use a defined observation window, and state when feeds/timestamps prevent exact counts. |
| No named approver or role is listed for internal pilot approval metadata. | Knowledge index v0.4, market v0.2, brand v0.3, claims v0.2 | Vajra knowledge owner (named person not supplied) | No for this internal scan | Preserve the recorded internal-use scope; do not infer public claim approval. |

## Verdict
- Result: READY
- Reason: The user requested the optional scan, the three competitors are approved for research, current market/brand/claims records and the previous scan are available, and the scan is limited to public sources. The known lack of complete public feed/frequency data is a reporting limitation, not a blocker.
- Permitted next action: Research the approved competitor set and relevant industry developments using public sources, compare with the 11 Nov scan, and clearly separate observations, interpretations and hypotheses.
- Limitations: Public LinkedIn feed completeness and relative dates may prevent exact post-frequency counts. Competitor facts and metrics remain source-attributed and are not approved for reuse as Vajra claims.

## Run record
- Records and versions checked: Knowledge index v0.4; market v0.2; brand v0.3; claims v0.2; Competitor Scan instructions; previous `competitor_scan_11_11_01.md`.
- Sources withheld due to permission/status: No logged-in, paid, private or restricted sources were selected. No unsupported Vajra proof points were included.
- Escalations or questions: None.
