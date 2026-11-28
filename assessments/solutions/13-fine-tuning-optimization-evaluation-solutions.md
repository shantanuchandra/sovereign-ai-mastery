# Module 13 solutions and assessment rubric

**Instructor/source artifact.** Excluded from the public learner build. Same-author worked answers, not independent assessment. The factual product example is distinct from the hypothetical bank and Q6's fictional observations. No score overrides a hard constraint or missing approval.

## Q1. Diagnose before choosing adaptation

First verify that the correct, current, authorized source is indexed, retrievable under the caller's identity and present in the actual model context. Inspect document/version, parsing/chunk boundaries, retrieval/reranking, permissions and assembled prompt. A model fine-tune is not the first causal experiment for evidence that never reached inference. If authorized context is correct and the same cases still fail, investigate template, format, reasoning or task suitability with controlled comparisons. More than one cause can coexist.

**Five points:** two for targeting missing context, one for identity/version, one for inspectable controlled evidence and one for a stated condition that changes the intervention.

## Q2. Adapter dependency and memory scope

Keep base model/revision and rights disposition, adapter weights/configuration, target modules/rank/scaling, tokenizer/template, dataset/splits, training settings/checkpoints, runtime/hardware and held-out results. Retain a reproducible load/merge procedure and rollback predecessor. LoRA's frozen-base low-rank updates reduce the trainable parameter set in its mechanism; this does not remove base weights, activations, gradients/optimizer state or runtime overhead. It provides no independent permissions, privacy or task guarantee. A merged result needs a new build identity and evaluation.

**Five points:** two for complete compatible artifact, one for training/data evidence, one for memory components and one for rights/quality limits.

## Q3. Define what was measured

The real lab measures elapsed local `generate` time after tokenization, excluding load, network and queueing. It retains load separately, input/generated tokens, raw continuation, model files/revision, runtime/hardware, thread count, float32, greedy policy, cache, cap of 24, warm-up and repeats. There are eight unique cases and 24 measurements per profile, not 24 independent examples. One then two threads is not counterbalanced; thermal/order/background effects may contribute.

The observed median difference does not establish a causal or general speedup. It is not time-to-first-token, production p95, service throughput at concurrency, peak memory or energy. Both profiles fail the literal criterion; a faster failed task is not release-eligible. Repeat target-service tests under stated context/output length/load before operational claims.

**Five points:** one each for clock, controlled build/settings, unique-versus-repeated denominators, performance limits and quality gating.

## Q4. Arabic sample coverage and reviewer responsibility

Four unique examples repeated three times remain four examples. Preserve both unique-case coverage and twelve measurement counts, grouped by profile. No unsupported confidence or representative-language claim follows. Add independently designed examples for the intended varieties, code-switching, terminology, names/numerals, negation, correct abstention and adverse sector consequences. Split by document/conversation leakage unit, preserve a held-out set and document annotation disagreement.

Qualified Arabic/domain specialists must assess semantic appropriateness and risk; product defines task consequences, engineering binds results to the exact build, and security reviews any external annotation/judging path. Literal-output failures need interpretation: helpful prose may violate schema without a false fact. A generic model judge does not replace this competence or authorize off-site data use.

**Five points:** one each for correct denominator, relevant slices, held-out/leakage method, qualified roles and literal/semantic distinction.

## Q5. Real documentation, hypothetical deployment

**Source-backed:** Hugging Face's *Transformers 4.57.3 Quantization overview*, introduction and method/hardware table, explains lower-precision weight storage and differing support. Verified 28 November 2026: https://huggingface.co/docs/transformers/v4.57.3/en/quantization/overview. This is original product documentation, not an independent hardware evaluation. The fictional BANK-A proposal is not a real reported incident.

Check exact method/library/version, CPU architecture and backend compatibility, model layers, serialization/loading and needed calibration before selecting a recipe. Reject an unsupported recipe rather than silently switching to a remote GPU. On the approved actual host, compare the verified baseline and new artifact using held-out task/safety/language slices, elapsed service clocks, real peak memory, load/response lengths and recovery. Smaller serialized weights alone measure neither process memory nor acceptable answers nor energy.

A supported, locally reproducible candidate with acceptable critical slices, measured target-host performance/capacity, rights and rollback evidence could justify human review. The unchanged site rule still blocks external training/judging/fallback; changed authorization must be explicit. This lab has performed inference-thread tuning, not a quantized experiment.

**Five points:** one for accurate source/scope, one for compatibility, one for controlled measurement, one for quality/memory distinction and one for conditional evidence/unchanged boundary.

## Q6. Step-by-step evidence-state and root-cause analysis

