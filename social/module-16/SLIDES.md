# Module 16 question carousel

Educational draft. Eight 4:5 portrait slides; HTML is canonical and the export is an untagged PDF. No em dash is used in social artifacts.

## 1. Does encryption decide who can read?

At-rest, transit and in-use protection address different boundaries. An authorized application can still expose another tenant’s record.

Decision: Inspect the identity-to-data path.

Source/scope: RFC 9846 section 1; NIST SP 800-207; checked 28 Nov 2026.

## 2. Who controls a customer-managed key?

Ask who creates, copies, uses, disables and recovers it. Include the people who change identity, deployment and key policy.

Decision: Write effective powers beside each label.

Source/scope: Course custody analysis; primary references in the chapter.

## 3. Should a key administrator read data?

Administrative rights and data-use permission need separate decisions. The lab refuses administrator and support reads.

Decision: Test both direct and indirect authority.

Source/scope: Synthetic metadata policy exercise; no actual authentication.

## 4. Does rotation replace historical protection?

A wrapping-key change need not replace data keys or migrate ciphertext. Old versions may remain necessary for historical recovery.

Decision: Define exactly which layer changes.

Source/scope: AWS KMS rotation guide; checked 28 Nov 2026.

## 5. What does an attestation result decide?

A verifier appraises evidence under policy. Release should bind trusted, fresh results to the permitted workload and purpose.

Decision: Review the verifier and release policy too.

Source/scope: IETF RFC 9334, introduction and section 8.4; checked 28 Nov 2026.

## 6. Can an attested service cross this boundary?

BANK-A’s fictional physical-site-only rule still blocks an external service. Hardware protection does not change location or operator requirements.

Decision: Keep the unchanged boundary before scoring.

Source/scope: Illustrative policy; no legal or facility assurance claimed.

## 7. Can one custodian approve twice?

Two fixture grants from the same actor fail. Policy revision, key revision, expiry and current custodian eligibility are checked again.

Decision: Bind distinct approvals to the exact operation.

Source/scope: Course-authored two-custodian metadata simulation.

## 8. What did the local exercise establish?

Seven synthetic attempts exercise separation, tenant policy, rotation metadata, replay and old references. No encryption or TEE ran.

Decision: Carry observations and open owners into review.

Source/scope: Educational draft; independent/manual/hardware assurance pending.

Export: `python social/module-16/export_pdf.py`. Render check: `python social/module-16/test_rendered_carousel.py`. Manual screen-reader, 200% zoom, contrast and PDF tagging review remain open.
