# 中国語混入箇所の自動修正ガイド

このガイドでは、LLM翻訳時に誤って混入した中国語（簡体字）を検出し、正しい日本語に自動再翻訳する方法を説明します。

## 📋 前提条件

- Ollamaがインストール済み
- 翻訳用LLMモデルがダウンロード済み（Qwen2.5, Gemma2など）
- Python 3.8以上

## 🚀 クイックスタート（3ステップ）

### ステップ1: 中国語混入箇所を検出

```powershell
cd h:\ftcdocs-ja

# 検出スクリプトを実行（レポート生成）
python tools/analysis/detect_chinese_chars.py
```

**出力**: 
- `chinese_chars_report.md` - 詳細レポート
- コンソールに問題ファイル一覧

### ステップ2: 自動修正を実行

```powershell
# 検出された全ての中国語混入箇所を自動修正
python tools/translation/fix_chinese_errors.py --po-dir locales/ja/LC_MESSAGES
```

**これだけ！** あとは自動で：
1. ✅ 問題箇所を再スキャン
2. ✅ 英語原文から正しい日本語に翻訳
3. ✅ POファイルを自動更新
4. ✅ 進捗を自動保存

### ステップ3: 結果確認

修正完了後、再度検出して問題が残っていないか確認：

```powershell
# 再検出（問題がなければ "No Chinese characters found!" と表示）
python tools/analysis/detect_chinese_chars.py
```

## 🎯 詳細オプション

### 1. ドライラン（変更せずに検出のみ）

```powershell
# 何が修正されるかを事前確認
python tools/translation/fix_chinese_errors.py --po-dir locales/ja/LC_MESSAGES --dry-run
```

### 2. 特定のモデルを使用

```powershell
# より高品質なモデルで翻訳
python tools/translation/fix_chinese_errors.py --po-dir locales/ja/LC_MESSAGES --model gemma2:9b-instruct-q4_K_M
```

### 3. 修正済み箇所も再実行

```powershell
# 全て最初からやり直し
python tools/translation/fix_chinese_errors.py --po-dir locales/ja/LC_MESSAGES --no-skip
```

### 4. 進捗ファイルのリセット

```powershell
# 進捗をリセット
Remove-Item chinese_fix_progress.json
python tools/translation/fix_chinese_errors.py --po-dir locales/ja/LC_MESSAGES
```

## 📊 処理時間の目安

現在の検出結果（64ファイル）の場合：

| モデル | 1箇所あたり | 全体（約100箇所） |
|--------|-------------|-------------------|
| Qwen2.5 7B | 3-5秒 | 5-10分 |
| Gemma 2 9B | 5-8秒 | 8-15分 |
| Llama 3.1 8B | 2-4秒 | 3-7分 |

## 🔍 検出される問題パターン

### 1. 簡体字（日本語では使われない文字）

```
× 为了提供良好的姿态估计
○ 良いポーズ推定を提供するために
```

### 2. 中国語の文法パターン

```
× 只有在特定情况下才需要重播
○ 特定の状況でのみリプレイが必要です
```

### 3. 中国語特有の表現

```
× 可以通过设置来调整
○ 設定で調整できます
```

## 🛠️ 設定のカスタマイズ

`translate_config.json`を編集してデフォルト設定を変更：

```json
{
  "model": "qwen2.5:7b-instruct-q5_K_M",
  "temperature": 0.3,
  "max_retries": 3,
  "skip_already_fixed": true
}
```

### パラメータ説明

- **model**: 使用するOllamaモデル
- **temperature**: 翻訳の創造性（0.1-0.5推奨、低いほど安定）
- **max_retries**: 翻訳失敗時のリトライ回数
- **skip_already_fixed**: 修正済み箇所をスキップするか

## 📈 修正結果の例

### 修正前
```po
#: ../../source/apriltag/vision_portal/apriltag_camera_calibration/apriltag-camera-calibration.rst:4
msgid ""
"To provide good pose estimates, **each RC phone camera or webcam model** "
"requires calibration data, for **each specific resolution**."
msgstr "良いポーズ推定为了提供良好的姿态估计，**各RC電話カメラまたはウェブカムモデル**对于**每个特定分辨率**都需要校准数据。"
```

