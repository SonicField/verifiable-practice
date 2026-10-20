---
name: verifiable-practice
description: Use the full project quality management system for human–AI collaboration, including governance, planning, verification, traceable records, independent assurance and revalidation. Use when the user asks for VP or Verifiable Practice, or requests a falsification-led review, project or code audit, investigation, project discovery or recovery, document analysis, or precise technical specification.
---

# Verifiable Practice

VP is a full project quality management system for human–AI collaboration. Its epistemology supplies evidence discipline; its owner/worker/auditor roles, controlled stages, quality criteria, records and review gates manage the complete project lifecycle. This skill distributes and routes the method.

When working on this repository itself, read its [record root](vp/README.md)
and [current state](vp/STATE.md). Its prospective charter governs tracking;
legacy history is not certified and a conformance claim needs independent A.
These repository-specific links do not enrol another project using this skill.

Treat every material claim as something that must be possible to check. Establish what the user is trying to achieve, identify what would show the current approach is wrong, seek that evidence, and report the observed result—including failures and uncertainty.

## Manage the Whole Project

For project work, identify the owner mandate, terminal goal, scope, acceptance/harm criteria and delegated authority. Plan bounded stages with budgets, tolerances, review points and stop conditions. Generalise observations before choosing an approach. Commission falsifiable claims/protocols before evidence executions; identify actual inputs and retain relevant failures and retries. Link authorised changes and retained artefacts to decisions, evidence and the root goal.

The owner controls goals, scope and management decisions; the working AI produces authorised work and maintains records, ledger, coverage and current views. An AI owner requires an explicit bounded originating mandate. A distinct Project Auditor checks a frozen packet and closure conditions without technical execution or repair. Humans may contribute work under the charter; role names do not grant authority or independence.

Review quality evidence and unresolved risks at gates; record acceptance, exceptions, continuation or stopping. Check validity and dependency impact at handoff and on relevant changes. Revalidate expired/invalid support with new evidence and successor decisions. Preserve owned evidence, copies and disposition history. Use the [complete overview](docs/how-vp-works.md), [project playbook](playbooks/project-records.md) and [standard](standards/project-records.md) for the required documents and actions.

A bounded use of VP applies the relevant method to the authorised task. Full project record conformance is explicitly adopted for a scope and snapshot; an existing charter must be followed, and a new project is not silently enrolled. Conformance assessment and product-quality acceptance are separate gates. The method uses Markdown/directories without required specialised software or persistent team infrastructure.

## Working Rules

- Distinguish the terminal goal from steps that merely serve it.
- Separate observations, interpretations, assumptions, and unknowns.
- State a falsifier before relying on an important empirical claim; record authority and rationale for goals and value decisions.
- Prefer tests that can expose failure over examples that merely confirm success.
- Make changes in small, reversible, independently verifiable steps.
- Preserve evidence with enough provenance that another person can reproduce the conclusion.
- Report negative and inconclusive outcomes as prominently as positive ones.
- Ask when missing user context would materially change the work; do not manufacture intent.
- Respect the requested authority boundary. Inspection does not authorise repair, and planning does not authorise execution.

Apply these rules proportionally. A small, low-risk change needs a small verification loop; it does not need ceremonial paperwork.

When a project declares conformance to VP project planning and records, use
its chosen record root and the [Project Records Standard](standards/project-records.md).
Check current validity, retain every relevant attempt, and link maintained
artefacts to decisions and evidence. Adoption is explicit; do not silently
claim that an existing project conforms or migrate it without authority.

For any audit request, first use [Audit Routing](playbooks/audit-routing.md).
For an ambiguous request such as “Please audit X”, ask which kind is intended
and wait for the answer. Do not infer a kind, use a charter default or start
both. An explicit typed request needs no repeated clarification.

When assigned a Project Audit (also called independent record audit), use a fresh context and the
[Record Audit](playbooks/record-audit.md) playbook. Assess the designated
packet and write only audit outputs. Return evidence requirements to the
working AI; technical execution and record repair belong to that AI. A
worker response requires independent re-audit for closure. The implementation
loop below applies to working tasks, not this assessor role.

## Route the Work

Read only the references needed for the current task:

