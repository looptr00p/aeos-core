# AEOS Core v0.3

AI Engineering Operating System. Governance-first, repo-driven, markdown-first, human-governed, deterministic, auditable, reproducible.

## What AEOS Actually Is

AEOS is not "run" as an autonomous system. It has no daemon, no orchestration engine, no runtime agents, and no self-governing logic.

AEOS is operated through **governed sessions over real projects**. Each session produces markdown artifacts that are committed to git, validated by deterministic scripts, and reviewed by humans.

AEOS operates through:
- **Repository governance** — rules, protocols, and workflows defined in markdown files.
- **Operational workflows** — structured lifecycles from objective creation through closure.
- **Markdown artifacts** — objectives, tasks, reviews, audits, handoffs, incidents, escalations, ADRs.
- **Longitudinal operational sessions** — discrete work sessions governed by explicit objectives.
- **OpenCode/LLM-assisted cognition** — AI-assisted engineering within strict governance boundaries.
- **Human review** — no artifact is approved without human judgment.

**AEOS is not "run." It is operated.** Each operational session follows the same pattern: define an objective, create tasks, produce artifacts, validate with lint, review, audit, and close with a handoff. The repository state is the system state.

## Repository Structure

| Directory | Purpose |
|-----------|---------|
| `governance/` | Rules, constraints, permission model, safety rules, severity model, state classification policy |
| `protocols/` | How work is done — task, review, context, memory, handoff, incident, and ADR protocols |
| `templates/` | Reusable artifact templates — objectives, tasks, reviews, audits, handoffs, incidents, escalations |
| `workflows/` | End-to-end process definitions — feature, bugfix, architecture change, audit, incident, research |
| `agents/` | Agent definitions and registry — director, architect, implementer, reviewer, auditor, QA, documentation |
| `memory/` | Explicit institutional memory — objectives, tasks, reviews, audits, handoffs, incidents, decisions, research |
| `memory/objectives/` | OBJ-XXX files — operational goals with status (ACTIVE/DRAFT/CLOSED) |
| `memory/decisions/` | ADR-XXX files — architecture decision records |
| `memory/incidents/` | INC-XXX and ESC-XXX files — incidents and escalations |
| `memory/research/` | OPR-XXX and GHR-XXX files — operational reports and governance health reports |
| `docs/` | Operational documentation — learnings, design documents, baselines, simulation frameworks |
| `scripts/` | Deterministic validation — `aeos_lint.py` checks repository integrity |
| `tests/` | Repository structure validation — pytest tests for governance, protocols, templates, agents, workflows |
| `gpt_knowledge_base/` | Curated cognition package for external consumption — repository-grounded, not volatile state |
| `dashboard/` | Read-only observability layer — visualizes repository state, does not make governance decisions |

## Why AEOS Exists

AI-assisted engineering introduces risks that traditional development workflows do not address: autonomous behavior without accountability, hidden state, uncontrolled scope expansion, missing audit trails, and non-reproducible outputs. AEOS provides a framework that keeps AI-assisted engineering human-governed and auditable.

## Governance-First Philosophy

Governance precedes implementation. Before any work begins:

1. Governance documents define the rules (`governance/`).
2. Protocols define how work is done (`protocols/`).
3. Templates standardize artifacts (`templates/`).
4. Agents operate within defined boundaries (`agents/`).
5. Workflows define the process (`workflows/`).

Governance cannot be bypassed. Critical changes require human approval.

## Workflow-First Philosophy

All work follows defined workflows with entry criteria, validation gates, review requirements, and exit criteria. See `workflows/` for available workflows.

## Human-in-the-Loop Operation

No agent may self-approve. Critical changes require human approval. Escalations route to human review. Humans retain ultimate decision authority.

## Explicit Memory Model

All institutional memory is stored as markdown files in `memory/`, is human-readable, git-versioned, auditable, and reproducible. No hidden memory, embeddings, or autonomous memory mutation is allowed.

## Reproducibility Principles

All outputs must be reproducible from git history, traceable to originating objectives and tasks, documented with explicit artifacts, and validated through defined gates. No hidden state or implicit behavior is allowed.

## Auditability Principles

All operations must be traceable to specific agents, tasks, and objectives; documented with review and audit artifacts; subject to governance compliance checks; and preserved in git history without deletion.

## Repository Overview

