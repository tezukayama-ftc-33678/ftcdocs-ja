#!/usr/bin/env python3
"""
Anthropic Translator Module

Provides translation using Anthropic's Claude API (Claude 2, Claude 3, etc.).
Supports the same interface as other translators for seamless backend switching.
"""

import os
import time
from typing import Dict, List, Optional

try:
    import anthropic
except ImportError:
    anthropic = None

from .translator_base import Translator, TranslationError


class AnthropicTranslator(Translator):
    """
    Anthropic Claude translator implementation.
    
    Supports:
    - Claude 2 (100K context)
    - Claude 3 Opus (high quality)
    - Claude 3 Sonnet (balanced)
    - Claude 3 Haiku (fast)
    
    Features:
    - Automatic retry with exponential backoff
    - Large context window support
    - Token usage tracking
    - Cost estimation
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-3-sonnet-20240229",
        temperature: float = 0.3,
        max_tokens: int = 4096,
        max_retries: int = 3,
        timeout: int = 60,
        glossary: Optional[Dict[str, str]] = None
    ):
        """
        Initialize Anthropic translator.
        
        Args:
            api_key: Anthropic API key (defaults to ANTHROPIC_API_KEY env var)
            model: Model name (claude-2, claude-3-opus, claude-3-sonnet, claude-3-haiku)
            temperature: Creativity (0.0-1.0, lower = more consistent)
            max_tokens: Maximum output tokens
            max_retries: Maximum retry attempts on failure
            timeout: Request timeout in seconds
            glossary: Optional translation glossary
        
        Raises:
            ImportError: If anthropic package not installed
            ValueError: If API key not provided
        """
        super().__init__()
        
        if anthropic is None:
            raise ImportError(
                "anthropic package not found. Install with: pip install anthropic"
            )
        
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError(
                "Anthropic API key required. Set ANTHROPIC_API_KEY environment variable "
                "or pass api_key parameter"
            )
        
        # Configure Anthropic client
        self.client = anthropic.Anthropic(api_key=self.api_key)
        
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.max_retries = max_retries
        self.timeout = timeout
        self.glossary = glossary or {}
        
        # Usage tracking
        self.total_tokens = 0
        self.input_tokens = 0
        self.output_tokens = 0
    
    def translate(
        self,
        text: str,
        context: Optional[str] = None,
        max_length: Optional[int] = None
    ) -> str:
        """
        Translate English text to Japanese using Claude API.
        
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
        
        # Build prompt
        system_prompt = self._build_system_prompt()
        user_prompt = self._build_user_prompt(text, context)
        
        # Attempt translation with retries
        last_error = None
        for attempt in range(1, self.max_retries + 1):
            try:
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=self.max_tokens,
                    temperature=self.temperature,
                    system=system_prompt,
                    messages=[
                        {"role": "user", "content": user_prompt}
                    ]
                )
                
                # Extract translation
                translation = response.content[0].text.strip()
                
                # Track usage
                if hasattr(response, 'usage'):
                    self.input_tokens += response.usage.input_tokens
                    self.output_tokens += response.usage.output_tokens
                    self.total_tokens += (response.usage.input_tokens + response.usage.output_tokens)
                
                return translation
                
            except anthropic.RateLimitError as e:
                last_error = e
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Rate limit hit. Waiting {wait_time}s before retry {attempt}/{self.max_retries}")
                time.sleep(wait_time)
                
            except anthropic.APIError as e:
                last_error = e
                print(f"API error: {e}. Retry {attempt}/{self.max_retries}")
                time.sleep(1)
                
            except Exception as e:
                raise TranslationError(f"Claude translation failed: {e}")
        
        # All retries failed
        raise TranslationError(
            f"Claude translation failed after {self.max_retries} attempts: {last_error}"
        )
    
    def _build_system_prompt(self) -> str:
        """Build system prompt for translation."""
        prompt = """You are a professional translator specializing in technical documentation translation from English to Japanese.

Requirements:
- Translate accurately while preserving technical terminology
- Use natural Japanese expression suitable for technical documentation
- Maintain formal tone (です/ます調)
- Do NOT translate proper nouns, product names, or technical terms that should remain in English
- Preserve formatting, spacing, and punctuation
- Output ONLY the Japanese translation, nothing else"""
        
        if self.glossary:
            prompt += "\n\nGlossary (use these translations):\n"
            for en, ja in self.glossary.items():
                prompt += f"- {en} → {ja}\n"
        
        return prompt
    
    def _build_user_prompt(self, text: str, context: Optional[str] = None) -> str:
        """Build user prompt with text and optional context."""
        prompt = f"Translate to Japanese:\n\n{text}"
        
        if context:
            prompt = f"Context: {context}\n\n{prompt}"
        
        return prompt
    
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
        pricing = {
            "claude-2": {"input": 0.008, "output": 0.024},  # per 1K tokens
            "claude-3-opus": {"input": 0.015, "output": 0.075},
            "claude-3-sonnet": {"input": 0.003, "output": 0.015},
            "claude-3-haiku": {"input": 0.00025, "output": 0.00125},
        }
        
        # Find matching pricing
        prices = None
        for model_key, model_prices in pricing.items():
            if model_key in self.model:
                prices = model_prices
                break
        
        if not prices:
            prices = pricing["claude-3-sonnet"]  # Default
        
        input_cost = (self.input_tokens / 1000) * prices["input"]
        output_cost = (self.output_tokens / 1000) * prices["output"]
        total_cost = input_cost + output_cost
        
        return {
            "total_tokens": self.total_tokens,
            "input_tokens": self.input_tokens,
            "output_tokens": self.output_tokens,
            "estimated_cost_usd": round(total_cost, 4)
        }
    
    def reset_stats(self) -> None:
        """Reset usage statistics."""
        self.total_tokens = 0
        self.input_tokens = 0
        self.output_tokens = 0
