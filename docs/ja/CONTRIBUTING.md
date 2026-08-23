# Org-OS Starter への寄稿

English version: [../../CONTRIBUTING.md](../../CONTRIBUTING.md)

寄稿を検討していただきありがとうございます。本文書は **この上流リポジトリ** に寄稿する人と AI エージェント向け。導入組織が自分のリポジトリに定める運用ルールのテンプレートは [運用規約](docs/governance/運用規約.md) であり、本文書とは別物。

このリポジトリは Markdown のみで構成される。ビルド手順・依存インストール・テストスイートは存在しない。品質ゲートは下記のレビューチェックリストがすべてで、それ以外に通すべきものはない。

## 上流に還元してほしいもの

このスターターは「Use this template」で複製し、各組織の中で独立に育てることを前提にしている。上流に置くべきなのは **どの導入組織にも効く改善** だけ。

**歓迎:**

- `layer1/`・`knowledge/`・`docs/` のテンプレートの汎用的な穴 — 規範の欠落・曖昧さ・自己矛盾
- 実際の導入で有効だった運用パターンのうち、1組織に閉じず一般化できるもの
- 修正: リンク切れ・古いファイルマップ・翻訳の誤り・文書間の矛盾
- [導入ガイド](docs/導入ガイド.md) の導入フローが特定のステップで破綻するという報告

**上流では受け取れないもの:**

- 自組織で充填した `layer1/` の内容・実プロジェクトノート・実際の意思決定。これらは自組織の private リポジトリに置く
- 実在の顧客・取引先・人事情報（サンプル内も含む。下記の架空データ規約を参照）
- Layer 3〜5 のディレクトリ新設。実体ができるまで作らないのは設計原則であり、記述漏れではない（[README.md](../../README.md)「設計原則」）

一般化できるか判断がつかない場合は、変更を書く前に issue を立てる。

## Pull Request を出す前に

すべての項目を確認する。CI が何も強制しないため、以下は気づかずに壊れやすい不変条件になっている。

- [ ] **英語 canon と日本語ミラーを同時に更新した。** 英語文書が canon で、`docs/ja/` はその日本語ミラー。片側だけ変更するとリポジトリが不整合になる。対応関係は、root の `AGENTS.md` / `CLAUDE.md` / `CONTRIBUTING.md` ↔ `docs/ja/`、`docs/**` ↔ `docs/ja/docs/**`、`layer1/**` ↔ `docs/ja/layer1/**`、`knowledge/**` ↔ `docs/ja/knowledge/**`、`README.md`（日本語）↔ `README.en.md`（英語）。`examples/` はこの対応表の外にあり、ミラーを作らず、English summary のみを英語正本と歩調を合わせる。各側の参照先をどちらの言語にするかは次の項目で定める
- [ ] **参照先が読者の言語の文書を指している。** `docs/ja/` 内の参照は、日本語版が存在する限りそちらを指す。それ以外の場所では英語正本を指す — `AGENTS.md` の読み順の1件目（日本語の `README.md` ではなく `README.en.md`）と、**両方**の README の読み順表・ファイルマップのパス列（両者は同じ英語正本のパスを行単位で一致させる。読み順表のREADME自身の行だけが例外で、各READMEが自分自身のファイル名を書く）を含む。日本語ミラーは補足リンクとして併記してよいが、行のパスそのものにはしない。規約は [CLAUDE.md](CLAUDE.md)「上流リポジトリ専用の規約」にある。下記の検査は `docs/ja/` の外へ出るリンクをすべて列挙する。残る各件は意図した例外（`English version:` の冒頭リンク・日本語版である `README.md`・`LICENSE` のように日本語版が存在しないファイル）でなければならない。`python3` が無い環境では、下記は参照実装として扱い、node・ripgrep＋シェルループ・変更した `docs/ja/` 配下ファイルの直接確認などで同等の出力を作る

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

