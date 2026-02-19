# Orchestrate

> **When to use:** Decompose complex tasks, spawn agents, and manage dependency graphs to guaranteed completion. Use when tasks require 3+ distinct phases, multiple files/modules need coordinated changes, there's risk of partial implementation, E2E verification is required, or the task is too complex for a single agent.

---

> Decompose complex tasks, spawn agents, and manage dependency graphs to guaranteed completion.

## When to Orchestrate

Use when:
- Task requires 3+ distinct phases (data → logic → UI → integration)
- Multiple files/modules need coordinated changes  
- Risk of "partial implementation" (UI done, but API missing)
- E2E verification required
- "Just implement it" would be too vague for a single agent

## The Dependency Graph

Decompose the task into nodes. Each node = 1 agent session with explicit inputs/outputs.

```yaml
Example: Add Grimoire Card Editing Feature
├── 1-analyze-current     [archaeologist]     [BLOCKS: 2,3]
├── 2-data-model          [db-architect]      [BLOCKS: 4]       [NEEDS: 1]
├── 3-pure-functions      [developer]         [BLOCKS: 5]       [NEEDS: 1]
├── 4-api-endpoints       [developer]         [BLOCKS: 5]       [NEEDS: 2]
├── 5-ui-components       [ui-architect]      [BLOCKS: 6]       [NEEDS: 3,4]
└── 6-integration-e2e     [qa-specialist]     [BLOCKS: none]    [NEEDS: 5]
```

## Phase Structure

| Phase | Agent Type | Output | Verification |
|-------|-----------|--------|--------------|
| **1. Data Model** | Database Architect | Schema, types, migrations | `drizzle-kit generate` succeeds |
| **2. Pure Functions + TDD** | Developer | Business logic + unit tests | `bun test` passes |
| **3. Verify Logic** | Debugger/Tester | Edge case analysis | 0 failing tests, coverage >80% |
| **4. Isolated UI Component** | UI/UX Architect | Storybook/isolated route | Screenshot comparison passes |
| **5. Integration + E2E** | Integration Specialist | Wired UI + E2E tests | Real user flow simulation passes |

## Orchestration Protocol

### 1. DECOMPOSE

Create the dependency graph. For each node:

```markdown
### Node X: [Name]
- **Agent**: [specialist type]
- **Task**: [specific deliverable]
- **Inputs**: [files/data needed]
- **Outputs**: [files produced]
- **Blocked By**: [node IDs]
- **Unblocks**: [node IDs]
- **Completion Criteria**: [specific checks]
```

### 2. SPAWN

Spawn agents for ready nodes (all dependencies satisfied):

Use the Task tool to create subagents. If wait is needed, poll status via checking files.

### 3. MANAGE

Track state in memory or status file:

```yaml
Orchestration State:
  task_id: "add-card-editing"
  status: "in_progress"
  nodes:
    1-analyze-current:
      status: "complete"
      agent_id: "ag_001"
      outputs: ["analysis.md"]
    2-data-model:
      status: "running"
      agent_id: "ag_002"
      blocked_by: []
    3-pure-functions:
      status: "blocked"
      blocked_by: ["1-analyze-current"]
```

**Management Loop**:
1. Check all nodes for completion
2. If node completes successfully → mark outputs → unblock dependents
3. If node fails → HALT orchestration → report failure
4. If no nodes ready and incomplete remain → DEADLOCK detected → escalate

### 4. VERIFY

Each phase must pass before proceeding:

**Phase 1 Verify**:
```bash
cd packages/db && pnpm drizzle-kit generate
pnpm tsc --noEmit
```

**Phase 2 Verify**:
```bash
bun test packages/core/src/cards/edit.test.ts
```

**Phase 3 Verify**:
```bash
bun test --coverage packages/core/src/cards/
# Check coverage >80%
```

**Phase 4 Verify**:
- Screenshot isolation route
- Visual comparison (if baseline exists)
- Accessibility check (keyboard nav)

**Phase 5 Verify**:
```bash
# E2E test literally clicks buttons
bun test e2e/card-editing.spec.ts
# Asserts: network calls succeed, UI updates, state changes
```

## Completion Criteria

**MANDATORY** — Orchestration is NOT complete until:

- [ ] **All dependency graph nodes** marked COMPLETE
- [ ] **E2E tests pass** (simulates real user clicking through flow)
- [ ] **No regressions** in existing test suite (`bun test` passes)
- [ ] **Integration verified** (UI actually calls API, API actually writes DB)
- [ ] **Documentation** updated (module headers, README if needed)

## Handling Failures

### Node Failure
If agent reports ERROR:
1. Capture logs from agent output
2. Analyze: Is it a logic error or requirement issue?
3. **Logic error** → Respawn same agent with fix instructions
4. **Requirement issue** → Halt, ask user for clarification

### Timeout
If node exceeds timebox:
- 30 min for data model
- 45 min for pure functions  
- 60 min for UI
- 60 min for integration

**Action**: Escalate to `summon-council` to evaluate if task is too complex.

### Deadlock Detection
If circular dependencies detected in graph:
```
A blocks B, B blocks C, C blocks A
```
**Action**: Halt immediately. Require user to resolve architecture.

## Cross-Skill Integration

**With "Prove It Works"**:
- Before spawning Phase 2, run `prove-it-works` on data model
- Before spawning Phase 5, run `prove-it-works` on API endpoints

**With "Summon the Council"**:
- If architecture is uncertain during decomposition → summon council first
- If integration approach is debated (REST vs WebSocket) → summon council

**With "Project Audit"**:
- Run audit before orchestration if codebase state is unknown
- Use audit findings to populate "analyze-current" node

## Invocation

Say: **"Orchestrate the implementation of [feature]"**

The agent will:
1. Decompose into dependency graph
2. Spawn specialists for ready nodes
3. Manage flow until completion
4. Report final verification status

## Example Session

**User:** "Orchestrate adding real-time presence to cards"

**Orchestrator:**
```
Decomposing task...

Dependency Graph:
├── 1-audit-current       [archaeologist]     [READY]
├── 2-design-presence     [db-architect]      [BLOCKED:1]
├── 3-api-presence        [developer]         [BLOCKED:2]
├── 4-ui-presence         [ui-architect]      [BLOCKED:3]
└── 5-e2e-test            [qa-specialist]     [BLOCKED:4]

Spawning node 1 (audit-current)...
[Agent spawned - Archaeologist]
Polling status... [RUNNING] → [COMPLETE]
Outputs: analysis.md, current-flow.json
Unblocking node 2...

Spawning node 2 (design-presence)...
[Agent spawned - DB Architect]
[COMPLETE] → schema updated, migration created

... (progress through all nodes) ...

Running Phase 5 verification...
✅ E2E test passed: "User A sees User B editing"
✅ All nodes complete
✅ No regressions detected

Orchestration complete. Real-time presence active.
```

## Anti-Patterns

**DON'T:**
- Skip phases (don't go from data model straight to UI)
- Spawn multiple agents on same file concurrently (merge conflicts)
- Consider it done when "it works on my machine" (must pass E2E)
- Ignore blocked dependencies (orchestrate in order)

**DO:**
- Verify outputs of phase N before spawning phase N+1
- Keep dependency graph visible in status updates
- Fail fast if any node errors (don't limp along)
- Update orchestration status file after each node completion

## Remember

> "Orchestration guarantees completion, not just effort."

The goal is a **shippable feature**, not busy work. If the graph can't complete, halt and escalate.
