# Review and Audit

VP has two audit kinds: **Project Audit** (`project`) and **Code Audit**
(`code`). “Independent record audit” is another name for Project Audit.
Reasoning review is a separate, lighter activity.

For “Please audit X” or another ambiguous request, the AI must ask which kind
is intended and wait before starting. A charter default or the contents of X
must not silently choose it. Use [Audit Routing](../playbooks/audit-routing.md).

| Dimension | Project Audit | Code Audit | Reasoning review |
|-----------|---------------|------------|------------------|
| Subject | Plans, decisions, records, provenance, validity and code-to-root traceability | Implementation and executable contracts | Current reasoning and goal alignment |
| Finds | Missing/unreliable history, unsupported reliance, expired claims and record gaps | Defects, silent failures, missing technical validation | Drift, weak falsifiers, selective reporting |
| Output | A report with kind `project`, findings, evidence requirements and independent closure | Report with kind `code`, technical findings and proposed tests | Concise findings, questions and recommendations |
| Technical execution | Assessor does not run or repair the project | Technical scope is explicit; repairs separately authorised | None unless separately requested |
| Verdict | Record conformance for a snapshot/time | Engineering findings within the inspected code scope | No conformance verdict |

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

A Code Audit inspects a declared code scope against the [Engineering Standards](../concepts/engineering-standards.md). It must distinguish present defects from defensive hardening and avoid turning stylistic preferences into findings.

A credible finding contains a location, violated contract, failure mode, severity, proposed repair, and a test capable of exposing the gap. If no such test can be described, the finding may be too vague or the behaviour may not yet be understood.

Use a Code Audit:

- before a release or risky integration;
- after a large refactor;
- while adopting an unfamiliar codebase;
- when silent failures or missing invariants are suspected;
- periodically, when the scope and cost are explicit.

The operational procedure is in [Code Audit](../playbooks/code-audit.md).

## Project Audit (Independent Record Audit)

Record audit checks whether preserved records support a declared history,
choice, validity and code-to-goal trace. Its assessor has a separate context
from the working AI and writes only audit outputs. It can flag missing
validation or unsupported inference; technical investigation and repair remain
working tasks. It does not become a code reviewer by reading a referenced unit.

Use the [record audit playbook](../playbooks/record-audit.md). Findings carry
stable IDs and observable evidence requirements. Worker responses create new
records; a fresh independent report closes or retains findings. Preserved
original reports prevent either worker or assessor mistakes from disappearing.
The [role guide](independent-record-audit.md) explains packet custody and gates.

If both kinds are requested, commission two tasks and reports. A Code Audit
may supply technical evidence cited by a Project Audit, but does not itself
satisfy project conformance. A project record gap does not authorise the
assessor to switch into technical analysis. Keep any earlier report unchanged
and label its kind when cataloguing it.

## Why Audit and Repair Are Separate

An audit creates knowledge. A repair changes the system. Combining them hides false positives, makes the baseline harder to reconstruct, and expands a read-only request into mutation.

After the report, the user may authorise all repairs, a selected subset, or none. Repairs then use adversarial tests and the smallest coherent changes. The final evidence must say which findings remain open.
