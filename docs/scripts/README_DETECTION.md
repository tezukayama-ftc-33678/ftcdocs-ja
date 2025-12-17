# 未翻訳検出ツール

日本語HTMLビルドと英語版を比較して、未翻訳の英語が残っている箇所を自動検出するツールです。

## ファイル

- **detect_untranslated_simple.py**: シンプル版（Windows対応、推奨）
- **detect_untranslated.py**: フル機能版（自動修正機能付き、開発中）

## 使い方

### 1. HTMLビルドを準備

まず、日本語版と英語版の両方をビルドします：

```powershell
cd docs
make clean
make html-ja    # 日本語版
make html       # 英語版（比較用）
```

### 2. 検出を実行

```powershell
python scripts\detect_untranslated_simple.py
```

## 出力例

```
======================================================================
日本語HTMLビルド 未翻訳検出ツール
======================================================================
スキャン対象: C:\...\ftcdocs-ja\docs\build\html-ja

[FILE] hardware_and_software_configuration\self_inspect\self-inspect.html
  [HIGH] p: 'Item 12 rejects the presence of an RC app installed...'
  [MED]  strong: 'Android 8'
  [HIGH] li: 'Item 4 appears only on the Driver Hub...'
  ... 他 15 件

======================================================================
[STATS] スキャン結果
======================================================================
チェックしたファイル数: 245
問題が見つかったファイル数: 87
未翻訳の可能性がある箇所: 1523

[TOP] 頻出する未翻訳テキスト (Top 10):
  45回: 'Required Item(s)'
  32回: 'Note that'
  28回: 'For example'
  ...

[OK] 詳細レポート: untranslated_report.json
```

## レポートファイル

`docs/untranslated_report.json` に詳細な検出結果が保存されます：

```json
{
  "stats": {
    "files_checked": 245,
    "files_with_issues": 87,
    "total_issues": 1523
  },
  "issues": [
    {
      "file": "path/to/file.html",
      "text": "This is untranslated English text",
      "context": "p.some-class"
    }
  ]
}
```

## 検出ロジック

以下の英語テキストを検出します：

1. **長い英文**: 3単語以上の英語センテンス
2. **英語比率**: テキスト中の80%以上がASCIIアルファベット

以下は**除外**されます：

- 技術用語（FIRST, FTC, SDK, USB, Android, Java, REV等）
- 数字のみ
- ファイル名・パス
- コードブロック内のテキスト

## 次のステップ

検出された未翻訳箇所は、対応するPOファイルを修正してください：

1. 問題のHTMLファイルパスから対応するRSTファイルを特定
2. `locales/ja/LC_MESSAGES/` 配下の対応するPOファイルを編集
3. `make clean` → `make html-ja` で再ビルド
4. 再度スクリプトを実行して確認

## トラブルシューティング

### Unicode エンコードエラー

Windows環境で絵文字が表示できない場合、スクリプトは自動的に対応します。

### 誤検出が多い場合

`ALLOWED_TERMS` セットに許可する用語を追加してください：

```python
ALLOWED_TERMS = {
    'FIRST', 'Tech', 'Challenge',
    # 追加する用語をここに
    'YourTerm', 'AnotherTerm',
}
```

### ファイルが見つからない

HTMLビルドが存在することを確認：

```powershell
Test-Path docs\build\html-ja
```

存在しない場合は `make html-ja` を実行してください。
