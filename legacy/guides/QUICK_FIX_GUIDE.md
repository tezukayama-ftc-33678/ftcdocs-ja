# 🚀 修正作業：クイックガイド

## 現在の状況

✅ **完了済み**
- 翻訳（全 PO ファイル）
- 正規化（改行・空白削除）
- ビルド（html-ja 634 警告）
- 品質チェック（293 問題検出）

❌ **残タスク**
- PO ファイル内の問題を修正（強調・リンク・参照）
- 修正後のビルド確認

---

## ⚡ 実行方法（2 つのオプション）

### **オプション A：統合実行（推奨）**

**1 コマンドで全ステップ実行：**

```powershell
cd h:\ftcdocs-ja
.\run_fix_workflow.ps1
```

**実行内容：**
- ✅ LLM で msgstr 修正（1000 件）
- ✅ 品質チェック（修正前後の問題件数を比較）
- ✅ ビルド（make html + html-ja）
- ✅ 構造比較（html vs html-ja）

**実行時間：** 30-40 分

**出力ファイル：**
- `po_issues_after_fix.json` → 修正後の問題件数
- `docs/build/html-ja/` → 日本語 HTML
- `docs/build/build_structure_diff.txt` → 構造差分

---

### **オプション B：ステップバイステップ（デバッグ用）**

各ステップを個別に実行して進捗を確認：

```powershell
cd h:\ftcdocs-ja\docs

# ステップ 1: LLM で PO を修正
python tools/po-fixing/fix_po_with_llm.py --issues ../po_issues.json --types emphasis_mismatch inconsistent_ref missing_doc_ref --limit 1000

# ステップ 2: 修正後の品質確認
python tools/po-fixing/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues_after_fix.json --verbose

# ステップ 3: ビルド
make clean && make html && make html-ja

# ステップ 4: 構造比較
python scripts/compare_build_structures.py
```

---

## 📊 修正内容の詳細

### **修正対象：293 件の問題**

| 問題型 | 件数 | 修正方法 | 例 |
|--------|-----|---------|-----|
| `emphasis_mismatch` | 257 | msgstr に `**...**` を追加 | msgid: `"**bold**"` → msgstr: `"**太字**"` |
| `inconsistent_ref` | 31 | msgstr に URL/`:doc:` を追加 | msgid: `:doc:\`reference\`` → msgstr: `:doc:\`参照\`` |
| `missing_doc_ref` | 5 | `:doc:` リンクを追加 | msgid: `:doc:\`page\`` → msgstr に同じ |

### **Sphinx マークアップ（自動保護）**

LLM 修正時に以下を自動保持：
- `:doc:`...`` ← ドキュメント参照
- `:ref:`...`` ← セクション参照  
- `<https://...>`__ ← 外部リンク
- `**...**` ← 強調（太字）

---

## ✨ 実行後の確認

### **1. 修正前後の比較**

```powershell
# 修正前のファイル
cat po_issues.json | grep '"type"' | wc -l
# → 出力: 293

# 修正後のファイル
cat po_issues_after_fix.json | grep '"type"' | wc -l
# → 期待値: 50 以下
```

### **2. ビルド警告数の確認**

```powershell
# 修正前: 634 警告
# 修正後: 期待値 200 以下
```

### **3. 構造差分の確認**

```powershell
cat docs/build/build_structure_diff.txt
```

期待値：
- `.doctrees/` ファイル（キャッシュ）のみ差分
- 実質的な HTML ファイルは同じ

---

## 🔍 トラブルシューティング

### **LLM 修正が遅い or 失敗**

```powershell
# Ollama が起動しているか確認
ollama list
# もし空なら、モデルをプル
ollama pull qwen2.5:7b-instruct-q5_K_M
```

### **品質チェックエラー**

```powershell
# 特定のPOファイルをチェック
python tools/po-fixing/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --verbose 2>&1 | grep -i error
```

### **ビルドが失敗**

```powershell
# Sphinx の依存関係を確認
cd docs
pip install -r requirements.txt
make html  # テスト
```

---

## 📝 手動修正が必要な場合

修正後も問題が残っている場合は、PO ファイルを直接編集：

```powershell
# VS Code で編集
code locales/ja/LC_MESSAGES/path/to/file.po

# PO ファイル形式:
# msgid "English text with **bold**"
# msgstr "日本語テキスト **太字付き**"
```

修正後、再度品質チェック：

```powershell
cd h:\ftcdocs-ja\docs
python tools/po-fixing/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues_final.json --verbose
make clean && make html-ja
```

---

## ✅ 完了の条件

- [ ] LLM 修正実行完了
- [ ] 修正前後の問題件数を確認（100+ 件削減）
- [ ] ビルド警告が 200 以下に削減
- [ ] 構造比較で実質的な差分なし

---

## 🎯 まとめ

**いますぐやること：**

```powershell
cd h:\ftcdocs-ja
.\run_fix_workflow.ps1
```

**30 分待つだけで、ほぼすべての修正が完了します！**
