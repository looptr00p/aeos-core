# Concurrent Operations Learnings

## Purpose

Document what breaks first, what scales poorly, and what becomes operationally expensive when AEOS is applied to concurrent objective operations. This is the primary learning artifact from Concurrent Objective Operations Cycle 001.

## What Breaks First Under Concurrency

### Reviewer Capacity

Reviewer capacity is the first thing to break under concurrency. Under single-objective operations, reviewers can handle 2-3 concurrent reviews effectively. Under 2 concurrent objectives with 3 tasks each, reviewers must handle 4+ concurrent reviews. Context-switching overhead adds 30-40% to review time. Review quality degrades measurably. This is the first true concurrency limit of AEOS.

### Prioritization Ambiguity

When two objectives require simultaneous review attention, no mechanism exists to determine priority. This requires human judgment — which is correct but creates operational latency. Under time pressure, prioritization ambiguity becomes a significant coordination friction point. This is the second thing to break.

### Escalation Accumulation

Escalation generation rate doubles under concurrent objectives while resolution capacity remains constant. This creates escalation backlog risk. Under single-objective operations, 1 OPEN escalation was manageable. Under concurrent objectives, 2 OPEN escalations require monitoring. This is the third thing to break.

## What Scales Poorly

### Cross-Objective Coordination

Coordination overhead grows non-linearly with concurrent objectives. At 2 objectives, overhead is 1.5-2.0x single-objective overhead. This is multiplicative, not additive, because cross-objective coordination requires synchronized review timing, shared incident awareness, escalation priority alignment, and handoff context spanning both objectives.

### Context-Switching Overhead

Reviewers switching between objectives lose context and must re-establish understanding of each objective's scope, tasks, incidents, and escalations. This overhead is not captured in governance requirements but is a real operational cost.

### Traceability Maintenance

Traceability index maintenance burden doubles under concurrent artifact creation. Each artifact from both objectives requires corresponding index update. Under time pressure, this becomes error-prone.

### Handoff Density

Handoffs capturing context for 2 concurrent objectives become significantly denser. HND-005 captures 16 active artifacts — future resumption requires careful reading of both objective contexts.

## What Governance Layers Remain Valuable

- **Human approval authority** — non-negotiable, always valuable, especially under concurrency.
- **Audit lifecycle** — provides accountability across concurrent objectives.
- **Review requirements** — catches errors before they become incidents, even more critical under concurrency.
- **Escalation lifecycle** — ensures governance tension is not ignored across objectives.
- **Traceability IDs** — enables cross-objective audit, review, and handoff continuity.
- **Workflow stages** — provides structure for complex changes under concurrent pressure.

## What Governance Layers Become Operationally Expensive

- **Review requirements** — under concurrency, review demand exceeds reviewer capacity.
- **Escalation lifecycle** — under concurrency, escalation accumulation rate doubles.
- **Traceability maintenance** — under concurrency, maintenance burden doubles.
- **Handoff requirements** — under concurrency, handoff context spans multiple objectives.
- **Governance requirements sections** — under concurrency, near-identical sections multiply across objectives.

## What Causes Reviewer Fatigue

1. **Context-switching between objectives** — reviewers must maintain context for both objectives simultaneously.
2. **Overlapping review scopes** — TASK-004 and TASK-007 have overlapping governance review scopes.
3. **Review volume** — 4 concurrent reviews exceeds the 2-3 review capacity.
4. **Governance repetition** — same governance documents referenced across both objectives.
5. **Prioritization pressure** — reviewers must decide which objective to prioritize without explicit guidance.

## What Causes Coordination Drift

1. **Unsynchronized review timing** — reviews for different objectives run at different times.
2. **Uncoordinated traceability updates** — index updates from different objectives may conflict.
3. **Unaligned incident awareness** — INC-001 and INC-002 compound but are managed separately.
4. **Unprioritized escalations** — ESC-002 and ESC-003 compete for resolution attention.
5. **Uncoordinated task scopes** — overlapping task scopes create redundant review effort.

