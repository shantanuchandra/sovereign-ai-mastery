# Module 11 lab: a real local model with bounded evaluation

**Educational draft.** This exercise uses a small public English-first model and eight course-authored synthetic prompts, four English and four Arabic. These cases test literal outputs on a tiny sample. They are not a benchmark, authentication test, safety assessment or production Arabic evaluation. No real customer data or paid resource is used.

## Setup and cost

Use Python 3.13 on Apple Silicon or a compatible Linux CPU. The default uses CPU, two threads, float32, greedy generation and at most 24 new tokens per case. No CUDA, Metal, Docker or running Ollama service is required. Allow roughly 1 GB plus installer caches, network download time and free working memory; this is a planning allowance, not a measured maximum. The course baseline is M4 Pro/16 GB, but consult the [observed evidence](observed-local-run.json) for the actual platform. The two direct dependencies are pinned; transitive packages and OS can still differ.

From the repository root:

```bash
python3.13 -m venv /tmp/sovereign-model11-env
/tmp/sovereign-model11-env/bin/pip install -r labs/module-11/requirements.txt
/tmp/sovereign-model11-env/bin/python labs/module-11/prepare.py /tmp/sovereign-model11-artifacts
/tmp/sovereign-model11-env/bin/python labs/module-11/run_local.py /tmp/sovereign-model11-artifacts /tmp/model11-observation.json
python3 -m unittest discover -s labs/module-11 -p 'test_*.py' -v
```

`prepare.py` is online. It downloads nine allowlisted files from `HuggingFaceTB/SmolLM2-135M-Instruct`, full commit `12fd25f77366fa6b3b4b768ec3050bf629380bac`, without credentials. The model card declares Apache-2.0 and links the full licence; there is no separate LICENSE file in this revision's inventory. Inspect both the archived card and https://www.apache.org/licenses/LICENSE-2.0 for the intended use. A model-card declaration is not counsel approval. No weight files are committed or redistributed here. The eight prompts and expected labels in `cases.json` are course-authored synthetic data.

The program refuses a nonempty destination and produces `manifest.json`. Do not replace the acquired manifest after editing artifacts and then claim the original build was verified. Its SHA-256 values detect changes against that reference; they do not independently authenticate the publisher. Retain trusted acquisition evidence and review the supplier and dependency chain separately.

## Local evaluation and data flow

The second program verifies the exact file inventory and hashes before loading. It enables library offline options, local-file-only loading, safetensors and `trust_remote_code=False`. It denies Python `connect`, `create_connection` and `getaddrinfo` calls for the model run. This is a process-level guard, not a physical air gap or OS packet capture. Native-library, other-process, OS and supply-chain behavior remain separate review tasks. Prepare packages/model artifacts in an authorized connected staging environment before transferring them into a genuinely disconnected facility.

All prompts, tokens, outputs, temporary inference state and result JSON remain process/local-file artifacts under the stated workflow. No API or fallback endpoint is configured. This workflow does not test OCR, speech, embeddings, telemetry, update/activation, backup, remote support or recovery services; an enterprise must keep each protected path within its rule and test them separately. Do not infer those controls from a successful generation call.

The output contains the full artifact hash inventory, exact revision, platform/runtime, template-mediated input token counts, generated token counts, settings, load and individual generation times, raw outputs and exact-match counts by language. The input prompt is excluded from each decoded continuation. A generation time is elapsed local generation, not request latency at load, time-to-first-token or production p95.

## Observed local run, 27 November 2026

The retained Apple Silicon CPU run produced eight nonempty continuations: English 0/4 and Arabic 0/4 under the strict normalized exact-label rule. The English capital and arithmetic outputs included correct content plus extra words, so their literal failures are formatting failures rather than evidence of incorrect facts. Other responses require separate semantic/language interpretation. Arabic outputs did not meet the expected labels; qualified Arabic/domain assessment remains NOT COMPLETED. Raw outputs, build, settings and timings are retained; Q6 uses a different explicitly fictional result.

## Interpret results

Normalization applies Unicode NFKC, case folding and whitespace collapse. Punctuation, explanations and substring matches receive no automatic credit. A correct answer plus extra text can fail a literal-output contract without demonstrating a factual error. Inspect raw responses and have a qualified person separate format, semantic, language and task failures. The expected label is a test specification, not a claim about how every valid response must be written.

The experiment completes when all eight cases have inspectable outputs, settings and counts, even if quality fails. The fictional candidate policy in `evaluate.py` separately requires 100% exact match in each language, a BANK-A site, no network or remote operator, a declared positive licence review, provenance and a matching evaluated build. This deliberately strict teaching criterion has four examples per language and no statistical generalization. Its strongest favourable result is REVIEW_REQUIRED, never PASS or accepted. It checks declarations; it does not discover sites, enforce licences or validate reviewer authority.

```bash
python3 labs/module-11/evaluate.py labs/module-11/candidate.json
```

The fixture is invented and demonstrates a favourable declaration requiring review. Real raw model observations remain in `observed-local-run.json`; the fixture does not replace those results. Known site/network/operator/licence conflicts dominate gaps, missing language denominators remain UNVERIFIED, observed language failure blocks this fictional policy, and mismatched builds cannot be relied on.

## Failure recovery and mutation exercise

| Mutation or symptom | Check | Expected bounded result |
|---|---|---|
| Change an artifact after preparation | Run local loader | Reject digest mismatch before model load |
| Change model/revision/file inventory | Run local loader | Reject unexpected manifest |
| Missing model file | Verify manifest | Error, no remote fallback |
| Existing output evidence path | Run local loader | Refuse overwrite; select a new path |
| Four English cases only | Evaluate candidate | Arabic denominator missing, UNVERIFIED |
| Off-site candidate plus missing rights | Evaluate candidate | BLOCKED retains location conflict |
| Arabic format failure | Inspect raw result | Exact failure; semantic cause needs review |
| Installer/download unavailable | Keep failure log | NOT COMPLETED, no fabricated result |

For a fresh run choose a new empty artifact directory and new result path. No external account or resource requires teardown. Delete only the task-owned `/tmp/sovereign-model11-env`, `/tmp/sovereign-model11-artifacts` and chosen output after retaining wanted evidence; inspect names before deletion. The course does not automatically remove shared caches or a user's existing models.

## Acceptance and extension

Record the real run, all eight denominators, failures, runtime and artifact identity. Keep the study-experiment completion separate from bank acceptance. Add at least one dialect/code-switching and one adverse refusal case only after specifying the expected behavior and competent review. Do not relabel this English-first model as Arabic-ready from its ability to tokenize Arabic.

Complete the distinct [model-choice matrix](MODEL_MATRIX.md), then return to [Module 11](../../chapters/11-sovereign-models-model-strategy.md). Module 12 will add retrieval; this lab performs no training or RAG.
