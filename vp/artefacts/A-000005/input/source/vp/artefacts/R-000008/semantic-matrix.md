# Content-quality audit: candidate verification and finding disposition

**Assessment kind:** owner-selected documentation content quality, using Document Analysis.
**Assessor:** Codex worker /root, also author of the repairs; this is a disclosed worker content assessment, not independent Project Audit.
**Authority:** D-000012; requirements fixed in S-000002/E-000008 before edits/checks.
**Baseline:** [R-000007 content report](../R-000007/content-audit.md); exact before and after under C-000004.
**Candidate:** all 71 maintained files in C-000004 after snapshot; 64 public Markdown documents, 500 declared current headings/preambles/whole-file units. Changed-paths.json identifies 27 edited documents. Unit-count reduction reflects rewritten outlines and fence-aware parsing; no maintained file was removed.

## Scope, reading and provenance

Manual review read the primary entry documents and the complete method/architecture/records/role guides, original context, full relevant concepts, changed documents and their diff against the frozen baseline. All remaining public Markdown openings/headings and routing were inspected; specialised unchanged procedures were consulted for the process promises below. This is an orientation/coherence audit, not a sentence-by-sentence legal, scientific or code-correctness audit of every unchanged document. Mechanical inventories supplement the declared semantic reading, never expand it. Exact quoted candidate text below is extracted from the retained after source.

## Requirement-to-current-text assessment

### Q1: Complete system identity

**Observed:** README.md:3

> Verifiable Practice (VP) is a **full project quality management system for human–AI collaboration**. It defines how a project establishes its goals and authority, plans controlled work, makes justified choices, verifies results, keeps an auditable history, accepts deliverables and maintains their justification over time.

**Assessment:** The opening names the complete system and its human–AI audience; lifecycle, roles and startup immediately follow. WHY, SKILL and the main guide independently explain the same identity.

**Source/control locators:** README opening; WHY opening; SKILL opening/Manage the Whole Project; guide opening.

**Outcome:** supported for current documented purpose and source scope.

### Q2: Epistemology is a foundation

**Observed:** WHY.md:84

> ## Epistemology: the Evidence Foundation

**Assessment:** The worked example is explicitly inside a managed project. The subsequent section distinguishes observations from goals, values and authority. The concepts support the method rather than exhaust it.

**Source/control locators:** WHY Epistemology and Supporting Evidence Concepts; guide Epistemology Within the Method.

**Outcome:** supported for current documented purpose and source scope.

### Q3: Whole lifecycle and management controls

**Observed:** docs/how-vp-works.md:33

> 2. **Plan bounded stages.** Specify entry conditions, exact baseline, deliverables, independent checks, dependencies, budgets/tolerances and stop/reversal conditions. Preserve the plan baseline. Changes beyond delegation or tolerance require an authorised exception decision.

**Assessment:** Eight lifecycle actions run from root mandate to retirement; planning identifies baselines, independent checks, budgets/tolerances and stop/reversal conditions. Exceptions require authority. No test alone accepts the project.

**Source/control locators:** guide The Lifecycle and Its Gates; standard §§4/7/11.4; project playbook §§3/8.

**Outcome:** supported for current documented purpose and source scope.

### Q4: Roles, authority and tracking

**Observed:** docs/how-vp-works.md:26

> A human owner with an AI worker is common. An AI owner can coordinate under an explicit bounded mandate, including duration, reserved decisions, escalation and handoff. Humans may also perform technical work under the charter. The owner ensures tracking is done; the working AI maintains routine VP records. A worker can coordinate within already delegated authority but remains an author rather than its own independent auditor.

**Assessment:** The role table assigns management, execution/records and independent record assessment. AI owners need bounded mandates; humans can contribute technically. Coordination never makes the author an independent assessor. Zero-code is one pattern.

**Source/control locators:** guide Responsibilities and Authority; README roles; SKILL; role guide; standard §11.1.

**Outcome:** supported for current documented purpose and source scope.

