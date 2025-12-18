# 翻訳修正ワークフロー

## 📊 現状
✅ 翻訳完了（全 PO ファイル）
✅ 正規化完了（改行・空白削除）
✅ ビルド完了（html-ja 634 警告）
✅ 品質チェック完了（293 問題検出）

## 🎯 残タスク：3 ステップ

### **ステップ 1：問題の自動修正（LLM + スクリプト）**

**実行コマンド：**
```powershell
cd h:\ftcdocs-ja\docs
python scripts/fix_po_with_llm.py --issues ../po_issues.json --types emphasis_mismatch inconsistent_ref missing_doc_ref --limit 1000
```

**何をやるか：**
- po_issues.json の問題 1000 件を LLM で修正
- msgstr に `**`（強調）と URL/参照を復元
- Sphinx マークアップ（`:doc:`, `:ref:` など）を保持
- 各修正を quality check で検証
- PO ファイルに書き戻し

**実行時間：** 20-30 分（Ollama + 8GB VRAM）

---

### **ステップ 2：修正後の品質確認**

**実行コマンド：**
```powershell
cd h:\ftcdocs-ja\docs
python scripts/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues_after_fix.json --verbose
```

**何をするか：**
- 修正後の問題件数を確認
- 改善率をチェック

**期待値：**
- emphasis_mismatch：257 → 50 以下
- inconsistent_ref：31 → 5 以下
- missing_doc_ref：5 → 0

---

### **ステップ 3：日本語ビルド + 構造確認**

**実行コマンド：**
```powershell
cd h:\ftcdocs-ja\docs
make clean
make html
make html-ja
python scripts/compare_build_structures.py
```

**何をするか：**
- 修正後の日本語ドキュメント生成
- 英語との構造差を最終確認
- 警告数を集計

**期待値：**
- 警告数が 634 から 200 以下に削減

---

## 🔄 ステップ実行例

```powershell
# 全ステップを自動実行したい場合：
cd h:\ftcdocs-ja

# LLM 修正 → 品質チェック → ビルド
docs\scripts\fix_po_with_llm.py --issues po_issues.json --types emphasis_mismatch inconsistent_ref missing_doc_ref --limit 1000
docs\scripts\check_and_fix_po.py --po-dir locales/ja/LC_MESSAGES --output po_issues_after_fix.json --verbose
cd docs
make clean
make html
make html-ja
python scripts/compare_build_structures.py
```

---

## 📝 問題タイプ別の修正内容

| 問題型 | 数 | 修正内容 | 難易度 |
|--------|-----|---------|--------|
| `emphasis_mismatch` | 257 | msgstr に `**...**` を追加 | ⭐ 低 |
| `inconsistent_ref` | 31 | msgstr に URL/`:doc:` を追加 | ⭐⭐ 中 |
| `missing_doc_ref` | 5 | `:doc:` リンク追加 | ⭐⭐ 中 |

---

## ⚡ クイックスタート（推奨）

**1. LLM 修正を実行：**
```powershell
cd h:\ftcdocs-ja\docs
python scripts/fix_po_with_llm.py --issues ../po_issues.json --types emphasis_mismatch inconsistent_ref missing_doc_ref --limit 1000
```

**2. ビルド＆確認：**
```powershell
make clean && make html && make html-ja
python scripts/compare_build_structures.py
```

**3. 修正前後の問題数を比較：**
```powershell
python scripts/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues_after_fix.json --verbose
```

---

## 💾 スクリプト一覧

| スクリプト | 用途 | 実行時間 |
|-----------|------|---------|
| `fix_po_with_llm.py` | LLM で msgstr 修正 | 20-30分 |
| `check_and_fix_po.py` | 品質チェック | 1-2分 |
| `normalize_po_whitespace.py` | 改行・空白削除 | 1分 |
| `compare_build_structures.py` | ビルド構造差分 | 10秒 |

---

## 🚀 実行開始

**最初にやること：**
```powershell
cd h:\ftcdocs-ja\docs
python scripts/fix_po_with_llm.py --issues ../po_issues.json --types emphasis_mismatch inconsistent_ref missing_doc_ref --limit 1000
```

実行中に進捗が表示されます。完了後にビルドします。
