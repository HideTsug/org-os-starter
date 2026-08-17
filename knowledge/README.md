# knowledge/ — Knowledge Base (Layer 2)

Japanese version: [docs/ja/knowledge/README.md](../docs/ja/knowledge/README.md)

This is the non-sensitive derived layer for the organization's current state. In the v0.1 operating profile, human-authored originals remain in Google Drive. AI uses this area for compact project state, source links, and freshness metadata; it does not copy restricted originals here.

## Note Types

| Directory | Type | Unit of one note |
|---|---|---|
| `projects/` | Project note | One active project |
| `issues/` | Issue note | One noticed problem, optionally linked to a project |

Each directory's `_template.md` is the format SSoT. `PJ-sample-equipment.md` and `ISSUE-0001.md` are fictional examples. Delete them once the organization has real notes.

## Common Rules

- Self-declare the data category in frontmatter `classification`, using the four categories in `layer1/data-classification-matrix.md`. **Allowed values are only `public` and `internal`** because category 3, customer/vendor-identifying data, and category 4, regulated data, must not be stored in this repository.
- **Do not write real customer or vendor names or real figures**. If needed, refer by case ID or role labels such as "Customer A" or "Representative".
- Note type is identified by `tags`, using `project` or `issue`. Search and aggregation tools read this tag.
- Drive-derived notes record `source_urls`, `source_modified_at`, and `source_status`. `source_status` is `current` or `stale`; inability to re-open a source must make it `stale`.
- Every derived factual claim must be traceable to a source URL. If the source does not support a claim, label it as inference or omit it.
- Do not delete outdated content. Add updates and refresh `last_reviewed`.

## Extension

Add note types such as customer notes, case notes, or meeting-note summaries together with the Google Drive intake design. See `docs/google-drive-profile.md` and the expansion patterns in `docs/architecture.md`. When adding a type, define its `_template.md` first.
