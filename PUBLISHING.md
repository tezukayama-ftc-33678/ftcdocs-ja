# Read the Docs 公開ガイド

このドキュメントでは、日本語翻訳版FTCドキュメントをRead the Docsで公開するための手順を説明します。

## 前提条件の確認

### 1. ライセンスと法的事項

✅ **完了済み**
- 原文はBSD 3-Clause Licenseの下で公開されており、翻訳・再配布が許可されています
- `LICENSE-JA.md`に翻訳版の位置づけを明記
- フッターに非公式翻訳であることを明示
- 原文へのリンクと著作権表示を保持

### 2. FIRSTロゴとブランド資産の使用

✅ **使用可能**
- 原文のドキュメントに含まれるFIRSTロゴは、ドキュメント内での使用が許可されています
- 翻訳版でも同じ使用範囲内で使用可能
- ロゴファイル: `docs/source/assets/FIRST*.png`, `docs/source/assets/FIRST*.ico`
- **重要**: ロゴは削除せず、原文通り使用してください

### 3. 翻訳版としての免責事項

✅ **設定済み**
以下の場所で明確に表示されています：
- トップページ (`docs/source/index.rst`)
- README.md
- フッター (`docs/source/_templates/footer.html`)
- LICENSE-JA.md

## Read the Docs プロジェクト設定手順

### ステップ1: Read the Docsアカウントの準備

1. https://readthedocs.org にアクセス
2. GitHubアカウントでサインイン（推奨）
3. アカウントを作成/ログイン

### ステップ2: プロジェクトのインポート

1. ダッシュボードで「Import a Project」をクリック
2. GitHubリポジトリ一覧から `tezukayama-ftc-33678/ftcdocs-ja` を選択
3. プロジェクト設定:
   - **Name**: `ftcdocs-ja` または `ftc-docs-japanese`
   - **Repository URL**: `https://github.com/tezukayama-ftc-33678/ftcdocs-ja`
   - **Default branch**: `main`（または現在のデフォルトブランチ）

### ステップ3: 高度な設定（Admin > Advanced Settings）

以下の設定を確認・変更してください：

#### 言語設定
- **Language**: `ja - Japanese` を選択

#### ビルド設定
- **Documentation type**: `Sphinx Html`
- **Requirements file**: `docs/requirements.txt`
- **Python configuration file**: `docs/source/conf.py`
- **Default version**: `latest`

#### プログラミング言語
- **Programming Language**: `Python`

#### その他の設定
- **Privacy Level**: `Public`（公開する場合）
- **Show version warning**: 有効化（推奨）

### ステップ4: 環境変数の設定（オプション）

Admin > Environment Variables で以下を設定（必要に応じて）:

```
SPHINXOPTS=-D language=ja
```

### ステップ5: ビルドのトリガー

1. 「Builds」タブに移動
2. 「Build Version」をクリック
3. 「latest」または「main」を選択してビルド開始

### ステップ6: ビルド結果の確認

ビルドが完了したら：
1. ビルドログを確認（エラーがないか）
2. 「View Docs」をクリックして実際のドキュメントを確認
3. フッターの免責事項が正しく表示されているか確認

## カスタムドメインの設定（オプション）

Read the Docsの無料プランでは、デフォルトで以下のようなURLになります：
- `https://ftcdocs-ja.readthedocs.io/ja/latest/`

カスタムドメインを使用したい場合：
1. Admin > Domains でドメインを追加
2. DNSレコードを設定（CNAMEレコード）
3. SSL証明書は自動的に設定されます

## ビルド設定の詳細

### .readthedocs.yaml の設定

プロジェクトルートの `.readthedocs.yaml` ファイルで以下を設定済み：

```yaml
version: 2

sphinx:
  configuration: docs/source/conf.py
  fail_on_warning: false

formats:
  - pdf

build:
  os: "ubuntu-22.04"
  tools:
    python: "3.9"
  jobs:
    pre_build:
      - echo "Building Japanese documentation"

python:
  install:
    - requirements: docs/requirements.txt
```

### conf.py の日本語設定

`docs/source/conf.py` で以下が設定済み：

```python
# 言語設定（デフォルト）
language = os.environ.get('SPHINXOPTS', '').replace('-D language=', '').strip() or 'en'

# 翻訳ファイルの場所
locale_dirs = ["locale/", "../../locales/"]
gettext_compact = False
```

