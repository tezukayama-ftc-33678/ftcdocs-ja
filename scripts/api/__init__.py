"""
Translation API Module

Provides translation implementations for multiple backends:
- Local LLM (Ollama)
- OpenAI (GPT-3.5, GPT-4)
- Anthropic (Claude 2, Claude 3)

All translators implement the unified Translator interface for seamless backend switching.

Architecture:
- translator_base.py: Abstract base class and error types
- local_llm_translator.py: Ollama/local LLM implementation
- openai_translator.py: OpenAI ChatGPT implementation
- anthropic_translator.py: Anthropic Claude implementation
- translator_registry.py: Backend management and selection system

Usage:
    from api import create_translator, TranslatorRegistry
    
    # Create from config
    translator = create_translator(config_path="config.json")
    
    # Or specify backend directly
    translator = create_translator("openai", model="gpt-4")
    
    # Use translator
    result = translator.translate("Hello, world!")
"""

from .translator_base import Translator, TranslationError
from .local_llm_translator import LocalLLMTranslator
from .translator_registry import TranslatorRegistry, create_translator

# Optional API backends (imported conditionally)
__all_exports__ = []

try:
    from .openai_translator import OpenAITranslator
    __all_exports__.append("OpenAITranslator")
except ImportError:
    pass

try:
    from .anthropic_translator import AnthropicTranslator
    __all_exports__.append("AnthropicTranslator")
except ImportError:
    pass

__all__ = [
    # Base
    "Translator",
    "TranslationError",
    
    # Implementations
    "LocalLLMTranslator",
    
    # Registry
    "TranslatorRegistry",
    "create_translator",
] + __all_exports__
