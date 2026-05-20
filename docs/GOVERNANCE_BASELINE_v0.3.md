# AEOS Governance Baseline v0.3

**Date**: 2026-05-20
**Repository**: AEOS Core opencode
**Phase**: Phase 0 (Governance/Bootstrap)
**Baseline Type**: Governance stabilization checkpoint

---

## Purpose

This baseline preserves a known-good operational state of AEOS Core at v0.3. It exists to:

- **Preserve operational clarity before future expansion introduces additional governance pressure and architectural complexity.**
- Provide a rollback and recovery reference point.
- Enable future governance drift comparison against a documented low-entropy state.
- Support governance survivability analysis through longitudinal comparison.
- Anchor future operational reviews to a concrete reference point.
- Preserve epistemic and operational clarity achieved through the State Classification Policy.
- Reduce future governance ambiguity by documenting what exists, what is experimental, and what is proposed.

Low-entropy states matter because governance systems naturally accumulate complexity. Each new enforcement layer, metric, simulation, or policy adds cognitive load. Without periodic stabilization checkpoints, the repository drifts toward governance density that exceeds operational utility. This baseline captures the system at a point where governance clarity is high, enforcement is intentionally light, and epistemic distinctions are explicit.

Governance stabilization matters because it separates what has been validated through operational use from what is designed but untested. Without stabilization, proposed systems are mistaken for operational capabilities, and experimental findings are mistaken for enforced policy.

Epistemic clarity matters because governance legitimacy depends on honest representation of operational maturity. A system that claims more than it implements loses trust. A system that distinguishes clearly between what exists and what is planned retains trust even when incomplete.

Recoverable checkpoints matter because governance evolution is not linear. Future changes may introduce complexity that reduces operational usability. Having a documented baseline enables comparison: "Was the system clearer before or after this change?" Without baselines, drift is invisible.

Longitudinal comparison matters because governance quality cannot be assessed from a single snapshot. It requires comparison across time. This baseline provides the first formal comparison point for future AEOS governance audits.

---

## Baseline State Classification

The following classification reflects repository evidence at the time of baseline capture. Categories are not blurred.

### IMPLEMENTED

Repository-backed, active, and verifiable:

- **State Classification Policy** (`governance/STATE_CLASSIFICATION_POLICY.md`) — 4-state operational maturity model active.
- **Governance framework** — 8 governance files, 7 protocols, 13 templates, 6 workflows, 8 agent definitions.
- **Lifecycle system** — objectives, tasks, reviews, audits, handoffs, incidents, escalations with explicit state transitions.
- **Traceability system** — OBJ-XXX, TASK-XXX, REV-XXX, AUD-XXX, HND-XXX, INC-XXX, ESC-XXX, ADR-XXX with cross-reference validation.
- **Lint validation** (`scripts/aeos_lint.py`) — 11 deterministic checks, all passing.
- **Test suite** — 11 root-level governance validation tests + 3 experimental lab tests.
- **CI workflow** (`.github/workflows/aeos-validation.yml`) — executes experimental lab tests and lint on push.
- **Explicit memory model** — all institutional memory as markdown files in `memory/`, git-versioned, human-readable.
- **Repository truth supremacy** — repository is declared single source of truth; no hidden state, no runtime dependencies.
- **Human approval authority** — no agent may self-approve; critical changes require human approval.
- **Severity model** (`governance/GOVERNANCE_SEVERITY_MODEL.md`) — LOW/MEDIUM/HIGH/CRITICAL classification with response requirements.
- **Escalation policy** (`governance/ESCALATION_POLICY.md`) — escalation lifecycle with severity tracking.
- **Safety rules** (`governance/SAFETY_RULES.md`) — explicit prohibitions on autonomous behavior, hidden memory, scope expansion.
- **Permission model** (`governance/PERMISSION_MODEL.md`) — 4-level permission system (UNRESTRICTED, GOVERNANCE_READER, GOVERNANCE_WRITER, GOVERNANCE_ADMIN).
- **Porting policy** (`aeos-core/governance/PORTING_POLICY.md`) — governs artifact transfer between experimental lab and canonical base.
- **State-labeled documentation** — 14 of 20 docs in `docs/` carry explicit operational state labels.
- **Governance dashboard** — read-only observability layer operational. Vite dev server validated. Scanner generates repository-grounded JSON.
- **Operational session boot sequence** — documented in README: sync → validate → observe → operate.
- **GPT Knowledge Base** — 59-file curated cognition package for external consumption, repository-grounded.

