# INCIDENT_PROTOCOL.md

## Incident Protocol

All incidents within AEOS Core MUST be documented and handled following this protocol.

### Incident Categories

#### Governance Incidents

- Governance documents are contradicted or ambiguous.
- Governance rules are violated by an agent.
- Permission model is bypassed.
- Safety rules are violated.

#### Workflow Failures

- Required workflow steps are skipped.
- Validation gates are bypassed.
- Handoff artifacts are missing.
- Review requirements are not met.

#### Context Loss

- Active objective is missing or incomplete.
- Task definition lacks required fields.
- Canonical context sources are unavailable.
- Context references point to non-existent artifacts.

#### Audit Failures

- Audit trail is incomplete.
- Traceability IDs are missing or duplicated.
- Memory updates are untraceable.
- Review records are missing.

#### Unsafe Agent Behavior

- Agent operates outside assigned scope.
- Agent attempts self-approval.
- Agent uses unauthorized permissions.
- Agent stores hidden memory.
- Agent executes autonomous workflows.

#### CI Failures

- Required tests fail.
- CI configuration is invalid.
- Validation gates produce inconsistent results.
- Test coverage drops below threshold.

### Incident Response

1. Incident is identified by any agent or human.
2. Incident report is created using `templates/incident_template.md`.
3. Incident is saved to `memory/incidents/INC-XXX.md`.
4. Affected operations are halted.
5. Incident is escalated to director-agent.
6. Director-agent assesses severity and assigns responder.
7. Responder investigates and documents root cause.
8. Responder proposes resolution.
9. Human approves resolution (for governance-relevant incidents).
10. Resolution is applied.
11. Incident is marked resolved with closure notes.

### Incident Severity

| Severity | Description                          | Response Time   | Human Approval |
|----------|--------------------------------------|-----------------|----------------|
| CRITICAL | Safety rule violation, data loss     | Immediate       | Required       |
| HIGH     | Governance bypass, audit failure     | Within 1 cycle  | Required       |
| MEDIUM   | Workflow failure, context loss       | Within 2 cycles | Recommended    |
| LOW      | Minor documentation inconsistency    | Next cycle      | Optional       |

### Incident Prohibitions

- Agents MUST NOT delete incident reports.
- Agents MUST NOT resolve incidents autonomously (for CRITICAL/HIGH).
- Agents MUST NOT continue affected operations during incident.
- Agents MUST NOT alter incident history.
