---
name: publish-and-verify
description: Publishes human-approved text-only LinkedIn post copy through an authorised publisher and verifies the live post against the exact approved version. Records approval confirmation, scheduled and actual publication details, publisher role, live post URL and ID, calendar compliance, copy match, and final status. Identifies publishing failures or discrepancies for human review. Does not handle creative assets or request login secrets.
---

# Publish and Verify

## Purpose

Publish the final LinkedIn post only after its exact copy has received human approval. Verify that the live text matches the approved version and record the publication details. This is the only workflow stage that evaluates final-copy publication authorization, publisher access, live-post status, or publication verification. Upstream stages report their own readiness and human decision states without publication-readiness disclaimers.

For the current Vajra pilot, the publishing scope is text-only LinkedIn post copy. Do not request, require, publish, or verify images, carousels, videos, captions for media, alt text, or other creative materials.

## Required inputs

- Fresh context package assembled specifically for the Publish and Verify stage.
- Exact final post copy and its approved version.
- Approval status and the approval confirmation for that exact copy.
- Post or calendar item reference, topic, content pillar, and text-post format.
- LinkedIn company page identity.
- Scheduled publication date and time, timezone, relevant calendar record, restrictions, dependencies, and blackout dates.
- Authorised publisher and approval roles from the approved operations and calendar records.
- Confirmed publishing access for the authorised publisher.

Do not request or record account passwords, verification codes, or other login secrets. The authorised publisher must use their own approved signed-in session.

## Instructions

1. Run Context Assembler for this stage immediately before running Publish and Verify. Do not reuse a context package from another stage or earlier run.
2. Check the approved stage output and confirm that human approval is recorded for the exact copy version to be published.
3. Confirm that the final text, including hashtags and punctuation, matches the approved copy. Do not edit it during publication.
4. Use the current approved plan date for the Vajra pilot; no separate calendar-reconciliation step is required. Confirm the actual publication time and timezone before scheduling or publishing. Keep a planned date distinct from actual publication status.
5. Check calendar restrictions, blackout dates, and required dependencies.
6. Confirm the named publisher role and publishing access from the approved operations information. Do not infer access from a role assignment alone.
7. Do not publish if approval is missing, the exact approved version is unclear, access is unverified, dependencies are incomplete, or a relevant calendar restriction is unresolved. Record the status as pending or issue flagged for human review.
8. Only the authorised publisher may perform the publishing action through the approved LinkedIn company page and signed-in session.
9. After publication, open the live post and verify that it is available on the correct company page.
10. Compare the live post text with the approved version, including hashtags. Record any difference; do not mark it verified if the copy does not match.
11. Record the post URL, post ID, actual publication date and time, authorised publisher role, and publishing status.
12. Record calendar compliance and the copy-verification result. If publishing fails, the post is unavailable, or the live copy differs, flag the issue for the responsible human owner.
13. Do not mark content Published and verified without checking the live post.
14. For this pilot, LinkedIn organic impressions is the only KPI in scope. Do not add other performance metrics or targets to the publishing record.

## Supplied claim handling

Claims supplied in the active brief or project records are final for this workflow. Do not require separate claim-level approval or additional evidence before the human final-copy approval stage. Pass any claim accuracy concern identified upstream to the human approver, who addresses it while reviewing the exact final copy. Do not reject or alter supplied claims during publishing; publish only the exact copy that the human has approved. A current explicit instruction that withdraws or prohibits a claim still controls. This rule removes claim-by-claim approval; it does not remove the human approval requirement for the exact final post or the required access and publishing checks.

## Output

Produce a publishing and verification record containing:

### Publishing record

- Post or calendar item reference.
- Topic and content pillar.
- Content format: text-only LinkedIn post.
- Exact approved post copy.
- Publishing channel and company page identity.
- Scheduled publication date and time, with timezone.
- Actual publication date and time.
- Authorised publisher role.
- Approval status and confirmation.
- Publishing status.

### Verification record

- Published post URL.
- Verified post ID.
- Verified publication date and time.
- Live post copy matches approved copy: Yes / No / Not verified.
- Calendar compliance: Pass / Issue / Not verified.
- Verification result.
- Issues or discrepancies.

### Final publishing status

Use one status:

- Published and verified
- Scheduled
- Pending approval
- Pending publishing
- Publishing failed
- Verification required
- Issue flagged for human review

## Output storage

Save the publishing and verification record in the project's `output/` folder using `<skill_name>_<MM>_<DD>_<version>.md`. Start at version `01` for the first run on a date and increment the version for additional runs of this skill that day.