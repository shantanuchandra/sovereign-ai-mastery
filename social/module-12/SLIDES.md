# Module 12 question carousel source

Educational draft; 28 November 2026. Eight HTML-authored portrait slides. Exact question headings, readable sources and measured print/reflow checks are required. PDF is untagged; HTML preferred.

## 1. Can a local model still disclose another tenant’s data?

Yes. A globally searchable index can pass forbidden evidence to a generator without crossing a national border.

Decision: Authorize evidence before ranking.

Scope/source: Fictional BANK-A policy; locality and permissions are separate

## 2. Which part of the pipeline decides who may read a chunk?

Resolve identity through a trusted boundary. A tenant name or “I am HR” inside a question cannot grant access.

Decision: Carry source permissions through the entire request.

Scope/source: Course-authored control design; not an implemented identity provider

## 3. What can a permission filter after top-k miss?

Forbidden candidates can displace eligible ones. Their text may already have reached ranking, traces or context.

Decision: Restrict the candidate set before scoring.

Scope/source: Teaching design; test actual effective service roles

## 4. Does a citation prove the answer is supported?

A valid source reference shows where context came from. Each material claim still needs a declared support criterion.

Decision: Separate retrieval hit, support and task behavior.

Scope/source: Lewis et al., RAG, arXiv:2005.11401v4; checked 28 Nov 2026

## 5. What happens when access changes after retrieval?

Previously authorized context can become stale. Cached responses and queued work need a defined revocation boundary too.

Decision: Bind context to current source and policy versions.

Scope/source: Fixture rechecks before context; distributed delivery remains untested

## 6. What did the actual local generation show?

The response contained the correct seven-day fact with extra words. It failed the predeclared exact-format criterion.

Decision: Retain raw failures and keep release withheld.

Scope/source: One English synthetic generation; no production quality benchmark

## 7. Can a prompt wrapper prevent every malicious instruction?

No. Approved documents can contain hostile instructions. The teaching quarantine flag is a declaration, not a detector.

Decision: Keep access and action controls outside the model.

Scope/source: OWASP LLM01:2025 Prompt Injection; checked 28 Nov 2026

## 8. Which evidence would you require before a RAG pilot proceeds?

Test tenant/group denial, revocation, stale versions, abstention, language slices and every diagnostic or recovery destination.

Decision: Name owners, unresolved gaps and the retest.

Scope/source: Educational draft; independent/manual assurance pending
