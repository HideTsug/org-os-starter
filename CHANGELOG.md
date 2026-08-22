# Changelog

Japanese version: [docs/ja/CHANGELOG.md](docs/ja/CHANGELOG.md)

All notable changes to this repository are documented in this file, so that an adopting organization following the update strategy in [README.en.md](README.en.md) can judge upstream differences from inside its own copy. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions correspond to the GitHub release tags of this repository.

## [Unreleased]

Changes on `main` since v1.0.0.

### Added

- `CONTRIBUTING.md` with the English canon / Japanese mirror invariants and the pre-pull-request checklist (#17)
- An "editing this repository" branch at the top of `AGENTS.md`, so agents that load it automatically are not misrouted into the adoption flow (#18)
- `examples/demo-company/` — a filled fictional-company demo that can be tried right after cloning
- English canon: canonical documents translated to English with Japanese mirrors under `docs/ja/`, and all file and directory names renamed to English
- `docs/ai-agent-guide.md` — a pre-clone briefing for AI agents, loadable from a single raw URL, with a Japanese mirror (#26)
- `scripts/validate.py` — mechanical checks for relative links, wikilinks, frontmatter `status`, and bare placeholders (#28)
- `ADOPTERS.md` — an opt-in list of organizations running this convention, linked from both READMEs (#22)
- `CHANGELOG.md` with a Japanese mirror, and the current version stated at the top of both READMEs (#27)
- A user-guide FAQ entry on what a member should do when an AI answer carries no source link or contradicts the original (#29)

### Changed

- Adopted the Google Drive-first v0.1 operating profile: Drive keeps human-authored originals and ACLs, the repository keeps norms and non-sensitive derived state (ADR-0001) (#9)
- Enforced `access_policy: source_acl` on derived notes and extended the two-account permission-differential test to derived state (#10)
- Defined execution-environment rows in the data classification matrix by property instead of product name (#11)
- Made the agent-facing surface vendor-neutral (#12)
- Made AI-facing instructions verifiable and environment-independent (#23)
- Separated GitHub from the E2/E3 execution environments as its own storage rule, resolving the self-contradiction about committing category-2 "internal" notes (#3)
- Split the setup path into "Use this template" followed by cloning the organization's own private repository (#2)
- Added the effort estimates of the Japanese mirror to the Step 0/1/3 headings of the English setup guide (#33)
- Linked the "Company OS as Code" explainer page from both READMEs (#34)
- Added a national AI-governance guidance reference to the compliance norms of the Layer 1 `ORG-CLAUDE.md` template (#39)
- Prohibited unattended execution of irreversible operations by AI agents in `layer1/prohibited-uses.md` (#40)
- Made keeping this changelog current a checklist item in `CONTRIBUTING.md`, so upstream changes stop going unrecorded (#45)

### Fixed

- README file maps and reading-order tables matched to the actual repository tree (#4, #16)
- Translation polish and `docs/ja/` cross-reference fixes (#8)
- Demo README: the clone command's placeholder URL replaced with the repository URL, so it can be pasted and run (#35)

## [1.0.0] - 2026-08-13

Initial public release. A knowledge-foundation starter kit, MIT-licensed free OSS, for helping an organization become AI-native — the organizational counterpart of the personal [pm-os-starter](https://github.com/HideTsug/pm-os-starter).

### Added

- The 5-layer architecture: norms and SSoT separation → knowledge → roles and skills → integration → governance, starting from Layer 1
- v1 core: the three norm templates (organizational CLAUDE, data classification matrix, prohibited-uses list), the `knowledge/` structure, the setup and user guides, the operating-rules template, and the ADR scaffold
- The "Use this template" flow: create the organization's own private repository and start adoption with an agentic AI such as Claude Code, with only three decisions made by humans first — the implementation DRI, the approval body, and the first narrow use case
- `AGENTS.md` as the AI-agent entry point, the consent-based star/follow support confirmation, and `.gitignore`

[Unreleased]: https://github.com/HideTsug/org-os-starter/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/HideTsug/org-os-starter/releases/tag/v1.0.0
