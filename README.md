# AEOS Core v0.4 — AI Engineering Operating System

Governance-first, repo-driven, markdown-first, human-governed, deterministic, auditable, reproducible.

**AEOS is not "run." It is operated.** Each operational session follows the same pattern: define an objective, create tasks, produce artifacts, validate with lint, review, audit, and close with a handoff. The repository state is the system state.

---

## What AEOS Actually Is

AEOS is **organizational cognition infrastructure** for AI-assisted software development. It preserves strategic and operational continuity while multiple intelligences (human and artificial) participate in a project.

The problem AEOS solves:

```
how do I keep a project coherent after:
- 500 conversations
- 20 features
- multiple models
- direction changes
- contextual debt
- replaced agents
- mutated prompts
- partial memory
```

AEOS operates through:
- **Repository governance** — rules, protocols, and workflows defined in markdown files.
- **State graph workflows** — bidirectional feedback loops, not linear pipelines.
- **Markdown artifacts** — objectives, tasks, reviews, audits, handoffs, incidents, escalations, ADRs, state transitions.
- **Longitudinal operational sessions** — discrete work sessions governed by explicit objectives.
- **LLM-assisted cognition** — AI-assisted engineering within strict governance boundaries.
- **Human review** — no artifact is approved without human judgment.

---

## Architecture: 3 Layers

```
┌─────────────────────────────────────────────────────┐
│  Layer 1: Cognitive Governance Layer  ← THE CORE    │
│  Memory, ADRs, handoffs, state, protocols            │
├─────────────────────────────────────────────────────┤
│  Layer 2: Agent Orchestration Layer                  │
│  Director, architect, implementer, reviewer, etc.    │
├─────────────────────────────────────────────────────┤
│  Layer 3: Execution Layer                            │
│  OpenCode, Claude Code, Cursor, GPTs, Gemini...       │
└─────────────────────────────────────────────────────┘
```

**Key principle:** Layers 2 and 3 are replaceable. Layer 1 is permanent.

---

## Repository Structure

| Directory | Purpose |
|-----------|---------|
| `governance/` | Rules, constraints, permission model, safety rules, severity model, state classification policy |
| `protocols/` | How work is done — task, review, context, memory, handoff, incident, ADR, state transition protocols |
| `templates/` | Reusable artifact templates — objectives, tasks, reviews, audits, handoffs, incidents, escalations |
| `workflows/` | End-to-end process definitions as **state graphs** — feature, bugfix, architecture change, audit, incident, research |
| `agents/` | Agent definitions and registry — director, architect, implementer, reviewer, auditor, QA, documentation |
| `memory/` | Explicit institutional memory — objectives, tasks, reviews, audits, handoffs, incidents, decisions, research, state-log |
| `memory/state-log/` | ST-XXX files — state transition records |
| `docs/` | Operational documentation — learnings, design documents, baselines, simulation frameworks |
| `scripts/` | Deterministic validation — `aeos_lint.py` checks repository integrity |
| `tests/` | Repository structure validation — pytest tests for governance, protocols, templates, agents, workflows |
| `.opencode/` | OpenCode integration — agent definitions, config, governance skill |
| `dashboard/` | Read-only observability layer — visualizes repository state |
| `template/` | **Reusable AEOS template** — apply to any new project |

---

## Reusable Template

AEOS v0.4 includes a **reusable template** that can be applied to any project:

```bash
cp -r template/.aegos ./
cp -r template/.opencode ./
cp -r template/memory ./
cp template/scripts/aeos_lint.py ./scripts/
cp template/AGENTS.md ./
cp template/project-charter.md ./
```

Then fill in `project-charter.md` and validate:

```bash
python3 scripts/aeos_lint.py
```

See `template/README.md` for full instructions and governance profiles (Full, Standard, Lite).

---

## Why AEOS Exists

AI-assisted engineering introduces risks that traditional development workflows do not address: autonomous behavior without accountability, hidden state, uncontrolled scope expansion, missing audit trails, and non-reproducible outputs. AEOS provides a framework that keeps AI-assisted engineering human-governed and auditable.

---

## Governance-First Philosophy

Governance precedes implementation. Before any work begins:

1. Governance documents define the rules (`governance/`).
2. Protocols define how work is done (`protocols/`).
3. Templates standardize artifacts (`templates/`).
4. Agents operate within defined boundaries (`agents/`).
5. Workflows define the process (`workflows/`).

Governance cannot be bypassed. Critical changes require human approval.

---

## State Graph Workflows

Workflows are **NOT linear pipelines**. They are state graphs with bidirectional feedback loops:

```
director → architect → implementer → reviewer → qa → auditor → documentation → director
                ↑          ↑            ↑         ↑       ↑
                │          └────────────┘         │       │
                └─────────────────────────────────┘       │
                        feedback loops                     │
                                                          │
                        escalations ←────────────────────┘
```

See `workflows/state_graph.md` for the complete graph and `protocols/STATE_TRANSITION_PROTOCOL.md` for transition recording rules.

---

## Human-in-the-Loop Operation

No agent may self-approve. Critical changes require human approval. Escalations route to human review. Humans retain ultimate decision authority.