### Q5: Trace, attempts, validity and custody

**Observed:** docs/how-vp-works.md:35

> 4. **Produce and challenge the work.** Open an authorised change. Set hypotheses and protocols before running evidence. Identify actual source, executable, environment and inputs for builds/runs; retain positive, negative, aborted and inconclusive attempts. Choose checks that can expose the claimed failure.

**Assessment:** Lifecycle and record-view sections connect exact unit identity to change/choice/root, protocols/build/run outcomes and current validity. Maintenance traces expiry; preservation/recovery/disposal retain owned manifests and consumer checks. Lookup arrows are expressly distinct from chronological origins.

**Source/control locators:** guide lifecycle §§4/7/8 and Documents, Directories and the Audit Trail; standard §§5–10; project playbook §§5–7/9.

**Outcome:** supported for current documented purpose and source scope.

### Q6: Concrete onboarding and explicit adoption

**Observed:** docs/how-vp-works.md:89

> ## Start a Project or Use a Bounded Task

**Assessment:** The reader is told to agree charter/mandate, copy linked templates, record root and first stage and adopt the standard for scope/time. Existing projects read six views before work; missing old history stays unknown. Bounded procedure use does not claim full conformance.

**Source/control locators:** README Start Here; guide Start a Project or Use a Bounded Task; SKILL existing vp instruction; project playbook §§1/12 standard.

**Outcome:** supported for current documented purpose and source scope.

### Q7: Separate content/product and record assessments

**Observed:** README.md:56

> - **Document analysis:** content, claims, audience, purpose and whether a document achieves its intended effect.

**Assessment:** The four assessment descriptions state what each checks. Ambiguous requests require clarification and waiting. Record conformance is separate from product acceptance; worker repairs do not close independent findings. This report is Document Analysis, not an A verdict.

**Source/control locators:** README Choose the Assessment; guide Choose the Assessment and Keep Its Verdict; audit routing; standard §11.

**Outcome:** supported for current documented purpose and source scope.

### Q8: Portable storage, no required special software

**Observed:** docs/how-vp-works.md:56

> Decisions, stages, hypotheses, protocols, builds, runs, changes, events and audits live under typed record directories. Artefacts have an owning record and a Markdown manifest explaining bytes, meaning, sources, consumers, retention and custody. Documentation is Markdown; raw logs, datasets and executables retain native formats. No database, vendor product or custom software is required. Version control and automation can assist; they do not define the meaning of the records.

**Assessment:** Markdown defines documents/manifests, directories hold bundles, raw evidence keeps native formats. Skill distribution and optional Git/automation do not become prerequisites. Portable independent sessions suffice; persistent orchestration is outside this repo.

**Source/control locators:** guide Documents, Directories and the Audit Trail/Distribution and Limits; README Using VP with Any AI Tool; standard §2.

**Outcome:** supported for current documented purpose and source scope.

### Q9: Coherent layers and focused routes

**Observed:** docs/skill-architecture.md:3

> Verifiable Practice is a full project quality management system for human–AI collaboration, distributed as a self-contained skill repository. The [method overview](how-vp-works.md) explains governance, planning, quality control/assurance, acceptance and maintenance. This architecture separates discovery, procedures, normative contracts, templates and actual project records so an AI loads the references needed for its role and task.

**Assessment:** Architecture includes instantiated vp history alongside the skill/concepts/procedures/contracts/templates. ORIGIN separates historical extraction exclusions from current portable roles. Concepts and guides have tailored overview routes without forced full loading.

**Source/control locators:** architecture Repository Layers/Project Records and Evidence; ORIGIN opening; 8 concepts; related guides.

**Outcome:** supported for current documented purpose and source scope.

### Q10: Supported promises and explicit limits

**Observed:** docs/how-vp-works.md:101

> VP is a research method. Its effectiveness, process cost and sustained compliance need evaluation; full lifecycle coverage does not establish universal comprehension or product safety. Its design draws on project-management/process/maintenance ideas without claiming ISO, PRINCE2, CMM or aviation certification. Revise the method when evidence shows it obscures responsibility, loses context, fails to detect relevant defects or consumes effort without improving decisions.

