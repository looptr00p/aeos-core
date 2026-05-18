# HANDOFF_PROTOCOL.md

## Handoff Protocol

All task completions MUST produce a handoff report following this protocol.

### Required Handoff Fields

Every handoff report MUST include:

```
Handoff ID: HND-XXX
Task ID: TASK-XXX
Agent ID: [agent-id]
Date: [YYYY-MM-DD]

Summary:
[Concise description of what was accomplished]

Files Changed:
- [path/to/file] - [brief description of change]
- [path/to/file] - [brief description of change]

Decisions Made:
- [Decision description] - [rationale] - [reference to ADR if applicable]

Validations Executed:
- [Validation name] - [result: PASS/FAIL]
- [Validation name] - [result: PASS/FAIL]

Risks:
- [Risk description] - [severity: LOW/MEDIUM/HIGH] - [mitigation if any]

Unresolved Issues:
- [Issue description] - [impact] - [recommended action]

Rollback Considerations:
[If rollback is needed, what steps are required]

Next Recommended Step:
[Specific, actionable next step for the receiving agent or human]
```

### Handoff Process

1. Agent completes task implementation and validation.
2. Agent produces handoff report using the structure above.
3. Agent saves handoff report to `memory/handoffs/HND-XXX.md`.
4. Agent notifies the assigned reviewer.
5. Reviewer validates handoff completeness per REVIEW_PROTOCOL.
6. On validation failure: agent corrects and resubmits.
7. On validation pass: handoff proceeds to next stage.

### Handoff Prohibitions

- Agents MUST NOT mark a task complete without a handoff report.
- Agents MUST NOT omit any required handoff field.
- Agents MUST NOT produce vague or ambiguous handoff content.
- Agents MUST NOT delete handoff reports after creation.

### Handoff Traceability

All handoffs MUST be traceable to:
- The originating task (TASK-XXX).
- The originating objective (OBJ-XXX).
- The producing agent (agent-id).
- The reviewing agent (agent-id).
