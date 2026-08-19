---
status: draft
version: "0.3"
owner: (requires implementation DRI)
summary: Template for the permission matrix across four data categories and AI execution environments. This is the top-level rule for which data may be given to which AI environment. Fill it after inventorying the adopting organization's real environments.
---

Japanese version: [docs/ja/layer1/データ分類マトリクス.md](../docs/ja/layer1/データ分類マトリクス.md)

# Data Classification Matrix (Template)

> The top-level rule for which data may be given to AI in which execution environment. The data categories in this matrix also work directly as **execution environment selection criteria**.
>
> Filling policy: Keep the four data categories. Replace and enrich the examples with the adopting organization's real data. Classify every AI service actually used by the organization into E1, E1.5, E2, or E3.

- Drafted: [Date] / [Drafter]
- Agreement target: [approval body, for example a joined decision by representative + implementation DRI + system owner]
- Effective date: when frontmatter is promoted to `status: agreed`. Until then, interim operation allows only public-category data to be entered into AI.

## Four Data Categories

| Category | Definition | Examples to customize for the organization |
|---|---|---|
| **1. Public** | Data that may be seen by anyone without issue | Public information, industry articles, public laws and regulations, fictional or dummy cases, training cases, and statements already published by the person |
| **2. Internal** | Internal organizational data that does not identify customers or vendors. Split into **personal-origin** data, such as the contributor's own thinking or reflection with no unique information about others, and **organizational internal** data, such as meeting notes, SOPs, and work templates | Reflection and career-view notes; meeting notes with personal names replaced by initials; work procedure documents |
| **3. Customer/vendor-identifying** | Data that identifies or could lead to identification of a customer or vendor | Real personal names, company names, financial figures, communication history such as email, customer analysis notes, and non-public business themes such as HR, partnerships, M&A, and unpublished financials |
| **4. Regulated** | Data with special legal management duties | Statutory identifiers whose permitted purposes and recipients are restricted by law and the documents carrying them, identity-verification documents, sensitive personal information, litigation materials, and (requires qualified professional: identify the laws that apply in the organization's own jurisdiction and add its legally required documents. Example, Japanese jurisdiction: individual numbers and Individual Number Act-related documents) |

Classification principle: **When in doubt, choose the stricter category**. Even a personal thinking note should be classified by its actual content if it contains unique information about others, such as customer names, employee names, or vendor names. Customer analysis becomes category 3; HR notes are handled as category 3 non-public themes.

## Execution Environments

> Classify every environment used by the organization. Each row is defined by **where the AI process executes and where its files persist**, not by product name. The following defaults represent a common setup.

| Environment | Defining property | Data sovereignty |
|---|---|---|
| **E1: Local or organization-managed** | The AI process runs on hardware the organization provisions — a member's machine, an organization-managed server, or a runner inside the organization's network — and checkouts, working files, and secrets persist there. For production promotion, tenant-internal inference such as Bedrock or Vertex AI is the main path. Example: an agentic AI CLI running locally. | Organization-managed |
| **E1.5: Organization-tenant SaaS** | Data lives in a SaaS tenant contracted by the organization. AI reference is allowed only through per-user OAuth, inheriting the user's own permissions. Example: Google Workspace, an organization-contracted cloud database. | Organization-managed through tenant contract |
| **E2: Vendor-managed cloud AI under commercial contract** | The process executes on vendor-provisioned infrastructure and session files persist there. Even with no-training terms, the execution environment and file storage are outside organization management. Example: an agentic AI's default web or cloud session. | Outside organization management |
| **E3: General cloud AI** | Free chat AI services, personal accounts, and similar environments where inputs may be used for training. | Outside organization management |

**Classify by configured deployment, not by product name.** The same product can belong to different rows depending on how the organization deployed it, so confirm the deployment actually enabled before filing it. When execution and file residency move onto organization-controlled infrastructure while prompts, responses, and tool results are still sent to the vendor for inference, the two axes are assessed separately: the table above covers execution and file residency, and the inference path is assessed on the R axis in "E1.5 AI Reference Conditions" below.

Example of why the property decides the row, current as of 2026-08 — verify the vendor's current terms rather than relying on this paragraph: Claude Code cloud sessions run on vendor-provisioned infrastructure by default, which is E2. Organizations on Team or Enterprise plans can enable self-hosted environments so that sessions run on runners inside their own network, with repository checkouts, build artifacts, and secrets staying on infrastructure they provision — that moves the execution and file-residency axis to E1. The conversation is still sent to the vendor for inference either way, so the inference path remains a separate R-axis question.

## GitHub Repositories as a Storage Location

GitHub repositories, including this repository, are not AI execution environments; they are **storage locations on cloud infrastructure outside organization management**. Their data sovereignty is the same "outside organization management" as E2/E3, but **the E2/E3 columns of the input permission matrix below do not apply to them** — that matrix governs what may be given to AI, while this section governs what may be committed. Commit permission is as follows:

| Data category | Committing to GitHub |
|---|---|
| 1. Public | Allowed |
| 2. Internal | Allowed, but only after processing such as replacing personal names with initials or role titles (`knowledge/README.md`) |
| 3. Customer/vendor-identifying | **Prohibited** |
| 4. Regulated | **Prohibited** |

In every category, the "Commit Prohibitions" in `docs/governance/operating-rules.md` must also be satisfied. Note that the storage location (where data lives) and the inference path (which AI may read it) are separate axes — for the latter, see the R axis under "E1.5 AI Reference Conditions" below.

## Input Permission Matrix: Initial Defaults

> The defaults are intentionally conservative. Loosening them requires operational evidence and renewed agreement by the approval body.

| Data category | E1: Local or organization-managed | E1.5: Organization-tenant SaaS | E2: Vendor-managed cloud AI | E3: General cloud AI | Approver |
|---|---|---|---|---|---|
| 1. Public | ◎ | ◎ | ◎ | ◎ | Not required |
| 2. Internal, personal-origin | ◎ | ◎ | ✗ Non-public reflection is not allowed. Already published statements are category 1. | ✗ Same as left | The person, or implementation DRI if uncertain |
| 2. Internal, organizational internal | ○ After processing such as replacing personal names with initials | ○ Storage and reference both allowed | ✗ | ✗ | Implementation DRI |
| 3. Customer/vendor-identifying | △ Only when all operating conditions below are met | Storage = ◎ as formalization of existing work; AI reference = △ under the E1.5 AI-reference conditions below | ✗ | ✗ | Joined decision by approval body |
| 4. Regulated | ✗ Prohibited for now | Storage = follow statutory official storage; AI reference = ✗ | ✗ | ✗ | None. Unlocking requires revising this matrix, joined approval, and external legal confirmation. |

Legend: ◎ = freely allowed / ○ = conditionally allowed / △ = only after specified processing and prior approval / ✗ = prohibited

This matrix governs **what may be given to AI**. Commit permission for GitHub repositories follows the table in "GitHub Repositories as a Storage Location" above; do not reuse the E2/E3 columns for that purpose.

### Operating Conditions for Category 3 × E1

Input is allowed only when **all** of the following are satisfied:

1. The approval body has pre-confirmed that the E1 environment satisfies organization-managed requirements, such as local execution or inference inside an organizational tenant.
2. Prior joined approval has been obtained for each data type. Chat or email approval is acceptable if it is retained.
3. Required processing is applied: masking real names and proper nouns, converting financial figures to ranges or fictional replacements, and replacing personal names with initials. The required processing level is specified at approval time.
4. The input is recorded in the audit log below.

### E1.5 AI Reference Conditions: Phased Introduction

Treat the **storage environment axis** and the **inference path axis** separately. Define what inference paths are allowed when storage remains inside the organizational tenant.

| Inference path | Content | Category 3 data |
|---|---|---|
| R1: Inference inside organizational tenant | Vertex AI, Bedrock, or similar tenant-internal processing, including domestic-region options where applicable | ○ Main production path |
| R2: Vendor commercial API | Commercial API path with no-training terms and DPA | △ Only if all activation conditions are satisfied |
| R3: Path where data may be used for training | General cloud AI or consumer settings with training opt-in | ✗ Always prohibited |

Activation conditions for R2, initial defaults. Do not begin confidential reference until all are satisfied in addition to approval-body agreement:

1. AI reading of the confidential layer must use only per-user OAuth, inheriting the person's own permissions. Service accounts and domain-wide delegation are prohibited.
2. No-training contractual protection and a DPA have been confirmed in the vendor terms and commercial terms.
3. Retention period and controls are understood. Confirm retention settings for API and connector data. **Shared-chat features and consumer settings with training opt-in are prohibited.**
4. References are recorded in audit logs. Standard audit logs of the storage-side SaaS are acceptable.
5. **Classification inheritance for AI output**: If output contains category 3 data, treat the output as category 3. Do not copy it into GitHub, including PR bodies and issues, shared links, or shared chat.
6. **Customer explanation and agreement policy for AI use has been finalized**. (requires executive owner — blocker before activation. Follow industry guidelines if they exist.)

## Audit Log

- **Storage location**: Create a dedicated "data-input approval log" inside organization-managed cloud storage. (requires executive owner: specify the storage tenant)
- Do not store this log in this GitHub repository. Decision: the log itself may contain customer references. Reason: that would move category 3 data into cloud storage outside organization management.
- **Required fields**: date and time / submitter / environment (E1/E1.5/E2/E3) / data category / target overview using case IDs rather than real names / applied processing / approver / approval method
- **Events to record**: all △ category input. For ○ category input, record only entries approved by the implementation DRI; person-only judgments are out of scope.
- **Read permissions**: approval body and operators approved by the approval body

## Revision History

| Date | Version | Author | Change |
|---|---|---|---|
| [Date] | v0.1 | [Drafter] | Drafted from template |
| 2026-08-18 | v0.2 | upstream template | Defined the execution-environment rows by execution and file-residency property instead of product name, and separated them from the inference-path R axis |
| 2026-08-19 | v0.3 | upstream template | Restated the category 4 examples as jurisdiction-independent, with the Japanese items kept as a labelled example |
