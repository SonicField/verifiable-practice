# How Verifiable Practice Works

AI systems produce plausible language quickly. Plausibility is useful for generating possibilities, but it is not evidence that a claim is true or that software meets its goal. VP externalises the discipline needed to close that gap.

## The Failure Modes

| Failure mode | What happens |
|--------------|--------------|
| Goal drift | Work optimises an intermediate task while the desired outcome disappears from view |
| Confirmation bias | Checks demonstrate familiar examples but do not challenge the claim |
| Authority substitution | Existing code, documentation, convention, or model confidence stands in for evidence |
| Cherry-picking | Successful outcomes are prominent while failures and uncertainty are buried |
| Context loss | Decisions and their rationale disappear between sessions |
| Permission drift | A request to inspect or plan quietly becomes permission to modify |

These are not uniquely AI failures. AI increases their speed and scale.

## The Three Layers

VP separates material by purpose:

1. **Concepts** explain the reasoning model: goals, falsifiability, rhetoric, honest reporting, verification, contracts, precise language, and engineering standards.
2. **Playbooks** tell an AI collaborator how to perform a particular kind of work.
3. **The root skill** supplies shared rules and loads only the references needed for the current task.

This separation matters. A concept should remain true across tools. A playbook can prescribe a workflow. A platform adapter may translate capabilities into product-specific commands without changing either.

## The Default Loop

VP reduces most work to a short loop:

1. State the terminal goal.
2. State the next material claim or intended outcome.
3. Identify what observation would show it is wrong.
4. Seek that observation using the smallest useful test.
5. Make one coherent change.
6. Re-run focused and proportionate broader checks.
7. Record evidence, failures, and remaining uncertainty.

The loop scales with risk. Renaming a private variable does not need an investigation report. Changing a persistence format or security boundary does.

## What “Verifiable” Means

VP does not promise that work is verified forever. It asks that important claims be made checkable:

- the goal is explicit enough to assess alignment;
- assumptions are visible enough to challenge;
- tests are capable of failing for the defect they claim to detect;
- evidence has enough provenance to reproduce;
- negative results are retained;
- uncertainty is not rewritten as confidence.

Passing verification means the work survived the checks that were actually performed. It does not mean every possible failure was excluded.

## The Framework Is Also a Claim

VP should be revised or discarded if it does not improve decisions or outcomes. Warning signs include rituals that consume effort without changing decisions, documentation nobody uses, tests that cannot detect regressions, or process that obscures rather than clarifies responsibility.

The framework must remain verifiable too.
