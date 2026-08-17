---
status: agreed
version: "1.0"
owner: maintainer
audience: ai
summary: Google Drive is the only external knowledge source supported by the v0.1 operating profile; Drive keeps originals and ACLs while the repository keeps norms and non-sensitive derived knowledge.
---

# ADR-0001: Google Drive-First v0.1

- Drafted: 2026-08-17 / maintainer
- Decided: 2026-08-17 / maintainer

## Background and Problem

The original starter asked the implementation DRI and ordinary members to treat a private GitHub repository as both the operating interface and the knowledge store. That preserves strong history and machine-readable structure, but it adds a new daily tool for non-engineers and requires knowledge to be copied out of the system where people already create it.

The first adoption goal is narrower: connect an existing company knowledge source, ask recurring project questions, and receive answers with links to the originals. Supporting several SaaS sources before this path is proven would multiply connector, permission, and freshness behavior without proving recurring use.

## Decision

1. **Google Drive is the only external knowledge source in the v0.1 operating profile.** Notion, Slack, Chatwork, SharePoint, and generic file connectors are outside v0.1.
2. **Use a two-layer knowledge topology.** Google Drive is the SSoT for human-authored originals and its existing access controls. `knowledge/` is the SSoT for non-sensitive, AI-oriented derived state: project summaries, issue summaries, source links, and freshness metadata.
3. **Keep Layer 1 in the private repository.** `layer1/` remains the machine-readable normative SSoT. Google Drive specialization changes the Layer 2 operating path, not the five-layer model or the `Company OS as Code` convention.
4. **Access Drive with per-user OAuth.** AI must inherit the current user's Drive permissions. Service accounts and domain-wide delegation are prohibited in v0.1 because they can create an access path broader than the asking user.
5. **Start read-only.** The first path is search, question answering, and source-linked catch-up. Automated edits to Drive originals are outside v0.1. Members continue to edit originals in Drive.
6. **Keep the internal source boundary provider-neutral.** Derived notes record stable source metadata rather than embedding Drive-specific behavior throughout the knowledge schema. A later source may be added through a new ADR after the Drive path demonstrates recurring use.

## Data Ownership and Flow

```text
Google Drive original (content + ACL + revision history)
        │ per-user OAuth, read-only
        ▼
classification check → extraction → non-sensitive derivation
        │
        ├─ answer with original Drive links
        └─ knowledge/ summary + source metadata

layer1/ rules ────────────────────────▲
```

- Do not mirror category 3 or category 4 content into GitHub, prompts shared with unauthorized people, logs, PR bodies, or issues.
- A derived output inherits the highest classification of the content it retains.
- `knowledge/` is not an authorization boundary. Every v0.1 derived note uses `access_policy: source_acl`; before using it in an answer, AI must verify that the current user can open every source required for that answer. For a note derived from multiple sources, the effective audience is the intersection of their audiences. A broader derived audience is outside v0.1 and requires a new ADR.
- Drive folder placement is a routing hint, not permission evidence. The effective Drive permission of the current user is the access boundary.
- Notifications only indicate that changes exist; an implementation must read the Drive change feed before updating derived state.

## Acceptance Criteria

- The README, architecture, setup guide, user guide, and agent entry point all describe Google Drive as the sole v0.1 external source.
- Ordinary members can follow the read/write/ask paths without using GitHub; GitHub remains an implementation-DRI and AI-maintenance surface.
- Project and issue templates can record original source URLs and source freshness without copying restricted source content.
- The permission model requires a two-account differential test across both direct Drive retrieval and cached or derived `knowledge/` state: a user must not receive content from a Drive document they cannot open.
- A changed Drive source can be detected and its derived freshness metadata can be updated without full re-ingestion.
- No documentation describes another external source connector as part of the v0.1 core.

## Options Not Chosen

- **GitHub-only daily operation** — preserves structure but keeps the largest non-engineer adoption barrier.
- **Drive-only storage with no repository layer** — makes daily contribution easy but removes the machine-readable normative SSoT, reviewable derived state, and `Company OS as Code` boundary.
- **Multi-source v0.1** — increases surface area before repeat use of the core question-answering path is proven.
- **Central service-account ingestion** — simplifies background indexing but can bypass the asking user's permission boundary.
- **Automated write-back in v0.1** — adds destructive and authorization risk before read usefulness is established.

## Re-evaluation Conditions

Revisit this decision when either condition is met:

1. Three external organizations complete the Drive setup and at least one organization uses the ask path twice within fourteen days; or
2. A blocked adopter provides a concrete recurring workflow whose source is not Google Drive.

The first negative signal is that connected users cannot name a recurring question they want answered. In that case, investigate the use case and document coverage before adding another connector.

## References

- [Google Drive API: sharing and permissions](https://developers.google.com/workspace/drive/api/guides/manage-sharing)
- [Google Drive API: retrieve changes](https://developers.google.com/workspace/drive/api/guides/manage-changes)
- [Google Drive API: download and export files](https://developers.google.com/workspace/drive/api/guides/manage-downloads)
- [Google Drive operating profile](../google-drive-profile.md)

## Revision History

| Date | Version | Author | Change |
|---|---|---|---|
| 2026-08-17 | v1.0 | maintainer | Adopted Google Drive-first v0.1 and the two-layer knowledge topology |
