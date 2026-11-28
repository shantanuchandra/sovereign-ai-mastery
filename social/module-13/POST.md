# Which problem should a model optimization solve?

If a current document never reaches the prompt, would you fix retrieval before training? If a response contains the right fact plus extra prose, is the failure factual or contractual? If a smaller configuration runs faster, which quality slices and recovery tests still need to pass?

Module 13 separates prompting, RAG, LoRA and serving experiments. Its real CPU lab compares one and two threads on eight synthetic prompts. The observed two-thread median was lower, but both profiles failed the tiny English/Arabic literal-label criterion. Those timings do not establish production suitability or a general speedup.

The question carousel covers the measurements, missing evidence and full training/evaluation lifecycle. BANK-A is fictional; its premises rule is not a statement of UAE law. No training or quantization was performed. Independent and qualified language/domain reviews remain pending.

Which missing denominator would change your deployment decision?

Read the lesson: https://shantanuchandra.github.io/sovereign-ai-mastery/modules/13-fine-tuning-optimization-evaluation.html

Sources checked 28 November 2026: Hu et al., LoRA; Hugging Face PEFT and Transformers 4.57.3; PyTorch 2.9; HELM; pinned SmolLM2 card. Pinpoint links and exact extracts are in the lesson. Draft for review; not posted.
