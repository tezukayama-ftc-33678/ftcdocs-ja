#!/usr/bin/env python3
"""
簡体字中国語検出機能のテスト
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from translate_po_smart import SimplifiedChineseDetector

# テストケース
test_cases = [
    # (テキスト, 期待される結果, 説明)
    ("これは日本語です。", False, "日本語のみ（簡体字なし）"),
    ("This is English.", False, "英語のみ"),
    ("中国語です。", False, "中国語だが簡体字特定文字なし"),
    
    # 簡体字特定文字を含むテキスト（Qwen2.5-Coderが出力しやすい）
    ("为了让大家了解情况。", True, "簡体字特定文字あり（为了）"),
    ("这是中国人写的。", True, "簡体字特定文字あり（这）"),
    ("应该按照规定处理。", True, "簡体字特定文字あり（应该、按照、处理）"),
    
    # 日本語と簡体字の混在
    ("これは日本語です。但是应该注意这一点。", True, "日本語と簡体字の混在（簡体字あり）"),
    ("これは日本語です。中国についても記述します。", False, "日本語と簡体字なし（検出なし）"),
    
    # エッジケース
    ("", False, "空文字列"),
    ("123456789", False, "数字のみ"),
    ("ABCDEFGH", False, "英字のみ"),
]

def main():
    detector = SimplifiedChineseDetector()
    
    print("=" * 70)
    print("簡体字中国語検出テスト")
    print("=" * 70)
    print()
    
    passed = 0
    failed = 0
    
    for text, expected, description in test_cases:
        result = detector.has_simplified_chinese(text)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        
        if result == expected:
            passed += 1
        else:
            failed += 1
        
        print(f"{status} | {description}")
        print(f"  テキスト: {text}")
        print(f"  期待値: {expected}, 実際: {result}")
        print()
    
    # 結果サマリー
    print("=" * 70)
    print(f"テスト結果: {passed} 合格、{failed} 失敗")
    print("=" * 70)
    
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
