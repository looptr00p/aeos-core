# Memory Index

## Purpose

The memory index defines how AEOS artifacts are connected and provides a human-readable traceability system.

## Artifact Relationships

All AEOS artifacts are connected through explicit traceability IDs:

```
OBJ-XXX (Objective)
  └── ADR-XXX (Architecture Decision Record)
        └── TASK-XXX (Task)
              ├── REV-XXX (Review)
              ├── AUD-XXX (Audit)
              └── HND-XXX (Handoff)

INC-XXX (Incident)
  └── References: TASK-XXX, OBJ-XXX, ADR-XXX
```

## Traceability Rules

1. Every TASK-XXX MUST reference an OBJ-XXX.
2. Every TASK-XXX requiring architecture change MUST reference an ADR-XXX.
3. Every closed TASK-XXX MUST reference a HND-XXX.
4. Every REV-XXX MUST reference a TASK-XXX.
5. Every AUD-XXX MUST reference a TASK-XXX or OBJ-XXX.
6. Every INC-XXX MUST reference affected artifacts.
7. Every ADR-XXX MUST reference an OBJ-XXX or TASK-XXX.

## Index Structure

| Artifact Type | Directory | Prefix | Template |
|---------------|-----------|--------|----------|
| Objectives | `memory/objectives/` | OBJ- | `templates/objective_template.md` |
| Decisions | `memory/decisions/` | ADR- | `templates/adr_template.md` |
| Tasks | `memory/tasks/` | TASK- | `templates/task_template.md` |
| Reviews | `memory/audits/` | REV- | `templates/review_template.md` |
| Audits | `memory/audits/` | AUD- | `templates/audit_template.md` |
| Handoffs | `memory/handoffs/` | HND- | `templates/handoff_template.md` |
| Incidents | `memory/incidents/` | INC- | `templates/incident_template.md` |

## Validation

Run `scripts/aeos_lint.py` to validate traceability references.

## Principles

- Index is markdown-based and human-readable.
- Index is git-versioned and auditable.
- Index is explicit — no hidden relationships.
- Index is repo-driven — no external databases.
