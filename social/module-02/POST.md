# Module 02 | LinkedIn post draft

A model can run on a server inside your factory and still send its prompts outside the factory.

Consider a fictional UAE manufacturer. Its restricted engineering documents, embeddings, prompts, diagnostic logs and backups must remain inside one named physical plant. The team buys an on-site GPU, runs inference locally and reports a high sovereignty maturity score.

Then the gateway times out.

An availability fallback routes a synthetic restricted-label prompt to an off-site API. The off-site endpoint might be in the same country. It still violates the plant's stated boundary.

**The decision is BLOCKED, not “mostly sovereign.”**

This is the distinction I explore in Module 02 of the Sovereign AI Field Guide:

1. **Scope:** Is the requirement national, sectoral, enterprise-wide or specific to one workload?
2. **Control:** Who can access, move, update, recover or operate the system?
3. **Architecture:** Does the deployment class meet the actual boundary, including degraded modes?
4. **Evidence:** What do the network traces, permissions, contracts and dated tests show?
5. **Decision:** Which hard failures prevent launch regardless of a maturity score?

For a genuinely **air-gapped** workload, a private link, regional API, allowlist or temporary remote support tunnel is still a network connection. Updates and recovery must use controlled offline procedures. If the local model cannot meet the quality, licence and capacity requirements, the correct answer may be **not feasible under current constraints**.

The fix for the fictional manufacturer is to disable the off-site fallback, choose a tested local fallback or fail closed, then rerun synthetic normal, timeout, crash, restore and support-path tests. A configuration change alone is not evidence of closure.

The eight-slide carousel explains the architecture choices and a practical release-first scoring approach. The course taxonomy and M0–M4 maturity stages are educational tools, **not** regulatory requirements or certification.

**For your next AI architecture review:** What happens to your sovereignty claim when inference fails over, diagnostics upload or the vendor needs emergency access?

Read the full lesson and lab: https://github.com/shantanuchandra/sovereign-ai-mastery/blob/main/chapters/02-classifications-components-maturity-models.md

Carousel: https://github.com/shantanuchandra/sovereign-ai-mastery/blob/main/social/module-02/CAROUSEL.html

Source for the real-product comparison in the lesson: Microsoft Learn, *Deployment types for Microsoft Foundry Models*, https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/deployment-types (source reviewed 20 November 2026). The plant scenario is fictional and makes no assertion about an actual customer or Microsoft deployment.

#SovereignAI #AIProductManagement #EnterpriseAI #AIArchitecture
