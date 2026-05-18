# Research Workflow

## Purpose

Define the process for conducting research, analysis, and documentation within AEOS Core.

## Entry Criteria

- Research question or topic is identified.
- Research objective is defined.
- Human approval to proceed (if research affects governance).

## Required Inputs

- Research question or topic.
- Scope boundaries for research.
- Assigned documentation-agent or researcher.

## Lifecycle Stages

1. **Research Definition**: Define research question and scope.
2. **Task Definition**: Create TASK-XXX using task_template.md.
3. **Agent Assignment**: Assign documentation-agent.
4. **Research Execution**: Gather and analyze information.
5. **Documentation**: Document findings in memory/research/.
6. **Review**: reviewer-agent validates research completeness.
7. **Recommendations**: Document actionable recommendations.
8. **Handoff**: documentation-agent produces HND-XXX.
9. **Close**: Task is marked complete.

## Validation Gates

- Research findings are documented.
- Findings reference credible sources.
- Recommendations are actionable.
- Review passes per REVIEW_PROTOCOL.

## Review Requirements

- Completeness review by reviewer-agent.
- Governance impact review by auditor-agent (if applicable).

## Artifacts Produced

- TASK-XXX (task definition)
- Research document in memory/research/
- REV-XXX (review report)
- HND-XXX (handoff report)
- ADR-XXX (if research leads to architecture decision)

## Exit Criteria

- Research findings are documented.
- Recommendations are actionable.
- Review passes.
- Handoff report is complete.

## Failure Modes

- Research scope is too broad → narrow scope with approval.
- Research findings are inconclusive → document and close.
- Research reveals governance conflict → escalate to director-agent.
- Research leads to architecture change → initiate architecture_change_workflow.

## Handoff Requirements

- Handoff report must follow HANDOFF_PROTOCOL.
- Research document must be saved to memory/research/.
- Recommendations must be specific and actionable.
