# .po Translation - クイックリファレンス

## 📖 はじめに読むドキュメント

```
まずはこれを読む:
├── MIGRATION_SUMMARY.md      ← 全体像を把握
├── WHY_PO_TRANSLATION.md     ← なぜ移行するのか
└── COMPARISON_OLD_VS_NEW.md  ← 従来との違い

次にこれを読む:
└── MIGRATION_NEXT_STEPS.md   ← 何をすべきか

実行するとき:
├── PO_TRANSLATION_WORKFLOW.md ← 日常のワークフロー
└── MIGRATION_TO_PO_GUIDE.md   ← 技術的な詳細
```

## ⚡ クイックスタート

### テストしてみる（15分）

```bash
# 1. 上流を追加
git remote add upstream https://github.com/FIRST-Tech-Challenge/ftcdocs.git
git fetch upstream

# 2. 1ファイルを英語に戻す
git checkout upstream/main -- docs/source/index.rst

# 3. POTとPOを生成
cd docs
make gettext && make ja-update

# 4. 翻訳（エディタで開く）
vim locale/ja/LC_MESSAGES/index.po

# 5. ビルド
make ja-build

# 6. 確認
python -m http.server 8000 --directory build/html/ja
```

## 🎯 Make コマンド

```bash
# POTファイル生成（英語から翻訳可能文字列を抽出）
make gettext

# POファイル更新（POTの変更をPOに反映）
make ja-update

# 日本語版ビルド
make ja-build

# 翻訳統計
make ja-stats

# 組み合わせ
make gettext && make ja-update && make ja-build
```

## 📝 POファイルの編集

### 基本構造

```po
#: index.rst:10
msgid "English text"
msgstr "日本語テキスト"
```

### 状態の意味

| 状態 | 意味 | 対応 |
|------|------|------|
| `msgstr ""` | 未翻訳 | 翻訳する |
| `msgstr "text"` | 翻訳済み | OK |
| `#, fuzzy` | 要確認 | 確認して更新 |
| `#~ msgid` | 削除済み | 無視/削除 |

### 翻訳のルール

```po
# 技術用語は太字で英語
msgid "Create an OpMode"
msgstr "**OpMode** を作成します"

# コードは翻訳しない（自動でスキップ）

# マークアップを保持
msgid "See :doc:`intro` for details"
msgstr "詳細は :doc:`入門 <intro>` を参照"
```

## 🛠️ 推奨ツール

### Poedit（初心者向け）
```
無料のGUIエディタ
ダウンロード: https://poedit.net/
```

### VS Code（開発者向け）
```
i18n Ally 拡張機能をインストール
```

### テキストエディタ
```
vim, nano, VS Codeなど
POファイルはプレーンテキスト
```

## 🔄 日常のワークフロー

### 上流の変更を取り込む

```bash
# 1. マージ
git fetch upstream
git merge upstream/main

# 2. 更新
cd docs
make gettext && make ja-update

# 3. 変更を確認
make ja-stats

# 4. 翻訳
# fuzzyマークや空のmsgstrを探して翻訳

# 5. ビルド
make ja-build

# 6. コミット
git add locale/ja/
git commit -m "翻訳: 上流の変更を反映"
```

### 新しいページを翻訳

```bash
# 1. POT/PO更新
make gettext && make ja-update

# 2. 新しいPOファイルを編集
vim locale/ja/LC_MESSAGES/new_page.po

# 3. ビルド
make ja-build
```

## 📊 進捗確認

```bash
# 全体の統計
make ja-stats

# 特定ファイル
msgfmt --statistics locale/ja/LC_MESSAGES/index.po

# 未翻訳を探す
grep -r 'msgstr ""' locale/ja/LC_MESSAGES/

# fuzzyを探す
grep -r 'fuzzy' locale/ja/LC_MESSAGES/
```

## 🆘 トラブルシューティング

### POTファイルが生成されない

```bash
# クリーンビルド
cd docs
make clean
make gettext
```

### POファイルが更新されない

