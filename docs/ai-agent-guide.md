---
doc_type: reference
version: "1.0"
summary: Pre-clone briefing for an AI agent asked to build an organization's AI knowledge foundation. Confirms scope, self-assesses the execution environment, obtains private-repository consent, and hands over to Step 0 of the setup guide.
---

Japanese version: [docs/ja/docs/AIエージェント導入ガイド.md](ja/docs/AIエージェント導入ガイド.md)

# AI Agent Guide: Before You Clone

> This document is written for an AI agent that has **not cloned this repository yet** — typically one whose user just said "I want to build an AI knowledge base for my organization." It is self-contained and loadable from a single raw URL:
>
> `https://raw.githubusercontent.com/HideTsug/org-os-starter/main/docs/ai-agent-guide.md`
>
> If you are already inside a checkout of this repository, start from [`AGENTS.md`](../AGENTS.md) instead; this guide covers only the branch points **before** the repository exists on the user's side.

What you are looking at: Org-OS Starter is a knowledge-foundation starter kit, distributed as a **GitHub template repository**, for helping an organization become AI-native. It is free OSS under the MIT license — not a consulting engagement or onboarding service. The big picture is in [`README.en.md`](../README.en.md). Work through the four checks below in order; each exists because skipping it is a known way adoptions go wrong.

## 1. Confirm the Scope

Before touching anything, establish with the user:

- **Which organization is adopting.** One repository serves one organization. If the user names several organizations, pick one to start with.
- **Whether the requester is the implementation DRI or a delegated implementer.** The implementation DRI is the person who will hold merge authority and lead drafting of norms. If the requester is a delegate, confirm that a DRI exists and knows this work is happening — the DRI is one of the three decisions Step 0 of the setup guide requires, and cannot be filled in by AI.
- **What the first pain is.** The setup guide will ask for one narrow first use case. If the user can already name the area where people most often ask "what happened with that?", note it now.

## 2. Self-Assess Your Execution Environment

Determine honestly which of these describes you in this session:

- **You can create and edit files, and run `git` and `gh`** (an agentic environment such as Claude Code). You can drive the whole setup: continue with section 3.
- **You can only converse — no file writes, no shell.** Do not improvise the setup through copy-paste. Tell the user that adoption needs an agentic AI environment, hand them the raw URL of this guide to give that agent, and give the human-readable entry point [`README.en.md`](../README.en.md) for anything they want to read themselves.

Also state the standing constraint early: the v0.1 operating profile uses **Google Drive as its only external knowledge source**, read through each user's own OAuth grant. Whether your environment can actually read Drive that way is verified later, inside the setup steps — do not substitute a different access path if it cannot.

## 3. Get Consent for a Private Repository

The template starts public, but the filled copy will contain organizational norms, decisions, and real operating data. Before creating anything, obtain the user's explicit consent to these two points:

- The organization's copy is created with **"Use this template"** on the upstream repository — not by cloning or forking the public upstream and pushing to it.
- The copy is **private, from the moment it is created**. The acceptance criterion is mechanical: run `gh repo view --json visibility` inside the new repository and it must return `"visibility":"PRIVATE"`. Where `gh` is unavailable or the host is not GitHub, have a person confirm "Private" in the hosting settings screen. Either way, record the confirmation in the verification records section of [`docs/governance/operating-rules.md`](governance/operating-rules.md) once the repository exists.

Do not proceed while either point is unconfirmed. A public copy that is "made private later" has already leaked its history.

## 4. Hand Over to the Setup Guide

Once the private copy exists and is cloned:

1. Open [`AGENTS.md`](../AGENTS.md) in the new repository — it is the in-repository entry point for agents and contains the onboarding flow, including the one-time optional support confirmation.
2. Start from **Step 0** of [`docs/setup-guide.md`](setup-guide.md): the humans decide only the implementation DRI, the approval body, and the first narrow use case. Everything else should be filled by AI through questions.

## Revision History

| Date | Version | Author | Change |
|---|---|---|---|
| 2026-08-20 | v1.0 | upstream template | Initial version (#26) |
