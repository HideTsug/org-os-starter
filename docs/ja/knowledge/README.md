# knowledge/ — 知識基盤（Layer 2）

組織の「現在地」を表す非機微な派生層。v0.1運用では、人間が作る原本はGoogle Driveに残す。AIはここに短いPJ状態・原本リンク・鮮度メタデータを置き、制限情報を含む原本は複製しない。

## ノート種別

| ディレクトリ | 種別 | 1ノートの単位 |
|---|---|---|
| `projects/` | プロジェクトノート | 進行中のプロジェクト1つ |
| `issues/` | issueノート | 気づいた課題1つ（プロジェクトに紐付け可） |

各ディレクトリの `_テンプレート.md` が形式の SSoT。`PJ-sample-equipment.md`・`ISSUE-0001.md` は架空データの見本で、自組織のノートが入ったら削除してよい。

## 共通ルール

- frontmatter の `classification` にデータ区分（`layer1/data-classification-matrix.md` の4区分）を自己申告する。**許容値は `公開` / `社内` の2つのみ**（区分3「顧客・取引先特定」・区分4「規制対象」のデータはこのリポジトリに置けないため、値としても現れない）
- **顧客・取引先の実名・実数値は書かない**（区分3）。必要なら案件ID・ロール表記（「顧客A」「代表」等）で参照する
- 種別判定は `tags`（`project` / `issue`）で行う。検索・集計ツールはこのタグを見る
- Drive由来ノートは`source_urls`・`source_modified_at`・`source_status`を記録する。`source_status`は`current`または`stale`。原本を再度開けなければ`stale`にする
- `access_policy`の既定は`source_acl`。派生ノートを回答に使う前に必要な原本へのアクセスを確認し、repoアクセスだけを開示許可とみなさない
- 派生した事実主張は原本URLへ追跡可能にする。原本が裏付けない内容は推論と明示するか書かない
- 古くなった記述は消さず追記で更新し、`last_reviewed` を更新する

## 拡張

顧客ノート・案件ノート・議事録要約ノート等の種別追加は、Google Drive取込設計と合わせて行う（`docs/google-drive-profile.md`と`docs/architecture.md`の発展要素参照）。種別を増やすときは必ず`_テンプレート.md`を先に定義する。
