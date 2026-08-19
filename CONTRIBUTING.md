# Contributing to Org-OS Starter

Japanese version: [docs/ja/CONTRIBUTING.md](docs/ja/CONTRIBUTING.md)

Thank you for considering a contribution. This document is for people and AI agents contributing **to this upstream repository**. It is not a template for the adopting organization — the template for an adopting organization's own repository rules is [docs/governance/operating-rules.md](docs/governance/operating-rules.md).

This repository is a Markdown-only template repository. There is no build step, no dependency install, and no test suite. The quality gates are the review checklist below, and they are the whole of what has to pass.

## What Belongs Upstream

This starter is meant to be copied through "Use this template" and then to evolve independently inside each organization. Only improvements that help **every** adopter belong here.

**Welcome:**

- Generic gaps in the templates under `layer1/`, `knowledge/`, and `docs/` — a norm that is missing, ambiguous, or self-contradictory
- Operating patterns that proved useful in real adoption and generalize beyond one organization
- Corrections: broken links, stale file maps, translation errors, contradictions between documents
- Reports that the adoption flow in `docs/setup-guide.md` breaks down at a specific step

**Not welcome here:**

- Your organization's filled-in `layer1/` content, real project notes, or real decisions. Those stay in your own private repository
- Real customer, vendor, or personnel information of any kind, including inside examples (see the fictional-data rule below)
- New directories for Layers 3 through 5. Keeping them absent until real content exists is a design principle, not an omission (see [README.md](README.md), "Design Principles")

If you are unsure whether something generalizes, open an issue before writing the change.

## Before You Open a Pull Request

Check every item. These are the invariants that are easy to break without noticing, because nothing in CI enforces them.

- [ ] **English canon and Japanese mirror moved together.** The English documents are the canon; `docs/ja/` holds their Japanese mirrors. Changing one side only leaves the repository inconsistent. The mapping is: root `AGENTS.md` / `CLAUDE.md` / `CONTRIBUTING.md` ↔ `docs/ja/`, `docs/**` ↔ `docs/ja/docs/**`, `layer1/**` ↔ `docs/ja/layer1/**`, `knowledge/**` ↔ `docs/ja/knowledge/**`, and `README.md` (Japanese) ↔ `README.en.md` (English). `examples/` is outside this mapping: it is not mirrored, and only its English summary is kept in step with the English canon. Which language each side's references point to is the next item
- [ ] **References point to the document in the reader's language.** Inside `docs/ja/`, a reference points to the Japanese counterpart whenever one exists. Everywhere else it points to the English canon — including the first entry of the reading order in `AGENTS.md` (`README.en.md`, not the Japanese `README.md`) and the path column of the reading-order table and the file map in **both** READMEs, which name the same English canon paths row for row — the one exception is the reading-order row for the README itself, where each names its own file. A Japanese mirror may be named beside them as an extra pointer, never as the row's path. The rule is in [CLAUDE.md](CLAUDE.md), "Upstream-Only Rules". The check below lists every link that leaves `docs/ja/`; each remaining hit must be an intended exception — an `English version:` header link, the Japanese `README.md`, or a file with no Japanese counterpart such as `LICENSE`

```bash
python3 - <<'PY'
import re, os, subprocess
out = subprocess.run(['git', 'ls-files', '-z', 'docs/ja/*.md'], capture_output=True, text=True).stdout
for f in [f for f in out.split('\0') if f]:
    for link in re.findall(r'\]\(([^)#:]+?)(?:#[^)]*)?\)', open(f, encoding='utf-8').read()):
        target = os.path.normpath(os.path.join(os.path.dirname(f), link))
        if not target.startswith('docs/ja/'):
            print('leaves the Japanese mirror:', f, '->', target)
PY
```

