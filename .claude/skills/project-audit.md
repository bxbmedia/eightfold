# Project Audit

> **When to use:** Systematic assessment of codebase health, stage viability, and technical debt. Use for evaluating options with data before major decisions, understanding current state before big changes, revealing hidden blockers when stuck, effort estimation for roadmap planning, or documenting actual vs intended state during onboarding.

---

> Systematic assessment of codebase health, stage viability, and technical debt.

## When to Audit

| Trigger | Why |
|---------|-----|
| Major decision point | Evaluate options with data, not gut |
| Before big changes | Understand what you're building on |
| Stuck/uncertain | Reveal hidden blockers |
| Planning roadmap | Effort estimates based on reality |
| Onboarding new devs | Document actual vs intended state |

## The Audit Process

### Phase 1: Inventory (30 min)

Map what exists:

```bash
# File structure
find . -type f -name "*.ts" -o -name "*.tsx" | head -50

# Dependencies
cat package.json
cat apps/*/package.json
cat packages/*/package.json

# Database schema
ls packages/db/src/schema/
ls packages/db/migrations/

# Tests
find . -name "*.test.ts" -not -path "*/node_modules/*"

# API routes
ls apps/web/src/routes/api/

# Components
ls apps/web/src/components/
```

**Document:**
- What's implemented
- What's placeholder/stub
- What's empty
- What's missing

### Phase 2: Functionality Check (30 min)

Test the critical paths:

```bash
# Does it start?
pnpm dev

# Does it build?
pnpm build

# Do tests pass?
pnpm test

# Database connection?
psql $DATABASE_URL -c "SELECT 1"

# Health endpoint?
curl http://localhost:3000/api/health
```

**Document:**
- What works
- What's broken
- What's untested

### Phase 3: Code Quality Review (45 min)

Review key files:

```bash
# Security
cat apps/web/src/lib/security/*.ts

# Auth flow
cat apps/web/src/routes/api/auth/*.ts

# Core business logic
cat apps/web/src/routes/api/core-feature/*.ts

# Database schema
cat packages/db/src/schema/index.ts
```

**Check for:**
- Module headers (PURPOSE/EXPORTS/PATTERNS/NOTES)
- Consistent patterns
- Error handling
- Security issues
- Type safety

### Phase 4: Stage Viability Assessment (30 min)

For each planned stage:

| Question | Yes | No | Notes |
|----------|-----|-----|-------|
| Schema ready? | ✅ | ❌ | Migrations exist? |
| Dependencies available? | ✅ | ❌ | Packages installed? |
| Patterns established? | ✅ | ❌ | Similar features exist? |
| Blockers identified? | ✅ | ❌ | External dependencies? |
| Can parallelize? | ✅ | ❌ | Independent workstreams? |

**Rate each stage:**
- **HIGH viability**: Clear path, low risk
- **MEDIUM viability**: Doable but complex
- **LOW viability**: Significant unknowns
- **NOT VIABLE**: Blocked or premature

### Phase 5: Technical Debt Catalog (15 min)

List issues found:

| Priority | Issue | Impact | Mitigation |
|----------|-------|--------|------------|
| 🔴 High | No tests for X | Regression risk | Add one test |
| 🟡 Medium | Duplicate code | Maintenance | Refactor |
| 🟢 Low | Outdated comment | Confusion | Update docs |

## Audit Report Template

```markdown
# Project Audit: [PROJECT NAME]

> Date: YYYY-MM-DD | Auditor: [Name]

## Executive Summary

| Stage | Status | Viability | Effort | Blockers |
|-------|--------|-----------|--------|----------|
| X | Current | HIGH/MEDIUM/LOW | N weeks | None/X |

**Key Finding**: One-sentence summary

## Current State

### ✅ Implemented
- Feature A (working)
- Feature B (working)

### 📋 Placeholders/Stubs
- Feature C (page exists, no logic)

### ❌ Missing
- Feature D (not started)

## Stage Viability

### Stage X — [Name] ✅ HIGH
**Requirements**: List
**Dependencies**: List
**Risk**: Low/Medium/High
**Effort**: N weeks
**Recommendation**: Proceed/Defer/Cancel

## Technical Debt

| Priority | Issue | Action |
|----------|-------|--------|
| 🔴 High | X | Fix Y |

## Recommendations

### Immediate
1. Action

### Short Term
1. Action

### Not Recommended
1. Action (why not)

## Conclusion

Summary and next steps.
```

## Red Flags to Watch For

| Flag | Meaning | Action |
|------|---------|--------|
| Empty packages/ folders | Planned but not implemented | Use or remove |
| TODO comments everywhere | Half-finished features | Complete or document |
| No tests for core features | Regression risk | Add minimal tests |
| Duplicate migrations | Database confusion | Consolidate |
| Generic config files | Not production-ready | Customize |
| "It works on my machine" | Setup fragility | Document dependencies |

## Tools for Auditing

```bash
# Code stats
cloc . --exclude-dir=node_modules

# Dependency tree
pnpm list --depth=10

# Test coverage
vitest run --coverage

# Type check
pnpm tsc --noEmit

# Lint
pnpm eslint .

# Security scan
pnpm audit
```

## Post-Audit Actions

1. **Update documentation** — Reflect actual state
2. **Update issues** — Log findings
3. **Update stages** — Revise plans based on reality
4. **Make decisions** — Use data to choose direction
5. **Schedule follow-up** — Re-audit after major changes

## Philosophy

> "Audit to understand, not to criticize."

The goal is clarity, not blame. Every codebase has debt. Every plan has gaps. Auditing reveals them so you can make informed decisions.

**Audit regularly. Audit honestly. Audit without ego.**
