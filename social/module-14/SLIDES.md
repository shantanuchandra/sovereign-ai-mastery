# Eight questions before an agent acts

Educational draft. Synthetic ticket tools; no actual enterprise deployment. Sources checked 28 November 2026; full references and short quotes are in the chapter.

## 1. Does a proposed tool call carry authority?

A model can propose closing a ticket. The application must independently establish who may close which tenant’s record.

Decision: Validate the action before calling the tool.

Source/scope: Course-authored synthetic ticket scenario.

## 2. What changes when a workflow becomes an agent?

The next step may become model-selected. User delegation, tool permissions and operating boundaries still need enforcement.

Decision: Bound steps, retries, time and permitted tools.

Source/scope: Anthropic, Building effective agents, 19 Dec 2024; checked 28 Nov 2026.

## 3. Would one administrator token serve every tenant?

A generic credential can erase the user and tenant boundary. Separate user, agent and downstream service identities.

Decision: Check audience, scope, tenant and resource.

Source/scope: OWASP LLM06:2025; RFC 9700 section 2.3; checked 28 Nov 2026.

## 4. Does approval for A-1 also approve B-1?

Bind consent to the exact action, actor, tenant, resource version and policy. Recheck expiry and consume the grant once.

Decision: Changed context requires a fresh decision.

Source/scope: Course approval design; synthetic tamper, expiry and replay tests.

## 5. Does return control mean approved execution?

The real Bedrock interface returns proposed invocation context to the application. Human consent and permissions need separate controls.

Decision: An invocation ID is not a deployment approval.

Source/scope: AWS Bedrock return-control guide; checked 28 Nov 2026.

## 6. Should a timed-out write be repeated?

The write may have completed while its response was lost. Preserve the request identity and reconcile the authoritative record.

Decision: Keep an unknown outcome until evidence resolves it.

Source/scope: Course distributed-failure analysis; no external write tested.

## 7. Can external diagnostics preserve this site rule?

BANK-A’s fictional rule covers prompts, traces, support, updates and recovery. A protected external path remains a conflict.

Decision: No quality score overrides the unchanged boundary.

Source/scope: Physical-site-only scenario; no legal or facility assurance claim.

## 8. What did the gate exercise actually prove?

Synthetic permission, exact-action approval and replay checks ran against memory tools. Real IAM, durable recovery and site isolation remain open.

Decision: Carry the test record and unresolved owners into review.

Source/scope: Educational draft; independent and manual accessibility review pending.
