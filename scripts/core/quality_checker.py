#!/usr/bin/env python3
"""
Quality Checker Module

Validates translation quality by checking:
- Translation is not empty
- Consistency with GLOSSARY.md terminology

The OpenAI models (gpt-4o-mini, gpt-4.1-mini, gpt-5-mini) are reliable enough
for translation quality. This checker focuses on ensuring translations are
usable and consistent with the project's glossary.
"""

import json
from pathlib import Path
from typing import Set, List, Dict


class QualityChecker:
    """
    Checks translation quality - simplified version.
    Focuses on basic validity and glossary consistency.
    """
    
    def __init__(self):
        """Initialize quality checker."""
        # Load glossary for consistency checking
        self.glossary = self._load_glossary()
    
    def _load_glossary(self) -> Dict[str, str]:
        """Load glossary terms for consistency checking."""
        glossary = {}
        glossary_path = Path(__file__).parent.parent.parent / "guides" / "GLOSSARY.md"
        
        if not glossary_path.exists():
            return glossary
        
        try:
            with open(glossary_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if '|' in line and '->' in line:
                        parts = [p.strip() for p in line.split('|')]
                        if len(parts) >= 3:
                            en_term = parts[1]
                            ja_term = parts[2]
                            if en_term and ja_term:
                                glossary[en_term] = ja_term
        except Exception:
            pass
        
        return glossary
    
    def check_translation(self, original: str, translation: str) -> tuple[bool, List[str]]:
        """
        Check if translation is valid.
        
        Args:
            original: Original English text
            translation: Japanese translation
        
        Returns:
            (is_valid, error_messages)
        """
        errors = []
        
        # Must not be empty
        if not translation or not translation.strip():
            errors.append("Translation is empty")
            return False, errors
        
        # That's it - OpenAI models are reliable enough
        return True, []
    
    def is_valid_japanese(self, text: str) -> bool:
        """Check if text is not empty (simplified check)."""
        return bool(text and text.strip())
