---
tags:
  - project
classification: internal
owner: Yamada (fictional)
last_reviewed: 2026-08-13
name: Equipment Ledger Project (fictional sample)
project_status: active
summary: Fictional sample project showing the note structure. It manages office equipment inventory and checkout records to prevent loss and duplicate purchases.
---

Japanese version: [docs/ja/knowledge/projects/PJ-サンプル-備品管理.md](../../docs/ja/knowledge/projects/PJ-サンプル-備品管理.md)

# PJ: Equipment Ledger Project (Fictional Sample)

> **Fictional sample data.** This file shows how to write a project note. Delete it once the organization has three real project notes.

## Purpose and Value

- Manage inventory and checkout for office equipment, such as PC peripherals and stationery, through a ledger to prevent loss and duplicate purchases.
- Make annual duplicate-purchase spending visible so it can support purchasing decisions.

## Scope

**In Scope**
- Create the equipment ledger and conduct monthly inventory checks.

**Out of Scope**
- Automating consumables ordering, which will be considered after the ledger has operated for three months.

## Completion Criteria

- The difference between the ledger and actual inventory remains within 5% for two consecutive monthly inventory checks.

## Team

- Owner: Yamada (fictional)
- Members: Sato (fictional)

## Milestones

- 2026-08-31 Complete initial ledger entry.
- 2026-09-30 Conduct the first monthly inventory check.

## Current Issues

- Whether checkout records should be kept on paper or in a spreadsheet, balancing frontline entry burden against aggregation.

## Recent Decisions

- 2026-08-10 The ledger master will be consolidated into one spreadsheet. Decision: do not split it by department. Reason: splitting would make reconciliation during inventory checks repetitive.

## Next Actions

- [ ] Yamada: enter existing equipment by 2026-08-20.
- [ ] Sato: interview frontline users about the checkout-record method.
