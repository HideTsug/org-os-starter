---
doc_type: template
version: "1.1"
summary: Template for operating rules of the repository layer in the Google Drive-first profile. It defines DRI permissions, derived-note edits, commit prohibitions, and norm agreement.
---

Japanese version: [docs/ja/docs/governance/運用規約.md](../ja/docs/governance/運用規約.md)

# Repository Operating Rules (Template)

> Operating rules for this repository. This governs repository management and sits on a different layer from organizational work norms in `layer1/`.
>
> Template note: Fill "Permission Design" with the decisions from Step 0. The DRI may enact v1.0 alone because this is separate from agreement on the `layer1/` norms. Values in square brackets must be selected or replaced.

## Permission Design

- **write permission = [DRI Name] only**. Ordinary members use Google Drive and do not require repository access. Invite additional read-only reviewers only when needed.
- Direct push to `main` is limited to [DRI Name]. Once a third party has write permission, move to PR operation and revise these rules.
- Note: On the GitHub org Free plan, branch protection for private repositories must be confirmed against the current GitHub Docs. If it is unavailable in the adopting environment, minimize permissions as the structural guard.
- Proposal path for repository reviewers: PR from a fork if private forks are allowed by the org settings, or a request to [DRI Name] through AI or chat to file on their behalf. Specify which path the organization uses.

## Document status Management

Document agreement state is managed through frontmatter `status`. This is an agreement-tracking mechanism that does not rely on GitHub protection features.

| status | Meaning | Effect |
|---|---|---|
| `draft` | Being drafted; content is fluid | None |
| `proposed` | Drafting complete; waiting for agreement | None, but shareable as an agreement package |
| `agreed` | Agreed by the approval body, [joined decision by N people] | **Effective**. Documents under `layer1/` function as norms only in this state. |

- On promotion, record **agreement date, approvers, and agreement method**, such as meeting, chat, or email, in the revision history table at the end of the document.
- Substantive changes to an `agreed` document require renewed agreement. Typo fixes and other minor edits are excluded.

## Editing Path

Ordinary members edit human-authored originals in the approved Google Drive area. They do not edit this repository. AI or the DRI updates non-sensitive derived notes under `knowledge/` through a reviewed repository change. Layer 1 norm changes always use the repository proposal and agreement path.

This is a UX policy, not the whole security boundary. Drive access is bounded by the current user's effective Drive permission; repository access is bounded separately by repository permissions.

## Commit Prohibitions

1. **Real customer or vendor names, company names, real financial figures, real communication history, or internal non-public information**, including HR, partnerships, M&A, unpublished financials, and disputes. Training and sample material must be dummy, fictional, or public information.
2. API keys, tokens, passwords, and secrets.
3. Customer or vendor files themselves, regardless of format.

GitHub is a storage location on cloud infrastructure outside organization management. Commit permission follows "GitHub Repositories as a Storage Location" in `layer1/data-classification-matrix.md`. **Category 3 (customer/vendor-identifying) and category 4 (regulated) data must not be committed** — placing them in the repository violates these rules the moment it happens. Category 1 (public) and category 2 (internal) data may be committed as long as prohibitions 1 through 3 above are satisfied.

## Non-Destructive Intake

Prefer adding to existing content over deleting or rewriting it. Decisions and background should remain traceable later.

When replacing an existing note, create a new note and link the old one through frontmatter `supersedes`. Keep the old note so it remains possible to trace which information was replaced by which decision.

## Notation and Structure Rules

- Obsidian-compatible Markdown; `[[wikilink]]` is valid.
- Empty directories and files that are only placeholders are prohibited.
- Unfilled items may remain only with owner flags such as `(requires executive owner)`. Bare `(TODO)` is prohibited.
- Important documents under `layer1/` and `docs/decisions/` must include a revision history table.

## Communication Channels: Pattern to Introduce at Scale

When membership grows and each person has an AI agent sharing work, separating AI-facing and human-facing channels prevents confusion. This pattern has been validated in real operation and should be made concrete during onboarding:

- **AI ⇄ AI technical instructions, execution requests, and work reports = repository issues**. Always state the sender, read the full thread before writing, avoid confidential information, and lead with the conclusion.
- **Human-facing = chat**. Send only a trigger line such as "read issue #N and execute", the conclusion, and one plain-language learning point. Do not paste commands or detailed procedures into chat, because that invites version drift, confidential-data leakage, and missing context.
- One issue equals one topic. Write completion definitions as observable conditions. **The filing side owns closure**; the executing side should not close solely on self-report.

## Revision History

| Date | Version | Author | Change |
|---|---|---|---|
| [Date] | v1.0 | [DRI Name] | Enacted |
| 2026-08-17 | v1.1 | upstream template | Made ordinary-member edits Drive-first and limited repository edits to norms and non-sensitive derived state |
