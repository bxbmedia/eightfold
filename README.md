# eightfold — Git Training Portfolio

A hands-on GitHub training exercise for 8 developers. Each participant creates a personal portfolio page showcasing their demo project, practicing real git workflows: branching, committing, pushing, and pull requests.

## The Exercise

You will create your own portfolio page inside `portfolios/` and link it from the main landing page. Follow every step below from start to finish.

### Step-by-Step Workflow

#### 1. Clone the Repository

Open your terminal and clone the project to your local machine. This downloads a full copy of the repository so you can work on it locally.

```bash
git clone https://github.com/bxbmedia/eightfold.git
```

Then navigate into the project folder:

```bash
cd eightfold
```

#### 2. Pull the Latest Changes

Before starting any work, make sure you have the most up-to-date version of the project. Other developers may have pushed changes since the repo was first created. Run this command anytime you want to sync with what others have pushed.

```bash
git pull origin main
```

#### 3. Start the Local Server

Launch the built-in development server so you can preview the site in your browser as you work.

```bash
python start-server.py
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

#### 4. Create Your Branch

Create a new branch for your work. This keeps your changes separate from everyone else's until you're ready to merge. Replace `[your-name]` with your first name in lowercase.

```bash
git checkout -b add-[your-name]-portfolio
```

Example: `git checkout -b add-jordan-portfolio`

#### 5. Copy the Template

In your IDE (VS Code, Cursor, etc.), find the **portfolios/template** folder in the file explorer sidebar. Right-click the `template` folder, copy it, and paste it inside the **portfolios/** directory. Then rename the copied folder to your first name in lowercase.

For example, your new folder should be: `portfolios/jordan/`

> **Important:** Do not edit the original template folder — always work from your copy.

#### 6. Build Your Portfolio

This is your page — you have full creative control. Open `portfolios/[your-name]/index.html` in your IDE and make it your own:

- Fill in your project overview and details
- Add your tech stack
- Write your reflections on what you learned
- Customize the styling, layout, and content however you like

There are no restrictions on what you can do with your portfolio page. Make it yours.

#### 7. Update the Homepage

Open the root `index.html` file and scroll down to the Team section. Find the card with your name and:

- Replace the "Portfolio coming soon..." tagline with your own
- Update the link `href` to point to your portfolio (e.g. `portfolios/jordan/`)
- Change `btn-disabled` to `btn-primary` so the button is clickable

#### 8. Commit & Push

Stage all your changes, write a clear commit message, and push your branch to GitHub.

```bash
git add .
git commit -m "Add: [Your Name] portfolio page"
git push origin add-[your-name]-portfolio
```

If this is your first push for this branch, Git will create the remote branch automatically.

#### 9. Open a Pull Request

Go to the repository on GitHub — you should see a prompt to open a Pull Request for your recently pushed branch. Click it and:

- Give your PR a clear title (e.g. "Add: Jordan portfolio")
- Add a short description of what you built
- Request a code review from a teammate

You can also create the PR from the command line:

```bash
gh pr create --title "Add: [Your Name] portfolio"
```

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

1. Pull the latest changes from main into your branch:
   ```bash
   git pull origin main
   ```
2. Git will tell you which files have conflicts. Open them in your IDE and look for the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
3. Resolve by keeping both your card and any existing cards — don't delete anyone else's work.
4. Stage and commit the resolution:
   ```bash
   git add .
   git commit -m "Resolve: merge conflict in index.html"
   ```
5. Push again:
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
