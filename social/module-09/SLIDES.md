# Module 09 question deck

Educational draft; independent assessment and manual accessibility review pending. HTML is the design source.

## 1. What does a fitting weight file leave out?

A fictional factory assistant still needs working memory for context, concurrent sequences, runtime buffers and other services. A file-size check is the start of a capacity decision.

Budget the running profile at its permitted placement.

Source/scope: Course-authored scenario; no model benchmark.

## 2. Which memory term grows with concurrent context?

The toy worksheet adds weights, a simplified KV cache and assumed runtime overhead, then adds margin. Its numbers describe an invented profile on separate devices.

Measure the actual runtime and host budget.

Source/scope: Invented profile, not a measured model.

## 3. Can a healthy service reject its users?

The synthetic lab keeps health checks available while limiting concurrent work. Requests beyond admission capacity can receive 503 responses even when the health endpoint returns 200.

Test work admission separately from health.

Source/scope: Actual lab mechanism; synthetic CPU work.

## 4. What does successful-only p95 hide?

In the fictional acceptance scenario, successful-request p95 is 90 ms while 35% of requests fail a 1% error criterion. A low latency statistic does not clear that failure.

Read errors, successful throughput and latency together.

Source/scope: Invented scenario, not production measurements.

## 5. Does a GPU flag prove Apple Silicon capacity?

Docker scopes Linux-container --gpus passthrough to Windows with WSL 2 and describes other acceleration separately. This course CPU lab tests no GPU path.

Require an exact supported backend and measured profile.

Source/scope: Docker Desktop GPU scope note, checked 27 Nov 2026.

## 6. Can two processes share one disaster?

Two replicas on the same host share failure and memory domains. A second process is not evidence that the service survives losing that host or its shared storage.

Name the failure case and rehearse recovery.

Source/scope: Course-authored replica planning exercise.

## 7. Can cloud overflow repair a factory-only design?

An off-site overflow route conflicts with the unchanged physical requirement. More capacity, a domestic region or a favorable score does not authorize that route.

Keep known conflicts blocked until repaired or formally changed.

Source/scope: Fictional factory requirement, not a legal conclusion.

## 8. Which assumptions belong beside the price?

Record model/runtime/build, workload mix, memory, errors, spare capacity, operating costs, rights and support paths. Label invented figures and assign evidence owners.

Make the sizing decision conditional and reviewable.

Source/scope: Educational draft; independent assessment pending.

Primary source: Docker, *GPU support in Docker Desktop for Windows*, scope note, https://docs.docker.com/desktop/features/gpu/. Verified: 2026-11-27. Scope is Linux-container --gpus passthrough; do not generalize to other acceleration.
