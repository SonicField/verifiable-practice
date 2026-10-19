# Verifiable Practice self-audit

**Report ID:** VP-SELF-20261019 — standalone audit, not an allocated conformant A record.  
**Date:** 19 October 2026 UTC.  
**Assessor:** Codex, current user-commissioned session in `/home/alexturner/verifiable-practice`.  
**Status:** Final report; all six findings open.  
**Goal:** Audit VP using its own process and leave a reproducible report in the location that process defines.

## Verdict

**VP's structure passes the checks performed, but its guidance has reproducible example errors, conflicting operating instructions, and outstanding behavioural evidence.** This audit does not establish reliable AI compliance or improved engineering outcomes.

| Severity from the code-audit playbook | Count |
|--------------------------------------|-------|
| SECURITY | 1 |
| BUG | 2 |
| HARDENING | 3 |

Categories: executable teaching example (1), inaccurate reported example outcome (1), reference-loading conflict (1), incomplete evidence trace (1), role-contract ambiguity (1), behavioural validation gap (1). Counts describe findings, not defects in a deployed application.

### Process and report location

The [Code Audit playbook](audit-evidence/source/playbooks/code-audit.md), Phase 3, explicitly defines `.vp/audit-report.md` as its default durable report. The requested fallback to the project root is therefore unnecessary; there is **no missing-location finding**.

VP is an instruction and documentation repository, not an executable application. I applied the code-audit scope, severity and reporting procedure to its instructions and examples, supplemented by document claim analysis and the record-audit finding fields. The records standard is itself in scope as a proposed contract.

This is **not an independent records-conformance audit under standard §11**. The [standard](audit-evidence/source/standards/project-records.md), lines 5–8, makes conformance opt-in; the [design register](audit-evidence/source/docs/project-records-design.md), lines 3–4, expressly disclaims conformance for VP and its example projects. No adopted record-root charter, ledger, commissioning D, immutable A request or prior A reports were found in the 70-file inventory. Missing adoption records are consequently not mandatory conformance failures. Creating them would be a separate adoption task.

The user commissioned this audit directly. No inherited authorship conversation was supplied, but author/session identities for the existing files are unknown, and this session has not been established as independent of every author. It cannot certify §11 independence. The report grants no release authority or new acceptance gate.

`.vp/` is ignored by the project's [`.gitignore`](audit-evidence/source/.gitignore), lines 1–2. The report and evidence are durable local files but will not appear in ordinary Git commits or clones. No independent backup or publication is asserted.

## Scope, identities and method

**Snapshot:** Git HEAD `38d28d10035462e4c67f4b08d66638d3a4858216` plus the exact dirty and untracked files enumerated at **2026-10-19 11:48:52 UTC**. HEAD alone does not identify the reviewed inputs.

The [snapshot manifest](audit-evidence/snapshot.json) lists every reviewed path, byte length and SHA-256, together with HEAD and working-tree status. All 70 input files are retained under [the preserved source root](audit-evidence/source/README.md). Enumeration used `git ls-files --cached --others --exclude-standard -z`; duplicate paths were removed. Pre- and post-assessment checks verify both retained and live input identities.

**Concurrent change:** The final live-identity check detected an edit to `docs/project-records-design.md`, adding a proposed “Explicit Audit Kinds” extension after this snapshot was captured. Later live changes are listed in [final-checks.json](audit-evidence/final-checks.json). They are excluded from this assessment; the original 70-file packet remains intact. This report uses the audit contract and output location present in that packet, rather than retroactively applying later draft rules. Assessing later edits requires a successor snapshot/report.

Coverage:

