# GitHub PR Skill

> **When to use:** Create and manage GitHub Pull Requests using the GitHub CLI (gh). Use when the user wants to open a PR, create a pull request, review PR status, or manage PR workflows. Handles PR creation, setting title/body, adding reviewers, and linking issues. Triggers include "create a PR", "open pull request", "PR for this branch", or any PR-related workflow.

---

## Quick Start

```bash
# Create PR with title and body
gh pr create --title "Title" --body "Description"

# Create PR with draft flag
gh pr create --draft --title "WIP: Feature"

# Create PR and set reviewers
gh pr create --reviewer username --title "Title"
```

## Workflow

1. Check current branch: `git branch --show-current`
2. Push branch if needed: `git push -u origin <branch>`
3. Check for existing PR: `gh pr view`
4. Create PR with appropriate title/body
5. Set reviewers if specified
6. Mark as ready or draft

## PR Body Template

Include:
- What changed
- Why it changed
- Testing done
- Related issues (Fixes #123)

## Moonfall-Specific Workflow

For the Moonfall project (located at `moonfall/moonfall-dev/` and `moonfall/moonfall-main/`):

**Structure:**
- `moonfall/moonfall-main/` → Tracks `main` branch (live/production site)
- `moonfall/moonfall-dev/` → Tracks `dev` branch (development/production pipeline)

**PR Workflow (dev → main):**
```bash
# 1. Ensure you're in moonfall-dev with latest changes
cd moonfall/moonfall-dev
git checkout dev
git push origin dev  # if not already pushed

# 2. Create PR from dev to main
gh pr create --base main --head dev --title "Title" --body "Description"

# 3. After PR is merged on GitHub, update main folder
cd ../moonfall-main
git pull origin main
```

**PR Title Convention:** Use conventional commit format for PR titles:
- `feat: description` - New feature
- `fix: description` - Bug fix
- `refactor: description` - Code restructuring

**Always:** Create PR from `dev` → `main`, never the reverse.

## Scripts

- `scripts/create-pr.py` - Interactive PR creation with templates