## What Causes Lifecycle Ambiguity

1. **Multiple IN_PROGRESS tasks** — 6 tasks across 2 objectives makes status tracking difficult.
2. **Multiple ACTIVE incidents** — 2 incidents compound under concurrent pressure.
3. **Multiple OPEN escalations** — 2 escalations create resolution priority ambiguity.
4. **Cross-objective dependencies** — TASK-007 references INC-001 from OBJ-004, creating cross-objective lifecycle coupling.
5. **Shared handoff context** — HND-005 spans both objectives, making resumption context complex.

## What Should Remain Manual

- **Human approval authority** — never automate.
- **Review judgment** — never automate.
- **Audit judgment** — never automate.
- **Escalation resolution** — never automate.
- **Governance modification** — never automate.
- **Permission escalation** — never automate.
- **Operational risk acceptance** — never automate.
- **Objective prioritization** — never automate. Requires human judgment under resource contention.

## What May Eventually Become Mechanically Assisted

- **Traceability reference validation** — already partially assisted by aeos_lint.py.
- **Formatting validation** — already assisted by aeos_lint.py.
- **Lifecycle completeness validation** — already partially assisted by aeos_lint.py.
- **Unresolved lifecycle continuity** — already assisted by aeos_lint.py check [9].
- **Concurrent objective detection** — could extend aeos_lint.py to detect multiple ACTIVE objectives.
- **Escalation accumulation detection** — could extend aeos_lint.py to detect multiple OPEN escalations.
- **Reviewer workload tracking** — could extend aeos_lint.py to count concurrent reviews per reviewer.

## What Should NEVER Become Autonomous

- **Objective prioritization** — requires human judgment under resource contention.
- **Review scheduling** — requires human judgment about reviewer capacity and availability.
- **Escalation resolution priority** — requires human judgment about operational impact.
- **Incident resolution priority** — requires human judgment about operational risk.
- **Governance scheduling** — requires human judgment about timing and coordination.
- **Resource allocation** — requires human judgment about reviewer capacity and workload.

## First True Concurrency Limits of AEOS

### Limit 1: Reviewer Capacity (4 concurrent reviews)

Reviewer capacity is the first true concurrency limit. Under 2 concurrent objectives with 3 tasks each, reviewers must handle 4+ concurrent reviews. This exceeds the 2-3 concurrent review capacity identified under single-objective operations. Context-switching overhead adds 30-40% to review time.

### Limit 2: Prioritization Ambiguity (no mechanism)

When two objectives require simultaneous review attention, no mechanism exists to determine priority. This is not a governance failure — it is an operational constraint that requires human judgment. But it creates measurable operational latency.

### Limit 3: Active Artifact Count (16 across 2 objectives)

At 16 active artifacts across 2 objectives, cognitive overload emerges. Operators must track 2 objectives, 6 tasks, 4 reviews, 2 incidents, 2 escalations, and 1 handoff. Each artifact requires ongoing attention to prevent drift.

### Limit 4: Escalation Accumulation Rate (2 OPEN across 2 objectives)

Escalation generation rate doubles under concurrent objectives while resolution capacity remains constant. This creates escalation backlog risk if accumulation continues unchecked.

### Limit 5: Context-Switching Overhead (30-40% review time increase)

Reviewers switching between objectives lose context and must re-establish understanding. This overhead is not captured in governance requirements but is a real operational cost that limits concurrent throughput.

## Conclusion

AEOS scales to 2 concurrent objectives with strict artifact limits (6 per objective, 16 total). The first true concurrency limit is reviewer capacity — 4 concurrent reviews exceeds sustainable capacity. The second limit is prioritization ambiguity — no mechanism exists to determine objective priority under resource contention. These are not governance failures — they are operational constraints that should be addressed through guidance refinement and operational discipline, not structural governance changes. AEOS should not be pushed beyond 2 concurrent objectives until these limits are addressed through guidance.
