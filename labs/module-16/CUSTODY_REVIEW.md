# Key-custody and privileged-access review

**Module 16 PM deliverable · Educational draft · Course-derived 20-point rubric.** Complete with synthetic or explicitly authorized evidence. Never paste key material, tokens, protected prompts or customer records. This review is distinct from the 40-point chapter assessment and cannot certify a system.

## 1. Decision and boundary

Record workload/outcome, subject organization, jurisdictions for qualified review, named site or permitted service boundary, protected artifacts, users/operators, recovery target, decision owner, date and version. Distinguish BANK-A's physical-site rule from the multinational's expressly changed managed-service policy. State BLOCKED conflicts before scoring.

| Candidate | Effective data access | Key custody and policy administration | Complete operating boundary | Decision/gap owner |
|---|---|---|---|---|
| Local service, on-site custodians | Fill actual roles and indirect powers | Material, copies, lifecycle and recovery | Evidence required for every dependency | Eligible to investigate, not approved |
| External customer-managed key service | Inspect service/application/provider paths | Do not infer material custody from label | BLOCKED under unchanged BANK-A rule | Record changed assumption separately |
| External confidential workload | Inspect guest/application/verifier powers | Specify release policy | Attestation cannot erase location conflict | BLOCKED under unchanged BANK-A rule |

## 2. Effective permission graph

Draw actor → role/policy administrator → service/deployment → key operation → usable data. Include IdP administrators, application deployers, key administrators, custodians, backup restorers, provider/subcontractor support and audit administrators. Which one actor can combine permissions indirectly? Which powers remain in the TEE guest? Name independent approval and review boundaries and how they survive emergency recovery.

## 3. Lifecycle and recovery matrix

| Asset/version | Permitted purpose/users | Creation and current state | Rotation/migration/deletion rule | Backup/restore evidence and owner |
|---|---|---|---|---|
| Data key | Fill | Fill | Distinguish from wrapping key | Fill |
| Wrapping key | Fill | Fill | Identify old versions retained | Fill |
| Service credential | Fill | Fill | Expiry/revocation distribution | Fill |
| Attestation trust/reference material | Fill | Fill | Reviewed measurement/policy update | Fill |

Record key unavailability behavior, offboarding, compromised data, retired versions, restored old policy, and irreversible deletion approvals. Explain how already disclosed plaintext differs from remediating future access. No real deletion is required for this exercise.

## 4. Privileged-access and release contract

For each administrative operation specify exact resource/revision, initiator, two distinct eligible custodians where required, current policy, expiry, revocation, audit and result. State what rights support never receives and how approved access ends. For production attestation-based release specify workload/tenant/purpose binding, measurement/reference values, verifier trust, evidence freshness/nonce, result expiry, failure behavior and disconnected endorsement/update process. Mark implementation NOT COMPLETED if untested.

## 5. Evidence and release register

| Claim | Test / actual observation | Source and freshness | State | Owner and dated next test |
|---|---|---|---|---|
| Tenant/role/clearance enforcement | Lab metadata tests; replace with real identity test | Fixture only | Bounded educational observation | Fill |
| Distinct-custodian rotation | Lab two-grant checks | Process memory only | Bounded educational observation | Fill |
| No external path | Declarations are insufficient | Site/network/support/recovery review missing | UNVERIFIED or BLOCKED if conflict known | Fill |
| Attestation-based release | No hardware/verifier used | None | NOT COMPLETED | Fill |
| Key recovery and revocation | No actual cryptographic operation | None | NOT COMPLETED | Fill |

Define containment, restricted operation, rejection and retest. No numerical total overrides a known external path, failed permission check or missing required independent sign-off. Keep Module 04 HOLD and qualified legal applicability review open.

## 6. Educational rubric: 20 points

- **Boundary and decision, 4:** named subject/artifacts/operator/recovery; hard conflicts explicit.
- **Effective authority, 4:** identity trust, tenant and data-use/admin separation including indirect power.
- **Lifecycle and recovery, 4:** version/purpose inventory, rotation vs migration, revocation and safe recovery.
- **Privileged and attestation contract, 4:** bound approval, current eligibility, scoped support and honest attestation gaps.
- **Evidence and accountability, 4:** adverse/favorable observations, limits, states, owners and dated retest.

Suggested classroom threshold 16/20 plus all required sections; this is not a legal or production threshold. A polished narrative without evidence earns no evidence points. Return the review to product, security, platform, custody and qualified privacy/legal owners with explicit unresolved decisions.
