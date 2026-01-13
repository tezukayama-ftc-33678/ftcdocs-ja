#!/usr/bin/env python3
"""
Translator Registry Module

Manages multiple translation backends and provides unified interface for backend selection.
Supports: OpenAI, Anthropic, Local LLM (Ollama), and future backends.
"""

import json
from pathlib import Path
from typing import Dict, Type, Optional, List

from .translator_base import Translator, TranslationError
from .local_llm_translator import LocalLLMTranslator


# Optional imports (fail gracefully if packages not installed)
try:
    from .openai_translator import OpenAITranslator
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

try:
    from .anthropic_translator import AnthropicTranslator
    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False


class TranslatorRegistry:
    """
    Central registry for all translation backends.
    
    Features:
    - Automatic backend discovery
    - Configuration-based selection
    - Fallback mechanism
    - Unified interface across all backends
    
    Usage:
        # Create translator from config
        translator = TranslatorRegistry.create_from_config("config.json")
        
        # Or create directly
        translator = TranslatorRegistry.create("openai", model="gpt-4")
        
        # Use like any translator
        result = translator.translate("Hello, world!")
    """
    
    # Available backends
    _backends: Dict[str, Type[Translator]] = {
        "ollama": LocalLLMTranslator,
        "local": LocalLLMTranslator,  # Alias
    }
    
    # Conditionally register API backends
    if HAS_OPENAI:
        _backends["openai"] = OpenAITranslator
        _backends["gpt"] = OpenAITranslator  # Alias
    
    if HAS_ANTHROPIC:
        _backends["anthropic"] = AnthropicTranslator
        _backends["claude"] = AnthropicTranslator  # Alias
    
    @classmethod
    def list_backends(cls) -> List[str]:
        """
        List all available backend names.
        
        Returns:
            List of backend identifiers
        """
        return list(cls._backends.keys())
    
    @classmethod
    def is_available(cls, backend: str) -> bool:
        """
        Check if a backend is available.
        
        Args:
            backend: Backend name (openai, anthropic, ollama, etc.)
        
        Returns:
            True if backend is available
        """
        return backend.lower() in cls._backends
    
    @classmethod
    def create(
        cls,
        backend: str,
        **kwargs
    ) -> Translator:
        """
        Create a translator instance.
        
        Args:
            backend: Backend name (openai, anthropic, ollama)
            **kwargs: Backend-specific configuration
        
        Returns:
            Configured translator instance
        
        Raises:
            ValueError: If backend not available
            
        Example:
            # OpenAI
            translator = TranslatorRegistry.create(
                "openai",
                api_key="sk-...",
                model="gpt-4"
            )
            
            # Anthropic
            translator = TranslatorRegistry.create(
                "anthropic",
                api_key="sk-ant-...",
                model="claude-3-sonnet-20240229"
            )
            
            # Local LLM
            translator = TranslatorRegistry.create(
                "ollama",
                model="llama2-ja:13b",
                api_url="http://localhost:11434"
            )
        """
        backend_key = backend.lower()
        
        if backend_key not in cls._backends:
            available = ", ".join(cls.list_backends())
            raise ValueError(
                f"Backend '{backend}' not available. Available: {available}"
            )
        
        backend_class = cls._backends[backend_key]
        
        try:
            return backend_class(**kwargs)
        except Exception as e:
            raise TranslationError(f"Failed to create {backend} translator: {e}")
    
    @classmethod
    def create_from_config(
        cls,
        config_path: str,
        backend_override: Optional[str] = None
    ) -> Translator:
        """
        Create translator from configuration file.
        
        Args:
            config_path: Path to JSON config file
            backend_override: Override backend from config (optional)
        
        Returns:
            Configured translator instance
        
        Config format:
            {
                "backend": "openai",  // or "anthropic", "ollama"
                "openai": {
                    "api_key": "sk-...",
                    "model": "gpt-4",
                    "temperature": 0.3
                },
                "anthropic": {
                    "api_key": "sk-ant-...",
                    "model": "claude-3-sonnet-20240229"
                },
                "ollama": {
                    "model": "llama2-ja:13b",
                    "api_url": "http://localhost:11434"
                },
                "glossary": {
                    "robot": "ロボット",
                    "servo": "サーボ"
                }
            }
        """
        config_path_obj = Path(config_path)
        if not config_path_obj.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")
        
        with open(config_path_obj, 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # Determine backend
        backend = backend_override or config.get("backend", "ollama")
        
        if not cls.is_available(backend):
            print(f"Warning: Backend '{backend}' not available. Falling back to 'ollama'")
            backend = "ollama"
        
        # Get backend-specific config
        backend_config = config.get(backend, {})
        
        # Add glossary if present
        if "glossary" in config:
            backend_config["glossary"] = config["glossary"]
        
        return cls.create(backend, **backend_config)
    
    @classmethod
    def register_backend(
        cls,
        name: str,
        backend_class: Type[Translator]
    ) -> None:
        """
        Register a custom backend.
        
        Args:
            name: Backend identifier
            backend_class: Translator class (must inherit Translator)
        
        Example:
            class MyCustomTranslator(Translator):
                ...
            
            TranslatorRegistry.register_backend("custom", MyCustomTranslator)
            translator = TranslatorRegistry.create("custom")
        """
        if not issubclass(backend_class, Translator):
            raise ValueError(f"{backend_class} must inherit from Translator")
        
        cls._backends[name.lower()] = backend_class
    
    @classmethod
    def get_backend_info(cls, backend: str) -> Dict[str, str]:
        """
        Get information about a backend.
        
        Args:
            backend: Backend name
        
        Returns:
            Dict with backend information
        """
        if not cls.is_available(backend):
            return {"error": f"Backend '{backend}' not available"}
        
        backend_class = cls._backends[backend.lower()]
        
        info = {
            "name": backend,
            "class": backend_class.__name__,
            "module": backend_class.__module__,
        }
        
        if hasattr(backend_class, "__doc__"):
            info["description"] = backend_class.__doc__.strip().split("\n")[0]
        
        return info
    
    @classmethod
    def print_available_backends(cls) -> None:
        """Print all available backends with descriptions."""
        print("Available Translation Backends:")
        print("=" * 60)
        
        for backend in sorted(set(cls._backends.keys())):
            info = cls.get_backend_info(backend)
            desc = info.get("description", "No description")
            print(f"  {backend:15} - {desc}")
        
        print("=" * 60)
        
        # Show which optional backends are missing
        missing = []
        if not HAS_OPENAI:
            missing.append("openai (pip install openai)")
        if not HAS_ANTHROPIC:
            missing.append("anthropic (pip install anthropic)")
        
        if missing:
            print("\nOptional backends (not installed):")
            for m in missing:
                print(f"  - {m}")


# Convenience function
def create_translator(
    backend: str = "ollama",
    config_path: Optional[str] = None,
    **kwargs
) -> Translator:
    """
    Convenience function to create a translator.
    
    Args:
        backend: Backend name (default: "ollama")
        config_path: Optional config file path
        **kwargs: Backend-specific parameters
    
    Returns:
        Configured translator instance
    
    Example:
        # From config
        translator = create_translator(config_path="config.json")
        
        # Direct creation
        translator = create_translator("openai", model="gpt-4")
    """
    if config_path:
        return TranslatorRegistry.create_from_config(config_path, backend_override=backend)
    else:
        return TranslatorRegistry.create(backend, **kwargs)