### 修正後
```po
#: ../../source/apriltag/vision_portal/apriltag_camera_calibration/apriltag-camera-calibration.rst:4
msgid ""
"To provide good pose estimates, **each RC phone camera or webcam model** "
"requires calibration data, for **each specific resolution**."
msgstr "良いポーズ推定を提供するために、**各RCフォンカメラまたはウェブカムモデル**には、**各特定の解像度**ごとにキャリブレーションデータが必要です。"
```

## 🔧 トラブルシューティング

### 問題: "Ollama is not running"

```powershell
# Ollamaが起動しているか確認
ollama list

# 起動していない場合
ollama serve
```

### 問題: 翻訳品質が低い

```powershell
# より高品質なモデルを使用
ollama pull gemma2:9b-instruct-q4_K_M
python tools/translation/fix_chinese_errors.py --po-dir locales/ja/LC_MESSAGES --model gemma2:9b-instruct-q4_K_M
```

### 問題: 依然として中国語が残る

```powershell
# 温度を下げて再実行（より保守的な翻訳）
# translate_config.jsonで "temperature": 0.1 に変更
python tools/translation/fix_chinese_errors.py --po-dir locales/ja/LC_MESSAGES --no-skip
```

### 問題: 処理が途中で止まった

```powershell
# 進捗は保存されているので、そのまま再実行すればOK
python tools/translation/fix_chinese_errors.py --po-dir locales/ja/LC_MESSAGES
```

## 💡 ベストプラクティス

### 1. 修正前にバックアップ

```powershell
# localesディレクトリをバックアップ
Copy-Item -Recurse locales locales_backup_$(Get-Date -Format 'yyyyMMdd_HHmmss')
```

### 2. 段階的な確認

```powershell
# 1. まずドライランで確認
python tools/translation/fix_chinese_errors.py --po-dir locales/ja/LC_MESSAGES --dry-run

# 2. 実際に修正
python tools/translation/fix_chinese_errors.py --po-dir locales/ja/LC_MESSAGES

# 3. 再検出で確認
python tools/analysis/detect_chinese_chars.py
```

### 3. ビルドで検証

```powershell
cd docs
make html

# 警告が増えていないか確認
```

### 4. Git差分で確認

```powershell
# 変更内容を確認
git diff locales/ja/LC_MESSAGES/apriltag/vision_portal/apriltag_camera_calibration/apriltag-camera-calibration.po

# 問題なければコミット
git add locales/
git commit -m "Fix Chinese characters in translations"
```

## 📊 修正統計の見方

スクリプト実行後に表示される統計：

```
修正完了
============================================================

総問題箇所: 100
✓ 修正成功: 95
✗ 修正失敗: 3
⊘ スキップ: 2

成功率: 95.0%
```

- **修正成功**: 正しく翻訳された箇所
- **修正失敗**: 翻訳に失敗（リトライ後も失敗）
- **スキップ**: 既に修正済みでスキップされた箇所

## 🎯 次のステップ

修正完了後：

1. **検証**: `detect_chinese_chars.py`で再検出
2. **ビルド**: `make html`でHTMLビルド
3. **目視確認**: 修正された箇所をいくつかサンプル確認
4. **コミット**: Gitでコミット＆プッシュ

## 📚 関連ドキュメント

- [AUTO_TRANSLATE.md](AUTO_TRANSLATE.md) - 初回翻訳ガイド
- [TRANSLATION_GUIDE.md](TRANSLATION_GUIDE.md) - 翻訳ガイドライン
- [LOCAL_LLM_SETUP.md](LOCAL_LLM_SETUP.md) - LLMセットアップ

## 🆘 サポート

問題が発生した場合：

1. `chinese_fix_progress.json`で進捗確認
2. `chinese_chars_report.md`で詳細確認
3. `--dry-run`で動作確認
4. モデルやtemperatureを変更して再試行

---

## 🚀 完全自動化（推奨）

```powershell
# 検出→修正→再検出を一括実行
python tools/analysis/detect_chinese_chars.py
if ($LASTEXITCODE -ne 0) {
    python tools/translation/fix_chinese_errors.py --po-dir locales/ja/LC_MESSAGES
    python tools/analysis/detect_chinese_chars.py
}
```

これで中国語混入問題は完全解決！ 🎉
