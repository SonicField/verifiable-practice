# Select the Audit Kind

Use this entry point whenever an owner asks for a VP audit. Select its kind
before loading an audit procedure or inspecting the project as an audit.

| Kind | Canonical name | Subject | Procedure |
|------|----------------|---------|-----------|
| `project` | Project Audit | Goal/plan/decision history, records, provenance, evidence support, validity, custody and code-to-root traceability | [Project Audit](record-audit.md) |
| `code` | Code Audit | Implementation defects, engineering standards, executable contracts and missing technical checks | [Code Audit](code-audit.md) |

“Record audit”, “independent record audit” and “project conformance audit” are
aliases for Project Audit. A short [reasoning review](review.md) is a separate
review activity; it is not a substitute for either declared audit.

## Mandatory Clarification

For an ambiguous request such as “Please audit X”, the AI **must ask what
sort of audit is intended and wait for the answer before starting**.

Ask one concise question: “Do you mean a Project Audit of records and
justification, a Code Audit of implementation quality, or both?”

Do not guess from the target's name, source files, available records, a
charter default or the current task's technical interest. Do not silently
start either audit or both. Elapsed time without an answer does not select
a kind. This is required scope clarification, not approval for already
authorised work. An explicitly typed request or commissioning instruction
has already selected its kind and needs no repeated question.

## After the Kind Is Selected

1. State and record kind, subject, snapshot, role boundary and intended output.
2. Load and apply the selected playbook only.
3. If both are selected, create two scopes, role assignments and reports.
   Cross-reference them without merging permissions or verdicts. The same
   independent project-assessor session must not switch to technical auditing.
4. A later request to change kind creates a separate scope/task, not an
   unrecorded expansion of the first audit.

## Keep Verdicts Distinct

Project Audit uses A requests/reports, V responses and independent follow-up
A closure. It grants a scoped record-conformance verdict, not product quality
or release approval. Its assessor does not execute or repair the project.

Code Audit produces an explicitly labelled code report. In a conformant
project, preserve that report as technical evidence under the owning R
record and manifest; it may be cited by a Project Audit. It is not itself an
A project audit. Code repairs need separate authority and working records.

Missing project records do not authorise code-quality analysis. A code defect
noticed during Project Audit is an out-of-scope technical concern to route
separately. Missing rationale noticed during Code Audit does not turn that
report into independent project conformance. Keep each task's required output.
