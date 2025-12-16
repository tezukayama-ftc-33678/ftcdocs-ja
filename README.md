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

## 翻訳の編集方法

- **編集対象**: 翻訳は `locales/ja/LC_MESSAGES/*.po` を編集してください。`docs/build/gettext/*.pot` はビルド生成物のテンプレートであり、リポジトリでは追跡していません。
- PO ファイルの生成と更新 (ローカルまたは CI):
	- POT を生成: `make gettext` または `sphinx-build -b gettext docs/source docs/build/gettext`
	- PO を更新: `sphinx-intl update -p docs/build/gettext -l ja`
- 編集ツール: Poedit 等の PO エディタを推奨します。
- 翻訳をビルドに反映するには: `sphinx-intl build` または `msgfmt` を使って `.mo` を生成し、その後 `make html` を実行してください。

これにより翻訳ワークフローが安定します — POT は CI/ビルドで生成し、翻訳編集は `.po` のみ行ってください。
