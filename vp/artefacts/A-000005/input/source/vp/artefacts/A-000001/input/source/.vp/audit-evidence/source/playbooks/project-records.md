# Project Planning and Records

Use when establishing VP record conformance, planning a conformant project,
or working inside one that has already adopted the
[standard](../standards/project-records.md). Templates are
[here](../templates/project-records/README.md). This playbook implements the
standard; it does not grant authority to migrate, delete, publish or release.

## 1. Identify the Contract

Read the project's chosen record-root README, PROJECT, PLAN, STATE, ledger
and coverage inventory. Establish scope, root goal, delegated authority,
source identity, active stage, open operations and last audit. Check actual
dates, triggers and records; a stale current view is not sufficient.

For new adoption, create the six project views and root decision. For an
existing disordered project, perform read-only discovery and inventory old
paths first. Label imports retrospective; preserve originals. Record unknown
history and assign current retain/replace work before claiming conformance.
Do not reorganise another project merely because it supplied an example.

## 2. Generalise the Need before Choosing a Response

For each material choice:

1. Preserve the observation/source and its date; distinguish user intent,
   empirical observations and interpretations.
2. State the general problem it illustrates, applicability and limits.
3. Connect that problem to the terminal goal.
4. Compare options and reasons to reject or defer them.
5. Reserve D and record authority, selected option, relied-on claims,
   falsifier, owner, finite review deadline and earlier triggers.

Do not generalise one workload, parser, host or reader into a universal rule.
Existing delegated authority allows routine work without repeated approval.
New authority or changed scope must be evidenced by a decision.

## 3. Baseline and Plan a Stage

Open S under the commissioning decision. Record entry conditions, baseline,
dependency stages, independently checkable deliverables, acceptance/harm
criteria, cost/time/scope tolerances, review gate and reversal. Preserve the
plan baseline. Before exceeding a tolerance, record an exception decision
within delegated authority or seek the missing owner decision.

Related small changes may share a stage. Do not split a mechanical edit into
one record per line, or omit its trace because it is small.

## 4. Record Claims and Protocols before Acting

Create H for each empirical claim relied on by the choice, including claims
about the verification instrument. Specify prediction, scope, falsifier,
dependencies, evidence, owner and horizon. Owner review addresses value
choices; experiments address technical claims.

Create E before execution: procedure, exact input identities, controls,
criteria, sample/analysis method, inconclusive conditions and stopping rules.
Fix criteria before observing results. If the work is exploratory, say so;
use a new protocol for later adoption tests.

## 5. Modify, Build and Execute with Identity

Open C before changing code, tests, configuration or contracts. Preserve the
before snapshot, affected units, intended outcome, falsifier and rollback.

Before every build invocation, reserve B and capture source, generated inputs,
dependencies, configuration, toolchain and predecessor. Record all phases and
statuses. An imported binary records known provenance and unknowns; its nearby
source checkout does not establish how it was built.

Before each evidence execution, reserve R and verify actual executable/input
identities. Preserve every outcome, including setup failure and abort. A
bounded batch needs separate labels, inputs, status and raw output for every
member. Retrying uses a new B or R. Manual and source-only checks explain why
no build applies and identify their checked inputs.

## 6. Preserve, Interpret and Decide

Copy relied-on inputs, logs and results out of disposable workspaces. Create
the owner's manifest with file meaning, identity, producers, retention and
recovery location. Check copied bytes before removing scratch files.

Separate observations, interpretations and unknowns. A valid observation may
falsify a claim; a failed instrument may make the experiment inconclusive.
Record regressions and exclusions as prominently as success. Derived summaries
must identify every contributing run and calculation.

Create a new D to adopt, reject, retain, investigate or stop using completed
evidence. Seal terminal operations. Update coverage for all maintained units
in the accepted snapshot, preserve the inventory, then update current views.
Experimental code needs an explicit adoption change before promotion.

## 7. Revalidate or Contain

When a deadline or trigger occurs, create V, follow incoming reliance links
and mark affected code/deliverables in coverage and state. Unknown impact
remains unknown. Pause dependent acceptance/release, revert, or document an
authorised finite exception with a test and stop condition.

Commission new evidence addressing the trigger. A successor decision renews,
replaces or rejects the justification and sets its new horizon. Extending a
date alone is insufficient. Preserve old verdicts as historical observations.

## 8. Close the Stage and Handoff

Check entry/exit gates, tolerances, all failed/skipped/inconclusive items and
continuing value. Record the checkpoint D to continue, revise, stop or accept.
Leave open operations with last phase, ownership, workspace, input identities
and safe resume/abort instructions. Never infer completion from partial output.

Commission an independent A at acceptance stage exits, declared periodic
checkpoints and before claiming conformance. Use the
[record audit playbook](record-audit.md): freeze a request/packet, receive
findings, respond through new V records and commission fresh re-audit for
closure. A worker self-check is preparation. The assessor does not execute
technical work or repair records; conformance and product acceptance are
separate verdicts. Follow charter budgets and gates.

## 9. Dispose Only with a Trace

Identify consumers and retention obligations. Preserve needed bytes and
verify their new location. Create V with reason, authority, old/new paths and
digests, recovery method or irreversible loss. Preserve records and manifests.
If evidence becomes unauditable, downgrade dependent claims. Unknown ownership
requires discovery before cleanup.
