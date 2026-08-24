---
status: draft
version: "0.4"
owner: (requires implementation DRI)
summary: Template for explicitly prohibited AI uses inside the organization and the response to violations. It pairs with the data classification matrix.
relates_to:
  - "[[data-classification-matrix]]"
---

Japanese version: [docs/ja/layer1/禁止用途リスト.md](../docs/ja/layer1/禁止用途リスト.md)

# Prohibited Uses (Template)

> An explicit list of what AI **must not** be used for inside the organization. [[data-classification-matrix]] defines what data may be given to AI; this document defines what AI must not be made to do.
>
> Filling policy: Items 1 through 3 should be customized to match professional responsibility in the organization's industry. Regulated industries such as licensed professions, healthcare, and finance must fill them. Items 4 through 10 can usually be used almost as-is across industries.

- Drafted: [Date] / [Drafter]
- Agreement target: [approval body]
- Scope: all AI use inside the organization

## Absolutely Prohibited in Any Environment

1. **Direct AI generation of deliverables involving professional responsibility, followed by submission or sending without review by a qualified professional or responsible owner.** AI output is always a draft. Do not submit deliverables to customers or public authorities without final human review. Reference examples: diagnosis-related documents in healthcare, customer-facing advice in finance, and legally required documents in licensed professions.
2. **Providing specialized advice outside the contract scope to customers as-is from AI output.** AI may be used for preliminary research on out-of-scope topics, but advice to customers must pass through human judgment inside the contract and responsibility scope.
3. **Automating statutorily exclusive acts, or judgments reserved by law to qualified professionals, as direct AI responses.** Do not connect AI directly to customers to answer such judgments automatically. The automatic-response scope of customer-facing AI must be designed separately by the approval body. (requires qualified professional: identify applicable work under the organization's industry law)
4. **Entering regulated data, category 4 in [[data-classification-matrix]], into AI.** This includes statutory identifiers restricted by law, identity-verification documents, sensitive personal information, and litigation materials. Which items belong here is decided by the laws of the organization's own jurisdiction (example, Japanese jurisdiction: individual numbers under the Individual Number Act).
5. **Unreviewed automatic execution of external communication under the representative or organization name.** This includes sending email, posting to social media, and sending customer-facing documents. Generation is allowed; sending and publication require human confirmation.
6. **Uses that avoid or hollow out conflict-of-interest checks**, such as combining information from multiple customers to generate advice favorable to one side.
7. **Unattended automatic execution of irreversible operations by an AI agent.** This includes bulk deletion of data, execution of payments or orders, and changes to production-system configuration. Generation and proposals are allowed; execution requires human confirmation — the internal counterpart of item 5's rule for external communication. (requires implementation DRI: identify which operations count as irreversible in the organization)

## Environment-Conditioned Prohibitions: Data Export

8. **Entering category 3 customer/vendor-identifying data into environments outside organization management**. Input into vendor-managed cloud AI or general cloud AI, and committing to GitHub, are prohibited regardless of anonymization. This restates the category-3 row ✗ cells and "GitHub Repositories as a Storage Location" in [[data-classification-matrix]]. Category 4 is prohibited in the same way.
9. **Allowing input data to be used for training.** Do not use a service configuration for organizational work if its terms or settings allow input data to be used for training.
10. **Adding a new AI service, or an extension to an approved environment, without approval.** Any work use of a service not classified into E1 through E3 in the matrix requires prior classification by the implementation DRI. The same applies to an extension installed into an already-approved environment — an MCP server, an agent plugin, or a connector — because it changes that environment's effective data boundary without changing which row it occupies. See "Extensions Added to an Approved Environment" in [[data-classification-matrix]].

## Response to Violations

1. The discoverer immediately stops the use and reports it to the implementation DRI, including self-reporting. **Do not disadvantage the reporter.**
2. The approval body assesses impact, including what went where, whether recovery is possible, and customer or legal impact, then decides the response.
3. Record the incident as a violation in the audit log, using the same storage location as the audit log in [[data-classification-matrix]].
4. **If [3] or more non-standard data-handling incidents occur, suspend the relevant AI use and redefine data-handling rules through the approval body.**

## Revision

- Adding, loosening, or deleting items in this list requires a joined decision by the approval body and renewed agreement on `status: agreed`.
- If a use case is ambiguous, **do not execute it**. Confirm with the implementation DRI first.

## Revision History

| Date | Version | Author | Change |
|---|---|---|---|
| [Date] | v0.1 | [Drafter] | Drafted from template |
| 2026-08-19 | v0.2 | upstream template | Restated item 4 as jurisdiction-independent, with the Japanese items kept as a labelled example |
| 2026-08-22 | v0.3 | upstream template | Added item 7 prohibiting unattended execution of irreversible operations by AI agents, and renumbered the data-export items to 8–10 |
| 2026-08-25 | v0.4 | upstream template | Extended item 10 to cover extensions added to an already-approved environment, such as MCP servers, agent plugins, and connectors |
