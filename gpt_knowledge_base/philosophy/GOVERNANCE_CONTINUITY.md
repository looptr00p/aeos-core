# Governance Continuity

## Why Governance Continuity Matters

Governance is the foundation of AEOS Core. Without continuity, governance becomes inconsistent, ambiguous, and unenforceable. Governance continuity ensures that:

- Rules remain consistent across versions.
- Protocols are applied uniformly.
- Templates remain current and usable.
- Workflows are followed without deviation.
- Human approval authority is preserved.

Governance discontinuity leads to scope creep, autonomous behavior, and loss of auditability.

## Why Explicit Memory Matters

AEOS Core stores all institutional memory as markdown files in the `memory/` directory. Explicit memory ensures that:

- All context is human-readable.
- All context is git-versioned.
- All context is auditable.
- All context is reproducible.
- No hidden state exists.

Hidden memory — state stored outside the repository, in embeddings, or in runtime systems — creates untraceable behavior that cannot be audited or reproduced.

## Why Repo-Driven Traceability Matters

All AEOS artifacts are stored in the repository and connected through traceability IDs (OBJ-XXX, ADR-XXX, TASK-XXX, etc.). Repo-driven traceability ensures that:

- Every artifact can be traced to its origin.
- Every relationship is explicit and documented.
- Every change is versioned and reviewable.
- Every decision is recorded and attributable.

Without repo-driven traceability, artifacts become orphaned, relationships become implicit, and auditability is lost.

## Why Human-Readable Operational Artifacts Matter

All AEOS templates, protocols, and governance documents are written in markdown. Human-readable artifacts ensure that:

- Any stakeholder can understand the system.
- Reviews can be conducted without tooling.
- Decisions can be validated by humans.
- No specialized runtime is required to interpret state.

Machine-only formats (binary, serialized state, embeddings) create barriers to human oversight.

## Why AEOS Avoids Hidden Runtime State

AEOS Core does not use databases, vector stores, event buses, or runtime state machines. Avoiding hidden runtime state ensures that:

- The repository is the single source of truth.
- All state is visible in git history.
- No external system is required to understand current state.
- Reproducibility is guaranteed by git.

Hidden runtime state creates divergence between what the repository says and what the system does.

## Why Workflow Closure Validation Exists

Every workflow in AEOS Core has entry criteria, validation gates, and exit criteria. Workflow closure validation ensures that:

- Closed tasks reference valid objectives.
- Closed tasks reference valid handoffs.
- All references use valid traceability prefixes.
- No artifact is left in an incomplete state.

Without closure validation, workflows terminate without producing required artifacts, breaking the audit trail and traceability chain.

## Enforcement

Governance continuity is validated by:

- `scripts/aeos_lint.py` — automated lint checks.
- `pytest tests/` — repository structure validation.
- Manual review per REVIEW_PROTOCOL.
- Audit per audit_workflow.md.

Violations are reported as incidents per INCIDENT_PROTOCOL.
