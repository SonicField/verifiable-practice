# Testing AI Behaviour

AI output varies between runs and is sensitive to visible context. Testing an AI workflow therefore requires both deterministic checks and semantic evaluation, with careful isolation of the scenario.

## Start with Observable Behaviour

Define the behaviour being tested before choosing an evaluator:

- the input and visible context;
- the required output or action;
- prohibited output or action;
- evidence that distinguishes success from a superficially plausible answer;
- allowed variation in wording or sequence.

A test that accepts every plausible answer cannot falsify the workflow.

## Use the Cheapest Reliable Oracle

| Oracle | Appropriate for |
|--------|-----------------|
| Exact structural check | Required files, fields, exit codes, or state transitions |
| Pattern or schema check | Stable markers with variable prose |
| Programmatic behavioural check | Whether the produced artefact actually works |
| Independent AI evaluation | Meaning, reasoning quality, or other semantic criteria |
| Human review | High-impact value judgements or unresolved ambiguity |

Prefer deterministic checks when they measure the real requirement. Use an AI evaluator only where judgement is genuinely semantic, and give it an explicit rubric rather than asking whether the output is “good.”

## Test Positive and Negative Behaviour

A confirmational scenario checks that required behaviour occurs. An adversarial scenario checks that prohibited behaviour does not occur. Both matter.

For example, if a root investigation marker should switch the assistant into investigation review:

- the positive test checks for hypothesis and experiment analysis;
- the adversarial test checks that the assistant does not also emit the ordinary review workflow;
- a control scenario checks ordinary review when the marker is absent.

## Isolate Context

Everything the model can see is part of the input, including test names, fixture directories, planning notes, prior messages, and evaluator instructions. A model that detects the harness may respond to the meta-situation rather than the intended scenario.

Run behavioural tests in disposable environments containing only realistic scenario material. Keep harness code and expected verdicts outside the assistant's visible workspace. Record the model, configuration, skill revision, prompt, and available tools.

For interactive behaviour, wait for observable readiness rather than fixed delays. Script the conversation state, capture each turn, bound retries and total time, and clean up sessions even after failure.

## Evaluate Non-Determinism Honestly

One passing sample establishes little for a stochastic system. The number of repetitions should follow the risk and expected variance. Record every run, not only representative successes.

When using an AI judge:

- isolate the judge from the intended verdict;
- provide raw output and a concrete rubric;
- require cited evidence for each criterion;
- allow an inconclusive result;
- calibrate against known passing and failing examples;
- check disagreement with deterministic signals and human review.

An AI judge is another fallible measurement instrument. Its verdict is evidence, not ground truth.

## Preserve the Test Record

A useful record contains scenario inputs, environment, output, evaluator result, deterministic checks, run count, failures, and the decision taken. Generated verdict files may be excluded from version control, but the test definition and rubric should be reviewable.
