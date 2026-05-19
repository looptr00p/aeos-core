# Operational Examples

## Purpose

Provide deterministic, human-readable lifecycle examples with traceability continuity.

## 1. Objective Lifecycle

- Create `OBJ-101` with measurable success criteria.
- Approve objective with human sign-off.
- Link downstream tasks `TASK-101`, `TASK-102`.
- Close objective only after linked handoffs are complete.

## 2. ADR Lifecycle

- Draft `ADR-101` for a governance-impacting change.
- Review alternatives and consequences.
- Human approves ADR status `ACCEPTED`.
- Link implementation tasks referencing `ADR-101`.

## 3. Task Lifecycle

- Define `TASK-101` with allowed/forbidden changes.
- Assign implementer with explicit permission level.
- Execute implementation and required validations.
- Produce `HND-101` before close.

## 4. Review Lifecycle

- Reviewer records `REV-101` against `TASK-101`.
- Validate scope, implementation, governance, and tests.
- If failed, return to implementation with explicit actions.
- If passed, continue to audit/handoff.

## 5. Audit Lifecycle

- Auditor creates `AUD-101` covering traceability and compliance.
- Verify `TASK-101`, `REV-101`, `HND-101` linkage.
- Record findings and corrective actions.
- Close only when findings are resolved or accepted by human decision.

## 6. Incident Lifecycle

- Detect governance issue and open `INC-101`.
- Contain impact and assign owner.
- Record root cause and corrective action.
- Close incident with approval and follow-up evidence.

## 7. Escalation Lifecycle

- Trigger condition creates `ESC-101` (severity classified).
- Route to required reviewers and human approver.
- Pause affected task flow until resolution.
- Resume only after explicit resolution status update.

## 8. Handoff Lifecycle

- Implementation closes with `HND-101`.
- Handoff includes files changed, validations, risks, unresolved issues.
- Receiving reviewer validates handoff completeness.
- Memory update references `OBJ-101`, `TASK-101`, and `HND-101`.
