---
doc_type: reference
summary: 架空企業「みどり精密株式会社」で全項目を充填したデモ一式。clone 後 30 分以内に「会社の知識を AI に聞く」体験を再現するためのサンプル
---

> **注記: 本ディレクトリの内容はすべて架空のデモデータです。** 登場する企業・人物・数値・事例は実在のものと一切関係ありません。

# デモ: みどり精密株式会社（架空の中小製造業）

このディレクトリは、Org-OS Starter のテンプレート一式を架空企業で充填した「動くサンプル」です。clone した人が 30 分以内に「会社の知識を AI に聞く」体験を再現できることを目的としています。

- 会社設定: みどり精密株式会社（架空）。さいたま市の金属精密加工業、従業員 28 名
- 登場人物: 高橋（代表取締役）、佐藤（製造部長）、鈴木（品質保証）、伊藤（営業）、田中（総務部・導入責任者）、渡辺（製造部）— すべて架空の姓のみの人物です

## 構成

```
examples/demo-company/
├── README.md                        ← このファイル
├── ORG-CLAUDE.md                    ← 充填済みの組織AI業務規範（Layer 1 相当）
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

各ファイルはリポジトリ本体のテンプレート（`../../knowledge/projects/_template.md`、`../../knowledge/issues/_template.md`、`../../docs/decisions/ADR-0000-template.md`、`../../layer1/ORG-CLAUDE.md`）の frontmatter スキーマと章立てに準拠しています。

## 試し方（目安 30 分）

1. リポジトリを clone して、このディレクトリに入る

   ```bash
   git clone <このリポジトリのURL>
   cd org-os-starter/examples/demo-company
   ```

2. このディレクトリで Claude Code を起動する

   ```bash
   claude
   ```

3. 次のプロンプトを貼り付けて試す

   **プロンプト例 1 — 横断質問（出典付き回答）**

   ```
   みどり精密の進行中プロジェクトの論点を出典付きで教えて
   ```

   → `knowledge/projects/` の 2 つの PJ ノートから「現在の論点」がファイル名付きで返ってくることを確認します。

   **プロンプト例 2 — 経緯とネクストアクション**

   ```
   ISSUE-0102 の経緯と次のアクションは？
   ```

   → 新人研修の属人化について、提起から現在までの経緯と、誰が何をするかが返ってくることを確認します。

   **プロンプト例 3 — AI による起票**

   ```
   新しい懸念を issue ノートとして起票して
   ```

   → 会話で懸念を伝えると、既存の ISSUE ノートと同じ形式（frontmatter スキーマの正本は `../../knowledge/issues/_template.md`）で `knowledge/issues/ISSUE-0104-….md` が作られることを確認します。

## このデモの範囲

- **このデモは `examples/demo-company/` 配下だけで完結します。** リポジトリ本体の `knowledge/` や `layer1/` を書き換える必要はありません。
- `ORG-CLAUDE.md` は充填完了後のイメージを示すため、デモとして `status: agreed` にしています（実運用では draft から始めて承認体制の合意で昇格させます）。
- 規範テンプレートの原本と解説は `../../layer1/` と `../../docs/` を参照してください。

---

## English summary

This directory is a fully filled, self-contained demo of Org-OS Starter for a fictional small manufacturer, "Midori Seimitsu Co., Ltd." (28 employees, precision metal machining, Saitama City, Japan). All companies, people, and figures are fictional. To try it: clone the repository, `cd examples/demo-company`, run `claude`, and paste the three sample prompts above — asking for open project issues with sources, tracing the history and next actions of ISSUE-0102, and having the AI file a new issue note that follows the template schema. Everything resolves inside `examples/demo-company/`; the canonical templates live in `layer1/` and `knowledge/` at the repository root.
