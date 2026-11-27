# What does a fitting model leave out of the capacity decision?

A fictional factory assistant can fit its weight files yet miss context, concurrency, runtime and recovery budgets. A fast p95 can also hide rejected work when only successes are timed.

Three questions before buying capacity:

- What is the full per-replica and per-host memory budget?
- Which request population, errors and failure case did the candidate build actually test?
- Does every preprocessing, support, activation and overflow path stay within the unchanged boundary?

One product-scope check matters: Docker distinguishes its documented Linux-container --gpus passthrough from other acceleration paths.[^gpu] The CPU course exercise supplies no GPU evidence.

Module 09 includes an actual synthetic CPU service/probe, a separate sizing calculator and a PM worksheet. Its model, performance and cost inputs are invented. Educational draft; independent assessment and manual accessibility review pending.

[Read the lesson](../../chapters/09-gpus-compute-networking-platform-engineering.md) and the [eight-question HTML deck](CAROUSEL.html).

[^gpu]: Docker, *GPU support in Docker Desktop for Windows*, opening scope note, https://docs.docker.com/desktop/features/gpu/. Verified: 2026-11-27. No CUDA, Metal or Docker Model Runner path was tested.