**Assessment:** Process promises route to existing normative/procedural controls; full lifecycle identity describes defined scope, not demonstrated effectiveness, certification, universal comprehension, technical correctness or historical authenticity. Fictional examples retain labels.

**Source/control locators:** guide What the System Manages/Distribution and Limits; README Scope Boundary; WHY summary; examples/scenarios introductions.

**Outcome:** supported for current documented purpose and source scope.

## CQ-001–006 dispositions

| Baseline finding | Generalised repair from D-000013 | Current evidence / outcome |
|---|---|---|
| CQ-001 undercommunicated full identity | Put purpose, lifecycle and starting actions before foundations/packaging | Q1/Q3/Q6; four primary entries explicit; addressed |
| CQ-002 flexible practice versus adopted contract | Explain why whole-project controls are needed, with explicit adoption | Q2/Q3/Q6; WHY summary + guide distinguish scope; addressed |
| CQ-003 method versus distribution/original exclusions | Show operational layer and current portable roles independently of runtime | Q8/Q9; architecture and ORIGIN preserve history; addressed |
| CQ-004 roles, tracking and inferred intent | Actor-neutral bounded mandates, worker records, separate auditor; zero-code one pattern | Q4/Q7; Goals preserves explicit instruction authority; addressed |
| CQ-005 empirical truth versus value/authority | Falsify empirical claims; review mandate/value choices through authority | Q2/Q4/Q10; WHY/Goals/Falsifiability and skill working rule aligned; addressed |
| CQ-006 component positioning | Tailored overview links and contribution identity | Q9; all eight concept introductions and affected guides; addressed |

These are worker content-finding dispositions. They do not retroactively change the baseline report or independently close any Project Audit finding.

## Changed-file reasons and coherence review

| Changed file | Purpose/continued justification |
|---|---|
| CHANGELOG.md | Communicate this full-method content and authority clarification; preserve earlier outcomes. |
| CONTRIBUTING.md | Q1/Q9 contribution purpose identifies complete management method and ongoing efficacy research. |
| ORIGIN.md | Q9 current method versus original extraction provenance; no revision/date/source evidence reconstructed. |
| README.md | Q1–Q10 primary entry: complete purpose/lifecycle/roles/startup/limits; exact content reviewed above; D-000013 choices 1–5. |
| SKILL.md | Q1–Q10 primary entry: complete purpose/lifecycle/roles/startup/limits; exact content reviewed above; D-000013 choices 1–5. |
| WHY.md | Q1–Q10 primary entry: complete purpose/lifecycle/roles/startup/limits; exact content reviewed above; D-000013 choices 1–5. |
| concepts/bullshit-detection.md | Q9 tailored component purpose and overview route; specialised procedure/illustrative limits retained; D-000013 choice 6. |
| concepts/engineering-standards.md | Q9 tailored component purpose and overview route; specialised procedure/illustrative limits retained; D-000013 choice 6. |
| concepts/falsifiability.md | Q2/Q4 empirical falsifier versus value/permission/mandatory authority; experiments do not waive mandates. |
| concepts/goals.md | Q4/Q10 source goal/authority; clarification rather than inferred replacement; bounded AI owner. |
| concepts/pte.md | Q9 tailored component purpose and overview route; specialised procedure/illustrative limits retained; D-000013 choice 6. |
| concepts/rhetoric.md | Q9 tailored component purpose and overview route; specialised procedure/illustrative limits retained; D-000013 choice 6. |
| concepts/verification-cycle.md | Q3/Q5 local cycle within complete lifecycle; recorded meaningful checks and controls, not required prior natural failure. |
| concepts/zero-code-contract.md | Q4 scope zero-code to one collaboration pattern; worker tracking/delegated technical choices, independent assessment. |
| docs/discovery-and-recovery.md | Q9 tailored component purpose and overview route; specialised procedure/illustrative limits retained; D-000013 choice 6. |
| docs/document-work.md | Q9 tailored component purpose and overview route; specialised procedure/illustrative limits retained; D-000013 choice 6. |
| docs/how-vp-works.md | Q1–Q10 primary entry: complete purpose/lifecycle/roles/startup/limits; exact content reviewed above; D-000013 choices 1–5. |
| docs/independent-record-audit.md | Q9 tailored component purpose and overview route; specialised procedure/illustrative limits retained; D-000013 choice 6. |
| docs/investigations.md | Q9 tailored component purpose and overview route; specialised procedure/illustrative limits retained; D-000013 choice 6. |
| docs/project-records-design.md | Q9/Q10 append new sourced design links while preserving historical observation/generalisation register. |
| docs/project-records-examples.md | Q9 tailored component purpose and overview route; specialised procedure/illustrative limits retained; D-000013 choice 6. |
| docs/project-records-scenarios.md | Q9 tailored component purpose and overview route; specialised procedure/illustrative limits retained; D-000013 choice 6. |
| docs/project-records.md | Q9 tailored component purpose and overview route; specialised procedure/illustrative limits retained; D-000013 choice 6. |
| docs/review-and-audit.md | Q9 tailored component purpose and overview route; specialised procedure/illustrative limits retained; D-000013 choice 6. |
| docs/skill-architecture.md | Q8/Q9 distinguish distribution layers, actual records, method responsibilities and optional runtime. |
| docs/testing-ai-behaviour.md | Q9 tailored component purpose and overview route; specialised procedure/illustrative limits retained; D-000013 choice 6. |
| templates/project-records/README.md | Q9 tailored component purpose and overview route; specialised procedure/illustrative limits retained; D-000013 choice 6. |

