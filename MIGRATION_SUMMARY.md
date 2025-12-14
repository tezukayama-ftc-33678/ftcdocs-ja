# .po-based Translation Migration - 完了サマリー

## ✅ 完了したこと

このPRでは、ftcdocs-ja を標準的な .po ベースの翻訳システムに移行するための準備が完了しました。

### 1. 環境のセットアップ

- ✅ `sphinx-intl` をインストール・設定
- ✅ `docs/requirements.txt` に追加
- ✅ `docs/source/conf.py` の gettext 設定を確認
  ```python
  language = 'en'
  locale_dirs = ['locale/']
  gettext_compact = False
  ```

### 2. ドキュメントの作成

| ドキュメント | 内容 | 対象読者 |
|------------|------|---------|
| **WHY_PO_TRANSLATION.md** | 移行の理由と利点 | すべて |
| **MIGRATION_NEXT_STEPS.md** | 具体的な次のステップ | プロジェクト管理者 |
| **PO_TRANSLATION_WORKFLOW.md** | 日常的なワークフロー | 翻訳者 |
| **MIGRATION_TO_PO_GUIDE.md** | 技術的な詳細 | 開発者 |
| **TRANSLATION_MAPPING.md** | 既存翻訳の抽出 | リファレンス |
| **MIGRATION_REPORT.md** | スキャン結果 | リファレンス |

### 3. ツールとスクリプト

- ✅ `docs/scripts/migrate_translations_to_po.py` - 移行支援スクリプト
- ✅ `docs/Makefile` に新しいターゲットを追加:
  - `make gettext` - .pot ファイル生成
  - `make ja-update` - .po ファイル更新
  - `make ja-build` - 日本語版ビルド
  - `make ja-stats` - 翻訳統計表示

### 4. 既存翻訳の分析

スキャン結果:
- **161ファイル** に日本語コンテンツ
- **3,258ブロック** の翻訳
- 詳細は `MIGRATION_REPORT.md` と `TRANSLATION_MAPPING.md` 参照

## ⏳ 次に必要なステップ

### 重要な決定事項

以下の3つのオプションから選択してください：

#### オプション1: 完全移行（推奨）

**内容**: すべてのRSTを英語に戻し、完全に .po ベースへ移行

**メリット**:
- 上流の変更に完全に追従可能
- 標準的なワークフロー
- 長期的に最も効率的

**手順**: `MIGRATION_NEXT_STEPS.md` の「オプション1」参照

**期間**: 数日〜数週間（翻訳の移行作業による）

#### オプション2: 段階的移行

**内容**: セクションごとに少しずつ .po ベースへ移行

**メリット**:
- リスクが低い
- 学習しながら進められる
- 既存の翻訳も並行して使える

**手順**: `MIGRATION_NEXT_STEPS.md` の「オプション2」参照

**期間**: 数週間〜数ヶ月

#### オプション3: テスト移行

**内容**: 小さなファイルで試してから決定

**メリット**:
- コミットメント不要
- 実際に試してから判断
- 理解を深められる

**手順**: `MIGRATION_NEXT_STEPS.md` の「オプション3」参照

**期間**: 1-2日

### 推奨フロー

```
1. WHY_PO_TRANSLATION.md を読む
   └─> 移行の利点を理解
   
2. チームで議論・決定
   └─> どのオプションにするか
   
3. MIGRATION_NEXT_STEPS.md を読む
   └─> 選んだオプションの手順を確認
   
4. テストまたは移行を実施
   └─> 段階的に進める
   
5. PO_TRANSLATION_WORKFLOW.md を使用
   └─> 日常的な翻訳作業
```

## 🚀 クイックスタート（テスト移行）

今すぐ試したい場合:

```bash
# 1. 上流リポジトリを追加
git remote add upstream https://github.com/FIRST-Tech-Challenge/ftcdocs.git
git fetch upstream

# 2. 1つのファイルを英語に戻す
git checkout upstream/main -- docs/source/index.rst

# 3. .pot ファイルを生成
cd docs
make gettext

# 4. 日本語 .po ファイルを作成
make ja-update

# 5. index.po を翻訳（テキストエディタで）
vim locale/ja/LC_MESSAGES/index.po

# 6. 日本語版をビルド
make ja-build

# 7. 確認
python -m http.server 8000 --directory build/html/ja
# ブラウザで http://localhost:8000 を開く
```

## 📊 移行の影響

### Before (現在)
```
docs/source/
├── index.rst               (日本語)
├── tutorial.rst            (日本語)
└── hardware.rst            (日本語)

上流更新時:
└── git merge upstream/main
    └── 161個のコンフリクト！
```

### After (.po ベース)
```
docs/
├── source/
│   ├── index.rst           (英語 - 上流と同期)
│   ├── tutorial.rst        (英語 - 上流と同期)
│   └── hardware.rst        (英語 - 上流と同期)
│
└── locale/ja/LC_MESSAGES/
    ├── index.po            (日本語翻訳)
    ├── tutorial.po         (日本語翻訳)
    └── hardware.po         (日本語翻訳)

上流更新時:
└── git merge upstream/main
    ├── コンフリクトなし！
    └── make ja-update
        └── 変更箇所だけ翻訳
```

## 💡 重要なポイント

### 1. mainブランチの扱い

**現在**: mainブランチは日本語

**移行後**: mainブランチは英語（上流と同期）
- 日本語翻訳は `locale/ja/` で管理
- ビルド時に言語を指定: `make ja-build`

### 2. 既存の翻訳

**心配不要**: すべての翻訳は保存されています
- `TRANSLATION_MAPPING.md` に全て抽出済み
- .po ファイルに手動で移行
- または段階的に移行

### 3. 学習曲線

**.po ファイルは簡単**:
```po
# これだけ覚えればOK
msgid "English text"
msgstr "日本語テキスト"
```

### 4. ツールのサポート

以下のツールが使えます:
- **Poedit**: 無料のGUIエディタ
- **VS Code**: i18n Ally拡張機能
- **Weblate**: オンライン翻訳プラットフォーム
- **任意のテキストエディタ**: .poファイルはプレーンテキスト

## 📚 リソース

### このリポジトリ内

- 📖 `WHY_PO_TRANSLATION.md` - なぜ移行するのか
- 🗺️ `MIGRATION_NEXT_STEPS.md` - 次のステップ
- 🔧 `PO_TRANSLATION_WORKFLOW.md` - 日常のワークフロー
- 📘 `MIGRATION_TO_PO_GUIDE.md` - 技術詳細
- 📊 `TRANSLATION_MAPPING.md` - 既存翻訳
- 📋 `MIGRATION_REPORT.md` - スキャン結果

### 外部リソース

- [Sphinx i18n Guide](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)
- [sphinx-intl Documentation](https://sphinx-intl.readthedocs.io/)
- [Poedit](https://poedit.net/)
- [GNU gettext Manual](https://www.gnu.org/software/gettext/manual/)

## 🤝 サポートとフィードバック

質問や問題がある場合:
1. まず該当するドキュメントを確認
2. GitHub Issue を作成
3. チームで議論

## まとめ

✅ **完了**: 移行のための準備は全て整いました

⏳ **次のステップ**: チームで決定し、移行を開始

📈 **期待される効果**:
- 上流の変更への追従が容易に
- 翻訳作業の効率化
- チーム協力の改善
- 長期的なメンテナンスコストの削減

**移行は一度の投資で、長期的に大きなメリットがあります！**

---

## 連絡先

- GitHub: このリポジトリの Issues
- プロジェクト: Team 33678 Tezukayama

**質問があれば遠慮なくお尋ねください！**
