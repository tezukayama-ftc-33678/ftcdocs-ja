# Sphinx 日本語ビルド警告分析レポート

**日時**: 2025-12-18  
**総警告数**: 569件  
**ビルドコマンド**: `make clean && make html-ja`

## 警告分類サマリー

| 警告タイプ | 件数 | 割合 |
|-----------|------|------|
| Inline strong start-string without end-string (`**`) | 266 | 46.7% |
| Inline emphasis start-string without end-string (`*`) | 70 | 12.3% |
| undefined label | 48 | 8.4% |
| Inline interpreted text or phrase reference start-string | 46 | 8.1% |
| Inline literal start-string without end-string (`` ` ``) | 34 | 6.0% |
| inconsistent term references in translated message | 25 | 4.4% |
| inconsistent references in translated message | 21 | 3.7% |
| unknown document | 15 | 2.6% |
| document isn't included in any toctree | 5 | 0.9% |
| その他（Mismatch, term not in glossary等） | 39 | 6.9% |

## 主要な問題

### 1. Inline Markup の不一致（最優先）

**総計**: 370件（65%）

#### a) `**`（強調）の不一致: 266件
- 原因: 翻訳時に`**`の開始と終了が対応していない
- 影響: ボールドテキストが正しく表示されない
- 修正方法: POファイル内で`**`の数を偶数にする

#### b) `*`（イタリック）の不一致: 70件
- 原因: 翻訳時に`*`の開始と終了が対応していない
- 影響: イタリックテキストが正しく表示されない
- 修正方法: POファイル内で`*`の数を偶数にする

#### c) `` ` ``（コードリテラル）の不一致: 34件
- 原因: 翻訳時にバッククォートの開始と終了が対応していない
- 影響: インラインコードが正しく表示されない
- 修正方法: POファイル内でバッククォートの数を偶数にする

### 2. 未定義ラベル参照（48件、8.4%）

主な問題:
- 日本語化されたラベル名が元のラベル名と一致していない
- 例: `'ハードウェアとソフトウェア設定/外部ウェブカムを設定する/configuring-external-webcam:画像プレビュー'`
- 影響: クロスリファレンスリンクが機能しない

修正方法:
- ラベル参照は英語のまま保持する必要がある
- POファイルで`:ref:`タグ内のラベル名を英語に戻す

### 3. Inline interpreted text の問題（46件、8.1%）

- 原因: `:ref:`, `:doc:`, `:term:`などのSphinxロール構文の不一致
- 影響: クロスリファレンスが機能しない
- 修正方法: ロール構文の開始と終了バッククォートを確認

### 4. 参照の不一致（46件、8.1%）

#### a) inconsistent term references (25件)
- 翻訳で`:term:`や`:ref:`のリストが元と異なる
- 一部が欠落したり、重複している

#### b) inconsistent references (21件)
- ハイパーリンク参照`[text]_`の不一致
- アンカー参照の欠落

### 5. 不明なドキュメント参照（15件、2.6%）

- 日本語に翻訳されたドキュメントパスが見つからない
- 例: `'../../../blocks/ブロックチュートリアル'`
- 修正方法: ドキュメントパスは英語のまま保持

## 正規表現で修正可能な問題

以下の問題は自動スクリプトまたは正規表現で修正可能:

### 1. Inline markup の数を偶数にする

```python
# `**`が奇数個の場合、末尾に追加または削除
import re

def fix_inline_markup(text):
    # **を数える
    bold_count = text.count('**')
    if bold_count % 2 != 0:
        # 最後の**を削除するか、末尾に追加
        pass
    
    # *を数える（ただし**は除外）
    # `を数える
```

### 2. 日本語化されたラベル参照を英語に戻す

```bash
# POファイル内で日本語化されたラベルを検出
grep -E ':ref:`[^`]*[\u3000-\u9FFF]' locales/ja/LC_MESSAGES/**/*.po
```

## 修正の優先順位

### 高優先度（自動修正可能）

1. **Inline strong/emphasis/literal markup の不一致** (370件)
   - 既存スクリプト: `scripts/normalize_po_files.py`
   - 実行コマンド: `python scripts/normalize_po_files.py`

### 中優先度（半自動修正可能）

2. **未定義ラベル参照** (48件)
   - 日本語化されたラベルを英語に戻す
   - 正規表現で検出して手動修正

3. **不明なドキュメント参照** (15件)
   - 日本語化されたパスを英語に戻す
   - 比較的簡単に修正可能

### 低優先度（手動修正必要）

4. **inconsistent term/references** (46件)
   - 各POファイルを個別に確認
   - 翻訳の質を保ちながら修正

5. **その他のエラー** (40件)
   - ケースバイケースで対応

## 推奨ワークフロー

### ステップ1: 自動修正の実行

```bash
# POファイル正規化スクリプトを実行
python scripts/normalize_po_files.py

# ビルドして結果確認
cd docs
make clean
make html-ja 2>&1 | tee /tmp/build_warnings_after_normalize.log
```

### ステップ2: 残存警告の分析

```bash
# 警告を分析
grep "WARNING:" /tmp/build_warnings_after_normalize.log | wc -l
```

### ステップ3: 手動修正

- undefined labelの修正
- unknown documentの修正
- inconsistent referencesの修正

## 期待される削減効果

- **自動修正で削減可能**: 約370件（65%）→ 残り約200件
- **半自動修正で削減可能**: 約60件（10%）→ 残り約140件
- **手動修正が必要**: 約140件（25%）

## 長期的な対策

1. **翻訳品質の向上**
   - LLM翻訳時にRST構造を保持するプロンプトの改善
   - Inline markupの開始/終了を必ず対応させる

2. **自動検証の導入**
   - CI/CDで警告数をチェック
   - 新規翻訳時に警告が増えないように監視

3. **ドキュメント化**
   - 翻訳ガイドラインの整備
   - よくある間違いのリスト化

## 次のアクション

1. ✅ 警告ログを保存（完了）
2. ✅ 警告レポートを作成（完了）
3. ⏳ `scripts/normalize_po_files.py`を実行
4. ⏳ 修正後のビルドで警告数を確認
5. ⏳ 残存警告の手動修正計画を立案

---

**作成者**: GitHub Copilot  
**最終更新**: 2025-12-18