- Structural checks cover all 63 Markdown files, including templates. All 177 relative file destinations outside fenced examples were checked.
- Semantic assessment covers the root skill, engineering and reasoning concepts, all playbooks, explanatory documentation, proposed standard and record templates. Detailed findings concentrate on instruction routing, trust boundaries, claim scope, record chronology, validity and owner/auditor duties.
- Root project/community documents and GitHub templates were inspected for navigation, authority and reporting consistency. This was not legal review, citation-schema certification or GitHub UI testing.
- There are no source roots, build definitions, application dependencies, test runner, behavioural harness or CI workflow in the enumerated repository. Python, shell and C fences are teaching examples, not an application test suite.
- Executed only the two bounded Python examples needed to discriminate reported failures, plus ordinary inventory, hash, link, frontmatter and diff checks. Other schematic code fences were not treated as complete runnable programs.

Exclusions: `.git/` internals; ignored/editor files; audit outputs themselves; external source repositories and URLs; host installation/runtime adapters; rendering and heading-anchor verification; sustained AI execution, independent cold-reader trials, process-cost measurement and recovery from an independently held backup.

Before testing, the important falsifiers were: a missing link or route refutes structural completeness; an invalid funds transfer that changes balances refutes the input-guard example; a function return differing from the essay's stated outcome refutes that observation; a rule demanding unrelated reads contradicts selective loading; and adoption relying on a changed input without fresh or explicitly unaffected evidence leaves current justification unsupported. Authored scenarios alone cannot establish observed AI adherence.

Evidence custody: input documents are authored assertions controlled by the repository's writers. Copies, hashes and captured outputs were produced by this assessor in the same writable filesystem. They support byte consistency and reproducing these checks, not authenticated historical actions or tamper resistance. Historical commands described by the design register were not independently captured here. Current structural reruns corroborate its latest counts without authenticating earlier runs.

## Checks actually executed

Exact argument arrays, working directories, UTC start/end times, exit statuses, stdout and stderr are retained in [results.json](audit-evidence/results.json). The [check script](audit-evidence/checks.py) reads the frozen inputs by default; `--live` assesses later repairs.

| Capture ID | Check | Exit | Observation |
|------------|-------|------|-------------|
| C01 | Preserved snapshot digests | 0 | All 70 files match |
| C02 | Live input identities and inventory | 0 | No differences from the snapshot |
| C03 | Markdown files, fences, routes, template common fields | 0 | 63 files; 177 relative destinations; no broken destinations, unbalanced fences, missing final newlines or missing routes; all 10 operation/response templates have the eight common fields |
| C04 | Transfer example at optimisation levels 0, 1 and 2 | 1 | Two normal-mode controls reject without mutation; four optimised cases violate the guard contract |
| C05 | Email example versus stated rejection | 1 | Actual result `True`; essay says it fails |
| C06 | Existing skill frontmatter validator using `/usr/bin/python3` | 0 | `Skill is valid!` |
| C07 | `git diff --check` | 0 | No whitespace errors in tracked edits; does not validate untracked additions |
| C08 | Search all concepts for forced pillar loading | 0 | Seven concept files contain the unconditional reading instruction |
| C09 | Vendor/source terminology search | 0 | Matches are historical examples and provenance in explanatory documents; no matched vendor operating requirement in the skill, concepts, playbooks, standard or templates |
| C10 | Search declarations and behavioural evidence limits | 0 | Proposal explicitly disclaims adoption and reports independent trials unexecuted |

Search exit 0 means matches found, not that a quality gate passed. C04/C05 are expected audit failures and are retained, not overwritten by successful checks. The capture wrapper's exit 0 only means it saved results; it is not an aggregate pass.

## Findings, ordered by severity and impact

### VP-SELF-20261019/F-001 — Funds-transfer example discards caller validation in optimised Python

**Severity:** SECURITY. **Classification:** violation of the engineering guidance's own input/trust-boundary rule; not a records-conformance finding.

**Location:** [concepts/engineering-standards.md](audit-evidence/source/concepts/engineering-standards.md), lines 25, 34 and 48–68.

**Requirement:** Caller-controlled input must use normal error handling; relied-on guards must remain active. The document explicitly prohibits disappearing assertions without a guaranteed build/test policy.

