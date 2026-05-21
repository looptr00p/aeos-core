# Feature Workflow

## Purpose

Define the end-to-end process for implementing new features within AEOS Core.

**Este workflow opera como parte del State Graph de AEOS.** Ver `workflows/state_graph.md` para el grafo completo de estados y loops de feedback.

## Entry Criteria

- Objective is defined and approved (OBJ-XXX).
- ADR is created if architecture changes are needed (ADR-XXX).
- Human approval to proceed with feature implementation.

## Required Inputs

- Active objective (OBJ-XXX).
- ADR if architecture is affected (ADR-XXX).
- Defined acceptance criteria.
- Assigned implementer-agent.
- Assigned reviewer-agent.

## State Graph Mapping

Este workflow mapea a los siguientes nodos del grafo de estado:

| Stage | Nodo del Grafo | Agente | Artifact |
|-------|---------------|--------|----------|
| 1-2 | `objective_defined` → `architecture_reviewed` | director → architect | OBJ-XXX, ADR-XXX |
| 3 | `task_defined` | director | TASK-XXX |
| 4-5 | `implementing` | implementer | Código + HND-XXX |
| 6 | `reviewing` | reviewer | REV-XXX |
| 7 | `testing` | qa | Resultados de tests |
| 8 | `auditing` | auditor | AUD-XXX |
| 9-10 | `documenting` → `handoff_complete` | documentation → director | Memoria + HND-XXX |
| 11-12 | `closed` | director | OBJ-XXX CLOSED |

## Lifecycle Stages (State Graph con Loops)

1. **Objective Definition**: Create OBJ-XXX using objective_template.md.
2. **Architecture Review**: If architecture is affected, create ADR-XXX.
3. **Task Definition**: Create TASK-XXX using task_template.md.
4. **Agent Assignment**: Assign implementer-agent and reviewer-agent.
5. **Implementation**: implementer-agent executes within defined scope.
6. **Review**: reviewer-agent conducts review per REVIEW_PROTOCOL.
7. **Validation**: qa-agent validates tests and acceptance criteria.
8. **Audit**: auditor-agent validates governance compliance.
9. **Human Approval**: Human reviews and approves (if required).
10. **Handoff**: implementer-agent produces HND-XXX.
11. **Memory Update**: documentation-agent updates memory artifacts.
12. **Close**: Task is marked complete.

## Feedback Loops

Este workflow NO es lineal. Los siguientes loops pueden ocurrir:

| Loop | Trigger | Acción | Re-entry |
|------|---------|--------|----------|
| reviewing → implementing | Review encuentra issues | Implementer corrige | implementing → reviewing |
| testing → implementing | Tests fallan | Implementer corrige bugs | implementing → reviewing → testing |
| testing → task_defined | Spec ambigua | PM re-define task | task_defined → implementing → testing |
| auditing → reviewing | Gaps en review | Reviewer re-revisa | reviewing → testing |
| auditing → objective_defined | Inconsistencia estratégica | Director re-alinea | objective_defined → ... |
| implementing → architecture_reviewed | Constraint técnico descubierto | Architect re-evalúa | architecture_reviewed → task_defined → implementing |

Cada loop debe registrarse en `memory/state-log/ST-NNN.md` siguiendo `protocols/STATE_TRANSITION_PROTOCOL.md`.

## Validation Gates

- All tests must pass.
- All review types must pass per REVIEW_PROTOCOL.
- All acceptance criteria must be met.
- Audit must pass governance compliance.
- Human approval obtained (if required).

## Review Requirements

- Scope review by reviewer-agent.
- Implementation review by reviewer-agent.
- Governance review by auditor-agent.
- Validation review by qa-agent.
- Handoff review by reviewer-agent and director-agent.

## Artifacts Produced

- OBJ-XXX (objective)
- ADR-XXX (if applicable)
- TASK-XXX (task definition)
- REV-XXX (review report)
- AUD-XXX (audit report)
- HND-XXX (handoff report)
- ST-NNN (state transition records, uno por cada transición)

## Exit Criteria

- All validation gates pass.
- All reviews pass.
- Handoff report is complete.
- Memory is updated.
- Human approval obtained (if required).
- All state transitions logged in `memory/state-log/`.

## Failure Modes

- Objective lacks clear acceptance criteria → escalate to director.
- Architecture ADR not accepted → halt implementation.
- Review fails → return to implementation (feedback loop).
- Audit fails → escalate to director-agent.
- Human approval denied → close or revise task.
- Feedback loop exceeds 3 iterations → escalate to director.
