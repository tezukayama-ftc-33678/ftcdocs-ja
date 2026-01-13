#!/usr/bin/env python3
"""
RST Markup Protection Module

This module extracts, protects, and restores reStructuredText (RST) markup.
It ensures RST syntax is never modified during translation while maintaining
proper spacing between Japanese text and markup.

Key Feature: Japanese Spacing
-----------------------------
Japanese text requires half-width spaces around inline markup to prevent Sphinx errors:

    BAD:  日本語this_is_code`_へのリンク  → Sphinx build fails
    GOOD: 日本語 this_is_code `_ へのリンク  → Sphinx builds correctly

This module automatically detects Japanese characters adjacent to markup and inserts
the required spaces during restoration.

Protected Patterns
------------------
Listed in priority order (more specific patterns first):

1. External links: `text <url>`_
2. Roles: :ref:`text`, :doc:`text`, :download:`file`, etc.
3. URLs: http://..., https://...
4. File paths: file.py, images/sample.png, manual.pdf, etc.
5. Inline literals: ``code``
6. Bold/italic: **bold**, *italic*
7. Internal links: `text`_
8. Substitutions: |name|

Each pattern is replaced with a unique placeholder (e.g., __RST_ROLE_0__),
allowing the translator to work with clean text while preserving all markup.
"""

import re
from typing import Dict, List, Tuple


class RSTProtector:
    """
    Protects RST markup from translation and restores it afterward.
    
    Handles Japanese spacing requirements: ensures half-width spaces
    before/after markup when adjacent to Japanese characters.
    """
    
    def __init__(self):
        """Initialize the protector with RST pattern definitions."""
        self.placeholders: Dict[str, str] = {}
        self.counter: int = 0
        
        # RST patterns to protect, in priority order (more specific first)
        # Order matters: longer/more specific patterns must be processed before shorter ones
        self.patterns = [
            # 1. External links: `text <url>`_
            # Must come before generic roles to avoid mismatching
            (r'`[^<`]+<[^>`]+>`_', 'extlink'),
            
            # 2. Roles (most common): :ref:`text`, :doc:`text`, :download:`file`, etc.
            # Pattern: :word:word::`text`
            (r':[a-z_]+:`[^`]+`', 'role'),
            
            # 3. URLs (http/https)
            # Standalone URLs that aren't inside markup
            (r'https?://[^\s<>`\[\]()]+', 'url'),
            
            # 4. File paths with extensions
            # Matches: file.py, path/to/file.txt, etc.
            (r'[a-zA-Z0-9_\-./]+\.(png|jpg|jpeg|gif|svg|pdf|rst|py|java|md|txt|zip|tar|gz|bmp|ico)', 'filepath'),
            
            # 5. Inline literals: ``code``
            (r'``[^`]+``', 'literal'),
            
            # 6. Strong emphasis: **text**
            (r'\*\*[^\*]+\*\*', 'strong'),
            
            # 7. Emphasis: *text* (but not *text* in the middle of words)
            (r'\*[^\*\s][^\*]*[^\*\s]\*', 'emphasis'),
            
            # 8. Internal links: `text`_
            (r'`[^`]+`_', 'intlink'),
            
            # 9. Substitutions: |name|
            (r'\|[^\|]+\|', 'substitution'),
        ]
    
    def protect(self, text: str) -> Tuple[str, Dict[str, str]]:
        """
        Extract and protect RST markup from text.
        
        Replaces all RST patterns with unique placeholders, allowing
        the translator to work with clean text.
        
        Args:
            text: Raw text containing RST markup
        
        Returns:
            Tuple of:
            - protected_text: Text with markup replaced by placeholders
            - placeholders: Dict mapping placeholder → original markup
            
        Example:
            >>> protector = RSTProtector()
            >>> text = "See :doc:`docs </path>` for details."
            >>> protected, ph = protector.protect(text)
            >>> protected
            'See __RST_ROLE_0__ for details.'
            >>> ph
            {'__RST_ROLE_0__': ':doc:`docs </path>`'}
        """
        protected_text = text
        self.placeholders = {}
        self.counter = 0
        
        # Apply each pattern in order
        for pattern, markup_type in self.patterns:
            protected_text = self._protect_pattern(protected_text, pattern, markup_type)
        
        return protected_text, self.placeholders
    
    def _protect_pattern(self, text: str, pattern: str, markup_type: str) -> str:
        """
        Replace all matches of a pattern with placeholders.
        
        Args:
            text: Text to search
            pattern: Regex pattern to match
            markup_type: Category name for the placeholder
        
        Returns:
            Text with all pattern matches replaced by placeholders
        """
        def replace_match(match):
            # Create unique placeholder
            placeholder = f"__RST_{markup_type.upper()}_{self.counter}__"
            # Store original content
            self.placeholders[placeholder] = match.group(0)
            self.counter += 1
            return placeholder
        
        # Use re.IGNORECASE for case-insensitive role matching
        return re.sub(pattern, replace_match, text)
    
    def restore(self, text: str, placeholders: Dict[str, str]) -> str:
        """
        Restore placeholders back to original RST markup.
        
        Critically handles Japanese spacing: inserts half-width spaces
        before/after markup when adjacent to Japanese characters.
        
        Sphinx requires spaces between Japanese and markup:
            日本語 :role: テキスト  ← correct
            日本語:role:テキスト    ← causes build errors
        
        Args:
            text: Text with placeholders (already translated)
            placeholders: Dict mapping placeholder → original markup
        
        Returns:
            Text with placeholders restored and proper spacing
            
        Example:
            >>> text = "詳細は __RST_ROLE_0__ を参照してください。"
            >>> ph = {'__RST_ROLE_0__': ':doc:`docs </path>`'}
            >>> protector.restore(text, ph)
            '詳細は :doc:`docs </path>` を参照してください。'
        """
        if not placeholders:
            return text
        
        result = text
        
        # Helper function to detect Japanese characters
        def is_japanese(c: str) -> bool:
            """Check if character is Japanese (hiragana, katakana, kanji, or Japanese punctuation)."""
            if not c:
                return False
            try:
                code = ord(c)
                # Unicode ranges for Japanese text
                is_hiragana = '\u3040' <= c <= '\u309f'      # U+3040-U+309F
                is_katakana = '\u30a0' <= c <= '\u30ff'      # U+30A0-U+30FF
                is_kanji = '\u4e00' <= c <= '\u9fff'         # U+4E00-U+9FFF
                is_jp_punct = c in '、。（）【】「」『』'      # Japanese punctuation
                
                return is_hiragana or is_katakana or is_kanji or is_jp_punct
            except (TypeError, ValueError):
                return False
        
        # Restore each placeholder
        for placeholder, original in placeholders.items():
            pos = 0
            while True:
                # Find next occurrence of placeholder
                pos = result.find(placeholder, pos)
                if pos == -1:
                    break
                
                # Check characters before and after placeholder
                before_char = result[pos - 1] if pos > 0 else ''
                after_pos = pos + len(placeholder)
                after_char = result[after_pos] if after_pos < len(result) else ''
                
                # Determine if spaces are needed
                # Space needed if Japanese character is directly adjacent
                need_space_before = is_japanese(before_char) and before_char not in ' \n\t'
                need_space_after = is_japanese(after_char) and after_char not in ' \n\t'
                
                # Build restored text with proper spacing
                restored_with_space = ''
                if need_space_before:
                    restored_with_space += ' '
                restored_with_space += original
                if need_space_after:
                    restored_with_space += ' '
                
                # Replace in result text
                result = result[:pos] + restored_with_space + result[after_pos:]
                
                # Update position for next search
                pos = pos + len(restored_with_space)
        
        return result