```bash
# POTを再生成してから更新
make gettext
make ja-update
```

### 翻訳が反映されない

```bash
# クリーンビルド
make clean
make ja-build

# ブラウザのキャッシュをクリア
```

### POファイルの構文エラー

```bash
# 検証
msgfmt -c locale/ja/LC_MESSAGES/index.po

# エラー箇所を表示
msgfmt -c -v locale/ja/LC_MESSAGES/index.po
```

## 📁 ファイル構成

```
docs/
├── source/                    ← 英語RST（上流と同期）
│   ├── index.rst
│   └── ...
│
├── locale/ja/LC_MESSAGES/     ← 日本語翻訳
│   ├── index.po
│   └── ...
│
└── build/
    ├── gettext/               ← POTファイル（自動生成）
    │   ├── index.pot
    │   └── ...
    └── html/ja/               ← 日本語HTML（ビルド結果）
```

## 🎓 POファイルの例

### 最小限の例

```po
# Translation of index.rst
msgid ""
msgstr ""
"Language: ja\n"
"MIME-Version: 1.0\n"
"Content-Type: text/plain; charset=UTF-8\n"

#: index.rst:5
msgid "Welcome"
msgstr "ようこそ"
```

### 実践的な例

```po
# 通常の翻訳
#: tutorial.rst:10
msgid "This is a tutorial for beginners."
msgstr "これは初心者向けのチュートリアルです。"

# 技術用語を含む
#: tutorial.rst:15
msgid "Create a new OpMode"
msgstr "新しい **OpMode** を作成します"

# 複数行
#: tutorial.rst:20
msgid ""
"This is a long paragraph that spans "
"multiple lines in the source."
msgstr ""
"これは複数行にわたる "
"長い段落です。"

# fuzzy（要確認）
#: tutorial.rst:25
#, fuzzy
msgid "Updated text from upstream"
msgstr "古い翻訳"

# 未翻訳
#: tutorial.rst:30
msgid "New section added"
msgstr ""
```

## 🔗 リンク集

### このリポジトリ

- [MIGRATION_SUMMARY.md](MIGRATION_SUMMARY.md) - 完了サマリー
- [COMPARISON_OLD_VS_NEW.md](COMPARISON_OLD_VS_NEW.md) - 詳細比較
- [WHY_PO_TRANSLATION.md](WHY_PO_TRANSLATION.md) - 移行の理由
- [MIGRATION_NEXT_STEPS.md](MIGRATION_NEXT_STEPS.md) - 次のステップ
- [PO_TRANSLATION_WORKFLOW.md](PO_TRANSLATION_WORKFLOW.md) - ワークフロー
- [MIGRATION_TO_PO_GUIDE.md](MIGRATION_TO_PO_GUIDE.md) - 技術ガイド

### 外部リソース

- [Sphinx i18n](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)
- [sphinx-intl](https://sphinx-intl.readthedocs.io/)
- [Poedit](https://poedit.net/)
- [GNU gettext](https://www.gnu.org/software/gettext/manual/)

## 💬 よくある質問

**Q: 既存の翻訳は？**  
A: TRANSLATION_MAPPING.md に保存済み

**Q: 全部移行する必要は？**  
A: いいえ、段階的でもOK

**Q: 英語のままでもビルドできる？**  
A: はい、msgstrが空なら英語で表示

**Q: ツールは必須？**  
A: いいえ、テキストエディタだけでもOK

**Q: 複数人で翻訳できる？**  
A: はい、POファイルをGitで管理

## ⚡ チートシート

```bash
# 完全なワークフロー（コピー&ペースト可）
git fetch upstream && \
git merge upstream/main && \
cd docs && \
make gettext && \
make ja-update && \
make ja-stats
# ↑ ここで翻訳作業 ↓
make ja-build && \
cd .. && \
git add locale/ja/ && \
git commit -m "翻訳: 更新" && \
git push
```

---

**このリファレンスをブックマークしておくと便利です！**

質問？ → GitHub Issue で聞いてください！
