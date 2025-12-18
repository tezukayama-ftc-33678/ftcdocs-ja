# 🎉 ローカルLLM自動翻訳システム - 完成！

## 📦 作成されたファイル一覧

### 📘 ドキュメント
1. **[LOCAL_LLM_SETUP.md](LOCAL_LLM_SETUP.md)** - 環境構築ガイド（Ollama、モデル選定）
2. **[AUTO_TRANSLATE.md](AUTO_TRANSLATE.md)** - 完全自動翻訳実行ガイド（メイン手順書）
3. **[README.md](README.md)** - 更新済み（自動翻訳セクション追加）

### ⚙️ 設定ファイル
4. **[translate_config.json](translate_config.json)** - 翻訳設定（モデル、温度、リトライ等）

### 🐍 Pythonスクリプト
5. **[translate_po.py](translate_po.py)** - 単一POファイル翻訳スクリプト
6. **[batch_translate.py](batch_translate.py)** - 全POファイル一括翻訳スクリプト（メイン）
7. **[test_translation_env.py](test_translation_env.py)** - 環境テストスクリプト

### 💻 PowerShellスクリプト
8. **[run_auto_translate.ps1](run_auto_translate.ps1)** - ワンクリック実行スクリプト

---

## 🚀 今すぐ始める（超簡単3ステップ）

### ステップ1: Ollamaインストール
https://ollama.com/download/windows からダウンロードしてインストール

### ステップ2: 環境テスト
```powershell
python test_translation_env.py
```

### ステップ3: 自動翻訳開始
```powershell
.\run_auto_translate.ps1
```

**たったこれだけ！あとは放置するだけで全翻訳が完了します 🎉**

---

## 📊 機能一覧

### ✨ 主要機能
- ✅ **完全自動翻訳**: 全POファイルを自動処理
- ✅ **VRAM 8GB対応**: 軽量モデル（Qwen2.5 7B等）
- ✅ **中断・再開可能**: 進捗自動保存、途中から再開
- ✅ **品質チェック統合**: 翻訳後に自動検証
- ✅ **リトライ機能**: エラー時自動リトライ
- ✅ **進捗表示**: tqdmによる視覚的進捗バー
- ✅ **統計レポート**: 完了後に詳細統計表示

### 🛡️ 品質保証
- `:doc:` / `:ref:` 参照の保持チェック
- `**強調**` マーカーの一致チェック
- 外部リンクの保持チェック
- Sphinx-Design記法の保護
- 空msgstr防止

### ⚡ パフォーマンス
- バッチ処理（10エントリごと保存）
- チェックポイント自動保存
- 優先順位付きファイル処理
- 既翻訳エントリスキップ可能

---

## 📋 使用方法の詳細

### 基本的な使い方

#### 1. 全自動モード（推奨）
```powershell
python batch_translate.py --po-dir locales/ja/LC_MESSAGES
```

#### 2. PowerShellラッパー使用
```powershell
.\run_auto_translate.ps1
```

#### 3. 単一ファイルのみ翻訳
```powershell
python translate_po.py locales/ja/LC_MESSAGES/index.po
```

### 高度なオプション

#### 進捗リセット（最初からやり直し）
```powershell
python batch_translate.py --po-dir locales/ja/LC_MESSAGES --reset-progress
```

#### ビルド検証をスキップ
```powershell
python batch_translate.py --po-dir locales/ja/LC_MESSAGES --skip-build
```

#### 既翻訳も再翻訳
```powershell
# translate_config.json で設定変更
{
  "skip_translated": false
}
```

#### 別のモデルを使用
```powershell
# translate_config.json で設定変更
{
  "model": "gemma2:9b-instruct-q4_K_M"
}
```

---

## 🎯 推奨モデル（VRAM 8GB）

| モデル | VRAM | 品質 | 速度 | 推奨度 |
|--------|------|------|------|--------|
| **Qwen2.5 7B** | 6GB | ★★★★☆ | ★★★★☆ | ⭐⭐⭐ |
| Gemma 2 9B | 7GB | ★★★★★ | ★★★☆☆ | ⭐⭐ |
| Llama 3.1 8B | 6GB | ★★★★☆ | ★★★★★ | ⭐⭐ |

### ダウンロードコマンド
```powershell
# 推奨
ollama pull qwen2.5:7b-instruct-q5_K_M

# 高品質優先
ollama pull gemma2:9b-instruct-q4_K_M

# 高速優先
ollama pull llama3.1:8b-instruct-q5_K_M
```

