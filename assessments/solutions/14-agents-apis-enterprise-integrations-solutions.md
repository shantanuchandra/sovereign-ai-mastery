# Module 14 solutions and PM rubric

**Instructor/source answer key; excluded from the public reader build.** Educational draft; independent assessment pending. BANK-A and adverse event are fictional. Source review 2026-11-28.

## Q1. Execution architecture

Assistant names an interface role. Workflow follows programmed transitions; agent lets a model choose intermediate process/tool steps. The Anthropic source uses that architectural distinction, not an assurance level. Authorization must remain independently enforced at invocation for every origin of a proposal. A fixed workflow can still issue an unauthorized write; an agent cannot safely authorize itself.

## Q2. Three separate checks

A gateway token targets a model interface and does not establish permission on a ticket-service resource. Read permission does not imply close permission. A conversation sentence is untrusted content, not eligible reviewer consent. Require trusted identity/delegation, current downstream audience/scope/resource/tenant checks and a bound approval where required. See RFC 9700 section 2.3 and OWASP complete mediation in chapter references.

## Q3. Exact proposal and current context

Bind tenant, user, agent, tool/version, resource/version, parameters, request ID and policy revision. Grant adds eligible reviewer, expiry, identifier and authentication/integrity. Reject changed context, expired grant, revoked reviewer/credential/delegation, spent grant and duplicate request; do not merely re-sign the changed action without a fresh decision. The lab records tool name/policy but has one fixed implementation version; a production tool version also needs binding/review.

## Q4. Lost response

Use UNKNOWN_OUTCOME after an ambiguous downstream timeout. Preserve the original identity and intent record, inspect authoritative status and reconcile before retrying. A local log, queue acknowledgment or process lock cannot prove an external write did not occur. Durable idempotency, concurrency and reconciliation are separate target-system contracts. Stop additional high-impact actions if status cannot be established.

## Q5. Worked real-interface answer

AWS documents returning proposed invocation details in `invocationInputs` with a unique `invocationId`, and supplying results in a later InvokeAgent request using the matching invocation context. That supports an application fulfillment boundary. It does not state that enabling the mode verifies a human approver, enforces a tenant's authorization or physically moves the managed service to BANK-A.

The fictional bank must retain its unchanged site/offline rule. Require actual complete flow/placement evidence, eligible local execution infrastructure, user/agent identity and downstream permission tests, consent binding/replay/expiry tests, and audit/update/support/recovery evidence. An external managed dependency conflicts if it processes protected artifacts outside BANK-A. Only an explicit policy change by accountable authorities could widen eligibility; a good score or returned invocation ID cannot do so.

Primary source: Amazon Web Services, *Return control to the agent developer by sending elicited information in an InvokeAgent response*, introduction and invocation-results flow, https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html. Verified 2026-11-28. Provider interface documentation; no AWS service or actual bank deployment tested.

## Q6. Step-by-step root-cause analysis

1. **Pre-test state:** UNVERIFIED while authorization/approval evidence is missing; do not call the agent accepted.
2. **Observation:** B-1 was closed after approval for A-1. The observed cross-tenant write changes the action-control claim to BLOCKED. External diagnostics independently block the premises claim.
3. **Direct cause:** adapter treats a Boolean as sufficient approval and executes with an overprivileged identity without exact-resource/tenant authorization. A changed model proposal triggered the flaw; the model alone is not the authorization root cause.
4. **Systemic cause:** deployment review omitted independent complete mediation, scoped delegation, approval/action binding and adverse tenant/version/replay tests. A better retrieval filter cannot contain arbitrary direct tool requests.
5. **Containment:** disable affected write adapter, revoke overbroad credentials and pending grants, preserve redacted evidence, inspect authoritative records across affected tenants and reconcile/restore B-1 through the approved enterprise process. Stop diagnostic export pending incident/privacy review. Do not blindly issue a compensating write without current authority.
6. **Remediation and owners:** enterprise application owner implements downstream tenant/resource/version checks and narrow scopes; IAM owner restores trusted delegated identity; security owner implements eligible exact-action single-use approval; operations implements local diagnostics, durable intent/results and reconciliation; product updates high-impact acceptance.
7. **Validation:** attempt changed tenant/resource/parameters/request/policy/version, foreign credentials, expired/revoked/forged grants, replay/concurrency and audit failure. Direct tool attempts must fail even if retrieval hides B-1. Confirm zero unauthorized side effects and inspect logs without secrets.
8. **Dated retest:** target 2026-11-29 on a synthetic isolated staging stack, named engineering/security owners, exact build and observed outcomes retained. An unavailable reviewer/environment means NOT COMPLETED, not a backdated pass.
9. **Residual risk and closure:** passing bounded control tests closes only their named defects after evidence review. External diagnostics keep the premises design BLOCKED; real IAM/durable/disaster-recovery gaps stay UNVERIFIED. Independent production approval remains open. No aggregate score can close a known conflict.

## Lab verification

Run `python3 -m unittest discover -s labs/module-14 -p 'test_*.py' -v`: 44 tests. Run `python3 labs/module-14/gated_agent.py`: four attempted cases, outcomes DENIED/COMPLETED/DENIED/DENIED, exactly one tool call. Approval and replay reason codes can reflect the first failed guard (for example stale resource before spent grant); tests also directly cover spent-grant rejection. Grant IDs/ephemeral keys vary, so compare semantic outcomes rather than byte equality.

Audit has APPROVED, AUTHORIZED, COMPLETED and DENIED records. AUTHORIZED is intent, not success; a missing result must not be inferred completed. Favorable boundary is DECLARED_ONLY. Each external protected-artifact mutation is BLOCKED; missing fields UNVERIFIED. Standard-library fixture proves neither OAuth correctness nor physical isolation or durable distributed behavior.

## Scenario comparison and PM scoring

For BANK-A, prefer an eligible local workflow initially: narrow tools, local trusted IAM/reviewer service, no prohibited external logging or fallback, declared bounds and independently tested recovery. A bounded agent can change evidence-collection flexibility without widening authority. The second organization's expressly wider policy may permit a reviewed managed orchestrator, but still needs real permissions, terms, destinations and evidence; it cannot reuse BANK-A's result.

Score the PM artifact 0–4 on each of scoped identity, exact authorization, approval lifecycle, durable audit/reconciliation and complete operating boundary, total 20. Require owners, adverse tests, observed/declared distinction and target retest. The suggested 15-point educational threshold requests review, never overrides hard exclusions. A strong answer recommends a bounded disposition and identifies what would change it rather than inventing completed approvals.

## Assessment scoring

Total 40 points: Q1–Q4 four points each (16), Q5 six, Q6 ten, and scenario challenge eight. Award reasoning, testable evidence and bounded decisions, not product-name recall. The separate PM artifact rubric remains 20 points. Hard conflicts and unresolved high-impact failures prevent a go-live recommendation regardless of aggregate score.
