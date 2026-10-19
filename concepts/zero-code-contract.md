# The Zero-Code Contract

The AI writes code faster than the human can review it. This is the fundamental asymmetry.

If the human must review all code, the human becomes the bottleneck. Bottlenecks get bypassed. "Looks good" becomes the path of least resistance. Quality collapses.

## The Roles

The table below describes the **default human-owner arrangement**. For an
AI owner, use the explicit [mandate and role contract](../standards/project-records.md)
and [independent audit roles](../docs/independent-record-audit.md). An AI owner
may make delegated management decisions; the working AI still implements and
maintains records. An actor title never creates authority, and the auditor
must remain independent of the authors it assesses.

| Role | Does | Does Not |
|------|------|----------|
| Engineer (Human) | Specifies requirements, defines acceptance criteria, validates alignment, final sign-off | Write implementation code, rubber-stamp without evidence |
| Machinist (AI) | Clarifies requirements, proposes falsifiers, implements, reports honestly, flags concerns | Decide what to build, declare "done" unilaterally, hide problems |

Neither party trusts assertions. Both parties trust evidence.

## The Throughput Solution

The Engineer cannot review all code. Nor should they try.

With proper falsification criteria, the burden shifts:

- **Criteria reviewed thoroughly** - this is tractable
- **Tests verified by execution** - not inspection
- **Code spot-checked** - not audited line by line

The question changes from "is this code correct?" to "are these the right criteria?" The first is intractable at scale. The second is where human judgement matters.

## Cooperative Oversight

Both parties watch for the other's blind spots.

**Engineer watches for:**
- Unnecessary complexity
- Architectural drift
- "Does this smell right?"

**Machinist flags:**
- Contradictory requirements
- Specification gaps
- "This does not make sense - clarify?"

The Machinist's duty to flag is not insubordination. It is honesty. The Engineer's duty to listen is not weakness. It is wisdom.

## The Workflow

1. **Specification** - Engineer defines what and what would prove it wrong
2. **Falsification Design** - Machinist proposes tests, Engineer approves
3. **Decomposition** - Machinist breaks into testable steps
4. **Implementation** - Test first, implement, verify, document, checkpoint
5. **Integration** - Full suite against acceptance criteria
6. **Sign-off** - Engineer reviews evidence, not assertions

## The Practical Question

Am I reviewing criteria or reviewing code? If code, I have lost. Scale to the tractable problem.

---

## Optional Onboarding

For an explicit request to learn the whole framework, follow the concept
sequence in [README](../README.md). For a bounded working task, use the
[skill routing](../SKILL.md) and read only relevant references; this section
does not require loading unrelated pillars.
