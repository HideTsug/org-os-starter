---
doc_type: reference
version: "1.1"
summary: Overview of the Org-OS five-layer architecture and its Google Drive-first Layer 2 topology. Layer 3 through Layer 5 concepts exist only in this document until real content is ready.
---

Japanese version: [docs/ja/docs/アーキテクチャ.md](ja/docs/アーキテクチャ.md)

# Org-OS Architecture Overview

> A blueprint that treats an organization's AI foundation as five layers. See `layer1/` for the individual norm templates.

## Design Approach

This architecture maps an AI work foundation proven in personal operations to an organizational scale. The personal foundation combined Obsidian and Claude Code to operate knowledge, norms, and agents together. The personal starter is [pm-os-starter](https://github.com/HideTsug/pm-os-starter).

How principles proven in personal work map to organizations:

| Principle proven in personal work | Organizational application |
|---|---|
| Structured knowledge written for AI-first use | Structured notes for customers, projects, cases, and work templates (Layer 2) |
| Separation of norms and metadata (`CLAUDE.md` / frontmatter) | Machine-readable organizational policy and compliance norms (Layer 1) |
| Role-triggered agents through skills | Skillization of AI for each work domain (Layer 3) |
| Working memory across sessions | Handoffs between owners through each project's current issues and recent decisions (Layer 2) |
| Collaboration between worker AI and reviewer AI | Separation of worker AI and audit AI, with quality gates (Layer 5) |
| Event-driven automation through hooks | Automated actions triggered by monthly cycles, deadlines, contract renewals, and similar events (Layer 4) |
| Searchability and idempotency through indexes and intake guards | A foundation for handling many customers and large data volumes (Layer 2) |

## Five Layers

```text
Layer 5  Governance          Audit logs / reviews / compliance verification
Layer 4  Integration         Core systems / SaaS such as accounting and CRM / customer touchpoints
Layer 3  Role and Skill      Domain-specific AI, such as accounting AI, HR AI, sales-support AI, and reviewer AI
Layer 2  Knowledge Base      Structured notes for project state / issues / decisions / work templates
Layer 1  Norms and SSoT      ORG-CLAUDE.md / data classification matrix / prohibited uses
```

### Layer Responsibilities

**Layer 1: Norms and SSoT** — The top-level rules followed by all AI agents and humans inside the organization. It consists of three documents:

1. `ORG-CLAUDE.md` — organizational policy, decision priorities, compliance norms, and escalation paths
2. `data-classification-matrix.md` — which data may be given to which AI execution environment; this is also the basis for choosing environments
3. `prohibited-uses.md` — what AI must not be used for; this pairs with the matrix

Norm agreement state is managed in machine-readable form through frontmatter `status`. Only `agreed` documents are authoritative.

**Layer 2: Knowledge Base** — A two-layer representation of the organization's current state. In v0.1, Google Drive is the only external source and remains the SSoT for human-authored originals and ACLs. `knowledge/` contains non-sensitive derived state optimized for AI:

- Google Drive — existing project originals, sharing, permissions, and revision history
- `knowledge/projects/` — derived project purpose, current state, recent decisions, next actions, source links, and freshness
- `knowledge/issues/` — non-sensitive derived issues linked to original evidence
- Three member paths: ask through AI, read the cited original in Drive, and edit the original in Drive

```text
Google Drive originals ──per-user OAuth──▶ AI answer with original links
        │                                      ▲
        └──non-sensitive derivation──▶ knowledge/
                                               ▲
layer1/ norms ─────────────────────────────────┘
```

See [Google Drive Operating Profile](google-drive-profile.md) and [ADR-0001](decisions/ADR-0001-google-drive-first-v0.1.md).

**Layer 3: Role and Skill** — AI agents triggered by work domain, packaged as skills. Write each one as a portable `SKILL.md` file, a format that Claude Code and several other agents can load, so the layer does not become tied to one vendor. Operationally observed skill candidates are the input to design. Do not write role definitions before candidates exist, because that creates unused structure. Convert repeated procedures into skills in order, such as project catch-up summaries, meeting-note intake, and issue filing.

**Layer 4: Integration** — Connections to core systems, SaaS, and customer touchpoints. Google Drive is the one v0.1 integration profile and is read-only through per-user OAuth. Incremental intake may update non-sensitive `knowledge/` derivations after classification checks. Additional SaaS connectors and automated write-back are future Layer 4 decisions, not v0.1 core.

**Layer 5: Governance** — Audit logs, reviewer AI, and compliance verification. Audit-log storage locations and required fields must be defined first in the Layer 1 norms, especially the data classification matrix.

## Start Order: Layer 1 → 2 → Layer 3 and Later

Starting from Layer 3 skills creates structure without norms or knowledge behind it. Once Layers 1 and 2 are working, repeated operations that should become skills become visible through real use.

Do not build the five layers side by side. The v0.1 goal is: select one Drive boundary, answer five recurring project questions with original links, and verify that Drive permissions remain effective. Expand only after the ask path repeats in real operation.

## Execution Environment Policy

The question "which AI execution environment should we use?" is not a tool preference. It is decided by data classification.

- The data categories in `layer1/data-classification-matrix.md` act directly as the environment selection criteria.
- For example, work involving customer-identifying data may be limited to organization-managed environments such as local execution or inference inside an organizational tenant, while tests using public or fictional data may be allowed in cloud tools. This distinction must be agreed first.
- Adding a new AI service for work use must go through classification in the matrix first.

## Expansion Patterns Outside v0.1 Core

The following patterns are intentionally outside the v0.1 core. Consider them after the Drive-first daily operation is working:

- **Additional source adapters** — Notion, Slack, Chatwork, SharePoint, and generic files. Add one only after a blocked recurring workflow is observed
- **Automated write-back** — creating, editing, or deleting Drive originals through AI. v0.1 is read-only
- **Expanded intake pipelines** — DLP-style derivation from Drive changes, followed by idempotent updates to `knowledge/`
- **Two-layer confidential storage** — storing real-name source material in organization-managed storage with access controls, while keeping only non-sensitive stubs in the repository
- **AI-to-AI communication channel** — members' AI agents exchange technical instructions and work reports through GitHub issues, while humans receive only plain-language summaries in chat
- **Project board** — cross-project visibility where issues are the SSoT, using GitHub Projects or similar tools
- **Autonomous construction loop** — a mechanism where AI advances construction of the toolset itself, paired with safeguards such as read-only access to normative documents and human gates

## Revision History

| Date | Version | Author | Change |
|---|---|---|---|
| 2026-08-13 | v1.0 | HideTsug | Initial version |
| 2026-08-17 | v1.1 | HideTsug | Made Google Drive the sole v0.1 external source and defined the two-layer Layer 2 topology |
