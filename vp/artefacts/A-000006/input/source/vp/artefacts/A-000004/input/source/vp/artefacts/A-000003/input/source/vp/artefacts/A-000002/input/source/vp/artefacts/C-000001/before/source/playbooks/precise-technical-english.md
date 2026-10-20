# Precise Technical English

Use this playbook to turn ambiguous requirements into falsifiable technical statements. Read [Precise Technical English](../concepts/pte.md) first.

## Activation

Apply PTE only where ambiguity is costly: interfaces, invariants, state transitions, preconditions, postconditions, failure behaviour, security boundaries, and acceptance criteria. Use natural prose for rationale and explanation.

## Resolution Loop

1. Render the current understanding as explicit condition-action statements.
2. Identify the one unresolved ambiguity that most affects implementation or verification.
3. Ask one focused question.
4. Record the answer as a requirement clause.
5. Repeat until each material clause has one testable interpretation.

## Required Form

- Use active voice and name the actor.
- Use RFC 2119 terms: MUST, MUST NOT, SHOULD, SHOULD NOT, MAY.
- State cardinality explicitly: exactly one, zero or more, at most one.
- State timing explicitly: before, after, within, until.
- Use `IF [condition], THEN [actor] [modal] [action] [object]` for conditional behaviour.
- Define technical nouns once and use one term for one concept.
- Name error states and required responses.
- Give each consequential clause an observable acceptance or falsification test.

## Output

Present natural-language context first, followed by the PTE contract and a short list of unresolved questions. Do not invent a value merely to eliminate ambiguity. If the user cannot yet decide, preserve the uncertainty explicitly.
