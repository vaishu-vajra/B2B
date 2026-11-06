---
name: publish-and-verify
description: Ensures approved content is published by an authorised publisher and verifies that the published content matches the approved version and publishing requirements.
---

# Publish and Verify

## 1. Main Purpose

Ensure content is published only after the required human approval.

Verify that the published content matches the approved version and the applicable publishing requirements. Record the publishing and verification results for future reference.

## 2. Input

### 2.1 Approved Content

- Final approved content or caption.
- Approved creative or media.
- Content format.
- Content pillar.
- Post ID or internal content reference.
- Approval status.
- Approval confirmation.
- Approved stage output.

### 2.2 Publishing Context

- Publishing channel.
- Scheduled publishing date and time.
- Timezone.
- Relevant calendar record from the context package.
- Calendar restrictions and blackout dates.
- Required dependencies.
- Authorised publisher and approval roles from `operations.md`.

### 2.3 Verification Information

- Post ID.
- Post URL.
- Actual published date.
- Final published copy.
- Published creative reference.
- Publishing status.
- Content owner.
- Data source, where applicable.
- Extraction date, where applicable.

## 3. Instructions

1. Read the relevant publishing information from the current run's context package.

2. Review the approved stage output and confirm that the required human approval is recorded.

3. Verify that the final caption and creative match the approved content.

4. Confirm the scheduled publishing date, time and timezone against the calendar record.

5. Check the applicable calendar restrictions, blackout dates and required dependencies.

6. Confirm the authorised publisher and approval roles using the information in `operations.md`.

7. Do not publish content if approval is missing, dependencies are incomplete, or a relevant calendar restriction is unresolved. Flag the issue for human review.

8. Ensure that only an authorised publisher performs the publishing action through the approved channel.

9. After publishing, verify that the post is available on the publishing channel.

10. Compare the published caption and creative against the approved version.

11. Record the actual publication details, including the post ID, post URL and published date.

12. Record the verification results and update the publishing status.

13. If publishing fails, the post is unavailable, or the published content differs from the approved version, flag the issue for the responsible human owner.

14. Do not mark content as published and verified without checking the published post.

15. Do not modify approved content during publishing without obtaining the required human approval.

16. Store approved publishing and verification outputs in `stage_outputs/`.

## 4. Output

Produce a structured publishing and verification record.

### 4.1 Publishing Record

- Post ID or internal content reference.
- Content owner.
- Content pillar.
- Topic, if available.
- Campaign, if applicable.
- Content format.
- Approved caption.
- Creative reference.
- Publishing channel.
- Scheduled publishing date and time.
- Actual published date.
- Authorised publisher.
- Approval status.
- Publishing status.

### 4.2 Verification Record

- Published post URL.
- Verified post ID.
- Verified published date.
- Caption verification result.
- Creative verification result.
- Calendar compliance result.
- Verification result.
- Issues or discrepancies identified.

### 4.3 Final Publishing Status

Identify the applicable status:

- Published and verified
- Scheduled
- Pending approval
- Pending publishing
- Publishing failed
- Verification required
- Issue flagged for human review

### Output Requirements

- Publish only after required human approval.
- Use an authorised publisher.
- Verify published content against the approved version.
- Record actual publishing details.
- Clearly report failures, discrepancies and unresolved issues.
- Do not assume successful publication without verification.
- Retain the approved output and verification record in `stage_outputs/`.