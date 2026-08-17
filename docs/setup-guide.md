---
doc_type: reference
version: "1.1"
summary: Org-OS Starter setup guide covering Layer 1 agreement, a Google Drive-first Layer 2, permission verification, and recurring use.
---

Japanese version: [docs/ja/docs/導入ガイド.md](ja/docs/導入ガイド.md)

# Setup Guide

> A guide for turning this repository into the adopting organization's Org-OS. Every step can be done through conversation with AI such as Claude Code. The parts humans must decide directly are called out explicitly.

## Step 0: Decide the Operating Body

Before working on documents, decide only three things.

1. **Implementation DRI** — The administrator of this repository. This person has merge authority and leads drafting of norms. The best fit is the person most familiar with AI tools; they do not need to be an engineer.
2. **Approval body** — The people whose agreement makes the norms in `layer1/` effective. The recommended shape is a joined decision by the executive owner, implementation DRI, and system owner. Two or three people is typical. One person may hold multiple roles, but keep business judgment and AI technical judgment distinct.
3. **First narrow use case** — The recommended use case is cross-project knowledge organization plus conversational catch-up. Choose the area where people most often ask, "what happened with that?"

After deciding, fill the permission design section in `docs/governance/operating-rules.md`.

## Step 1: Fill the Three Layer 1 Documents

Fill the three templates under `layer1/` for the adopting organization. **Do not wait for perfection.** Fill the parts that can be confirmed, and leave management-judgment items as owner flags such as `(requires executive owner)` while beginning draft operation.

| Document | Main filling work | Strongly industry-dependent areas |
|---|---|---|
| [ORG-CLAUDE.md](../layer1/ORG-CLAUDE.md) | Organizational policy, decision priorities, industry-law compliance | Compliance norms, including industry law, qualification law, and statutory confidentiality |
| [data-classification-matrix.md](../layer1/data-classification-matrix.md) | Concrete examples for the four data categories and inventory of execution environments | What belongs in category 4, regulated data |
| [prohibited-uses.md](../layer1/prohibited-uses.md) | Concrete wording for absolute prohibitions | Professional responsibility and exclusive professional acts |

Filling tips:

- Ask AI: "Our industry is ____. Create a draft for the industry-dependent parts of this document based on our industry law. **Always verify the primary legal text.**" Do not leave final judgment to AI; qualified professionals and responsible owners must confirm.
- When unsure about classification, choose the stricter category. Loosening should come only after operational evidence.
- When all three documents are `proposed`, obtain approval-body agreement, promote frontmatter to `status: agreed`, and record agreement date and approvers in the revision history. **From this point, they are effective norms.**

**Interim operation until agreed promotion**: AI input is limited to public-category data such as fictional cases and public information. Communicate this interim rule to members first.

## Step 2: Connect One Google Drive Area

Follow [Google Drive Operating Profile](google-drive-profile.md). The goal is to connect one existing knowledge boundary without reorganizing the entire drive.

1. Choose one shared drive or top-level folder and three to five active projects inside it.
2. Establish a read-only per-user OAuth path. Do not use a service account or domain-wide delegation.
3. Run the required two-account permission-differential test with harmless test documents. An account without access must receive neither the restricted content nor its source.
4. For each selected project, create a non-sensitive derived note from `knowledge/projects/_template.md`. Record the Drive source URL and newest source modification time.
5. Have project owners choose five recurring questions, then verify that every answer cites an original Drive document and states when it was modified or reviewed.

**Do not connect real confidential documents until the permission test passes and the applicable Layer 1 documents are `agreed`.** Category 3 and category 4 details remain in Drive. They must not be copied into `knowledge/`, prompts shared with unauthorized people, logs, PR bodies, or issues. Have AI run a confidentiality check before every commit; see `CLAUDE.md`.

The sample notes, `PJ-sample-equipment.md` and `ISSUE-0001.md`, show the derived-note structure. Delete them after the organization has three real derived project notes.

## Step 3: Put Daily Operation in Place

Distribute [user-guide.md](user-guide.md) to members. They only need the three Drive-first paths: ask through AI, read the cited Drive original, and edit the Drive original.

The main driver of adoption is that **the DRI uses it visibly every day**:

- In recurring meetings, demonstrate that AI answers from Drive with original links. This is the ask path.
- After meetings, record the decision in the approved Drive area. This is the write path.
- Once a week, check `source_modified_at` against the original and refresh stale derived notes.

If, after two weeks, asking AI is faster than asking people, adoption is working. If not, analyze with AI which part is missing: note granularity, freshness, or coverage.

## Step 4: Expand from Real Operation

After Layer 2 starts working, consider the following. See the expansion patterns in [architecture.md](architecture.md).

- **Skillization, Layer 3** — Convert dialogue patterns repeated three or more times into skills, such as catch-up summaries, meeting-note intake, and issue filing.
- **Drive change intake, Layer 4** — Incrementally refresh non-sensitive derived notes from the Drive change feed, with idempotency and stale-source handling.
- **Additional source adapter, Layer 4** — Add one only when a recurring workflow is blocked because its source is outside Drive. Notion, Slack, Chatwork, and SharePoint are not v0.1 core.
- **Audit and review, Layer 5** — Put the audit-log operation in the data classification matrix into full use.

**Use daily usage as the criterion for expansion.** Do not build a new layer on top of a layer that is not being used.

## Customization Points

| Area | Initial default | When to change |
|---|---|---|
| Size of approval body | Joined decision by three people | Organization size. The minimum useful shape is one business owner plus one builder. |
| Data-category granularity | Four categories | Regulated industries may split category 4 further. Even in non-regulated industries, keep the four-category frame. |
| Execution-environment inventory | E1 through E3 plus E1.5 | Put every AI service actually used by the organization into the matrix. |
| Drive source boundary | One shared drive or top-level folder | Expand only after the first five recurring questions work and permissions are verified. |
| Note types under `knowledge/` | projects / issues | Add customer, case, or meeting-note types together with Layer 4 intake design. |
| Owner-flag notation | `(requires <role name>)` | Real names or role names are both acceptable. Prefer role names if the repository may be shared externally. |
| Merge authority | DRI only | If more people receive write permission, move to PR operation with required review. |

## Common Pitfalls from Real Operation

- **Building tools before norms** — This is the most common failure. If norms are created only after a data incident, trust is harder to recover.
- **Starting all five layers side by side** — Everything becomes half-built and unused. Protect the narrow start.
- **Leaving everything to AI without human reading** — Humans must perform final confirmation of norm documents, especially compliance norms. AI is a drafting and research aid.
- **Letting notes become stale** — If people believe "AI's answer is old" even once, usage drops. Make weekly `last_reviewed` checks a DRI habit.
- **Treating folder placement as authorization** — A folder name or project mapping does not grant access. Test the current user's effective Drive permission with two accounts.
- **Adding another connector before repeat use** — If users cannot name a recurring question, source breadth is not the bottleneck.

## Revision History

| Date | Version | Author | Change |
|---|---|---|---|
| 2026-08-13 | v1.0 | HideTsug | Initial version |
| 2026-08-17 | v1.1 | HideTsug | Replaced the repository-only Layer 2 setup with the Google Drive-first v0.1 path |
