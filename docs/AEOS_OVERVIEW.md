# AEOS Overview

## What is AEOS?

AEOS (AI Engineering Operating System) is a governance-first, repo-driven operating model for AI-assisted software engineering. It provides structured governance, explicit protocols, reusable templates, and defined workflows to ensure AI-assisted engineering remains auditable, reproducible, and human-governed.

## Why AEOS Exists

AI-assisted engineering introduces risks that traditional development workflows do not address:

- Autonomous behavior without accountability.
- Hidden state and implicit memory.
- Uncontrolled scope expansion.
- Missing audit trails.
- Non-reproducible outputs.

AEOS exists to provide a structured framework that keeps AI-assisted engineering safe, auditable, and human-controlled.

## Governance-First Philosophy

AEOS places governance above implementation. Before any code is written:

1. Governance documents define the rules.
2. Protocols define how work is done.
3. Templates standardize artifacts.
4. Workflows define the process.
5. Agents operate within defined boundaries.

Governance cannot be bypassed. All changes require review. Critical changes require human approval.

## Workflow-First Philosophy

All work in AEOS follows defined workflows:

- Feature development follows the feature workflow.
- Bug fixes follow the bugfix workflow.
- Architecture changes follow the architecture change workflow.
- Audits follow the audit workflow.
- Incidents follow the incident workflow.
- Research follows the research workflow.

Each workflow has entry criteria, validation gates, review requirements, and exit criteria.

## Human-in-the-Loop Operation

AEOS is designed for human-governed operation:

- No agent may self-approve.
- Critical changes require human approval.
- Escalations route to human review.
- Phase transitions require human approval.
- Governance changes require human approval.

Humans retain ultimate decision authority.

## Explicit Memory Model

All institutional memory in AEOS is:

- Stored as markdown files in the `memory/` directory.
- Human-readable.
- Git-versioned.
- Auditable.
- Reproducible.

No hidden memory, embeddings, or autonomous memory mutation is allowed.

## Reproducibility Principles

All outputs in AEOS must be:

- Reproducible from git history.
- Traceable to originating objectives and tasks.
- Documented with explicit artifacts.
- Validated through defined gates.

No hidden state or implicit behavior is allowed.

## Auditability Principles

All operations in AEOS must be:

- Traceable to specific agents, tasks, and objectives.
- Documented with review and audit artifacts.
- Subject to governance compliance checks.
- Preserved in git history without deletion.

Audit trails cannot be deleted or altered.
