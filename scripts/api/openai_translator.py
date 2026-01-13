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
    - GPT-3.5-turbo (fast, cost-effective)
    - GPT-4 (high quality, more expensive)
    - GPT-4-turbo (balance of speed and quality)
    
    Features:
    - Automatic retry with exponential backoff
    - Rate limiting support
    - Token usage tracking
    - Cost estimation
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "gpt-3.5-turbo",
        temperature: float = 0.3,
        max_retries: int = 3,
        timeout: int = 30,
        glossary: Optional[Dict[str, str]] = None
    ):
        """
        Initialize OpenAI translator.
        
        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            model: Model name (gpt-3.5-turbo, gpt-4, gpt-4-turbo)
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
                "OpenAI API key required. Set OPENAI_API_KEY environment variable "
                "or pass api_key parameter"
            )
        
        # Configure OpenAI client
        openai.api_key = self.api_key
        
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
        
        # Build prompt
        system_prompt = self._build_system_prompt()
        user_prompt = self._build_user_prompt(text, context)
        
        # Attempt translation with retries
        last_error = None
        for attempt in range(1, self.max_retries + 1):
            try:
                response = openai.ChatCompletion.create(
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
                
            except openai.error.RateLimitError as e:
                last_error = e
                wait_time = 2 ** attempt  # Exponential backoff
                print(f"Rate limit hit. Waiting {wait_time}s before retry {attempt}/{self.max_retries}")
                time.sleep(wait_time)
                
            except openai.error.APIError as e:
                last_error = e
                print(f"API error: {e}. Retry {attempt}/{self.max_retries}")
                time.sleep(1)
                
            except openai.error.Timeout as e:
                last_error = e
                print(f"Request timeout. Retry {attempt}/{self.max_retries}")
                time.sleep(2)
                
            except Exception as e:
                raise TranslationError(f"OpenAI translation failed: {e}")
        
        # All retries failed
        raise TranslationError(
            f"OpenAI translation failed after {self.max_retries} attempts: {last_error}"
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
            "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},  # per 1K tokens
            "gpt-4": {"input": 0.03, "output": 0.06},
            "gpt-4-turbo": {"input": 0.01, "output": 0.03},
        }
        
        prices = pricing.get(self.model, pricing["gpt-3.5-turbo"])
        
        input_cost = (self.prompt_tokens / 1000) * prices["input"]
        output_cost = (self.completion_tokens / 1000) * prices["output"]
        total_cost = input_cost + output_cost
        
        return {
            "total_tokens": self.total_tokens,
            "prompt_tokens": self.prompt_tokens,
            "completion_tokens": self.completion_tokens,
            "estimated_cost_usd": round(total_cost, 4)
        }
    
    def reset_stats(self) -> None:
        """Reset usage statistics."""
        self.total_tokens = 0
        self.prompt_tokens = 0
        self.completion_tokens = 0
