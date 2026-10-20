# Hypothesis-Driven Debugging

Use a debugger as a measurement instrument. State the hypothesis and its falsifier before issuing commands.

## 1. Verify the Subject

Before attaching a debugger, prove that the executable and symbols correspond to the source under investigation. Record an identifier such as a build ID, checksum, timestamp relationship, or reproducible build reference. If the executable is stale or provenance is uncertain, rebuild before drawing conclusions.

Also record the invocation, environment, inputs, and configuration needed to reproduce the fault.

## 2. State Competing Hypotheses

Write at least two plausible explanations when possible. For each one state:

- what you believe is happening;
- the exact observation that would contradict it;
- the exact observation that would be consistent with it.

Do not confuse “consistent with” and “proved.”

## 3. Design a Discriminating Observation

Choose the smallest debugger action that distinguishes the hypotheses:

- breakpoints to test control flow;
- conditional breakpoints to isolate relevant state;
- watchpoints to catch the writer of corrupted data;
- exact memory, register, stack, or expression inspection;
- observations immediately before and after a suspected transition.

Prefer targeted stops over aimless stepping. If two hypotheses predict the same observation, the experiment does not discriminate and must be redesigned.

## 4. Observe and Record

Record exact commands and values, not qualitative summaries. Keep observation separate from interpretation:

```text
OBSERVATION: [exact value, stack, address, or control-flow event]
COMMAND: [debugger command that produced it]
INTERPRETATION: [which hypotheses this falsifies or leaves viable]
```

Re-check executable identity after any rebuild. A persistent debugger session is useful only while its loaded program remains the program being reasoned about.

## 5. Conclude Carefully

State which hypotheses were falsified, which survived, what remains unknown, and the next discriminating test. Convert a discovered defect into a repeatable automated test before implementing the fix whenever practical.

## Anti-Patterns

- exploring without stating an expectation;
- debugging a stale or unidentified build;
- recording “small” or “wrong” instead of exact values;
- collecting only evidence for the first hypothesis;
- treating a crash location as proof of the corruption source;
- changing code during measurement without starting a new recorded experiment.
