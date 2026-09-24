---
name: verifiable-practice
description: Apply goal-aligned, falsification-first, evidence-led practice to software work. Use when the user asks for VP or Verifiable Practice, or requests a rigorous review, code audit, investigation, project discovery or recovery, technical explanation, document analysis, or precise specification.
---

# Verifiable Practice

Treat every material claim as something that must be possible to check. Establish what the user is trying to achieve, identify what would show the current approach is wrong, seek that evidence, and report the observed result—including failures and uncertainty.

## Working Rules

- Distinguish the terminal goal from steps that merely serve it.
- Separate observations, interpretations, assumptions, and unknowns.
- State a falsifier before relying on an important claim.
- Prefer tests that can expose failure over examples that merely confirm success.
- Make changes in small, reversible, independently verifiable steps.
- Preserve evidence with enough provenance that another person can reproduce the conclusion.
- Report negative and inconclusive outcomes as prominently as positive ones.
- Ask when missing user context would materially change the work; do not manufacture intent.
- Respect the requested authority boundary. Inspection does not authorise repair, and planning does not authorise execution.

Apply these rules proportionally. A small, low-risk change needs a small verification loop; it does not need ceremonial paperwork.

## Route the Work

Read only the references needed for the current task:

| Need | Read |
|------|------|
| Understand VP's purpose | [Why Verifiable Practice](WHY.md) |
| Clarify outcomes or detect drift | [Goals](concepts/goals.md), then [Review](playbooks/review.md) when a formal review is requested |
| Evaluate a claim or proposed approach | [Falsifiability](concepts/falsifiability.md) and [Bullshit Detection](concepts/bullshit-detection.md) |
| Implement or assess software | [Verification Cycle](concepts/verification-cycle.md) and [Engineering Standards](concepts/engineering-standards.md) |
| Clarify human and AI responsibilities | [Zero-Code Contract](concepts/zero-code-contract.md) |
| Audit a codebase | [Code Audit](playbooks/code-audit.md) |
| Test an uncertain technical claim | [Investigation](playbooks/investigation.md) |
| Diagnose with a debugger | [Hypothesis-Driven Debugging](playbooks/debugging.md) |
| Understand a disordered project | [Project Discovery](playbooks/discovery.md), followed by [Discovery Verification](playbooks/discovery-verification.md) |
| Restructure discovered work | [Project Recovery](playbooks/recovery.md) |
| Analyse a document's claims and incentives | [Document Analysis](playbooks/document-analysis.md) and [Rhetoric](concepts/rhetoric.md) |
| Plan or explain a document | [Document Planning](playbooks/document-planning.md) or [Document Description](playbooks/document-description.md) |
| Remove ambiguity from a contract | [Precise Technical English](concepts/pte.md) and its [playbook](playbooks/precise-technical-english.md) |

Do not load every reference by default. Begin with the smallest applicable set and follow links only when they affect the task.

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
