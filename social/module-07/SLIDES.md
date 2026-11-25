# Module 07 architecture questions

Educational draft. Fictional examples; independent assessment pending.

## Where does your local model depend on someone else?
A fictional factory assistant may use local inference but remote embeddings, identity, telemetry or support. Trace the dependencies before choosing the architecture.

Inventory all four planes.

Source/scope: Course-authored PLANT-A scenario.

## Which plane owns the decision?
Separate data storage and transformation, workload execution, administration, and policy or identity decisions. A single product can span several responsibilities.

Split functions when owners, privileges or locations differ.

Source/scope: Course-authored four-plane taxonomy.

## Does being inside the building authorize access?
NIST SP 800-207 rejects implicit trust based solely on physical or network location. Location and authorization answer different questions.

Test both the boundary and the permission.

Source/scope: NIST SP 800-207, official abstract.

## What happens outside the happy path?
Include speech/OCR, diagnostics, telemetry, backups, support, activation, updates, failover and retirement. A rare operation can still move a protected derivative.

Trace lifecycle paths through failure and recovery.

Source/scope: Course-authored architecture exercise.

## Can an on-site rack still need a regional link?
AWS Outposts racks documentation describes a necessary service link to an AWS Region for management and traffic. The described link challenges a fictional physical-air-gap proposal.

Inspect the exact product and every dependency.

Source/scope: AWS Outposts racks service-link guide.

## Can an arrow repair a network route?
Removing an off-site diagnostic arrow from a diagram changes the drawing. An observed prohibited route still needs containment, repair and a build-linked retest.

Preserve observed conflicts until evidence changes.

Source/scope: Synthetic root-cause scenario.

## Which assumption changes the recommendation?
Changing factory-only scope to country scope can admit a domestic campus. It is an explicit requirement change, with new authorization and evidence questions.

Record the decision authority and remaining gates.

Source/scope: Fictional counterfactual; no legal approval.

## What belongs in the architecture decision record?
Record intended use, hard constraints, rejected options, owners, evidence, operating costs and review triggers. Favorable synthetic declarations still require human review.

Connect the diagram to an accountable decision.

Source/scope: Educational draft; independent review pending.
