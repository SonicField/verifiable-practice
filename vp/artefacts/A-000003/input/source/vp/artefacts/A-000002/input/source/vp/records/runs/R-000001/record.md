# R-000001: Initial preservation and baseline check batch

**ID:** verifiable-practice:R-000001
**Type:** run
**Created:** 2026-10-19 12:07:15 UTC
**Author/operator:** Codex working AI /root; current adoption invocation
**Status:** sealed completed; baseline falsified
**Origin:** [E-000001](../../experiments/E-000001/record.md)
**Goal served:** [D-000001](../../decisions/D-000001/record.md)
**Sealed:** 2026-10-19 12:12:16 UTC

## Inputs before Execution

Protocol H-000001/E-000001. Live source will be frozen by per-file SHA-256
and preserved copies, with Git HEAD/status and dirty bytes recorded. Working
directory /home/alexturner/verifiable-practice; physical/logical identity is
this directory. Existing initial read-only inspections are bootstrap observations,
not backdated executions: date/status/audit inventory and interpreter availability
were read before formal allocation; complete outputs from those reads are not
claimed retained. No reliance on a manufactured earlier run.

Execution uses ordinary Python and preserved checks; exact runtime, scripts,
argv, timestamps, outputs and member exits will be captured. No build required
for this source/document/interpreter batch. No accepted outcome yet.

## Outcome

Pending; record exists before the capture invocation. Evidence location:
vp/artefacts/R-000001/, with MANIFEST.md. Falsification, setup failures and
negative baseline controls will remain separate from wrapper success.


## Recorded outcome at 2026-10-19 12:12:16 UTC

**Actual start/end:** 2026-10-19T12:08:06.533845+00:00 / 2026-10-19T12:08:06.708083+00:00.

| Member | Exit | Retained evidence |
|--------|------|-------------------|
| inventory | 0 | artefacts/R-000001/inventory.stdout.txt; inventory.stderr.txt |
| head | 0 | artefacts/R-000001/head.stdout.txt; head.stderr.txt |
| git-status | 0 | artefacts/R-000001/git-status.stdout.txt; git-status.stderr.txt |
| runtime | 0 | artefacts/R-000001/runtime.stdout.txt; runtime.stderr.txt |
| structural | 0 | artefacts/R-000001/structural.stdout.txt; structural.stderr.txt |
| behavior | 1 | artefacts/R-000001/behavior.stdout.txt; behavior.stderr.txt |
| frontmatter | 0 | artefacts/R-000001/frontmatter.stdout.txt; frontmatter.stderr.txt |
| diff-whitespace | 0 | artefacts/R-000001/diff-whitespace.stdout.txt; diff-whitespace.stderr.txt |

Exact argv/cwd/times are in ../../../artefacts/R-000001/results.json. Behaviour validly falsified the baseline claim; structural/frontmatter observations are bounded. No after-source inference. Historical missing captures remain unknown.
