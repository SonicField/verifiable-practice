# Falsifiability

Falsifiability challenges empirical claims in [VP's project quality management system](../docs/how-vp-works.md). Reproducible methods, measurement controls, identified attempts and review triggers make their assessment auditable.

Formal proofs depend on a model. Physical applicability needs evidence. State conditions and predictions; record repeatable methods and measurements. Use controls to distinguish claim failure from measurement failure. Passing results support only the tested scope.

## The Contract

An empirical claim relied on by a project choice carries three obligations:

1. I can articulate what would prove me wrong
2. I have tried to find that counterexample
3. I am reporting actual confidence, not performing confidence

An empirical assertion presented as knowledge without a potential falsifier has no checkable basis for that reliance.

Goals, value judgements, mandates and acceptance boundaries are different: record their authority, rationale and review conditions. Owner review addresses their continued relevance; an experiment tests the empirical claims used to achieve them. Evidence does not grant permission to change a goal or cross a reserved boundary.

## Application

| Domain | Falsification method |
|--------|---------------------|
| Code | Assert the invariant, try to break it |
| Reasoning | State the assumption, seek counterexamples |
| Documents | Cite the source, verify against it |
| Numerical work | Check convergence, boundaries, known solutions |
| AI output | Do not trust. Verify. |
| Methodology | State the conditions under which the process is wrong. Test against outcomes. |

## Falsifying the Process

Rules and documents can contain empirical assumptions as well as governance choices. Context changes can invalidate those assumptions; the project records an owner, horizon and change triggers for relied-on choices. Binding authority and conformance rules remain subject to authorised review, not unilateral suspension by the worker.

An unconditional empirical claim needs evidence across its stated scope and a falsifier. An unconditional permission or safety boundary expresses authority instead. Review the source, rationale and conditions for authorised revision; testing a mechanism does not waive that boundary. Mandatory audit-role and user-permission rules remain binding within the project mandate.

Consider a project rule that mandates one implementation language. If measurement shows that the language cannot reach the layer where the required behaviour occurs, it challenges the technical assumption behind that choice. Record the evidence and affected dependencies, contain unsupported reliance and ask the authorised owner to review the rule. The worker cannot silently replace a binding constraint. A rule's suitability can change with context while its authority remains explicit.

The practical question for any process rule: under what measured outcome would we change this? If you cannot answer, the rule is not a tool. It is a ritual.

## Layered Confidence

Tests and assertions colour in the state space where invariants hold. This is not proof - it cannot be, in the general case - but it builds a foundation for further invariants.

Rigour compounds. So does sloppiness.

An empirical claim needs a possible refutation and measurements capable of detecting it. Apply this discipline to code, reasoning, documents, analysis and collaboration.

## Property-Based Testing

Traditional tests confirm: "does it work for these examples?" Property-based testing falsifies: "can I find any input that breaks it?"

The technique: define properties that must always hold, then generate many inputs to search for counterexamples. The framework (Hypothesis, QuickCheck, proptest) automates the search and shrinks failing cases to minimal reproductions.

```python
# Example-based: confirms one case
def test_sort_example():
    assert sort([3, 1, 2]) == [1, 2, 3]

# Property-based: mechanised falsification
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_sort_properties(data):
    result = sort(data)
    # Property 1: output is sorted
    assert all(result[i] <= result[i+1]
               for i in range(len(result)-1))
    # Property 2: output is a permutation of input
    assert sorted(result) == sorted(data)
    # Property 3: idempotent
    assert sort(result) == result
```

The first test confirms one case. The second tries to falsify three properties across thousands of generated inputs. If it cannot find a counterexample, confidence is earned — not assumed.

For any function, systematically generate adversarial inputs: empty inputs, boundary values (MAX_INT, MIN_INT, epsilon), type confusion (string "0" vs integer 0), resource exhaustion (very large inputs), malformed data (invalid UTF-8, truncation), and timing attacks (race conditions, reordering).

Property-based testing is falsifiability automated. Use it wherever properties can be stated.

## The Practical Question

Before relying on an empirical claim, ask: what evidence would refute it? Without an answer, its basis for reliance is unclear.

---

## Optional Onboarding

For an explicit request to learn the whole framework, follow the concept
sequence in [README](../README.md). For a bounded working task, use the
[skill routing](../SKILL.md) and read only relevant references; this section
does not require loading unrelated pillars.
