#!/usr/bin/env python3
"""
Token Estimatorのユニットテスト

トークン数推定、コスト計算が正しく動作することを検証する。
"""

import unittest
import sys
from pathlib import Path

# scriptsディレクトリをパスに追加
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.token_estimator import TokenEstimator


class TestTokenEstimator(unittest.TestCase):
    """TokenEstimatorクラスのテスト"""
    
    def setUp(self):
        """各テスト前の初期化"""
        self.estimator = TokenEstimator()
    
    def test_english_text_estimation(self):
        """英語テキストのトークン数推定"""
        text = "This is a test sentence."
        tokens = self.estimator.estimate_tokens(text)
        
        # 英語は単語数とほぼ同じか少し多い
        self.assertGreater(tokens, 0)
        self.assertLess(tokens, 20)  # 単語数より多少多い程度
    
    def test_japanese_text_estimation(self):
        """日本語テキストのトークン数推定"""
        text = "これは日本語のテストです。"
        tokens = self.estimator.estimate_tokens(text)
        
        # 日本語は文字数に近い
        self.assertGreater(tokens, 0)
        self.assertLess(tokens, len(text) * 2)  # 文字数の2倍以内
    
    def test_mixed_language_estimation(self):
        """混在言語のトークン数推定"""
        text = "これはtest文です。This is a test."
        tokens = self.estimator.estimate_tokens(text)
        
        self.assertGreater(tokens, 0)
    
    def test_empty_text(self):
        """空文字列のトークン数推定"""
        text = ""
        tokens = self.estimator.estimate_tokens(text)
        
        self.assertEqual(tokens, 0)
    
    def test_special_characters(self):
        """特殊文字のトークン数推定"""
        text = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
        tokens = self.estimator.estimate_tokens(text)
        
        # 特殊文字もトークンとしてカウントされる
        self.assertGreater(tokens, 0)
    
    def test_code_snippet(self):
        """コードスニペットのトークン数推定"""
        text = "def hello():\n    print('Hello, World!')"
        tokens = self.estimator.estimate_tokens(text)
        
        self.assertGreater(tokens, 0)
    
    def test_model_specific_estimation(self):
        """モデル固有のトークン数推定"""
        text = "This is a test."
        
        # GPT
        gpt_tokens = self.estimator.estimate_tokens(text, model_family='gpt')
        self.assertGreater(gpt_tokens, 0)
        
        # Claude
        claude_tokens = self.estimator.estimate_tokens(text, model_family='claude')
        self.assertGreater(claude_tokens, 0)
        
        # Ollama
        ollama_tokens = self.estimator.estimate_tokens(text, model_family='ollama')
        self.assertGreater(ollama_tokens, 0)
    
    def test_cost_estimation(self):
        """コスト推定"""
        text = "This is a test sentence for cost estimation."
        
        # GPT-4のコスト推定
        cost = self.estimator.estimate_cost(
            text,
            model='gpt-4',
            input_price_per_1k=0.03,
            output_price_per_1k=0.06
        )
        
        self.assertGreater(cost, 0)
        self.assertIsInstance(cost, float)
    
    def test_batch_cost_estimation(self):
        """バッチコスト推定"""
        texts = [
            "First sentence.",
            "Second sentence.",
            "Third sentence."
        ]
        
        total_cost = self.estimator.estimate_batch_cost(
            texts,
            model='gpt-4',
            input_price_per_1k=0.03,
            output_price_per_1k=0.06,
            translation_multiplier=1.5
        )
        
        self.assertGreater(total_cost, 0)
        self.assertIsInstance(total_cost, float)
    
    def test_very_long_text(self):
        """非常に長いテキストのトークン数推定"""
        long_text = "This is a test. " * 1000
        tokens = self.estimator.estimate_tokens(long_text)
        
        # 長いテキストでも正しく推定される
        self.assertGreater(tokens, 1000)
    
    def test_unicode_characters(self):
        """Unicode文字のトークン数推定"""
        text = "🚀 ロケット 🎉 パーティー"
        tokens = self.estimator.estimate_tokens(text)
        
        # 絵文字も含めてトークン数が推定される
        self.assertGreater(tokens, 0)


class TestTokenEstimatorComparison(unittest.TestCase):
    """TokenEstimatorの比較テスト"""
    
    def setUp(self):
        """各テスト前の初期化"""
        self.estimator = TokenEstimator()
    
    def test_model_family_comparison(self):
        """異なるモデルファミリーのトークン数比較"""
        text = "This is a test sentence."
        
        gpt_tokens = self.estimator.estimate_tokens(text, model_family='gpt')
        claude_tokens = self.estimator.estimate_tokens(text, model_family='claude')
        ollama_tokens = self.estimator.estimate_tokens(text, model_family='ollama')
        
        # すべてのモデルで正の値
        self.assertGreater(gpt_tokens, 0)
        self.assertGreater(claude_tokens, 0)
        self.assertGreater(ollama_tokens, 0)
    
    def test_translation_multiplier(self):
        """翻訳倍率の効果"""
        text = "Short text."
        
        # 倍率1.0（入力のみ）
        cost_1x = self.estimator.estimate_cost(
            text,
            model='gpt-4',
            input_price_per_1k=0.03,
            output_price_per_1k=0.06,
            translation_multiplier=1.0
        )
        
        # 倍率2.0（出力も同じ長さ）
        cost_2x = self.estimator.estimate_cost(
            text,
            model='gpt-4',
            input_price_per_1k=0.03,
            output_price_per_1k=0.06,
            translation_multiplier=2.0
        )
        
        # 倍率が大きいほどコストが高い
        self.assertGreater(cost_2x, cost_1x)


if __name__ == '__main__':
    unittest.main()
