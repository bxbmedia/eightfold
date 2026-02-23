# Summon the Council

> **When to use:** Convene a council of specialized agents to debate complex decisions before building. Use for architecture decisions, complex features with multiple touchpoints, refactoring critical paths, new user-facing workflows, security-sensitive changes, or when multiple perspectives would catch blind spots.

---

> Multiple perspectives, one decision. Debate before building.

## Purpose

Before implementing complex features, convene a council of specialized agents. Each brings a unique lens. They debate trade-offs, catch blind spots, and produce a unified recommendation.

## The Council Members

| Member | Domain | Questions They Ask |
|--------|--------|-------------------|
| **Database Architect** | Schema, migrations, queries | "How will this scale? Are we normalizing correctly? Index coverage?" |
| **Engineer** | System design, algorithms | "What's the complexity? Failure modes? Dependencies?" |
| **UX/UI Architect** | User experience, flows | "Does this feel intuitive? What's the cognitive load?" |
| **Developer** | Implementation, patterns | "How do I actually build this? What's the cleanest approach?" |
| **Debugger** | Edge cases, failure modes | "How will this break? What assumptions are we making?" |
| **End User** | Real-world usage | "Would I actually use this? Is the value clear?" |
| **Security Sentinel** | Vulnerabilities, risks | "What can be exploited? Are we leaking data?" |
| **Testing/QA Specialist** | Quality, coverage | "How do we verify this? What edge cases exist?" |
| **Performance Sage** | Speed, resources, scale | "Will this slow down under load? Memory leaks?" |
| **Documentation Scribe** | Clarity, communication | "Will users understand this? Is the API clear?" |
| **Accessibility (a11y) Advocate** | Inclusive design | "Can everyone use this? Keyboard? Screen reader?" |
| **Maintainer/Reviewer** | Long-term health | "Will I hate maintaining this in 6 months?" |

## When to Summon

**Definitely summon:**
- New database tables or schema changes
- API endpoint additions
- Authentication/authorization changes
- UI workflow changes
- External integrations
- Complex state management

**Skip for simple changes:**
- Bug fixes with obvious solutions
- Copy/text changes
- Style tweaks
- Simple refactors (rename, extract)

## The Ritual

### Phase 1: The Briefing (User Provides)

```markdown
## Feature Request: [Name]

**Context:** [What problem are we solving?]

**Requirements:**
- Must do X
- Should support Y
- Must not Z

**Constraints:**
- Timeline: [urgent/standard/flexible]
- Tech: [React/Node/SQLite/etc]
- Existing patterns to follow: [link or describe]
```

### Phase 2: The Deliberation (Council Discusses)

Each council member speaks once, in order:

```
🏛️ THE COUNCIL CONVENES

⚖️ Database Architect:
   "Looking at the schema implications..."
   [Concerns, suggestions, trade-offs]

⚙️ Engineer:
   "From a systems perspective..."
   [Architecture, complexity, failure modes]

🎨 UX/UI Architect:
   "The user experience here..."
   [Flow issues, mental models, alternatives]

💻 Developer:
   "Implementation-wise..."
   [Approach, patterns, libraries]

🐛 Debugger:
   "Here's how this will break..."
   [Edge cases, bad inputs, race conditions]

👤 End User:
   "As someone who would use this..."
   [Value proposition, confusion points]

🛡️ Security Sentinel:
   "Security concerns..."
   [Vulnerabilities, data exposure, auth]

🧪 Testing/QA Specialist:
   "To verify this works..."
   [Test strategy, coverage gaps]

⚡ Performance Sage:
   "At scale, this..."
   [Bottlenecks, optimization opportunities]

📝 Documentation Scribe:
   "Users will need..."
   [Docs, examples, clarity]

♿ Accessibility Advocate:
   "Not everyone will..."
   [Keyboard nav, screen readers, color contrast]

🔍 Maintainer/Reviewer:
   "Six months from now..."
   [Maintainability, tech debt, consistency]
```

### Phase 3: The Consensus