- [ ] **Samples use fictional data only.** No real customer or vendor names, real financial figures, real communication logs, or internal non-public information, and no API keys, tokens, or secrets. `examples/demo-company/` is entirely fictional by design — see [CLAUDE.md](CLAUDE.md), "Commit Prohibitions"
- [ ] **No Layer 3–5 directories, no empty directories, no placeholder-only files.** Unfilled items carry an owner flag such as `(requires executive owner)`, never a bare `(TODO)` — see [CLAUDE.md](CLAUDE.md), "Structure Rules". `python3 scripts/validate.py` detects bare placeholders mechanically
- [ ] **Every relative link resolves.** If you added, moved, or renamed a file, the file maps and reading-order tables in `README.md` and `README.en.md` need the same change. Run `python3 scripts/validate.py` from the repository root: it verifies that **every** relative link resolves — directories and non-Markdown targets such as `LICENSE` included, not only `.md` files — and also checks `[[wikilink]]` resolution, frontmatter `status` values, and bare placeholders, printing the number of files checked and every violation. Exit code 0 means no violations. Paste its output in the pull request. Where `python3` is not available, the script cannot run; the snippet below is a reference implementation of the link portion — reproduce equivalent output with node, ripgrep plus a shell loop, or direct inspection of the files you changed

```bash
python3 - <<'PY'
import re, os, subprocess, sys
out = subprocess.run(['git', 'ls-files', '-z', '*.md'], capture_output=True, text=True).stdout
files = [f for f in out.split('\0') if f]
bad = []
for f in files:
    base = os.path.dirname(f)
    for link in re.findall(r'\]\(([^)#:]+?)(?:#[^)]*)?\)', open(f, encoding='utf-8').read()):
        if not os.path.exists(os.path.normpath(os.path.join(base, link))):
            bad.append((f, link))
for b in bad:
    print('broken link:', b[0], '->', b[1])
print('checked', len(files), 'files;', len(bad), 'broken')
sys.exit(1 if bad else 0)
PY
```

- [ ] **Notes under `knowledge/` match their template's frontmatter contract.** A note derived from Drive carries `source_urls`, `source_modified_at`, `source_status`, and `access_policy`, as in the matching `_template.md`. The shipped samples are not Drive-derived and say so in their own body instead of carrying the four keys. `examples/` is out of scope
- [ ] **Documents that carry frontmatter keep it valid.** `status` (`draft → proposed → agreed`) belongs to normative documents under `layer1/`, enacted operating rules, and ADRs; `doc_type` (`reference` / `template`) belongs to everything else. Do not promote a template's `status` in an upstream pull request — promotion is an act of agreement inside an adopting organization. `python3 scripts/validate.py` checks that every `status` value is one of the three
- [ ] **Changes are non-destructive.** Prefer adding to existing content. Replace a note by creating a new one and linking the old through frontmatter `supersedes`, rather than deleting it

## Writing an Issue

Use the same three sections the maintainer uses, so the issue can be picked up and worked on without a follow-up conversation:

1. **Background** — what is wrong, observed concretely. Quote the file and line, or paste the command and its output. Link the source if the claim comes from outside this repository
2. **Approach** — which files change and how. An issue that cannot name the files it would touch is not ready yet
3. **Acceptance criteria** — a condition someone else can check. A command with an expected exit status, a string that must appear in a named file, or a link that must resolve. "Reads better" is not an acceptance criterion

Reports of a broken adoption flow are useful even without an approach — say which step of `docs/setup-guide.md` you were on and what happened instead.

## Pull Request Conventions

- One logical change per pull request. Do not bundle unrelated fixes; open a separate issue for anything you notice along the way
- Reference the issue with `Closes #<number>` in the pull request body
- Describe how you verified the change, including the output of `python3 scripts/validate.py` if you touched links, file maps, frontmatter, or placeholders
- Everything you write here is public and is read by adopting organizations and by AI agents. Keep the tone plain and factual, and match the language of the document you are editing

## Scope Notes

- This repository ships no GitHub Actions workflows. Adding CI, issue templates, or anything under `.github/` is a supply-chain decision for the maintainer — open an issue and let the maintainer decide rather than sending the workflow in a pull request
- Licensing is MIT ([LICENSE](LICENSE)) and applies to contributions. Do not paste text from sources whose license does not permit it
