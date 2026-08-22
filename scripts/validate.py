#!/usr/bin/env python3
"""Repository invariant checks for Org-OS Starter.

Runs the five mechanical checks named in CONTRIBUTING.md, "Before You Open
a Pull Request":

1. relative-link — every relative Markdown link resolves, including
   directories and non-.md targets such as LICENSE
2. wikilink     — every [[wikilink]] resolves to a Markdown file in the
   repository (by basename, or by path when the target contains "/")
3. status       — a document whose frontmatter carries `status` uses one of
   draft / proposed / agreed
4. placeholder  — no bare placeholder such as (TODO), (TBD), or (FIXME);
   unfilled items must carry an owner flag instead (CLAUDE.md,
   "Structure Rules")
5. file-map     — the full file maps in README.md and README.en.md match the
   repository's files in both directions

The first four checks run over every tracked Markdown file. The file-map
check compares each README tree with tracked files and mapped untracked files
that exist.

Fenced code blocks and inline code spans are excluded: the repository's own
rule documents quote `(TODO)` and `[[wikilink]]` literally as examples.

Usage: python3 scripts/validate.py   (from the repository root)
Requires only the Python 3 standard library. Prints the number of files
checked and every violation with its file path and line number.
Exit code 0 when there are no violations, 1 otherwise.
"""

import os
import re
import subprocess
import sys

MDLINK_RE = re.compile(r"\]\(([^)#:]+?)(?:#[^)]*)?\)")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
PLACEHOLDER_RE = re.compile(r"[（(]\s*(?:TODO|TBD|FIXME)\s*[）)]", re.IGNORECASE)
FENCE_RE = re.compile(r"^\s*(```|~~~)")
CODESPAN_RE = re.compile(r"`[^`\n]*`")
STATUS_RE = re.compile(r"^status:\s*[\"']?([^\"'\s]+)[\"']?\s*$")
ALLOWED_STATUS = {"draft", "proposed", "agreed"}
FILE_MAP_READMES = ("README.md", "README.en.md")
FILE_MAP_ROOT = "org-os-starter/"
TREE_ENTRY_RE = re.compile(r"^((?:(?:│   | {4}))*)(?:├── |└── )(.+)$")
TREE_COMMENT_RE = re.compile(r"\s+#.*$")


def list_md_files():
    """Tracked .md files via git; fall back to walking the tree."""
    try:
        out = subprocess.run(
            ["git", "ls-files", "-z", "*.md"],
            capture_output=True, text=True, check=True,
        ).stdout
        files = [f for f in out.split("\0") if f]
        if files:
            return files
    except (OSError, subprocess.CalledProcessError):
        pass
    files = []
    for root, dirs, names in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in names:
            if name.endswith(".md"):
                files.append(os.path.normpath(os.path.join(root, name)))
    return sorted(files)


def list_repo_files(mapped_files):
    """Tracked files via git, plus mapped untracked files that exist."""
    try:
        out = subprocess.run(
            ["git", "ls-files", "-z"],
            capture_output=True, text=True, check=True,
        ).stdout
        files = [f for f in out.split("\0") if f]
        if files:
            files.extend(path for path in mapped_files if os.path.isfile(path))
            return sorted(set(files))
    except (OSError, subprocess.CalledProcessError):
        pass
    files = []
    for root, dirs, names in os.walk("."):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in names:
            files.append(os.path.normpath(os.path.join(root, name)))
    return sorted(files)


def read_file_map(path, violations):
    """Return mapped file paths with their lines and the tree root line."""
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()

    for i, raw in enumerate(lines[:-1]):
        if not raw.strip().startswith("```"):
            continue
        if not lines[i + 1].startswith(FILE_MAP_ROOT):
            continue

        mapped = {}
        directories = []
        for j in range(i + 2, len(lines)):
            if lines[j].strip().startswith("```"):
                break
            match = TREE_ENTRY_RE.match(lines[j])
            if not match:
                continue

            depth = len(match.group(1)) // 4
            name = TREE_COMMENT_RE.sub("", match.group(2)).rstrip()
            directories = directories[:depth]
            if name.endswith("/"):
                directories.append(name[:-1])
                continue

            mapped["/".join(directories + [name])] = j + 1
        return mapped, i + 2

    violations.append(("file-map", path, 1,
                       "full file map block not found"))
    return {}, None


def check_file_map(path, mapped, root_line, repo_files, violations):
    """Compare one README file map with the repository in both directions."""
    mapped_files = set(mapped)
    for missing in sorted(mapped_files - repo_files, key=mapped.get):
        violations.append(("file-map", path, mapped[missing],
                           "mapped file does not exist -> %s" % missing))
    for missing in sorted(repo_files - mapped_files):
        violations.append(("file-map", path, root_line,
                           "repository file is missing from map -> %s" % missing))


def frontmatter_end(lines):
    """Index one past the closing --- of a leading frontmatter block, else 0."""
    if not lines or lines[0].strip() != "---":
        return 0
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return i + 1
    return 0


def check_file(path, basenames, violations):
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()

    fm_end = frontmatter_end(lines)
    for i in range(1, max(fm_end - 1, 0)):
        m = STATUS_RE.match(lines[i])
        if m and m.group(1) not in ALLOWED_STATUS:
            violations.append(("status", path, i + 1,
                               "status '%s' is not draft/proposed/agreed" % m.group(1)))

    in_fence = False
    base_dir = os.path.dirname(path)
    for i, raw in enumerate(lines):
        if FENCE_RE.match(raw):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        line = CODESPAN_RE.sub("", raw)

        for m in MDLINK_RE.finditer(line):
            target = os.path.normpath(os.path.join(base_dir, m.group(1)))
            if not os.path.exists(target):
                violations.append(("relative-link", path, i + 1,
                                   "-> %s" % m.group(1)))

        for m in WIKILINK_RE.finditer(line):
            target = m.group(1).strip()
            if "/" in target:
                rooted = target if target.endswith(".md") else target + ".md"
                if not (os.path.exists(rooted)
                        or os.path.exists(os.path.normpath(os.path.join(base_dir, rooted)))):
                    violations.append(("wikilink", path, i + 1, "-> [[%s]]" % target))
            elif target not in basenames:
                violations.append(("wikilink", path, i + 1, "-> [[%s]]" % target))

        if PLACEHOLDER_RE.search(line):
            violations.append(("placeholder", path, i + 1,
                               "bare placeholder without an owner flag"))


def main():
    files = list_md_files()
    basenames = {os.path.splitext(os.path.basename(f))[0] for f in files}
    violations = []
    for path in files:
        check_file(path, basenames, violations)

    file_maps = {}
    mapped_files = set()
    for path in FILE_MAP_READMES:
        mapped, root_line = read_file_map(path, violations)
        file_maps[path] = (mapped, root_line)
        mapped_files.update(mapped)
    repo_files = set(list_repo_files(mapped_files))
    for path in FILE_MAP_READMES:
        mapped, root_line = file_maps[path]
        if root_line is not None:
            check_file_map(path, mapped, root_line, repo_files, violations)

    for kind, path, lineno, detail in violations:
        print("%s: %s:%d %s" % (kind, path, lineno, detail))
    counts = {}
    for kind, _, _, _ in violations:
        counts[kind] = counts.get(kind, 0) + 1
    breakdown = ", ".join("%s %d" % (k, counts[k]) for k in sorted(counts)) or "none"
    print("checked %d files; %d violations (%s)" % (len(files), len(violations), breakdown))
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
