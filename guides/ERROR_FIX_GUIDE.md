# 対処ガイド：残存ビルドエラーへの対応

## 現状分析

**修正前**: 293 件  
**修正後**: 346 件（増加）  
**原因**: LLM が一部の msgstr を悪化させた

## 対処戦略：3 ステップ

### **ステップ 1: 正規化（優先）**

正規化で簡単に直る問題を先に修正：

```powershell
cd h:\ftcdocs-ja\docs
python scripts/normalize_po_whitespace.py --po-dir ../locales/ja/LC_MESSAGES
```

**効果**: 改行・空白・文末クリーンアップで 50-100 件削減

---

### **ステップ 2: LLM 修正（段階的）**

問題を少数ずつ修正して検証：

```powershell
cd h:\ftcdocs-ja\docs

# ラウンド1: 最重要問題（missing_doc_ref）
python scripts/fix_po_with_llm.py --issues ../po_issues_after_fix.json --types missing_doc_ref --limit 10

# 正規化
python scripts/normalize_po_whitespace.py --po-dir ../locales/ja/LC_MESSAGES

# 品質チェック
python scripts/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues_round1.json --verbose

# ラウンド2: リンク切れ（inconsistent_ref）
python scripts/fix_po_with_llm.py --issues ../po_issues_round1.json --types inconsistent_ref --limit 50

# 正規化
python scripts/normalize_po_whitespace.py --po-dir ../locales/ja/LC_MESSAGES

# 品質チェック
python scripts/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues_round2.json --verbose

# ラウンド3: 強調（emphasis_mismatch）
python scripts/fix_po_with_llm.py --issues ../po_issues_round2.json --types emphasis_mismatch --limit 100

# 正規化
python scripts/normalize_po_whitespace.py --po-dir ../locales/ja/LC_MESSAGES

# 品質チェック
python scripts/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues_round3.json --verbose
```

**効果**: タイプ別に段階修正、各ラウンドで検証

---

### **ステップ 3: ビルド確認**

```powershell
cd h:\ftcdocs-ja\docs
make clean
make html
make html-ja
python scripts/compare_build_structures.py
```

---

## 優先度別の対処

### **最優先（手動修正推奨）**

#### 1. PO 構文エラー

```powershell
# エラー箇所を特定
python -c "
import polib
from pathlib import Path
errors = []
for po in Path('locales/ja/LC_MESSAGES').rglob('*.po'):
    try:
        polib.pofile(str(po))
    except Exception as e:
        errors.append((po, str(e)))
for p, e in errors:
    print(f'{p}: {e}')
"
```

**修正**: VS Code で該当 PO を開き、エスケープされていないクォートを修正

#### 2. missing_doc_ref（5 件）

ビルドエラーの直接原因。手動で確認：

```powershell
python -c "
import json
issues = json.load(open('po_issues_after_fix.json'))
for i in issues:
    if i['type'] == 'missing_doc_ref':
        print(f\"{i['file']}:{i['line']}\")
"
```

各ファイルを開いて `:doc:` リンクを追加。

---

### **高優先（LLM + 正規化）**

#### 3. inconsistent_ref（37 件）

URL や `:ref:` の欠落。LLM で修正可能：

```powershell
python docs/scripts/fix_po_with_llm.py --issues po_issues_after_fix.json --types inconsistent_ref --limit 40
python docs/scripts/normalize_po_whitespace.py --po-dir locales/ja/LC_MESSAGES
```

---

### **中優先（正規化のみでOK）**

#### 4. emphasis_mismatch（304 件）

多くは `**` の位置ズレ。正規化で改善可能。手動修正も簡単：

```
msgid "See **bold text**"
msgstr "**太字テキスト** を参照"
```

---

## 実行例（推奨フロー）

```powershell
cd h:\ftcdocs-ja

# 1. 正規化
python docs/scripts/normalize_po_whitespace.py --po-dir locales/ja/LC_MESSAGES

# 2. 品質チェック
python docs/scripts/check_and_fix_po.py --po-dir locales/ja/LC_MESSAGES --output po_issues_clean.json --verbose

# 3. 問題数を確認
python -c "import json; print(f'{len(json.load(open(\"po_issues_clean.json\")))} 件')"

# 4. missing_doc_ref を手動修正（5件のみ）
# → VS Code で該当ファイルを開いて :doc: を追加

# 5. inconsistent_ref を LLM で修正
python docs/scripts/fix_po_with_llm.py --issues po_issues_clean.json --types inconsistent_ref --limit 50

# 6. 再正規化
python docs/scripts/normalize_po_whitespace.py --po-dir locales/ja/LC_MESSAGES

# 7. 最終ビルド
cd docs
make clean && make html && make html-ja
```

---

## 期待される改善

| ステップ | 開始 | 終了 | 削減 |
|---------|------|------|------|
| 正規化 | 346 | ~280 | ~70 |
| missing_doc_ref 手動修正 | 280 | 275 | 5 |
| inconsistent_ref LLM修正 | 275 | ~240 | ~35 |
| emphasis_mismatch 部分修正 | 240 | ~150 | ~90 |

**最終目標**: 100 件以下

---

## トラブルシューティング

### LLM が逆効果

**対策**: `--limit` を小さく（10-20）して試す。悪化したら中止。

### 正規化でエラー

**対策**: 構文エラーの PO を先に修正：

```powershell
# エラーファイル一覧
python -c "
import polib
from pathlib import Path
for po in Path('locales/ja/LC_MESSAGES').rglob('*.po'):
    try: polib.pofile(str(po))
    except: print(po)
"
```

### ビルド警告が減らない

**対策**: 警告ログを分析：

```powershell
cd docs
make html-ja 2>&1 | Select-String "WARNING" | Group-Object | Sort-Object Count -Descending
```

上位の警告タイプに対して PO を修正。

---

## まとめ

**最短ルート**:

1. **正規化実行** → 70 件削減
2. **missing_doc_ref 手動修正（5 件のみ）** → 5 件削減
3. **ビルド確認** → 警告が 500 以下なら OK

**慎重ルート（推奨）**:

1. 正規化
2. 品質チェック
3. タイプ別に LLM 少量修正（10-20 件ずつ）
4. 各回正規化＋チェックで検証
5. 改善を確認しながら進行

**現在の最優先**:
```powershell
# これだけ実行
python docs/scripts/normalize_po_whitespace.py --po-dir locales/ja/LC_MESSAGES
python docs/scripts/check_and_fix_po.py --po-dir locales/ja/LC_MESSAGES --output po_issues_normalized.json --verbose
```

その後、結果を見て次の手を決定。
