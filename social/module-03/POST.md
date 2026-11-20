# Eight questions before buying sovereign AI

A vendor can offer strong security controls and still be the wrong architecture for a particular workload.

Consider a fictional UAE manufacturer. Its engineering assistant has a signed requirement that restricted prompts, embeddings, outputs, logs and backups stay inside one named factory. A service hosted elsewhere in the UAE does not meet that requirement simply by remaining in-country.

The procurement decision changes once you ask:

- Which requirement is a hard gate rather than a weighted preference?
- What happens if local inference times out?
- Does the network firewall denying egress prove the application behaved correctly?
- Who can sign off on exceptions and when must evidence be retested?

In the example, a remote fallback attempt is blocked by the firewall. That is a successful network control but a failed application-routing policy. Release remains on hold until the degraded path is corrected and tested.

The same principle applies to a physically air-gapped environment: an online licence check is not an acceptable hidden dependency.

The eight-slide teaching asset walks through these decisions, the evidence to request and the board-level go/no-go.

Full chapter: https://shantanuchandra.github.io/sovereign-ai-mastery/chapters/03-enterprise-sovereignty-requirements-strategy/

All scenarios are fictional and use synthetic data. This is a learning framework, not legal advice or a claim of production certification.

#SovereignAI #AIProductManagement #EnterpriseArchitecture
