# Optimization trade-off memo and evaluation plan

**Reusable educational template, not an enterprise approval.** Complete with synthetic/public or approved information only. Author publication does not establish independent review. A score never overrides a hard conflict.

## Decision and failure diagnosis

- Workload, affected users, languages/varieties and sector consequences:
- Decision owner, date and exact physical/data/operator rule:
- Observed failure with raw-output references and expected behavior:
- Confirmed cause versus competing hypotheses requiring tests:
- Baseline build, template, retrieval/data revision and existing approvals:

## Alternatives and admissibility

| Alternative | Failure it might address | Hard conflicts / unresolved evidence | Bounded next experiment |
|---|---|---|---|
| Prompt/template or parser | Instruction/format | Schema compatibility and held-out regressions | Freeze cases; change one instruction |
| RAG correction | Missing/current authorized information | Tenant/ACL, reranker/embedding and cache paths | Inspect retrieval and grounding separately |
| Local LoRA candidate | Repeated approved task behavior | Data/rights, compatible base/adapter, training lifecycle | Approved split and reproducible recipe |
| Local serving change | Measured runtime bottleneck | Hardware/method support, quality and rollback | Controlled profile comparison |
| External alternative | Only if expressly authorized | Premises-only rule blocks it unchanged | Requirement review; never silent fallback |

Choose an eligible experiment and state what result would reverse the recommendation. All rows are decision prompts, not claims of measured effectiveness.

## Evaluation contract before execution

| Item | Required declaration |
|---|---|
| Dataset | Provenance, permissions, annotation, deduplication/leakage unit, train/dev/test IDs and cutoff |
| Coverage | Task, English, Arabic varieties, code-switching, sector/adverse slices and missing coverage |
| Quality | Exact versus semantic rubric, abstention, critical failures, reviewer qualification/adjudication |
| Performance | Clock, context/output lengths, load/concurrency, warm/cold, repetitions and variability |
| Build | Base/adapter, hashes, tokenizer/template, runtime, hardware, settings and script revision |
| Experiment | Single intervention, baseline, profile order/counterbalancing, stopping rule and raw evidence |
| Boundary | Training/evaluation/tracker/derivatives, OCR/speech/embeddings, logs, activation/update/support, backup/failover |
| Deployment | Canary scope, predecessor, rollback trigger, tested recovery and accountable operator |

Thresholds and example counts are product choices justified by risk, not official course standards. Missing critical slices stay missing. A repeated case does not add independent sample coverage.

## Worked bounded disposition from this lab

Actual 28 November local CPU observation: 8 synthetic cases ×3 repeats ×2 profiles =48 generations. One-thread median0.449638s; two-thread0.4364415s. Both profiles fail literal output on four English and four Arabic examples. Lower observed median alone does not establish a reproducible speedup, production capacity or suitability. Recommendation: retain both as experimental evidence; withhold BANK-A task release; investigate format versus semantic/language failure. Qualified review and representative/adverse tests remain open. No training, quantization, energy or memory improvement was measured.

## Economics and operational owners

Compute total cost per acceptable completed task, including fixed operations, attempts/retries, review, annotation, experimentation, idle capacity, revalidation and incident/rollback work. Declare invented assumptions separately from prices and actual measurements. Show sensitivity to completion rate, traffic and staffing. If zero acceptable completions were observed, do not invent a successful-task denominator.

| Gate / evidence | Owner role | Due / retest date | State and next action |
|---|---|---|---|
| Task specification and failure labels | Product + domain specialist | Fill | OPEN |
| Dataset permissions and intended use | Data steward + counsel | Fill | OPEN |
| Arabic/sector evaluation | Qualified language/domain reviewers | Fill | OPEN |
| Build and controlled experiment | Model engineering | Fill | OPEN |
| Complete lifecycle boundary | Security + platform | Fill | OPEN |
| Capacity, canary and rollback | Platform service owner | Fill | OPEN |
| Final bounded release decision | Accountable product/service owner | Fill | OPEN |

Closure rule: any known hard conflict or failed critical criterion blocks release; missing required evidence stays UNVERIFIED. Favourable evidence goes to human review. Record residual risks, scope and revalidation triggers after data/build/threshold changes.

## Learning rubric, 20 points

Award four points each for (1) evidence-led diagnosis/alternatives, (2) admissibility and full lifecycle, (3) reproducible/slice-aware evaluation, (4) actual results/economics with honest limits, and (5) accountable rollout/rollback/retest. Suggested learning threshold12/20. Any concealed hard conflict, fabricated result or substituted aggregate requires revision regardless of score. This is a PM artifact distinct from the generation lab and separate knowledge-check assessment.
