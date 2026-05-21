# PERMISSION_MODEL.md

## Permission Levels

All agent operations are constrained by explicit permission levels.

### READ_ONLY

- Agents may read files, protocols, governance documents, and memory.
- Agents may NOT modify any file.
- Agents may NOT create any file.
- Agents may NOT execute any workflow.
- Default permission for unassigned agents.

### DOCS_ONLY

- Agents may read all files.
- Agents may create or modify documentation files (`.md`).
- Agents may NOT modify governance, protocols, or workflows.
- Agents may NOT modify implementation code.
- Agents may NOT modify tests.
- Assigned to: documentation-agent.

### TESTS_ONLY

- Agents may read all files.
- Agents may create or modify test files under `tests/`.
- Agents may NOT modify governance, protocols, or workflows.
- Agents may NOT modify implementation code.
- Agents may NOT modify documentation outside test comments.
- Assigned to: qa-agent.

### LIMITED_IMPLEMENTATION

- Agents may read all files.
- Agents may create or modify implementation files within explicitly defined scope.
- Agents may NOT modify governance documents.
- Agents may NOT modify protocols.
- Agents may NOT modify workflows.
- Agents may NOT modify tests outside assigned scope.
- Must reference a specific TASK-ID with defined file scope.
- Assigned to: implementer-agent (per task assignment).

### CRITICAL_SYSTEM_CHANGE

- Applies to: governance changes, protocol changes, workflow changes, permission changes, CI changes.
- REQUIRES explicit human approval before any change.
- No agent may execute CRITICAL_SYSTEM_CHANGE autonomously.
- Changes MUST follow REVIEW_PROTOCOL.
- Changes MUST be documented via ADR.
- Changes MUST pass audit review.

### Permission Assignment

- Permissions are assigned per task, not per agent permanently.
- Permission assignment MUST be documented in the task definition.
- Permission escalation requires human approval.
- Permission revocation is immediate upon task completion or escalation.
