#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
翻訳システムのテストスクリプト
環境が正しくセットアップされているか確認
"""

import sys
import os

def test_imports():
    """必要なパッケージのインポートテスト"""
    print("📦 パッケージインポートテスト...")
    
    try:
        import ollama
        print("  ✓ ollama")
    except ImportError:
        print("  ✗ ollama が見つかりません")
        print("    pip install ollama")
        return False
    
    try:
        import polib
        print("  ✓ polib")
    except ImportError:
        print("  ✗ polib が見つかりません")
        print("    pip install polib")
        return False
    
    try:
        from tqdm import tqdm
        print("  ✓ tqdm")
    except ImportError:
        print("  ✗ tqdm が見つかりません")
        print("    pip install tqdm")
        return False
    
    try:
        from colorama import init, Fore, Style
        print("  ✓ colorama")
    except ImportError:
        print("  ✗ colorama が見つかりません")
        print("    pip install colorama")
        return False
    
    return True


def test_ollama_connection():
    """Ollama接続テスト"""
    print("\n🔌 Ollama接続テスト...")
    
    try:
        import ollama
        models = ollama.list()
        print(f"  ✓ Ollama接続成功")
        print(f"  利用可能なモデル: {len(models.get('models', []))} 個")
        
        for model in models.get('models', []):
            name = model.get('name', 'unknown')
            print(f"    - {name}")
        
        return True
    except Exception as e:
        print(f"  ✗ Ollama接続エラー: {e}")
        print("    Ollamaサービスが起動しているか確認してください")
        return False


def test_translation():
    """簡単な翻訳テスト"""
    print("\n🌐 翻訳テスト...")
    
    try:
        import ollama
        import json
        
        # 設定読み込み
        if os.path.exists("translate_config.json"):
            with open("translate_config.json", 'r', encoding='utf-8') as f:
                config = json.load(f)
            model = config.get("model", "qwen2.5:7b-instruct-q5_K_M")
        else:
            model = "qwen2.5:7b-instruct-q5_K_M"
        
        print(f"  使用モデル: {model}")
        print(f"  テスト文: 'Hello, World!'")
        
        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'user',
                    'content': 'Translate to Japanese: "Hello, World!"'
                }
            ],
            options={'temperature': 0.3}
        )
        
        result = response['message']['content'].strip()
        print(f"  翻訳結果: {result}")
        
        if "こんにちは" in result or "世界" in result:
            print("  ✓ 翻訳テスト成功")
            return True
        else:
            print("  ⚠ 翻訳結果が予期しない形式です")
            return False
            
    except Exception as e:
        print(f"  ✗ 翻訳テストエラー: {e}")
        return False


def test_po_files():
    """POファイル存在確認"""
    print("\n📄 POファイル確認...")
    
    po_dir = "locales/ja/LC_MESSAGES"
    
    if not os.path.exists(po_dir):
        print(f"  ✗ POディレクトリが見つかりません: {po_dir}")
        return False
    
    from pathlib import Path
    po_files = list(Path(po_dir).rglob("*.po"))
    
    print(f"  ✓ POファイル検出: {len(po_files)} 個")
    
    if len(po_files) > 0:
        print(f"  サンプル:")
        for po_file in list(po_files)[:5]:
            print(f"    - {po_file.relative_to(po_dir)}")
        if len(po_files) > 5:
            print(f"    ... 他 {len(po_files) - 5} 個")
        return True
    else:
        print("  ⚠ POファイルが見つかりません")
        return False


def test_scripts():
    """スクリプト存在確認"""
    print("\n📜 スクリプト確認...")
    
    # Get the script directory (tools/translation/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    required_scripts = [
        ("translate_po.py", os.path.join(script_dir, "translate_po.py")),
        ("batch_translate.py", os.path.join(script_dir, "batch_translate.py")),
        ("translate_config.json", "translate_config.json")  # In project root
    ]
    
    all_exist = True
    for name, path in required_scripts:
        if os.path.exists(path):
            print(f"  ✓ {name}")
        else:
            print(f"  ✗ {name} が見つかりません")
            all_exist = False
    
    return all_exist


def main():
    """テスト実行"""
    print("=" * 60)
    print("  翻訳システム環境テスト")
    print("=" * 60)
    
    results = []
    
    # 各テスト実行
    results.append(("パッケージ", test_imports()))
    results.append(("Ollama接続", test_ollama_connection()))
    results.append(("翻訳機能", test_translation()))
    results.append(("POファイル", test_po_files()))
    results.append(("スクリプト", test_scripts()))
    
    # 結果サマリー
    print("\n" + "=" * 60)
    print("  テスト結果サマリー")
    print("=" * 60)
    
    all_passed = True
    for name, passed in results:
        status = "✓ 成功" if passed else "✗ 失敗"
        print(f"  {name:20s} {status}")
        if not passed:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("\n🎉 全てのテストに合格しました！")
        print("\n次のコマンドで翻訳を開始できます:")
        print("  python tools/translation/batch_translate.py --po-dir locales/ja/LC_MESSAGES")
        print("または:")
        print("  .\\run_auto_translate.ps1")
        return 0
    else:
        print("\n⚠ いくつかのテストが失敗しました。")
        print("上記のエラーメッセージを確認して修正してください。")
        return 1


if __name__ == "__main__":
    sys.exit(main())
