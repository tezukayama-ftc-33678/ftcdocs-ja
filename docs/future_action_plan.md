# 今後の警告対応方針

**作成日**: 2025-12-18  
**現在の警告数**: 575件  
**目標警告数**: 100件以下

## 優先度別対応計画

### 🔴 高優先度（即座に実施可能、効果大）

#### 1. 未定義ラベル参照の修正（48件、8.3%）

**問題**:
日本語化されたラベル参照が原因で、クロスリファレンスが機能していない。

**例**:
```rst
:ref:`ハードウェアとソフトウェア設定/外部ウェブカムを設定する/configuring-external-webcam:画像プレビュー`
```

**修正方法**:
1. POファイル内で日本語化されたラベルを検出
2. ラベル名を英語の元の形式に戻す
3. 表示テキストのみを日本語化

**正しい形式**:
```rst
:ref:`画像プレビュー <hardware_and_software_configuration/configuring/configuring_external_webcam/configuring-external-webcam:image preview>`
```

**実装スクリプト**:
```bash
# 日本語ラベルを含む:ref:を検出
grep -r ':ref:`[^`]*[\u3000-\u9FFF]' locales/ja/LC_MESSAGES/ -n

# または
python tools/fix_japanese_labels.py
```

**期待される削減**: 48件

---

#### 2. 不明なドキュメント参照の修正（15件、2.6%）

**問題**:
ドキュメントパスが日本語化されている。

**例**:
```rst
:doc:`../../../blocks/ブロックチュートリアル`
```

**修正方法**:
POファイル内でドキュメントパスを英語に戻す。

**実装**:
```bash
# 日本語パスを検出
grep -r ':doc:`[^`]*[\u3000-\u9FFF]' locales/ja/LC_MESSAGES/ -n
```

**期待される削減**: 15件

---

### 🟡 中優先度（半自動で対応可能）

#### 3. Inline Markup の不一致（372件、64.7%）

**内訳**:
- `**` (強調): 268件
- `*` (イタリック): 70件
- `` ` `` (コードリテラル): 34件

**問題**:
現在のスクリプトではPOファイルレベルの単純な不一致しか検出できないが、
実際の警告はSphinx処理時のコンテキスト依存。

**対応方法**:

1. **警告ログから具体的な問題箇所を抽出**
   ```bash
   grep "Inline strong start-string" /tmp/build_warnings.log | \
     cut -d: -f1-3 | sort | uniq > /tmp/inline_strong_issues.txt
   ```

2. **各ファイルを個別に確認**
   - RSTファイルの該当行を確認
   - 対応するPOファイルのエントリを特定
   - 手動で修正

3. **パターン分析**
   - よくある誤りのパターンを特定
   - パターンごとに自動修正スクリプトを作成

**期待される削減**: 100-200件（段階的）

---

#### 4. Inconsistent References（46件、8.0%）

**内訳**:
- inconsistent term references: 25件
- inconsistent references: 21件

**問題例**:
```
original: [':term:`fork <Fork>`', ':term:`main repository <Main Repository>`']
translated: [':term:`フォーク <Fork>`']  # 1つ欠落
```

**修正方法**:
1. 警告ログから具体的な不一致を特定
2. POファイルで元の参照リストと翻訳後のリストを比較
3. 欠落または重複した参照を修正

**期待される削減**: 46件

---

### 🟢 低優先度（手動対応が必要）

#### 5. Inline Interpreted Text（50件、8.7%）

**問題**:
`:ref:`, `:doc:`, `:term:`などのSphinxロール構文のバッククォートが不整合。

**対応方法**:
各ファイルを個別に確認して手動修正。

**期待される削減**: 20-30件

---

#### 6. その他の警告（44件、7.7%）

- document isn't included in any toctree: 5件
- Mismatch: 2件
- term not in glossary: 1件
- Title underline too short: 1件
- Block quote ends without a blank line: 1件
- duplicate term description: 1件

**対応方法**:
ケースバイケースで個別対応。

---

## 実装計画

### フェーズ1: 即座に実施（1-2時間）

```bash
# 1. 日本語ラベルの検出と修正
python tools/fix_japanese_labels.py --dry-run
python tools/fix_japanese_labels.py

# 2. 日本語ドキュメントパスの検出と修正
python tools/fix_japanese_doc_paths.py --dry-run
python tools/fix_japanese_doc_paths.py

# 3. ビルドして確認
cd docs
make clean
make html-ja 2>&1 | tee /tmp/build_warnings_phase1.log

# 期待: 575件 → 512件（-63件）
```

### フェーズ2: 半自動対応（3-5時間）

```bash
# 1. Inline markup の警告を抽出
python tools/extract_inline_markup_warnings.py /tmp/build_warnings_phase1.log

# 2. パターン分析
python tools/analyze_inline_markup_patterns.py

# 3. パターンごとに修正
python tools/fix_inline_markup_by_pattern.py

# 4. Inconsistent referencesの修正
python tools/fix_inconsistent_references.py

# 期待: 512件 → 300-350件（-150-200件）
```

### フェーズ3: 手動対応（5-10時間）

残存する200-300件の警告を個別に確認して手動修正。

---

## 必要なスクリプト

### 作成済み
- ✅ `tools/fix_inline_markup.py` - 単純なインラインマークアップ修正

### 作成が必要
- ⏳ `tools/fix_japanese_labels.py` - 日本語ラベル参照を英語に変換
- ⏳ `tools/fix_japanese_doc_paths.py` - 日本語ドキュメントパスを英語に変換
- ⏳ `tools/extract_inline_markup_warnings.py` - 警告から具体的な問題箇所を抽出
- ⏳ `tools/analyze_inline_markup_patterns.py` - パターン分析
- ⏳ `tools/fix_inline_markup_by_pattern.py` - パターンベースの修正
- ⏳ `tools/fix_inconsistent_references.py` - 不整合な参照の修正

---

## 正規表現パターン集

### 日本語ラベルの検出

```python
import re

# :ref:`で始まり日本語を含む
pattern = r':ref:`[^`]*[\u3000-\u9FFF][^`]*`'

# :doc:`で始まり日本語を含む
pattern = r':doc:`[^`]*[\u3000-\u9FFF][^`]*`'

# :term:`で始まり日本語を含む
pattern = r':term:`[^`]*[\u3000-\u9FFF][^`]*`'
```

### インラインマークアップの検出

```python
# **が奇数個
def has_odd_bold(text):
    return text.count('**') % 2 != 0

# *が奇数個（**を除外）
def has_odd_italic(text):
    text_no_bold = text.replace('**', '')
    return text_no_bold.count('*') % 2 != 0

# `が奇数個
def has_odd_backtick(text):
    return text.count('`') % 2 != 0
```

---

## 定期メンテナンス

### 週次
```bash
# ビルド警告数を確認
cd docs
make clean
make html-ja 2>&1 | grep "build succeeded" | grep "warnings"
```

### 月次
```bash
# すべての修正スクリプトを実行
python tools/fix_japanese_labels.py
python tools/fix_japanese_doc_paths.py
python tools/fix_inline_markup.py

# ビルドして確認
cd docs
make clean
make html-ja
```

---

## 長期的な改善

### 1. 翻訳品質の向上

**LLM翻訳プロンプトの改善**:
```
あなたはSphinx RST形式のドキュメントを翻訳する専門家です。
以下のルールを厳守してください：

1. RST構造を絶対に変更しない
2. `:ref:`, `:doc:`, `:term:`内のラベル名は英語のまま保持
3. インラインマークアップ（**, *, `）の開始と終了を必ず対応させる
4. ドキュメントパスは英語のまま保持
5. 表示テキストのみを日本語化する

例：
元: :ref:`Image Preview <hardware_and_software_configuration/configuring/configuring_external_webcam/configuring-external-webcam:image preview>`
訳: :ref:`画像プレビュー <hardware_and_software_configuration/configuring/configuring_external_webcam/configuring-external-webcam:image preview>`
```

### 2. CI/CD統合

```yaml
# .github/workflows/check-warnings.yml
name: Check Build Warnings

on: [push, pull_request]

jobs:
  check-warnings:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Build Japanese docs
        run: |
          cd docs
          make clean
          make html-ja 2>&1 | tee build.log
      - name: Count warnings
        run: |
          WARNINGS=$(grep "build succeeded" build.log | grep -oP '\d+(?= warnings)')
          echo "Warnings: $WARNINGS"
          if [ $WARNINGS -gt 100 ]; then
            echo "Too many warnings: $WARNINGS"
            exit 1
          fi
```

### 3. ドキュメント整備

- 翻訳者向けガイドライン作成
- よくある間違いとその修正方法をまとめる
- レビュープロセスの確立

---

## 参考情報

### 関連ドキュメント
- `docs/WARNING_FIX_GUIDE.md` - 既存の修正ガイド
- `docs/warning_analysis_report.md` - 詳細な警告分析
- `docs/PO_FIX_REPORT_2025-12-18.md` - PO修正レポート

### ログファイル
- `docs/build_warnings_2025-12-18.log` - 初回ビルド警告（569件）
- `/tmp/build_warnings_after_fix.log` - 修正後ビルド警告（575件）

### スクリプト
- `tools/fix_inline_markup.py` - インラインマークアップ修正
- `tools/po-fixing/normalize_po_files.py` - PO正規化

---

**最終更新**: 2025-12-18  
**作成者**: GitHub Copilot
