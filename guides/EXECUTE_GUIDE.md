# 🚀 実行ガイド：修正ワークフロー TLDR

## いますぐやること

現在、以下が自動実行中です：

```powershell
cd h:\ftcdocs-ja
python run_fix_workflow.py
```

**実行時間：** 30-40 分（放置でOK）

---

## 何をやってるのか（簡潔版）

| ステップ | 内容 | 時間 |
|---------|------|------|
| 1️⃣ | 293 件の PO 問題を LLM で修正（強調・リンク・参照） | 20 分 |
| 2️⃣ | 修正後の品質チェック（改善率を確認） | 2 分 |
| 3️⃣ | ビルド再実行（make html + html-ja） | 15 分 |
| 4️⃣ | 差分確認 | 1 分 |

---

## 修正対象（293 件）

✅ **emphasis_mismatch（257 件）**
- msgstr に不足している `**太字**` を復元

✅ **inconsistent_ref（31 件）**
- msgstr に不足している `:doc:` / `:ref:` / URL を復元

✅ **missing_doc_ref（5 件）**
- `:doc:` リンク欠落を修正

---

## 期待される改善

| 指標 | 修正前 | 修正後 | 削減率 |
|------|-------|--------|--------|
| 問題件数 | 293 | ~50 | ~83% |
| ビルド警告 | 634 | ~200 | ~69% |
| emphasis_mismatch | 257 | ~30 | ~88% |

---

## 完了後のファイル

```
h:\ftcdocs-ja\
├── po_issues_after_fix.json        ← 修正後の問題
├── docs\build\html-ja\            ← 日本語 HTML 📄
└── docs\build\build_structure_diff.txt  ← 差分確認用
```

---

## 完了後にやること

**1. 修正を確認**
```powershell
# 修正前後の比較
python -c "
import json
before = len(json.load(open('po_issues.json')))
after = len(json.load(open('po_issues_after_fix.json')))
print(f'{before} → {after} ({before-after} 件削減 {100*(before-after)/before:.0f}%)')
"
```

**2. ブラウザで日本語 HTML を開く**
```powershell
start docs\build\html-ja\index.html
```

**3. 手動修正が必要なら PO ファイルを編集**
```powershell
code locales/ja/LC_MESSAGES/path/to/file.po
```

---

## スクリプト説明

### **実行スクリプト**
- `run_fix_workflow.py` ← **これを実行中**
  - LLM修正 → 品質チェック → ビルド → 確認 を自動実行

### **各種スクリプト**
- `fix_po_with_llm.py` ← LLM で msgstr を修正（ステップ1）
- `check_and_fix_po.py` ← 品質チェック（ステップ2）
- `compare_build_structures.py` ← 構造比較（ステップ4）
- `normalize_po_whitespace.py` ← 改行・空白削除（既済）

---

## トラブルシューティング

### **Ollama が起動していない**
```powershell
# Windows Terminal で
ollama serve
```

### **スクリプトが固まった**
```powershell
# Ctrl+C で中断
# ワークフローを再実行（修正済みはスキップ）
python run_fix_workflow.py
```

### **ビルドエラー**
```powershell
cd h:\ftcdocs-ja\docs
pip install -r requirements.txt
make clean
make html
```

---

## 📚 詳細ドキュメント

| ドキュメント | 内容 |
|-----------|------|
| `FIX_WORKFLOW.md` | 修正ワークフロー全詳細 |
| `QUICK_FIX_GUIDE.md` | 実行ガイド + トラブル対応 |
| `WORKFLOW_EXPLANATION.md` | 技術詳細＋何が起こってるか |

---

## ✨ まとめ

**現在の状況：**
- 翻訳完了 ✅
- 正規化完了 ✅
- **修正作業実行中 🔄** ← ここ
- ビルド確認待機中 ⏳

**待つだけで以下が自動完了：**
- msgstr の強調・リンク・参照を復元
- PO ファイルを修正
- ビルドして警告を削減
- 修正結果を json で出力

**30 分後：** 日本語ドキュメント完成予定！

---

## 💾 実行ログ確認

```powershell
# ターミナルで進捗を見守る
python run_fix_workflow.py

# または別ターミナルで修正後の問題をチェック
Get-Content po_issues_after_fix.json | head -100
```

**お疲れ様でした！実行は進行中です。** ☕
