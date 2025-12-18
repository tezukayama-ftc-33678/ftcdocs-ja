# 📋 修正ワークフロー完全解説

## 🎯 現在のフェーズ

**フェーズ 2: 修正作業（実行開始）**

- ✅ 翻訳完了（全 256 PO ファイル）
- ✅ 正規化完了（改行・空白削除）
- ✅ 品質チェック完了（293 問題抽出）
- 🔄 **修正作業開始（LLM + スクリプト自動実行）**
- ⏳ ビルド＆確認（修正完了後）

---

## 📊 実行中のワークフロー内容

### **ステップ 1️⃣: LLM で PO を修正（進行中）**

**対象：** 293 件の問題を最大 1000 件まで処理

**修正内容：**
1. **emphasis_mismatch（257 件）**
   - msgstr に不足している `**...**` を復元
   - 例）msgid: `"**bold text**"` → msgstr: `"**太字テキスト**"`

2. **inconsistent_ref（31 件）**
   - msgstr に不足している URL や `:doc:` / `:ref:` を復元
   - 例）msgid: `:doc:\`page\`` → msgstr: `:doc:\`ページ\``

3. **missing_doc_ref（5 件）**
   - `:doc:` リンクの欠落を修正

**処理方法：**
- 各問題の msgid/msgstr を抽出
- LLM で修正案を生成（Ollama + qwen2.5:7b or gemma2:9b）
- 簡易品質チェック（参照数が一致するか）
- PO ファイルに書き戻し

**実行時間：** 15-20 分

---

### **ステップ 2️⃣: 品質チェック（修正前後を比較）**

**出力ファイル：** `po_issues_after_fix.json`

**期待値：**
- emphasis_mismatch：257 → 30 以下
- inconsistent_ref：31 → 3 以下
- missing_doc_ref：5 → 0

---

### **ステップ 3️⃣: ビルド（make html + html-ja）**

**処理：**
```bash
make clean
make html      # 英語
make html-ja   # 日本語
```

**期待値：**
- 警告数：634 → 200 以下

---

### **ステップ 4️⃣: 構造比較**

**出力ファイル：** `docs/build/build_structure_diff.txt`

**内容：**
- html と html-ja の差分ファイル一覧
- `.doctrees/` キャッシュは除外（無視可）

---

## ⏱️ スケジュール

| ステップ | 処理時間 | 状態 |
|---------|--------|------|
| 1️⃣ LLM 修正 | 15-20 分 | 🔄 進行中 |
| 2️⃣ 品質チェック | 1-2 分 | ⏳ 待機中 |
| 3️⃣ ビルド | 10-15 分 | ⏳ 待機中 |
| 4️⃣ 構造比較 | 10 秒 | ⏳ 待機中 |

**合計時間：** 30-40 分

---

## 📂 出力ファイル

修正完了後に確認するファイル：

```
h:\ftcdocs-ja\
├── po_issues.json              # 修正前の問題（293 件）
├── po_issues_after_fix.json    # 修正後の問題（期待：50 以下）
├── docs\
│   └── build\
│       ├── html\               # 英語 HTML
│       ├── html-ja\            # 日本語 HTML ✅
│       └── build_structure_diff.txt   # 差分レポート
```

---

## ✅ 修正完了後の確認方法

### **1. 問題件数の改善確認**

```python
import json

# 修正前
with open('po_issues.json') as f:
    before = json.load(f)
    
# 修正後
with open('po_issues_after_fix.json') as f:
    after = json.load(f)

print(f"修正前: {len(before)} 件")
print(f"修正後: {len(after)} 件")
print(f"改善: {len(before) - len(after)} 件削減 ({100*(len(before)-len(after))/len(before):.1f}%)")
```

### **2. 問題タイプ別の改善**

```python
before_types = {}
for issue in before:
    t = issue['type']
    before_types[t] = before_types.get(t, 0) + 1

after_types = {}
for issue in after:
    t = issue['type']
    after_types[t] = after_types.get(t, 0) + 1

for issue_type in before_types:
    b = before_types.get(issue_type, 0)
    a = after_types.get(issue_type, 0)
    print(f"{issue_type}: {b} → {a} ({b-a} 削減)")
```

### **3. ビルド警告数の確認**

```bash
# 修正前
# → ビルド 成功, 634 警告

# 修正後
cd h:\ftcdocs-ja\docs
make html 2>&1 | grep -i "警告\|warning" | tail -1
make html-ja 2>&1 | grep -i "警告\|warning" | tail -1
```

