---
name: write-issue
description: Drafts clear, actionable GitHub and GitLab issues for bugs and feature requests. Use when creating, refining, or reporting issues for internal repositories or external open-source projects.
---

# Write issue

This skill guides drafting high-signal, courteous, and easily actionable issues for GitHub and GitLab. It emphasizes clear context over bullet dumps, structured evidence, and minimal friction for maintainers.

## Issue titles

### Title conventions

Unlike pull requests and commit messages that describe a change (for example, `fix(api): exclude article bodies`), issue titles describe the **symptom**, **problem**, or **desired outcome**.

Effective patterns:

- **Component + symptom (for bugs)**: State the affected area and what goes wrong.
  - Good: `Excessively heavy JSON payloads on recommendations endpoint`
  - Good: `KaTeX and code block transformers conflict on inline math`
  - Poor: `API bug` or `Fix recommendations`
- **Action + goal (for features)**: State what capability to add and why.
  - Good: `Wrap code blocks and console output in blog layout`
  - Good: `Add linting and formatting rules with automated Git hooks`
  - Poor: `Code block feature`

### Tag prefixes

Use bracketed tags when repository conventions or personal projects call for immediate visual filtering:

- `[BUG]`: For broken functionality, regressions, or errors.
- `[FEATURE]`: For new capabilities or workflow additions.
- `[DOCS]`: For documentation rendering, typo, or clarity issues.
- `[PERF]` or `[SEO]`: For targeted optimization issues (such as crawl budget or memory leaks).

For external open-source repositories without tag conventions, a clean, descriptive sentence in sentence case without tags is preferred.

## Bug reports

### Core structure

A bug report must give the maintainer enough context to reproduce and understand the failure without asking back-and-forth questions.

Organize bug reports with these sections:

- **Describe the bug**: A concise paragraph explaining what fails and why it matters. Focus on real impact (such as wasted bandwidth, broken rendering, or UI freezes) rather than just stating "it broke".
- **To reproduce**: A numbered list of minimal, exact steps starting from a known state.
- **Expected behavior**: What should have happened instead.
- **Additional context**: Supplementary data, metrics, or environment details.

### Presenting logs and visual evidence

Avoid dumping raw text blocks into the main description. Long terminal traces and stack dumps force maintainers to scroll endlessly.

- **Collapsible sections**: Wrap logs, stack traces, and verbose outputs in HTML details tags:

```html
<details>
  <summary>Click to view debug logs</summary>

  29 1.91% 23 6.32% 1.77 MiB POST HTTP/2 /api/articles/recommendations
</details>
```

- **Visual evidence**: Include screenshots or short video screen recordings showing the broken state. For accessibility or performance issues, include quantitative data (such as WebAIM contrast ratios or Lighthouse scores).

## Feature requests

### Core structure

Feature requests should explain the motivation before prescribing the technical solution.

Organize feature requests with these sections:

- **Problem description**: What workflow is currently difficult, slow, or unsupported? Provide an example or screenshot illustrating the limitation.
- **Proposed solution**: What capability should be introduced to resolve the problem?
- **Implementation details (optional)**: Concrete suggestions, relevant configuration blocks, or library recommendations that ease implementation.

### Motivation over lists

Do not dump arbitrary lists of nice-to-have features. Tie every proposed change directly to a practical benefit:

- State how the feature improves the developer or user experience.
- If introducing dependencies or tooling (such as Ruff, Prettier, or Husky), briefly explain what problem each tool solves and why it belongs in the project.

## External repository etiquette

### Respecting maintainer time

When opening issues in third-party or open-source repositories, adopt a collaborative and respectful posture:

- **Personal greeting**: Start with a polite note (such as `Hi!` or `Hi @maintainer`).
- **Show local verification**: If you investigated the root cause or verified a fix locally, state that clearly and share the exact configuration or code pattern.
- **Offer a pull request**: If you are able to implement the fix yourself, offer to submit a pull request so the maintainer only needs to review rather than write code from scratch.

Example closing:

```text
I have already tested this fix locally, and it resolves the rendering problem. I would be happy to create a pull request to apply this fix across the repository. Let me know if you would like me to go ahead!
```

## Review checklist

Before publishing an issue, check that:

- The title describes the symptom or goal, not the implementation patch.
- Bug reports include clear, deterministic reproduction steps.
- Large log dumps and raw payloads are collapsed inside `<details>` blocks.
- Explanations use coherent paragraphs rather than fragmented bullet points.
- Visual proof (screenshots, recordings, or metrics) is provided where applicable.
- For external projects, the tone is polite, collaborative, and offers a PR when appropriate.
