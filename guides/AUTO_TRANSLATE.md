# 完全自動翻訳実行ガイド

このガイドに従って実行すれば、**放置するだけで全PO翻訳が完了**します。

## 📋 前提条件チェックリスト

実行前に以下を確認してください：

- [ ] NVIDIA GPU搭載（VRAM 8GB以上）
- [ ] Windows 10/11
- [ ] Python 3.8以上インストール済み
- [ ] Git for Windowsインストール済み
- [ ] 十分なディスク空き容量（20GB以上推奨）

## 🚀 ステップ1: 環境セットアップ（初回のみ）

### 1.1 Ollamaのインストール

```powershell
# Ollamaをダウンロード＆インストール
# https://ollama.com/download/windows からインストーラーをダウンロードして実行

# インストール確認
ollama --version
```

### 1.2 推奨LLMモデルのダウンロード

以下のいずれか1つを選択（推奨順）：

#### 推奨1: Qwen2.5 7B（バランス型）
```powershell
ollama pull qwen2.5:7b-instruct-q5_K_M
```
- **翻訳品質**: ★★★★☆
- **速度**: ★★★★☆
- **VRAM**: 約6GB

#### 推奨2: Gemma 2 9B（高品質）
```powershell
ollama pull gemma2:9b-instruct-q4_K_M
```
- **翻訳品質**: ★★★★★
- **速度**: ★★★☆☆
- **VRAM**: 約7GB

#### 推奨3: Llama 3.1 8B（高速）
```powershell
ollama pull llama3.1:8b-instruct-q5_K_M
```
- **翻訳品質**: ★★★★☆
- **速度**: ★★★★★
- **VRAM**: 約6GB

### 1.3 Pythonパッケージのインストール

```powershell
cd h:\ftcdocs-ja

# 必要なパッケージをインストール
pip install ollama polib tqdm colorama
```

### 1.4 設定ファイルの確認

`translate_config.json`を開いて、ダウンロードしたモデル名を確認：

```json
{
  "model": "qwen2.5:7b-instruct-q5_K_M",
  "temperature": 0.3,
  "max_retries": 3,
  "batch_size": 10,
  "skip_translated": true,
  "quality_check_enabled": true,
  "auto_fix_common_errors": true
}
```

モデル名を変更した場合は `"model"` の値を修正してください。

## 🎯 ステップ2: 自動翻訳の実行

### 2.1 完全自動モード（推奨）

**これを実行したら放置するだけ！** 数時間後に全て完了します。

```powershell
cd h:\ftcdocs-ja

# バッチ翻訳開始（完全自動）
python tools/translation/batch_translate.py --po-dir locales/ja/LC_MESSAGES
```

実行されること：
1. ✅ 全POファイルを自動検出
2. ✅ 未翻訳エントリを順次翻訳
3. ✅ 10ファイルごとに自動保存（中断しても再開可能）
4. ✅ 翻訳完了後に品質チェック
5. ✅ 最終的にHTMLビルド検証

### 2.2 進捗確認

別のPowerShellウィンドウで進捗確認：

```powershell
# 進捗ファイルの確認
cat translation_progress.json

# リアルタイムログ確認（オプション）
Get-Content batch_translate.log -Wait -Tail 20
```

### 2.3 中断と再開

**中断した場合でも安心**: 進捗は自動保存されています。

```powershell
# 再開（前回の続きから自動再開）
python tools/translation/batch_translate.py --po-dir locales/ja/LC_MESSAGES
```

## 📊 ステップ3: 結果の確認

翻訳完了後に以下を確認：

### 3.1 統計サマリー

翻訳完了時に自動表示される統計：
- 総ファイル数
- 翻訳完了数
- スキップ数
- エラー数
- 成功率

### 3.2 品質チェック結果

`po_issues.json`に問題がリストされます：

```powershell
# 問題の確認
cat po_issues.json | ConvertFrom-Json
```

### 3.3 ビルド結果

`docs/build/html-ja/`にHTMLが生成されます：

```powershell
# ブラウザで確認
start docs/build/html-ja/index.html
```

## 🔧 ステップ4: 問題があった場合の対処

