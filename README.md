# eightfold — Git Training Portfolio

A hands-on GitHub training exercise for 8 developers. Each participant creates a personal portfolio page showcasing their demo project, practicing real git workflows: branching, committing, pushing, and pull requests.

## Quick Start

```bash
# 1. Clone this repository
git clone https://github.com/YOUR_ORG/eightfold.git
cd eightfold

# 2. Start the local server
python start-server.py

# 3. Open http://localhost:8000
```

## The Exercise

You will create your own portfolio page inside `portfolios/` and link it from the main landing page.

### Step-by-Step Workflow

1. **Create your branch**
   ```bash
   git checkout -b add-[your-name]-portfolio
   ```

2. **Copy the template**
   ```bash
   cp -r portfolios/template portfolios/[your-firstname]
   # Example: cp -r portfolios/template portfolios/jordan
   ```

3. **Edit your portfolio page**
   - Fill in all bracketed sections in `portfolios/[your-name]/index.html`
   - Add custom styling if desired

4. **Update the landing page**
   - Edit root `index.html`
   - Replace your placeholder card with your actual info
   - Link to your portfolio folder

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: [Your Name] portfolio page"
   ```

6. **Push and open PR**
   ```bash
   git push origin add-[your-name]-portfolio
   ```
   Then open a Pull Request on GitHub.

### Content Requirements

Your portfolio page must include:
- [ ] Project overview (what your demo does, who it's for)
- [ ] Link to your demo project repository
- [ ] README summary or full content from your demo project
- [ ] claude.md explanation (what AI context you provided)
- [ ] Tech stack list (minimum 3 items)
- [ ] Reflection: what you learned building the demo

### Merge Conflicts (Expected!)

Since all 8 developers edit `index.html` to add their card, merge conflicts will happen. This is intentional practice. When you encounter a conflict:

1. Pull latest changes from main
   ```bash
   git pull origin main
   ```
2. Resolve by keeping both your card and existing cards
3. Commit the resolution
   ```bash
   git add .
   git commit -m "Resolve: merge conflict in index.html"
   ```
4. Push again
   ```bash
   git push origin add-[your-name]-portfolio
   ```

## Design System

| Element | Value |
|---------|-------|
| Background | `#0f0f13` (deep void) |
| Accent | `#d4a853` (amber/gold) |
| Primary text | `#f5f5f5` |
| Secondary text | `#a1a1aa` |
| Card surface | `rgba(255,255,255,0.03)` |
| Card border | `rgba(255,255,255,0.08)` |
| Border radius | `12px` cards, `8px` buttons |

Responsive breakpoints:
- Desktop: 4-column grid
- Tablet (≤1024px): 2-column grid
- Mobile (≤640px): 1-column grid

## File Structure

```
eightfold/
├── README.md                 # You are here
├── start-server.py          # Local dev server
├── index.html               # Landing page (edit your card here)
├── css/
│   ├── styles.css          # Global styles
│   └── portfolio.css       # Individual page styles
├── portfolios/
│   └── template/           # COPY THIS — don't edit directly
│       ├── index.html      # Your portfolio page starter
│       └── README.md       # Quick reference
└── .github/
    └── PULL_REQUEST_TEMPLATE.md
```

## Team

| Developer | Portfolio |
|-----------|-----------|
| Bailey | `portfolios/bailey/` |
| Don | `portfolios/don/` |
| Julio | `portfolios/julio/` |
| Kelvin | `portfolios/kelvin/` |
| Krystian | `portfolios/krystian/` |
| Mike | `portfolios/mike/` |
| Rion | `portfolios/rion/` |
| Vlad | `portfolios/vlad/` |

## Rules

1. **Never edit someone else's portfolio folder**
2. **Never push directly to main** — always use Pull Requests
3. **Write clear commit messages** explaining your changes
4. **Review at least one teammate's PR** before yours can merge

## Troubleshooting

**Server won't start?**
- Make sure you have Python 3 installed: `python --version`
- Try `python3 start-server.py` if `python` doesn't work

**Page not updating?**
- Hard refresh: `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac)
- Check the terminal for errors

**Git says "permission denied"?**
- You might be trying to push to main directly
- Create a branch first: `git checkout -b add-[your-name]-portfolio`

---

Built for learning. Break things. Ask questions. Have fun.
