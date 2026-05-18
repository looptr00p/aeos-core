# Incident Workflow

## Purpose

Define the process for identifying, responding to, and resolving incidents within AEOS Core.

## Entry Criteria

- Incident is identified by any agent or human.
- Incident is classified by category and severity.

## Required Inputs

- Incident description.
- Affected artifacts and operations.
- Severity classification.
- Assigned responder (per INCIDENT_PROTOCOL).

## Lifecycle Stages

1. **Incident Identification**: Document incident using incident_template.md.
2. **Incident Classification**: Classify category and severity.
3. **Incident Report**: Save INC-XXX to memory/incidents/.
4. **Operations Halt**: Halt affected operations.
5. **Escalation**: Escalate to director-agent per INCIDENT_PROTOCOL.
6. **Investigation**: Responder investigates root cause.
7. **Resolution Proposal**: Responder proposes resolution.
8. **Human Approval**: Human approves resolution (for CRITICAL/HIGH).
9. **Resolution Application**: Apply approved resolution.
10. **Validation**: Validate resolution resolves the incident.
11. **Closure**: Mark incident resolved with closure notes.
12. **Lessons Learned**: Document prevention measures.

## Validation Gates

- Incident report is complete.
- Root cause is identified.
- Resolution is validated.
- Affected operations are restored.
- Lessons learned are documented.

## Review Requirements

- Incident report reviewed by director-agent.
- CRITICAL/HIGH incidents require human review.
- Resolution requires human approval (for CRITICAL/HIGH).
- Closure notes reviewed by auditor-agent.

## Artifacts Produced

- INC-XXX (incident report)
- Root cause analysis
- Resolution documentation
- Lessons learned document

## Exit Criteria

- Incident is resolved.
- Affected operations are restored.
- Resolution is validated.
- Lessons learned are documented.
- Incident is marked closed.

## Failure Modes

- Root cause cannot be identified → escalate with best analysis.
- Resolution introduces new issues → rollback and re-investigate.
- Human approval unavailable (CRITICAL) → follow emergency protocol.
- Incident scope expands → re-classify and re-escalate.

## Handoff Requirements

- Incident closure must include summary of resolution.
- All artifacts must be saved to memory/incidents/.
- Lessons learned must be propagated to relevant governance documents.
