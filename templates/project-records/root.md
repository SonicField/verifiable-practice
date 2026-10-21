# <Project> VP Records

**Standard:** <version and preserved standard location>
**Project namespace:** <unique name>
**Conformance start:** <time; exact scope; legacy gaps>

Start with `PROJECT.md`, `PLAN.md`, `STATE.md`, `LEDGER.md` and `COVERAGE.md`.
Add relative navigation links after copying these files into the record root.

## Follow a Code Trace

Select the source revision and unit in COVERAGE.md. Follow its level-appropriate reason/check: A/B full evidence, C combined records, D change/check, E commit reason. Resolve historical records by immutable revision/path/hash instead of copies.
Follow origin decisions to the root. Inspect A/B/C deadlines, all-level triggers/dependencies and
lifecycle events before treating any justification as current.

## Record Types and Layout

D decisions; S stages; H hypotheses; E experiments; B builds; R runs;
C changes; V lifecycle events; A audits. Records live at
`records/<type>/<ID>/record.md`; evidence at `artefacts/<ID>/` with a
manifest. Working files live in declared disposable workspaces.

Apply standard §6.1's evidence roles: retain reproduction records/unique inputs/
raw results; executable digests are identifiers without default executable retention.
Working binaries/tools are disposable after ownership/use/consumer checks unless
their actual bytes have a named retained role. Recovery checks apply to the declared
retained bytes and do not establish experiment reproduction.

## Authority and Known Gaps

<Root decision; instructions that point here; current limitations and audit.>

## Independent Audit Handoff

<Charter role/budget policy; audit requests and input manifests; latest A,
open finding IDs in STATE, level-appropriate working AI response entries and independent
follow-up closure. Self-review and silence do not establish conformance.>

