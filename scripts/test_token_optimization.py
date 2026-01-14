#!/usr/bin/env python3
"""
トークン最適化の効果を検証するテストスクリプト

最適化前後のプロンプト長を比較し、トークン削減率を測定します。
"""

import sys
from pathlib import Path

# モジュールパスを追加
sys.path.insert(0, str(Path(__file__).parent))

from api.openai_translator import OpenAITranslator
from api.local_llm_translator import LocalLLMTranslator


def count_tokens_roughly(text: str) -> int:
    """トークン数の概算（英語: ~4文字/token, 日本語: ~2文字/token）"""
    # 英語部分
    english_chars = sum(1 for c in text if ord(c) < 128)
    # 日本語・その他
    other_chars = len(text) - english_chars
    
    return (english_chars // 4) + (other_chars // 2)


def test_openai_optimization():
    """OpenAI翻訳のトークン最適化をテスト"""
    print("="*60)
    print("OpenAI Translator - Token Optimization Test")
    print("="*60)
    
    # テスト用の用語集
    test_glossary = {
        "FTC": "FTC",
        "FIRST Tech Challenge": "FIRST Tech Challenge",
        "Android": "Android",
        "Control Hub": "Control Hub",
        "Driver Station": "Driver Station",
        "REV Robotics": "REV Robotics",
        "Configuration": "設定",
        "Telemetry": "テレメトリー",
    }
    
    # テストテキスト（用語集の一部のみ含む）
    test_text = """The FTC Control Hub is a powerful Android device.
It connects to the Driver Station via Wi-Fi.
See the documentation for more details."""
    
    test_context = "This section explains the basic setup process for FTC robotics competition teams using the Control Hub device."
    
    # 翻訳クラスを初期化（API keyなしでもプロンプト生成は可能）
    try:
        translator = OpenAITranslator(
            api_key="dummy",  # プロンプトテストなので実際には使わない
            model="gpt-4o-mini",
            glossary=test_glossary
        )
        
        # プロンプトを生成（最適化版）
        system_prompt = translator._build_system_prompt(test_text)
        user_prompt = translator._build_user_prompt(test_text, test_context)
        
        # トークン数を計測
        system_tokens = count_tokens_roughly(system_prompt)
        user_tokens = count_tokens_roughly(user_prompt)
        total_tokens = system_tokens + user_tokens
        
        print(f"\n✅ 最適化版プロンプト:")
        print(f"  System prompt: ~{system_tokens} tokens")
        print(f"  User prompt:   ~{user_tokens} tokens")
        print(f"  Total:         ~{total_tokens} tokens")
        
        print(f"\n📄 System Prompt:\n{system_prompt}")
        print(f"\n📄 User Prompt:\n{user_prompt[:200]}...")
        
        # 比較: 旧版の推定
        # 旧版では全用語集を送信
        old_glossary_text = "\n".join([f"- {en} → {ja}" for en, ja in test_glossary.items()])
        old_system_prompt = f"""You are a professional translator specializing in technical documentation translation from English to Japanese.

Requirements:
- Translate accurately while preserving technical terminology
- Use natural Japanese expression suitable for technical documentation
- Maintain formal tone (です/ます調)
- Do NOT translate proper nouns, product names, or technical terms that should remain in English
- Preserve formatting, spacing, and punctuation
- Output ONLY the Japanese translation, nothing else

Glossary (use these translations):
{old_glossary_text}
"""
        old_user_prompt = f"Context: {test_context}\n\nTranslate to Japanese:\n\n{test_text}"
        
        old_system_tokens = count_tokens_roughly(old_system_prompt)
        old_user_tokens = count_tokens_roughly(old_user_prompt)
        old_total_tokens = old_system_tokens + old_user_tokens
        
        print(f"\n\n⚠️  旧版プロンプト（推定）:")
        print(f"  System prompt: ~{old_system_tokens} tokens")
        print(f"  User prompt:   ~{old_user_tokens} tokens")
        print(f"  Total:         ~{old_total_tokens} tokens")
        
        # 削減率
        reduction = ((old_total_tokens - total_tokens) / old_total_tokens) * 100
        print(f"\n🎯 トークン削減率: {reduction:.1f}%")
        print(f"   ({old_total_tokens} → {total_tokens} tokens)")
        
    except Exception as e:
        print(f"Error: {e}")


def test_local_llm_optimization():
    """ローカルLLM翻訳のトークン最適化をテスト"""
    print("\n\n" + "="*60)
    print("Local LLM Translator - Token Optimization Test")
    print("="*60)
    
    # テスト用の用語集
    test_glossary = {
        "FTC": "FTC",
        "FIRST Tech Challenge": "FIRST Tech Challenge",
        "Android": "Android",
        "Control Hub": "Control Hub",
        "Driver Station": "Driver Station",
        "REV Robotics": "REV Robotics",
        "Configuration": "設定",
        "Telemetry": "テレメトリー",
    }
    
    # テストテキスト（プレースホルダーあり）
    test_text = """The __RST_ROLE_0__ provides access to the __RST_ROLE_1__ interface.
For more information, see __RST_REF_2__."""
    
    test_context = "This explains FTC Control Hub configuration."
    
    try:
        translator = LocalLLMTranslator(
            model="qwen2.5-coder:7b-instruct",
            glossary=test_glossary
        )
        
        # プロンプトを生成（最適化版）
        prompt = translator._create_prompt(test_text, test_context)
        
        # トークン数を計測
        prompt_tokens = count_tokens_roughly(prompt)
        
        print(f"\n✅ 最適化版プロンプト:")
        print(f"  Total: ~{prompt_tokens} tokens")
        
        print(f"\n📄 Prompt:\n{prompt}")
        
        # 比較: 旧版の推定（全用語集 + 詳細な説明）
        old_glossary_text = "\n".join([f"- {en} → {ja}" for en, ja in list(test_glossary.items())[:20]])
        old_prompt = f"""You are a technical translator specializing in reStructuredText (RST) documentation for FTC (FIRST Tech Challenge).

🚨 CRITICAL RULES:
1. Write ONLY in Japanese (Hiragana, Katakana, Kanji)
2. DO NOT write Chinese - Avoid: 为应该这处理方式设置获取发送接收检查验证
3. Preserve ALL placeholders exactly (e.g., __RST_ROLE_0__)
4. Use です・ます form (polite Japanese)
5. Keep important technical terms in English (see GLOSSARY)
6. Ensure proper spacing around placeholders

GLOSSARY (preserve in English):
{old_glossary_text}

PLACEHOLDERS (keep EXACTLY as-is, DO NOT translate):
__RST_ROLE_0__, __RST_ROLE_1__, __RST_REF_2__

These are RST markup protectors. Preserve them exactly.

CONTEXT: {test_context}

TEXT TO TRANSLATE:
{test_text}

TRANSLATE TO JAPANESE ONLY:"""
        
        old_prompt_tokens = count_tokens_roughly(old_prompt)
        
        print(f"\n\n⚠️  旧版プロンプト（推定）:")
        print(f"  Total: ~{old_prompt_tokens} tokens")
        
        # 削減率
        reduction = ((old_prompt_tokens - prompt_tokens) / old_prompt_tokens) * 100
        print(f"\n🎯 トークン削減率: {reduction:.1f}%")
        print(f"   ({old_prompt_tokens} → {prompt_tokens} tokens)")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    print("トークン最適化効果の検証\n")
    
    test_openai_optimization()
    test_local_llm_optimization()
    
    print("\n\n" + "="*60)
    print("✅ テスト完了")
    print("="*60)
    print("\n主な最適化ポイント:")
    print("  1. 用語集: テキストに含まれる項目のみ送信")
    print("  2. コンテキスト: 最初の80-100文字のみ")
    print("  3. プレースホルダー: 簡潔な注記のみ")
    print("  4. 説明文: 商用APIでは最小限に")
