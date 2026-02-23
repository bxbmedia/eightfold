# GitHub Commit Skill

> **When to use:** Create Git commits using the GitHub CLI (gh). Use when the user wants to commit changes with messages, stage files, or push to remote. Handles conventional commits format, signing, and commit best practices. Triggers include "commit these changes", "make a commit", "commit with message", or any commit-related workflow.

---

## Quick Start

```bash
# Stage and commit with message
gh commit -m "message"

# Stage specific files and commit
gh commit path/to/file -m "message"

# Commit with conventional commit format
gh commit -m "feat: add new feature"
```

## Commit Message Format

Prefer conventional commits:
- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation
- `style:` Formatting
- `refactor:` Code restructuring
- `test:` Tests
- `chore:` Maintenance

## Workflow

1. Check status: `git status`
2. Stage files: `git add <files>` or `git add -A`
3. Write descriptive commit message
4. Commit: `git commit -m "message"`
5. Push if needed: `git push`
