---
doc_type: template
version: "1.0"
summary: Template for a human-facing knowledge-base user guide. It covers the three paths of reading, writing, and asking, plus what must not be written. Replace placeholders such as [Organization Name] before distributing it to members.
---

Japanese version: [docs/ja/docs/利用ガイド.md](ja/docs/利用ガイド.md)

# Knowledge Base User Guide

> A guide to this knowledge base written for non-engineers. No git knowledge is required. Members only need to remember the three paths of **read, write, and ask**, plus **what must not be written**.
>
> Template note: Replace `[Administrator Name]` with the organization's value, then remove any unnecessary notes before distribution. "Administrator" is the member-facing name for the implementation DRI.

## First Principles

- This GitHub knowledge-base repository contains **organizational knowledge**: project status, decision history, procedures, and rules.
- It does not contain, and must not contain, real customer or vendor names, figures, or communications.
- Members usually use it through AI. They do not need to memorize the repository structure.

## Path 1: Ask

**Ask AI in natural language.** Examples:

- "What are the current issues in the ____ project?"
- "List the active projects."
- "What are the rules for entering data into AI?"

AI searches this repository and answers with sources, including which note it used. **Searching is not a human task.**

## Path 2: Read

Log in to GitHub and open the repository. Documents can be read directly in the browser, including on a phone.

- First-time readers: start from the reading-order table in `README.md`.
- To understand a project's current state: open the relevant note under `knowledge/projects/` and read "Current Issues" and "Recent Decisions".
- To confirm rules: read `layer1/`. Only documents whose frontmatter has `status: agreed` are effective rules.

## Path 3: Write

**Main path: speak to AI.** Say things like "record this", "leave this decision in the project note", or "turn this method into a procedure." AI converts the content into the correct note format and opens a proposal, or PR. The administrator reviews the diff in the browser and presses "Merge" to apply it.

Lightweight path: use the pencil icon, Edit, in GitHub's browser UI, edit the text, and choose "Propose changes." This also becomes a proposal, so the main content is not rewritten immediately.

### Three Writing Rules

1. **Do not delete; add** — If old content becomes outdated, add an update or replace it with a new note. The history is also knowledge.
2. **One topic per note** — Do not put everything into one file.
3. **Leave format to AI** — Do not decide metadata, frontmatter, or location yourself. Through AI, those are handled correctly.

## What Must Not Be Written

- Real customer or vendor names, company names, financial figures, or email and chat communications
- Data with special legal management duties, such as individual numbers and identity-verification documents, according to the organization's category 4 definition
- Non-public information about HR, partnerships, M&A, unpublished financials, or disputes
- Passwords and API keys

If unsure, **do not write it**. Ask AI or [Administrator Name]. Detailed rules are in `layer1/data-classification-matrix.md` and `layer1/prohibited-uses.md`.

## FAQ

- **Q. What if we merge something wrong?** → A. Git can revert it. The repository is designed to be recoverable, so proposing changes is safe.
- **Q. I do not know where to write something.** → A. You do not need to decide. Tell AI the content, and AI will place it appropriately.
- **Q. My proposal, or PR, is left untouched.** → A. Send [Administrator Name] a short chat message.

## Revision History

| Date | Version | Author | Change |
|---|---|---|---|
| 2026-08-13 | v1.0 | HideTsug | Initial template |
