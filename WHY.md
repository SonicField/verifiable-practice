# Why Verifiable Practice

Verifiable Practice (VP) is a **full project quality management system for human–AI collaboration**. It manages the work from the originating goal and mandate through planning, implementation, quality checks, acceptance, maintenance and retirement. Its records let another person or AI inspect the choices and evidence that justify the work.

Human and AI contributors need shared criteria, bounded authority and continuity across sessions. Falsification gives them a way to challenge technical claims. Project management supplies the roles, stages, gates and durable history needed to act on that evidence.

Bullshit is not lying. Liars know the truth and conceal it. Bullshitters are indifferent to truth. They say what sounds right, what fits the meeting, what satisfies the prompt. Whether it happens to be true is incidental.

Software engineering is drowning in bullshit. "Best practice" that nobody tested. Architecture decisions justified by vibes. AI-generated code that looks correct and compiles and passes the obvious tests and fails in production.

VP makes goals, choices, quality criteria, evidence and acceptance decisions explicit and reviewable.

## Why a Project Needs the Whole Method

A good test is one part of a continuing project. Someone must decide what outcome matters, what work is authorised, how much uncertainty and cost are acceptable, which result justifies a choice, and when changed conditions require review. Those decisions must remain understandable after the original conversation disappears. Owned manifests explain retained inputs, byte identities, custody and retention; verified independent revision replicas support actual recovery. Missing old history remains unknown, while new choices and evidence justify current work.

VP supplies four connected quality functions:

| Function | What the collaborators do |
|----------|---------------------------|
| Quality planning | Agree requirements, acceptance/harm criteria, responsibilities, stages, budgets and tolerances |
| Quality control | Check code, specifications, documents and experiments against the chosen criteria; retain all relevant outcomes |
| Quality assurance | Independently inspect records, provenance and current justification; return gaps to the worker and check closure |
| Quality improvement | Use failures, review findings and process observations to revise methods, controls and future choices |

The owner preserves the goal and mandate and makes or delegates management decisions. The working AI performs authorised work and keeps the records. A distinct record auditor checks a frozen packet without becoming an implementer. An owner can be human or AI, with explicit authority; the [role guide](docs/independent-record-audit.md) explains that contract.

The [overview](docs/how-vp-works.md) explains the whole lifecycle. The [project standard](standards/project-records.md) defines the adopted documents, directory structure and actions. Markdown and directories preserve meaning; no particular AI vendor, database or team runtime is required.

## The Core Question

Before relying on an empirical claim, ask: what observation would show this is wrong?

If you cannot answer, you do not understand what you are claiming. You are making noises shaped like assertions.

This is not philosophy for its own sake. It has immediate practical consequences.

## Worked Example: Adversarial Testing

You write a function to validate user input:

```python
def validate_email(email: str) -> bool:
    return "@" in email and "." in email
```

You test it:

```python
assert validate_email("user@example.com") == True
assert validate_email("invalid") == False
```

Both pass. You commit. The code is tested. You are done.

You have produced bullshit.

### What Would Prove This Wrong?

The function claims to validate email addresses. What would falsify that claim?

- `"@."` passes but is not valid
- `"user@localhost"` fails; that is a false rejection if the contract permits local domains
- `"user@[192.168.1.1]"` passes; acceptance alone does not establish correct address-literal validation
- `"user+tag@example.com"` passes (good) but you did not check
- `"user@example..com"` passes but is not valid

You did not try to break it. You tried to confirm it.

### The VP Approach

1. **State the goal**: Specify which address forms the application accepts, including its policy for local domains and address literals.

2. **State the falsifier**: Find an input that is accepted when it should be rejected, or rejected when it should be accepted.

3. **Try to falsify**: Generate adversarial inputs. Edge cases. Malformed data. Known attack patterns.

4. **Report honestly**: Record each input, expected outcome under the chosen contract and actual result. The displayed function is a substring check, not a regex; these observations provide no measured failure rate. Either document a bounded input contract or choose and test a parser suited to it.

These checks challenge the function. The surrounding project still needs to record which input contract the owner authorised, why the chosen mechanism serves it, which exact version was tested and what result justifies retaining it.

In an adopted project, that history travels through the root decision and charter, a bounded stage, the commissioning choice and protocol, identified build/run attempts, and a later adopting decision/change. Coverage links the maintained function to those records. A changed contract, runtime or expired review horizon triggers impact review and revalidation. This is an illustrative application of the method, not a report of additional executed tests.

## Epistemology: the Evidence Foundation

Epistemology is the study of knowledge. What can we know? How do we know it? When are we wrong?

These are not abstract questions. Every line of code embodies an epistemic claim: this is correct. Every test embodies an epistemic method: this is how I checked.

VP applies that evidence discipline inside the management method. An empirical claim needs a falsifier and suitable observations. Goals, value judgements and authority need explicit sources and owner review; a successful experiment does not grant new permission. The practice is to distinguish what was observed, what was chosen and what remains unknown.

## Supporting Evidence Concepts

These concepts support the management lifecycle. The [complete foundation list](README.md#foundations) and [method overview](docs/how-vp-works.md) show where each contributes:

| Concept | Core Question |
|---------|---------------|
| Goals | What are we actually trying to achieve? |
| Falsifiability | What would prove this wrong? |
| Rhetoric | Who needs to be convinced, and of what? |
| Verification | How do we check at each stage? |

Goals need attributable authority and owner review. Empirical plans for achieving them need falsifiable claims and suitable evidence. Falsifiability without a goal is undirected scepticism; persuasion about technical outcomes needs verification.

## The Practice

Start project work with a charter, plan, state, ledger and coverage using the [templates](templates/project-records/README.md). Agree roles, gates and review policy; preserve current choices and every relevant evidence attempt. At acceptance, review the artefact against its criteria and use a separately commissioned independent Project Audit for record conformance.

Use the [Reasoning Review](playbooks/review.md) during work to ask:

- What is the terminal goal?
- What would falsify the current approach?
- Is this report honest about confidence?
- What does this failure reveal?

The discomfort is not a bug. Comfortable collaboration produces comfortable bullshit.

## Summary

VP defines a complete management method for collaborative project work. Projects choose technical techniques proportionately and explicitly adopt the required planning/record contract for a declared scope. Choices, verification, acceptance and maintenance remain connected to the originating goal through durable evidence and consequence-based review dates/triggers.

Passing record audit describes the inspected history and justification. Product acceptance needs its own quality evidence. The method's effectiveness and cost remain subjects for evaluation; full lifecycle coverage supplies a process to evaluate, rather than a guarantee of success.