### 4.1 品質チェックで警告が出た場合

自動修正スクリプトを実行：

```powershell
cd docs
python tools/archived/fix_po_issues.py --po-dir ../locales/ja/LC_MESSAGES --issues ../po_issues.json
```

### 4.2 特定のファイルだけ再翻訳

```powershell
# 単一ファイルを再翻訳
python tools/translation/translate_po.py locales/ja/LC_MESSAGES/index.po --no-skip
```

### 4.3 全てリセットして再実行

```powershell
# 進捗をリセット（全て最初からやり直し）
python tools/translation/batch_translate.py --po-dir locales/ja/LC_MESSAGES --reset-progress
```

## ⚡ 高度なオプション

### 既に翻訳済みのエントリも再翻訳

```powershell
# translate_config.json を編集
{
  "skip_translated": false  # true から false に変更
}

python tools/translation/batch_translate.py --po-dir locales/ja/LC_MESSAGES
```

### ビルド検証をスキップ（翻訳のみ）

```powershell
python tools/translation/batch_translate.py --po-dir locales/ja/LC_MESSAGES --skip-build
```

### モデルの切り替え

```powershell
# translate_config.json で別のモデルに変更
{
  "model": "gemma2:9b-instruct-q4_K_M"
}
```

### 並列処理（複数ファイルを同時に翻訳）

現在は順次処理ですが、将来対応予定。

## 📈 予想処理時間

環境により異なりますが、目安：

| モデル | 1ファイルあたり | 全体（約500ファイル） |
|--------|----------------|---------------------|
| Qwen2.5 7B | 2-5分 | 20-40時間 |
| Gemma 2 9B | 3-7分 | 25-60時間 |
| Llama 3.1 8B | 1-3分 | 10-25時間 |

※エントリ数や内容により変動します

## 🎉 完了後のチェックリスト

全翻訳完了後：

- [ ] `po_issues.json`で重大な問題がないか確認
- [ ] `docs/build/html-ja/index.html`をブラウザで開いてUI崩れがないか目視
- [ ] 重要ページ（persona_pages, gp等）を確認
- [ ] ビルド警告数が許容範囲内（50件以下推奨）
- [ ] Gitでコミット＆プッシュ

## 🆘 トラブルシューティング

### メモリ不足エラー

より軽量なモデルに切り替え：
```powershell
ollama pull qwen2.5:7b-instruct-q4_K_M  # Q5からQ4へ
```

### OllamaがGPUを認識しない

```powershell
# CUDA確認
nvidia-smi

# Ollama再起動
net stop ollama
net start ollama
```

### 翻訳品質が低い

温度パラメータを下げる（translate_config.json）：
```json
{
  "temperature": 0.1  # 0.3から0.1へ
}
```

### 処理が遅すぎる

より高速なモデルに切り替え：
```powershell
ollama pull llama3.1:8b-instruct-q5_K_M
```

## 📚 参考ドキュメント

- [LOCAL_LLM_SETUP.md](LOCAL_LLM_SETUP.md) - 詳細なセットアップガイド
- [COPILOT_TRANSLATION_PROMPT.md](COPILOT_TRANSLATION_PROMPT.md) - 翻訳品質ガイドライン
- [BUILD_JA.md](BUILD_JA.md) - ビルド手順
- [docs/scripts/README.md](docs/scripts/README.md) - 品質チェックツール

## 💡 ヒント

1. **夜間実行推奨**: 処理には時間がかかるため、寝る前に実行して朝確認
2. **電源設定**: スリープモードを無効にしておく
3. **モニタリング**: 進捗ファイルを定期的に確認
4. **バックアップ**: 翻訳前にlocalesディレクトリをバックアップ推奨

---

## 🚀 クイックスタート（3コマンドで完了）

```powershell
# 1. モデルダウンロード
ollama pull qwen2.5:7b-instruct-q5_K_M

# 2. 依存パッケージインストール
pip install ollama polib tqdm colorama

# 3. 翻訳開始（あとは放置）
python tools/translation/batch_translate.py --po-dir locales/ja/LC_MESSAGES
```

**以上！数時間後に全て完了しています 🎉**
