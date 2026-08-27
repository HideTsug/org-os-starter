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
- Run this check before every commit, so that whether it happened is visible afterwards. Over all added lines in `git diff --cached`, inspect (a) real names, real financial figures, real communication history, and non-public internal themes, (b) keys, tokens, and secrets, and (c) any frontmatter `classification` outside categories 1 and 2 in `layer1/data-classification-matrix.md` — `public` and `internal` in the English canon, and whatever labels another working language gives those same two categories. Then output the list of files inspected and a single `PASS` or `HOLD` line. On `HOLD`, do not commit. What falls into each of the three is defined in `layer1/data-classification-matrix.md`.

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
- `working_language`: the language body text is written in. It is the repository's own working language and is declared once, on this line — the upstream Org-OS Starter declares **English**, with Japanese mirrors under `docs/ja/` (see "Upstream-Only Rules"). An adopting organization replaces this declaration with its own working language after copying the template; no bulk retranslation is required, since documents can be rewritten as they are revised. Frontmatter key names must remain English whatever the working language is.

## Upstream-Only Rules

This section applies to the upstream Org-OS Starter repository only. It is also the single list of what a copy of the template should drop or replace; Step 0 in `docs/setup-guide.md` points here.

- **English canon and Japanese mirror.** The English documents are the canon; `docs/ja/` holds their Japanese mirrors, and both sides move in the same change. Inside `docs/ja/`, references — including `[[wikilink]]` targets, frontmatter values, and file names quoted in prose — point to the Japanese counterpart whenever one exists, and to the English canon only when it does not. The `English version:` / `Japanese version:` header link at the top of a document is the intended exception. The file-by-file mapping is in `CONTRIBUTING.md`, "Before You Open a Pull Request".
- **Which language a reference points to, outside `docs/ja/`.** In the English canon — root `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `README.en.md`, and `docs/**` outside `docs/ja/` — every reference points to the English canon, including the first entry of the reading order in `AGENTS.md`, which is `README.en.md` and not the Japanese `README.md`. `README.md` is the Japanese entry point but is not a `docs/ja/` mirror: its reading-order table and file map describe the actual repository tree, so those two structures name the same English canon paths as `README.en.md`, row for row — except the reading-order row for the README itself, where each names its own file. A Japanese mirror may be named next to them — in the description column, or in prose outside those two structures — as an additional pointer for Japanese readers, never as the row's path.

After copying the template, clear these items:

| Item | Action |
|---|---|
| This section | Delete |
| `docs/ja/` | Delete, or keep only the documents the organization actually reads — and then stop maintaining them as mirrors |
| `working_language` in "Document Style" | Replace with the organization's own working language |
| `examples/demo-company/` | Delete once the demo has been tried |
| `ADOPTERS.md` | Delete — it lists organizations running the upstream template, not the copy. To be listed, open a PR or issue upstream |
| `docs/ai-agent-guide.md` | Delete — it is the upstream pre-clone briefing, and once the organization's copy exists its branch points are already behind you. Its Japanese mirror follows the `docs/ja/` row |
| `CONTRIBUTING.md` | Keep only as the guide for sending improvements back upstream. It governs the upstream repository, not the organization's own |
| The file map and reading-order table in `README.md`, and `README.en.md` if it is kept | Rewrite so they describe the organization's own repository |

## Writing Notes Under knowledge/

- Project notes follow `knowledge/projects/_template.md`; issue notes follow `knowledge/issues/_template.md`.
- Treat Google Drive as the v0.1 SSoT for human-authored originals. `knowledge/` contains only non-sensitive derived state, source links, and freshness metadata. Do not copy an original into the repository.
- Populate `source_urls` and `source_modified_at` when a note is derived from Drive. If a source becomes unavailable, mark the derived reference stale rather than treating cached content as current.
- Before using a derived note in an answer, enforce its `access_policy`. For `source_acl`, verify that the current user can open every source needed for the answer; repository access is not sufficient. Having no way to run that check — for example an agent with no Drive access in this session — is a failed check, not an exemption. If even one required source cannot be confirmed as openable by the current user, do not use the derived note in the answer and say that the answer cannot be given because access could not be verified.
- Drive access must follow `docs/google-drive-profile.md`: per-user OAuth, read-only in v0.1, and no service accounts or domain-wide delegation.
- Prefer non-destructive intake. Add to existing notes rather than deleting or rewriting them. Replace a note by creating a new note and linking the old one through frontmatter `supersedes`.
- The main path for non-engineer contributions is editing or creating the original in the approved Drive area. AI maintains a schema-compliant non-sensitive derived note when needed. Norm changes still use a repository proposal and review.

## Optional Support Confirmation

The optional support confirmation at the beginning of onboarding, for starring and following, must follow the "Optional Support Confirmation" section in `AGENTS.md`. Automated execution without consent is prohibited.

## Git Operations

- Direct push and merge permissions for `main` follow the adopting organization's operating rules in `docs/governance/operating-rules.md`.
- Split commits by logical unit and write messages that explain the intent of the change.
