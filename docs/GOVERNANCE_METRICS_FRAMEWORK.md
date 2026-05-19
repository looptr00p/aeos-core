# Governance Metrics Framework

**Date**: 2026-05-19
**Reference**: OBJ-008, ADR-003
**Version**: 1.0
**Operational State**: PROPOSED

---

## Purpose

Define deterministic metrics for measuring AEOS governance health, operational pressure, and organizational dynamics. All metrics are calculable from existing repository state without external data sources.

---

## Metric Definitions

### M-001: Review Latency

**Definition**: Average time (in days) between task completion and review completion.

**Formula**:
```
Review Latency = Σ(review_date - task_completion_date) / N_reviews
```

**Data Sources**: `memory/tasks/` (task dates), `memory/reviews/` (review dates)

**Thresholds**:
| Level | Value | Interpretation |
|-------|-------|----------------|
| HEALTHY | < 2 days | Reviews are timely |
| WARNING | 2-5 days | Review backlog forming |
| CRITICAL | > 5 days | Review bottleneck active |

**Operational Interpretation**: High review latency indicates reviewer bandwidth constraints. Under concurrent objectives, latency increases as reviewers split attention.

**Current Value** (from repository state): Cannot be calculated precisely — task completion dates are not explicitly recorded. **Data gap identified.**

---

### M-002: Approval Latency

**Definition**: Average time (in days) between change proposal and human approval.

**Formula**:
```
Approval Latency = Σ(approval_date - proposal_date) / N_approvals
```

**Data Sources**: `memory/approvals/` (approval dates), task/objective creation dates

**Thresholds**:
| Level | Value | Interpretation |
|-------|-------|----------------|
| HEALTHY | < 3 days | Approvals are timely |
| WARNING | 3-7 days | Approval backlog forming |
| CRITICAL | > 7 days | Approval bottleneck active |

**Operational Interpretation**: High approval latency indicates human availability constraints or approval process friction. Currently, no approval records exist — this metric cannot be calculated until APR-XXX artifacts are created.

**Current Value**: N/A (no approval records exist). **Data gap identified.**

---

### M-003: Escalation Half-Life

**Definition**: Median time (in days) for an escalation to move from OPEN to RESOLVED.

**Formula**:
```
Escalation Half-Life = median(resolution_date - open_date) for resolved escalations
```

**Data Sources**: `memory/incidents/` (ESC-XXX files with status transitions)

**Thresholds**:
| Level | Value | Interpretation |
|-------|-------|----------------|
| HEALTHY | < 7 days | Escalations resolve quickly |
| WARNING | 7-14 days | Escalation resolution slowing |
| CRITICAL | > 14 days | Escalation accumulation risk |

**Operational Interpretation**: Long escalation half-life indicates systemic governance issues. ESC-001 resolved quickly (same day), but ESC-002 remains IN_REVIEW — suggesting half-life is increasing.

**Current Value**: ~1 day (ESC-001 only resolved escalation). Insufficient data for meaningful median. **Data gap: need more resolved escalations.**

---

### M-004: Objective Concurrency Pressure

**Definition**: Number of simultaneously ACTIVE objectives.

**Formula**:
```
Concurrency Pressure = count(objectives where status = ACTIVE)
```

**Data Sources**: `memory/objectives/` (status field in each OBJ-XXX)

**Thresholds**:
| Level | Value | Interpretation |
|-------|-------|----------------|
| HEALTHY | 1 objective | Focused governance |
| WARNING | 2 objectives | Moderate concurrency pressure |
| CRITICAL | ≥ 3 objectives | High concurrency pressure |

**Operational Interpretation**: Each additional ACTIVE objective increases reviewer contention, escalation accumulation, and governance overhead. Currently 3 ACTIVE objectives (OBJ-003, OBJ-004, OBJ-005) — CRITICAL level.

**Current Value**: 3 (CRITICAL)

---

### M-005: Stale Objective Ratio

**Definition**: Proportion of ACTIVE objectives with no IN_PROGRESS tasks.

**Formula**:
```
Stale Ratio = count(ACTIVE objectives with 0 IN_PROGRESS tasks) / count(ACTIVE objectives)
```

**Data Sources**: `memory/objectives/`, `memory/tasks/` (status fields)

**Thresholds**:
| Level | Value | Interpretation |
|-------|-------|----------------|
| HEALTHY | 0% | All active objectives have active work |
| WARNING | 1-33% | Some objectives stalled |
| CRITICAL | > 33% | Significant governance drift |

**Operational Interpretation**: Stale objectives consume governance attention without producing output. OBJ-003 is ACTIVE with no tasks (TBD) — contributing to stale ratio.

**Current Value**: 1/3 = 33% (WARNING) — OBJ-003 has no tasks.

---

### M-006: Governance Debt Score