## トラブルシューティング

### ビルドエラーが発生する場合

1. **依存関係エラー**
   - `docs/requirements.txt` のパッケージが正しくインストールされているか確認
   - Read the Docsのビルドログで具体的なエラーメッセージを確認

2. **Sphinx警告/エラー**
   - ローカルで `make html-ja` を実行してエラーを確認
   - `.readthedocs.yaml` で `fail_on_warning: false` を設定

3. **翻訳ファイルが見つからない**
   - `locales/ja/LC_MESSAGES/` ディレクトリが存在するか確認
   - `.mo` ファイルが生成されているか確認（POファイルからコンパイル）

### 日本語が表示されない場合

1. Read the Docs管理画面で言語設定が `ja` になっているか確認
2. URLに `/ja/latest/` が含まれているか確認
3. ブラウザの言語設定を確認

### PDFビルドエラー

日本語PDFビルドにはフォント設定が必要です。
PDF生成でエラーが出る場合は、`.readthedocs.yaml` の `formats` から `pdf` を削除できます。

## バージョン管理

### バージョニング戦略

1. **latest**: 最新の開発版（mainブランチ）
2. **stable**: 安定版（タグまたはリリースブランチ）
3. **特定バージョン**: `v1.0`, `v2.0` など

### タグベースのバージョン公開

```bash
# バージョンタグを作成
git tag -a v1.0.0-ja -m "Japanese translation v1.0.0"
git push origin v1.0.0-ja
```

Read the Docsで自動的に新しいバージョンとしてビルドされます。

## アクセス統計

Read the Docs Pro（有料版）では、アクセス統計を確認できます。
無料版では、Google Analyticsなどの外部サービスを使用してください。

## メンテナンスとアップデート

### 定期的な更新

1. **原文の更新を追跡**
   - 原文リポジトリ: https://github.com/FIRST-Tech-Challenge/ftcdocs
   - 変更をフォローして翻訳を更新

2. **翻訳の改善**
   - コミュニティからのフィードバックを受け付け
   - Issues/PRで改善提案を募集

3. **ビルドの確認**
   - 定期的にビルドが成功しているか確認
   - エラーや警告を修正

## セキュリティとプライバシー

### 個人情報の取り扱い

- Read the Docsの利用規約とプライバシーポリシーに従ってください
- アクセスログは Read the Docs によって管理されます
- カスタムアナリティクスを追加する場合は、プライバシーポリシーを明記

### アクセス制限

無料版では公開のみですが、Pro版では：
- プライベートプロジェクト
- パスワード保護
- チーム内限定公開

## サポートとコミュニティ

### 質問や問題がある場合

1. **Read the Docs ドキュメント**: https://docs.readthedocs.io/
2. **GitHub Issues**: このリポジトリのIssues
3. **Read the Docs コミュニティ**: https://readthedocs.org/sustainability/

## ライセンスと引用

このドキュメントを引用する場合：

```
FIRST Tech Challenge ドキュメント 日本語翻訳版
翻訳: Team 33678 Tezukayama
原文: https://ftc-docs.firstinspires.org
翻訳版: [あなたのRead the Docs URL]
ライセンス: BSD 3-Clause License
```

## チェックリスト: 公開前の最終確認

- [ ] LICENSE-JA.md が存在し、内容が正確
- [ ] フッターに免責事項が表示される
- [ ] トップページに警告が表示される
- [ ] 原文へのリンクが機能する
- [ ] FIRSTロゴが正しく表示される
- [ ] .readthedocs.yaml の設定が正しい
- [ ] ビルドがエラーなく完了する
- [ ] 主要なページが正しく翻訳・表示される
- [ ] ナビゲーションが機能する
- [ ] 検索機能が日本語で動作する

## 次のステップ

公開後：
1. READMEにRead the DocsのURLを追加
2. GitHubリポジトリの説明とウェブサイトリンクを更新
3. コミュニティに公開を通知
4. フィードバックを収集して継続的に改善

---

**注意**: このガイドは2024年12月時点の情報に基づいています。Read the Docsの仕様は変更される可能性がありますので、公式ドキュメントも併せてご確認ください。
