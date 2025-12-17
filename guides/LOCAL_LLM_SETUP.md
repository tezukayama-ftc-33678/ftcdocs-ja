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
以下のモデルから選択（日本語性能順）:

#### 推奨1: Qwen2.5 7B Instruct（最もバランスが良い）
```powershell
ollama pull qwen2.5:7b-instruct-q5_K_M
```
- VRAM使用量: 約6GB
- 日本語翻訳品質: 優秀
- 速度: 中速

#### 推奨2: Gemma 2 9B Instruct（高品質）
```powershell
ollama pull gemma2:9b-instruct-q4_K_M
```
- VRAM使用量: 約7GB
- 日本語翻訳品質: 非常に優秀
- 速度: やや遅め

#### 推奨3: Llama 3.1 8B Instruct（安定）
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
セットアップ完了後、`AUTO_TRANSLATE.md`の手順に従って自動翻訳を実行してください。
