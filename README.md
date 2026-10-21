# Verifiable Practice

Verifiable Practice (VP) is a **full project quality management system for human–AI collaboration**. It defines how a project establishes its goals and authority, plans controlled work, makes justified choices, verifies results, keeps an auditable history, accepts deliverables and maintains their justification over time.

Falsification and honest reporting provide its evidence discipline. Project roles, stage gates, records, independent assessment and revalidation turn that discipline into a repeatable management method. VP applies to code, specifications, documents, experiments and other maintained project artefacts.

The method uses Markdown documents and directories, with revision control providing content identity, immutable history and a verified independent replica. Git is an ordinary implementation; equivalent alternatives must demonstrate those properties. No VP-specific software, database, service or persistent AI team is required. This repository also packages the method as a reusable AI skill: [SKILL.md](SKILL.md) gives operating rules and routes an assistant to the references needed for its current responsibility.

## Start Here

- **Understand the complete method:** read [How VP Works](docs/how-vp-works.md), then [Why VP](WHY.md) for its motivation and evidence discipline.
- **Start or adopt a project:** use [Project Planning and Records](playbooks/project-records.md), the [standard](standards/project-records.md) and [templates](templates/project-records/README.md).
- **Give an AI working instructions:** provide [SKILL.md](SKILL.md), the project's charter and its current task. Keep owner, worker and assessor responsibilities explicit.
- **Resume a project:** read its `PROJECT.md`, `PLAN.md`, `STATE.md`, `LEDGER.md` and `COVERAGE.md`; check source identity, open work, deadlines and triggers before proceeding.
- **Learn the foundations:** use the concept sequence below. A bounded task loads the references relevant to that task.

For a new conformant project, select a record root, normally `vp/`, and create its README plus those five project views. Record the owner's mandate, root decision, first stage, quality criteria, budgets, gates, retention and review policy before execution. Existing projects preserve their source and distinguish missing history from new choices; a new retention decision can justify current work without inventing the past.

## The Project Lifecycle

| Boundary | Management action | Durable evidence |
|----------|-------------------|------------------|
| Establish | Agree the goal, owner mandate, scope, quality/acceptance criteria, risks and authority | Root decision and project charter |
| Plan | Divide work into bounded stages with deliverables, budgets, tolerances, review points and stop conditions | Plan and stage records |
| Choose | Generalise observations, compare alternatives and explain how the choice serves the goal | Level-appropriate reasons/checks, with dates for A/B/C and triggers for all levels |
| Build and verify | Set hypotheses and protocols before tests; make authorised changes; identify actual inputs and retain every relevant attempt | Records scaled by consequence: full forms for A/B, combined C, one change/check for D, commit message for E |
| Control and assure quality | Check technical/document quality; independently assess records and justification; respond to findings | Checks, content analysis, typed audit reports and linked responses |
| Accept or redirect | Review evidence, open risks, gates and continuing value; accept, revise, continue or stop within authority | Owner/delegated checkpoint and exception decisions |
| Maintain and hand off | Track changed premises, expiry, dependencies and unfinished work; revalidate affected justification | State, ledger, coverage and level-appropriate successor entries/evidence |
| Retire or recover | Preserve revision history and replica, actually verify restoration and record pruning or explicit loss | Unique evidence and commit/path/hash locators, with level-appropriate disposition |

