# Agent skills

My personal collection of [Agent Skills](https://agentskills.io/) configured for my own workflows and preferences.

This repository serves as a central place to synchronize the rules and habits I care about across my different computers and coding assistants (Antigravity, Claude Code, OpenAI Codex, Cursor, and any tool supporting the open `SKILL.md` specification).

## Available skills

This repository currently includes the following skills:

- **[writing-style](skills/writing-style/SKILL.md)**: Enforces direct, human technical writing and eliminates AI fluff.
- **[write-issue](skills/write-issue/SKILL.md)**: Formats actionable bug reports and feature requests for GitHub and GitLab.
- **[write-pr](skills/write-pr/SKILL.md)**: Structures pull request descriptions and Conventional Commits titles.

## Installation

### Global install via npx skills

Install all skills directly into your global agent configuration directories:

```bash
npx skills add ImadSaddik/agent-skills --global
```

To update installed skills to the latest version:

```bash
npx skills update
```

### Symlink setup

If you have cloned the repository locally, run the script to link the skills directly into your agent folders:

```bash
python3 scripts/link.py
```

This creates symbolic links in the skill folders for each agent:

- `~/.gemini/antigravity-cli/skills/`
- `~/.claude/skills/`
- `~/.agents/skills/`
- `~/.cursor/skills/`
