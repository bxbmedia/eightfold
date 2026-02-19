# Claude Code Skills

This directory contains skills adapted for Claude Code from the global Kimi skills system.

## Available Skills

| Skill | Description |
|-------|-------------|
| [`gh-commit`](gh-commit.md) | Create Git commits using the GitHub CLI with best practices |
| [`gh-pr`](gh-pr.md) | Create and manage GitHub Pull Requests |
| [`moonfall`](moonfall.md) | Digital familiar for memory, context, and knowledge integration |
| [`orchestrate`](orchestrate.md) | Decompose complex tasks and manage dependency graphs |
| [`project-audit`](project-audit.md) | Systematic assessment of codebase health and technical debt |
| [`skill-creator`](skill-creator.md) | Guide for creating effective skills |
| [`summon-the-council`](summon-the-council.md) | Debate complex decisions with multiple perspectives |

## Usage

These skills are reference documents. When working on tasks related to a skill's domain, reference the relevant skill file for:

- **Workflows** - Step-by-step procedures
- **Best practices** - Conventions and patterns
- **Examples** - Common usage patterns

## Skill Format

Each skill follows this structure:

```markdown
# Skill Name

> **When to use:** Clear description of triggers and contexts...

---

## Instructions...
```

The "when to use" section helps determine which skill applies to a given task.

## Adapting from Kimi Skills

These skills were retrofitted from the global Kimi skills (`~/.config/agents/skills/`). Key changes for Claude Code:

1. **Removed YAML frontmatter** - Claude Code doesn't use frontmatter-based triggering
2. **Added "when to use" header** - Preserves the description as a usage trigger
3. **Simplified file structure** - Single markdown file per skill (no SKILL.md naming)
4. **Kept content mostly intact** - Workflows, examples, and guidance remain the same
