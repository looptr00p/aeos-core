# Real Operations Learnings

## Purpose

Document what scales well, what scales poorly, and what becomes cognitively expensive when AEOS is applied to real engineering operational pressure. This is the primary learning artifact from Operational Cycle 001.

## What Scales Well

### Governance Invariants

Human approval, audit requirements, review requirements, and escalation lifecycle all remain intact under operational pressure. Governance-first design proves resilient — it does not bend under coordination stress.

### Lifecycle Persistence

ACTIVE tasks, OPEN escalations, and ACTIVE incidents persist correctly across handoffs. Markdown files in a git repository provide reliable persistence without infrastructure. This is one of AEOS's strongest properties.

### Review Minimization Guidance

Consolidating review types from 6 to 2-3 for MEDIUM-tier tasks reduces fatigue without weakening governance. The guidance document works as intended.

### Workflow Tiering Guidance

Reducing workflow stages from 12 to 8-10 for MEDIUM-tier tasks reduces overhead without weakening governance. The tiering approach is effective.

### aeos_lint.py Validation

Lightweight linting catches traceability errors, missing references, and lifecycle inconsistencies reliably. Single-file, deterministic, no dependencies beyond pytest/pyyaml.

### Markdown-First Approach

Everything is inspectable, searchable, and version-controllable. No hidden state, no runtime, no infrastructure. This remains the correct architectural choice.

## What Scales Poorly

### Traceability Index Maintenance

Manual maintenance of TRACEABILITY_INDEX.md becomes cognitively expensive at 12+ active artifacts. Each artifact creation or update requires corresponding index update. This is mechanical but easy to forget under time pressure. aeos_lint.py catches errors but does not prevent them.

### Governance Requirements Repetition

Tasks under the same objective contain near-identical governance requirements sections. This is intentional (self-containment) but creates repetitive reading and writing overhead. At 3+ concurrent tasks, this becomes noticeable friction.

### Cross-Artifact Coordination

The number of cross-references grows non-linearly with active artifact count. At 3 tasks, 2 reviews, 1 incident, 1 escalation, and 1 handoff (8 artifacts), cross-references total approximately 20-25 individual links. At 6 tasks, this would exceed 50 links.

### Review Synchronization

Multiple concurrent reviews covering overlapping scopes require coordination to avoid contradictory findings. At 2 reviews, manageable through communication. At 4+, becomes a coordination problem.

### Handoff Context Density

Handoffs capturing context for 3+ active artifacts become dense documents. Future resumption requires careful reading. No quick-resume summary exists.

## What Becomes Cognitively Expensive

1. **Traceability index maintenance** — mechanical but requires discipline.
2. **Governance requirements writing** — repetitive across similar tasks.
3. **Review scope differentiation** — requires careful reading to distinguish similar reviews.
4. **Cross-reference tracking** — grows non-linearly with artifact count.
5. **Lifecycle state management** — remembering which tasks are IN_PROGRESS, which reviews are APPROVED, which incidents are ACTIVE.

## What Governance Layers Remain Valuable

- **Human approval authority** — non-negotiable, always valuable.
- **Audit lifecycle** — provides accountability and historical record.
- **Review requirements** — catches errors before they become incidents.
- **Escalation lifecycle** — ensures governance tension is not ignored.
- **Traceability IDs** — enables audit, review, and handoff continuity.
- **Workflow stages** — provides structure for complex changes.

## What Governance Layers Become Repetitive

- **Governance requirements sections** — near-identical across tasks under same objective.
- **Severity classification references** — same severity model referenced repeatedly.
- **Review type selection** — same minimization strategy applied repeatedly.
- **Acceptance criteria structure** — similar patterns across similar tasks.

## What Artifacts Create Leverage

- **TRACEABILITY_INDEX.md** — single source of truth for all artifacts.
- **aeos_lint.py** — catches errors before they propagate.
- **WORKFLOW_TIERING_GUIDANCE.md** — reduces overhead for low-risk tasks.
- **REVIEW_MINIMIZATION_GUIDANCE.md** — reduces review fatigue.
- **HND-*.md** — preserves context across operational cycles.

## What Artifacts Create Drag

- **Near-identical governance sections** across tasks under same objective.
- **TRACEABILITY_INDEX.md** at 50+ artifacts — navigation becomes difficult.
- **Dense handoff documents** at 3+ active artifacts.
- **Multiple concurrent reviews** with overlapping scopes.

## What Should Remain Manual

- **Human approval authority** — never automate.
- **Review judgment** — never automate.
- **Audit judgment** — never automate.
- **Escalation resolution** — never automate.
- **Governance modification** — never automate.
- **Permission escalation** — never automate.
- **Operational risk acceptance** — never automate.

## What May Eventually Become Mechanically Assisted

- **Traceability reference validation** — already partially assisted by aeos_lint.py.
- **Formatting validation** — already assisted by aeos_lint.py.
- **Lifecycle completeness validation** — already partially assisted by aeos_lint.py.
- **Index update reminders** — could be a pre-commit hook (mechanical, not autonomous).
- **Cross-reference consistency checks** — could extend aeos_lint.py (deterministic, not autonomous).

## What Should NEVER Become Autonomous

- **Governance decision-making** — requires human judgment.
- **Review approval** — requires human judgment.
- **Audit conclusions** — requires human judgment.
- **Escalation resolution** — requires human judgment.
- **Risk acceptance** — requires human judgment.
- **Permission changes** — requires human authority.
- **Lifecycle state transitions** — requires human intent.

## First Real Scaling Limits of AEOS

### Limit 1: Active Artifact Count (~12 per objective)

Beyond approximately 12 active artifacts under a single objective, traceability maintenance and coordination overhead become the primary constraint. This is not a governance failure — it is an operational friction point.

### Limit 2: Concurrent Objectives (1 validated, 2+ untested)

AEOS has not been validated under 2+ concurrent objectives. Cross-project coordination, traceability spanning objectives, and escalation priority across objectives are untested scaling frontiers.

### Limit 3: Review Reviewer Capacity (2-3 concurrent per reviewer)

Human review quality degrades when reviewers must context-switch between 4+ concurrent reviews. This is a human constraint, not an AEOS constraint.

### Limit 4: Traceability Index Size (~50 artifacts)

TRACEABILITY_INDEX.md becomes difficult to navigate at approximately 50 artifacts. This is a markdown navigation constraint, not a governance constraint.

### Limit 5: Governance Documentation Overhead (3+ similar tasks)

Governance requirements sections become repetitive at 3+ similar tasks under the same objective. This is a documentation overhead constraint, not a governance constraint.

## Conclusion

AEOS scales well for single-objective operational cycles with up to approximately 12 active artifacts. The primary scaling limits are operational friction (traceability maintenance, coordination overhead, review fatigue) rather than governance failures. These limits should be monitored and addressed through guidance refinement and operational discipline, not structural governance changes. AEOS remains governance-first, repo-driven, markdown-first, human-governed, auditable, and deterministic under real operational pressure.
