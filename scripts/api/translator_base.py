#!/usr/bin/env python3
"""
Abstract Translator Base Class

Defines the interface that all translator implementations must follow.
This allows for swappable backends (local LLM, OpenAI, Anthropic, etc.)
without changing the core translation pipeline.

All translator implementations inherit from Translator and implement:
- translate(text, context) → translated text
- estimate_tokens(text) → token count

Error Handling
---------------
TranslationError is raised on failures:
- Network errors
- Model errors
- Quality check failures
- Any recoverable/retryable error

This allows the caller to implement retry logic as needed.
"""

from abc import ABC, abstractmethod
from typing import Optional, Dict


class TranslationError(Exception):
    """
    Raised when translation fails.
    
    Provides context for retry logic and error handling.
    """
    
    def __init__(self, message: str, original_text: Optional[str] = None, 
                 retryable: bool = True):
        """
        Args:
            message: Error description
            original_text: The text that failed to translate
            retryable: Whether the operation should be retried
        """
        self.message = message
        self.original_text = original_text
        self.retryable = retryable
        super().__init__(message)


class Translator(ABC):
    """
    Abstract base class for translation backends.
    
    All translator implementations must:
    1. Inherit from Translator
    2. Implement translate() method
    3. Implement estimate_tokens() method
    4. Raise TranslationError on failures
    
    Example Implementation:
    
        class MyTranslator(Translator):
            def __init__(self, api_key: str):
                self.api_key = api_key
            
            def translate(self, text: str, context: str = "") -> str:
                try:
                    # Call external API
                    response = call_api(text, context)
                    return response.get_translation()
                except NetworkError as e:
                    raise TranslationError(
                        f"Network error: {e}",
                        original_text=text,
                        retryable=True
                    )
            
            def estimate_tokens(self, text: str) -> int:
                # Return estimated token count
                return len(text) // 4
    """
    
    @abstractmethod
    def translate(self, text: str, context: str = "") -> str:
        """
        Translate text to Japanese.
        
        The translator is responsible for:
        1. Handling protected placeholders (e.g., __RST_ROLE_0__)
           - Preserve them exactly as-is
           - Do NOT translate placeholder CONTENT
        2. Producing valid Japanese output
        3. Maintaining readability and accuracy
        
        Args:
            text: Text to translate (may contain RST placeholders)
            context: Context from previous chunks (for coherence)
        
        Returns:
            Translated Japanese text with placeholders preserved
        
        Raises:
            TranslationError: If translation fails
            
        Example:
            >>> translator = LocalLLMTranslator()
            >>> result = translator.translate(
            ...     "See __RST_ROLE_0__ for details",
            ...     context="This document explains..."
            ... )
            >>> result
            '__RST_ROLE_0__ の詳細を参照してください。'
        """
        pass
    
    @abstractmethod
    def estimate_tokens(self, text: str) -> int:
        """
        Estimate token count for text.
        
        Used for:
        1. Cost estimation (for paid APIs)
        2. Pre-flight checks (verify text will fit in context window)
        3. Planning and reporting
        
        Args:
            text: Text to estimate
        
        Returns:
            Estimated token count (backend-specific)
            
        Note:
            Different models have different tokenizers:
            - OpenAI: ~4 characters per token
            - Claude: ~3-4 characters per token
            - Ollama: varies by model
            
            Implement conservatively (round up) to avoid surprises.
        """
        pass
    
    def validate_output(self, original: str, translated: str) -> bool:
        """
        Validate translated output.
        
        Can be overridden by subclasses to add custom validation.
        Default implementation always returns True.
        
        Args:
            original: Original English text
            translated: Translated Japanese text
        
        Returns:
            True if valid, False otherwise
        """
        return True
    
    def get_config(self) -> Dict:
        """
        Get current configuration as a dictionary.
        
        Used for logging and debugging.
        
        Returns:
            Configuration dictionary (implementation-specific)
        """
        return {}
