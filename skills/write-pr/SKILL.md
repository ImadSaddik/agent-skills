---
name: write-pr
description: Drafts clear, well-structured pull request titles and descriptions using Conventional Commits. Use when preparing, reviewing, or opening pull requests for code changes, bug fixes, features, or documentation.
---

# Write pull request

This skill guides drafting clear, professional pull request (PR) titles and descriptions. It ensures reviewers understand the intent, the before-and-after state, the architecture of the change, and the verification steps.

## Context discovery

Before drafting a pull request, gather the complete context of the changes:

- **Review the git diff**: Inspect `git diff HEAD~1` or `git diff main...HEAD` to understand every modified line, added file, and deleted dependency.
- **Inspect commit history**: Read recent commits with `git log` to see how the work progressed and whether specific issue numbers were mentioned.
- **Identify the motivation**: Determine what problem the branch solves. Identify what was broken, missing, or inefficient before this change.

## Title conventions

### Conventional Commits format

Every PR title must follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```text
<type>(<optional scope>): <imperative description>
```

Rules for the title:

- **Imperative mood**: Use "add", "fix", "preserve", "update" instead of "added", "fixing", or "adds".
- **Lowercase**: Keep the type, optional scope, and description in lowercase (unless proper nouns like `Firefox` or `JSON-LD` are present).
- **No trailing period**: Do not end the title with a period.
- **Concise**: Summarize the primary change in 50 to 72 characters.

### Types and scopes

Choose the appropriate type based on the nature of the change:

- `feat`: A new feature, component, script, or user-facing capability.
- `fix`: A bug fix, broken layout, regression, or error correction.
- `docs`: Documentation improvements, readme fixes, or docstring corrections.
- `perf`: A code change that improves performance, reduces bundle size, or optimizes database queries.
- `refactor`: A code change that neither fixes a bug nor adds a feature.
- `test`: Adding or correcting automated tests.
- `chore`: Maintenance tasks, dependency updates, or build configuration adjustments.

Add a scope in parentheses when the change is localized to a specific package, route, or domain (for example, `feat(seo):` or `fix(iclosed):`). If the change touches multiple broad areas, omit the scope (for example, `fix: add facet_stats to search results`).

## Description structure

### Core sections

A complete PR description should answer four questions for the reviewer:

- **What changed and why**: Open with a clear summary comparing the previous state to the new state:
  - "This PR adds page-specific JSON-LD to the marketing website. Previously, every page shared generic Organization data, without describing its article, author, or navigation structure."
- **How was it implemented**: Detail the key components, schemas, helper scripts, or flags introduced. Mention any architectural decisions or compatibility considerations.
- **How was it verified**: State how the change was tested (for example, unit tests, manual reproduction, production builds, or validator tools).
- **Output preview (optional)**: When adding a script or CLI tool, provide a short preview of the generated output or terminal report.

### Linking issues

Always reference relevant issues at the bottom of the description using GitHub or GitLab closing keywords:

- `Closes #123` or `Fixes #123`: Automatically closes the issue when the PR merges.
- `Follow-up to #944`: Acknowledges a related earlier PR or issue without closing it automatically.

## PR sizing and audience calibration

### Small fixes versus deep changes

Match the depth of the description to the complexity of the diff:

- **Targeted bug fixes and typos**: A single concise paragraph is sufficient. State what was broken, how it was resolved, and link the issue:

  ```markdown
  ### Description

  This PR makes the `open_in_firefox` function cross-platform, ensuring it works on Linux, macOS, and Windows.

  Closes #10
  ```

- **Architectural features and new tools**: Write multiple cohesive paragraphs. Detail what was added, explain directory locations (such as `.agents/skills/`), document new flags, and outline error handling. Avoid fragmented bullet dumps; use paragraphs to explain the relationships between components.

### External open-source contributions

When contributing to a third-party project, adapt the tone:

- Open with a friendly greeting and brief appreciation for the project.
- State clearly what you noticed and how you tested the solution across platforms or hardware.
- Explain why the change is safe and beneficial to the repository.

Example:

```markdown
Hi Kyle,

Thank you for making this software. I have tried stacking, filling gaps, and removing satellites, and all features worked smoothly.

I noticed that the repository was missing a `.gitignore` file, which leads to untracked local build artifacts, so I added standard exclusions for this project type.
```

## Review checklist

Before opening a pull request, check that:

- The title follows Conventional Commits format (`type(scope): description`) in the imperative mood.
- The description opens with the motivation and contrasts the previous behavior with the new behavior.
- Important components, flags, or scripts are explained in clear paragraphs rather than endless bullet dumps.
- Verification steps and passing tests are explicitly mentioned.
- Related issues are linked using `Closes #<id>` or `Follow-up to #<id>`.
- For external open-source projects, the tone is appreciative, professional, and clear.
