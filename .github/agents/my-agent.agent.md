---
# Fill in the fields below to create a basic custom agent for your repository.
# The Copilot CLI can be used for local testing: https://gh.io/customagents/cli
# To make this agent available, merge this file into the default repository branch.
# For format details, see: https://gh.io/customagents/config

name:Translation-ja
description:翻訳用
---

# My Agent
このリポジトリでLLMを使って翻訳作業を行う際の注意点と、事前・事後チェック手順のプロンプト例をまとめています。Copilot/GPTに投げる前に、この内容を貼り付け・指示してください。

## よくあるLLMのミス（今回実際に発生した/要注意）
- `:doc:` 参照の欠落による **WARNING: inconsistent term references**（例: msgidに`:doc:`があるのにmsgstrで消える）
- 強調マーカー `**...**` の不一致（片側だけで **inline strong start-string without end-string**）
- ボタン/カードのラベルをリンク付きに書き換えてUI崩壊（sphinx-designのbutton-refはリンクを持つので、翻訳はラベルだけ）
- 外部リンク(URL)を削除してしまう
- msgidの改行/連結を勝手に変えて、msgstrとの対応が崩れる（長文msgidを分割しない）
- 空の `msgstr` を生成して未翻訳を増やす

## プロンプトに必ず含める指示（テンプレ）
- **参照保持**: msgidにある`:doc:`や外部リンク(http/https)、強調`**...**`はmsgstrにも必ず残す。
- **ボタンの翻訳**: sphinx-designのbutton系はリンクを翻訳しない。ラベルだけ訳し、URL/参照は触らない。
- **構造保持**: msgidの改行・スペースは極力崩さない。長文msgidを分割しない。
- **空訳禁止**: 不要な空msgstrを作らない。
- **技術用語**: 専門用語は原文踏襲、固有名詞は訳さない。(GLOSSARY.mdを参照)
- **品質チェック**: 翻訳後にスクリプトで検証（下記手順）。

### Copilotに渡す例文
```
あなたはSphinxドキュメントのPO翻訳校正者です。以下を厳守して翻訳/修正してください:
- msgidに含まれる`:doc:`参照、外部リンク、`**...**`強調をmsgstrでも必ず保持する
- sphinx-designのbutton/cardはラベルのみ翻訳し、リンク部分は変更しない
- 長いmsgidを分割しない。空のmsgstrを作らない
- 専門用語・固有名詞は原文を尊重する
出力はPOのmsgstrのみを示し、説明は不要。
```

## スクリプトを使ったチェック手順
- ルートで実行する場合:
  ```powershell
  cd h:\ftcdocs-ja\docs
  python scripts/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues.json --verbose
  ```
- missing_doc_ref や emphasis_mismatch を確認し、必要に応じて手動修正。
- 修正後の再チェック:
  ```powershell
  python scripts/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues_fixed.json
  ```
- ビルド確認（警告数を確認）:
  ```powershell
  make clean
  make html-ja
  ```

## 具体的な警告例（再発防止リスト）
- `WARNING: inconsistent term references in translated message.` → :doc: をmsgstrで落とした。
- `WARNING: inline strong start-string without end-string.` → `**` ペア崩れ。
- `WARNING: unknown document: ...` → リンクを翻訳してパスが消失/改変。

## PR前のチェックリスト
- [ ] `python scripts/check_and_fix_po.py ...` で警告種類と件数を把握
- [ ] missing_doc_ref を優先修正（:doc: を戻す）
- [ ] emphasis_mismatch を修正（`**`のペア確認）
- [ ] make clean && make html-ja で警告数を確認
- [ ] 重要ページ（index, persona_pages, gp等）のUI崩れがないかブラウザで目視

## 参照
- ツールの詳細: [docs/scripts/README.md](docs/scripts/README.md)
- ビルド手順: [BUILD_JA.md](BUILD_JA.md)
- 用語一覧: [GLOSSARY.md](GLOSSARY.md)
