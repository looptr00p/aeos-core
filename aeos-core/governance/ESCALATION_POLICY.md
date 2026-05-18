# ESCALATION_POLICY.md

## Escalation Policy

Agents MUST escalate when specific conditions are met. Escalation routes to the director-agent and requires human review.

### Escalation Conditions

#### Unclear Requirements

- Task objective is ambiguous.
- Acceptance criteria are not defined.
- Scope boundaries are unclear.
- Required inputs are missing.
- **Action**: Escalate to director-agent. Halt implementation until clarified.

#### Conflicting Documentation

- Governance documents contradict each other.
- Protocols conflict with workflows.
- Agent definitions conflict with permission model.
- Templates reference non-existent protocols.
- **Action**: Escalate to director-agent. Document conflict via incident report.

#### Failed Validation

- Tests fail after implementation.
- Acceptance criteria are not met.
- Protocol compliance check fails.
- Governance review fails.
- **Action**: Escalate to director-agent. Do not proceed to handoff.

#### Unsafe Permissions

- Task requires permissions beyond assigned level.
- Permission escalation is requested without justification.
- CRITICAL_SYSTEM_CHANGE is attempted without human approval.
- **Action**: Escalate to director-agent. Halt all operations.

#### Missing Acceptance Criteria

- Task definition lacks acceptance criteria.
- Objective has no measurable success conditions.
- Review requirements are undefined.
- **Action**: Escalate to director-agent. Do not begin implementation.

#### Architecture Uncertainty

- Proposed change conflicts with existing architecture.
- Architecture documentation is outdated or missing.
- Multiple valid approaches exist with no clear selection criteria.
- **Action**: Escalate to director-agent. Request architect-agent review.

### Escalation Process

1. Agent identifies escalation condition.
2. Agent documents the condition with references.
3. Agent creates incident report (INC-XXX) per INCIDENT_PROTOCOL.
4. Agent notifies director-agent.
5. Agent halts operations on affected task.
6. Director-agent assesses and routes to human review.
7. Human provides resolution or decision.
8. Agent resumes or closes task based on resolution.

### Escalation Prohibitions

- Agents MUST NOT bypass escalation.
- Agents MUST NOT resolve escalated conditions autonomously.
- Agents MUST NOT continue work on an escalated task.
- Agents MUST NOT delete escalation records.
