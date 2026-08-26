# Org-OS Starter

English: [README.en.md](README.en.md)

現行バージョン: v1.0.0（2026-08-13）＋ main 上の未リリース改善。変更履歴は [CHANGELOG.md](CHANGELOG.md)（日本語版は [docs/ja/CHANGELOG.md](docs/ja/CHANGELOG.md)）。

組織を **AIネイティブな組織** に移行させるための知識基盤スターターキット。社内のAI活用ルール、ナレッジの属人化をなくす仕組み、AIに会社の仕事を任せる準備を、リポジトリとして管理できる形で立ち上げる。

> Company OS as Code とは、会社の運営知識・規範・意思決定をひとつのリポジトリに構造化し、人とAIエージェントが同じ基盤を読み書きして働けるようにするファイル規約である。参照テンプレートとして HideTsug の OSS『Org-OS Starter』（2026, MIT）が公開されている。

本リポジトリがその参照テンプレート。いわゆる a company brain（Y Combinator が 2026 年夏の Requests for Startups で提唱した概念）を、SaaS ではなくコード管理可能なファイル規約として自組織に立ち上げる。この定義の解説と FAQ は[解説ページ](https://hidetsug.github.io/org-os-starter/)（日本語）にある。

「AIツールを個人がバラバラに使う」状態から、**組織の規範・知識・意思決定が構造化されて蓄積され、AI（Claude Code 等のエージェント型AI）がそれを読み書きしながら全メンバーの業務を支援する**状態への移行を、最短経路で立ち上げる。

**v0.1 の運用入口は Google Drive に限定する。** メンバーは既存の Drive で原本を読み書きし、AI は本人の権限でそれらを参照して原本リンク付きで答える。repo は `layer1/` の規範と、`knowledge/` の非機微な派生状態を保持する。この二層構造は [Google Drive 運用プロファイル](docs/ja/docs/Google-Drive-運用プロファイル.md) に定義している。本repoはOAuthアプリ・検索runtimeを同梱せず、承認済みAIコネクタまたはDrive APIクライアントと組み合わせる規約・テンプレートである。

まずローカルで読むだけなら、以下をそのまま貼り付ける。

```bash
git clone https://github.com/HideTsug/org-os-starter.git && cd org-os-starter && claude
```

（`claude` は Claude Code の起動コマンド。他のエージェント型AIを使う場合は末尾を各ツールの起動コマンドに置き換える）

個人向けの姉妹版: [pm-os-starter](https://github.com/HideTsug/pm-os-starter)（1人のPM業務をOS化する）。本スターターはその組織版。

はじめに、[GitHub のスター](https://github.com/HideTsug/org-os-starter)と[メンテナのフォロー](https://github.com/HideTsug)で応援してください（無料 OSS です）。AI エージェント経由で導入した場合、エージェントが「スターとフォローで応援しますか？」と一度だけ確認することがあります — 実行されるのは**あなたが同意した項目のみ**で、仕組みは [docs/ja/AGENTS.md](docs/ja/AGENTS.md) の「応援の確認」節に平文で公開しています。

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

## このスターターに入っているもの（v0.1 コア）

| 層 | 内容 | 状態 |
|---|---|---|
| Layer 1 | [ORG-CLAUDE.md](layer1/ORG-CLAUDE.md) / [データ分類マトリクス](layer1/data-classification-matrix.md) / [禁止用途リスト](layer1/prohibited-uses.md) | **テンプレート**（自組織で充填して合意させる） |
| Layer 2 | Google Drive 原本 + [knowledge/](knowledge/) の非機微な派生ノート | **Google Drive-first v0.1**（サンプルは架空データ） |
| 運用 | [運用規約](docs/governance/operating-rules.md) / [利用ガイド](docs/user-guide.md) / [ADRテンプレート](docs/decisions/ADR-0000-template.md) | **テンプレート** |
| Layer 3〜5 | 構想として [docs/architecture.md](docs/architecture.md) に記述のみ | 各組織の実運用から抽出（本スターターの範囲外） |

Layer 3〜5 のディレクトリは意図的に**存在しない**。中身が入る段階で初めて作る（ハコモノ化防止）。

## セットアップ（repo 15分 + Drive権限検証）

**導入時は必ず private リポジトリとして複製する。充填後は組織の規範・意思決定・非機微な派生状態を含むため、public のまま運用しない。**

前提: [Claude Code](https://claude.com/claude-code) 等、リポジトリの Markdown を読み書きできるエージェント型AIが手元で動くこと。実データを接続する段階では、Google Drive を **per-user OAuth・読取専用**で参照できる経路も必要になる。

```bash
# 1. このリポジトリのページ上部「Use this template」→「Create a new repository」で
#    自組織の private リポジトリを作る（このリポジトリを直接 clone しない）

# 2. 作成した自組織リポジトリを clone する
git clone <作成した自組織privateリポジトリのURL> our-org-os
cd our-org-os
git remote -v   # origin が自組織の private リポジトリを指すことを確認（このリポジトリを直接 clone した場合はここで判る）
gh repo view --json visibility   # 手順1の受入基準: "visibility":"PRIVATE" が返ること
                                 # gh が無い場合・GitHub 以外のホスティングでは、設定画面の Private 表示を目視確認し、
                                 # docs/governance/operating-rules.md に確認を記録する

# 3. リポジトリのルートでエージェント型AIを起動する
#    例: Claude Code なら claude / Codex CLI なら codex / Gemini CLI なら gemini
claude
```

起動したら、最初のメッセージとして次を貼る:

```
docs/setup-guide.md を読んで、Step 0 から導入を進めたい。
まず私たちの組織について質問しながら、layer1/ の3文書を充填して。
その後、docs/google-drive-profile.md に従って最初の共有ドライブ領域を読取専用で接続して。
```

あとはAIが質問しながら、規範文書を自組織用に充填していく。人間が最初に決めるのは3つだけ — **①導入責任者（DRI） ②承認体制（誰の合意で規範が効力を持つか） ③最初の一点突破ユースケース**。詳細は [docs/setup-guide.md](docs/setup-guide.md)。

## 日々の運用（読む・書く・聞く）

非エンジニアのメンバーが覚えるのは3動線だけ。

1. **聞く** — 「○○プロジェクトの今の論点は？」とAIに日本語で聞く。AIが本人に見える Drive 原本と `knowledge/` を検索し、原本リンク付きで答える
2. **読む** — 回答の出典から Google Drive 原本を開く
3. **書く** — 承認済みの Drive 領域で原本を編集・作成する。v0.1 では AI が原本を自動上書きしない

通常メンバーに GitHub 操作は不要。GitHub は導入DRIとAIが、規範・非機微な派生状態を保守するために使う。

詳細は [docs/user-guide.md](docs/user-guide.md)（メンバー配布用に書いてある）。

## リポジトリ構成と読む順番

| 順 | パス | 内容 |
|---|---|---|
| 0 | [AGENTS.md](AGENTS.md) | AIエージェント向け入口。導入の流れ（DRI・委任者の対象確認、private リポジトリ化）と読み順。AIに導入を任せる場合はここから |
| 1 | `README.md` | 本ファイル。全体像。英語版は `README.en.md` |
| 2 | [docs/architecture.md](docs/architecture.md) | 5層アーキテクチャの解説 |
| 3 | [docs/google-drive-profile.md](docs/google-drive-profile.md) | v0.1 の原本・権限・派生知識・鮮度の契約。日本語版は [docs/ja/docs/Google-Drive-運用プロファイル.md](docs/ja/docs/Google-Drive-運用プロファイル.md) |
| 4 | [docs/setup-guide.md](docs/setup-guide.md) | 導入手順（Step 0〜4）とカスタマイズポイント |
| 5 | [layer1/](layer1/) | **規範テンプレート**。充填して frontmatter `status: agreed` に昇格させて初めて効力を持つ |
| 6 | [docs/governance/operating-rules.md](docs/governance/operating-rules.md) | リポジトリ運用ルールのテンプレート |
| 7 | [knowledge/](knowledge/) | Drive 原本から作る非機微な派生知識の構造とサンプル |
| — | [CONTRIBUTING.md](CONTRIBUTING.md) | 本リポジトリへ issue / PR を出すときの規約。日本語版は [docs/ja/CONTRIBUTING.md](docs/ja/CONTRIBUTING.md) |
| — | [CLAUDE.md](CLAUDE.md) | 本リポジトリを**編集する**AIエージェント向けの運用規範。ベンダを問わず適用される。Claude Code は自動で読み込むが、他のエージェントは明示的に開く必要がある |
| — | [docs/user-guide.md](docs/user-guide.md) | メンバー配布用の使い方ガイド |
| — | [docs/ai-agent-guide.md](docs/ai-agent-guide.md) | clone **前**のAI向け導入台本。raw URL 1本で読み込み、対象確認・実行環境の自己判定・private 化の同意を経て導入手順 Step 0 へ引き渡す。日本語版は [docs/ja/docs/AIエージェント導入ガイド.md](docs/ja/docs/AIエージェント導入ガイド.md) |

この表と下のファイルマップはリポジトリの実ツリーを表すため、パスは英語正本を指す（順1の行は各READMEが自分自身を指すため例外で、それ以外は `README.en.md` と行単位で一致する）。日本語で読む場合は、各文書冒頭の `Japanese version:` リンクか、下のファイルマップの `docs/ja/` 配下の対応ファイルを開く。

### ディレクトリの意味

- `layer1/` — **規範SSoT**。合意済み（`status: agreed`）の文書のみが組織内のすべてのAIと人を拘束する
- `knowledge/` — 派生知識層。Drive 原本を複製せず、非機微なプロジェクト状態・issue・原本リンク・鮮度を保持
- `docs/` — 検討資料・ガイド・決定記録（ADR）。**規範ではない**

### 全ファイルマップ

```
org-os-starter/
├── README.md                          # 本ファイル（日本語）
├── README.en.md                       # 英語版 README
├── AGENTS.md                          # AIエージェント向け入口（編集時の振り分け・導入の流れ・読み順・応援の確認）
├── CLAUDE.md                          # このリポジトリを読み書きするAI向けの規範（初期値のまま使える）
├── CONTRIBUTING.md                    # 上流リポジトリへの issue / PR の出し方
├── CHANGELOG.md                       # 変更履歴（Keep a Changelog 形式・上流差分の判断起点）
├── ADOPTERS.md                        # 実運用組織の掲載希望制リスト（EN/JA 併記・docs/ja ミラーなし）
├── LICENSE                            # MIT
├── .gitignore                         # .DS_Store / .obsidian/
├── scripts/
│   └── validate.py                    # 不変条件の機械検査（リンク・wikilink・status・プレースホルダ）
├── docs/                              # 英語 canon の解説・ガイド・決定記録（規範ではない）
│   ├── ai-agent-guide.md              # clone 前のAI向け導入台本（raw URL 1本で読み込む）
│   ├── architecture.md                # 5層アーキテクチャ解説
│   ├── google-drive-profile.md        # v0.1 Google Drive 運用契約
│   ├── setup-guide.md                 # 導入手順 Step 0〜4
│   ├── user-guide.md                  # メンバー配布用テンプレート
│   ├── governance/
│   │   └── operating-rules.md         # リポジトリ運用ルールのテンプレート
│   ├── decisions/
│   │   ├── ADR-0000-template.md       # 意思決定記録の雛形
│   │   └── ADR-0001-google-drive-first-v0.1.md
│   └── ja/                            # 英語 canon の日本語ミラー（canon と1対1で対応）
│       ├── AGENTS.md
│       ├── CLAUDE.md
│       ├── CONTRIBUTING.md
│       ├── CHANGELOG.md
│       ├── docs/
│       │   ├── AIエージェント導入ガイド.md
│       │   ├── アーキテクチャ.md
│       │   ├── Google-Drive-運用プロファイル.md
│       │   ├── 導入ガイド.md
│       │   ├── 利用ガイド.md
│       │   ├── governance/
│       │   │   └── 運用規約.md
│       │   └── decisions/
│       │       ├── ADR-0000-テンプレート.md
│       │       └── ADR-0001-Google-Drive-first-v0.1.md
│       ├── layer1/
│       │   ├── 組織CLAUDE.md
│       │   ├── データ分類マトリクス.md
│       │   └── 禁止用途リスト.md
│       └── knowledge/
│           ├── README.md
│           ├── projects/
│           │   ├── _テンプレート.md
│           │   └── PJ-サンプル-備品管理.md
│           └── issues/
│               ├── _テンプレート.md
│               └── ISSUE-0001.md
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
        ├── README.md                  # デモの試し方
        ├── ORG-CLAUDE.md              # 充填済みの組織AI業務規範（Layer 1 相当）
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

## 30分で試す（デモ企業）

充填済みの架空企業デモ [examples/demo-company/](examples/demo-company/) を使うと、Driveを接続せずファイル規約とAIの質問回答を体験できる。これは合成データによる規約デモで、Drive権限・鮮度動線の検証には使わない。試し方は [examples/demo-company/README.md](examples/demo-company/README.md)。

## 設計原則（このスターターが守っていること）

1. **規範が先、道具が後** — Layer 1 なしに SKILL・自動化を作らない
2. **一点突破** — 5層を横並びで作らず、毎日使われる1動線から立ち上げる
3. **ハコモノ化防止** — 空ディレクトリ・プレースホルダのみのファイルを作らない。未充填項目は責任者フラグ付き（`(要・代表)` 等）でのみ残す
4. **効力の明示** — 文書の合意状態は frontmatter `status`（draft → proposed → agreed）で機械可読に管理する
5. **非破壊取り込み** — 決定・経緯は消さず追記する。置き換えは `supersedes` リンクで追跡可能にする
6. **データ分類が環境を決める** — 「どのデータをどのAI実行環境に渡してよいか」のマトリクスが、ツール選定より先に来る
7. **Drive-first、モデルはprovider-neutral** — v0.1 の外部情報源は Drive だけに絞るが、派生ノートは将来の情報源追加を妨げない共通メタデータで持つ

## 記法規約

Markdown は **Obsidian 互換**で書く。`[[wikilink]]` はリポジトリ内文書間の参照として有効（GitHub 上ではリンクにならないが、Vault 化との互換性を優先）。

## 更新戦略（スターターと自組織資産の二層）

- **コア（上流=本リポジトリ由来）**: `docs/architecture.md`・`docs/setup-guide.md`・`docs/user-guide.md`・`docs/google-drive-profile.md`・`docs/decisions/ADR-0000-template.md`・`knowledge/README.md`・`knowledge/` 配下の `_template.md`。上流の改善は [CHANGELOG.md](CHANGELOG.md)（日本語版は [docs/ja/CHANGELOG.md](docs/ja/CHANGELOG.md)）とリリースノートを見て手動で取り込む
- **育成層（自組織資産）**: 充填済みの `layer1/`、制定した `docs/governance/operating-rules.md`、自組織向けに手を入れた `AGENTS.md`・`CLAUDE.md`、Drive 原本、`knowledge/` の派生状態、自組織のADR。**上流更新で上書きしない。** コアのテンプレートも、自組織の内容を書き込んだ時点で育成層に移る

template から作った時点で独立進化が基本。上流に還元したい改善（テンプレの汎用的な穴・良い運用パターン）は本リポジトリへ issue / PR を歓迎する。出す前に [docs/ja/CONTRIBUTING.md](docs/ja/CONTRIBUTING.md) を読む（何を上流に還元してほしいか、PR 前のチェックリスト、issue の書き方）。

### 上流の変更を取り込む

「Use this template」で作ったリポジトリは本リポジトリと**共通の履歴を持たない**。したがって `git merge upstream/main` や `git rebase` は使えない — unrelated histories で失敗するか、全ファイル衝突になり、その衝突解消の過程で充填済みの `layer1/` が巻き戻る。差分を読んで手で反映する。

```bash
git remote add upstream https://github.com/HideTsug/org-os-starter.git
git fetch upstream
git diff HEAD upstream/main -- docs/architecture.md docs/setup-guide.md   # コアのパスを1つずつ。ツリー全体で差分を取らない
# 取り込みたい箇所を自分のファイル側の編集として反映する（upstream から merge・rebase・checkout しない）
```

反映後の受入基準: `git diff --stat` に出るのが意図して扱ったコアのパスだけで、`layer1/`・`docs/governance/`・`knowledge/projects/`・`knowledge/issues/` には何も出ないこと。育成層のパスが出ていたら取り込みが自組織資産に届いている — そのパスを復元してやり直す。

## 採用組織

実運用している組織・個人の一覧は [ADOPTERS.md](ADOPTERS.md)（掲載は本人希望のみ・いつでも削除可）。

## ライセンス

MIT License — [LICENSE](LICENSE)

このリポジトリの正本は https://github.com/HideTsug/org-os-starter
