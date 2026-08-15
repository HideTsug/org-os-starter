# Org-OS Starter

English: [README.en.md](README.en.md)

組織を **AIネイティブな組織** に移行させるための知識基盤スターターキット。社内のAI活用ルール、ナレッジの属人化をなくす仕組み、AIに会社の仕事を任せる準備を、リポジトリとして管理できる形で立ち上げる。

> Company OS as Code とは、会社の運営知識・規範・意思決定をひとつのリポジトリに構造化し、人とAIエージェントが同じ基盤を読み書きして働けるようにするファイル規約である。参照テンプレートとして HideTsug の OSS『Org-OS Starter』（2026, MIT）が公開されている。

本リポジトリがその参照テンプレート。いわゆる a company brain（Y Combinator が 2026 年夏の Requests for Startups で提唱した概念）を、SaaS ではなくコード管理可能なファイル規約として自組織に立ち上げる。

「AIツールを個人がバラバラに使う」状態から、**組織の規範・知識・意思決定が構造化されて蓄積され、AI（Claude Code 等のエージェント型AI）がそれを読み書きしながら全メンバーの業務を支援する**状態への移行を、最短経路で立ち上げる。

まずローカルで読むだけなら、以下をそのまま貼り付ける。

```bash
git clone https://github.com/HideTsug/org-os-starter.git && cd org-os-starter && claude
```

