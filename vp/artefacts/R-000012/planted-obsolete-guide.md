# Document Work

Document analysis, planning and description provide content-quality control within [VP's full project quality management method](how-vp-works.md). Record document requirements, sources, changes and evidence under the project's authority and acceptance gates.

VP treats documents as instruments: they should change a reader's understanding, decision, or action. Three related modes address different failures.

| Mode | Question | Use it when |
|------|----------|-------------|
| Analysis | What does this document claim, optimise, and cause? | Something feels wrong or unsupported |
| Planning | What must this document accomplish, for whom? | An important document has not yet been drafted |
| Description | What model will let this reader understand the thing? | The subject is understood but difficult to explain |

## Analysis

Analysis separates direct statements from interpretation. It extracts stated goals, examines incentives and effects, identifies rhetorical modes, tests important claims for falsifiability, and shows the gap between what is promised and what is optimised.

Analysis should not invent hidden motives. “This incentive rewards speed over accuracy” can be supported from structure; “the author wants errors” usually cannot.

See [Document Analysis](../playbooks/document-analysis.md).

## Planning

Planning begins with the intended change in the reader, not a heading list. It establishes audience, evidence, failure conditions, constraints, and only then structure. A section belongs when it performs a necessary job for the reader.

Planning is complete when the writer can explain how the proposed document will produce the intended outcome and what response would show that it failed.

See [Document Planning](../playbooks/document-planning.md).

## Description

Description translates a real system into a useful mental model. It identifies the essential facts, relevant boundaries, common misconceptions, and an ordering that matches the reader's needs.

Analogies can reduce cognitive load, but every analogy has a break point. State that boundary before the analogy becomes a false implementation claim.

See [Document Description](../playbooks/document-description.md).

## Clear and Testable Requirements

Use ordinary English to express requirements. A consequential clause needs enough meaning for another reader to identify the permitted behaviour and an observable acceptance or failure check. Apply this review to interfaces, invariants, state transitions, failure behaviour and acceptance criteria, as well as implementation specifications.

Check the information that matters to the clause:

- Who performs the action, and who has authority to approve it?
- What inputs, outputs or states do the technical terms identify?
- Under which conditions does the requirement apply?
- Which ordering, deadline or quantity affects the outcome?
- What happens on failure, including any retry or escalation?
- What observation would distinguish compliance from a defect?

Identify whether a clause is a requirement, recommendation or option. The adopted project standard defines those distinctions; its meanings do not depend on capitalisation.

Define a term when different interpretations could change a choice or test. State timing and quantities when the outcome depends on them. Split or rewrite a sentence when its actors, conditions or ordering are unclear. Readability and checkable meaning determine whether the wording succeeds; a prescribed capitalisation, sentence pattern or vocabulary does not establish that result.

Use the project's existing [planning and record contract](../standards/project-records.md): the charter and stage define authority and acceptance criteria; decisions record selected requirements and their sources; protocols record inputs, checks and thresholds; runs record actual outcomes. [Document Analysis](../playbooks/document-analysis.md) checks whether the wording supports the intended decision or action. A Project Auditor checks the records and evidence support under its separate commission.

When the owner's intended behaviour or threshold is unresolved, identify the consequential ambiguity and ask the owner. Record the answer and its authority before dependent work proceeds. A worker must not invent a value to make a requirement appear complete. An experiment can test a selected mechanism; the experiment cannot grant permission or choose a reserved goal.

### Worked Review Scenarios

These are illustrative requirements and expected review responses, not reports of executed reader experiments.

**Failure response.** “Retry failed requests” leaves the actor, eligible failures and limit unclear. With owner-confirmed values, a checkable clause could read: “The request worker retries a timed-out request at most twice. The request worker reports failure to the caller after the second unsuccessful retry. The request worker does not retry an authorisation rejection.” A check observes the attempts and caller outcome for each failure class. Without those confirmed values, the correct review response is to ask which failures permit retries and what limit applies.

**Timing and quantity.** “Write the results soon” supplies no acceptance boundary. An owner-confirmed requirement could read: “The results writer writes one result file for each completed run before the stage review begins. The review cannot accept a run whose result file is missing.” A check compares completed run IDs with identified result files at the review boundary. The requirement does not invent a duration when an ordering constraint is sufficient.

**Authority and uncertainty.** “Use a faster method if necessary” does not establish a performance threshold or permission to change a reserved method. Record the unknown threshold and the owner's method constraint. Ask for the missing decision before changing the method. Preserve any authorised measurement as evidence for that decision; a faster result does not itself authorise the change.

Use PTE through concepts/pte.md.
