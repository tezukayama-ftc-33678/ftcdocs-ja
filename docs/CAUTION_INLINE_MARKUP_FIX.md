# ⚠️ インラインマークアップ修正の注意事項

**作成日**: 2025-12-18  
**重要度**: 高

## 発見された問題

`tools/fix_inline_markup.py` スクリプトによる自動修正が一部の箇所で不適切な変更を加えたことが判明。

## 問題の詳細

### 1. コンテキストを無視した修正

**スクリプトのロジック**:
- インラインマークアップ（`**`, `*`, `` ` ``）が奇数個の場合、最後の出現箇所を削除

**問題**:
このアプローチは、以下のようなケースで正しく動作しない：

```rst
# 元のテキスト（正しい）
"we would add two asterisks (**) to the front and end of each word to make them **bold**."

# スクリプトによる誤修正
# **の数が奇数（3個）と判定され、最後の**が削除される
"we would add two asterisks (**) to the front and end of each word to make them **bold."
# → これでも奇数（2個）なので、さらに削除される可能性
```

### 2. コードレビューで発見された問題

修正後のビルドで以下の新たな問題が発見された：

1. **不完全なボールドマークアップ** (overview.po:104)
   - `them **bold` - 閉じる`**`が欠落

2. **欠落した文字** (basic_rst_content.po:459, 1138)
   - `星()` → 本来は `星(*)`
   - アスタリスクを削除しすぎた

3. **不整合なマークアップ** (overview.po:152)
   - `** dog *` - ダブルとシングルが混在

## 原因分析

### スクリプトの設計上の問題

```python
# 問題のあるコード
def fix_inline_markup_in_text(text, markup_char, description):
    count = text.count(markup_char)
    if count % 2 == 0:
        return text, False
    
    # 最後の出現箇所を単純に削除
    last_index = text.rfind(markup_char)
    if last_index != -1:
        text = text[:last_index] + text[last_index + len(markup_char):]
        return text, True
```

**問題点**:
1. マークアップが説明的に使用されている場合を考慮していない
   - 例: "two asterisks (**)" ← これは実際のマークアップではなく、説明
2. コンテキストを無視して機械的に削除
3. ペアになっているマークアップを識別していない

## 正しいアプローチ

### 1. コンテキスト認識

マークアップには2種類ある：

**A. 実際のフォーマットマークアップ**:
```rst
This is **bold** text.
This is *italic* text.
This is ``code`` text.
```

**B. 説明的な使用（エスケープされるべき）**:
```rst
We use asterisks (**) to make text bold.
The backtick (`) is used for code.
```

### 2. ペア検出

マークアップは必ずペアで機能する：
```python
def find_markup_pairs(text, markup):
    """マークアップのペアを検出"""
    positions = []
    i = 0
    while i < len(text):
        idx = text.find(markup, i)
        if idx == -1:
            break
        positions.append(idx)
        i = idx + len(markup)
    
    # ペアを作成
    pairs = []
    for i in range(0, len(positions) - 1, 2):
        pairs.append((positions[i], positions[i+1]))
    
    # 余ったものが問題
    if len(positions) % 2 != 0:
        unpaired = positions[-1]
        return pairs, unpaired
    return pairs, None
```

### 3. 手動確認が必要

自動修正は以下の場合のみ適用すべき：
- 明らかにペアになっていないマークアップ
- コンテキストから判断して安全な場合

**推奨**: 警告ログから具体的な問題箇所を抽出し、個別に手動確認

## 修正が必要な箇所

コードレビューで指摘された18件：

### 優先度：高（誤った自動修正）

1. `contrib/tutorials/make_rst/overview/overview.po:104`
   - 不完全なボールドマークアップ
   - 手動で`**`を追加

2. `contrib/tutorials/make_rst/overview/overview.po:152`
   - `** dog *` → `** dog **` に修正

3. `contrib/tutorials/make_rst/basic_rst_content/basic_rst_content.po:459`
   - `星()` → `星(*)` に修正

4. `contrib/tutorials/make_rst/basic_rst_content/basic_rst_content.po:1138`
   - `星()` → `星(*)` に修正

### 優先度：中（リンク構文の問題）

5-18. 各種POファイルのリンク構文
- `>__ ` (スペースあり) → `>__` (スペースなし)
- `>_ ` → `>__` 

## 推奨される対応

### 即座に実施

```bash
# 1. 誤った自動修正を手動で元に戻す
# 該当する4-5ファイルを確認して修正

# 2. ビルドして確認
cd docs
make clean
make html-ja 2>&1 | tee /tmp/build_warnings_fixed.log
```

### 長期的対応

1. **スクリプトの改良**
   - コンテキスト認識機能の追加
   - ペア検出アルゴリズムの実装
   - Dry-runで変更内容を詳細に表示

2. **段階的な修正**
   - 自動修正は最小限に
   - 各修正後にビルドして確認
   - 警告が減ったことを確認してから次へ

3. **手動確認プロセス**
   - 警告ログから具体的な問題箇所を抽出
   - 各箇所を個別に確認
   - パターンが見つかったらスクリプト化

## 教訓

1. **自動修正は慎重に**
   - 単純な文字数カウントだけでは不十分
   - コンテキストの理解が必要

2. **段階的なアプローチ**
   - 小さな変更を積み重ねる
   - 各段階でビルドして検証

3. **コードレビューの重要性**
   - 自動修正後は必ずレビュー
   - 意図しない変更がないか確認

## 次のステップ

1. ✅ この注意事項ドキュメントを作成（完了）
2. ⏳ コードレビューで指摘された18件を手動修正
3. ⏳ ビルドして警告数を確認
4. ⏳ `fix_inline_markup.py` スクリプトの改良（または使用停止）

---

**重要**: 今後、自動修正スクリプトを使用する場合は、必ず以下を実施：
1. Dry-runで変更内容を確認
2. 少数のファイルでテスト
3. ビルドして警告が減ることを確認
4. 問題なければ全体に適用

**作成者**: GitHub Copilot  
**ステータス**: 注意喚起
