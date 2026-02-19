# Eightfold Project - Agent Guidelines

> This file provides context for AI assistants working on the Eightfold project.

## Project Overview

Eightfold is a portfolio website project containing multiple developer portfolios.

## Available Skills

This project includes Claude Code skills in `.claude/skills/`:

- **gh-commit** - Git commit best practices and conventional commits
- **gh-pr** - Pull request creation and management
- **moonfall** - Memory and context integration
- **orchestrate** - Complex task decomposition and management
- **project-audit** - Codebase health assessment
- **skill-creator** - Creating new skills
- **summon-the-council** - Multi-perspective decision making

Reference these skills when working on related tasks.

## Project Structure

```
.
├── css/                    # Stylesheets
├── portfolios/             # Individual portfolio pages
├── assets/                 # Images and other assets
├── index.html             # Main landing page
└── start-server.py        # Development server
```

## Development Workflow

1. Make changes to files
2. Test locally using `python start-server.py`
3. Commit using conventional commit format (`feat:`, `fix:`, `docs:`, etc.)
4. Push and create PR if needed

## Technology Stack

- HTML/CSS/JavaScript
- Python (development server)

---

*See `.claude/skills/README.md` for detailed skill documentation.*