def should_skip_translation(text: str) -> bool:
    """
    Determine if text should be skipped during translation.
    
    Some entries are not meant to be translated:
    - Empty or whitespace-only text
    - URLs
    - Numbers and symbols only
    - Code block markers
    
    Args:
        text: Text to check
    
    Returns:
        True if text should be skipped, False otherwise
    """
    # Empty or whitespace only
    if not text or not text.strip():
        return True
    
    # URL only
    if re.match(r'^https?://', text.strip()):
        return True
    
    # Numbers and symbols only
    if re.match(r'^[\d\s\-_.,:;!?()[\]{}]+$', text.strip()):
        return True
    
    # Code block marker
    if text.strip().startswith('```') or text.strip().startswith('::'):
        return True
    
    return False


def split_into_chunks(text: str, max_length: int = 500) -> List[str]:
    """
    Split text into manageable chunks for translation.
    
    Large entries are split by:
    1. Paragraphs (separated by blank lines)
    2. If still too long, by sentences
    
    This prevents exceeding LLM context windows and improves translation quality.
    
    Args:
        text: Text to split
        max_length: Maximum characters per chunk
    
    Returns:
        List of text chunks
        
    Example:
        >>> text = "Paragraph 1.\n\nParagraph 2. More text."
        >>> chunks = split_into_chunks(text, max_length=20)
        >>> len(chunks)
        2
    """
    # First, split by paragraphs (blank lines)
    paragraphs = re.split(r'\n\s*\n', text)
    
    chunks = []
    current_chunk = []
    current_length = 0
    
    for para in paragraphs:
        para_length = len(para)
        
        # If paragraph is too long, split by sentences
        if para_length > max_length:
            sentences = re.split(r'([.!?。！？])\s*', para)
            for i in range(0, len(sentences), 2):
                sentence = sentences[i]
                if i + 1 < len(sentences):
                    sentence += sentences[i + 1]
                
                # Add sentence to current chunk or start new one
                if current_length + len(sentence) > max_length and current_chunk:
                    chunks.append('\n\n'.join(current_chunk))
                    current_chunk = [sentence]
                    current_length = len(sentence)
                else:
                    current_chunk.append(sentence)
                    current_length += len(sentence)
        else:
            # Paragraph fits, add to current chunk or start new one
            if current_length + para_length > max_length and current_chunk:
                chunks.append('\n\n'.join(current_chunk))
                current_chunk = [para]
                current_length = para_length
            else:
                current_chunk.append(para)
                current_length += para_length
    
    # Add remaining chunk
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
    
    return chunks