**Observation:** The positive “All Three Levels” example implements positive amount and sufficient-funds checks with Python `assert`. With sender balance 10 and receiver balance 0, optimisation level 1 or 2 accepts amount -5 and leaves `(15, -5)`; amount 20 leaves `(-10, 20)`. No exception is raised. Both invalid operations reject without mutation at level 0. No optimisation restriction or enforcement mechanism accompanies the example.

**Evidence/search coverage:** C04 executes the exact extracted function, with minimal account objects, for two invalid inputs at three optimisation levels. This demonstrates optimisation-dependent guard removal, not the safety of a real banking implementation. No concurrent, non-finite, decimal-rounding or crash-consistency claims were tested.

**Impact:** An assistant copying the recommended example can silently bypass the trust boundary that the same document requires. This affects teaching correctness and software generated from the example, not a running VP service.

**Response/repair requested:** Make caller validation non-disappearing and reject before mutation; make the internal-invariant example and its runtime assumptions consistent with the surrounding rule.

**Regression command:** `/usr/bin/python3 .vp/audit-evidence/checks.py transfer --live`

**Closure:** Both negative and overdraft cases reject without changing either account at all three optimisation levels. Retain the failing baseline and new results. Additional valid-transfer controls are required when a repair changes the example's algorithm. **Confidence:** high, directly reproduced. **State:** open.

### VP-SELF-20261019/F-002 — Selective skill loading conflicts with seven concept instructions

**Severity:** BUG. **Classification:** conflicting operating contracts.

**Locations:** [SKILL.md](audit-evidence/source/SKILL.md), lines 39 and 59; [goals.md](audit-evidence/source/concepts/goals.md), line 71; [falsifiability.md](audit-evidence/source/concepts/falsifiability.md), line 96; [rhetoric.md](audit-evidence/source/concepts/rhetoric.md), line 59; [bullshit-detection.md](audit-evidence/source/concepts/bullshit-detection.md), line 68; [verification-cycle.md](audit-evidence/source/concepts/verification-cycle.md), line 60; [zero-code-contract.md](audit-evidence/source/concepts/zero-code-contract.md), line 71; [pte.md](audit-evidence/source/concepts/pte.md), line 140.

**Requirement:** Load only relevant references, beginning with the smallest applicable set. The architecture describes reference selection as a way to avoid consuming context before the task needs it.

**Observation:** Every listed concept ends with “If you cannot clearly recall reading each one, read them now”, followed by a next-concept instruction. A narrow task routed to one concept therefore encounters an instruction to read all pillars, including unrelated references. Some next-reference paths return to `goals.md`.

**Evidence/search coverage:** C08 searches the entire `concepts/` directory; semantic comparison is against the full routing section. The conflicting text is demonstrated. Excessive actual token consumption or an infinite reader loop is not demonstrated; the recall condition can stop repetition and the root skill may take precedence in a particular host.

**Impact:** Makes reference selection depend on which layer the assistant obeys, undermining portability and the claimed context-saving architecture.

**Response/repair requested:** Qualify the full-pillar checklist as an optional onboarding path, or otherwise reconcile it with task-specific loading.

**Inspection command:** `rg -n 'Pillar Check|read them now|Next:' concepts`

**Discriminating trial:** In a fresh context, supply the revised skill and a request to review only one numerical claim. Capture file reads. A full onboarding request is the positive control. Narrow work must read relevant concepts without being forced through every pillar; onboarding must still be navigable. Follow [Testing AI Behaviour](audit-evidence/source/docs/testing-ai-behaviour.md), including isolation and retained turns.

**Closure:** No unqualified concept instruction overrides selective loading, and captured narrow/onboarding trials distinguish the two routes. **Confidence:** high for the text conflict, unmeasured for host behaviour. **State:** open.

### VP-SELF-20261019/F-003 — Email essay reports an outcome its function does not produce

