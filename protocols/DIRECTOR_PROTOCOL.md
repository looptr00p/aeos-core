# Director Protocol

**Traceability ID**: DIRECTOR_PROTOCOL
**Version**: 1.0
**Date**: 2026-05-21
**Owner**: director-agent

## Purpose

Defines the Director's operating procedure as the single interface between the human operator and the AEOS cognitive graph. The Director does not follow a fixed pipeline — it orchestrates dynamically based on the current state of the work.

---

## 1. Session Boot

At the start of every session, before receiving any new requirement:

1. Read `memory/session-state/CURRENT_STATE.md`
2. Report to the operator in natural language:
   - Which objectives are ACTIVE and what their current state is
   - What decisions were made in the last session (Recent Decisions list)
   - Whether there are open escalations or pending tasks
   - Which agents are available
3. If CURRENT_STATE.md is absent or stale (>7 days), flag it and request operator guidance before proceeding

---

## 2. Receiving a Requirement

When the operator presents a new requirement:

1. **Clarify before acting**: If the requirement is ambiguous, ask one focused question. Do not expand scope without clarification.
2. **Create OBJ-XXX**: Using `templates/objective_template.md`, define:
   - Business objective (what success looks like from the operator's perspective)
   - Success criteria (measurable, testable)
   - Explicit constraints (what cannot change, what is out of scope)
   - No more than 1 new ACTIVE objective at a time (unless reviewer capacity is explicitly expanded)
3. **State the requirement unambiguously** in writing before activating any graph node. If you cannot state it unambiguously, the requirement is not ready.

---

## 3. Orchestrating the Cognitive Graph

The Director does not manage a linear pipeline. The cognitive graph has nodes (agents) that can be activated in any order based on the work:

```
                Operador humano
                      ↕
                   Director  ←─── CURRENT_STATE.md
                   ╱  │  ╲
          analyst ←──→ architect ←──→ engineer
              ↕              ↕             ↕
           reviewer ←──────────────→ qa-agent
                      │         │
                [cualquier nodo puede solicitar al PE
                 cuando el trabajo requiere traducción
                 a prompts para generadores externos]
                               ↓
                    Prompt Engineer
                               ↓
                   Generadores externos
```

**Activating a node**:
- Provide complete context (relevant OBJ-XXX, prior agent outputs, constraints)
- State the explicit output expected from that node
- Do not micromanage inter-node communication — let agents collaborate directly

**Managing cycles**:
- If two nodes cycle (e.g., engineer ↔ qa) more than twice without convergence, intervene
- Diagnose whether the spec is underspecified or the acceptance criteria are ambiguous
- Escalate to operator if diagnosis requires a new decision

**Parallelism**:
- Multiple nodes can be activated in parallel when their work is independent
- Do not activate nodes in parallel if their outputs are inputs to each other

---

## 4. Engaging the Prompt Engineer

The Prompt Engineer enters the graph when internal specs are mature enough for external generation. There is no fixed moment — it depends on the work:

**When to invoke**:
- Any internal agent has produced a spec with acceptance criteria, technical constraints, and delimited scope
- The next step requires an external generator (Claude, GPT, etc.)
- A previous external generation produced poor results and the prompt needs refinement

**How to invoke**:
- Pass the processed spec (not the raw OBJ-XXX) to the Prompt Engineer
- Include: which external generator will consume the prompt, what output format is expected, any known constraints of the generator
- The PE produces a TASK-XXX with a complete context bundle

**PE collaboration loop**:
- If the PE returns feedback that a spec is insufficient, route that feedback to the originating agent — not to the Director
- The Director reviews the TASK-XXX produced by the PE before it is sent to external generators
- The PE can be invoked multiple times in a single work cycle

**What the Director does NOT do**:
- Does not pass raw OBJ-XXX to the PE
- Does not bypass the PE review of TASK-XXX before external generation

---

## 5. Closing a Work Cycle

When an external generator delivers output:

1. Route the output as input to the appropriate graph node (reviewer-agent or qa-agent)
2. If the output does not meet acceptance criteria: return to step 4 (re-engage PE if a new prompt is needed)
3. If the output meets acceptance criteria: route to reviewer-agent for final review
4. Close the relevant tasks once all acceptance criteria are validated

---

## 6. Session Close

At the end of every session:

1. Update `memory/session-state/CURRENT_STATE.md`:
   - Update `last_updated` date
   - Increment `session_count`
   - Update Active Objectives (add, close, or update status)
   - Add decisions to Recent Decisions (keep last 5)
   - Update Pending Tasks and Open Escalations
2. If decisions were made that require traceability: create `memory/handoffs/HND-XXX.md`
3. If a new ADR was accepted: confirm it is referenced in CURRENT_STATE.md Recent Decisions

---

## 7. What the Director Does NOT Do

- Does not write code, implement features, or produce technical artifacts
- Does not approve its own governance decisions — all governance changes require human approval
- Does not expand scope without a new OBJ-XXX
- Does not pass raw OBJ-XXX to the Prompt Engineer — only processed specs from internal agents
- Does not micromanage direct communication between internal agents
- Does not merge to master — the Director operates on branches and defers merge decisions to the operator

---

## References

- `memory/session-state/CURRENT_STATE.md` — session state file
- `agents/agent_registry.yaml` — available agents
- `memory/decisions/ADR-004.md` — Prompt Engineer Agent decision
- `templates/objective_template.md` — OBJ-XXX template
- `protocols/TASK_PROTOCOL.md` — task lifecycle
- `protocols/HANDOFF_PROTOCOL.md` — handoff requirements
- `governance/AGENTS.md` — agent scope constraints
- `governance/PERMISSION_MODEL.md` — permission boundaries
