#!/usr/bin/env python3
"""
Local LLM Translator Implementation

Translates text using Ollama (local, offline LLM service).

Uses Qwen2.5-Coder model (or fallback) for technical documentation translation
with RST markup protection and quality checks.

Requirements:
- Ollama installed and running (http://localhost:11434)
- Model downloaded: ollama pull qwen2.5-coder:7b-instruct

See: https://ollama.com/
"""

import time
import re
from typing import Dict, Optional, List
from pathlib import Path
import sys

from .translator_base import Translator, TranslationError

# Import QualityChecker from core module
sys.path.insert(0, str(Path(__file__).parent.parent))
from core.quality_checker import QualityChecker


class LocalLLMTranslator(Translator):
    """
    Translates text using a local Ollama LLM model.
    
    Configuration:
        model: Main model to use (default: qwen2.5-coder:7b-instruct)
        fallback_model: Alternative model if main fails (default: qwen2.5:7b-instruct-q5_K_M)
        temperature: LLM temperature (0.0-1.0, lower = more consistent)
        max_retries: Number of retry attempts on failure
        glossary: Dict of English terms to preserve (e.g., {"FTC": "FTC"})
    """
    
    def __init__(self, model: str = "qwen2.5-coder:7b-instruct",
                 fallback_model: Optional[str] = None,
                 temperature: float = 0.1,
                 max_retries: int = 3,
                 glossary: Optional[Dict[str, str]] = None):
        """
        Initialize LocalLLMTranslator.
        
        Args:
            model: Main Ollama model name
            fallback_model: Fallback model if main fails
            temperature: LLM temperature (lower = more deterministic)
            max_retries: Number of retry attempts
            glossary: Terms to preserve in English
            
        Raises:
            ImportError: If ollama package not available
        """
        try:
            import ollama
            self.ollama = ollama
        except ImportError:
            raise ImportError(
                "ollama package required. Install with: pip install ollama"
            )
        
        self.model = model
        self.fallback_model = fallback_model or "qwen2.5:7b-instruct-q5_K_M"
        self.temperature = temperature
        self.max_retries = max_retries
        self.glossary = glossary or {}
        self.quality_checker = QualityChecker()
        
        # Statistics
        self.stats = {
            'total_requests': 0,
            'successful': 0,
            'failed': 0,
            'retries_used': 0,
        }
    
    def translate(self, text: str, context: str = "") -> str:
        """
        Translate text using local LLM.
        
        Args:
            text: Text to translate (may contain RST placeholders like __RST_ROLE_0__)
            context: Previous chunk context for coherence
        
        Returns:
            Translated Japanese text
        
        Raises:
            TranslationError: If translation fails after all retries
        """
        self.stats['total_requests'] += 1
        
        if not text or not text.strip():
            return text
        
        # Try models in order: main, then fallback
        models_to_try = [self.model]
        if self.fallback_model != self.model:
            models_to_try.append(self.fallback_model)
        
        last_error = None
        
        for model in models_to_try:
            for attempt in range(self.max_retries):
                try:
                    # Generate translation prompt
                    prompt = self._create_prompt(text, context)
                    
                    # Call Ollama
                    response = self.ollama.generate(
                        model=model,
                        prompt=prompt,
                        options={
                            'temperature': self.temperature,
                            'num_predict': len(text) * 3,  # Japanese is longer
                        }
                    )
                    
                    translated = response['response'].strip()
                    
                    # Clean output (remove extra explanations)
                    translated = self._clean_translation(translated)
                    
                    # Quality check (Chinese detection)
                    if self.quality_checker.has_simplified_chinese(translated):
                        if model == models_to_try[0]:  # Not on fallback
                            # Try fallback model
                            break
                        else:
                            # Fallback also failed, record and continue
                            error_msg = f"Simplified Chinese detected in output"
                            raise TranslationError(
                                error_msg,
                                original_text=text,
                                retryable=True
                            )
                    
                    # Validate Japanese
                    if not self.quality_checker.is_valid_japanese(translated):
                        raise TranslationError(
                            "Output is not valid Japanese",
                            original_text=text,
                            retryable=True
                        )
                    
                    self.stats['successful'] += 1
                    return translated
                    
                except Exception as e:
                    last_error = e
                    
                    if attempt < self.max_retries - 1:
                        # Exponential backoff
                        wait_time = 2 ** attempt
                        time.sleep(wait_time)
                        self.stats['retries_used'] += 1
                        continue
                    
                    # Last attempt failed, try next model
                    break
        
        # All models and retries exhausted
        self.stats['failed'] += 1
        raise TranslationError(
            f"Translation failed with all models after {self.max_retries} retries: {last_error}",
            original_text=text,
            retryable=True
        )
    
    def _create_prompt(self, text: str, context: str = "") -> str:
        """
        Create translation prompt for the LLM.
        
        Optimized for token efficiency:
        - Only include relevant glossary terms
        - Shorter placeholder notes
        - Minimal context
        """
        # 用語集: テキストに含まれる項目のみ（最大10件）
        relevant_glossary = {en: ja for en, ja in self.glossary.items() if en.lower() in text.lower()}
        glossary_text = "\n".join([
            f"- {en} → {ja}" for en, ja in list(relevant_glossary.items())[:10]
        ]) if relevant_glossary else "(none needed)"
        
        # プレースホルダー: 存在する場合のみ注記
        placeholder_pattern = r'__RST_[A-Z_]+_\d+__'
        placeholders_in_text = re.findall(placeholder_pattern, text)
        
        placeholder_note = ""
        if placeholders_in_text:
            # 簡潔化: 具体的なリストは不要（パターンで十分）
            placeholder_note = f"\nPLACEHOLDERS: Keep __RST_*__ exactly as-is.\n"
        
        # コンテキスト: 最初の100文字のみ
        context_note = ""
        if context:
            context_short = context[:100] + "..." if len(context) > 100 else context
            context_note = f"CONTEXT: {context_short}\n\n"
        
        prompt = f"""Technical translator: English → Japanese (FTC docs)

🚨 RULES:
1. Japanese ONLY (no Chinese: 为应该这处理)
2. です・ます form
3. Preserve placeholders & formatting{placeholder_note}
GLOSSARY:
{glossary_text}

{context_note}TRANSLATE:
{text}

JAPANESE:"""
        
        return prompt
    
    def _clean_translation(self, text: str) -> str:
        """
        Clean LLM output: remove unwanted explanations and formatting.
        
        The LLM sometimes adds extra text like:
        - "(Translation: ...)"
        - Markdown image syntax
        - Bullet point lists
        - Extra sentences
        
        This method removes such artifacts.
        """
        # Remove markdown explanations
        text = re.sub(r'\s*\(Translation:.*?\)', '', text, flags=re.DOTALL)
        text = re.sub(r'!\[.*?\]\(.*?\)', '', text, flags=re.DOTALL)
        
        # Remove bullet points
        text = re.sub(r'(：|。)\n(- .*?\n)+', r'\1\n', text)
        
        # Remove extra explanatory sentences
        text = re.sub(r'(。)\n([こここれ].*?。)', r'\1', text, flags=re.DOTALL)
        
        # Normalize whitespace
        text = re.sub(r'\n\n+', '\n', text)
        
        # Remove lines that are just markers
        lines = text.split('\n')
        cleaned_lines = []
        
        for line in lines:
            stripped = line.strip()
            
            if not stripped:
                continue
            
            # Skip marker lines
            if re.match(r'^[\*\_]+$', stripped):
                continue
            
            # Skip bullet lists (usually added by LLM)
            if stripped.startswith('- '):
                continue
            
            cleaned_lines.append(line)
        
        text = '\n'.join(cleaned_lines).strip()
        
        return text
    
    def estimate_tokens(self, text: str) -> int:
        """
        Estimate tokens for text.
        
        Ollama uses different tokenizers per model, but rough estimate:
        - English: ~4 characters per token
        - Japanese: ~2-3 characters per token (more densely packed)
        
        Uses conservative estimate (round up).
        
        Args:
            text: Text to estimate
        
        Returns:
            Estimated token count
        """
        # Conservative estimate: Japanese is ~2.5 chars per token
        # English is ~4 chars per token
        # Mixed: use 3 as average
        return max(1, len(text) // 3)
    
    def get_config(self) -> Dict:
        """Get current configuration."""
        return {
            'model': self.model,
            'fallback_model': self.fallback_model,
            'temperature': self.temperature,
            'max_retries': self.max_retries,
            'glossary_size': len(self.glossary),
        }
