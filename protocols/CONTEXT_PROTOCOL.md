# CONTEXT_PROTOCOL.md

## Context Protocol

All agents MUST operate with explicit, documented context. Hidden or implicit context is prohibited.

### Canonical Sources

Agents MUST derive context from the following canonical sources only:

- Active objective: `memory/objectives/OBJ-XXX.md`
- Active task: `memory/tasks/TASK-XXX.md`
- Governance documents: `governance/*.md`
- Protocols: `protocols/*.md`
- Architecture records: `memory/architecture/`
- Agent definitions: `agents/`

Agents MUST NOT use context from:
- Previous unrelated tasks.
- Implicit knowledge not documented in canonical sources.
- External sources not explicitly referenced.

### Required Context Fields

Every task execution MUST reference:

```
Current Objective: [Reference to OBJ-XXX]
Constraints: [List of applicable constraints from governance and protocols]
Allowed Scope: [Files and changes permitted]
Forbidden Scope: [Files and changes prohibited]
Stop Conditions: [Conditions that halt execution]
```

### Context Updates

- Context is updated only when the objective or task changes.
- Context updates MUST be documented in the task definition.
- Context updates MUST NOT alter governance or protocol meaning.

### Context Loss

If context is lost, incomplete, or ambiguous:
1. Agent MUST halt execution.
2. Agent MUST escalate per ESCALATION_POLICY.
3. Agent MUST NOT resume until context is restored.

### Context Prohibitions

- Agents MUST NOT assume context not explicitly documented.
- Agents MUST NOT carry forward context from closed tasks without explicit reference.
- Agents MUST NOT modify context sources without proper permissions.
