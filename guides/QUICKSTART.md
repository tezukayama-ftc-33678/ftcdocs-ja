# ⚡ クイックスタート - 3分で始める

## 前提条件
- ✅ Windows 10/11
- ✅ NVIDIA GPU (VRAM 8GB以上)
- ✅ Python 3.8+

---

## 🚀 3ステップで完了

### ステップ1: Ollamaインストール（2分）

1. https://ollama.com/download/windows を開く
2. `OllamaSetup.exe`をダウンロード
3. インストーラーを実行
4. PowerShellで確認:
   ```powershell
   ollama --version
   ```

### ステップ2: 環境準備（1分）

PowerShellを開いて実行:

```powershell
# プロジェクトディレクトリに移動
cd h:\ftcdocs-ja

# LLMモデルをダウンロード（1-2分）
ollama pull qwen2.5:7b-instruct-q5_K_M

# Pythonパッケージをインストール
pip install ollama polib tqdm colorama

# 環境テスト
python test_translation_env.py
```

### ステップ3: 翻訳開始（1コマンド）

```powershell
# 自動翻訳開始
.\run_auto_translate.ps1
```

または:

```powershell
python batch_translate.py --po-dir locales/ja/LC_MESSAGES
```

---

## ✅ これだけ！

あとは**放置するだけ**で全POファイルの翻訳が完了します。

### ⏱️ 処理時間の目安
- 約20-40時間（モデルとPC性能による）
- 夜間実行推奨

### 📊 進捗確認
別のウィンドウで:
```powershell
Get-Content translation_progress.json | ConvertFrom-Json
```

### 🎉 完了後
1. `po_issues.json` で品質確認
2. `start docs\build\html-ja\index.html` でブラウザ確認
3. 問題なければコミット！

---

## 📚 詳細情報

より詳しい情報は以下を参照:

- **[COMPLETE_GUIDE.md](COMPLETE_GUIDE.md)** - 完全ガイド
- **[AUTO_TRANSLATE.md](AUTO_TRANSLATE.md)** - 詳細な実行手順
- **[LOCAL_LLM_SETUP.md](LOCAL_LLM_SETUP.md)** - 環境構築詳細

---

## 🆘 問題が起きたら

### エラーが出た場合
```powershell
# 環境テストを実行
python test_translation_env.py
```

### 途中で止まった場合
```powershell
# 再実行すれば続きから再開
python batch_translate.py --po-dir locales/ja/LC_MESSAGES
```

### 最初からやり直したい場合
```powershell
.\run_auto_translate.ps1 -ResetProgress
```

---

**🎊 以上！簡単でしょう？**

質問があれば [COMPLETE_GUIDE.md](COMPLETE_GUIDE.md) を確認してください。
