# AEOS Core v0

AI Engineering Operating System. Governance-first, repo-driven, markdown-first, human-governed, deterministic, auditable, reproducible.

## What is AEOS?

AEOS (AI Engineering Operating System) is a structured governance framework for AI-assisted software engineering. It provides explicit governance documents, protocols, templates, agent definitions, and workflows to ensure AI-assisted engineering remains safe, auditable, and human-controlled.

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

```
aeos-core/
  governance/       Rules, constraints, and policies
  protocols/        How work is done
  templates/        Reusable artifact templates
  agents/           Agent definitions and registry
  workflows/        End-to-end process definitions
  memory/           Explicit institutional memory
  tests/            Repository structure validation
  docs/             Operational documentation
```

## Quick Start

```bash
# Install dependencies
pip install pytest pyyaml

# Run validation tests
cd aeos-core
pytest tests/
```

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

AEOS Core v0 is NOT:

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

AEOS Core v0 does NOT execute autonomous workflows.

## Documentation

- [AEOS Overview](docs/AEOS_OVERVIEW.md)
- [Operating Model](docs/OPERATING_MODEL.md)
- [MVP Scope](docs/MVP_SCOPE.md)

## Current Phase

**Phase 0: Governance/Bootstrap**

See [PHASE_POLICY.md](governance/PHASE_POLICY.md) for phase definitions.
