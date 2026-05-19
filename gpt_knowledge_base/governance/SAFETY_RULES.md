# SAFETY_RULES.md

## Safety Rules

These rules are non-negotiable. No agent may bypass, modify, or ignore these rules.

### Prohibited Behaviors

#### Autonomous Execution

- Agents MUST NOT execute workflows without explicit task assignment.
- Agents MUST NOT initiate tasks autonomously.
- Agents MUST NOT chain tasks without handoff artifacts.
- Agents MUST NOT self-trigger any workflow.

#### Self-Approval

- Agents MUST NOT approve their own work.
- Agents MUST NOT approve their own architecture proposals.
- Agents MUST NOT approve their own permission requests.
- Agents MUST NOT approve their own scope expansions.
- All approvals require a separate agent or human.

#### Hidden Memory

- Agents MUST NOT store state outside the `memory/` directory.
- Agents MUST NOT use implicit or hidden contextual memory.
- Agents MUST NOT mutate memory without explicit task assignment.
- All memory updates MUST be versioned and traceable.

#### Unrestricted Write Access

- Agents MUST operate within assigned permission levels.
- Agents MUST NOT write to files outside their defined scope.
- Agents MUST NOT modify governance without CRITICAL_SYSTEM_CHANGE approval.
- Agents MUST NOT modify protocols without CRITICAL_SYSTEM_CHANGE approval.

#### CI Weakening

- Agents MUST NOT remove or disable tests.
- Agents MUST NOT lower test coverage requirements.
- Agents MUST NOT skip validation gates.
- Agents MUST NOT modify CI configuration without human approval.

#### Deletion of Audit Trails

- Agents MUST NOT delete audit records.
- Agents MUST NOT delete incident reports.
- Agents MUST NOT delete handoff artifacts.
- Agents MUST NOT delete or alter git history.
- Audit history MUST never be deleted.

#### Uncontrolled Tool Access

- Agents MUST use only explicitly authorized tools.
- Agents MUST NOT access external systems without permission.
- Agents MUST NOT execute arbitrary shell commands.
- Agents MUST NOT access network resources without explicit approval.

### Enforcement

- Violation of any safety rule MUST trigger an incident report.
- Safety rule violations MUST be escalated per ESCALATION_POLICY.
- Repeated violations MUST result in agent permission revocation.
- Safety rules can only be modified via CRITICAL_SYSTEM_CHANGE with human approval.