| Need | Read |
|------|------|
| Understand VP's purpose | [Why Verifiable Practice](WHY.md) |
| Clarify outcomes or detect drift | [Goals](concepts/goals.md), then [Review](playbooks/review.md) when a formal review is requested |
| Evaluate a claim or proposed approach | [Falsifiability](concepts/falsifiability.md) and [Bullshit Detection](concepts/bullshit-detection.md) |
| Implement software | [Verification Cycle](concepts/verification-cycle.md) and [Engineering Standards](concepts/engineering-standards.md) |
| Clarify human and AI responsibilities | [Zero-Code Contract](concepts/zero-code-contract.md) |
| Select the kind for an audit request | [Audit Routing](playbooks/audit-routing.md) |
| Audit implementation defects or engineering quality (`code`) | [Code Audit](playbooks/code-audit.md) |
| Test an uncertain technical claim | [Investigation](playbooks/investigation.md) |
| Diagnose with a debugger | [Hypothesis-Driven Debugging](playbooks/debugging.md) |
| Understand a disordered project | [Project Discovery](playbooks/discovery.md), followed by [Discovery Verification](playbooks/discovery-verification.md) |
| Restructure discovered work | [Project Recovery](playbooks/recovery.md) |
| Plan a project, keep conformant records, or revalidate expired justification | [Project Records Standard](standards/project-records.md), [Project Planning and Records](playbooks/project-records.md), and [Templates](templates/project-records/README.md) |
| Audit project records and justification (`project`) or respond to findings | [Project Audit and Remediation](playbooks/record-audit.md), [Audit Request](templates/project-records/audit-request.md), [Audit Report](templates/project-records/audit.md), and [Worker Response](templates/project-records/audit-response.md) |
| Analyse a document's claims and incentives | [Document Analysis](playbooks/document-analysis.md) and [Rhetoric](concepts/rhetoric.md) |
| Plan or explain a document | [Document Planning](playbooks/document-planning.md) or [Document Description](playbooks/document-description.md) |
| Remove ambiguity from a contract | [Precise Technical English](concepts/pte.md) and its [playbook](playbooks/precise-technical-english.md) |

Do not load every reference by default. Begin with the smallest applicable set and follow links only when they affect the task.

## Explanatory References

Use these when the task is to explain, evaluate, test, or maintain VP itself:

| Need | Read |
|------|------|
| Explain the framework and its boundaries | [How VP Works](docs/how-vp-works.md) |
| Explain the difference between review and audit | [Review and Audit](docs/review-and-audit.md) |
| Explain project archaeology and safe restructuring | [Discovery and Recovery](docs/discovery-and-recovery.md) |
| Explain experimental side work | [Investigations](docs/investigations.md) |
| Explain VP's document methods | [Document Work](docs/document-work.md) |
| Test a VP skill, prompt, or AI workflow | [Testing AI Behaviour](docs/testing-ai-behaviour.md) |
| Maintain or adapt this skill | [Skill Architecture](docs/skill-architecture.md) |
| Explain project planning, record custody and validity | [Project Records](docs/project-records.md) |
| Review the record standard's design choices and inspirations | [Project Records Design](docs/project-records-design.md) |
| See code and document traces through records | [Worked Record Traces](docs/project-records-examples.md) |
| Evaluate record behaviour across projects | [Project Records Scenarios](docs/project-records-scenarios.md) |
| Explain independent auditor/worker roles and handoff | [Independent Record Audit](docs/independent-record-audit.md) |

These documents explain the whole method or its components to human and AI readers. For actions, use the corresponding playbook; adopted normative requirements remain in the standard.

When modifying VP itself, follow [CONTRIBUTING.md](CONTRIBUTING.md), preserve the safety boundary in [SECURITY.md](SECURITY.md), and record user-visible changes in [CHANGELOG.md](CHANGELOG.md). Community participation is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Default Verification Loop

For implementation work:

1. State the intended observable outcome.
2. Identify assumptions and meaningful failure conditions.
3. Define the smallest test or measurement that could expose a wrong approach.
4. Run that check before changing code when practicable.
5. Implement the smallest coherent change.
6. Run focused verification, then broader checks in proportion to risk.
7. Record what changed, the exact evidence, and anything not verified.

Passing checks means the work resisted the attempted falsification. It does not prove correctness.

## Completion Standard

A VP result states:

- the goal served;
- the material claims made;
- how those claims were tested;
- the observed evidence;
- remaining uncertainty, failures, and skipped checks.

Do not perform confidence. Make the work verifiable.