1. **Before:** UNVERIFIED, because critical Arabic, rights and rollback evidence is missing. No favourable score or presumed licence closes it.
2. **Observation:** the hypothetical experiment reports English 95/100 and Arabic 3/10 plus shorter median generation. These are adverse subgroup evidence under a defined criterion, not the real lab's output. Verify raw data, labels, version, denominator and measurement clock; missing raw baseline prevents a reliable comparative gain claim.
3. **After:** if the declared Arabic acceptance criterion fails, the candidate is BLOCKED for release; intended-use/rollback gaps remain separately recorded. A proposed prohibited external judge/fallback adds an explicit boundary conflict. If a criterion had never been set, retain the observed adverse result and UNVERIFIED acceptance until the owner defines and evaluates the contract; do not invent a retrospective threshold to pass.
4. **Direct confirmed problems:** reported Arabic result is weak for the stated purpose; comparison provenance and base/adapter mapping are missing; repeats are being misrepresented as independent coverage. The proposed external path conflicts with the given rule. These observations do not establish that low rank, quantization, model architecture or a particular training example caused the errors.
5. **Hypotheses to test:** Arabic/dialect data mismatch, label or annotation defects, tokenization/template/masking errors, wrong base/adapter compatibility, training contamination/overfitting, and a literal scorer rejecting semantically valid outputs. Reconstruct and freeze a baseline, correct one hypothesis at a time and preserve failed runs. Check retrieval separately where source availability matters.
6. **Systemic gaps:** absent experiment registry/version binding, inadequate subgroup release gates, missing data/rights review and pressure to substitute aggregate performance for task suitability. Product and engineering must repair the release process, not just tune another parameter.
7. **Containment:** withhold the candidate and proposed API/judge paths; preserve evidence with access/retention controls, use the prior approved service or suspend this task. Do not silently route protected content elsewhere or assert a rollback already passed.
8. **Owners/remediation:** model engineering reconstructs compatible artifacts/raw evidence and runs controlled tests; data steward verifies sources/splits/permissions; qualified Arabic/domain reviewers adjudicate failures; security validates complete data/operator/derivative paths; counsel closes scoped rights; platform rehearses rollback/restart; product owns task thresholds and the bounded decision.
9. **Retest plan:** propose 30 November 2026, not a completed test. Require frozen baseline/candidate hashes, independent Arabic examples with explicit denominators and adverse cases, authenticated review records, approved local evaluation path and demonstrated predecessor restoration. Retain raw outputs/timing/labels and identify which hypothesis each change tests. Repeat if artifacts or criteria change.
10. **Residual risk and closure:** synthetic/limited cases, population mismatch, unmeasured production load and undiscovered lifecycle paths remain. Later quality improvement removes only the demonstrated quality failure. Missing rights/rollback means UNVERIFIED deployment evidence; prohibited external paths keep BLOCKED until removed or an explicitly authorized rule changes. Complete favourable evidence goes to accountable human review, never automatic production certification.

**Fifteen points:** pre/post evidence states 2; observation/cause separation 3; tested hypotheses and systemic gap 3; containment/owners 3; dated retest 2; bounded closure/residual risk 2. Require revision for hidden external fallback, fabricated retest or claims that aggregate quality/latency authorize the bank.

## Scenario challenge and lab verification

Missing content: inspect authorized retrieval/context first. Format failure: compare explicit prompt/schema/parser before an approved adaptation trial. Latency: measure the bottleneck before changing serving settings. Each can reverse only after controlled evidence shows the suspected component is adequate and another cause remains. Preserve the premises boundary for training, evaluation, telemetry, backups and support as well as inference.

Lab verification commands:

```bash
python3 -m unittest discover -s labs/module-13 -p 'test_*.py' -v
python3 labs/module-13/experiment.py labs/module-13/observed-local-run.json
```

Expected retained observation: 48 actual generations, two profiles, 8 distinct cases; four English/four Arabic cases repeated 3 times/profile. Medians 0.449638s/0.4364415s; each language/profile 0/12 repeated literal passes, 0/4 distinct. These are actual local values, not required machine-independent timings. Reject incomplete/duplicate matrices, changed cases/summary/settings, nonfinite timing, bad hashes/runtime, false approval and scope. Manifest verification detects altered artifacts, not publisher authenticity. Python socket denial is not physical isolation. No quantization, training or paid resource was used.

**Total 40 points**; suggested learning threshold 24/40, with hard-gate misconceptions corrected regardless of points. PM memo is separate 20-point artifact; award 4 each for diagnosis/alternatives, full-lifecycle admissibility, reproducible slice evaluation, honest results/economics and rollout/rollback/owners/retest. Threshold 12/20 is educational progress, never enterprise authorization.
