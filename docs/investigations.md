# Investigations

An investigation is a bounded, hypothesis-driven departure from implementation. It answers a question whose result could change the direction of the main work.

Investigations produce evidence. Any experimental code is scaffolding unless the user later chooses to integrate it.

## A Good Hypothesis

A useful hypothesis is:

- specific enough to predict an observation;
- falsifiable by a realistic experiment;
- connected to a decision;
- narrow enough to investigate without building the proposed solution first.

“The cache is broken” is not enough. “The cache returns stale values because invalidation occurs after readers are notified” predicts observable ordering and can be challenged.

## Isolation and Records

Use an appropriate reversible boundary: a branch, worktree, disposable environment, notebook, or dedicated experiment directory. Record the hypothesis, falsifier, environment, procedure, observations, and verdict in a durable status document.

Isolation protects the main work from experimental changes. The record protects the result from memory loss and prevents a failed approach from being rediscovered without its history.

Projects adopting [record conformance](../standards/project-records.md) use
canonical hypothesis, protocol, build and run IDs, retained evidence manifests,
and separate commissioning/adoption decisions. This makes an investigation
traceable from maintained code and lets later instrument defects trigger
review of dependent conclusions.

## Three Honest Verdicts

| Verdict | Meaning |
|---------|---------|
| Falsified | A valid observation contradicts the hypothesis |
| Failed to falsify | The observed evidence is consistent with the hypothesis, but does not prove it |
| Inconclusive | The experiment could not distinguish the predicted outcomes |

“Confirmed” is usually too strong. An experiment tests a defined slice of conditions, not every possible state.

## Returning to Main Work

An investigation should end with the decision it informs, not merely a technical observation. State what changes, what does not, and whether further evidence is worth its cost. Port only deliberate, reviewed artefacts into the main work.

See [Investigation](../playbooks/investigation.md) and [Hypothesis-Driven Debugging](../playbooks/debugging.md).
