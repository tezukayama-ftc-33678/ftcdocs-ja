#!/usr/bin/env python3
"""
OpenAI Translator Module

Provides translation using OpenAI's ChatGPT API (GPT-3.5, GPT-4, etc.).
Supports the same interface as LocalLLMTranslator for seamless backend switching.
"""

import os
import time
from typing import Dict, List, Optional

try:
    import openai
except ImportError:
    openai = None

from .translator_base import Translator, TranslationError


class OpenAITranslator(Translator):
    """
    OpenAI ChatGPT translator implementation.
    
    Supports:
        - GPT-4o-mini (recommended: fast and cheap)
        - GPT-4.1-mini (recommended: balanced performance)
        - GPT-5-mini (high quality, higher cost)
        - Legacy models: GPT-4, GPT-4-turbo
    Features:
    - Automatic retry with exponential backoff
    - Rate limiting support
    - Token usage tracking
    - Cost estimation
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gpt-4o-mini",
        temperature: float = 0.1,
        max_retries: int = 3,
        timeout: int = 30,
        glossary: Optional[Dict[str, str]] = None
    ):
        """
        Initialize OpenAI translator.
        
        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            model: Model name (gpt-4o-mini, gpt-4.1-mini, gpt-5-mini, etc.)
            temperature: Creativity (0.0-1.0, lower = more consistent)
            max_retries: Maximum retry attempts on failure
            timeout: Request timeout in seconds
            glossary: Optional translation glossary
        
        Raises:
            ImportError: If openai package not installed
            ValueError: If API key not provided
        """
        super().__init__()
        
        if openai is None:
            raise ImportError(
                "openai package not found. Install with: pip install openai"
            )
        
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError(
                "OpenAI API key required. Set OPENAI_API_KEY environment variable or .env file"
            )
        
        # Configure OpenAI client (v1.0+ uses client instance)
        self.client = openai.OpenAI(api_key=self.api_key)
        
        self.model = model
        self.temperature = temperature
        self.max_retries = max_retries
        self.timeout = timeout
        self.glossary = glossary or {}
        
        # Usage tracking
        self.total_tokens = 0
        self.prompt_tokens = 0
        self.completion_tokens = 0
    
    def translate(
        self,
        text: str,
        context: Optional[str] = None,
        max_length: Optional[int] = None
    ) -> str:
        """
        Translate English text to Japanese using OpenAI API.
        
        Args:
            text: English text to translate
            context: Optional context for better translation
            max_length: Maximum output length (not strictly enforced)
        
        Returns:
            Japanese translation
        
        Raises:
            TranslationError: If translation fails after retries
        """
        if not text or not text.strip():
            return ""
        
        # Build prompt (text passed to optimize glossary)
        system_prompt = self._build_system_prompt(text)
        user_prompt = self._build_user_prompt(text, context)
        
        # Attempt translation with retries
        last_error = None
        for attempt in range(1, self.max_retries + 1):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=self.temperature,
                    timeout=self.timeout
                )
                
                # Extract translation
                translation = response.choices[0].message.content.strip()
                
                # Track usage
                if hasattr(response, 'usage'):
                    self.prompt_tokens += response.usage.prompt_tokens
                    self.completion_tokens += response.usage.completion_tokens
                    self.total_tokens += response.usage.total_tokens
                
                return translation
                
            except openai.RateLimitError as e:
                last_error = e
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Rate limit hit. Waiting {wait_time}s before retry {attempt}/{self.max_retries}")
                time.sleep(wait_time)
                
            except openai.APIError as e:
                last_error = e
                print(f"API error: {e}. Retry {attempt}/{self.max_retries}")
                time.sleep(1)
                
            except openai.APITimeoutError as e:
                last_error = e
                print(f"Request timeout. Retry {attempt}/{self.max_retries}")
                time.sleep(2)
                
            except Exception as e:
                raise TranslationError(f"OpenAI translation failed: {e}")
        
        # All retries failed
        raise TranslationError(
            f"OpenAI translation failed after {self.max_retries} attempts: {last_error}"
        )
    
    def _build_system_prompt(self, text: str = "") -> str:
        """Build system prompt for translation (optimized for token efficiency)."""
        # OpenAIは高性能なので簡潔なプロンプトで十分
        prompt = """Technical translator: English → Japanese (です/ます). Preserve formatting and placeholders."""
        
        # 用語集: テキストに含まれる項目のみ追加（トークン節約）
        if self.glossary and text:
            relevant_terms = {en: ja for en, ja in self.glossary.items() if en.lower() in text.lower()}
            if relevant_terms:
                prompt += "\nTerms: " + ", ".join(f"{en}→{ja}" for en, ja in list(relevant_terms.items())[:10])
        
        return prompt
    
    def _build_user_prompt(self, text: str, context: Optional[str] = None) -> str:
        """Build user prompt with text and optional context."""
        # コンテキストは最小限に（最初の80文字のみ）
        if context and len(context) > 80:
            context = context[:80] + "..."
        
        if context:
            return f"Context: {context}\n\n{text}"
        return text
    
    def translate_batch(
        self,
        texts: List[str],
        context: Optional[str] = None
    ) -> List[str]:
        """
        Translate multiple texts.
        
        Args:
            texts: List of English texts
            context: Optional context for all translations
        
        Returns:
            List of Japanese translations (same order)
        """
        translations = []
        for text in texts:
            try:
                translation = self.translate(text, context=context)
                translations.append(translation)
            except TranslationError as e:
                print(f"Warning: Translation failed for text: {text[:50]}... Error: {e}")
                translations.append("")  # Empty on failure
        
        return translations
    
    def get_stats(self) -> Dict[str, int]:
        """
        Get usage statistics.
        
        Returns:
            Dict with token counts and estimated cost
        """
        # Pricing (as of 2024, subject to change)
        # Daily limit: 2.5M tokens across all mini models
        pricing = {
            "gpt-4o-mini": {"input": 0.00015, "output": 0.0006},  # per 1K tokens
            "gpt-4.1-mini": {"input": 0.00075, "output": 0.003},  # per 1K tokens
            "gpt-5-mini": {"input": 0.001, "output": 0.004},      # per 1K tokens
            "gpt-4o": {"input": 0.005, "output": 0.015},          # per 1K tokens
            "gpt-4": {"input": 0.03, "output": 0.06},             # per 1K tokens
        }
        
        prices = pricing.get(self.model, pricing["gpt-4o-mini"])
        
        input_cost = (self.prompt_tokens / 1000) * prices["input"]
        output_cost = (self.completion_tokens / 1000) * prices["output"]
        total_cost = input_cost + output_cost
        
        return {
            "total_tokens": self.total_tokens,
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "estimated_cost_usd": round(total_cost, 6),
            "daily_limit_tokens": 2500000
        }
    
    def reset_stats(self) -> None:
        """Reset usage statistics."""
        self.total_tokens = 0
        self.prompt_tokens = 0
        self.completion_tokens = 0
    
    def estimate_tokens(self, text: str) -> int:
        """
        Estimate token count for OpenAI models.
        
        OpenAI's tokenizers use roughly 4 characters per token.
        Conservative estimate (round up) to avoid context overflow.
        
        Args:
            text: Text to estimate
        
        Returns:
            Estimated token count
        """
        if not text:
            return 0
        
        # OpenAI tokenizer: approximately 4 characters per token
        # Conservative estimate: divide by 3 to be safe
        estimated_tokens = len(text) // 3 + 1
        
        return estimated_tokens