See [Repository Structure](#repository-structure) above for directory purposes.

Key artifact counts at baseline v0.3:
- 8 governance files, 7 protocols, 12 templates, 6 workflows, 7 agents
- 8 objectives (2 CLOSED, 3 ACTIVE, 3 DRAFT), 3 ADRs (all PROPOSED)
- 11 lint checks (all passing), 14 test files defined

## v0.3 Additions

AEOS Core v0.3 introduces operational execution readiness:

- **Governance Severity Model** (`governance/GOVERNANCE_SEVERITY_MODEL.md`) — [IMPLEMENTED] classifies governance violations as LOW, MEDIUM, HIGH, or CRITICAL with defined response requirements.
- **Escalation Classification** (`templates/escalation_template.md`) — [IMPLEMENTED] standardized escalation template with severity, impact, and resolution tracking.
- **Operational Review Cadence** (`docs/REVIEW_CADENCE.md`) — [IMPLEMENTED] defines daily, weekly, monthly, and quarterly review cycles.
- **Governance Health Reporting** (`templates/governance_health_report_template.md`) — [IMPLEMENTED] reusable template for governance health assessment.
- **Operational Lifecycle Examples** (`docs/OPERATIONAL_EXAMPLES.md`) — [IMPLEMENTED] complete realistic examples of all AEOS artifact lifecycles with traceability.
- **State Classification Policy** (`governance/STATE_CLASSIFICATION_POLICY.md`) — [IMPLEMENTED] defines operational states (IMPLEMENTED, EXPERIMENTAL, PROPOSED, STRATEGIC) to prevent capability inflation and state ambiguity.

AEOS Core v0.3 still does NOT include:

- Orchestration runtime.
- Autonomous workflows.
- Runtime agents.
- Hidden memory.
- Distributed execution.
- Workflow execution engines.

## Running AEOS Locally

AEOS is **not** a daemon, SaaS platform, autonomous agent system, or orchestration runtime.

AEOS is operated through:
- Repository state (markdown governance artifacts)
- Deterministic validation (`aeos_lint.py`)
- OpenCode sessions (human-in-the-loop)
- Human review and approval
- Dashboard observability (read-only)

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/looptr00p/aeos-core.git
cd aeos-core

# 2. Install Python dependencies
pip install pytest pyyaml

# 3. Run lint/validation
python3 scripts/aeos_lint.py

# 4. (Optional) Run pytest validation
pytest tests/ -v

# 5. Install dashboard dependencies
cd dashboard
npm install

# 6. Generate dashboard data from repository markdown
npm run scan

# 7. Start dashboard locally (opens browser)
npm run dev

# 8. Begin an AEOS operational session using OpenCode
# All governance work happens through markdown artifacts, not the dashboard
```

### How an Operational Session Works

1. **Define an objective** — Create an OBJ-XXX file in `memory/objectives/` with title, description, and acceptance criteria.
2. **Create tasks** — Create TASK-XXX files in `memory/tasks/` linked to the objective.
3. **Work through tasks** — Implement changes, produce artifacts, follow the appropriate workflow from `workflows/`.
4. **Validate** — Run `python3 scripts/aeos_lint.py` to verify repository integrity.
5. **Review** — Create REV-XXX files in `memory/reviews/` with findings.
6. **Audit** — Create AUD-XXX files in `memory/audits/` with compliance checks.
7. **Handoff** — Create HND-XXX files in `memory/handoffs/` documenting decisions, risks, and next steps.
8. **Commit** — All artifacts are committed to git. The repository state is the system state.
9. **Close** — Update objective status to CLOSED when acceptance criteria are met.

### Dashboard

The [dashboard](dashboard/) is a read-only observability layer. It visualizes repository-grounded governance state but does not make governance decisions. See [dashboard/README.md](dashboard/README.md) for details.

The dashboard shows:
- Governance counts and objective/ADR status
- State classification view (IMPLEMENTED/EXPERIMENTAL/PROPOSED/STRATEGIC)
- Baseline information and operational risks
- All governance documents, protocols, templates, and workflows

Dashboard data is generated by scanning repository markdown — it is never a source of truth.

## Lifecycle

The official AEOS Core lifecycle:

```
Objective
  -> ADR
  -> Task Definition
  -> Agent Assignment
  -> Implementation
  -> Review
  -> Audit
  -> CI Validation
  -> Handoff
  -> Memory Update
  -> Close
```

Each stage produces explicit artifacts. No stage may be skipped.

## Governance Boundaries

- No agent may self-approve.
- Governance cannot be bypassed.
- Critical changes require human approval.
- All workflows require handoff artifacts.
- Memory updates must be explicit and traceable.
- Audit history must never be deleted.
- No unrestricted permissions are allowed.

## Operational Constraints

- Agents operate within assigned permission levels.
- Scope expansion requires new objective and human approval.
- Escalation is mandatory when requirements are unclear.
- All decisions must reference explicit artifacts.
- All workflows must terminate explicitly.

## Explicit Non-Goals

AEOS Core v0.3 is NOT:

- An autonomous execution system.
- A hidden memory system.
- A self-modifying agent system.
- An uncontrolled orchestration runtime.
- An autonomous approval system.
- A SaaS platform.
- A chatbot platform.
- A workflow execution engine.
- A cloud platform.
- A distributed runtime.
- A runtime agent system.

AEOS Core v0.3 does NOT execute autonomous workflows.

## Documentation

- [AEOS Overview](docs/AEOS_OVERVIEW.md)
- [Operating Model](docs/OPERATING_MODEL.md)
- [MVP Scope](docs/MVP_SCOPE.md)
- [Governance Continuity](docs/GOVERNANCE_CONTINUITY.md)
- [Review Cadence](docs/REVIEW_CADENCE.md)
- [Operational Examples](docs/OPERATIONAL_EXAMPLES.md)

## Current Phase

**Phase 0: Governance/Bootstrap**

See [PHASE_POLICY.md](governance/PHASE_POLICY.md) for phase definitions.

## Repository Role

This repository is the **AEOS Experimental Governance Lab**.

- `aeos-core-opencode` is the canonical operational base.
- This repository is used for governance, enforcement, lifecycle, traceability, and validation experiments.
- Experiments are not canonical by default.
- All porting to `aeos-core-opencode` requires explicit review, validation evidence, and human approval.
- No autonomous runtime exists in this repository.

## Operational State Classification

All AEOS capabilities are classified using explicit operational states:

- **IMPLEMENTED** — exists in repository, validated, operational.
- **EXPERIMENTAL** — defined and tested, not yet stable.
- **PROPOSED** — documented direction, not yet implemented.
- **STRATEGIC** — long-term vision, no active work.

Use explicit operational state classification where implementation maturity may be ambiguous. See `governance/STATE_CLASSIFICATION_POLICY.md`.

## Governance Baseline

A formal governance stabilization checkpoint is documented in [GOVERNANCE_BASELINE_v0.3.md](docs/GOVERNANCE_BASELINE_v0.3.md). It preserves a known-good operational state for rollback, drift comparison, and longitudinal analysis.
