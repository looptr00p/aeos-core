# TASK_PROTOCOL.md

## Task Protocol

All tasks within AEOS Core MUST follow this protocol.

### Task Definition Structure

Every task MUST be defined using the following fields:

```
TASK-ID: TASK-XXX
Objective: [Clear, measurable objective]
Context: [References to relevant objectives, decisions, and constraints]
Files to Create: [List of files to be created]
Files to Modify: [List of files to be modified with allowed changes]
Allowed Changes: [Explicit description of permitted modifications]
Forbidden Changes: [Explicit description of prohibited modifications]
Implementation Steps: [Ordered list of implementation actions]
Required Validations: [List of validations that must pass]
Acceptance Criteria: [Measurable conditions for task completion]
Handoff Output Required: [Reference to handoff artifact format]
Reviewer: [Assigned reviewer agent ID]
Human Approval Required: [yes/no]
```

### Task Lifecycle

1. **Definition**: Task is defined using the structure above.
2. **Assignment**: Task is assigned to an agent with appropriate permissions.
3. **Implementation**: Agent executes implementation steps within allowed scope.
4. **Validation**: Agent runs required validations.
5. **Review**: Assigned reviewer conducts review per REVIEW_PROTOCOL.
6. **Human Approval**: If required, human reviews and approves.
7. **Handoff**: Agent produces handoff report per HANDOFF_PROTOCOL.
8. **Memory Update**: Relevant memory is updated per MEMORY_PROTOCOL.
9. **Close**: Task is marked complete with all artifacts archived.

### Task Constraints

- Tasks MUST NOT exceed assigned permission level.
- Tasks MUST NOT modify files outside the defined scope.
- Tasks MUST reference canonical context sources.
- Tasks MUST define explicit acceptance criteria.
- Tasks MUST define a reviewer.
- Tasks requiring governance, protocol, or workflow changes MUST require human approval.

### Handoff Requirement

No task is complete without a handoff artifact following HANDOFF_PROTOCOL.

### Traceability

All tasks MUST be traceable to:
- An objective (OBJ-XXX)
- An agent (agent-id)
- A handoff (HND-XXX)
- A review (REV-XXX) if applicable
