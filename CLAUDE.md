# Operating Rules for AI Agents Maintaining This Repository

Japanese version: [docs/ja/CLAUDE.md](docs/ja/CLAUDE.md)

This file defines the operating rules for AI agents that read and write this knowledge-base repository. It is different from `layer1/ORG-CLAUDE.md`, which defines business operating norms for all AI agents supporting the adopting organization. Do not confuse the two.

> Template note: This file is the initial default provided by Org-OS Starter. It can be used as-is at the beginning and revised as the organization's own operations mature.

## Document Authority and Priority

- `layer1/` is the normative SSoT. Only documents whose frontmatter has `status: agreed` are authoritative.
- `docs/` contains explanatory material, guides, and decision records. It is not normative unless explicitly promoted by the adopting organization.
- Do not duplicate the same information across documents. Refer to it with `[[wikilink]]` or relative Markdown links.
- Frontmatter key usage:
  - `status` is the agreement state. It moves through `draft → proposed → agreed`. It belongs to normative documents such as `layer1/`, operating rules after enactment, and ADRs. Promotion requires recording the agreement date and approvers in the revision history.
  - `doc_type` is the document type. Use `reference` for explanatory reading material and `template` for fill-in templates. Documents that are outside the agreement process use this key and do not carry `status`.

## Commit Prohibitions

- Do not commit real customer or vendor names, real financial figures, real communication logs, or internal non-public information (HR, partnerships, M&A, unpublished financials, disputes). Samples and training material must use dummy, fictional, or public information. Ordinary category-2 "Internal" notes — project status, issues, work procedures — do not fall under this prohibition and are expected to be committed after processing (`knowledge/README.md`).
- Do not commit API keys, tokens, passwords, or secrets.
- If the classification of data is unclear, check `layer1/data-classification-matrix.md` before adding it.

## Structure Rules

- Do not create empty directories or files that are only placeholders. Create directories only when real content is ready to live there.
- Do not create directories for Layers 3 through 5. Keep those concepts described only in `docs/architecture.md` until real operational content is ready.
- Unfilled items must not use bare `(TODO)`. Use owner-marked flags such as `(requires executive owner)` or `(requires system owner)`.
- Placeholder conventions across templates:
  - `[square brackets]` mark values that must be replaced during onboarding, such as `[Organization Name]`, `[DRI Name]`, or `[Date]`. If they remain after operations begin, something was missed.
  - `(requires role name)` marks an undecided item with an accountable owner. These may remain while the document is still in `draft`.

## Document Style

- Use Obsidian-compatible Markdown. Normative documents should include `status`, `version`, and `summary` in frontmatter.
- Prefer bullet lists, one fact per item, and fact-based writing. For decisions, use the format "Decision: ... Reason: ...".
- Important documents under `layer1/` and `docs/decisions/` must end with a revision history table.
- Body text should be English. Frontmatter key names must remain English.

## Writing Notes Under knowledge/

- Project notes follow `knowledge/projects/_template.md`; issue notes follow `knowledge/issues/_template.md`.
- Prefer non-destructive intake. Add to existing notes rather than deleting or rewriting them. Replace a note by creating a new note and linking the old one through frontmatter `supersedes`.
- The main path for non-engineer contributions is: speak to AI → AI converts the content into a schema-compliant note → AI opens a PR.

## Optional Support Confirmation

The optional support confirmation at the beginning of onboarding, for starring and following, must follow the "Optional Support Confirmation" section in `AGENTS.md`. Automated execution without consent is prohibited.

## Git Operations

- Direct push and merge permissions for `main` follow the adopting organization's operating rules in `docs/governance/operating-rules.md`.
- Split commits by logical unit and write messages that explain the intent of the change.