- [ ] **サンプルは架空データのみ。** 実在の顧客名・取引先名・実際の財務数値・実際のやり取り・社内非公開情報（人事・提携・M&A・未公開財務・係争）を含めない。APIキー・トークン・シークレットも同様。`examples/demo-company/` は設計上すべて架空（[CLAUDE.md](CLAUDE.md)「コミット禁止事項」）
- [ ] **Layer 3〜5 のディレクトリ・空ディレクトリ・プレースホルダのみのファイルを作っていない。** 未充填項目は `(要・代表)` のような責任者フラグ付きでのみ残し、裸の `(TODO)` は書かない（[CLAUDE.md](CLAUDE.md)「構造ルール」）。裸のプレースホルダは `python3 scripts/validate.py` が機械検出する
- [ ] **相対リンクがすべて解決し、ファイルマップが実ツリーと一致している。** ファイルを追加・移動・改名した場合は、`README.md` と `README.en.md` のファイルマップ・読み順表にも同じ変更が必要。リポジトリルートで `python3 scripts/validate.py` を実行する: `.md` だけでなくディレクトリや `LICENSE` 等の非Markdownを含む**すべて**の相対リンクの解決に加え、`[[wikilink]]` の解決・frontmatter `status` 値・裸のプレースホルダ・両 README の全ファイルマップと実ファイルの双方向一致（ツリーにあってマップに無いファイルも、その逆も違反）を検査し、検査したファイル数と違反の全件を出力する。exit code 0 が違反なし。その出力を PR に貼る。`python3` が無くスクリプトを実行できない環境では、下記のリンク検査部分の参照実装をもとに、node・ripgrep＋シェルループ・変更したファイルの直接確認などで同等の出力を作る

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

- [ ] **`knowledge/` のノートが対応するテンプレートの frontmatter 契約を満たしている。** Drive由来のノートは対応する `_テンプレート.md` と同じく `source_urls`・`source_modified_at`・`source_status`・`access_policy` を持つ。同梱サンプルはDrive由来ではないため4キーを持たず、その旨を本文に明記する。`examples/` は対象外
- [ ] **frontmatter を持つ文書はその妥当性を保っている。** `status`（`draft → proposed → agreed`）は `layer1/` の規範文書・制定後の運用規約・ADR に付く。`doc_type`（`reference` / `template`）はそれ以外に付く。テンプレートの `status` を上流の PR で昇格させない — 昇格は導入組織の中での合意行為。`status` 値が3値のいずれかであることは `python3 scripts/validate.py` が検査する
- [ ] **変更が非破壊である。** 既存内容への追記を優先する。ノートを置き換える場合は新しいノートを作り、古いノートを frontmatter `supersedes` でリンクする（削除しない）
- [ ] **変更を変更履歴に記録した。** `CHANGELOG.md` と `docs/ja/CHANGELOG.md` の `## [Unreleased]` に、Keep a Changelog の該当分類（`Added` / `Changed` / `Deprecated` / `Removed` / `Fixed` / `Security`）で1行を追加し、末尾に issue 番号を付す。導入組織が自分の複製の中から上流との差分を判断するための唯一の起点であり、ここに無い変更はどの導入組織からも見えない。除外: 変更履歴自体の変更と、導入組織が読む内容が変わらない変更（誤字修正・意味を変えない整形）

## issue の書き方

メンテナが使っているものと同じ3節構成で書く。追加のやり取りなしにそのまま着手できる状態にするため。

1. **背景** — 何が問題か。具体的な観測を書く。ファイル名と行番号を引用するか、コマンドとその出力を貼る。リポジトリ外の根拠に基づく場合はソースをリンクする
2. **対応方針** — どのファイルをどう変えるか。触るファイルを名指しできない issue はまだ書ける状態にない
3. **AC（受入基準）** — 他人が検証できる条件。期待する終了ステータス付きのコマンド、指定ファイルに現れるべき文字列、解決すべきリンクなど。「読みやすくなる」は AC ではない

導入フローが壊れているという報告は、対応方針がなくても有用。[導入ガイド](docs/導入ガイド.md) のどのステップで、代わりに何が起きたかを書く。

## Pull Request の規約

- 1 PR = 1 論理変更。無関係な修正を束ねない。作業中に気づいたことは別 issue に起票する
- PR 本文で `Closes #<番号>` により issue を参照する
- どう検証したかを書く。リンク・ファイルマップ・frontmatter・プレースホルダに触れた場合は `python3 scripts/validate.py` の出力を含める
- ここに書くものはすべて公開され、導入組織と AI エージェントに読まれる。平易・事実ベースの記述に留め、編集している文書の言語に合わせる

## スコープ外の注記

- このリポジトリは GitHub Actions のワークフローを同梱していない。CI・issue テンプレート・`.github/` 配下の追加はサプライチェーンに関わるメンテナの判断事項。ワークフローを PR で送るのではなく issue を立てる
- ライセンスは MIT（[LICENSE](../../LICENSE)）で、寄稿にも適用される。ライセンス上許諾されないソースからの文章を貼り付けない