### **4. 日本語 HTML の動作確認**

```bash
# ブラウザで開く
start docs\build\html-ja\index.html
```

---

## 🔧 修正スクリプトの詳細

### **fix_po_with_llm.py**

**役割：** LLM を使用して PO ファイルの msgstr を修正

**処理フロー：**
```
1. po_issues.json を読み込み
2. 各問題に対して：
   a. PO ファイルから該当行の msgid/msgstr を抽出
   b. LLM に修正案を問い合わせ
   c. 簡易品質チェック（参照数が一致するか）
   d. 通過した場合のみ PO ファイルに書き戻し
3. 修正内容をログに記録
```

**制約事項：**
- `:doc:`, `:ref:` の数は必ず保持
- `**...**` の数は必ず保持
- 外部リンク `<URL>`__ の数は必ず保持
- sphinx-design リンク `{doc}` は変更しない

---

## 🎓 何が起こっているか（技術詳細）

### **元の問題：LLM 翻訳の不完全性**

1. **強調が消える**
   - 英語：`"**Connection pool**"`
   - LLM 翻訳：`"接続プール"` ← `**` がない ❌
   - 修正後：`"**接続プール**"` ✅

2. **リンクが消える**
   - 英語：`"See :doc:\`guide\`"`
   - LLM 翻訳：`"ガイドを参照"` ← `:doc:` がない ❌
   - 修正後：`"`:doc:\`ガイド\`` を参照"` ✅

3. **URL が消える**
   - 英語：`"Visit <https://example.com>`__"`
   - LLM 翻訳：`"例.comを訪問"` ← URL がない ❌
   - 修正後：`"<https://example.com>`__ を訪問"` ✅

### **修正戦略**

LLM に「英語版を見ながら日本語を修正してほしい」と指示：

```
【指示】
msgid（英語原文）: "See **important** info in :doc:\`guide\`"
msgstr（日本語翻訳）: "ガイドの重要情報を見て"

このmsgstrに以下を追加してください：
1. msgidに存在する ** 強調を復元
2. msgidに存在する :doc: 参照を復元
3. 日本語として自然に読める形に

【期待される修正】
msgstr: "**重要な**情報を :doc:\`ガイド\` で確認してください"
```

このプロセスを 293 件分、自動で繰り返す。

---

## 🚀 ワークフロー実行中

現在、以下が自動実行中です：

```
[████████░░░░░░░░] ステップ 1️⃣  LLM 修正: ~50%
                  ステップ 2️⃣  品質チェック: 待機中
                  ステップ 3️⃣  ビルド: 待機中
                  ステップ 4️⃣  構造比較: 待機中
```

**推定残り時間：** 15-20 分

完了後に自動的に出力ファイルが生成されます。

---

## 📞 トラブル時の対応

### **LLM が応答しない**

```powershell
# Ollama の状態を確認
ollama list
ollama ps

# モデルが見つからない場合、プル
ollama pull qwen2.5:7b-instruct-q5_K_M

# 再度実行
python docs\scripts\fix_po_with_llm.py --issues po_issues.json --limit 100
```

### **ビルドが失敗**

```powershell
cd h:\ftcdocs-ja\docs

# 依存関係を再インストール
pip install -r requirements.txt

# キャッシュを削除して再ビルド
make clean
make html
make html-ja
```

---

## 📝 次のステップ（修正完了後）

1. **修正前後の問題件数を比較**
   ```python
   python -c "
   import json
   before = len(json.load(open('po_issues.json')))
   after = len(json.load(open('po_issues_after_fix.json')))
   print(f'修正前: {before} → 修正後: {after} ({before-after}件削減)')
   "
   ```

2. **手動修正が必要な項目を特定**
   - po_issues_after_fix.json を確認
   - 残った問題について、PO ファイルを直接編集

3. **最終ビルドと公開**
   - 修正完了後、docs/build/html-ja/ を本番に配置
   - 英語版と日本語版の整合性を確認

---

## 🎉 完了！

ワークフロー完了後、以下のファイルが利用可能になります：

✅ **日本語ドキュメント HTML**
   - `docs/build/html-ja/index.html`
   - すべてのリンク、強調、参照が適切に翻訳＋修正済み

✅ **修正ログ**
   - `po_issues_after_fix.json`
   - 修正結果の詳細

✅ **構造確認**
   - `docs/build/build_structure_diff.txt`
   - 英語版との差分確認

---

**お疲れ様でした！**