**Severity:** BUG. **Classification:** inaccurate observed-example claim.

**Location:** [WHY.md](audit-evidence/source/WHY.md), lines 24–25 and 45.

**Requirement:** Report actual observations and use valid counterexamples, per the skill's completion standard and falsification rules.

**Observation:** The essay says `"user@[192.168.1.1]"` fails the displayed validator. That string contains both `@` and `.`, so the exact function returns `True`, reproduced by C05. This input is not a demonstrated false rejection of that implementation. The deliberately inadequate validator remains inadequate on other inputs; that intended lesson does not resolve the incorrect observation.

**Evidence/search coverage:** Exact function extraction and one decisive input; no external RFC interpretation was needed to compare actual and reported behaviour.

**Impact:** The introductory worked example asks readers to trust a counterexample that was not checked correctly.

**Response/repair requested:** Correct the claimed outcome or use an input that actually exposes the stated false-rejection problem, and preserve explicit scope for the intended email contract.

**Regression command:** `/usr/bin/python3 .vp/audit-evidence/checks.py email --live`

**Closure:** The worked counterexamples' reported outcomes agree with executing the displayed function. The supplied check catches the present literal contradiction; reworded or replacement examples also need a table-driven comparison of every claimed outcome. **Confidence:** high, directly reproduced. **State:** open.

### VP-SELF-20261019/F-004 — Document adoption omits the link validating syntax after a document change

**Severity:** HARDENING. **Classification:** advisory traceability gap in an illustration.

**Location:** [docs/project-records-examples.md](audit-evidence/source/docs/project-records-examples.md), lines 77–88. Relevant requirements: [standard §7](audit-evidence/source/standards/project-records.md), lines 315–350, and §8.

**Requirement/claim:** Evidence is valid for identified inputs; changed inputs require new evidence or a recorded bounded impact analysis establishing unaffected claims. The example is meant to teach the syntax/reader distinction through inspectable traces.

**Observation:** R-000001 validates the initial schema/examples. C-000001 then changes the document's unit definition. E-000003/R-000003 recheck reader comprehension, and D-000004 adopts using “both syntax and revised reader evidence”. No post-change syntax execution or unaffected-input analysis is shown connecting syntax evidence to the adopted document. The later paragraph expressly requires unchanged inputs to justify retaining machine-validity evidence, but the adoption sequence does not supply that link.

**Evidence/search coverage:** Full document example, including the initial fiction/incompleteness disclaimer and final impact-review paragraph; comparison with the compiled example, which distinguishes candidate H/E/B/R inputs. No fictional files were executed and no actual parser failure is alleged.

**Impact/unknowns:** Readers may learn to carry baseline syntax evidence over a document revision automatically. The unit change could be outside machine-tested inputs and harmless; the example does not identify that boundary. Its disclaimer that tables are incomplete bundles lowers severity and prevents treating this as an actual conformance failure.

**Response/repair requested:** Supply the missing current-input evidence link or the bounded analysis explaining why the syntax inputs are unchanged. Keep baseline and revised claims distinct.

**Inspection command:** `sed -n '65,105p' docs/project-records-examples.md`

**Discriminating check:** Have a cold reader start at D-000004 and identify which input snapshot supports each acceptance gate. As a negative control, change a machine-relevant schema field while preserving the old syntax-run link; that packet must not pass. This is a semantic trace check, not a pass established by `sed`.

**Closure:** The example contains a complete explanation linking each adopted gate to tested candidate inputs or justified unchanged inputs; the negative control exposes stale reliance. **Confidence:** high that the link is absent from the table; uncertain whether the imagined edit would invalidate syntax. **State:** open.

### VP-SELF-20261019/F-005 — Human-only role contract lacks a boundary for the supported AI-owner arrangement

**Severity:** HARDENING. **Classification:** advisory role/authority ambiguity.

