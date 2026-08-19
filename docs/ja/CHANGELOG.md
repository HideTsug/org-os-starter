# Changelog

English version: [CHANGELOG.md](../../CHANGELOG.md)

本リポジトリの主な変更をこのファイルに記録する。[README.md](../../README.md) の更新戦略に従う導入組織が、自分の複製の中から上流との差分を判断できるようにするためのもの。形式は [Keep a Changelog](https://keepachangelog.com/ja/1.1.0/) に基づく。バージョンは本リポジトリの GitHub リリースタグに対応する。

## [Unreleased]

v1.0.0 以降の `main` 上の変更。

### Added

- 英語 canon／日本語ミラーの不変条件と PR 前チェックリストを載せた `CONTRIBUTING.md`（#17）
- `AGENTS.md` 冒頭の「このリポジトリを編集する場合」の分岐 — 自動読込するエージェントが導入フローへ誤誘導されないようにするもの（#18）
- `examples/demo-company/` — clone してすぐ試せる架空企業の充填済みデモ
- 英語 canon 化: 正本文書を英語へ翻訳して日本語ミラーを `docs/ja/` 配下に置き、全ファイル・ディレクトリ名を英語に改名
- `docs/ai-agent-guide.md` — raw URL 1本で読み込める clone 前の AI 向け導入台本（日本語ミラー付き）（#26）
- `scripts/validate.py` — 相対リンク・wikilink・frontmatter `status`・裸のプレースホルダの機械検査（#28）

### Changed

- Google Drive-first の v0.1 運用プロファイルを採用: Drive が人の書いた原本と ACL を保持し、リポジトリが規範と非機微な派生状態を保持する（ADR-0001）（#9）
- 派生ノートへの `access_policy: source_acl` の強制と、2アカウント権限差テストの派生状態への拡張（#10）
- データ分類マトリクスの実行環境の行を、製品名でなく性質で定義（#11）
- エージェント向けの記述をベンダ中立化（#12）
- AI 向け指示を検証可能・環境非依存に改善（#23）
- GitHub を E2/E3 実行環境から切り離して独自の保管先ルールとし、区分2「社内」ノートのコミット可否の自己矛盾を解消（#3）
- セットアップ経路を「Use this template」→ 自組織 private リポジトリの clone に分離（#2）

### Fixed

- README のファイルマップ・読み順表をリポジトリの実ツリーに一致（#4, #16）
- 翻訳の推敲と `docs/ja/` 相互参照の修正（#8）

## [1.0.0] - 2026-08-13

正式公開。組織を AI ネイティブに移行させるための知識基盤スターターキット（MIT・無料 OSS）。個人向け姉妹版 [pm-os-starter](https://github.com/HideTsug/pm-os-starter) の組織版。

### Added

- 5層アーキテクチャ: 規範・SSoT分離 → ナレッジ → ロール/SKILL → 統合 → ガバナンス。着手順は Layer 1 から
- v1 コア: 規範テンプレート3種（組織CLAUDE・データ分類マトリクス・禁止用途リスト）、`knowledge/` 構造、導入・利用ガイド、運用規約テンプレート、ADR の雛形
- 「Use this template」フロー: 自組織の private リポジトリを作り、Claude Code 等のエージェント型 AI と導入を開始。人間が最初に決めるのは導入責任者（DRI）・承認体制・最初の一点突破ユースケースの3つだけ
- AI エージェント入口としての `AGENTS.md`、同意ベースのスター/フォロー応援確認、`.gitignore`

[Unreleased]: https://github.com/HideTsug/org-os-starter/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/HideTsug/org-os-starter/releases/tag/v1.0.0
