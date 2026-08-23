---
doc_type: reference
version: "1.0"
audience: dual
summary: Executable v0.1 operating profile for using Google Drive originals with repository-based norms and non-sensitive derived knowledge.
---

Japanese version: [docs/ja/docs/Google-Drive-運用プロファイル.md](ja/docs/Google-Drive-運用プロファイル.md)

# Google Drive Operating Profile (v0.1)

> The v0.1 wedge is one path: connect an existing Google Drive area, ask recurring project questions, and receive answers with links to the originals. This profile does not require ordinary members to use GitHub.

This repository defines the operating contract and templates. It does not bundle an OAuth app, connector runtime, or search indexer.

## Responsibilities

| Surface | SSoT responsibility | Primary users |
|---|---|---|
| Google Drive | Human-authored originals, existing folder organization, sharing, ACLs, and revision history | All members |
| `layer1/` | Agreed AI-use rules, data classification, and prohibited uses | Approval body, implementation DRI, AI |
| `knowledge/` | Non-sensitive derived project state, issues, source links, and freshness metadata | AI, implementation DRI |

Do not silently copy an original from Drive into `knowledge/`. A derived note must be useful without reproducing restricted details and must link back to every original it summarizes.

## Included and Not Included

**Included in v0.1**

- One Google Workspace tenant
- One selected shared drive or top-level folder
- Google Docs and other files readable through the Drive API
- Read-only search, project catch-up, and source-linked answers
- Non-sensitive derived notes under `knowledge/`
- Per-user OAuth and permission-differential verification

**Not included in v0.1**

- Notion, Slack, Chatwork, SharePoint, or generic filesystem sources
- Service accounts or domain-wide delegation
- Automated editing or deletion of Drive originals
- Copying restricted originals into GitHub
- A company-wide migration or forced reorganization of existing Drive content

## Setup Contract

### 1. Choose the Source Boundary

- Select one shared drive or top-level folder for the first use case.
- Select three to five active projects inside that boundary.
- Keep existing originals in place. Do not reorganize the entire drive for onboarding.
- Record a stable project slug and the corresponding Drive folder URL in the derived project note.

Recommended minimal mapping:

| Project slug | Drive folder | Derived note |
|---|---|---|
| `PJ-EXAMPLE` | Original project folder URL | `knowledge/projects/PJ-example.md` |

Folder placement helps route documents to a project, but it does not override the user's effective Drive permission.

### 2. Establish the Access Path

- Use an agent connector or Drive API client authenticated with the current user's OAuth grant.
- Request read-only access for v0.1.
- Do not use a service account or domain-wide delegation.
- Record which inference path from `layer1/data-classification-matrix.md` processes the retrieved content.

### 3. Run the Permission-Differential Test

Use two organization accounts with different access:

1. Put one harmless test document in a folder visible to both accounts.
2. Put a second harmless test document in a restricted folder visible to only one account.
3. Ask the same question as each account.
4. Test both direct retrieval and an existing derived note. Pass only if the restricted answer and source are absent for the account without access.

Do not connect real confidential documents until this test passes and the applicable Layer 1 documents are `agreed`.

Record the result where a later session can find it. Agreement is already machine-readable in frontmatter `status`; the test result needs an equivalent. When the test passes, create `docs/decisions/ADR-000N-drive-permission-test.md` from [ADR-0000-template.md](decisions/ADR-0000-template.md) and record the date, the role and access scope of each of the two accounts, both paths tested — direct retrieval and an existing derived note — and the result. Before connecting real confidential documents, AI confirms that this ADR exists and that its recorded result is a pass. If it is absent, treat the test as not yet run, whatever an earlier session may have reported.

### 4. Create the First Derived State

For each selected project, create or update a note from `knowledge/projects/_template.md`:

- `source_urls`: the original Drive folder or document URLs
- `source_modified_at`: the newest source modification time used for the summary
- `last_reviewed`: when a human or AI last verified that the derived state still matches the originals
- `classification`: only categories 1 and 2 of `layer1/data-classification-matrix.md` may be committed — `public` and `internal` in the English canon, and whatever labels another working language gives those same two categories
- `access_policy`: `source_acl`, the only allowed v0.1 value. Before using the derived note, AI verifies access to every source needed for the answer

Keep category 3 and category 4 details in Drive. The derived note may contain a non-sensitive reference such as a case ID only when Layer 1 permits it.

Do not treat repository access as permission to disclose a derived note. For a note built from multiple sources, use the intersection of source audiences. A broader derived audience is outside v0.1 and requires a new ADR.

### 5. Verify the Ask Path

Before expanding scope, answer five recurring questions chosen by project owners. Every answer must:

- state when the source was last modified or reviewed;
- link to the original Drive document;
- distinguish source facts from AI inference;
- omit documents the asking user cannot open;
- say that evidence is missing when the source does not support an answer.

## Change and Freshness Contract

- Use the Drive change feed for incremental discovery. A push notification is only a wake-up signal; fetch the corresponding changes before updating derived state.
- Store a stable source ID, URL, modification time, and content hash when an implementation has an index.
- Make reprocessing idempotent: unchanged source content must not create duplicate notes or repeated history entries.
- If a source is deleted, moved, or loses access, mark the derived reference stale. Do not silently treat the last cached content as current.

## Daily Member Workflows

1. **Ask** — Ask the approved AI about a project. It searches accessible Drive originals and the derived `knowledge/` state, then cites the originals.
2. **Read** — Open the cited original in Google Drive. Drive is the member-facing reading surface.
3. **Write** — Edit or create the original in the approved Drive area. v0.1 does not let AI overwrite originals automatically.

Changes to Layer 1 norms are different: they use the repository agreement and review process, not the ordinary Drive write path.

## Exit Gate

The Drive-first path is validated when three external organizations complete setup and at least one repeats the ask path within fourteen days. If connected users cannot name a recurring question, do not add a new connector; refine the use case or source coverage first.

## Related Decisions

- [ADR-0001: Google Drive-First v0.1](decisions/ADR-0001-google-drive-first-v0.1.md)
