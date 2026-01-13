#!/usr/bin/env python3
"""
翻訳バックエンド選択ツール

利用可能な翻訳バックエンドを表示し、設定ファイルの作成を支援する。
"""

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from api.translator_registry import TranslatorRegistry


def main():
    """メイン関数"""
    print("\n翻訳バックエンド管理ツール")
    print("=" * 70)
    
    # 利用可能なバックエンドを表示
    TranslatorRegistry.print_available_backends()
    
    # 設定ファイルサンプルを表示
    print("\n\n設定ファイルサンプル (data/translate_config.json):")
    print("=" * 70)
    
    sample_config = {
        "backend": "ollama",
        "ollama": {
            "model": "gemma2:27b-instruct-q4_K_M",
            "api_url": "http://localhost:11434",
            "temperature": 0.3,
            "max_retries": 3
        },
        "openai": {
            "api_key": "sk-YOUR_API_KEY_HERE",
            "model": "gpt-4",
            "temperature": 0.3,
            "max_retries": 3
        },
        "anthropic": {
            "api_key": "sk-ant-YOUR_API_KEY_HERE",
            "model": "claude-3-sonnet-20240229",
            "temperature": 0.3,
            "max_tokens": 4096,
            "max_retries": 3
        },
        "glossary": {
            "FIRST Tech Challenge": "FIRST Tech Challenge",
            "robot": "ロボット",
            "servo": "サーボ",
            "motor": "モーター"
        }
    }
    
    print(json.dumps(sample_config, indent=2, ensure_ascii=False))
    
    print("\n\n使用方法:")
    print("=" * 70)
    print("1. 上記の設定を data/translate_config.json にコピー")
    print("2. 使用したいバックエンドの api_key を設定 (OpenAI/Anthropicの場合)")
    print("3. backend フィールドで使用するバックエンドを選択")
    print("4. 翻訳スクリプトを実行:")
    print("   python translate_po_smart.py <po_file>")
    print("\n注: Ollamaを使用する場合はAPIキー不要 (ローカル実行)")
    print("=" * 70)


if __name__ == '__main__':
    main()
