# ADR_PROTOCOL.md

## Architecture Decision Record Protocol

All architectural and governance decisions MUST be documented as Architecture Decision Records (ADRs).

### ADR Structure

Every ADR MUST follow this structure:

```
ADR-ID: ADR-XXX
Title: [Short, descriptive title]
Status: [PROPOSED | ACCEPTED | DEPRECATED | SUPERSEDED]
Date: [YYYY-MM-DD]
Owner: [agent-id or human]
Review Date: [YYYY-MM-DD]

Context:
[Description of the situation requiring a decision]

Decision:
[The decision that was made, stated clearly]

Alternatives Considered:
- [Alternative 1] - [Pros] - [Cons] - [Reason rejected]
- [Alternative 2] - [Pros] - [Cons] - [Reason rejected]

Consequences:
- [Positive consequence]
- [Negative consequence]
- [Risk or trade-off]

References:
- [Related OBJ-XXX, TASK-XXX, or other ADR-XXX]
```

### ADR Lifecycle

1. **Proposed**: ADR is drafted by architect-agent or human.
2. **Review**: ADR is reviewed per REVIEW_PROTOCOL.
3. **Accepted**: Human approves the ADR.
4. **Deprecated**: ADR is no longer applicable but remains in history.
5. **Superseded**: ADR is replaced by a newer ADR (reference the successor).

### ADR Requirements

- ADRs MUST be stored in `memory/decisions/ADR-XXX.md`.
- ADRs MUST use the template in `templates/adr_template.md`.
- ADRs MUST reference the originating objective or task.
- ADRs MUST NOT be deleted after creation.
- ADRs MUST have an explicit owner.
- ADRs MUST have a review date for periodic validation.

### ADR Prohibitions

- Agents MUST NOT create ADRs without human approval for governance-relevant decisions.
- Agents MUST NOT change ADR status autonomously.
- Agents MUST NOT delete or alter existing ADRs.
- Agents MUST NOT implement decisions that lack an accepted ADR (when required).