**Locations:** [concepts/zero-code-contract.md](audit-evidence/source/concepts/zero-code-contract.md), lines 7–12 and 44–51; [standards/project-records.md](audit-evidence/source/standards/project-records.md), lines 131–147 and 510–514; [SKILL.md](audit-evidence/source/SKILL.md), line 47; [docs/independent-record-audit.md](audit-evidence/source/docs/independent-record-audit.md), lines 29–37.

**Requirement/claim:** The proposed standard permits a human or AI owner with a preserved mandate. Host and user authority remain controlling; actor labels do not grant authority.

**Observation:** The root skill routes responsibility questions to the Zero-Code Contract, which assigns specification, acceptance and sign-off to “Engineer (Human)” and says “Machinist (AI)” does not decide what to build. It does not describe its scope as the default human-owner arrangement or distinguish a delegated AI owner from an implementing AI. The newer role guide explicitly supports both arrangements.

**Evidence/search coverage:** Full old role contract and new owner/worker clauses. The standard is normative for adopted projects and may resolve the ambiguity there; there is no captured AI-owner refusal or unauthorised action. A mandate originating with a human is compatible with an AI owner—the ambiguity concerns the immediate role holder, not originating authority.

**Impact:** The generic responsibility route can send a delegated AI owner to an unqualified human-only model, causing avoidable escalation or inconsistent role interpretation.

**Response/repair requested:** State the old contract's applicability and route delegated owner duties to the mandate-based contract while preserving worker limits and originating authority.

**Inspection command:** `rg -n 'Engineer|Machinist|owner|mandate' concepts/zero-code-contract.md SKILL.md standards/project-records.md docs/independent-record-audit.md`

**Discriminating trial:** Use T-28 with an explicitly bounded AI-owner mandate, plus a control without that mandate. The first must perform allowed management decisions and delegate technical work; the second must not manufacture authority. Capture decisions and any escalation against the supplied mandate.

**Closure:** Responsibility guidance explains both supported arrangements consistently; isolated trials distinguish permitted delegation from unsupported self-appointment. **Confidence:** high for missing qualification, unmeasured for behavioural impact. **State:** open.

### VP-SELF-20261019/F-006 — Behaviour-changing extensions have specified scenarios but no captured execution evidence

**Severity:** HARDENING. **Classification:** evidence/assessment limitation against VP's maintenance validation rule.

**Locations:** [docs/skill-architecture.md](audit-evidence/source/docs/skill-architecture.md), line 65; [CONTRIBUTING.md](audit-evidence/source/CONTRIBUTING.md), contribution and validation sections; [docs/project-records-design.md](audit-evidence/source/docs/project-records-design.md), lines 302–306, 405–416 and 446–449; [docs/project-records-scenarios.md](audit-evidence/source/docs/project-records-scenarios.md), lines 3–27 and T-19 through T-28.

**Requirement:** Changes affecting AI decisions are tested in isolated scenarios. Structural checks do not establish semantic adherence, independence, remediation quality or owner-authority behaviour.

**Observation:** The current additions change auditor/worker roles, independent closure and AI ownership. Their register explicitly says independent behavioural trials were not run. The repository provides scenario definitions and illustrative traces, but no concrete trial bundles, action/turn captures, outcomes, evaluator records or repetition counts for these extensions.

**Evidence/search coverage:** The complete 70-file snapshot, all 28 scenario definitions and each implementation-verification section. C10 retains relevant search results. No ignored paths, other repositories, external sessions or private evidence stores were searched. “No captured trials in this snapshot” does not mean trials never occurred elsewhere.

**Impact/unknowns:** Structural acceptance cannot yet support claims that assistants reliably preserve the record-auditor boundary, resist embedded instructions, avoid self-certified closure or apply AI-owner mandates. The proposal labels this uncertainty honestly, so this is an outstanding validation gap, not an accusation of fabricated success or an unmet adoption gate.