### EXPERIMENTAL

Behavioral normalization and operational validation still under evaluation:

- **Repository-wide behavioral normalization** — state classification adoption is spreading organically but not universally enforced.
- **Governance pressure simulation** — 8 descriptive scenarios (S-001 through S-008) defined in `docs/GOVERNANCE_PRESSURE_SIMULATION.md`. Descriptive models, not executable simulations.
- **Governance metrics framework** — 12 deterministic metrics (M-001 through M-012) defined in `docs/GOVERNANCE_METRICS_FRAMEWORK.md`. 5 of 12 metrics cannot be calculated due to data gaps.
- **Governance dashboard template** — markdown-first dashboard template defined but not yet populated with longitudinal data.
- **Operational learnings** — 5 learnings documents from real operational cycles (concurrent operations, debt recovery, stabilization, external validation, real operations). These are retrospective findings, not enforced policy.
- **Epistemic governance layer** — state classification policy is implemented, but its behavioral effects are still being observed.
- **Operational ergonomics** — findings from operational validation cycles. What should remain manual vs. mechanically assisted.
- **Review minimization guidance** — reduces review type proliferation. Under operational evaluation.
- **Workflow tiering guidance** — reduces governance overhead for low-risk work. Under operational evaluation.
- **Operating model** — strategic doctrine for AEOS roles, responsibilities, and operational constraints.

### PROPOSED

Future enforcement, observability, and scaling concepts not yet operationally implemented:

- **Governance Enforcement Layer** (OBJ-007, ADR-002) — 10 new lint checks, approval record artifacts (APR-XXX), lifecycle transition logging. Designed but not implemented.
- **Governance Pressure Observability** (OBJ-008, ADR-003) — metrics calculation, dashboard population, longitudinal tracking. Framework defined, not operational.
- **AEOS MVP vNext** (`docs/AEOS_VNEXT_DESIGN.md`) — scalable design addressing 5 core bottlenecks. Roadmap, not implementation.
- **CI enforcement expansion** — proposed to run root-level tests, add GitHub environment protection gates. Not implemented.
- **ADR enforcement** — ADR_PROTOCOL.md requires ADRs for governance changes, but no automated check validates compliance.
- **Approval record system** — template and directory exist (`memory/approvals/`), but no operational requirement or enforcement.

### STRATEGIC

Long-horizon governance survivability vision:

- **Governance continuity** (`docs/GOVERNANCE_CONTINUITY.md`) — philosophy of governance consistency, explicit memory, repo-driven traceability, human-readable artifacts.
- **AEOS operating model** — governance-first, repo-driven, markdown-first, human-governed, deterministic, auditable, reproducible.
- **Anti-entropy operational discipline** — preference for low governance density, lightweight enforcement, behavioral normalization over aggressive policy expansion.
- **Repository truth supremacy doctrine** — repository as single source of truth, no hidden state, no runtime dependencies, all outputs reproducible from git history.

---

## Repository Snapshot

All metrics are derived from repository evidence at baseline capture date. No estimation. No inferred metrics.

### Governance Structure

| Category | Count | Location |
|----------|-------|----------|
| Governance files | 8 | `governance/` |
| Protocols | 7 | `protocols/` |
| Templates | 13 | `templates/` |
| Workflows | 6 | `workflows/` |
| Agent definitions | 8 | `agents/` |

### Operational Memory

| Artifact Type | Count | Location |
|---------------|-------|----------|
| Objectives | 8 | `memory/objectives/` |
| Tasks | 11 | `memory/tasks/` |
| Reviews | 10 | `memory/reviews/` |
| Audits | 5 | `memory/audits/` |
| Handoffs | 7 | `memory/handoffs/` |
| Incidents + Escalations | 6 | `memory/incidents/` |
| Operational/Governance Reports | 13 | `memory/research/` |
| Architecture Decisions | 3 | `memory/decisions/` |
| Approval Records | 1 | `memory/approvals/` |

### Objective Status

