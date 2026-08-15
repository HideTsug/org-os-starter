# knowledge/ — Knowledge Base (Layer 2)

Japanese version: [docs/ja/knowledge/README.md](../docs/ja/knowledge/README.md)

This is where the organization's current state is accumulated as structured notes. AI searches this area to answer questions and converts member input into notes that belong here.

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
- Do not delete outdated content. Add updates and refresh `last_reviewed`.

## Extension

Add note types such as customer notes, case notes, or meeting-note summaries together with Layer 4 intake automation design. See the expansion patterns in `docs/architecture.md`. When adding a type, define its `_template.md` first.