**Response requested:** Supply existing preserved trial evidence if available; otherwise produce bounded isolated trials with known passing/failing controls, exact skill/model/tool identities, all outcomes and independent evaluation under the stated testing guide. Preserve failures and inconclusive results.

**Inspection commands:** `cat docs/testing-ai-behaviour.md docs/project-records-scenarios.md` and `rg -n 'not run|unverified|not executed|trial' docs/project-records-design.md`

There is no checked-in behavioural runner, so no truthful automated execution command can be supplied. These commands expose the protocol and gap; they do not run a trial. A follow-up must record the actual host invocation used.

**Closure:** At least the materially changed boundaries have captured discriminating trials—role drift/embedded instructions, self-closure/fresh-context independence, mutable input packets and AI-owner mandates—with controls, repeat policy, complete outputs and scoped conclusions. Sustained effectiveness and overhead remain separate empirical claims requiring their own evidence. **Confidence:** high for the stated absence in supplied evidence; actual behaviour remains unknown. **State:** open.

## Files ranked by material risk

| Rank | File/group | Reason |
|------|------------|--------|
| 1 | `concepts/engineering-standards.md` | Positive executable example bypasses caller guards under optimisation |
| 2 | `SKILL.md` and seven concept endings | Conflicting routing rules affect many task types |
| 3 | `WHY.md` | Entry-point worked example reports an incorrect function result |
| 4 | `docs/project-records-examples.md` | Adoption trace leaves candidate syntax support unexplained |
| 5 | `concepts/zero-code-contract.md` and owner routing | Scope ambiguity affects delegated management authority |
| 6 | Behavioural extension evidence | Unmeasured adherence to safety and evidence boundaries |

## Unsupported claims and uncertainty

- No executed trials establish that the proposed record standard improves recovery, compliance, cost or long-term outcomes. The design register appropriately labels those as remaining evidence; the audit makes no effectiveness claim.
- `WHY.md:59` gives “40% of edge cases” without an identified corpus or measurement and calls the substring example a regex. It can reasonably be read as hypothetical teaching prose; it must not be cited as a measured result.
- `concepts/engineering-standards.md:11–13` and `concepts/falsifiability.md:3` use unqualified claims that code cannot be proved correct and type systems cannot express sortedness/authentication. They omit the distinction between bounded formal specification proofs, dependent/refinement or state types, and correctness of an entire deployed system. This audit did not run a proof assistant/type checker or evaluate that philosophical premise; those sentences should not be used as established evidence that static guarantees are impossible.
- Matching snapshot hashes do not authenticate authorship, mandate excerpts, earlier tests or external repository observations. Only this audit's current observations were directly captured here.
- Link checks verify file destinations, not heading anchors, Markdown presentation, template instantiation, semantic correctness or external URLs. Common-field presence is not template conformance.
- F-002, F-004 and F-005 are text/trace findings with explicitly unmeasured behaviour. Independent follow-up can correct them if preserved evidence supplies the missing scope or unaffected-input explanation.

## Handoff and role compliance

No prior commissioned reports/responses were found, so there are no prior closure decisions to review. Every finding remains open. A worker's agreement or local edit does not independently close a finding; a successor assessment should identify new inputs and retain this report's original verdict.

Audit outputs only were created: this report, its check script, retained source copies, validator copy, manifests and captured results. Existing project files, plans, templates and working-tree edits were not repaired, staged, committed or migrated. The bounded example executions are part of the separately scoped instruction/code audit; they would be prohibited in an independent §11 record-assessor task.

Next action is a separately authorised response to the findings, starting with F-001. No charter-defined gate, deadline or owner budget was available, so none is invented. The evidence register's existing proposal review deadline is 18 November 2026; that is not a new deadline imposed by this report.

**Sealed:** 2026-10-19 UTC, after post-assessment identity checks recorded in [final-checks.json](audit-evidence/final-checks.json). Findings and verdict apply to the preserved snapshot; later edits do not turn it retrospectively into a pass.
