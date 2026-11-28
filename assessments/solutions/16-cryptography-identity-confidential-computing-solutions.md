# Module 16 facilitator solutions

**Educational draft. Keep out of the public build.** Course-authored assessment, not independent certification. Total 40 points; separate PM deliverable rubric is 20 points. Accept equivalent supported reasoning. Qualified legal, cryptographic, hardware and facility review remain open; Module 04 HOLD persists.

## Q1. Protection boundaries (5 points)

Stored representation, communication channel and specified execution boundary differ (2). TLS protects its channel endpoints, not arbitrary downstream memory/logs or caller permissions (1). A valid connection can make an unauthorized cross-tenant request if the application fails resource authorization (2).

## Q2. Customer-managed custody (5 points)

Identify material creation/storage/copies/use/deletion/recovery (2), policy and identity/deployment administration including indirect access (2), and actual provider/support/operating boundary plus evidence rather than label (1). Do not award full credit for customer owns it.

## Q3. Rotation and recovery (6 points)

Distinguish wrapping material, data-key rotation and ciphertext migration (2). Retired material may still permit old reads, and old backups/policy can restore exposure (1). Compromised data-key remediation and credential/policy containment remain necessary (1). Test approved recovery and retention before irreversible deletion; disclosed plaintext cannot be undisclosed by rotation (2).

## Q4. Attestation release (6 points)

Attester/verifier/relying-party roles and current appraisal policy (1); trusted endorsements/reference measurements (1); freshness challenge, authenticated results and expiry (1); binding to permitted workload/tenant/purpose and fail-closed result (1); CPU/GPU/guest/application scope and residual attack surface (1); separate site/operator/support/legal and recovery evidence (1). The lab implements none of this hardware assurance.

## Q5. Real-source analysis (6 points)

AWS documents changing KMS key material while keeping old material usable for corresponding decryptions; generated data keys/ciphertext are not automatically replaced (2). Do not infer historical confidentiality repair, compromised-data-key removal, credential revocation or plaintext retrieval (2). Inspect actual affected material/objects, permitted access and migration/recovery evidence before revising the bounded decision (2). No real incident is asserted.

## Q6. Decision and root-cause scenario (12 points)

- **Evidence transitions, 2:** initial UNVERIFIED; observed authentication/tenant failures defeat release; external fallback known conflict is BLOCKED. Lab declarations cannot produce production VERIFIED.
- **Causes, 2:** public fixture labels substituted for authentication, shared elevated authority, missing tenant/resource checks and combined administration; systemic ownership/release-test failures.
- **Containment, 2:** suspend affected access and fallback, revoke/replace compromised service credentials, preserve minimal authorized evidence, assess scope and disclosed data with incident owners.
- **Mitigation and owners, 3:** security/IAM trusted identities/current tenant checks; platform/application narrow resource authorization; custodians effective separation and affected data-key/ciphertext lifecycle; support and independent reviewers own unresolved powers and boundary review.
- **Dated retest and bounded decision, 3:** name a real date and adverse/favorable tests for identity, cross-tenant access, current revocation, combined powers, recovery and audit. Local restricted operation only after its required gates and approvals pass; external diagnostics/support/recovery still block fallback under unchanged rule. Scores/attestation/rotation cannot override conflicts.

Independent assessment and actual deployment approval NOT COMPLETED. Deduct points for calling simulated metadata encryption, treating a fixture label as authentication, claiming attestation proves location, or erasing Module 04 HOLD.
