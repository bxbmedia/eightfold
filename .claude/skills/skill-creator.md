# Skill Creator

> **When to use:** Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations.

---

This skill provides guidance for creating effective skills.

## About Skills

Skills are modular, self-contained packages that extend Claude's capabilities by providing specialized knowledge, workflows, and tools. Think of them as "onboarding guides" for specific domains or tasks—they transform Claude from a general-purpose agent into a specialized agent equipped with procedural knowledge.

### What Skills Provide

1. **Specialized workflows** - Multi-step procedures for specific domains
2. **Tool integrations** - Instructions for working with specific file formats or APIs
3. **Domain expertise** - Company-specific knowledge, schemas, business logic
4. **Bundled resources** - Scripts, references, and assets for complex and repetitive tasks

## Core Principles

### Concise is Key

The context window is a public good. Skills share the context window with everything else: system prompt, conversation history, other skills, and the actual user request.

**Default assumption: Claude is already very smart.** Only add context Claude doesn't already have. Challenge each piece of information: "Does Claude really need this explanation?" and "Does this paragraph justify its token cost?"

Prefer concise examples over verbose explanations.

### Set Appropriate Degrees of Freedom

Match the level of specificity to the task's fragility and variability:

**High freedom (text-based instructions)**: Use when multiple approaches are valid, decisions depend on context, or heuristics guide the approach.

**Medium freedom (pseudocode or scripts with parameters)**: Use when a preferred pattern exists, some variation is acceptable, or configuration affects behavior.

**Low freedom (specific scripts, few parameters)**: Use when operations are fragile and error-prone, consistency is critical, or a specific sequence must be followed.

Think of Claude as exploring a path: a narrow bridge with cliffs needs specific guardrails (low freedom), while an open field allows many routes (high freedom).

## Anatomy of a Skill

Every skill consists of a required markdown file:

```
skill-name/
└── skill-name.md (required)
    ├── Description header (required) - when to use this skill
    └── Markdown instructions (required)
```

### Skill Document (required)

Every skill document consists of:

- **Description header** (text): Contains a "when to use" description. This helps Claude understand when the skill gets used.
- **Body** (Markdown): Instructions and guidance for using the skill.

### Bundled Resources (optional)

Skills can also include optional resources in subdirectories:

- **`scripts/`** - Executable code (Python/Bash/etc.)
- **`references/`** - Documentation intended to be loaded into context as needed
- **`assets/`** - Files used in output (templates, icons, fonts, etc.)

## Progressive Disclosure Design Principle

Skills use a three-level loading system to manage context efficiently:

1. **Skill name** - Available in directory listing
2. **Description header** - When skill is referenced
3. **Full document** - When skill is explicitly used

## Skill Naming

- Use lowercase letters, digits, and hyphens only
- Prefer short, verb-led phrases that describe the action
- Namespace by tool when it improves clarity (e.g., `gh-commit`, `linear-issue`)
- Name the skill file exactly after the skill name

## Skill Creation Process

1. **Understand the skill** with concrete examples
2. **Plan reusable skill contents** (scripts, references, assets)
3. **Initialize the skill** - create the markdown file
4. **Edit the skill** - implement resources and write instructions
5. **Test the skill** - try it on real tasks
6. **Iterate** based on real usage

### Step 1: Understanding the Skill with Concrete Examples

To create an effective skill, clearly understand concrete examples of how the skill will be used. Ask:

- "What functionality should this skill support?"
- "Can you give some examples of how this skill would be used?"
- "What would a user say that should trigger this skill?"

### Step 2: Planning the Reusable Skill Contents

To turn concrete examples into an effective skill, analyze each example by:

1. Considering how to execute on the example from scratch
2. Identifying what scripts, references, and assets would be helpful when executing these workflows repeatedly

**Example:** When building a `pdf-editor` skill:
- Rotating a PDF requires re-writing the same code each time
- A `scripts/rotate_pdf.py` script would be helpful

### Step 3: Initializing the Skill

Create a new skill file with a descriptive header:

```markdown
# Skill Name

> **When to use:** Description of when to use this skill...

---

## Instructions...
```

### Step 4: Edit the Skill

When editing the skill, remember that the skill is being created for another Claude instance to use. Include information that would be beneficial and non-obvious.

**Writing Guidelines:** Always use imperative/infinitive form.

#### Description Header

Write a clear "when to use" description that includes:
- What the skill does
- Specific triggers/contexts for when to use it
- Example triggers from user queries

#### Body

Write instructions for using the skill and its bundled resources.

### Step 5: Testing

After creating the skill, test it on real tasks to ensure:
- The instructions are clear
- The workflow makes sense
- The outputs are as expected

### Step 6: Iterate

After testing the skill, users may request improvements. Often this happens right after using the skill, with fresh context of how the skill performed.

**Iteration workflow:**
1. Use the skill on real tasks
2. Notice struggles or inefficiencies
3. Identify how the skill should be updated
4. Implement changes and test again

## What to Not Include in a Skill

A skill should only contain essential files that directly support its functionality. Do NOT create extraneous documentation or auxiliary files, including:

- README.md
- INSTALLATION_GUIDE.md
- QUICK_REFERENCE.md
- CHANGELOG.md
- etc.

The skill should only contain the information needed for an AI agent to do the job at hand. It should not contain auxiliary context about the process that went into creating it, setup and testing procedures, user-facing documentation, etc.
