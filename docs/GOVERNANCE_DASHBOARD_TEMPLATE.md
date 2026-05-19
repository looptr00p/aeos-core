# Governance Dashboard Template

**Template ID**: DASH-GOV-001
**Version**: 1.0
**Regeneration Cadence**: Weekly (or per observation cycle)

---

## Usage Instructions

1. Copy this template to `memory/research/DASH-YYYY-MM-DD.md`
2. Fill in metric values from current repository state
3. Update status indicators based on thresholds
4. Add simulation results if applicable
5. Add trend data if longitudinal data exists
6. Save and commit

---

# AEOS Governance Dashboard

**Date**: YYYY-MM-DD
**Observation Cycle**: [cycle number]
**Prepared By**: [agent-id or human identifier]
**Phase**: [current phase]

---

## Governance Health Summary

| Metric | Value | Status | Trend |
|--------|-------|--------|-------|
| M-004: Concurrency Pressure | [N] | 🟢/⚠️/🔴 | ↑/↓/→ |
| M-005: Stale Objective Ratio | [N%] | 🟢/⚠️/🔴 | ↑/↓/→ |
| M-006: Governance Debt Score | [N] | 🟢/⚠️/🔴 | ↑/↓/→ |
| M-007: Reviewer Saturation | [N] | 🟢/⚠️/🔴 | ↑/↓/→ |
| M-009: Operational Entropy | [N] | 🟢/⚠️/🔴 | ↑/↓/→ |
| M-011: Escalation Persistence | [N days] | 🟢/⚠️/🔴 | ↑/↓/→ |

### Overall Health

**Status**: 🟢 HEALTHY / ⚠️ WARNING / 🔴 CRITICAL

**Summary**: [Brief narrative of governance health — 2-3 sentences]

---

## Active Objectives

| ID | Title | Status | Tasks | Reviews | Incidents | Escalations |
|----|-------|--------|-------|---------|-----------|-------------|
| OBJ-XXX | [Title] | [Status] | [N] | [N] | [N] | [N] |

---

## Governance Debt Breakdown

| Component | Count | Weight | Score |
|-----------|-------|--------|-------|
| OPEN Escalations | [N] | ×3 | [N] |
| ACTIVE Incidents | [N] | ×2 | [N] |
| IN_PROGRESS Tasks | [N] | ×1 | [N] |
| Stale Objectives | [N] | ×4 | [N] |
| **Total Debt Score** | | | **[N]** |

---

## Reviewer Workload

| Reviewer | Assigned Reviews | Capacity | Saturation |
|----------|-----------------|----------|------------|
| reviewer-agent | [N] | 3 | [N/3] |
| auditor-agent | [N] | 3 | [N/3] |
| **Total** | **[N]** | **6** | **[N/6]** |

---

## Escalation Status

| ID | Severity | Status | Age (days) | Related Tasks |
|----|----------|--------|------------|---------------|
| ESC-XXX | [Level] | [Status] | [N] | [TASK-XXX] |

---

## Incident Status

| ID | Severity | Status | Age (days) | Related Tasks |
|----|----------|--------|------------|---------------|
| INC-XXX | [Level] | [Status] | [N] | [TASK-XXX] |

---

## Simulation Results

### Active Simulations

| Scenario | Status | Trigger Date | Predicted Outcome | Actual Outcome |
|----------|--------|--------------|-------------------|----------------|
| S-XXX | [Active/Complete] | YYYY-MM-DD | [Prediction] | [Actual] |

### Simulation Insights

- [Insight 1]
- [Insight 2]

---

## Longitudinal Trends

### Metric Trends (Last 4 Cycles)

| Metric | Cycle N-3 | Cycle N-2 | Cycle N-1 | Current | Trend |
|--------|-----------|-----------|-----------|---------|-------|
| Debt Score | [N] | [N] | [N] | [N] | ↑/↓/→ |
| Saturation | [N] | [N] | [N] | [N] | ↑/↓/→ |
| Entropy | [N] | [N] | [N] | [N] | ↑/↓/→ |
| Concurrency | [N] | [N] | [N] | [N] | ↑/↓/→ |

### Trend Analysis

- [Trend observation 1]
- [Trend observation 2]
- [Trend observation 3]

---

## Governance Alerts

| Alert | Severity | Description | Action Required |
|-------|----------|-------------|-----------------|
| [Alert name] | HIGH/MEDIUM/LOW | [Description] | [Action] |

---

## Recovery Status

| Recovery Item | Status | Progress | ETA |
|---------------|--------|----------|-----|
| [Item name] | [In Progress/Complete/Blocked] | [N%] | [date or "unknown"] |

---

## Observations

### What Is Working

- [Observation 1]
- [Observation 2]

### What Needs Attention

- [Observation 1]
- [Observation 2]

### Emerging Patterns

- [Pattern 1]
- [Pattern 2]

---

## Next Observation Cycle

**Scheduled**: YYYY-MM-DD
**Focus Areas**:
- [Area 1]
- [Area 2]

**Data Gaps to Address**:
- [Gap 1]
- [Gap 2]

---

## Appendix: Metric Calculations

### M-004: Concurrency Pressure

```
count(objectives where status = ACTIVE) = [N]
```

### M-005: Stale Objective Ratio

```
count(ACTIVE objectives with 0 IN_PROGRESS tasks) / count(ACTIVE objectives) = [N]/[N] = [N%]
```

### M-006: Governance Debt Score

```
(OPEN_escalations × 3) + (ACTIVE_incidents × 2) + (IN_PROGRESS_tasks × 1) + (stale_objectives × 4)
= ([N] × 3) + ([N] × 2) + ([N] × 1) + ([N] × 4) = [N]
```

### M-007: Reviewer Saturation Index

```
count(IN_PROGRESS tasks requiring review) / (count(reviewers) × max_reviews_per_reviewer)
= [N] / ([N] × 3) = [N]
```

### M-009: Operational Entropy Index

```
(broken_references / total_references) + (orphan_artifacts / total_artifacts) + (missing_approvals / required_approvals) + (incomplete_tasks / total_tasks)
= [N]/[N] + [N]/[N] + [N]/[N] + [N]/[N] = [N]
```

### M-011: Escalation Persistence

```
max(current_date - open_date) for all OPEN/IN_REVIEW escalations = [N] days
```