| Status | Count | IDs |
|--------|-------|-----|
| CLOSED | 2 | OBJ-001, OBJ-002 |
| ACTIVE | 3 | OBJ-003, OBJ-004, OBJ-005 |
| DRAFT | 3 | OBJ-006, OBJ-007, OBJ-008 |

### ADR Status

| Status | Count | IDs |
|--------|-------|-----|
| PROPOSED | 3 | ADR-001, ADR-002, ADR-003 |

### Validation

| Category | Count | Location |
|----------|-------|----------|
| Root-level tests | 11 | `tests/` |
| Experimental lab tests | 3 | `aeos-core/tests/` |
| Lint checks | 11 | `scripts/aeos_lint.py` |
| Lint status | ALL PASS | — |

### Documentation

| Category | Count | Notes |
|----------|-------|-------|
| Total docs | 20 | `docs/` |
| State-classified docs | 14 | 70% of docs carry explicit operational state labels |
| Knowledge base files | 59 | `gpt_knowledge_base/` |

### Uncertainty

- **Test execution**: pytest is not installed in the current environment. Test pass/fail status cannot be locally verified. CI workflow is configured to run tests on push, but CI execution history is not available in repository state.
- **ADR-001 status**: The file exists and is marked PROPOSED, but it was created before the current ADR numbering convention. Its relationship to current objectives is documented but not formally linked.

---

## Current Operational Characteristics

The following operational qualities are supported by repository evidence:

- **Governance-first** — governance files, protocols, and templates exist before implementation artifacts.
- **Repository-driven** — all state, memory, and decisions stored in git. No external dependencies.
- **Markdown-first** — all artifacts are human-readable markdown. No binary state, no serialized formats.
- **Human-governed** — no agent may self-approve. Human approval authority is explicit in AGENTS.md and SAFETY_RULES.md.
- **Lifecycle-aware** — objectives, tasks, reviews, audits, and handoffs follow explicit state transitions.
- **Anti-entropy oriented** — preference for low governance density, lightweight enforcement, and behavioral normalization over aggressive policy expansion.
- **Explicit operational semantics** — state classification policy distinguishes IMPLEMENTED, EXPERIMENTAL, PROPOSED, and STRATEGIC.
- **Epistemic governance enabled** — operational maturity is classified, not assumed. Lessons learned are not automatically enforced.
- **Operationally auditable** — traceability IDs link all artifacts. Lint validates cross-references.
- **Deterministic where possible** — lint checks are file-based, deterministic, locally executable. No probabilistic reasoning.

---

## Known Operational Strengths

The following strengths are supported by repository evidence:

- **Explicit state classification** — 9 of 19 docs in `docs/` carry operational state labels. Policy file exists and is active.
- **Repository truth supremacy** — repository is declared single source of truth. GPT Knowledge Base explicitly defers to repository for current state.
- **Low orchestration complexity** — no runtime, no workflow engine, no distributed systems, no hidden state. Single lint script, 11 checks.
- **Lightweight governance** — 8 governance files for a framework of this scope. Enforcement remains PROPOSED, not implemented.
- **Operational auditability** — 8 objective types, 11 tasks, 10 reviews, 5 audits, 7 handoffs, all traceable via explicit IDs.
- **Reviewer clarity** — review minimization guidance and workflow tiering reduce overhead for low-risk changes.
- **Explicit lifecycle semantics** — objectives, tasks, reviews, audits, and handoffs follow documented state transitions.
- **Low hidden-state dependency** — all memory is markdown in `memory/`. No databases, no vector stores, no runtime state machines.
- **Governance readability** — all governance files are short, human-readable markdown. No complex configuration languages.
- **Recoverable checkpoint** — this baseline provides a documented reference state for future drift comparison.

---

## Known Operational Risks

The following operational risks are visible from repository structure and governance state:

- **Knowledge base drift** — `gpt_knowledge_base/` contains 59 files mirrored from the repository. State labels added to `docs/` after KB creation are not reflected in KB copies. If KB is consumed independently, epistemic clarity is reduced.
- **Governance inflation pressure** — 5 governance commits in a single day (2026-05-19). Concentrated governance activity can create the appearance of maturity acceleration. The commits are correct (adding labels, not capabilities), but the pattern could normalize rapid governance changes.
- **Semantic inconsistency risk** — README.md uses `[IMPLEMENTED]` inline tags; docs use `**Operational State**: IMPLEMENTED` metadata fields. CURRENT_CAPABILITY_MATRIX.md uses a 5-state vocabulary (IMPLEMENTED/DEFINED/UNVERIFIED/PARTIAL/NOT PRESENT) that does not map cleanly to the policy's 4 states.
- **Contributor scaling pressure** — all governance work to date has been performed by a single human operator. Multi-contributor governance consistency has not been validated.
- **Policy ritualization risk** — state labels are currently applied with explicit rationale in commit messages. If future labeling becomes mechanical (label added without explanation), ritualization has begun.
- **Operational review bottleneck** — 3 ACTIVE objectives (OBJ-003, OBJ-004, OBJ-005) with 5 IN_PROGRESS tasks compete for 2 reviewers (reviewer-agent, auditor-agent). Reviewer saturation is 0.83 (CRITICAL threshold: >0.8).
- **Future enforcement complexity** — OBJ-007 proposes 10 new lint checks. If implemented, total lint checks would increase from 11 to 21. Governance enforcement complexity would nearly double.
- **Epistemic classification drift** — over time, the boundary between EXPERIMENTAL and IMPLEMENTED may blur as experimental findings accumulate. Without periodic re-evaluation, experimental documents may be treated as implemented policy by default.
- **CI gap** — CI workflow runs `aeos-core/tests` (3 tests) but not root `tests/` (11 tests). Governance validation suite is not enforced on push/PR.

---

## Recovery Guidance

This baseline should be used as follows:

- **Rollback reference** — if future governance changes introduce complexity that reduces operational usability, this baseline documents the known-good state to which the repository can be compared or restored.
- **Governance drift comparison** — future audits should compare current repository state against this baseline. Metrics that have changed (file counts, objective statuses, lint check counts, state-labeled document counts) indicate governance evolution. Metrics that should not have changed (governance file count, agent count, permission model structure) indicate potential drift.
- **Longitudinal operational analysis** — this baseline provides the first formal comparison point. Future baselines (if created) should reference this one to establish a governance evolution timeline.
- **Survivability evaluation** — if AEOS governance becomes too complex to maintain, this baseline demonstrates that a simpler, functional state existed. Governance survivability depends on the ability to return to a simpler state when complexity exceeds utility.
- **Future governance audits** — auditors should use this baseline to assess whether governance changes since v0.3 have improved or degraded operational clarity.
- **Operational coherence comparison** — this baseline documents a state where governance clarity is high and enforcement is light. Future states should be evaluated against this standard: does the change improve clarity or add complexity?

**This baseline is intended to preserve recoverability and governance clarity, not to block evolution.**

---

## Baseline Preservation Guidance

Baselines should not proliferate excessively. Each baseline adds to governance documentation and creates a new reference point that future audits must consider.

Baseline creation should remain intentional. A baseline should only be created when operational coherence materially improves — when the repository has reached a state that is demonstrably clearer, more stable, or more recoverable than the previous baseline.

Baselines exist to preserve recoverable low-entropy states. They are not ceremonial governance artifacts. They are practical recovery anchors.

Governance snapshots should not become ceremonial governance artifacts. A baseline that is never referenced is governance debt. A baseline that is referenced during drift comparison is governance value.

**A baseline should only be created when operational coherence materially improves.**

---

## Repository Tag Recommendation

The following git tag is recommended for this baseline:

```
aeos-v0.3-governance-baseline
```

This tag should point to the commit at which this baseline document is merged. It provides a machine-readable reference point for rollback, comparison, and audit purposes.

---

## Final Principles

- **Operational clarity over governance density** — clear, lightweight governance is more valuable than comprehensive, complex governance.
- **Survivability over sophistication** — a governance system that can survive complexity pressure is more valuable than one that is sophisticated but fragile.
- **Repository truth over conceptual inflation** — what exists in the repository is real. What exists only in documentation is proposed.
- **Governance legitimacy through epistemic clarity** — governance is legitimate only when it honestly represents its own operational maturity.
- **Recoverability over architectural expansion** — the ability to return to a known-good state is more valuable than the ability to add new capabilities.
- **Observability over autonomy** — understanding how governance behaves under pressure is more valuable than automating governance decisions.