---


**💡 ヒント**: 夜間実行推奨。寝る前に開始して朝確認！

---

## 🔍 進捗確認方法

### リアルタイム進捗
翻訳中は自動的にtqdmプログレスバーが表示されます。

### 別ウィンドウで確認
```powershell
# 進捗ファイルを確認
Get-Content translation_progress.json | ConvertFrom-Json

# 現在処理中のファイル
(Get-Content translation_progress.json | ConvertFrom-Json).current_file
```

---

## 🛠️ トラブルシューティング

### メモリ不足エラー
より軽量な量子化版を使用：
```powershell
ollama pull qwen2.5:7b-instruct-q4_K_M  # Q5 → Q4
```

### Ollamaが起動しない
```powershell
net stop ollama
net start ollama
```

### 翻訳品質が低い
温度パラメータを下げる（`translate_config.json`）：
```json
{
  "temperature": 0.1
}
```

### 処理が遅すぎる
より高速なモデルに変更：
```powershell
ollama pull llama3.1:8b-instruct-q5_K_M
```

---

## 📊 完了後の確認

### 1. 品質チェック結果
```powershell
cat po_issues.json | ConvertFrom-Json
```

### 2. ビルド結果
```powershell
start docs\build\html-ja\index.html
```

### 3. 警告数確認
ビルドログで警告数を確認（50件以下が目安）

---

## 🔄 ワークフロー全体図

```
1. 環境セットアップ
   ↓
2. テスト実行 (test_translation_env.py)
   ↓
3. 自動翻訳開始 (batch_translate.py)
   ├─ POファイル検索
   ├─ 優先順位ソート
   ├─ 順次翻訳 (translate_po.py)
   │   ├─ LLM呼び出し
   │   ├─ 品質チェック
   │   ├─ リトライ処理
   │   └─ 定期保存
   ├─ 全体品質チェック (check_and_fix_po.py)
   └─ HTMLビルド検証 (make html-ja)
   ↓
4. 結果確認・修正
   ↓
5. コミット＆プッシュ
```

---

## 📚 詳細ドキュメント

- **[AUTO_TRANSLATE.md](AUTO_TRANSLATE.md)** - 詳細な実行手順
- **[LOCAL_LLM_SETUP.md](LOCAL_LLM_SETUP.md)** - 環境構築詳細
- **[COPILOT_TRANSLATION_PROMPT.md](COPILOT_TRANSLATION_PROMPT.md)** - 翻訳品質ガイドライン
- **[BUILD_JA.md](BUILD_JA.md)** - ビルド手順
- **[docs/scripts/README.md](docs/scripts/README.md)** - 品質チェックツール

---

## 🎓 使用技術

- **LLMフレームワーク**: Ollama
- **言語**: Python 3.8+
- **主要ライブラリ**:
  - `ollama` - LLM API
  - `polib` - POファイル操作
  - `tqdm` - プログレスバー
  - `colorama` - ターミナル色付け
- **推奨モデル**: Qwen2.5 7B Instruct
- **量子化**: Q5_K_M / Q4_K_M

---

## 💡 ベストプラクティス

### 🌙 夜間実行
- 処理時間が長いため、就寝前に開始
- 電源設定でスリープを無効化

### 💾 定期バックアップ
- 翻訳前に`locales`ディレクトリをバックアップ
- Gitで定期コミット

### 🔍 段階的確認
- 10ファイルごとに品質チェック
- 重要ファイル（index, persona_pages等）を優先確認

### 🎯 モデル選定
- 初回: Qwen2.5 7B（バランス型）
- 品質重視: Gemma 2 9B
- 速度重視: Llama 3.1 8B

---

## 🙏 謝辞

このシステムは以下の技術を活用しています：
- [Ollama](https://ollama.com/) - ローカルLLM実行環境
- [Qwen2.5](https://qwenlm.github.io/) - 高性能言語モデル
- [polib](https://github.com/izimobil/polib) - POファイル操作
- [Sphinx](https://www.sphinx-doc.org/) - ドキュメント生成

---

## 📞 サポート

問題が発生した場合：
1. `test_translation_env.py`で環境確認
2. `translation_progress.json`で進捗確認
3. `po_issues.json`で品質問題確認
4. トラブルシューティングセクション参照

---

**🚀 さあ、今すぐ始めましょう！**

```powershell
.\run_auto_translate.ps1
```

**放置するだけで全翻訳完了！🎉**
