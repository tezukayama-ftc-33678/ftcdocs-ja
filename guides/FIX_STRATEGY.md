# ビルド警告修正戦略

## 現状分析

### 警告統計 (2024年実行時点)
- **総警告数**: 1,186件
- **Start of line didn't match**: 316件 (26%)
- **Inline strong不一致 (`**`)**: 78件 (6%)
- **Inline emphasis不一致 (`*`)**: 38件 (3%)
- **Inline literal不一致 (`` ` ``)**: 16件 (1%)
- **翻訳メッセージ参照矛盾**: 20件 (1%)
- **その他**: 718件 (61%)

### 根本原因
**70個のPOファイルに構文エラーあり** - これがすべての警告の根本原因

構文エラーの種類:
1. エスケープされていない二重引用符
2. 不完全なマルチライン文字列
3. メッセージIDとの不一致

## 修正アプローチ (3段階)

### Phase 1: PO構文エラー修正 (最優先)

**目標**: 70個のPOファイルの構文エラーを修正

**方法**:
1. `fix_po_syntax.py` の改良版を作成
   - より強力なエスケープロジック
   - 複数行文字列の修正
   - バックアップ作成

2. 手動修正が必要な場合:
   ```bash
   # エラーの詳細を確認
   python -c "import polib; polib.pofile('path/to/file.po')"
   ```

3. 修正スクリプト例:
   ```python
   # エスケープされていない " を \" に変換
   # ただし、既にエスケープされている \" は除く
   # 行末の " も除く
   ```

**実行**:
```bash
# バックアップ
cp -r locales locales_backup_$(date +%Y%m%d)

# 修正実行
python fix_po_syntax_v2.py

# 検証
python -c "import polib; [print(f) for f in Path('locales/ja/LC_MESSAGES').rglob('*.po') if not try_parse(f)]"
```

### Phase 2: Inline Markup修正

**目標**: `**`, `*`, `` ` `` の不一致を修正 (132件)

**方法**:
1. 正規表現ベースの自動修正
   - `**text` で始まり `**` で終わらないパターン
   - `*text*` の不一致
   - `` `code `` の不一致

2. 修正ルール:
   - 文の区切り（句読点、改行）を検出
   - 区切りの前にクローズマークを挿入
   - 日本語特有の句読点に対応

**実行**:
```bash
python fix_build_warnings.py
```

### Phase 3: 残存警告の修正

**目標**: Phase 1-2で解決されない警告を修正

**方法**:
1. LLMベースの修正
   - 翻訳の品質向上
   - 文脈に応じたマークアップ修正

2. 手動レビュー
   - 警告の多いファイル上位15個を優先
   - 特に `index.rst`, `new-self-inspect.rst`, `huskylens.rst`

**実行**:
```bash
# 残存警告を分析
make clean && make html-ja 2>&1 | Tee-Object -FilePath build_warnings_phase3.log
python summarize_warnings.py

# LLM修正
python fix_po_with_llm.py --files <top_priority_files>
```

## 実行手順

### ステップ1: 現状の確認
```powershell
cd h:\ftcdocs-ja

# 現在の警告数
python summarize_warnings.py

# 構文エラーのあるファイル一覧
python -c "from pathlib import Path; import polib; [print(f) for f in Path('locales/ja/LC_MESSAGES').rglob('*.po') if not (lambda p: (polib.pofile(str(p)), True)[1] if True else False)(f)]"
```

### ステップ2: バックアップ
```powershell
# タイムスタンプ付きバックアップ
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
Copy-Item -Recurse locales "locales_backup_$timestamp"
```

### ステップ3: Phase 1実行
```powershell
# 構文エラー修正スクリプトを作成・実行
python fix_po_syntax_advanced.py

# 検証
python verify_po_syntax.py
```

### ステップ4: Phase 2実行
```powershell
# Inline markup修正
python fix_build_warnings.py

# ビルドして確認
cd docs
make clean
make html-ja 2>&1 | Tee-Object -FilePath ..\build_warnings_phase2.log
cd ..

# 警告数の変化を確認
python summarize_warnings.py
```

### ステップ5: Phase 3実行
```powershell
# 残存警告の分析
python analyze_remaining_warnings.py

# LLM修正 (必要に応じて)
python fix_po_with_llm.py
```

## 成功基準

### Phase 1後:
- [ ] 70個の構文エラーがすべて解決
- [ ] すべてのPOファイルが `polib.pofile()` でパース可能
- [ ] 警告数が大幅に減少 (目標: 50%以上減)

### Phase 2後:
- [ ] Inline markup警告が90%以上減少
- [ ] 残存警告が300件以下

### Phase 3後:
- [ ] 総警告数が100件以下
- [ ] 致命的な警告 (ビルド失敗につながるもの) がゼロ
- [ ] ビルドが正常に完了

## トラブルシューティング

### 問題: 構文エラーが修正されない
**解決策**:
1. エラーメッセージの行番号を確認
2. 該当ファイルをテキストエディタで開く
3. 行番号付近の `msgstr` を確認
4. 手動でエスケープを修正

### 問題: 修正後も警告が残る
**解決策**:
1. `make clean` を実行してキャッシュをクリア
2. `.mo` ファイルを削除
3. ビルドを再実行

### 問題: 修正によって新しいエラーが発生
**解決策**:
1. バックアップから復元
2. より慎重な修正アプローチを採用
3. 小さなバッチで修正を適用し、都度検証

## ツール一覧

### 作成済みスクリプト
- `summarize_warnings.py` - 警告の集計とサマリー
- `analyze_warnings.py` - 詳細な警告分析
- `fix_build_warnings.py` - Inline markup自動修正
- `fix_po_syntax.py` - 基本的な構文エラー修正

### 作成が必要なスクリプト
- `fix_po_syntax_advanced.py` - より強力な構文エラー修正
- `verify_po_syntax.py` - POファイルの構文検証
- `analyze_remaining_warnings.py` - Phase 2後の残存警告分析

## 次のアクション

**即座に実行すべきこと**:
1. `fix_po_syntax_advanced.py` の作成
2. Phase 1の実行
3. 中間結果の確認

**その後**:
4. Phase 2の実行
5. 効果の測定
6. Phase 3の計画調整
