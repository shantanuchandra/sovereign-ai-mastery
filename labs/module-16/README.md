# Module 16 lab: separate key administration and data access

**Educational draft.** Execute real Python policy checks against synthetic identities and key-version metadata. This is not cryptography: no key bytes, ciphertext, plaintext, encryption, decryption, IdP, KMS, HSM, TEE or attestation are implemented. Public fixture session labels stand in for identity infrastructure and must never become production credentials. All data is invented.

## Environment and procedure

Python 3.11+ standard library on a compatible CPU, no packages, GPU, Docker, model download, internet or paid service. Budget 60–90 minutes. The tiny dictionaries fit the course M4 Pro/16 GB baseline; actual run environment appears in `observed-custody-run.json`. From repository root:

```bash
python3 labs/module-16/custody.py
python3 -m unittest discover -s labs/module-16 -p 'test_*.py' -v
```

Expected seven attempts: administrator read DENIED, cross-tenant read DENIED, legitimate metadata read ALLOWED, two-custodian metadata rotation ALLOWED, old-record metadata read ALLOWED, replay DENIED and support read DENIED. `observed-custody-run.json` retains an actual run. It contains public synthetic actor/resource labels and fixed reasons, no usable credentials or actual data.

## Control model

A server-owned fixture maps session labels to current users. Access requires an active unexpired identity, matching tenant, reader role and adequate classification clearance. Key administrators receive no implicit read permission. The returned value is metadata only; it is never a decryption result.

An administrator may change key-version metadata only with two distinct current custodians' registered approvals. Each binds the exact key, revision, policy revision and expiry. The administrator cannot be either approver. Expired, revoked, cross-tenant, stale or consumed approvals fail before mutation. The registry is trusted process memory, not a signed authorization protocol; learners can edit it directly. A single-process lock serializes concurrent attempts, without providing distributed or restart-safe guarantees.

Rotation retires version one and creates version two; the synthetic document still references version one, which remains readable as metadata. This deliberately demonstrates that changing a current version does not migrate old records. Setting an old version disabled causes access denial. It is not a test of data-key rotation, ciphertext migration, secure deletion, backup recovery or compromised-data remediation.

## Boundary and audit

The fictional BANK-A policy covers prompts, outputs, weights, embeddings, OCR, speech, diagnostics, logs, telemetry, backups, support, activation, updates, recovery and removable media, plus on-site operators, offline connectivity and reviewed media. Any known conflicting declaration yields BLOCKED even with missing evidence. Missing fields yield UNVERIFIED; favorable declarations yield DECLARED_ONLY. Neither actual placement nor a physical air gap is verified.

Boundary or audit unavailability blocks access and rotation. Audit records permitted metadata access and authorized metadata rotation with actor, target and policy revision; no rejected-attempt durable audit service is implemented. Records are mutable and lost at restart; no integrity, independent audit access or retention guarantee is claimed. Public metadata is still potentially sensitive in a real system.

## Mutation exercises and acceptance

| Mutation | Expected result | Observable evidence |
|---|---|---|
| Reader becomes inactive, expired, wrong tenant or lower clearance | DENIED | No metadata access audit added |
| Administrator/support requests data | DENIED | Role separation |
| Same custodian produces two grants | DENIED | Distinct actor check |
| Administrator also approves | DENIED | Initiator separation |
| Policy, key revision or approver changes | DENIED | Freshness/current eligibility |
| Invoke at exact expiry or replay a grant | DENIED | Expiry and consumption |
| Race two identical rotations | One ALLOWED | Current version increments once |
| Audit unavailable before rotation | DENIED | Versions/grants unchanged |
| Disable retired version | DENIED on old reference | No implicit migration |
| External diagnostics plus missing backups field | BLOCKED | Conflict dominates omission |

The 48 tests exercise these checks, including every artifact category. Successful educational acceptance means this bounded implementation behaves as declared. Actual authentication, cryptographic modules, support access, attestation, OS/network isolation and enterprise authorization remain separate work.

Cleanup: no services or resources were created. Delete only your own optional output file. Complete the [custody review](CUSTODY_REVIEW.md), then return to [Module 16](../../chapters/16-cryptography-identity-confidential-computing.md).
