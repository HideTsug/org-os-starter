---
doc_type: template
version: "1.1"
summary: Template for a human-facing Google Drive-first knowledge guide. Members ask through AI, read cited Drive originals, and edit originals in approved Drive areas.
---

Japanese version: [docs/ja/docs/利用ガイド.md](ja/docs/利用ガイド.md)

# Knowledge Base User Guide

> A guide to this knowledge base written for non-engineers. No git or GitHub knowledge is required. Members only need to remember three paths: **ask through AI, read the cited Drive original, and edit the Drive original**, plus where restricted information may be stored.
>
> Template note: Replace `[Administrator Name]` with the organization's value, then remove any unnecessary notes before distribution. "Administrator" is the member-facing name for the implementation DRI.

## First Principles

- Google Drive contains the human-authored originals and keeps the organization's existing access permissions.
- The repository contains agreed AI-use rules and non-sensitive derived state. It must not contain category 3 or category 4 details.
- Members use Drive and AI. The implementation DRI and AI maintain the repository layer.

## Path 1: Ask

**Ask AI in natural language.** Examples:

- "What are the current issues in the ____ project?"
- "List the active projects."
- "What are the rules for entering data into AI?"

AI searches Drive documents the current user can open plus non-sensitive derived state, then answers with links to the original Drive sources. It must distinguish source facts from inference and say when evidence is missing. **Searching is not a human task.**

## Path 2: Read the Original

Open the Google Drive link included in the answer. Drive is the normal member-facing reading surface, including on a phone.

- Confirm that the original supports the answer, especially for decisions and dates.
- If the link does not open, ask the document owner. Do not ask AI to bypass the permission.
- To confirm an AI-use rule, ask the implementation DRI or approved AI to cite the applicable agreed Layer 1 rule.

## Path 3: Write the Original

Edit or create the original in the approved Google Drive area. Keep it in the project's existing folder so the current sharing boundary remains visible. Examples include recording a decision in the meeting note or updating the project overview.

In v0.1, AI does not automatically overwrite or delete Drive originals. If you ask AI to draft an update, a human reviews it before placing it in Drive. Changes to AI-use norms are different: send them to [Administrator Name], because norms use the repository agreement process.

### Three Writing Rules

1. **Use the approved area** — Keep the original inside the selected shared drive or folder and follow its access rules.
2. **Preserve decisions and dates** — Add a dated correction instead of silently removing the context for an old decision.
3. **Keep one clear owner** — Every project folder or key original needs an owner who can confirm freshness and access.

## What Must Not Be Written

- Passwords, API keys, OAuth tokens, or recovery codes — nowhere in Drive or the repository
- Category 3 or category 4 information in the repository, PR bodies, issues, shared AI chats, or broadly shared Drive folders
- Information in a Drive folder whose audience is wider than the information's approved classification
- AI-generated text that retains restricted source details outside the original permission boundary

Restricted information may exist only in an approved Drive area whose access matches the organization's agreed data-classification rules. If unsure, **do not move or share it**. Ask [Administrator Name].

## FAQ

- **Q. Do I need a GitHub account?** → A. Not for ordinary ask, read, and write work. Use the approved AI and Google Drive.
- **Q. The cited source does not open.** → A. Ask the document owner. AI must not bypass Drive permissions.
- **Q. I do not know where to write something.** → A. Ask the project owner or [Administrator Name] for the approved Drive area.
- **Q. AI's answer looks stale.** → A. Check the cited original and report the mismatch to [Administrator Name] so the derived state can be refreshed.

## Revision History

| Date | Version | Author | Change |
|---|---|---|---|
| 2026-08-13 | v1.0 | HideTsug | Initial template |
| 2026-08-17 | v1.1 | HideTsug | Replaced member-facing GitHub workflows with Google Drive-first ask, read, and write paths |
