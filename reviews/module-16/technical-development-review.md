# Module 16 technical, source and security development audit

28 November 2026. Same-author AI-assisted development audit, not an independent or different-model review. Educational draft. Independent assurance NOT COMPLETED. Preserve Module 04 HOLD and earlier limitations.

## Scope and sources

Reviewed seven TOC topics, fourteen core chapter sections, synthetic policy/version lab, separate six-question 40-point key, distinct 20-point PM custody review, editable SVG/Mermaid and eight-question social derivative. Shared builder, ontology implementation, deployed routes, release CI and final PDF placement belong to coordinator integration; no publication result is asserted here.

Inspected six primary sources: NIST SP 800-57 Part 1 Rev. 5 landing-page abstract, NIST SP 800-207 abstract, AWS KMS rotation guide opening note, RFC 9334 introduction and attestation-result discussion, Google Confidential Computing overview introduction/trust table and current TLS RFC 9846 introduction. The RFC Editor explicitly marks RFC 8446 obsolete and links RFC 9846, published July 2026, which the chapter uses. Each retained brief extract was visible in its original page and is under 25 words per source; social artifacts paraphrase. Provider documents are not independent customer evidence. No legal requirement is asserted.

## Findings and decisions

- The lab performs actual Python RBAC/ABAC checks and version metadata mutation. It implements no encryption, decryption, key material, ciphertext, IdP, TLS, KMS, HSM, TEE or attestation. Names such as session labels and key identifiers are public fixtures. They are not deployable credentials. Trusted registries are writable process dictionaries, not a secure authorization service.
- Reader access checks current active/unexpired user, tenant, role, classification clearance and available referenced version. Key-admin and support roles do not grant data-use permission. A production deployer/IdP administrator may have indirect powers absent from this simple model; the PM permission graph explicitly asks for them.
- Rotation requires a current key-admin and two registered approvals from distinct eligible custodians, neither the initiator. Grants bind exact key, revision, current policy and expiry; invocation rechecks current custodian eligibility and consumes grants. No signatures are used. A process lock serializes races; no restart/durable/distributed transaction guarantee is claimed.
- The document retains version one after version two becomes current; old metadata remains readable while that referenced version is retired and becomes unavailable if disabled. This is a deliberate model of version references, not measured cryptographic rotation, ciphertext migration, secure deletion or actual backup restoration.
- Current boundary checks cover fifteen artifact categories and operator/network/media declarations. Known conflicts dominate omissions. Favorable declarations stay DECLARED_ONLY, never actual site or air-gap verification. No score enters the gate. Declared placement is not discovered from the OS, hardware or network.
- Audit readiness blocks before mutation. The list records only successful permitted metadata access and authorized metadata rotation, not durable denial audit or enterprise reconciliation. Records are mutable and lost on restart; minimization is not anonymization or tamper evidence. No raw credentials, key bytes or document content exist in this exercise.
- Attestation is discussed as a separate production design: trusted verifier/appraisal, freshness, workload binding, approved references and expiry. No fabricated Boolean attestation simulation is presented as hardware evidence. Physical residency, legal jurisdiction, application permission and guest-admin power remain distinct.

## Observed verification

`python3 -m unittest discover -s labs/module-16 -p 'test_*.py'`: **48 tests passed** on the current macOS environment. `python3 labs/module-16/custody.py` produced the retained `observed-custody-run.json`: seven attempts, three ALLOWED and four DENIED, including administrator/cross-tenant/support denial, successful two-custodian metadata rotation, replay denial and old reference retained. Three successful events appear in the minimal audit list. No real data or paid resource was used.

`social/module-16/test_rendered_carousel.py` passed with the existing QA Python/Chromium environment: eight question headings, reflow at 1280/390/320px, injected-overflow detection, keyboard reachability, no print clipping and eight 8×10-inch pages with extractable headings/text. Temporary PDF output only. Coordinator still owns final static build, final portrait-PDF export, visual inspection and deployment evidence.

## Open review and independent-review prompt

Independent/different-model assessment NOT COMPLETED. Manual assistive technology, 200% zoom/contrast, tagged PDF, actual IdP and cryptographic modules, attestation, hardware, facility/network isolation, operational recovery, revocation distribution and qualified legal applicability remain open.

Prompt for a genuinely independent reviewer: check every primary extract and current source version; attack session-to-subject trust, tenant/classification policy, role composition and indirect administration; test exact key/revision/policy/expiry binding, duplicate custodians, revocation, cross-tenant grant use and concurrent replay; distinguish version metadata from real key/ciphertext migration; inspect audit limits and restore-induced exposure; review a real verifier/release contract separately from site evidence. Record environment, reproducible findings and every conclusion the fixture cannot establish.
