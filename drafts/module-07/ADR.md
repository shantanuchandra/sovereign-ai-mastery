# Module 07 architecture decision record

Development draft, 25 November 2026. Course-authored template for a fictional workload; no production approval.

## Decision identity

Record ID, version, date, accountable owner, implementing owner, validator, expiry and review trigger. Reuse the Module 06 risk/control identifiers rather than creating an unrelated evidence inventory.

## Workload and constraints

Specify users, intended use, prohibited actions, protected artifacts and derivatives. State the exact physical site/country boundary and connectivity rule. Include prompts, weights, embeddings, speech/OCR intermediates, logs, diagnostics, telemetry, backups, support artifacts, activation, update media and recovery copies. Identify legal questions still awaiting qualified review.

## Options and hard gates

| Option | Physical/control paths | Known conflicts | Evidence gaps | Decision |
|---|---|---|---|---|
| Factory-local advisory assistant | Fill with node/edge IDs | List unchanged-rule violations | List owners/tests | Conditional |
| Domestic managed alternative | Include admin, telemetry and recovery | Test against factory-only rule | Do not infer residency from a product name | Conditional |
| Manual lookup fallback | Define existing process and limits | Assess its own risks | Record usability/continuity evidence | Conditional |

Reject known hard conflicts before comparing cost, performance, usability or operating burden. Do not average a veto into a weighted score. If proposing a policy change, record it as a separate decision with authority and consequences.

## Architecture and evidence

Attach editable Mermaid, a static diagram and a plain-language path walkthrough. For each plane, identify owner, zone, site, privileged access and dependency. For each lifecycle edge, identify purpose, artifacts, source/destination, transport, authorization, test, result, build and evidence reference. The diagram is an index into evidence, not a substitute for it.

## Trade-offs and consequences

State what becomes harder: on-site recovery capacity, offline updates, qualified operators, latency, throughput, capital cost or vendor substitution. Use dated inputs for real estimates and label invented planning inputs. Explain which single changed assumption could reverse the option choice.

## Validation and bounded closure

Record adverse observations separately from missing evidence. Assign containment, repair and dated retest to owners. State which component/use changes invalidate the result. Require human review of residual uncertainty after favorable tests; retain manual fallback and incident escalation. Do not assert certification or compliance from the synthetic graph validator.

## Illustrative marking rubric, 20 points

Boundary and intended use (4); all four planes plus privileged paths (4); lifecycle/evidence traceability (6); alternatives and economics with assumptions (3); bounded decision, owner and change trigger (3). Hard-boundary overrides or invented evidence require remediation regardless of score. This is a course rubric, not an external qualification.