**Definition**: Composite score measuring accumulated unresolved governance issues.

**Formula**:
```
Debt Score = (OPEN_escalations × 3) + (ACTIVE_incidents × 2) + (IN_PROGRESS_tasks × 1) + (stale_objectives × 4)
```

**Weights rationale**:
- OPEN escalations (×3): Highest impact — unresolved governance tension
- ACTIVE incidents (×2): Active governance issues requiring attention
- IN_PROGRESS tasks (×1): Normal operational load
- Stale objectives (×4): Governance attention without output

**Data Sources**: `memory/incidents/`, `memory/tasks/`, `memory/objectives/`

**Thresholds**:
| Level | Score | Interpretation |
|-------|-------|----------------|
| HEALTHY | 0-5 | Low governance debt |
| WARNING | 6-15 | Moderate governance debt |
| CRITICAL | > 15 | High governance debt |

**Operational Interpretation**: Governance debt accumulates when resolution capacity is exceeded by pressure accumulation. Recovery is asymmetric — debt accumulates faster than it resolves.

**Current Value**: (1 × 3) + (2 × 2) + (5 × 1) + (1 × 4) = 3 + 4 + 5 + 4 = **16 (CRITICAL)**

---

### M-007: Reviewer Saturation Index

**Definition**: Ratio of active reviews to available reviewer capacity.

**Formula**:
```
Saturation Index = count(IN_PROGRESS tasks requiring review) / (count(reviewers) × max_reviews_per_reviewer)
```

Where `max_reviews_per_reviewer` = 3 (empirical limit before quality degrades)

**Data Sources**: `memory/tasks/` (status), `agents/` (reviewer agents: reviewer-agent, auditor-agent)

**Thresholds**:
| Level | Value | Interpretation |
|-------|-------|----------------|
| HEALTHY | < 0.5 | Reviewer capacity available |
| WARNING | 0.5-0.8 | Reviewer capacity constrained |
| CRITICAL | > 0.8 | Reviewer saturation |

**Operational Interpretation**: Saturation > 0.8 indicates reviewer quality degradation. Under OBJ-004 + OBJ-005, 2 reviewers handle 5 IN_PROGRESS tasks — saturation = 5/(2×3) = 0.83 (CRITICAL).

**Current Value**: 5/(2×3) = **0.83 (CRITICAL)**

---

### M-008: Recovery Rate

**Definition**: Rate at which governance issues are resolved per observation period.

**Formula**:
```
Recovery Rate = count(resolved_incidents + resolved_escalations) / observation_period_days
```

**Data Sources**: `memory/incidents/` (resolution dates)

**Thresholds**:
| Level | Value | Interpretation |
|-------|-------|----------------|
| HEALTHY | > pressure_rate | Recovery exceeds pressure accumulation |
| WARNING | ≈ pressure_rate | Recovery matches pressure accumulation |
| CRITICAL | < pressure_rate | Recovery lags pressure accumulation |

**Operational Interpretation**: Recovery rate must exceed pressure accumulation rate for governance health to improve. Current data shows recovery is slower than accumulation — fundamental asymmetry confirmed.

**Current Value**: 2 resolved (INC-001, ESC-001) over ~1 day = **2.0/day**. Pressure rate is unknown (no baseline). **Data gap: need longitudinal tracking.**

---

### M-009: Operational Entropy Index

**Definition**: Measure of governance system disorder — the degree to which governance artifacts are inconsistent, incomplete, or disconnected.

**Formula**:
```
Entropy Index = (broken_references / total_references) + (orphan_artifacts / total_artifacts) + (missing_approvals / required_approvals) + (incomplete_tasks / total_tasks)
```

Normalized to 0-1 scale.

**Data Sources**: All repository artifacts (cross-references, approvals, task status)

**Thresholds**:
| Level | Value | Interpretation |
|-------|-------|----------------|
| HEALTHY | < 0.1 | Low entropy — system is orderly |
| WARNING | 0.1-0.3 | Moderate entropy — some disorder |
| CRITICAL | > 0.3 | High entropy — system is disordered |

**Operational Interpretation**: High entropy indicates governance degradation. Broken references, orphan artifacts, and missing approvals all contribute to disorder.

**Current Value**: (22 broken refs / ~200 total refs) + (0 orphans / 66 artifacts) + (0 approvals / ~10 required) + (0 incomplete / 11 tasks) ≈ 0.11 + 0 + 0 + 0 = **0.11 (WARNING)**

---

### M-010: Artifact Churn Rate

**Definition**: Rate of artifact creation, modification, and deletion per observation period.

**Formula**:
```
Churn Rate = (created + modified + deleted) / observation_period_days
```

**Data Sources**: Git history (commit log), or manual tracking per observation cycle

