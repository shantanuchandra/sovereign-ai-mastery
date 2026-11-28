# Module 13 lab: measure local inference tuning

**Educational draft.** Run real CPU generation with one and two intra-operation threads, keeping model, template, dtype and cases fixed. This is inference tuning, not quantization, LoRA training, service load testing or production approval. Use only the course's eight synthetic prompts, four English and four Arabic. Independent, qualified language/domain and production reviews remain pending.

## Environment, preparation and cost

Python 3.13; direct dependencies in `requirements.txt` pin torch 2.9.1 and Transformers 4.57.3. Transitive packages/OS remain variable. The runner accepts the same torch public version with packaging suffixes such as `+cpu`, preserving the full observed string. CPU only; no Metal, CUDA, Docker or running Ollama service. Apple Silicon M4 Pro/16 GB is the teaching target, not a minimum-memory guarantee. Plan roughly 1 GB plus installer caches and working memory. No paid resource or credentials are required.

From the repository root, prepare a fresh environment and pinned public artifacts:

```bash
python3.13 -m venv /tmp/sovereign-model13-env
/tmp/sovereign-model13-env/bin/pip install -r labs/module-13/requirements.txt
/tmp/sovereign-model13-env/bin/python labs/module-11/prepare.py /tmp/sovereign-model13-artifacts
/tmp/sovereign-model13-env/bin/python labs/module-13/run_tuning.py /tmp/sovereign-model13-artifacts /tmp/model13-observation.json
python3 labs/module-13/experiment.py /tmp/model13-observation.json
python3 -m unittest discover -s labs/module-13 -p 'test_*.py' -v
```

Preparation is **online**. The reused Module 11 preparation script obtains nine allowlisted files for `HuggingFaceTB/SmolLM2-135M-Instruct` revision `12fd25f77366fa6b3b4b768ec3050bf629380bac`, retaining a manifest. Existing verified Module 11 artifacts may be reused. No weights are committed. The pinned card declares Apache-2.0 and links its full terms; there is no separate LICENSE file in that revision's inventory. Intended-use/redistribution rights require separate review. Hash consistency is not independent publisher authenticity.

## Experiment procedure and data flow

The parent validates the model/revision/inventory and hashes before launching two bounded subprocesses, one for each thread count. Each child verifies the bundle again, loads safetensors locally with `trust_remote_code=False`, configures threads before model work and uses offline library options. Python `connect`, `create_connection` and `getaddrinfo` are denied. This guards this Python path, not native/OS/other-process behavior or physical isolation.

Each child warms up once on the first case, then measures all eight cases three times. Settings remain float32 CPU, greedy generation, enabled KV cache and at most 24 new tokens. Time covers `model.generate` only, after tokenization; load times are recorded separately. Raw decoded continuations exclude the prompt. Results include artifact/case hashes, runtime/platform, settings, 48 rows and raw-derived summaries. All prompts/outputs are synthetic local artifacts. There is no inference API, remote fallback, external judge, tracker or training.

The fixed order is one-thread then two-thread, without counterbalancing. Single-machine variability, warm-up adequacy, thermal effects, background activity and order confounding remain. Repeats are executions, not independent task examples. No confidence interval, production p95, time-to-first-token, user-level latency, peak memory, energy, quantization or multi-user throughput is measured.

For a real physical-site-only deployment include raw/cleaned training data, OCR/speech, embeddings, checkpoints/adapters, activation/update, telemetry, diagnostics, backups, remote support and failover in the same policy. This experiment does not test those paths. Prepare/inspect packages and artifacts on authorized staging before controlled media transfer; a successful local command cannot demonstrate a physical air gap.

## Actual retained observation

`observed-local-run.json` started at 2026-11-27 19:03:41 UTC, which is 28 November 2026 00:33:41 in Asia/Kolkata. Platform: macOS arm64, Python 3.13.9, torch 2.9.1, Transformers 4.57.3. The observed run used the pinned actual public model.

| Profile | Measured generations | Median generation seconds | Distinct English literal passes | Distinct Arabic literal passes |
|---|---:|---:|---:|---:|
| One CPU thread | 24 | 0.449638 | 0/4 | 0/4 |
| Two CPU threads | 24 | 0.4364415 | 0/4 | 0/4 |

Each language has 12 repeated measurements per profile, all failing the literal criterion. The denominator for distinct examples remains four. Normalization uses Unicode NFKC, case folding and whitespace collapse; punctuation, explanations and substrings get no automatic credit. Some English responses contain correct content plus prose; a format failure is not necessarily a factual error. Qualified Arabic/semantic review is NOT COMPLETED. Repeated outputs were preserved rather than replaced by invented favourable labels.

Aggregate generated token rates are retained as total generated tokens divided by total measured generation seconds. They are descriptive local statistics with varying response lengths, not endpoint load capacity or an established causal improvement. The observed two-thread median was smaller; that cannot authorize a profile that fails the fictional task-quality gate.

## Verification and failure exercises

The standalone checker recomputes summaries and requires the exact case/profile/repeat matrix, case content/hash, fixed settings, runtime, nine artifact hashes, finite timing and educational status. It checks internal consistency, not forensic authenticity of a hand-edited record or physical facilities.

| Mutation | Expected outcome |
|---|---|
| Modify an acquired model artifact | Digest mismatch before model load |
| Change model revision/inventory | Reject the bundle |
| Remove Arabic rows or duplicate a row | Reject incomplete/duplicate matrix |
| Invent a better summary without changing rows | Reject raw-summary mismatch |
| Insert NaN, negative duration or too many tokens | Reject malformed evidence |
| Call an output “APPROVED” or the guard “physical air gap” | Reject unsupported status/scope |
| Run with an existing evidence path | Refuse overwrite; choose a fresh path |
| Package/model unavailable | Keep error; mark NOT COMPLETED; no fabricated output |

`experiment.decide` is a separate course-authored **declaration** exercise. The fictional BANK-A policy requires its named site, no network/remote operator, rights/data/quality reviews, rollback evidence and perfect literal outputs in each present language/profile. Known conflicts or observed criterion failures yield BLOCKED; absent evidence yields UNVERIFIED; favourable declarations yield REVIEW_REQUIRED only. It does not discover sites, authenticate reviewers or replace the strict complete-record validator. Unit tests use invented favourable rows only to test branches; the retained actual observation remains unchanged.

## Acceptance, extension and cleanup

Acceptance means the real experiment produced inspectable complete evidence, including failed quality. Keep a copy under a new path for each run and compare raw outputs/settings before drawing conclusions. Do not claim a deployment, safety or rights acceptance from completion.

Optional extension: measure a supported quantization recipe on the actual target hardware with the same held-out cases and a new artifact identity. Optional cloud LoRA is **NOT PERFORMED**: define approved data/site/operator paths, intended-use review, budget cap, stopping rule and deletion/checkpoint plan before provisioning anything. No cloud resources were created by this lab.

After retaining evidence, remove only task-owned temporary environment/artifact/result paths that you have inspected. Do not delete shared caches or pre-existing models automatically. Complete the distinct [PM memo](TRADEOFF_MEMO.md), then return to [Module 13](../../chapters/13-fine-tuning-optimization-evaluation.md).
