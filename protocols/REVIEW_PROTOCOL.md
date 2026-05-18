# REVIEW_PROTOCOL.md

## Review Protocol

All changes within AEOS Core MUST undergo review following this protocol.

### Review Types

#### Scope Review

- Validates that changes remain within defined task scope.
- Checks that no forbidden files were modified.
- Checks that no scope expansion occurred.
- Performed by: reviewer-agent.

#### Architecture Review

- Validates that changes are consistent with documented architecture.
- Checks that architectural invariants are preserved.
- Checks that no unintended architectural drift occurred.
- Performed by: architect-agent, auditor-agent.

#### Implementation Review

- Validates correctness of implementation.
- Checks that implementation follows defined steps.
- Checks that code quality standards are met.
- Checks that no hidden functionality was introduced.
- Performed by: reviewer-agent.

#### Governance Review

- Validates that changes comply with governance documents.
- Checks that permission model is respected.
- Checks that safety rules are not violated.
- Checks that escalation policies were followed if applicable.
- Performed by: auditor-agent.

#### Validation Review

- Validates that all required tests pass.
- Checks that acceptance criteria are met.
- Checks that validation gates were not skipped.
- Performed by: qa-agent.

#### Handoff Review

- Validates that handoff report is complete.
- Checks that all required fields are populated.
- Checks that risks and unresolved issues are documented.
- Checks that next recommended step is defined.
- Performed by: reviewer-agent, director-agent.

### Review Process

1. Reviewer receives task with implementation complete.
2. Reviewer conducts applicable review types.
3. Reviewer documents findings with specific references.
4. Reviewer marks review as PASS or FAIL.
5. On FAIL: reviewer documents required corrections.
6. On PASS: review proceeds to next stage (human approval if required).
7. All review artifacts are archived in `memory/audits/`.

### Review Documentation

Every review MUST produce a review artifact using `templates/review_template.md`.

### Review Prohibitions

- Reviewers MUST NOT review their own work.
- Reviewers MUST NOT skip review types without documented justification.
- Reviewers MUST NOT approve changes with failing validations.
- Reviewers MUST NOT bypass governance requirements.
