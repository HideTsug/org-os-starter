---
tags:
  - issue
classification: internal
owner: Sato (fictional)
last_reviewed: 2026-08-13
issue_status: open
project: PJ-sample-equipment
reporter: Sato (fictional)
created: 2026-08-13
source: Initial equipment-ledger entry work (fictional)
summary: Fictional sample issue. The same equipment is registered under different names by department, so a normalization rule is needed.
---

Japanese version: [docs/ja/knowledge/issues/ISSUE-0001.md](../../docs/ja/knowledge/issues/ISSUE-0001.md)

# ISSUE-0001: Equipment names vary, preventing ledger normalization

> **Fictional sample data.** This file shows how to write an issue note. Delete it once the organization has real issues.
>
> It is not derived from Drive, so it carries none of `source_urls`, `source_modified_at`, `source_status`, or `access_policy`. A note derived from Drive must carry all four; see `_template.md` in this directory and `knowledge/README.md`.

## Overview

- The same equipment, such as monitors, is registered under different names by department, such as "display" and "LCD", so inventory aggregation is inaccurate.

## Background and Reproduction

- Among 120 initially registered items, 18 were found to be duplicate registrations under alternate names. These numbers are fictional.

## Expected State

- Define an approved equipment-category name list. New entries should select from that list, reducing new naming variation to zero.

## Notes

- Linked PJ: `[[PJ-sample-equipment]]`
