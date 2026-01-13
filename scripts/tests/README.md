# テストスイート

コアモジュールのユニットテストを提供します。

## テストの実行

### すべてのテストを実行

```bash
cd scripts
python -m pytest tests/ -v
```

または

```bash
cd scripts/tests
python -m unittest discover -v
```

### 個別のテストファイルを実行

```bash
cd scripts
python -m pytest tests/test_rst_protector.py -v
python -m pytest tests/test_po_file_handler.py -v
python -m pytest tests/test_quality_checker.py -v
python -m pytest tests/test_token_estimator.py -v
```

または

```bash
cd scripts/tests
python test_rst_protector.py
python test_po_file_handler.py
python test_quality_checker.py
python test_token_estimator.py
```

### カバレッジレポートを生成

```bash
cd scripts
python -m pytest tests/ --cov=core --cov-report=html
```

カバレッジレポートは `htmlcov/index.html` に生成されます。

## テストファイル

| ファイル | テスト対象 | 説明 |
|---------|----------|------|
| `test_rst_protector.py` | `core/rst_protector.py` | RSTマークアップ保護・復元、日本語スペース処理 |
| `test_po_file_handler.py` | `core/po_file_handler.py` | POファイルI/O、msgid保護、統計情報 |
| `test_quality_checker.py` | `core/quality_checker.py` | 中国語検出、日本語検証、品質チェック |
| `test_token_estimator.py` | `core/token_estimator.py` | トークン数推定、コスト計算 |

## テストカバレッジ目標

- **目標: 80%以上**
- 各コアモジュールの主要機能を網羅
- エッジケースとエラーハンドリングをテスト

## テストの種類

### 1. 基本機能テスト
- 各モジュールの主要機能が正しく動作することを確認
- 正常系のテストケース

### 2. エッジケーステスト
- 空文字列、非常に長いテキスト、特殊文字などの処理
- 境界値のテスト

### 3. エラーハンドリングテスト
- 不正な入力に対する適切なエラー処理
- 例外の発生と捕捉

### 4. 統合テスト
- 複数のモジュールが連携して動作することを確認
- 実際の使用シナリオに近いテスト

## 依存関係

テスト実行には以下のパッケージが必要です:

```bash
pip install pytest pytest-cov polib
```

## CI/CD統合

GitHubActionsなどのCI/CDパイプラインで自動実行できます:

```yaml
- name: Run tests
  run: |
    cd scripts
    python -m pytest tests/ -v --cov=core
```

## テストの追加

新しいコアモジュールを追加する場合:

1. `tests/test_<module_name>.py` を作成
2. `unittest.TestCase` を継承したテストクラスを作成
3. `test_*` で始まるテストメソッドを追加
4. このREADMEに追加したテストファイルを記載

## トラブルシューティング

### ImportError: No module named 'core'

```bash
cd scripts
python -m pytest tests/
```

スクリプトディレクトリから実行してください。

### PermissionError: ファイルにアクセスできません

テスト実行中に一時ファイルが削除されない場合があります。
`tearDown()` メソッドでクリーンアップが正しく実行されているか確認してください。

## 参考資料

- [Python unittest documentation](https://docs.python.org/3/library/unittest.html)
- [pytest documentation](https://docs.pytest.org/)
- [Coverage.py documentation](https://coverage.readthedocs.io/)
