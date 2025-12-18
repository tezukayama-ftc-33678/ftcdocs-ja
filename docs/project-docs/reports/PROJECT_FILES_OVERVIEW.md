# プロジェクトファイル一覧

このドキュメントは、ビルド警告修正プロジェクトで作成されたすべてのファイルの概要です。

## 📄 ドキュメントファイル（5個）

### 1. COMPLETION_SUMMARY_JA.md ⭐ 推奨開始点
**言語**: 日本語  
**目的**: プロジェクト全体の完了報告書  
**内容**:
- プロジェクト概要
- 達成した成果の詳細
- 作成したツールの説明
- クイックスタートガイド
- 今後のアクション
- 技術的な詳細

**読むべき人**: すべての人（最初に読むべきファイル）

---

### 2. QUICK_START_WARNINGS.md
**言語**: 日本語  
**目的**: 最速で警告修正を始めるガイド  
**内容**:
- 最速3ステップガイド
- よくある質問
- トラブルシューティング
- 簡潔なコマンド集

**読むべき人**: すぐに作業を始めたい人

---

### 3. BUILD_WARNINGS_REPORT.md
**言語**: 英語  
**目的**: 包括的な技術レポート  
**内容**:
- 詳細な統計分析
- 修正履歴
- 警告の分類
- 期待される効果
- 長期計画

**読むべき人**: 詳細な分析が必要な人、技術的な詳細を知りたい人

---

### 4. docs/WARNING_FIX_GUIDE.md
**言語**: 日本語  
**目的**: 警告修正の詳細ガイド  
**内容**:
- 警告の分類と説明
- 各スクリプトの詳細
- 推奨ワークフロー
- トラブルシューティング
- 定期メンテナンス

**読むべき人**: 問題解決が必要な人、深い理解を得たい人

---

### 5. scripts/warnings/README.md
**言語**: 日本語  
**目的**: スクリプトの技術ドキュメント  
**内容**:
- 各スクリプトの詳細説明
- コマンドライン引数
- 使用例
- 依存関係
- トラブルシューティング

**読むべき人**: スクリプトを使う人、カスタマイズしたい人

---

## 🛠️ スクリプトファイル（5個）

### 1. scripts/normalize_po_files.py ⭐ 最も推奨
**用途**: POファイルの総合正規化  
**機能**:
- Gitマージコンフリクト削除
- Inline markup修正
- 空白正規化

**実行方法**:
```bash
python scripts/normalize_po_files.py
python scripts/normalize_po_files.py --dry-run
python scripts/normalize_po_files.py --file path/to/file.po
```

**実績**: 29ファイルを正規化

---

### 2. scripts/warnings/fix_merge_conflicts.py
**用途**: Gitマージコンフリクトの自動削除  
**機能**:
- `<<<<<<<`, `=======`, `>>>>>>>` マーカー削除
- HEAD側のコンテンツを保持

**実行方法**:
```bash
python scripts/warnings/fix_merge_conflicts.py
python scripts/warnings/fix_merge_conflicts.py --dry-run
```

**実績**: 95ファイル、305個の競合を解決

---

### 3. scripts/warnings/analyze_all_warnings.py
**用途**: 警告の詳細分析  
**機能**:
- 警告のタイプ別分類
- ファイル別集計
- 修正推奨事項の生成
- レポート出力

**実行方法**:
```bash
python scripts/warnings/analyze_all_warnings.py /tmp/warnings.log
python scripts/warnings/analyze_all_warnings.py /tmp/warnings.log --output report.md
```

---

### 4. scripts/warnings/fix_po_syntax_errors.py
**用途**: PO構文エラーの自動修正  
**機能**:
- エスケープされていない引用符を修正
- 不正な複数行文字列を修正
- 警告ログから問題ファイルを検出

**実行方法**:
```bash
python scripts/warnings/fix_po_syntax_errors.py --warning-log /tmp/warnings.log
python scripts/warnings/fix_po_syntax_errors.py --dry-run
```

---

### 5. scripts/warnings/fix_po_newlines.py
**用途**: 改行エラーの自動修正  
**機能**:
- msgid/msgstr後の改行不足を修正
- 警告ログから問題ファイルを検出

**実行方法**:
```bash
python scripts/warnings/fix_po_newlines.py --warning-log /tmp/warnings.log
python scripts/warnings/fix_po_newlines.py --dry-run
```

---

## 📊 ファイル関係図