---

## Explicit Memory Model

All institutional memory is stored as markdown files in `memory/`, is human-readable, git-versioned, auditable, and reproducible. No hidden memory, embeddings, or autonomous memory mutation is allowed.

**The memory of the project lives in the project.**

---

## Reproducibility Principles

All outputs must be reproducible from git history, traceable to originating objectives and tasks, documented with explicit artifacts, and validated through defined gates. No hidden state or implicit behavior is allowed.

---

## Auditability Principles

All operations must be traceable to specific agents, tasks, and objectives; documented with review and audit artifacts; subject to governance compliance checks; and preserved in git history without deletion.

---

## AEOS Session Boot Sequence

```
sync → validate → observe → operate
```

### 1. Sync repository

```bash
git pull
```

### 2. Validate repository truth

```bash
pip install pytest pyyaml
pytest tests/
python3 scripts/aeos_lint.py
```

### 3. Operate

Begin the operational session. Define an objective, follow the state graph workflow.

### How an Operational Session Works

1. **Define an objective** — Create an OBJ-XXX file in `memory/objectives/` with title, description, and acceptance criteria.
2. **Create tasks** — Create TASK-XXX files in `memory/tasks/` linked to the objective.
3. **Work through tasks** — Implement changes, produce artifacts, follow the appropriate workflow from `workflows/`.
4. **Validate** — Run `python3 scripts/aeos_lint.py` to verify repository integrity.
5. **Review** — Create REV-XXX files in `memory/reviews/` with findings.
6. **Audit** — Create AUD-XXX files in `memory/audits/` with compliance checks.
7. **Handoff** — Create HND-XXX files in `memory/handoffs/` documenting decisions, risks, and next steps.
8. **Log state transitions** — Create ST-XXX files in `memory/state-log/` for each transition.
9. **Commit** — All artifacts are committed to git. The repository state is the system state.
10. **Close** — Update objective status to CLOSED when acceptance criteria are met.

---

## Lifecycle

The official AEOS Core lifecycle (as a state graph):

```
Objective → ADR → Task Definition → Agent Assignment → Implementation → Review → Audit → CI Validation → Handoff → Memory Update → Close
```

Each stage produces explicit artifacts. No stage may be skipped. Feedback loops allow returning to previous stages when issues are found.

---

## Governance Boundaries

- No agent may self-approve.
- Governance cannot be bypassed.
- Critical changes require human approval.
- All workflows require handoff artifacts.
- Memory updates must be explicit and traceable.
- Audit history must never be deleted.
- No unrestricted permissions are allowed.

---

## Operational Constraints

- Agents operate within assigned permission levels.
- Scope expansion requires new objective and human approval.
- Escalation is mandatory when requirements are unclear.
- All decisions must reference explicit artifacts.
- All workflows must terminate explicitly.

---

## Explicit Non-Goals

AEOS Core v0.4 is NOT:

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

---

## Documentation

- [AEOS Constitutional Core](docs/AEOS_CONSTITUTIONAL_CORE.md) — shared operational doctrine
- [AEOS Overview](docs/AEOS_OVERVIEW.md)
- [Operating Model](docs/OPERATING_MODEL.md)
- [Governance Continuity](docs/GOVERNANCE_CONTINUITY.md)
- [Review Cadence](docs/REVIEW_CADENCE.md)
- [Operational Examples](docs/OPERATIONAL_EXAMPLES.md)
- [Template README](template/README.md) — how to apply AEOS to any project

---

## Current Phase

**Phase 0: Governance/Bootstrap** — governance established, validated, and template-ized. Ready for Phase 1 (Controlled Internal Adoption).

See [PHASE_POLICY.md](governance/PHASE_POLICY.md) for phase definitions.

---

## v0.4 Additions

AEOS Core v0.4 introduces:

- **OpenCode Integration** — `.opencode/` with 7 agents, mixed models, and governance skill
- **State Graph Orchestration** — workflows as graphs with feedback loops, not linear pipelines
- **State Transition Protocol** — `protocols/STATE_TRANSITION_PROTOCOL.md` for recording transitions
- **Reusable Template** — `template/` directory with complete AEOS structure for any project
- **Configurable Lint** — `aeos_lint.py` supports environment variables for custom paths
- **Project Charter** — `project-charter.md` template for project-specific configuration
- **3 Governance Profiles** — Full, Standard, Lite based on project complexity

---

## Operational State Classification

All AEOS capabilities are classified using explicit operational states:

- **IMPLEMENTED** — exists in repository, validated, operational.
- **EXPERIMENTAL** — defined and tested, not yet stable.
- **PROPOSED** — documented direction, not yet implemented.
- **STRATEGIC** — long-term vision, no active work.

Use explicit operational state classification where implementation maturity may be ambiguous. See `governance/STATE_CLASSIFICATION_POLICY.md`.

---

## Governance Baseline

A formal governance stabilization checkpoint is documented in [GOVERNANCE_BASELINE_v0.3.md](docs/GOVERNANCE_BASELINE_v0.3.md). It preserves a known-good operational state for rollback, drift comparison, and longitudinal analysis.