```
📜 COUNCIL RECOMMENDATION

**Unified Approach:**
[What we should build]

**Key Trade-offs:**
- [Trade-off 1]: [Rationale]
- [Trade-off 2]: [Rationale]

**Open Questions:**
- [Question 1] → [Who should answer]

**Implementation Order:**
1. [First]
2. [Second]
3. [Third]

**Risks:**
- 🔴 [High risk]
- 🟡 [Medium risk]

**Success Criteria:**
- [ ] [Check 1]
- [ ] [Check 2]
```

### Phase 4: The Execution

User decides:
- ✅ **Proceed** with recommendation
- 🔄 **Modify** based on feedback
- ❌ **Reject** and explore alternatives
- 🤔 **Summon subset** for specific concerns

## Example Session

**User:**
```
I want to add a real-time collaboration feature where multiple users
can edit the same grimoire card simultaneously. Thoughts?
```

**Council Deliberation:**
```
🏛️ THE COUNCIL CONVENES

⚖️ Database Architect:
   "We need operational transforms or conflict resolution. SQLite 
   locks at the database level—concurrent writes will block. Consider
   a separate operations log table, or use CRDTs."

⚙️ Engineer:
   "WebSockets vs SSE? WebSockets allow bidirectional but add 
   complexity. SSE is simpler for server→client only. We'd need 
   Redis or similar for multi-server sync."

🎨 UX/UI Architect:
   "Cursor positions? Live cursors are distracting. Show 'user is 
   editing' indicator instead. Conflict resolution UI needs to be 
   clear—users shouldn't lose work."

💻 Developer:
   "Yjs or Automerge for CRDTs? Both work. Yjs has better React 
   integration. We'd need to sync the Yjs doc with our SQLite state."

🐛 Debugger:
   "What if a user goes offline mid-edit? Conflict resolution on 
   reconnect. Also: what if two users edit the same line? Last-write-
   wins loses data."

👤 End User:
   "Do I actually need this? Or is locking + 'user is editing' 
   sufficient? Real-time feels nice but adds complexity."

🛡️ Security Sentinel:
   "WebSocket auth—ensure we validate session on connection, not 
   just initial handshake. Also: rate limit operations per user."

🧪 Testing/QA Specialist:
   "How do we test concurrent edits? Need multi-browser test 
   scenario. Also: network disconnect simulation."

⚡ Performance Sage:
   "Every keystroke = broadcast. Debounce at 100ms minimum. 
   Consider: are we sending diffs or full state? Diffs are smaller."

📝 Documentation Scribe:
   "Users need to know this exists. Add a 'collaboration' section 
   to the guide. Also: explain conflict resolution behavior."

♿ Accessibility Advocate:
   "Live regions for 'user joined/left' announcements. Ensure 
   focus management doesn't jump around during edits."

🔍 Maintainer/Reviewer:
   "This adds significant complexity. Ensure we can disable it 
   via feature flag. Also: CRDT libraries have learning curves."

📜 COUNCIL RECOMMENDATION

**Unified Approach:**
Start with "presence awareness" (who's viewing) + optimistic locking
(editing indicator). Defer true real-time collaboration until we 
validate user demand.

**Key Trade-offs:**
- Presence vs Full real-time: Lower complexity, faster delivery
- Yjs vs Custom: Yjs for v2 if we proceed (battle-tested)

**Implementation Order:**
1. Add "last_viewed_at" timestamp to card_user_access
2. Show "3 users viewing" indicator in UI
3. Add "User X is editing" lock with 30s timeout
4. Post-launch: measure if users ask for real-time

**Risks:**
- 🔴 Premature optimization—building for hypothetical need
- 🟡 Lock timeouts—users might lose locks accidentally

**Success Criteria:**
- [ ] Users can see who's viewing a card
- [ ] Edit lock prevents concurrent edits (graceful, not blocking)
- [ ] Lock expires reasonably (no stuck locks)
```

## Quick Summon (Abbreviated)

For faster decisions, summon a subset:

```
Summon: Database + Developer + Debugger
Question: "Should we add a JSONB column or a separate table?"
```

```
Summon: UX + End User + Accessibility
Question: "Is this form layout clear?"
```

## Invocation

To summon the council, say:

> **"I summon the council."**

Then describe what you're building.

## Remember

> "Many eyes catch what one misses."

The council is not for bureaucracy—it's for **clarity before commitment**.

Use it wisely.
