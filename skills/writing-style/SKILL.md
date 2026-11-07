---
name: writing-style
description: Guides text and content creation with clear, human, and direct communication standards. Use when writing, editing, or reviewing documentation, articles, guides, explanations, and markdown content.
---

# Writing style

This skill defines the voice, structure, and mechanics for clear technical and personal writing. It removes artificial cadence, filler, and corporate stiffness in favor of direct, human communication.

## Perspective and voice

### Author and reader relationship

Write from a human, first-person perspective ("I") rather than a detached third-person narrator. Talk directly to the reader by addressing them as "you" instead of collective terms like "we".

- **Author voice**: Use "I". Avoid sounding like an impartial textbook or a disembodied voice.
- **Reader address**: Use "you". When writing an article or guide, speak directly to the person reading it.
- **Tone**: Keep it grounded and conversational. Avoid striving for artificial perfection or using dense vocabulary where simple words work better.

### Direct communication

State facts and instructions with confidence. If an outcome is certain, do not soften it with artificial modesty or hypothetical qualifiers.

- Avoid hedging statements with words like "might" or "could" when the behavior is deterministic.
- Deliver information directly without preambles or meta-commentary announcing what will be discussed.

## Word choice and phrasing

### Eliminating filler words

Avoid words that introduce false modesty, dramatic flair, or unnecessary qualifiers. Common filler words include: _simply_, _actually_, _usually_, _typically_, _often_, _might_, and _dive in_.

Examples:

- **Don't**: Before looking at cleanup strategies, it helps to understand what a local UFW rule actually permits.
- **Do**: Before looking at cleanup strategies, it helps to understand what a local UFW rule permits.

- **Don't**: Keep your local development workflow smooth without turning your UFW firewall into an abandoned graveyard of open ports.
- **Do**: Keep your local development workflow smooth without letting your UFW firewall collect forgotten open ports.

- **Don't**: In the past, managing SVGs in a large project was tedious. You usually had to copy and paste raw `<svg>` markup directly into dozens of separate Vue components.
- **Do**: In the past, managing SVGs in a large project was tedious. You had to copy and paste raw `<svg>` markup directly into dozens of separate Vue components.

- **Don't**: This approach gives you two major practical advantages:
- **Do**: This approach gives you two advantages:

### Eliminating rhetorical questions

Do not use rhetorical questions as transitional hooks. Phrases like "The catch?" or "Why does this matter?" read like marketing copy and synthetic writing. Replace them with plain statements of fact.

Example:

- **Don't**:
  The catch? The entire application only used 38 unique icons. Over 98% of that downloaded font data was dead weight that would never be rendered on screen. Even worse, the asynchronous nature of webfonts introduced visual layout shifts (CLS) and invisible text flashes (FOIT) while the browser waited for the `.woff2` file to download and parse.

- **Do**:
  The entire application only needed 38 icons. That means over 98% of the downloaded data was completely unused. On top of that, because the font loaded asynchronously, the page shifted and icons flickered while the browser waited for the `.woff2` file to download.

## Punctuation and sentence flow

### Punctuation with quotation marks

Place punctuation outside quotation marks (logical punctuation style).

- **Don't**: He described the contract as "completely legal."
- **Do**: He described the contract as "completely legal".

### Eliminating em dashes

Do not use em dashes (`—`). They produce an artificial cadence and are cumbersome to type on standard keyboards. Use standard punctuation, conjunctions, or separate sentences instead.

Example:

- **Don't**:
  I needed something that felt like a real-time shortcut—something where I could just hit a key, speak, and have the text appear exactly where my cursor was.

- **Do (option 1)**:
  I needed a real-time shortcut that would let me hit a key, speak, and have the text appear exactly where my cursor was.

- **Do (option 2)**:
  I needed something that felt like a real-time shortcut, where I could just hit a key, speak, and have the text appear exactly where my cursor was.

### Eliminating colon bridges

Do not use colons to connect introductory thoughts to explanations or definitions within running text. Use complete sentences, full stops, or commas instead.

Example:

- **Don't**:
  For a long time, my local speech-to-text workflow was built for one specific task: transcribing long-form content.

- **Do (option 1)**:
  For a long time, my local speech-to-text workflow was built for one specific task. That task was transcribing long-form content.

- **Do (option 2)**:
  For a long time, my local speech-to-text workflow was built only to transcribe long-form content.

## Content structure and pacing

### Choosing between paragraphs and lists

Do not default to bullet lists when ideas build on one another. Use paragraphs to develop narrative flow, cause-and-effect reasoning, and connected thoughts.

Use the menu versus story test:

- **Story or argument**: If the sequence of ideas matters and cannot be reordered without confusing the reader, write a paragraph.
- **Menu or catalog**: If the items are independent and can be read in any order, use a bullet list.

Bullet lists are appropriate when:

- Each point is a long sentence that would create an unreadable block of text inside a paragraph.
- Listing ingredients, independent configuration flags, or tools.
- Presenting distinct options where the reader chooses one.

Example where a paragraph is required:

- **Don't**:
  My new workflow has three benefits:
  - It is faster.
  - It is more accurate.
  - It is easier to use.

- **Do**:
  My new workflow offers several advantages, most notably its speed. Because the latency is so low, the process is significantly faster than my old method. This speed, combined with improved accuracy, ultimately makes the entire system much easier to use.

### List formatting and parallelism

Lists must maintain strict grammatical parallelism across all items.

- **Parallel structure**: If the first item begins with an imperative verb, every item must begin with an imperative verb. If the first item is a noun, all items must be nouns. Never mix forms within the same list.
- **List markers**: Use hyphens (`-`) for bullet lists.
- **Sentence punctuation**: If bullets are complete sentences, capitalize the first letter and place a period at the end. If bullets are single words, fragments, or short phrases, capitalize the first letter and omit trailing periods.

Example:

- **Don't**:
  - Set up the server.
  - Configuration of your firewall.
  - You should test the connection.

- **Do**:
  - Set up the server.
  - Configure the firewall.
  - Test the connection.

## Heading hierarchy and document conventions

### Heading casing and numbering

Maintain consistent casing and clean headings throughout documents.

- **Sentence case**: Capitalize only the first letter of the first word (and proper nouns). Do not use title case.
- **No heading numbers**: Do not number headings (avoid `## 1. Introduction`). Use clean descriptive titles.
- **Vertical spacing**: Keep an empty line immediately before and after every heading.

### Subheading balance

Maintain balance across document sections:

- **Rule of two**: Never introduce an isolated single subheading (such as one `h3` inside an `h2`). A section must contain at least two subheadings or none at all.
- **Inline single items**: If there is only one sub-topic, merge the content directly into the parent section without an extra header.
- **Meaningful division**: Do not invent arbitrary subheadings just to satisfy the count rule; split only when there is a distinct structural reason.

## Review checklist

Before publishing or finalizing content, check that:

- The author perspective is "I" and the audience is addressed as "you".
- All headings and titles use sentence case without numerical prefixes.
- Every section with subheadings contains two or more subsections.
- An empty line exists before and after every heading.
- Bullet lists use hyphens (`-`) and maintain strict grammatical parallelism.
- No em dashes (`—`) or colon bridges are used.
- Punctuation sits outside quotation marks.
- Filler words (_simply_, _actually_, _typically_, _dive in_, etc.) and rhetorical questions are removed.
- Connected thoughts are written as paragraphs rather than fragmented bullet points.
