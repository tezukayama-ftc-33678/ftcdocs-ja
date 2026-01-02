# ローカルLLM翻訳環境のセットアップ（VRAM 8GB対応）

## 1. Ollamaのインストール

### Windows版Ollamaのインストール
1. [Ollama公式サイト](https://ollama.com/download/windows)からインストーラーをダウンロード
2. `OllamaSetup.exe`を実行してインストール
3. PowerShellで確認:
   ```powershell
   ollama --version
   ```

### 推奨モデルのダウンロード（VRAM 8GB対応）
以下のモデルから選択:

#### 🏆 推奨1: Qwen2.5-Coder 7B Instruct（RST構文に最適）
```powershell
ollama pull qwen2.5-coder:7b-instruct
```
- VRAM使用量: 約6GB
- **RST構文保護**: 優秀（コード生成モデル）
- 日本語翻訳品質: 優秀
- 速度: 中速
- **特徴**: マークアップ構文を理解し、正確に保持

#### 推奨2: Qwen2.5 7B Instruct（汎用翻訳）
```powershell
ollama pull qwen2.5:7b-instruct-q5_K_M
```
- VRAM使用量: 約6GB
- 日本語翻訳品質: 優秀
- 速度: 中速

#### 推奨3: Gemma 2 9B Instruct（高品質）
```powershell
ollama pull gemma2:9b-instruct-q4_K_M
```
- VRAM使用量: 約7GB
- 日本語翻訳品質: 非常に優秀
- 速度: やや遅め

#### 推奨4: Llama 3.1 8B Instruct（高速）
```powershell
ollama pull llama3.1:8b-instruct-q5_K_M
```
- VRAM使用量: 約6GB
- 日本語翻訳品質: 良好
- 速度: 高速

### モデルのテスト
```powershell
ollama run qwen2.5:7b-instruct-q5_K_M "翻訳テスト: Hello World"
```

## 2. Python環境のセットアップ

### 必要なパッケージのインストール
```powershell
pip install ollama polib tqdm colorama
```

### パッケージ説明
- `ollama`: Ollama Python SDK
- `polib`: POファイル操作ライブラリ
- `tqdm`: 進捗バー表示
- `colorama`: ターミナル色付け（Windows対応）

## 3. 動作確認

### Ollama APIのテスト
```powershell
python -c "import ollama; print(ollama.list())"
```

ダウンロードしたモデルが表示されればOK。

## 4. 設定ファイルの作成

`translate_config.json`を作成:
```json
{
  "model": "qwen2.5:7b-instruct-q5_K_M",
  "temperature": 0.3,
  "max_retries": 3,
  "batch_size": 10,
  "context_window": 4096,
  "checkpoint_interval": 50
}
```

## トラブルシューティング

### VRAM不足エラーが出る場合
より軽量な量子化版を使用:
```powershell
ollama pull qwen2.5:7b-instruct-q4_K_M
```

### Ollamaサービスが起動しない
```powershell
# サービスの再起動
net stop ollama
net start ollama
```

### GPU認識されない場合
```powershell
# CUDA確認
nvidia-smi

# Ollama環境変数確認
$env:OLLAMA_GPU_DRIVER
```

## 次のステップ

### 新しい構文保護型翻訳スクリプト（推奨）

前回の翻訳でRST構文が崩れた経験から、新しい賢い翻訳システムを作成しました：

```powershell
# 単一ファイルをテスト翻訳
python scripts/translate_po_smart.py locales/ja/LC_MESSAGES/index.po --test

# 単一ファイルを翻訳
python scripts/translate_po_smart.py locales/ja/LC_MESSAGES/index.po

# 全ファイルをバッチ翻訳
python scripts/batch_translate_smart.py locales/ja/LC_MESSAGES
```

**新システムの特徴**:
- ✅ RST構文を事前抽出・保護
- ✅ 段落単位の小チャンク翻訳（VRAM 8GBでも安全）
- ✅ 日本語マークアップ前後の空白を自動追加
- ✅ 構文に強いQwen2.5-Coderを使用
- ✅ 用語集（GLOSSARY.md）の自動適用

詳細は `guides/SMART_TRANSLATE_GUIDE.md` を参照してください。

### 従来の翻訳スクリプト

シンプルな翻訳には `AUTO_TRANSLATE.md` の手順を参照してください。
