# Incident Workflow

> **State Graph Reference:** This workflow operates within the AEOS state graph defined in [state_graph.md](state_graph.md). All transitions and feedback loops follow the graph edges documented therein.

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

## State Graph Mapping

| Workflow Stage | State Graph Node | Responsible Agent | Output Artifact |
|----------------|------------------|-------------------|-----------------|
| Incident Identification | `objective_defined` | director | OBJ-XXX / INC-XXX |
| Investigation | `implementing` | implementer | Root cause analysis |
| Resolution Proposal | `task_defined` | director | TASK-XXX |
| Resolution Application | `implementing` | implementer | Código fix |
| Validation | `testing` | qa | Resultados de tests |
| Closure | `closed` | director | OBJ-XXX CLOSED |

## Feedback Loops

| Feedback Loop | Trigger | Condition | Action | Re-entry Path |
|---------------|---------|-----------|--------|---------------|
| `testing → implementing` | Resolution validation fails | Test results = FAIL | Rollback and re-investigate root cause | implementing → reviewing → testing |
| `implementing → task_defined` | Resolution scope insufficient | Cannot resolve incident with defined scope | Director expands TASK-XXX with broader scope | task_defined → implementing |
| `implementing → architecture_reviewed` | Root cause reveals architectural flaw | Current architecture is cause of incident | Architect evaluates and creates/updates ADR | architecture_reviewed → task_defined → implementing |
| `auditing → objective_defined` | Post-incident audit finds strategic gap | Incident reveals misalignment with OBJ-XXX | Director re-aligns with human operator | objective_defined → ... |

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
- ST-NNN (state transition log for each state change)

## Exit Criteria

- Incident is resolved.
- Affected operations are restored.
- Resolution is validated.
- Lessons learned are documented.
- Incident is marked closed.
- All state transitions logged in `memory/state-log/ST-NNN.md`.
- Final state transition recorded: `testing → closed`.

## Failure Modes

- Root cause cannot be identified → escalate with best analysis.
- Resolution introduces new issues → rollback and re-investigate.
- Human approval unavailable (CRITICAL) → follow emergency protocol.
- Incident scope expands → re-classify and re-escalate.

## Handoff Requirements

- Incident closure must include summary of resolution.
- All artifacts must be saved to memory/incidents/.
- Lessons learned must be propagated to relevant governance documents.
