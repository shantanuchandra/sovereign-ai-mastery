# Module 06 lab: challenge a governance register

**Educational simulation; no production approval.** Use public code and synthetic case records to calculate subgroup errors, inspect versioned control evidence and triage a release. Return to [Module 06](../../chapters/06-governance-responsible-ai-risk.md) or [Architecture Studio](../../learning/index.html).

## Environment, time and boundaries

Python 3.11+ and its standard library; CPU only, no model, Docker, GPU or account. Allow 60–90 minutes. Compatible with the Apple Silicon/16 GB baseline; verified here with Python 3.14 on macOS. No paid service or network call is used by the evaluator. Downloading the public repository is the preparation stage; evaluation can then run offline. No cloud extension, resource creation or cleanup bill is required. Do not replace fixtures with personal or customer data.

## Procedure

From the repository root:

```bash
python3 labs/module-06/evaluate.py labs/module-06/cases.json > /tmp/module06-results.json
python3 -m unittest discover -s labs/module-06 -p 'test_*.py' -v
```

1. Read the `review-ready` case. Identify intended use, named roles and the four controls. Favorable declarations still require human review.
2. Recalculate each language's errors/count and the weighted aggregate in `aggregate-masks-arabic`. Explain why the denominator matters.
3. Compare `diagnostics-offsite`, `airgap-activation` and `missing-backup`. Separate an observed conflict from an undocumented route.
4. Inspect `stale-build`, `self-validation`, `open-incident` and `machine-control-creep`. Map each to a charter rule and owner.
5. Copy a case into a new JSON array outside the canonical manifest. Propose a repair, retain the old evidence and add the new build, date and observation. Re-run the evaluator; write what it still cannot establish.

## Input and course rules

Each case declares a physical `site`, `country`, boundary (`country`, `premises`, `airgap`), build ID, intended/allowed uses, responsible/validator/accountable people, incident state, control evidence, subgroup counts and nine lifecycle routes. Routes include inference, training, embeddings, speech/OCR, diagnostics, telemetry, backup, support/activation and failover. Include prompts, outputs, weights, vectors, logs, update media and recovery artifacts in those declarations as appropriate. A false declaration can fool this lab; real evidence must inspect the actual routes and operations.

For air gap, `network: true` on any declared route is a known conflict. For premises, a different physical site is a conflict even in the same country. Controlled offline media and update procedures need separate real inspection. Missing routes remain unverified, never implicitly local.

The fixture's 10% group error limit, 10 percentage-point disparity limit, minimum group size of 20 and maximum evidence age of 30 days are **course-authored examples**. Criteria are explicit inputs, not fixed NIST/ISO/statutory rules. These simple counts do not estimate statistical confidence or settle fairness. The declared `review_date` is the reproducible reference date; dates after it or more than 30 days before it are gaps. In real use the review date must be authenticated as part of the decision record.

Controls need a recognized ID, outcome, current build, test ID, evidence pointer, matching named validator and date. The program does not open or authenticate the evidence pointer. Changed use and an open incident block. Missing/malformed evidence and role conflicts create gaps. Known conflicts outrank gaps. Extra risk-acceptance prose cannot override them.

## Expected evidence and acceptance

The 16 fixture statuses are recorded as `expected_status` for regression checking, not as instructions to the evaluator. There are 2 `REVIEW_REQUIRED`, 7 `UNVERIFIED` and 7 `BLOCKED` cases. Verify the counts from output rather than treating this guide as the test oracle. No state means certified, compliant, fair or production-safe.

Submit the output, your hand calculation, a four-row risk register, one proposed repair/retest and a bounded decision note. Each row needs affected users, cause, control, owner, versioned evidence, open action and review date. Explain at least one limitation of the measurement and one of the physical-boundary declarations.

## Troubleshooting and extension

An import error usually means the test discovery path or Python environment is wrong. A failed fixture assertion should trigger comparison with the exact input; do not change expected results to conceal a defect. Missing build or provenance should remain an evidence gap even when numerical quality improves.

Optional local extension: add dialect and task-family cohorts, document sample selection and test whether one overlap can distort an aggregate. Keep groups disjoint if calculating a population aggregate. Do not claim this extension constitutes a full fairness audit. The current evaluator assumes supplied groups partition the evaluated population; it cannot infer overlap from counts.
