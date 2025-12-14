# FIRST Tech Challenge ドキュメントプロジェクト（日本語翻訳版）
=====================================================

![ビルド](https://readthedocs.com/projects/first-tech-challenge-ftcdocs/badge/?version=latest) ![リンクチェック](https://github.com/FIRST-Tech-Challenge/ftcdocs/actions/workflows/link-check.yaml/badge.svg)

本リポジトリは、 **FIRST Tech Challenge 公式ドキュメント**の非公式日本語翻訳プロジェクトです。

---

## ⚠️ 非公式な翻訳と免責事項（重要）

**本プロジェクトは、FIRST Tech Challenge (FIRST®) の公式ドキュメントではありません。**

* この日本語翻訳は、日本のFTCコミュニティのために **[Team 33678 Tezukayama]** が自主的に運営・提供しているものです。
* 翻訳の正確性には努めていますが、**公式な情報源としては必ず英語のオリジナルドキュメントを参照してください。**
* 本翻訳の使用により生じたいかなる損害についても、本プロジェクトの貢献者および運営者は一切の責任を負いません。

公式ウェブサイト（英語原文）：
https://ftc-docs.firstinspires.org

---

## 貢献について

私たちは、FTC Docs の改善にご協力いただける方を常に求めています。

貢献に関する詳細情報については、公式 FTC Docs の [貢献セクション](https://ftc-docs.firstinspires.org/contrib/index.html) を参照してください。
（この翻訳プロジェクトへの貢献方法については、別途[CONTRIBUTING.mdなどのリンク]を参照してください。）

---

## 📚 翻訳ドキュメント

### ⚠️ 重要なお知らせ: 新しい翻訳システムへの移行

このプロジェクトは、より効率的で標準的な **.po ベースの翻訳システム** への移行を進めています。

### 🆕 新しい翻訳システム (.po ベース)

**[WHY_PO_TRANSLATION.md](WHY_PO_TRANSLATION.md)** - なぜ移行するのか？
- 現在の問題点と .po ベースの利点
- 具体的な改善例
- 移行の決断材料

**[MIGRATION_NEXT_STEPS.md](MIGRATION_NEXT_STEPS.md)** - 移行の手順
- 段階的な移行方法
- 3つのオプション（完全移行、段階的移行、テスト移行）
- 次に何をすべきか

**[PO_TRANSLATION_WORKFLOW.md](PO_TRANSLATION_WORKFLOW.md)** - 新しいワークフロー
- 日常的な翻訳作業の流れ
- Make コマンドの使い方
- 翻訳ツールの活用

**[MIGRATION_TO_PO_GUIDE.md](MIGRATION_TO_PO_GUIDE.md)** - 技術的詳細
- .po システムの仕組み
- セットアップ手順
- トラブルシューティング

### 📊 移行状況

- ✅ 翻訳システムのセットアップ完了
- ✅ 既存翻訳のスキャン完了（161ファイル、3258ブロック）
- ✅ 翻訳マッピングの抽出完了 ([TRANSLATION_MAPPING.md](TRANSLATION_MAPPING.md))
- ⏳ 英語版RSTの復元と .pot 生成（次のステップ）
- ⏳ .po ファイルへの翻訳移行（段階的に実施）

### 🔧 従来の翻訳システム (RST直接翻訳)

翻訳作業に関するすべてのドキュメントは **[docs-ja/](docs-ja/)** フォルダに整理されています。

**[docs-ja/guides/AI_TRANSLATION_GUIDE.md](docs-ja/guides/AI_TRANSLATION_GUIDE.md)** 【従来の方法】
- AI翻訳ツール向けの統合ガイド
- 翻訳ルール、RST構文、エラー対策をすべて網羅
- **注意**: この方法は段階的に .po ベースに移行予定

### 主要ドキュメント

- **[docs-ja/README.md](docs-ja/README.md)** - 翻訳プロジェクトの概要とフォルダ構成
- **[docs-ja/reference/GLOSSARY.md](docs-ja/reference/GLOSSARY.md)** - 用語統一リスト（92語）
- **[docs-ja/reference/RST_TROUBLESHOOTING_GUIDE.md](docs-ja/reference/RST_TROUBLESHOOTING_GUIDE.md)** - RSTエラー解決ガイド
- **[docs-ja/reference/TRANSLATION_ROADMAP.md](docs-ja/reference/TRANSLATION_ROADMAP.md)** - 翻訳ロードマップ
- **[docs-ja/reference/TRANSLATION_PROGRESS.md](docs-ja/reference/TRANSLATION_PROGRESS.md)** - 翻訳進捗状況

### 翻訳支援スクリプト

#### 翻訳進捗チェッカー

全てのRSTファイルをスキャンし、翻訳の完了状況を確認します。

```bash
# 進捗レポートを生成
python docs/scripts/check_translation_progress.py

# レポートを確認
cat TRANSLATION_PROGRESS.md
```

**機能:**
- 255個の全RSTファイルを自動スキャン
- 英語が残っている箇所を検出（文中・文末の混在も検出）
- 完了率と詳細な問題箇所を`TRANSLATION_PROGRESS.md`に出力

#### ファイル検索ツール

翻訳ステータスに基づいてファイルを検索します。

```bash
# 翻訳完了ファイルの数を表示
python docs/scripts/find_files_by_status.py --status completed --count

# 部分的に翻訳されたファイルを問題数とともに表示
python docs/scripts/find_files_by_status.py --status partial --show-issues

# 特定ディレクトリ内の未翻訳ファイルを表示
python docs/scripts/find_files_by_status.py --status untranslated --directory programming_resources
```

詳細な使い方は [TRANSLATION_WORKFLOW_TOOLS.md](TRANSLATION_WORKFLOW_TOOLS.md) を参照してください。