## Mechanical observations and contrary controls

R-000008 results.json records all 12 members with actual argv, source/instrument/runtime/dependency identities, raw stdout/stderr and expected status. Every candidate member met its declared bounded criterion; Python/dependencies and 71 live product bytes remained stable. Structural check covers all maintained Markdown local destinations/fences/routes and template fields; frontmatter validator passed. Teaching/example results preserve bounded behaviour at optimisation levels 0/1/2 and email substring outcomes. Executable-language fenced examples remain byte-identical. No compiled build applies.

The exact identity checker rejects the preserved baseline and an isolated removed README identity statement. The exact coverage checker rejects an actually removed unit row and a wrong digest. Expected failing controls are retained, not relabelled as candidate failures or replaced by set inequality. Neither marker detection nor unchanged examples prove semantic understanding; the direct Q/CQ assessment does the content work. Same-host custody verification is captured separately in custody.json under this open R before sealing.

## Rhetoric, incentives and alternative interpretation

The baseline could be read accurately by a careful reader following records/standard links; the full management implementation already existed. Its concepts-first opening and skill framing made a partial reading more likely. This is an observed communication mismatch, not evidence of concealed intent or deception. The revised full-system label names concrete controls and immediately presents limits; it is not a borrowed certification claim. Authority (mandate), value (purpose), and empirical support (checks) are now separated where the earlier content blurred them.

Human/AI newcomers benefit from explicit starting actions and responsibility boundaries; maintainers bear a documentation/record cost. This run measures actual bounded artefact checks, not the cost-benefit of sustained VP operation. Specialised readers retain focused routes; they are not required to load every concept before a task.

## Verdict and remaining unknowns

For this exact candidate and stated communication goal, the primary entry documents now describe a full project quality management system for human–AI collaboration, with epistemology as its evidence foundation. Q1–Q10 have meaningful text and supporting existing procedure/control routes; CQ-001–006 are addressed in the worker content assessment. General reader comprehension, sustained AI compliance, scientific truth of all historical rhetoric, process efficiency and product safety remain unmeasured. Current changed-source record acceptance is still pending a separately commissioned independent Project Audit and stage-exit choice.
