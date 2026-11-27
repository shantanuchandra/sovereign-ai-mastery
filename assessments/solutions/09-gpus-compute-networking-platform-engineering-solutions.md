# Module 09 facilitator solutions and scoring rubric

27 November 2026. Course-authored educational key; excluded from the public reader build, not confidential in the source repository. No independent assessment or production approval.

## Q1. Whole running profile (5 points)

Weights are one allocation (1). Context, cached keys/values, concurrent sequences, runtime buffers and other processes consume budget (2). Device placement/sharding and host/VM budgets must be operable, not inferred from aggregate advertised memory (1). Require candidate-build peak-memory and task-specific load evidence rather than accepting a fitting file (1).

## Q2. Requests, limits and remaining controls (5 points)

Kubernetes requests inform placement; limits govern runtime resource use (2). Official documentation describes CPU throttling and reactive memory enforcement, so declarations alone do not establish measured throughput or freedom from termination (1). Authorization/tenant boundaries and real physical placement need distinct controls/evidence (2).

Source: Kubernetes project, *Resource Management for Pods and Containers*, requests/limits and enforcement sections, https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/. Inspected 2026-11-27. No cluster was tested in this course lab.

## Q3. Reproducible arithmetic (5 points)

Weights `7e9 × 4 / 8 / 2^30 ≈ 3.2596 GiB`; KV `2 × 32 × 8 × 128 × 4096 × 2 × 4 / 2^30 = 2 GiB` (2). Added 2 GiB overhead and 20% margin yield about 8.7116 GiB per replica (1). `ceil(2 / (5 × .6)) = 1` active plus one spare means two installed replicas (1). All profile/per-device/overhead/failure assumptions need actual evidence; two separate device budgets do not prove two replicas fit a 16 GB laptop (1).

## Q4. Independent boundary gates (5 points)

An off-site domestic backup conflicts with factory-only scope, and network activation conflicts with the strict air-gap variant (2). More compute does not relocate those paths or authorize their use (1). Contain/block the proposal, preserve derivative and lifecycle constraints, assign owners and require repair/retest or an explicitly authorized changed requirement (2). No legal-compliance conclusion follows.

## Q5. Documented product scope, hypothetical proposal (5 points)

Docker scopes described Linux-container `--gpus` passthrough to Windows with the WSL 2 backend (1). It distinguishes other acceleration, including Docker Model Runner; do not overgeneralize to every Docker-related GPU capability on macOS (1). Require exact host/runtime/backend, compatible model/kernel/precision, memory and representative task measurements, plus rights and boundary checks (2). This module tests synthetic CPU work; it supplies no CUDA/Metal/Model Runner/GPU evidence (1).

Source: Docker, *GPU support in Docker Desktop for Windows*, opening scope note, https://docs.docker.com/desktop/features/gpu/. Inspected 2026-11-27. The proposed supplier/customer is hypothetical, not an actual reported incident.

## Q6. Root-cause analysis and bounded closure (15 points)

1. **State and observation (3):** Assumed performance begins UNVERIFIED. Candidate-test 35% 503 errors breach the 1% criterion and block release despite successful-only p95 of 90 ms. External cloud overflow also conflicts with unchanged premises-only handling. Preserve build, workload, complete denominator, timestamps and route evidence.
2. **Direct causes and diagnostics (3):** Examine admission rejections and queue settings first, but do not assume low GPU use proves the CPU or model is at fault. Inspect resource throttling, memory/OOM/restarts, downstream latency and per-stage tracing. These remain hypotheses until evidence isolates them. The synthetic lab's deliberately exhausted semaphore demonstrates one mechanism, not the real system's cause.
3. **Systemic cause (2):** A weights-only/average-performance acceptance process, successful-only dashboard and missing failure/overflow review allowed gaps. Treat organizational causes as scenario hypotheses, not real findings.
4. **Containment and owners (2):** Accountable release owner keeps real-data deployment blocked and prohibits the off-site route. Platform/admission owner investigates workload and resource behavior; data/security owners protect paths; recovery owner tests the failure model. Use the approved manual fallback or bounded synthetic exercise.
5. **Repair and dated retest (3):** Match candidate build and workload; repair the evidenced bottleneck/admission policy, size memory/context/replicas, maintain approved placement and retest normal/burst/cold and replica-loss cases. Plan a retest such as 2026-11-30 with errors, all-request outcomes, successful throughput, latency population, resource observations and route checks. A plan is not observed passing evidence.
6. **Closure (2):** Repeated failure stays BLOCKED. Missing/stale evidence remains UNVERIFIED. Favorable scoped declarations can support REVIEW_REQUIRED only; qualified reviewers must inspect actual acceptance evidence. A purchased GPU or synthetic CPU result does not establish model quality, production capacity, identity isolation, high availability or sovereignty certification.

**Total 40 points.** Illustrative knowledge threshold 24/40, with hard-gate or unsupported performance/assurance claims requiring remediation regardless of score.

## Lab observations and PM deliverable

The fixture returns UNVERIFIED with weights 3.2596 GiB, KV 2 GiB, 8.7116 GiB including added margin, two required installed replicas and invented cost 20.18 AED per 1,000 assumed successes. These are arithmetic checks. The 25 tests also exercise invalid inputs, every lifecycle destination and actual loopback behavior. The native runner should complete serial 32/32 work; concurrent results vary and must include errors. The Docker path separately inspects configured constraints, records resolved base digest and removes its owned container/tag. Local Mac Docker execution is NOT COMPLETED when its engine is stopped; inspect the matching Linux CI result before claiming container evidence. Neither path benchmarks a model or measures physical residency.

PM rubric (20 points): profile/memory 5; load/error/failure evidence 5; boundaries/operations 4; costs/provenance 3; decision/ownership 3. Require 12/20 plus hard-gate remediation. For the co-location scenario, identify shared host/memory/power/failure domains, combined allocations and measured failover behavior. A second process on the same laptop is not an independent disaster-recovery site.
