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

## 🤖 ローカルLLMによる自動翻訳（推奨）

**VRAM 8GB以上のGPUがあれば、全自動で翻訳できます！**

### クイックスタート（3ステップ）

```powershell
# 1. LLMモデルをダウンロード
ollama pull qwen2.5:7b-instruct-q5_K_M

# 2. 依存パッケージをインストール
pip install ollama polib tqdm colorama

# 3. 自動翻訳開始（放置で完了）
python batch_translate.py --po-dir locales/ja/LC_MESSAGES
```

または、全自動スクリプトを実行：

```powershell
.\run_auto_translate.ps1
```

詳細は **[AUTO_TRANSLATE.md](AUTO_TRANSLATE.md)** を参照してください。

### テスト実行

環境が正しくセットアップされているか確認：

```powershell
python test_translation_env.py
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

**詳細**: [TRANSLATION_APPROACH.md](TRANSLATION_APPROACH.md) を参照してください。

### ビルド方法

```bash
cd docs
make html-ja  # 日本語版をビルド
```

---

## 🔍 翻訳問題トラッカー

人力での問題修正を支援するため、ブラウザベースの問題トラッカーを提供しています。

### 使い方

1. ドキュメントをビルド: `cd docs && make html-ja`
2. 問題トラッカーを開く: `docs/build/html-ja/_static/issue_tracker.html`
3. ドキュメントを読みながら、おかしい箇所を記録
4. JSON または Markdown 形式でエクスポート

**詳細**: [ISSUE_TRACKER_GUIDE.md](ISSUE_TRACKER_GUIDE.md) を参照してください。

---

## 📚 ドキュメント

- **[TRANSLATION_APPROACH.md](TRANSLATION_APPROACH.md)** - 翻訳アプローチの詳細説明
- **[ISSUE_TRACKER_GUIDE.md](ISSUE_TRACKER_GUIDE.md)** - 問題トラッカーの使用方法
- **[AUTO_TRANSLATE.md](AUTO_TRANSLATE.md)** - 自動翻訳の詳細（もし存在する場合）
