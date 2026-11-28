# Module 15 lab: constrain hostile proposals

**Educational synthetic exercise; independent security and manual accessibility review pending.** No model, network, external API, real identity, customer data, Docker or paid service. Python 3.11+ standard library; CPU; allow 60–90 minutes.

## Outcome and scope

Execute a fixed local read capability behind independent schema, fixture-identity, tenant/resource, current revocation, artifact-digest, declared-boundary and audit-availability checks. A hostile `http_export` proposal is rejected whether it originated in a user prompt, retrieved note or arbitrary caller. This does not detect injection, measure model behavior or make the fixture safe for multi-user deployment.

## Run

From the repository root:

```bash
python3 labs/module-15/security_gate.py
python3 -m unittest discover -s labs/module-15 -p 'test_*.py' -v
```

The four demonstration cases perform two fixed local reads and deny an export and a cross-tenant read. [observed-security-run.json](observed-security-run.json) is a retained real execution of the synthetic fixture. Tests compare it with a fresh deterministic demonstration. No timestamps or hardware performance claims are inferred.

## Inspect and challenge

1. Trace trusted `alice` to tenant A using the fixture registry. Proposal JSON cannot select its tenant. The public fixture handle simulates a trusted identity; it is not a password, session or authentication protocol.
2. Read A-1, then try B-1. Denial happens before source text is returned. Missing and foreign resources share the same reason.
3. Read A-injected. Its hostile text is returned as **data**, not detected or sanitized. Propose `http_export`; it is absent from the allowed capability and denied. No language model or automatic parser turns the note into this proposal: the case explicitly supplies it.
4. Modify the harmless template bytes and recompute a matching caller manifest. Rejection uses a separately code-owned digest. This is not a signature, trusted-build pipeline or proof against someone editing the program itself.
5. Revoke Alice, change a document's tenant or mark it inactive, then re-run. Checks use current fixture state.
6. Change any of fourteen protected lifecycle locations to outside BANK-A. BLOCKED dominates missing data. Remove a location without a conflict: UNVERIFIED. Favorable declarations yield DECLARED_ONLY, never facility approval.
7. Disable audit availability. Reads fail closed before the call counter changes. The in-memory fixed-code audit is neither durable nor tamper-evident.

## Acceptance and limitations

All 35 named tests must pass, including loops for all fourteen protected categories. Retain failures, reasons, source revision and changes with the [PM threat model](THREAT_MODEL.md). A passing suite supports this fixture's bounded control behavior. There is no real RAG retrieval, model attack-success rate, data-loss prevention, signature/provenance verification, browser output protection, adversarial process isolation, identity provider, container scan, network inspection or physical air-gap verification.

The process has no network operations; that is a source property, not OS enforcement. The sample byte string is harmless and is never loaded as executable model code. Use synthetic local data for extensions; do not scan other systems or use a real secret. Production requires independent threat review, authenticated boundaries, complete output-channel controls, durable audit, realistic abuse tests and deployment evidence.

Return to the [chapter](../../chapters/15-ai-security-threat-modeling.md). Separate facilitator key remains outside this lab.
