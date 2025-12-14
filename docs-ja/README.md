# FTC日本語翻訳プロジェクト ドキュメント

このフォルダには、FTCドキュメントの日本語翻訳プロジェクトに関するすべてのドキュメントが整理されています。

## 📁 フォルダ構成

```
docs-ja/
├── README.md                    # このファイル
├── guides/                      # 翻訳作業ガイド（必読）
│   └── AI_TRANSLATION_GUIDE.md # 【最重要】AI翻訳統合ガイド
├── reference/                   # リファレンスドキュメント
│   ├── GLOSSARY.md             # 用語集
│   ├── RST_TROUBLESHOOTING_GUIDE.md  # RSTエラー解決ガイド
│   ├── TRANSLATION_ROADMAP.md  # 翻訳ロードマップ
│   ├── TRANSLATION_PROGRESS.md # 翻訳進捗状況
│   └── TRANSLATION_TOOLS_*.md  # ツール関連ドキュメント
└── archive/                     # 過去の作業記録
    ├── phase_summaries/        # フェーズ別作業サマリー
    └── error_fix_summaries/    # エラー修正サマリー
```

## 🚀 翻訳を始める前に

### 必読ドキュメント

1. **[AI_TRANSLATION_GUIDE.md](guides/AI_TRANSLATION_GUIDE.md)** 【最重要】
   - AI翻訳ツール向けの統合ガイド
   - 翻訳ルール、RST構文、エラー対策をすべて網羅
   - このガイドを読めば翻訳作業を開始できます

2. **[GLOSSARY.md](reference/GLOSSARY.md)**
   - 和訳しない用語の完全リスト
   - 技術用語、製品名、API名など

3. **[RST_TROUBLESHOOTING_GUIDE.md](reference/RST_TROUBLESHOOTING_GUIDE.md)**
   - RSTエラーの詳細な解決方法
   - よくあるエラーパターンと対処法

## 🛠️ 検証ツール

翻訳後は以下のツールで品質を確認してください：

```bash
# RST構文検証
python docs/scripts/validate_rst_syntax.py

# インラインマークアップ自動修正
python docs/scripts/fix_rst_inline_markup.py --dry-run

# ビルド警告解析
python docs/scripts/check_build_warnings.py --verbose

# 翻訳進捗チェック
python docs/scripts/check_translation_progress.py
```

## 📊 現在の状態

### 翻訳進捗
- 詳細は [TRANSLATION_PROGRESS.md](reference/TRANSLATION_PROGRESS.md) を参照

### ビルド状態
- ビルド: ✅ 成功
- 警告数: 86件（非クリティカル）
- すべての重大エラー: ✅ 解決済み

## 📖 リファレンス

### コアドキュメント（reference/）

- **GLOSSARY.md** - 用語集（92語）
- **TRANSLATION_ROADMAP.md** - 翻訳計画とロードマップ
- **TRANSLATION_PROGRESS.md** - 翻訳進捗状況（255ファイル）
- **RST_TROUBLESHOOTING_GUIDE.md** - RSTエラー解決ガイド
- **TRANSLATION_TOOLS_QUICKSTART.md** - ツールクイックスタート
- **TRANSLATION_WORKFLOW_TOOLS.md** - ワークフローとツール詳細

### アーカイブ（archive/）

過去の作業記録や段階的な修正サマリー：
- Phase 1-5 翻訳サマリー
- RSTエラー修正サマリー
- 各種イシュー解決サマリー

## 🤝 貢献方法

### 翻訳ワークフロー

1. **準備**
   - AI_TRANSLATION_GUIDE.md を読む
   - GLOSSARY.md で用語を確認

2. **翻訳**
   - RSTファイルを翻訳
   - 技術用語は太字の英語で残す
   - インラインマークアップの後にスペースを入れる

3. **検証**
   ```bash
   python docs/scripts/fix_rst_inline_markup.py
   python docs/scripts/validate_rst_syntax.py
   cd docs && make clean && make html
   ```

4. **コミット**
   ```bash
   git add .
   git commit -m "翻訳: [ファイル名] を追加"
   ```

### 注意事項

- **必ずスペースを入れる**: `**text**と` ではなく `**text** と`
- **太字で英語を残す**: `OpMode` ではなく `**OpMode**`
- **コードは翻訳しない**: コメントのみ翻訳可能
- **ディレクティブの後に空行**: `.. note::` の後は必ず空行

## 🔗 外部リンク

- [FIRST Tech Challenge 公式](https://www.firstinspires.org/robotics/ftc)
- [FTC Docs（英語版）](https://ftc-docs.firstinspires.org/)
- [reStructuredText 公式](https://docutils.sourceforge.io/rst.html)
- [Sphinx ドキュメント](https://www.sphinx-doc.org/)

## 📝 質問・問題報告

- 翻訳に関する質問: AI_TRANSLATION_GUIDE.md の「トラブルシューティング FAQ」を参照
- RSTエラー: RST_TROUBLESHOOTING_GUIDE.md を参照
- その他の問題: GitHubのIssueで報告

---

**最終更新**: 2025-12-14
