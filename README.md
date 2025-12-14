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

翻訳作業に関するすべてのドキュメントは **[docs-ja/](docs-ja/)** フォルダに整理されています。

### 🚀 翻訳を始める方へ

**[docs-ja/guides/AI_TRANSLATION_GUIDE.md](docs-ja/guides/AI_TRANSLATION_GUIDE.md)** 【最重要】
- AI翻訳ツール向けの統合ガイド
- 翻訳ルール、RST構文、エラー対策をすべて網羅
- **このガイドを読めば翻訳作業を開始できます** 👈 まずはこちら！

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