```
Start Here
    ↓
COMPLETION_SUMMARY_JA.md (全体像)
    ↓
    ├─→ QUICK_START_WARNINGS.md (すぐに始める)
    │       ↓
    │   normalize_po_files.py を実行
    │
    ├─→ BUILD_WARNINGS_REPORT.md (詳細分析)
    │       ↓
    │   analyze_all_warnings.py で分析
    │
    └─→ WARNING_FIX_GUIDE.md (深い理解)
            ↓
        各種スクリプトを使い分け
```

## 🎯 目的別ファイルガイド

### すぐに作業を始めたい
1. **QUICK_START_WARNINGS.md** を読む
2. `python scripts/normalize_po_files.py` を実行

### 全体を理解したい
1. **COMPLETION_SUMMARY_JA.md** を読む
2. **BUILD_WARNINGS_REPORT.md** で詳細を確認

### 問題を解決したい
1. **WARNING_FIX_GUIDE.md** を読む
2. トラブルシューティングセクションを参照

### スクリプトを使いたい
1. **scripts/warnings/README.md** を読む
2. 各スクリプトの詳細を確認

### カスタマイズしたい
1. スクリプトのソースコードを読む
2. **scripts/warnings/README.md** で技術詳細を確認

## 📈 推奨される読む順序

### 初めての人
1. COMPLETION_SUMMARY_JA.md（10分）
2. QUICK_START_WARNINGS.md（5分）
3. 実際にスクリプトを実行（5分）

### 詳細を知りたい人
1. COMPLETION_SUMMARY_JA.md（10分）
2. BUILD_WARNINGS_REPORT.md（15分）
3. WARNING_FIX_GUIDE.md（20分）
4. scripts/warnings/README.md（15分）

### メンテナンス担当者
1. QUICK_START_WARNINGS.md（5分）
2. WARNING_FIX_GUIDE.md（20分）
3. scripts/warnings/README.md（15分）
4. 各スクリプトのソースコード（30分）

## 🔧 スクリプトの使い分け

### 日常的なメンテナンス
```bash
python scripts/normalize_po_files.py
```
**理由**: 包括的で安全、すべての一般的な問題に対応

### 特定の問題に対処
- マージコンフリクト → `fix_merge_conflicts.py`
- PO構文エラー → `fix_po_syntax_errors.py`
- 改行エラー → `fix_po_newlines.py`

### 分析と報告
```bash
python scripts/warnings/analyze_all_warnings.py /tmp/warnings.log
```
**理由**: 現状把握、進捗確認、問題の特定

## 💾 ファイルサイズと所要時間

| ファイル | サイズ | 読む時間 |
|---------|--------|----------|
| COMPLETION_SUMMARY_JA.md | 約6KB | 10分 |
| QUICK_START_WARNINGS.md | 約3KB | 5分 |
| BUILD_WARNINGS_REPORT.md | 約6KB | 15分 |
| WARNING_FIX_GUIDE.md | 約5KB | 20分 |
| scripts/warnings/README.md | 約4KB | 15分 |

## 🌟 おすすめの使い方

### Case 1: 初めてプロジェクトに参加
```
1. COMPLETION_SUMMARY_JA.md を読む
2. QUICK_START_WARNINGS.md の手順に従う
3. normalize_po_files.py を実行
4. 結果を確認
```

### Case 2: 警告が増えてきた
```
1. ビルドして警告を記録
2. analyze_all_warnings.py で分析
3. normalize_po_files.py を実行
4. WARNING_FIX_GUIDE.md でトラブルシューティング
```

### Case 3: 特定の問題に対処
```
1. WARNING_FIX_GUIDE.md で問題を特定
2. scripts/warnings/README.md で適切なスクリプトを選択
3. --dry-run で動作確認
4. 実際に実行
```

## 🎓 学習パス

### 初心者向け（30分）
1. COMPLETION_SUMMARY_JA.md
2. QUICK_START_WARNINGS.md
3. 実際にスクリプトを実行

### 中級者向け（1時間）
1. COMPLETION_SUMMARY_JA.md
2. BUILD_WARNINGS_REPORT.md
3. WARNING_FIX_GUIDE.md
4. スクリプトのカスタマイズ

### 上級者向け（2時間）
1. すべてのドキュメントを読む
2. スクリプトのソースコードを理解
3. 新しいスクリプトを作成

## 📞 サポート

質問や問題がある場合:
1. まず該当ドキュメントのトラブルシューティングを確認
2. それでも解決しない場合はGitHubのIssuesで報告

---

**最終更新**: 2025-12-17  
**作成者**: GitHub Copilot  
**バージョン**: 1.0
