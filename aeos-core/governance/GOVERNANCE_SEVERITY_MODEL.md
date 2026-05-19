# Governance Severity Model

## Purpose

Provide a deterministic severity model for governance-impacting events and changes.

## LOW

Description:
- Minor issue with no governance logic impact.

Examples:
- markdown typo
- formatting adjustment
- non-semantic documentation cleanup

Required review level:
- reviewer-agent

Required audit level:
- optional spot-check by auditor-agent

Human approval requirements:
- not required

Escalation requirements:
- escalate only if repeated or combined with other issues

Rollback expectations:
- simple revert if needed

## MEDIUM

Description:
- Operational clarification that can affect execution consistency.

Examples:
- workflow clarification
- protocol clarification
- template update

Required review level:
- reviewer-agent plus auditor-agent

Required audit level:
- targeted audit note in AUD-XXX

Human approval requirements:
- required when change affects active operational usage

Escalation requirements:
- escalate when ambiguity remains after review

Rollback expectations:
- documented rollback path in handoff

## HIGH

Description:
- Change with direct governance or validation impact.

Examples:
- governance policy change
- validation logic change
- permission model change
- CI validation change

Required review level:
- director-agent, reviewer-agent, auditor-agent

Required audit level:
- explicit governance audit required

Human approval requirements:
- required before merge

Escalation requirements:
- mandatory escalation record (ESC-XXX)

Rollback expectations:
- rollback plan required before approval

## CRITICAL

Description:
- Attempted or actual violation of core safety/governance invariants.

Examples:
- CI weakening
- workflow bypass
- hidden memory introduction
- autonomous execution attempt
- permission escalation attempt
- self-approval attempt
- unrestricted agent permissions

Required review level:
- immediate director-agent and auditor-agent review

Required audit level:
- full incident-linked audit required

Human approval requirements:
- mandatory immediate human intervention

Escalation requirements:
- mandatory escalation and incident report

Rollback expectations:
- immediate containment and rollback to last known safe state
