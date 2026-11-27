# Module 09 compute and platform lab

**Educational draft.** Run an actual synthetic CPU HTTP service and a separate arithmetic worksheet. No model, GPU benchmark, customer data, authentication or production isolation claim is included.

## Environment and preparation

Python 3.11+ standard library; default learning target Apple Silicon with 16 GB memory. The native path needs no downloads after obtaining the course files. The container path needs an already authorized compatible local Unix-socket Docker engine on macOS/Linux and internet preparation to pull the official `python:3.13-slim` image from Docker Hub. Review applicable image/runtime/software terms; this lab does not accept terms or start a paid account. Do not provision cloud/GPU resources.

Local evidence on 27 November 2026: native Python 3.13/macOS ARM64 execution and 25 tests. The Mac's Docker engine was stopped, so local Docker/ARM64 execution is **NOT COMPLETED**. The module CI separately runs the real container exercise on Linux; inspect its matching result before claiming container verification. No Kubernetes or GPU path is tested. Allow 90 minutes.

## Native CPU path

From the repository root:

```bash
python3 labs/module-09/size.py
python3 labs/module-09/run_host.py
python3 -m unittest discover -s labs/module-09 -p 'test_*.py' -v
```

The host runner creates a loopback-only server on an ephemeral port, probes 32 requests with concurrency 1 and then 8, and shuts down that owned service. It accepts no document uploads and makes no external request. Work is a fixed 1,000-round hash calculation plus an explicitly artificial 10 ms delay. The service limits concurrent work to two requests and returns 503 when busy. It stores no request bodies or files and suppresses request logging.

The probe reports successes, errors, error rate, elapsed time, successful requests/s and nearest-rank p95 for successes only. Results vary by environment. Higher-concurrency results may include rejection; do not discard errors or claim the probe measures LLM tokens/s, real customer arrivals or a production SLA. The tests deliberately reserve admission capacity to demonstrate that health can remain 200 while work is rejected.

## Container path and bounded cleanup

```bash
python3 labs/module-09/run_container.py
```

The runner rejects explicit SSH/TCP Docker endpoints before contacting them. A Unix socket is a target-selection guard, not proof of physical residency. It resolves the official Python tag to a digest, records that digest and builds from the resolved digest. It uses a uniquely tagged owned image, non-root UID/GID 65532, a read-only root, dropped capabilities, no-new-privileges, one CPU quota, 128 MiB memory and a 64-process limit. It uses `--network none`, no host mounts and **no published host ports**. Probes run inside the same container through `docker exec` and loopback.

It inspects the actual running constraints and runs both probes. A successful serial probe must complete 32/32 requests; concurrent error counts are observed rather than forced to one expected value. It then removes its exact container ID and unique image tag. Base images and build cache can remain; it never runs global prune, removes another container or deletes host files. If an interrupted run leaves a resource, inspect the printed/build tag and exact owned ID before removing only that resource. A failed cleanup is not a successful lab result. Container memory/process restrictions are not measured peak-memory or attack-resistance evidence.

Image pull/build happen during connected preparation. A network-disabled container does not prove physical air-gapping of Docker, its VM, the host, support, update or media paths. A genuinely disconnected deployment needs separately verified artifact intake and host infrastructure controls. The runner is not an offline-preparation tool. No Apple GPU, CUDA flag or Docker Model Runner is configured.

## Capacity worksheet and interpretation

`factory.json` contains invented model/profile/cost inputs and all fourteen Module 07 lifecycle IDs. The worksheet assumes one independently budgeted replica per separate device, not two replicas on the learning laptop. Its memory formula adds weights, simplified KV cache and assumed runtime overhead, then multiplies by `1 + headroom_fraction`. A 20% added margin is not a claim that exactly 20% of physical memory is reserved.

Expected arithmetic: weights about 3.2596 GiB, KV 2 GiB, memory with added margin about 8.7116 GiB, one active plus one spare replica. Invented energy cost is 18 AED and total budget 2,018 AED/month, or 20.18 AED per 1,000 assumed successful requests. The design peak and monthly success volume are separate assumptions, not a continuous peak-load schedule. These are not a hardware quote, electricity tariff, model benchmark or real budget.

The default result is UNVERIFIED because performance is assumed. Marking a supplied current-build profile as a synthetic/deployment test can produce REVIEW_REQUIRED, never PASS. That label does not authenticate evidence. Known physical/network, memory, installed-replica and declared latency/error failures remain BLOCKED. Missing, unknown or duplicate route declarations and stale profiles create gaps; they cannot cancel known conflicts. Network permission does not relax site constraints. This strict worksheet does not implement a country-only deployment mode.

Twenty-five tests cover arithmetic, context/concurrency, spare requirements, all lifecycle destinations, air-gap conflicts, stale evidence, unknown/duplicate routes, malformed numbers and actual HTTP behavior. The estimator checks declarations, not real geography, privileged access, memory allocation, failure independence or legal applicability. The budget omits implementation-specific allocations and co-location packing.

## Experiments and submission

1. Double context, then concurrent sequences, one at a time. Explain the KV change.
2. Reduce memory or installed replicas; inspect the blocked reasons.
3. Move a backup, diagnostic, activation or unknown route off-site; preserve the hard conflict.
4. Mark performance assumed, stale and current in turn. Explain why no state is certified.
5. Compare serial/concurrent HTTP output; include errors with successful-only p95.
6. Record model/runtime/build, workload mix, host/VM budget, accepted failure case and unresolved evidence in the [compute worksheet](WORKSHEET.md).

Save outputs, environment, resolved image digest where applicable, one adverse mutation and bounded conclusions. Keep actual deployment measurements separate from this synthetic probe. Failure analysis and worked solutions remain in the separate facilitator key.
