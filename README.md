# FIRST Tech Challenge ドキュメントプロジェクト（日本語翻訳版）
=====================================================

![ビルド](https://readthedocs.com/projects/first-tech-challenge-ftcdocs/badge/?version=latest) ![リンクチェック](https://github.com/FIRST-Tech-Challenge/ftcdocs/actions/workflows/link-check.yaml/badge.svg)

本リポジトリは、 **FIRST Tech Challenge 公式ドキュメント**の非公式日本語翻訳プロジェクトです。

**🚀 すぐに始めたい方は**: [QUICKSTART.md](QUICKSTART.md) をご覧ください！

**📖 Read the Docsで公開したい方は**: [PUBLISHING.md](PUBLISHING.md) と [LICENSE_AND_LOGO_GUIDE.md](guides/LICENSE_AND_LOGO_GUIDE.md) をご覧ください！

---

## ⚠️ 非公式な翻訳と免責事項（重要）

**本プロジェクトは、FIRST Tech Challenge (FIRST®) の公式ドキュメントではありません。**

* この日本語翻訳は、日本のFTCコミュニティのために **[Team 33678 Tezukayama]** が自主的に運営・提供しているものです。
* 翻訳の正確性には努めていますが、**公式な情報源としては必ず英語のオリジナルドキュメントを参照してください。**
* 本翻訳の使用により生じたいかなる損害についても、本プロジェクトの貢献者および運営者は一切の責任を負いません。

公式ウェブサイト（英語原文）：
https://ftc-docs.firstinspires.org


---

## 🤖 ローカルLLMによる自動翻訳（推奨）

**VRAM 8GB以上のGPUがあれば、全自動で翻訳できます！**

### クイックスタート（3ステップ）

```powershell
# 1. LLMモデルをダウンロード
ollama pull qwen2.5:7b-instruct-q5_K_M

# 2. 依存パッケージをインストール
pip install ollama polib tqdm colorama

# 3. 自動翻訳開始（放置で完了）
python tools/translation/batch_translate.py --po-dir locales/ja/LC_MESSAGES
```

または、全自動スクリプトを実行：

```powershell
.\run_auto_translate.ps1
```

詳細は **[guides/AUTO_TRANSLATE.md](guides/AUTO_TRANSLATE.md)** を参照してください。

### テスト実行

環境が正しくセットアップされているか確認：

```powershell
python tools/translation/test_translation_env.py
```

---

## 📝 翻訳アプローチ

本プロジェクトでは、**2つの翻訳アプローチ**を組み合わせています：

### 1. 自動翻訳 (.po ファイル) - ほとんどのページ

- **編集対象**: `locales/ja/LC_MESSAGES/*.po` ファイル
- **利点**: 大量のページを効率的に翻訳可能
- **編集方法**: Poedit 等の PO エディタを推奨

### 2. 手動翻訳 (RST ファイル直接編集) - 重要なページ

以下のページは構造を確実に維持するため、RST ファイルを直接翻訳しています：

- **トップページ**: `docs/source/index.rst`
- **新規チーム**: `docs/source/persona_pages/rookie_teams/rookie_teams.rst`
- **既存チーム**: `docs/source/persona_pages/veteran_teams/veteran_teams.rst`
- **コーチ**: `docs/source/persona_pages/coach_admin/coach_admin.rst`
- **メンター**: `docs/source/persona_pages/mentor_tech/mentor_tech.rst`

**詳細**: [guides/TRANSLATION_APPROACH.md](guides/TRANSLATION_APPROACH.md) を参照してください。

### ビルド方法

```bash
cd docs
make html-ja  # 日本語版をビルド
```

### 翻訳品質チェック

```bash
# 翻訳品質をチェック
python tools/quality/translation_quality_checker.py --check

# 自動修正を実行
python tools/quality/translation_quality_checker.py --fix

# 詳細レポート生成
python tools/quality/translation_quality_checker.py --report
```

詳細は **[guides/QUALITY_CHECKER_GUIDE.md](guides/QUALITY_CHECKER_GUIDE.md)** を参照してください。

---

## 📚 ドキュメント構成

### ユーザー向けガイド
- **[QUICKSTART.md](QUICKSTART.md)** - 5分で始めるクイックスタート
- **[guides/](guides/)** - 詳細なガイド集
  - [AUTO_TRANSLATE.md](guides/AUTO_TRANSLATE.md) - 自動翻訳実行ガイド
  - [QUALITY_CHECKER_GUIDE.md](guides/QUALITY_CHECKER_GUIDE.md) - 翻訳品質チェックガイド ⭐ NEW
  - [BUILD_JA.md](guides/BUILD_JA.md) - ビルドガイド
  - [TRANSLATION_GUIDE.md](guides/TRANSLATION_GUIDE.md) - 翻訳ガイドライン
  - [GLOSSARY.md](guides/GLOSSARY.md) - 用語集
  - [ERROR_FIX_GUIDE.md](guides/ERROR_FIX_GUIDE.md) - エラー修正ガイド
  - [PO_SYNTAX_FIX_GUIDE.md](guides/PO_SYNTAX_FIX_GUIDE.md) - PO構文修正ガイド
  - その他多数...

### ツール
- **[tools/](tools/)** - 翻訳・修正・分析ツール集
  - [translation/](tools/translation/) - 自動翻訳ツール
  - [quality/](tools/quality/) - 翻訳品質チェックツール ⭐ NEW
  - [po-fixing/](tools/po-fixing/) - PO修正ツール
  - [analysis/](tools/analysis/) - 分析ツール
  - 詳細は [tools/README.md](tools/README.md) を参照

### プロジェクト資料
- **[docs/project-docs/](docs/project-docs/)** - プロジェクト内部資料
  - [archived/](docs/project-docs/archived/) - 過去のレポート
  - [reports/](docs/project-docs/reports/) - 現在のレポート