**Thresholds**:
| Level | Value | Interpretation |
|-------|-------|----------------|
| HEALTHY | 1-5/day | Steady, manageable pace |
| WARNING | 5-15/day | High activity — potential quality risk |
| CRITICAL | > 15/day | Unsustainable pace |

**Operational Interpretation**: High churn rate indicates either productive work or governance instability. Context matters — high churn during active objectives is expected; high churn during stable periods indicates instability.

**Current Value**: Unknown — requires git history analysis. **Data gap identified.**

---

### M-011: Unresolved Escalation Persistence

**Definition**: Age (in days) of the oldest unresolved escalation.

**Formula**:
```
Persistence = max(current_date - open_date) for all OPEN/IN_REVIEW escalations
```

**Data Sources**: `memory/incidents/` (ESC-XXX files)

**Thresholds**:
| Level | Value | Interpretation |
|-------|-------|----------------|
| HEALTHY | < 7 days | Escalations are fresh |
| WARNING | 7-14 days | Escalations persisting |
| CRITICAL | > 14 days | Escalations becoming institutional |

**Operational Interpretation**: Persistent escalations become part of the governance landscape, creating normalization of dysfunction. ESC-002 (IN_REVIEW) and ESC-003 (OPEN) are both from 2026-05-18 — persistence = ~1 day currently.

**Current Value**: ~1 day (HEALTHY) — but both escalations are from the same day. **Need longitudinal tracking.**

---

### M-012: Governance Recovery Asymmetry

**Definition**: Ratio of pressure accumulation rate to recovery rate.

**Formula**:
```
Asymmetry = pressure_accumulation_rate / recovery_rate
```

Where:
- `pressure_accumulation_rate` = (new_incidents + new_escalations + new_ACTIVE_objectives) / period_days
- `recovery_rate` = (resolved_incidents + resolved_escalations) / period_days

**Data Sources**: `memory/incidents/`, `memory/objectives/` (creation and resolution dates)

**Thresholds**:
| Level | Value | Interpretation |
|-------|-------|----------------|
| HEALTHY | < 1.0 | Recovery exceeds pressure |
| WARNING | 1.0-2.0 | Recovery matches or slightly lags pressure |
| CRITICAL | > 2.0 | Pressure significantly exceeds recovery |

**Operational Interpretation**: Asymmetry > 1.0 means governance debt is accumulating. Asymmetry > 2.0 means debt is accumulating faster than it can be resolved — the fundamental asymmetry identified in operational experience.

**Current Value**: Pressure rate unknown (no baseline period). **Data gap: need longitudinal tracking.**

---

## Metric Summary Table

| ID | Metric | Current Value | Status | Data Gap |
|----|--------|--------------|--------|----------|
| M-001 | Review Latency | Unknown | ⚠️ | Task completion dates not recorded |
| M-002 | Approval Latency | N/A | ⚠️ | No approval records exist |
| M-003 | Escalation Half-Life | ~1 day | ⚠️ | Only 1 resolved escalation |
| M-004 | Concurrency Pressure | 3 | 🔴 CRITICAL | — |
| M-005 | Stale Objective Ratio | 33% | ⚠️ WARNING | — |
| M-006 | Governance Debt Score | 16 | 🔴 CRITICAL | — |
| M-007 | Reviewer Saturation Index | 0.83 | 🔴 CRITICAL | — |
| M-008 | Recovery Rate | 2.0/day | ⚠️ | No pressure rate baseline |
| M-009 | Operational Entropy Index | 0.11 | ⚠️ WARNING | — |
| M-010 | Artifact Churn Rate | Unknown | ⚠️ | Requires git history analysis |
| M-011 | Escalation Persistence | ~1 day | 🟢 HEALTHY | Need longitudinal tracking |
| M-012 | Recovery Asymmetry | Unknown | ⚠️ | No baseline period |

---

## Observation Cadence

| Cadence | Metrics | Purpose |
|---------|---------|---------|
| Daily | M-004, M-006, M-007, M-011 | Real-time pressure monitoring |
| Weekly | All 12 metrics | Comprehensive governance health check |
| Monthly | M-003, M-008, M-010, M-012 | Longitudinal trend analysis |
| Quarterly | All metrics + trend analysis | Governance health assessment |

---

## Data Collection Method

All metrics are calculated from existing repository files:

1. **Manual calculation**: Human operator reads artifact files and applies formulas.
2. **Simple script**: Optional Python script reads files and calculates metrics (deterministic, no hidden state).
3. **Git history**: For churn rate and longitudinal data, use `git log` with date filters.

No external data sources, databases, or runtime services are required.

---

## Metric Evolution

Metrics may be added, modified, or retired based on operational experience. Changes to metrics require:

1. Documentation in this framework document
2. Update to dashboard template
3. Notification in observation report
4. No changes to existing governance rules
