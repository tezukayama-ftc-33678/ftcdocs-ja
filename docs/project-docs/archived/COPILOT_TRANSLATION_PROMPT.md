# GitHub Copilot で翻訳PRを出すときの共通プロンプト（ガイド）

このリポジトリでLLMを使って翻訳作業を行う際の注意点と、事前・事後チェック手順のプロンプト例をまとめています。Copilot/GPTに投げる前に、この内容を貼り付け・指示してください。

## よくあるLLMのミス（今回実際に発生した/要注意）
- `:doc:` 参照の欠落による **WARNING: inconsistent term references**（例: msgidに`:doc:`があるのにmsgstrで消える）
- ボタン/カードのラベルをリンク付きに書き換えてUI崩壊（sphinx-designのbutton-refはリンクを持つので、翻訳はラベルだけ）
- 外部リンク(URL)を削除してしまう
- msgidの改行/連結を勝手に変えて、msgstrとの対応が崩れる（長文msgidを分割しない）
- 空の `msgstr` を生成して未翻訳を増やす

**回避策:**
- `fix_po_auto.py --dry-run` で自動修正内容を事前確認
- `detect_untranslated_simple.py` で未翻訳英語の残存を確認
- GLOSSARY.mdから自動取得した訳語を使用（統一性を確保）
- ビルド警告を確認（missing_doc_ref は自動修正対象）

## プロンプトに必ず含める指示（テンプレ）
- **参照保持**: msgidにある`:doc:`や外部リンク(http/https)はmsgstrにも必ず残す。
- **ボタンの翻訳**: sphinx-designのbutton系はリンクを翻訳しない。ラベルだけ訳し、URL/参照は触らない。
- **構造保持**: msgidの改行・スペースは極力崩さない。長文msgidを分割しない。
- **空訳禁止**: 不要な空msgstrを作らない。
- **技術用語**: API名・製品名は英語のまま表記。専門用語は原文踏襲、固有名詞は訳さない。
- **品質チェック**: 翻訳後にスクリプトで検証（下記手順）。

### Copilotに渡す例文
```
あなたはSphinxドキュメントのPO翻訳校正者です。以下を厳守して翻訳/修正してください:

【重要な制約】
- msgidに含まれる`:doc:`参照、外部リンク、RSTマークアップをmsgstrでも必ず保持する
- sphinx-designのbutton/cardはラベルのみ翻訳し、リンク部分は変更しない
- 長いmsgidを分割しない。空のmsgstrを作らない
- API名・製品名は英語のまま表記（OpMode, LinearOpMode, HuskyLens, AprilTag等）
- 専門用語・固有名詞は原文を尊重する

【推奨】
修正後は以下を実行してください:
  1. python scripts/fix_po_auto.py --dry-run  # 修正候補の確認
  2. python scripts/fix_po_auto.py  # 自動修正
  3. make clean && make html-ja  # ビルド確認

【GLOSSARY.md連携】
以下の用語辞書に基づいて翻訳してください（GLOSSARY.md参照）:
- 英語保持: OpMode, LinearOpMode, Blocks, OnBot Java, Android Studio, FIRST, AprilTag等
- 翻訳語: Team→チーム, Coach→コーチ, Robot→ロボット, Competition→競技, Game Manual→競技マニュアル等

出力はPOのmsgstrのみを示し、説明は不要。
```

## スクリプトを使ったチェック・修正手順

### 1. 自動修正スクリプト（推奨フロー）
GLOSSARY.mdの用語集と連携して、未翻訳箇所を自動修正します。

```powershell
cd docs\scripts

# ドライラン（修正内容のプレビュー）
python fix_po_auto.py --dry-run

# 実際に修正
python fix_po_auto.py

# 特定ファイルのみ修正
python fix_po_auto.py --file persona_pages/rookie_teams/rookie_teams.po
```

**修正内容:**
- msgstr空白 → GLOSSARY.mdから自動翻訳
- 複合語優先マッチング（Game Manual → 競技マニュアル）
- パターンマッチング（Next → 次へ、etc）
- 194エントリを76ファイルで一括修正（実績）

詳細は `docs/scripts/README_AUTO_FIX.md` を参照。

### 2. 未翻訳英語の検出
HTMLビルドから未翻訳の英語を検出します。

```powershell
cd docs\scripts

# HTMLスキャン
python detect_untranslated_simple.py

# 結果確認（untranslated_report.json）
```

### 3. PO検証スクリプト（従来の手動チェック）
missing_doc_ref や emphasis_mismatch を詳細確認する場合：

```powershell
cd docs
python scripts/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues.json --verbose
```

- missing_doc_ref を優先修正（:doc: を戻す）
- 修正後の再チェック:
  ```powershell
  python scripts/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues_fixed.json
  ```

### 4. ビルド確認（警告数を確認）
```powershell
cd docs
make clean
make html-ja
```

**期待値:**
- 修正前: 11個の警告
- 修正後: 2個の警告（79%削減）

## 具体的な警告例（再発防止リスト）
- `WARNING: inconsistent term references in translated message.` → :doc: をmsgstrで落とした。
- `WARNING: unknown document: ...` → リンクを翻訳してパスが消失/改変。

## PR前のチェックリスト
- [ ] `python scripts/fix_po_auto.py --dry-run` で修正候補を確認
- [ ] `python scripts/fix_po_auto.py` で自動修正を実行
- [ ] `python scripts/detect_untranslated_simple.py` で残存する未翻訳英語を確認
- [ ] `python scripts/check_and_fix_po.py ...` で詳細な警告を確認（必要時）
- [ ] missing_doc_ref を優先修正（:doc: を戻す）
- [ ] `make clean && make html-ja` で警告数を確認（79%削減が目安）
- [ ] 重要ページ（index, persona_pages, gp等）のUI崩れがないかブラウザで目視

## 参照
- **自動修正ツール**: `docs/scripts/README_AUTO_FIX.md`（GLOSSARY.md連携、194エントリ修正実績）
- **未翻訳検出ツール**: `docs/scripts/README_DETECTION.md`（HTML英語検出）
- **用語辞書**: `GLOSSARY.md`（100+ エントリ、API名・専門用語の訳語統一）
- **PO検証ツール**: `docs/scripts/check_and_fix_po.py`（詳細な警告確認）
- **ビルド手順**: `BUILD_JA.md`
