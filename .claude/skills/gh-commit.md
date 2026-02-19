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

## Moonfall-Specific Workflow

For the Moonfall project (located at `moonfall/moonfall-dev/` and `moonfall/moonfall-main/`):

**Structure:**
- `moonfall/moonfall-main/` → Tracks `main` branch (live/production site)
- `moonfall/moonfall-dev/` → Tracks `dev` branch (development/production pipeline)

**Commit Workflow:**
```bash
# 1. Always work in moonfall-dev
cd moonfall/moonfall-dev

# 2. Make changes, then commit and push to dev branch
git add -A
git commit -m "feat: description"
git push origin dev

# 3. Create PR (dev → main) - see gh-pr skill

# 4. After PR is merged, update main folder
cd ../moonfall-main
git pull origin main
```

**Important:** Never commit directly to `moonfall/moonfall-main/`. It should only receive updates via `git pull` after PRs are merged.

## Scripts

- `scripts/commit-with-scope.py` - Interactive commit with scope selection
