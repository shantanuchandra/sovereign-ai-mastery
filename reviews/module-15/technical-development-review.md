# Module 15 technical, source and security development audit

28 November 2026. Same-author AI-assisted development audit, not independent or different-model review. Educational draft. Independent assurance NOT COMPLETED. Preserve Module 04 HOLD.

## Scope and verified sources

Reviewed seven syllabus topics, the 14-section chapter, synthetic policy gate, retained execution, 35 named adverse/favorable tests, PM threat-model/20-point rubric, separate Q1–Q6/40-point key, SVG/Mermaid and social sources. Root integration, matching-head CI, deployment and live mobile chapter checks are separate release tasks; no publication result is asserted here.

Inspected six primary pages using web retrieval: OWASP community Threat Modeling, OWASP LLM01:2025, OWASP LLM03:2025, NIST SP 800-207 abstract, OWASP API Security Project and SLSA v1.2 Provenance. Every brief ledger extract appears in its specified section. An initially guessed OWASP prompt-injection URL returned 404; the recorded canonical URL was retrieved successfully. SLSA v1.1 identifies itself as retired; the chapter uses inspected v1.2. The OWASP community/API URLs redirect to the canonical paths recorded in footnotes. Publication dates not established by the page are left unstated. Each source's exact extracts total fewer than 25 words; social derivatives paraphrase.

## Findings and corrections

- The lab intentionally returns injected source content as data to a permitted fixture principal. It does not claim detection, sanitization, model refusal, model attack-success rate or free-form output confidentiality. A later supplied hostile export proposal is independently denied. The demo does not automatically parse source instructions or run an LLM.
- Trusted identity and tenant context are public server-owned teaching fixtures, not credentials or authentication. Current identity/resource state is rechecked. Unknown and foreign resource IDs share a fixed denial reason. Exact schemas reject client tenant/approval/destination fields; only one fixed local read tool exists. No shell or network adapter is implemented.
- Artifact bytes are compared to a code-owned expected digest, separately from the caller's manifest. Replacing both artifact and manifest is denied. This demonstrates integrity comparison under the fixture's trust assumption, not signature/provenance verification or defense against an attacker editing the trusted process.
- The coordinator found a conflict-dominance defect: malformed artifacts could return UNVERIFIED before an explicit internet/remote-operator conflict was checked. Corrected ordering and added combinations of three malformed inventories with both external network and remote operators. Known conflicts now dominate missing inventory. Favorable declarations remain DECLARED_ONLY, never facility or air-gap assurance.
- Fourteen lifecycle artifact categories are tested individually for known outside locations and missing locations. Audit failure closes the fixed read before its counter changes. Audit contains only fixed decision/reason codes; it is neither persistent nor tamper-evident. No real resource, secret, customer data, external endpoint, container or infrastructure is used.
- The gate does not implement real RAG retrieval, model loading, browser rendering, tenant session security, authorization across concurrent services, DLP, host/network isolation or platform scanning. These stay open in the chapter and PM register.

## Observed checks

`python3 -m unittest discover -s labs/module-15 -p 'test_*.py' -v`: **35 tests passed**. `python3 labs/module-15/security_gate.py`: four cases, two fixed local reads, export denied and cross-tenant read denied. The retained record equals a fresh deterministic demonstration. Input/output content is synthetic. No performance benchmark is asserted.

Rendered carousel check passed after final test-count wording changes: eight question-led headings; document/slide reflow at 1280/390/320 px; an injected overflow mutation is detected; chapter link keyboard reachable; no print clipping; eight 8×10-inch pages with extractable text/headings. Root performs final site/PDF export after the shared build. Author inspected all eight slide previews and the complete diagram. Standalone SVG screenshot capture timed out in the local browser, while embedding the same XML in a local HTML page rendered completely; root should verify its actual reader `<img>` route.

## Independent-review prompt and open assurance

Independent/different-model review NOT COMPLETED. Prompt: verify each extract in context; challenge scope, principal/resource binding, modified artifacts and caller manifests, all lifecycle conflicts including malformed inventory, audit failure and data returned through permitted reads; distinguish hostile-proposal enforcement from model injection resistance; inspect actual rendering, complete authority graph, real identity, trust roots, platform/runtime controls, output channels, operational recovery and facility evidence. Report reproducible defects and claims not supported by the fixture. Qualified applicability, production security, manual assistive-technology/zoom/contrast and tagged-PDF assurance remain open.
