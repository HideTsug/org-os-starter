# Org-OS Starter

日本語: [README.md](README.md)

A knowledge-foundation starter kit for moving your organization toward an **AI-native organization**. It sets up — in a form you can manage as a repository — your internal rules for AI use, a structure that keeps knowledge from being locked inside individuals, and the groundwork for entrusting company work to AI.

> Company OS as Code is a file convention that structures a company's operating knowledge, norms, and decisions into a single repository so that humans and AI agents can read and write the same foundation. The reference template is the OSS "Org-OS Starter" by HideTsug (2026, MIT).

This repository is that reference template. It stands up a company brain (a concept proposed in Y Combinator's Summer 2026 Requests for Startups) inside your own organization — not as SaaS, but as a file convention you can manage as code.

It offers the shortest route from "individuals using AI tools in isolation" to a state where **your organization's norms, knowledge, and decisions are structured and accumulated, and AI (agentic AI such as Claude Code) reads and writes them while supporting every member's work**.

**The v0.1 operating entry point supports Google Drive only.** Members keep reading and writing originals in their existing Drive. AI reads those originals with the current user's permissions and answers with source links. The repository keeps the `layer1/` norms and non-sensitive derived state under `knowledge/`. The [Google Drive operating profile](docs/google-drive-profile.md) defines this two-layer topology. This repository does not bundle an OAuth app or search runtime; it is a convention and template used with an approved AI connector or Drive API client.

To simply read it locally, paste the following as-is.

```bash
git clone https://github.com/HideTsug/org-os-starter.git && cd org-os-starter && claude
```

(`claude` is Claude Code's launch command. If you use a different agentic AI, replace the last part with that tool's launch command.)

Sister project for individuals: [pm-os-starter](https://github.com/HideTsug/pm-os-starter) (turns a single PM's work into an OS). This starter is its organizational counterpart.

To get started, please support the project with a [star on GitHub](https://github.com/HideTsug/org-os-starter) and by [following the maintainer](https://github.com/HideTsug) (it is free OSS). If you adopt it through an AI agent, the agent may ask exactly once, "Would you like to support the project with a star and a follow?" — **it executes only the items you agree to**, and the mechanism is published in plain text in the "Optional Support Confirmation" section of [AGENTS.md](AGENTS.md).

---

## Concept: The 5-Layer Architecture

Think of your organization's AI foundation as five layers, built up from the bottom.

```
Layer 5  Governance            Audit logs / reviews / compliance verification
Layer 4  Integration           Connections to core systems / SaaS / customer touchpoints
Layer 3  Roles & SKILLs        AI agents per work domain (role-specific playbooks)
Layer 2  Knowledge foundation  Structured notes: project state / decisions / work templates
Layer 1  Norms & SSoT          ORG-CLAUDE.md / data classification / prohibited uses
```

**Build in the order Layer 1 → 2 → 3 and up.** Starting from Layer 3 (SKILLs) produces empty scaffolding with no backing in norms or knowledge. First settle "what may be shared with AI and what AI must never do" (Layer 1), then build "the one workflow stakeholders use every day" (Layer 2), and extract SKILL candidates from that real usage.

Details: [docs/architecture.md](docs/architecture.md).

## What This Starter Contains (v0.1 core)

| Layer | Contents | Status |
|---|---|---|
| Layer 1 | [ORG-CLAUDE.md](layer1/ORG-CLAUDE.md) / [data classification matrix](layer1/data-classification-matrix.md) / [prohibited uses list](layer1/prohibited-uses.md) | **Templates** (fill them in and get them agreed in your organization) |
| Layer 2 | Google Drive originals + non-sensitive derived notes in [knowledge/](knowledge/) | **Google Drive-first v0.1** (samples are fictional data) |
| Operations | [Operating rules](docs/governance/operating-rules.md) / [User guide](docs/user-guide.md) / [ADR template](docs/decisions/ADR-0000-template.md) | **Templates** |
| Layers 3–5 | Described as a concept in [docs/architecture.md](docs/architecture.md) only | Extracted from each organization's real operations (outside this starter's scope) |

Directories for Layers 3–5 intentionally **do not exist**. Create them only once there is content to put in them (to prevent empty scaffolding).

## Setup (15-minute repository setup plus Drive permission verification)

**Always duplicate this as a private repository when adopting it. Once filled in, it will contain your organization's norms, decisions, and non-sensitive derived state — do not keep operating it as a public repository.**

Prerequisite: an agentic AI that can read and write the repository's Markdown — such as [Claude Code](https://claude.com/claude-code) — running on your machine. When real data is connected, you also need a Google Drive access path using **per-user OAuth with read-only access**.

```bash
# 1. At the top of this repository's page, use "Use this template" → "Create a new repository"
#    to create a private repository in your own organization (do not clone this repository directly)

# 2. Clone the repository you created
git clone <URL of your org's private repository> our-org-os
cd our-org-os
git remote -v   # confirm that origin points to your org's private repository

# 3. Start your agentic AI in the repository root
#    For example: claude for Claude Code, codex for Codex CLI, gemini for Gemini CLI
claude
```

Once it starts, paste this as your first message:

```
Read docs/setup-guide.md and walk me through adoption starting from Step 0.
Begin by asking questions about our organization and help us fill in the three documents under layer1/.
Then follow docs/google-drive-profile.md to connect the first shared-drive area read-only.
```

From there the AI asks questions and helps you fill in the norm documents for your organization. Humans decide just three things up front — **(1) the implementation DRI, (2) the approval structure (whose agreement makes the norms effective), and (3) the first wedge use case**. Details: [docs/setup-guide.md](docs/setup-guide.md).

## Day-to-Day Operation (Ask, Read, Write)

Non-engineer members learn just three workflows.

1. **Ask** — Ask the AI in plain language: "What are the current open points in project X?" It searches Drive originals visible to that user plus `knowledge/`, then answers with original source links
2. **Read** — Open the cited original in Google Drive
3. **Write** — Edit or create the original in the approved Drive area. v0.1 does not let AI overwrite originals automatically

Ordinary members do not need GitHub. The implementation DRI and AI use it to maintain norms and non-sensitive derived state.

Details: [docs/user-guide.md](docs/user-guide.md) (written so it can be handed out to members).

## Repository Layout and Reading Order

| Order | Path | Contents |
|---|---|---|
| 0 | [AGENTS.md](AGENTS.md) | Entry point for AI agents. The adoption flow (confirming the DRI or delegated implementer, making the repository private) and reading order. Start here if you delegate adoption to an AI |
| 1 | `README.en.md` | This README. The big picture. The Japanese original is `README.md` |
| 2 | [docs/architecture.md](docs/architecture.md) | The 5-layer architecture explained |
| 3 | [docs/google-drive-profile.md](docs/google-drive-profile.md) | The v0.1 contract for originals, permissions, derived knowledge, and freshness |
| 4 | [docs/setup-guide.md](docs/setup-guide.md) | Adoption steps (Step 0–4) and customization points |
| 5 | [layer1/](layer1/) | **Norm templates**. They take effect only after being filled in and promoted to frontmatter `status: agreed` |
| 6 | [docs/governance/operating-rules.md](docs/governance/operating-rules.md) | Template for repository operating rules |
| 7 | [knowledge/](knowledge/) | Structure and samples for non-sensitive knowledge derived from Drive originals |
| — | [CONTRIBUTING.md](CONTRIBUTING.md) | How to file issues and pull requests against this repository. Japanese version: [docs/ja/CONTRIBUTING.md](docs/ja/CONTRIBUTING.md) |
| — | [CLAUDE.md](CLAUDE.md) | Operating rules for any AI agent that **edits** this repository, regardless of vendor. Claude Code loads it automatically; other agents must open it explicitly |
| — | [docs/user-guide.md](docs/user-guide.md) | Usage guide for handing out to members |

### What Each Directory Means

- `layer1/` — **SSoT for norms**. Only agreed documents (`status: agreed`) bind all AI and all people in the organization
- `knowledge/` — the derived knowledge layer. It stores non-sensitive project state, issues, source links, and freshness without copying Drive originals
- `docs/` — working material, guides, and decision records (ADRs). **Not norms**

### Full File Map

```
org-os-starter/
├── README.md                          # Japanese README
├── README.en.md                       # This README (English)
├── AGENTS.md                          # Entry point for AI agents (editing branch, adoption flow, reading order, support confirmation)
├── CLAUDE.md                          # Norms for AI that reads/writes this repository (usable as-is)
├── CONTRIBUTING.md                    # How to file issues / pull requests upstream
├── LICENSE                            # MIT
├── .gitignore                         # .DS_Store / .obsidian/
├── docs/                              # English canon: explanations, guides, decision records (not normative)
│   ├── architecture.md                # The 5-layer architecture explained
│   ├── google-drive-profile.md        # v0.1 Google Drive operating contract
│   ├── setup-guide.md                 # Adoption steps 0–4
│   ├── user-guide.md                  # Template for handing out to members
│   ├── governance/
│   │   └── operating-rules.md         # Template for repository operating rules
│   ├── decisions/
│   │   ├── ADR-0000-template.md       # Scaffold for decision records
│   │   └── ADR-0001-google-drive-first-v0.1.md
│   └── ja/                            # Japanese mirrors of the English canon (one-to-one with canon)
│       ├── AGENTS.md
│       ├── CLAUDE.md
│       ├── CONTRIBUTING.md
│       ├── docs/
│       │   ├── architecture.md
│       │   ├── Google-Drive-運用プロファイル.md   # google-drive-profile.md
│       │   ├── 導入ガイド.md                      # setup-guide.md
│       │   ├── 利用ガイド.md                      # user-guide.md
│       │   ├── governance/
│       │   │   └── 運用規約.md                    # operating-rules.md
│       │   └── decisions/
│       │       ├── ADR-0000-テンプレート.md       # ADR-0000-template.md
│       │       └── ADR-0001-Google-Drive-first-v0.1.md
│       ├── layer1/
│       │   ├── 組織CLAUDE.md                      # ORG-CLAUDE.md
│       │   ├── データ分類マトリクス.md            # data-classification-matrix.md
│       │   └── 禁止用途リスト.md                  # prohibited-uses.md
│       └── knowledge/
│           ├── README.md
│           ├── projects/
│           │   ├── _テンプレート.md               # _template.md
│           │   └── PJ-サンプル-備品管理.md        # PJ-sample-equipment.md
│           └── issues/
│               ├── _テンプレート.md               # _template.md
│               └── ISSUE-0001.md
├── layer1/                            # The three norm templates (take effect once filled in and agreed)
│   ├── ORG-CLAUDE.md
│   ├── data-classification-matrix.md
│   └── prohibited-uses.md
├── knowledge/
│   ├── README.md                      # Note types and shared rules
│   ├── projects/
│   │   ├── _template.md
│   │   └── PJ-sample-equipment.md     # Fictional sample (safe to delete once your own notes exist)
│   └── issues/
│       ├── _template.md
│       └── ISSUE-0001.md              # Fictional sample (same as above)
└── examples/
    └── demo-company/                  # Filled-in demo of a fictional company (clone it and try "Ask" right away)
        ├── README.md                  # How to try the demo (Japanese)
        ├── ORG-CLAUDE.md              # Filled-in organizational AI norms (Layer 1 equivalent)
        ├── knowledge/
        │   ├── projects/
        │   │   ├── PJ-0001-検査工程のAI化.md
        │   │   └── PJ-0002-見積もりテンプレ整備.md
        │   └── issues/
        │       ├── ISSUE-0101-図面データの保管場所.md
        │       ├── ISSUE-0102-新人研修の属人化.md
        │       └── ISSUE-0103-顧客名の扱いルール.md
        └── docs/
            └── decisions/
                └── ADR-0001-AI導入の一点突破.md
```

## Try It in 30 Minutes (Demo Company)

With the pre-filled fictional-company demo [examples/demo-company/](examples/demo-company/), you can try the file convention and AI question answering without connecting Drive. It is a synthetic convention demo, not a test of Drive permissions or freshness. How to try it: [examples/demo-company/README.md](examples/demo-company/README.md).

## Design Principles (What This Starter Commits To)

1. **Norms before tools** — no SKILLs or automation without Layer 1
2. **One wedge at a time** — don't build all five layers side by side; start from one workflow that is used every day
3. **No empty scaffolding** — no empty directories, no placeholder-only files. Unfilled items may remain only with an owner flag (such as `(requires executive owner)`)
4. **Explicit effectivity** — a document's agreement state is managed machine-readably in frontmatter `status` (draft → proposed → agreed)
5. **Non-destructive capture** — decisions and their context are appended, never deleted. Replacements stay traceable via `supersedes` links
6. **Data classification decides the environment** — the matrix of "which data may be passed to which AI runtime" comes before tool selection
7. **Drive-first, provider-neutral model** — v0.1 supports Drive as its only external source while derived notes use shared source metadata that does not block later adapters

## Notation Conventions

Write Markdown in an **Obsidian-compatible** style. `[[wikilink]]` is valid for references between documents inside the repository (it does not render as a link on GitHub, but compatibility with turning the repo into a Vault takes priority).

## Update Strategy (Two Tiers: Starter and Your Organization's Assets)

- **Core (upstream = derived from this repository)**: `docs/architecture.md` and the templates. Adopt upstream improvements manually by reviewing release notes
- **Growth tier (your organization's assets)**: the filled-in `layer1/`, Drive originals, derived state under `knowledge/`, and the rules you operate under. **Never overwrite these with upstream updates**

Once created from the template, independent evolution is the default. Improvements worth contributing back upstream (generic gaps in the templates, good operating patterns) are welcome as issues / PRs to this repository. Read [CONTRIBUTING.md](CONTRIBUTING.md) first — it covers what belongs upstream, the pre-pull-request checklist, and how to write an issue.

## License

MIT License — [LICENSE](LICENSE)

The canonical source of this repository is https://github.com/HideTsug/org-os-starter