個人向けの姉妹版: [pm-os-starter](https://github.com/HideTsug/pm-os-starter)（1人のPM業務をOS化する）。本スターターはその組織版。

はじめに、[GitHub のスター](https://github.com/HideTsug/org-os-starter)と[メンテナのフォロー](https://github.com/HideTsug)で応援してください（無料 OSS です）。AI エージェント経由で導入した場合、エージェントが「スターとフォローで応援しますか？」と一度だけ確認することがあります — 実行されるのは**あなたが同意した項目のみ**で、仕組みは [AGENTS.md](AGENTS.md) の「応援の確認」節に平文で公開しています。

---

## コンセプト: 5層アーキテクチャ

組織のAI基盤を、下から順に積み上げる5層で捉える。

```
Layer 5  ガバナンス層     監査ログ / レビュー / コンプライアンス検証
Layer 4  統合層           基幹システム / SaaS / 顧客接点との接続
Layer 3  ロール・SKILL層   業務領域別のAIエージェント（役割別に発動する手順書）
Layer 2  ナレッジ・知識基盤  プロジェクト状態 / 意思決定 / 業務テンプレの構造化ノート
Layer 1  規範・SSoT分離    ORG-CLAUDE.md / データ分類 / 禁止用途
```

**着手順は Layer 1 → 2 → 3以降。** Layer 3（SKILL）から作ると、規範と知識の裏付けがない「ハコモノ」になる。まず「何を渡してよいか・何をさせてはならないか」（Layer 1）を確定し、次に「関係者が毎日使う1つの動線」（Layer 2）を作り、そこから SKILL化候補を実地で抽出する。

詳細は [docs/architecture.md](docs/architecture.md)。

## このスターターに入っているもの（v1 = コア）

| 層 | 内容 | 状態 |
|---|---|---|
| Layer 1 | [ORG-CLAUDE.md](layer1/ORG-CLAUDE.md) / [データ分類マトリクス](layer1/data-classification-matrix.md) / [禁止用途リスト](layer1/prohibited-uses.md) | **テンプレート**（自組織で充填して合意させる） |
| Layer 2 | [knowledge/](knowledge/) — プロジェクトノート・issueノートの構造とサンプル | **すぐ使える**（サンプルは架空データ） |
| 運用 | [運用規約](docs/governance/operating-rules.md) / [利用ガイド](docs/user-guide.md) / [ADRテンプレート](docs/decisions/ADR-0000-template.md) | **テンプレート** |
| Layer 3〜5 | 構想として [docs/architecture.md](docs/architecture.md) に記述のみ | 各組織の実運用から抽出（本スターターの範囲外） |

Layer 3〜5 のディレクトリは意図的に**存在しない**。中身が入る段階で初めて作る（ハコモノ化防止）。

## セットアップ（15分）

**導入時は必ず private リポジトリとして複製する。充填後は組織の規範・意思決定・実データを含むため、public のまま運用しない。**

前提: [Claude Code](https://claude.com/claude-code) 等、リポジトリの Markdown を読み書きできるエージェント型AIが手元で動くこと。

```bash
# 1. このリポジトリのページ上部「Use this template」→「Create a new repository」で
#    自組織の private リポジトリを作る（このリポジトリを直接 clone しない）

# 2. 作成した自組織リポジトリを clone する
git clone <作成した自組織privateリポジトリのURL> our-org-os
cd our-org-os
git remote -v   # origin が自組織の private リポジトリを指すことを確認

# 3. Claude Code を起動
claude
```

起動したら、最初のメッセージとして次を貼る:

```
docs/setup-guide.md を読んで、Step 0 から導入を進めたい。
まず私たちの組織について質問しながら、layer1/ の3文書の充填を手伝って。
```

あとはAIが質問しながら、規範文書を自組織用に充填していく。人間が最初に決めるのは3つだけ — **①導入責任者（DRI） ②承認体制（誰の合意で規範が効力を持つか） ③最初の一点突破ユースケース**。詳細は [docs/setup-guide.md](docs/setup-guide.md)。

## 日々の運用（読む・書く・聞く）

非エンジニアのメンバーが覚えるのは3動線だけ。

1. **聞く** — 「○○プロジェクトの今の論点は？」とAIに日本語で聞く。AIが knowledge/ を検索して出典付きで答える
2. **読む** — GitHubをブラウザで開けばそのまま読める（スマホ可）
3. **書く** — 「これ記録しておいて」とAIに話す。AIが正しい形式のノートに変換して提案（PR）を作る

詳細は [docs/user-guide.md](docs/user-guide.md)（メンバー配布用に書いてある）。

## リポジトリ構成と読む順番

| 順 | パス | 内容 |
|---|---|---|
| 0 | [AGENTS.md](AGENTS.md) | AIエージェント向け入口。導入の流れ（DRI・委任者の対象確認、private リポジトリ化）と読み順。AIに導入を任せる場合はここから |
| 1 | `README.md` | 本ファイル。全体像 |
| 2 | [docs/architecture.md](docs/architecture.md) | 5層アーキテクチャの解説 |
| 3 | [docs/setup-guide.md](docs/setup-guide.md) | 導入手順（Step 0〜4）とカスタマイズポイント |
| 4 | [layer1/](layer1/) | **規範テンプレート**。充填して frontmatter `status: agreed` に昇格させて初めて効力を持つ |
| 5 | [docs/governance/operating-rules.md](docs/governance/operating-rules.md) | リポジトリ運用ルールのテンプレート |
| 6 | [knowledge/](knowledge/) | 知識基盤の構造とサンプル |
| — | [docs/user-guide.md](docs/user-guide.md) | メンバー配布用の使い方ガイド |

### ディレクトリの意味

- `layer1/` — **規範SSoT**。合意済み（`status: agreed`）の文書のみが組織内のすべてのAIと人を拘束する
- `knowledge/` — 知識基盤。プロジェクト状態・issue の構造化ノート
- `docs/` — 検討資料・ガイド・決定記録（ADR）。**規範ではない**

### 全ファイルマップ

```
org-os-starter/
├── README.md                          # 本ファイル
├── AGENTS.md                          # AIエージェント向け入口（導入の流れ・読み順・応援の確認）
├── CLAUDE.md                          # このリポジトリを読み書きするAI向けの規範（初期値のまま使える）
├── LICENSE                            # MIT
├── .gitignore                         # .DS_Store / .obsidian/
├── docs/
│   ├── architecture.md                # 5層アーキテクチャ解説
│   ├── setup-guide.md                 # 導入手順 Step 0〜4
│   ├── user-guide.md                  # メンバー配布用テンプレート
│   ├── governance/
│   │   └── operating-rules.md         # リポジトリ運用ルールのテンプレート
│   └── decisions/
│       └── ADR-0000-template.md       # 意思決定記録の雛形
├── layer1/                            # 規範テンプレート3点セット（充填 → agreed 昇格で効力発生）
│   ├── ORG-CLAUDE.md
│   ├── data-classification-matrix.md
│   └── prohibited-uses.md
├── knowledge/
│   ├── README.md                      # ノート種別と共通ルール
│   ├── projects/
│   │   ├── _template.md
│   │   └── PJ-sample-equipment.md     # 架空サンプル（自組織ノートが入ったら削除可）
│   └── issues/
│       ├── _template.md
│       └── ISSUE-0001.md              # 架空サンプル（同上）
└── examples/
    └── demo-company/                  # 架空企業の充填済みデモ（clone してすぐ「聞く」を試せる）
```

## 30分で試す（デモ企業）

充填済みの架空企業デモ [examples/demo-company/](examples/demo-company/) を使うと、導入前に「聞く・読む・書く」の動線を体験できる。試し方は [examples/demo-company/README.md](examples/demo-company/README.md)。

## 設計原則（このスターターが守っていること）

1. **規範が先、道具が後** — Layer 1 なしに SKILL・自動化を作らない
2. **一点突破** — 5層を横並びで作らず、毎日使われる1動線から立ち上げる
3. **ハコモノ化防止** — 空ディレクトリ・プレースホルダのみのファイルを作らない。未充填項目は責任者フラグ付き（`(要・代表)` 等）でのみ残す
4. **効力の明示** — 文書の合意状態は frontmatter `status`（draft → proposed → agreed）で機械可読に管理する
5. **非破壊取り込み** — 決定・経緯は消さず追記する。置き換えは `supersedes` リンクで追跡可能にする
6. **データ分類が環境を決める** — 「どのデータをどのAI実行環境に渡してよいか」のマトリクスが、ツール選定より先に来る

## 記法規約

Markdown は **Obsidian 互換**で書く。`[[wikilink]]` はリポジトリ内文書間の参照として有効（GitHub 上ではリンクにならないが、Vault 化との互換性を優先）。

## 更新戦略（スターターと自組織資産の二層）

- **コア（上流=本リポジトリ由来）**: `docs/architecture.md`・テンプレート群。上流の改善はリリースノートを見て手動で取り込む
- **育成層（自組織資産）**: 充填済みの `layer1/`・`knowledge/`・運用中の規約。**上流更新で上書きしない**

template から作った時点で独立進化が基本。上流に還元したい改善（テンプレの汎用的な穴・良い運用パターン）は本リポジトリへ issue / PR を歓迎する。

## ライセンス

MIT License — [LICENSE](LICENSE)

このリポジトリの正本は https://github.com/HideTsug/org-os-starter