The [project standard](standards/project-records.md) defines the management and record contract. [Playbooks](#playbooks) provide the procedures, including implementation, investigation, document work, discovery and recovery.

## Human and AI Responsibilities

| Responsibility | Accountable work |
|----------------|------------------|
| Owner | Preserve the goal; appoint roles; define scope, criteria, budgets and authority; review value and make acceptance/exception decisions |
| Working AI | Clarify gaps, propose choices/tests, implement authorised work, retain evidence and maintain VP's records/current views |
| Independent Project Auditor | Assess a revision identified by an audit reference, report gaps and check closure; remain separate from authors and technical problem solving |

A human owner and AI worker are a common arrangement. An AI owner can act under an explicit bounded mandate. Humans can also contribute technical work under the agreed project roles. The owner ensures tracking happens; the working AI performs routine tracking. The [zero-code contract](concepts/zero-code-contract.md) describes one arrangement for oversight when the AI writes implementation code.

## Quality, Traceability and Current Justification

Quality planning establishes what acceptable work means. Quality control checks the artefact against those criteria. Independent record assurance checks whether choices, results and current justification are supported. Failures, audit findings and process-cost observations inform improvement of the method itself.

For any maintained unit, `COVERAGE.md` leads to its level-appropriate reason and check, then the authorised root goal. A/B have fuller evidence and independent gates; C uses declared samples/stages; D has one change/check, E its commit message. Failed and abandoned attempts remain accessible in revision history. A/B/C have justified finite reviews; D/E use change triggers without default expiry. Expired or invalid support requires impact review before fresh reliance.

All required documentation is Markdown; raw evidence can retain native formats beside owned manifests. Revision control must preserve immutable content-addressed history, with a verified independent replica for recovery. Historical source is cited by commit/path or blob, never copied into worktree audit references. Conformance applies to an explicit scope and revision after independent Project Audit. It describes record discipline; product quality requires its own acceptance evidence.

## Choose the Assessment

- **Project Audit:** records, decisions, evidence provenance, validity and artefact-to-root traceability. “Independent record audit” is an alias.
- **Code Audit:** implementation correctness and engineering quality.
- **Document analysis:** content, claims, audience, purpose and whether a document achieves its intended effect.
- **Reasoning review:** a shorter check of current alignment and evidence.

For an ambiguous request such as “Please audit X”, the AI **must ask which sort of audit is intended and wait before starting**. It must not guess or silently perform both. See [Audit Routing](playbooks/audit-routing.md). Technical/content assessment and independent record conformance have separate scopes and verdicts. The worker repairs records and produces authorised evidence; a fresh independent follow-up report closes Project Audit findings.

## Foundations

These concepts support the complete management method:

1. [Goals](concepts/goals.md)
2. [Falsifiability](concepts/falsifiability.md)
3. [Rhetoric](concepts/rhetoric.md)
4. [Bullshit Detection](concepts/bullshit-detection.md)
5. [Verification Cycle](concepts/verification-cycle.md)
6. [Zero-Code Contract](concepts/zero-code-contract.md)
7. [Engineering Standards](concepts/engineering-standards.md)

## This Repository's Records

This repository has adopted prospective record keeping under its [project charter](vp/PROJECT.md). Its [operational records](vp/README.md) preserve choices, evidence, coverage and scoped audits. Pre-adoption history remains incomplete; inspect [current state](vp/STATE.md) before assuming that an earlier verdict covers a later change.

## Playbooks

Playbooks turn the concepts into repeatable work:

| Playbook | Use it when |
|----------|-------------|
| [Review](playbooks/review.md) | You need a short check for drift, weak evidence, and hidden assumptions |
| [Code Audit](playbooks/code-audit.md) | You need to audit a codebase and, if authorised, harden it with tests |
| [Investigation](playbooks/investigation.md) | A technical uncertainty needs a controlled experiment |
| [Debugging](playbooks/debugging.md) | A debugger should discriminate between explicit hypotheses |
| [Discovery](playbooks/discovery.md) | A project has scattered artefacts and unclear history |
| [Discovery Verification](playbooks/discovery-verification.md) | A discovery report must survive loss of conversation context |
| [Recovery](playbooks/recovery.md) | Valuable work must be reorganised without losing it |
| [Project Planning and Records](playbooks/project-records.md) | A project needs durable plans, traceable choices and evidence, or revalidation |
| [Project Audit](playbooks/record-audit.md) | A separate assessor reports project-record gaps and independently checks worker responses |
| [Audit Routing](playbooks/audit-routing.md) | An audit kind must be explicit; ambiguous requests require a question and answer |
| [Document Analysis](playbooks/document-analysis.md) | A document's stated purpose may differ from what it actually optimises |
| [Document Planning](playbooks/document-planning.md) | An important document needs a clear outcome and audience before drafting |
| [Document Description](playbooks/document-description.md) | You understand a system but need to explain it clearly |

## Documentation

The documentation explains the complete method and its components for human and AI readers. Playbooks give procedures for the selected responsibility; standards define adopted requirements.

| Document | Subject |
|----------|---------|
| [How VP Works](docs/how-vp-works.md) | Full project lifecycle, quality functions, roles, records, assurance and limits |
| [Review and Audit](docs/review-and-audit.md) | Project Audit, Code Audit and lighter reasoning review have separate scopes and verdicts |
| [Discovery and Recovery](docs/discovery-and-recovery.md) | The boundary between learning and controlled mutation |
| [Investigations](docs/investigations.md) | Hypotheses, isolation, evidence, and honest verdicts |
| [Document Work](docs/document-work.md) | Analysis, planning, description and clear, testable requirements |
| [Testing AI Behaviour](docs/testing-ai-behaviour.md) | Scenario isolation, oracles, adversarial cases, and stochastic results |
| [Skill Architecture](docs/skill-architecture.md) | Progressive disclosure, platform adapters, and maintenance |
| [Project Records](docs/project-records.md) | Consequence-based assurance, revision custody and review triggers |
| [Project Records Design](docs/project-records-design.md) | Observations, generalisation, alternatives and falsifiers behind the proposed standard |
| [Worked Record Traces](docs/project-records-examples.md) | Compiled, interpreted and document work using the same record structure |
| [Project Records Scenarios](docs/project-records-scenarios.md) | Adversarial cases, cold-reader trials and process cost evaluation |
| [Independent Record Audit](docs/independent-record-audit.md) | Separate assessor/worker contexts, audit references, finding responses and closure |

## Using VP with Any AI Tool

Point an assistant at the repository's root `SKILL.md`, install the repository as a skill directory, or provide `SKILL.md` as project instructions. Ask it to “use VP” for the task. The skill selects the smallest relevant set of supporting documents.

The supporting files are plain Markdown and contain no vendor-specific tool instructions. Map capability names to the host tool rather than editing the method:

| Capability in a playbook | Possible implementation |
|--------------------------|-------------------------|
| Read/search files | Built-in file tools, shell search, or IDE search |
| Ask the user | Normal conversation or a structured question interface |
| Run checks | Shell, CI, test runner, or debugger integration |
| Parallel review | Sub-agents when available; bounded sequential batches otherwise |
| Record evidence | A durable file; conformant project records use Markdown and directory bundles |

A platform adapter may add permissions or command metadata, but the canonical skill and playbooks should remain platform-neutral.

## Scope Boundary

VP defines project quality management, including governance, planning, verification, traceability, independent record assurance, maintenance, recovery and document work. Portable owner/worker/auditor responsibilities can use separate sessions and directory handoff. Persistent team orchestration software is outside this repository.

VP is a research method whose effectiveness, cost and sustained compliance require evaluation. Describing the full management lifecycle does not claim product correctness, universal reader comprehension or ISO, PRINCE2, CMM or aviation certification.

The framework's origin and extraction boundary are recorded in [ORIGIN.md](ORIGIN.md).

## Project Information

- [Contributing](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Security Policy](SECURITY.md)
- [Changelog](CHANGELOG.md)
- [Citation Metadata](CITATION.cff)
- [MIT Licence](LICENSE)
