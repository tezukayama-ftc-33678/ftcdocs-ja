# FTC日本語翻訳プロジェクト - ドキュメント索引

このプロジェクトのすべてのドキュメントが整理されています。

## 🚀 クイックスタート

### 翻訳を始める方へ

**👉 [docs-ja/guides/AI_TRANSLATION_GUIDE.md](docs-ja/guides/AI_TRANSLATION_GUIDE.md)**

このガイド一つで翻訳作業を開始できます：
- 翻訳ルール
- RST構文
- エラー対策
- 検証ツール
- ワークフロー

## 📁 ドキュメント構成

### [docs-ja/](docs-ja/) - 翻訳プロジェクトのメインドキュメント

```
docs-ja/
├── README.md                           # プロジェクト概要
├── guides/                             # 翻訳作業ガイド
│   └── AI_TRANSLATION_GUIDE.md        # 【最重要】AI翻訳統合ガイド
├── reference/                          # リファレンス
│   ├── GLOSSARY.md                    # 用語集（92語）
│   ├── RST_TROUBLESHOOTING_GUIDE.md   # RSTエラー解決
│   ├── TRANSLATION_ROADMAP.md         # 翻訳計画
│   ├── TRANSLATION_PROGRESS.md        # 進捗状況
│   ├── TRANSLATION_GUIDE.md           # 翻訳ガイドライン
│   ├── TRANSLATION_TOOLS_QUICKSTART.md    # ツールクイックスタート
│   ├── TRANSLATION_WORKFLOW_TOOLS.md      # ワークフロー詳細
│   └── TRANSLATION_FILE_LABELS_GUIDE.md  # ファイルラベルガイド
└── archive/                            # 過去の作業記録
    ├── README.md                       # アーカイブ索引
    ├── phase_summaries/                # フェーズ別サマリー
    │   ├── PHASE1_SUMMARY.md
    │   ├── PHASE2_SUMMARY.md
    │   ├── PHASE3_SUMMARY.md
    │   ├── PHASE4.*.md (13ファイル)
    │   └── PHASE5.1_SUMMARY.md
    ├── error_fix_summaries/            # エラー修正サマリー
    │   ├── BUILD_ERROR_RESOLUTION_SUMMARY.md
    │   ├── RST_ERROR_FIX_SUMMARY.md
    │   ├── RST_WARNING_FIX_SUMMARY.md
    │   └── RST_WARNING_FIX_COMPLETE_SUMMARY.md
    ├── ISSUE_RESOLUTION_SUMMARY.md
    ├── ROADMAP_UPDATE_V3.0_SUMMARY.md
    ├── TRANSLATION_CHECKER_IMPROVEMENTS.md
    └── TRANSLATION_INSTRUCTIONS_FOR_AI_OLD.md
```

## 📖 主要ドキュメント

### 必読ドキュメント

| ドキュメント | 説明 | 対象者 |
|------------|------|--------|
| [AI_TRANSLATION_GUIDE.md](docs-ja/guides/AI_TRANSLATION_GUIDE.md) | **AI翻訳統合ガイド** | すべての翻訳者 |
| [GLOSSARY.md](docs-ja/reference/GLOSSARY.md) | 用語統一リスト（92語） | すべての翻訳者 |
| [RST_TROUBLESHOOTING_GUIDE.md](docs-ja/reference/RST_TROUBLESHOOTING_GUIDE.md) | RSTエラー解決ガイド | エラー対処時 |

### 参考ドキュメント

| ドキュメント | 説明 |
|------------|------|
| [TRANSLATION_ROADMAP.md](docs-ja/reference/TRANSLATION_ROADMAP.md) | 翻訳計画とロードマップ |
| [TRANSLATION_PROGRESS.md](docs-ja/reference/TRANSLATION_PROGRESS.md) | 現在の翻訳進捗状況（255ファイル） |
| [TRANSLATION_GUIDE.md](docs-ja/reference/TRANSLATION_GUIDE.md) | 詳細な翻訳ガイドライン |
| [TRANSLATION_TOOLS_QUICKSTART.md](docs-ja/reference/TRANSLATION_TOOLS_QUICKSTART.md) | ツール5分ガイド |
| [TRANSLATION_WORKFLOW_TOOLS.md](docs-ja/reference/TRANSLATION_WORKFLOW_TOOLS.md) | ワークフローとツール詳細 |

