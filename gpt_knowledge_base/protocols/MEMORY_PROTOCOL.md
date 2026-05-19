# MEMORY_PROTOCOL.md

## Memory Protocol

All institutional memory within AEOS Core MUST follow this protocol.

### Explicit Memory Only

- Memory MUST be stored as markdown files in the `memory/` directory.
- Memory MUST be human-readable.
- Memory MUST be git-versioned.
- Memory MUST be auditable.
- Memory MUST be reproducible from git history.

### Memory Categories

| Category       | Directory                  | Content                              |
|----------------|----------------------------|--------------------------------------|
| Objectives     | `memory/objectives/`       | Active and completed objectives      |
| Decisions      | `memory/decisions/`        | Architectural and governance decisions|
| Tasks          | `memory/tasks/`            | Task definitions and status          |
| Handoffs       | `memory/handoffs/`         | Handoff reports                      |
| Audits         | `memory/audits/`           | Review and audit records             |
| Incidents      | `memory/incidents/`        | Incident reports                     |
| Architecture   | `memory/architecture/`     | Architecture documentation           |
| Research       | `memory/research/`         | Research findings and analysis       |

### Memory Update Rules

- Memory updates MUST be versioned (append or new file, never overwrite).
- Memory updates MUST reference the originating task or decision.
- Memory updates MUST follow the appropriate template.
- Memory updates MUST NOT introduce hidden contextual mutation.
- Memory updates MUST NOT be performed autonomously.

### Prohibited Memory Operations

- Agents MUST NOT store memory outside the `memory/` directory.
- Agents MUST NOT use hidden or implicit memory.
- Agents MUST NOT mutate memory without explicit task assignment.
- Agents MUST NOT delete memory records.
- Agents MUST NOT alter memory history.

### Memory Traceability

All memory entries MUST be traceable to:
- An originating task (TASK-XXX) or objective (OBJ-XXX).
- An agent that performed the update.
- A timestamp or git commit reference.

### Memory Format

- All memory files MUST use markdown format.
- All memory files MUST include a traceability ID.
- All memory files MUST follow the appropriate template.
