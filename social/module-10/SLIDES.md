# Module 10 question-led carousel

Educational draft. All bank examples, scores and timeline minutes are fictional. Canonical visual source: CAROUSEL.html.

## 1. Does private cloud mean inside your building?

NIST allows private-cloud placement on or off premises. A fictional BANK-A-only requirement still needs actual location, operator and lifecycle evidence.

Decision: Separate exclusive use, placement and control.

Source/scope: NIST SP 800-145, section 2; checked 27 Nov 2026.

## 2. Can the highest score select a forbidden design?

The fictional managed and hybrid options score higher than local-private. Their support, state or recovery routes still conflict with the unchanged BANK-A rule. Invented preference scores Local-private 70; review required Managed 95; blocked Hybrid 90; blocked

Decision: Apply hard gates before ranked preferences.

Source/scope: Course-authored comparison; no provider eligibility claim.

## 3. Which paths leave after inference stays local?

Trace derivatives, telemetry, support, activation, updates, backups, failover and infrastructure state. Normal operation is only one mode to inspect. Normal Degraded Update Recovery

Decision: Give every protected route an owner and permitted destination.

Source/scope: Fictional bank requirement; not a legal conclusion.

## 4. Can one site survive losing all of itself?

A same-site target cannot establish whole-site recovery. An off-site target violates an unchanged single-site-only rule. Record the incompatible objectives.

Decision: Escalate the requirement pair before choosing a fallback.

Source/scope: Course-authored site-loss scenario.

## 5. Do recovery time and data loss pass together?

The lab subtracts supplied minutes. A four-minute simulated recovery window and two-minute point age are separate quantities. No system was actually restored. Invented timeline, minutes Checkpoint 8 Failure 10 Restoration 14

Decision: Test RTO and RPO independently on the candidate build.

Source/scope: AWS REL13-BP01; numbers are course assumptions.

## 6. Does a private service link remove connectivity?

AWS documents a necessary connection between Outposts racks and the home Region, including management traffic. A hypothetical physical-air-gap proposal must resolve that conflict.

Decision: Inspect the exact product and operating mode.

Source/scope: AWS Outposts racks guide; checked 27 Nov 2026.

## 7. Where does infrastructure state belong?

Terraform redaction does not by itself omit sensitive values from state or plans. Classify the administrative plane and inspect the actual backend and supported handling.

Decision: Keep secrets and real state out of public learning artifacts.

Source/scope: HashiCorp sensitive-data guide; checked 27 Nov 2026.

## 8. What evidence could reverse your choice?

Record the original policy, failure scope, exact build, lifecycle inventory, independent recovery criteria, owners and dated retest. Label simulations and invented costs.

Decision: Keep the recommendation conditional and reviewable.

Source/scope: Educational draft; independent assessment pending.