### アーカイブ（過去の記録）

| ドキュメント | 説明 |
|------------|------|
| [phase_summaries/](docs-ja/archive/phase_summaries/) | フェーズ1-5の翻訳サマリー（16ファイル） |
| [error_fix_summaries/](docs-ja/archive/error_fix_summaries/) | エラー修正の記録（4ファイル） |
| [archive/README.md](docs-ja/archive/README.md) | アーカイブの詳細索引 |

## 🛠️ 検証ツール

すべてのツールは `docs/scripts/` にあります：

### RST構文検証
```bash
python docs/scripts/validate_rst_syntax.py
```
インラインマークアップのスペース不足、タイトル下線の長さなどを検出

### インラインマークアップ自動修正
```bash
python docs/scripts/fix_rst_inline_markup.py --dry-run
python docs/scripts/fix_rst_inline_markup.py
```
スペース不足を自動修正

### ビルド警告解析
```bash
python docs/scripts/check_build_warnings.py --verbose
```
警告を優先度別に分類（Critical/Important/Low）

### 翻訳進捗チェック
```bash
python docs/scripts/check_translation_progress.py
```
英語が残っている箇所を検出

## 📊 プロジェクト状況

### 翻訳進捗
- **総ファイル数**: 255ファイル
- **詳細**: [TRANSLATION_PROGRESS.md](docs-ja/reference/TRANSLATION_PROGRESS.md) を参照

### ビルド状態
- **ビルド**: ✅ 成功
- **警告数**: 86件（非クリティカル）
  - 63件: undefined labels（表示に影響なし）
  - 22件: grid-item design warnings（表示に影響なし）
  - 1件: anonymous hyperlink mismatch
- **重大エラー**: ✅ すべて解決済み

### 完了したフェーズ
- ✅ Phase 1: 基本ページ
- ✅ Phase 2: ハードウェア/ソフトウェア設定
- ✅ Phase 3: 制御システムコンポーネント
- ✅ Phase 4: プログラミングリソース（13サブフェーズ）
- ✅ Phase 5: AprilTag & Color Processing

## 🔗 外部リンク

- [FIRST Tech Challenge 公式](https://www.firstinspires.org/robotics/ftc)
- [FTC Docs（英語版）](https://ftc-docs.firstinspires.org/)
- [reStructuredText 公式](https://docutils.sourceforge.io/rst.html)
- [Sphinx ドキュメント](https://www.sphinx-doc.org/)

## 📝 よくある質問

### Q: 翻訳を始めたいのですが、何から読めばいいですか？

**A:** [AI_TRANSLATION_GUIDE.md](docs-ja/guides/AI_TRANSLATION_GUIDE.md) を読んでください。このガイド一つで翻訳作業を開始できます。

### Q: 用語の翻訳方法がわかりません

**A:** [GLOSSARY.md](docs-ja/reference/GLOSSARY.md) で用語を確認してください。92語の技術用語がリストされています。

### Q: RSTエラーが出ました

**A:** [RST_TROUBLESHOOTING_GUIDE.md](docs-ja/reference/RST_TROUBLESHOOTING_GUIDE.md) でエラーの解決方法を確認してください。

### Q: 過去の翻訳作業の記録を見たい

**A:** [docs-ja/archive/](docs-ja/archive/) フォルダを参照してください。フェーズ別のサマリーとエラー修正の記録があります。

### Q: ドキュメントが多すぎて混乱します

**A:** 以下の3つだけ読めば大丈夫です：
1. [AI_TRANSLATION_GUIDE.md](docs-ja/guides/AI_TRANSLATION_GUIDE.md) - 翻訳方法
2. [GLOSSARY.md](docs-ja/reference/GLOSSARY.md) - 用語リスト
3. [RST_TROUBLESHOOTING_GUIDE.md](docs-ja/reference/RST_TROUBLESHOOTING_GUIDE.md) - エラー対処

## 🤝 貢献

翻訳に貢献したい方は、[AI_TRANSLATION_GUIDE.md](docs-ja/guides/AI_TRANSLATION_GUIDE.md) の「翻訳ワークフロー」セクションを参照してください。

---

**最終更新**: 2025-12-14
**ドキュメント再編成**: すべての翻訳関連ドキュメントを `docs-ja/` フォルダに整理しました。
