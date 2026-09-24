# Review and Audit

VP distinguishes reasoning review from code audit. They answer different questions and grant different authority.

| Dimension | Reasoning review | Code audit |
|-----------|------------------|------------|
| Subject | Goals, decisions, evidence, and process | Source code and its executable contracts |
| Finds | Drift, hidden assumptions, weak falsifiers, selective reporting | Defects, silent failures, missing validation, unsupported guarantees |
| Normal output | Findings, questions, recommendations | A scoped report with reproducible findings and proposed tests |
| Mutation | None unless separately requested | None during audit; repair requires authorisation |
| Typical scope | Current task or session | Named files, subsystem, or codebase |

## Reasoning Review

A review asks whether the work remains connected to the terminal goal and whether its claims deserve their stated confidence. It examines plans, decisions, test evidence, failures, and unresolved questions.

The review should be short. Its value is prioritisation, not exhaustive narration. A useful finding identifies the evidence, explains why it threatens the goal, and proposes a checkable response.

Use a review:

- before committing to an expensive direction;
- after a long or confusing session;
- when progress looks busy but the outcome is unclear;
- when reported confidence exceeds the visible evidence;
- before declaring a substantial task complete.

The operational procedure is in [Reasoning Review](../playbooks/review.md).

## Code Audit

An audit inspects a declared code scope against the [Engineering Standards](../concepts/engineering-standards.md). It must distinguish present defects from defensive hardening and avoid turning stylistic preferences into findings.

A credible finding contains a location, violated contract, failure mode, severity, proposed repair, and a test capable of exposing the gap. If no such test can be described, the finding may be too vague or the behaviour may not yet be understood.

Use an audit:

- before a release or risky integration;
- after a large refactor;
- while adopting an unfamiliar codebase;
- when silent failures or missing invariants are suspected;
- periodically, when the scope and cost are explicit.

The operational procedure is in [Code Audit](../playbooks/code-audit.md).

## Why Audit and Repair Are Separate

An audit creates knowledge. A repair changes the system. Combining them hides false positives, makes the baseline harder to reconstruct, and expands a read-only request into mutation.

After the report, the user may authorise all repairs, a selected subset, or none. Repairs then use adversarial tests and the smallest coherent changes. The final evidence must say which findings remain open.
