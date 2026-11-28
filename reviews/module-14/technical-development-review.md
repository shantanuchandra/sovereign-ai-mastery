# Module 14 technical, source and security development audit

28 November 2026. Same-author AI-assisted development audit, not an independent or different-model review. Educational draft; independent assurance NOT COMPLETED. Preserve Module 04 HOLD and earlier module limitations.

## Scope and primary sources

Inspected the seven syllabus topics, synthetic gate, 44 adverse/favorable tests, retained run, PM control-spec/abuse register, separate six-question key, editable SVG and carousel source. Root integration, deployed routes and matching-head CI are separate release tasks; no publication result is asserted here.

Verified five primary pages live with HTTP 200 and found every short quotation in normalized visible source text: Anthropic Building effective agents (What are agents?), OWASP LLM06:2025 (Complete mediation), RFC 9700 (section 2.3), MCP 2025-11-25 (Token Passthrough), AWS Bedrock return-control introduction/flow. The MCP specification URL redirects to the versioned documentation URL recorded in the chapter. No publication date is invented for AWS or MCP. Quoted extracts are under 25 words per source across the package; social derivatives paraphrase rather than repeat extracts. Provider interface descriptions are not customer deployment evidence.

## Findings and bounded decisions

- Kept model proposal, trusted user/agent delegation, credential audience/scope, resource/tenant authorization and reviewer consent separate. The lab has fixed synthetic tools and public fixture handles, not actual credentials or protocol authentication. Trusted registries are directly mutable by the learner to test revocation; this is not secure multi-user infrastructure.
- Approval is registered and HMAC-bound to canonical request/tenant/user/agent/tool/resource/version/params/policy, with approver, expiry and random ID. Invocation rechecks reviewer, current permissions and versions, then consumes the grant/request under a single-process lock. Tamper, expiry boundary, revocation, stale context and concurrent replay are tested. A copied frozen dataclass still has mutable parameters; invocation and approval copy input before checking. Tool-version binding is a production specification requirement; the fixture has one fixed implementation.
- Checks fail closed before the mock tool. Audit unavailable before execution leaves the synthetic resource unchanged. AUTHORIZED denotes intent and COMPLETED denotes observed return. The fixture does not model a downstream transport failure, crash-safe persistence, distributed coordination, replay across process restart or externally atomic logging. Those gaps stay open; exactly-once delivery is not claimed.
- Audit omits raw params, credential/session handles, signatures, prompts and ticket bodies. Hashes of predictable data remain guessable, and the in-memory log has no external integrity, retention or audit-access service. Redaction is not anonymization.
- Boundary checker covers fourteen artifact categories plus on-site operator, offline network and media review. Known conflict dominates missing evidence and favorable scores. Favorable declarations yield DECLARED_ONLY, never acceptance or physical evidence. Actual facility, network/OS, support, activation, update and restore assurance are NOT COMPLETED.
- No language model, enterprise connector, MCP/OAuth implementation, AWS call, cloud resource, private data or paid service was used. Fictional scenario results are distinct from the retained actual synthetic-control observation.

## Observed verification

`python3 -m unittest discover -s labs/module-14 -p 'test_*.py' -v`: **44 tests passed** on macOS arm64, Python 3.14.8. `python3 labs/module-14/gated_agent.py`: missing approval denied, exact approved closure completed, replay denied, cross-tenant resource denied; exactly one tool invocation. `observed-control-run.json` retains a genuine run, with random identifier variation expected.

Rendered carousel checks passed using the existing Playwright environment: eight question headlines; document/slide reflow at 1280, 390 and 320 px; detector catches an injected overflow; chapter link keyboard reachable; print has no slide clipping; eight 8×10-inch pages with extractable text/headings. This run writes a temporary PDF. Final site build/export and root visual review occur separately. No deployment or whole-site assurance is inferred from this module's tests.

## Unresolved review and independent-review prompt

Independent/different-model review NOT COMPLETED. Manual screen-reader, zoom/contrast, actual consent UI, real identity/key service, enterprise resource semantics, durable/distributed recovery, facility evidence and qualified legal applicability remain open.

Prompt for an independent reviewer: verify every short extract in context; attack tenant/session/agent/resource binding and credential audience/scope; change approved arguments, reviewer eligibility, policy and resource versions; test replay and concurrent duplicate execution; inspect audit failure before and after downstream side effects, durable recovery and unknown outcomes; verify the complete physical boundary without scores masking conflicts; inspect the deployed chapter/diagram and accessible approval presentation. Report reproducible defects, target environment and any conclusion not established by this synthetic fixture.
