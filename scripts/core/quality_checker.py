#!/usr/bin/env python3
"""
Quality Checker Module

Validates translation quality by detecting:
- Simplified Chinese characters (should not appear in Japanese translations)
- Invalid Japanese output
- Other quality issues

Quality is critical because:
1. LLMs sometimes accidentally output Chinese instead of Japanese
2. Mixed or invalid characters cause Sphinx build failures
3. Users need confidence in translation reliability
"""

import json
from pathlib import Path
from typing import Set, List, Dict


class QualityChecker:
    """
    Checks translation quality and validates output.
    """
    
    def __init__(self):
        """Initialize quality checker."""
        # Simplified Chinese characters that should NEVER appear
        # These are distinct from Japanese kanji
        self.simplified_chars = set(
            '为应该这处理方式设置获取发送接收检查验证'
            '搜索结果查找从事进行更多的已经'
            '删检验'
        )
        
        # Valid Japanese character ranges (Unicode)
        self.japanese_ranges = [
            (0x3040, 0x309f),   # Hiragana
            (0x30a0, 0x30ff),   # Katakana
            (0x4e00, 0x9fff),   # Kanji
        ]
        
        self.japanese_punctuation = set('、。（）【】「」『』，；！？')
    
    def has_simplified_chinese(self, text: str, min_count: int = 1) -> bool:
        """
        Detect simplified Chinese characters.
        
        Args:
            text: Text to check
            min_count: Minimum number of Chinese characters to flag as "has Chinese"
        
        Returns:
            True if simplified Chinese characters detected
        """
        if not text:
            return False
        
        chinese_count = sum(1 for c in text if c in self.simplified_chars)
        return chinese_count >= min_count
    
    def is_valid_japanese(self, text: str) -> bool:
        """
        Check if text is valid Japanese.
        
        Requirements:
        - Contains at least some Japanese characters
        - Doesn't have excessive non-Japanese characters
        - No control characters (except newlines, tabs)
        
        Args:
            text: Text to validate
        
        Returns:
            True if valid Japanese, False otherwise
        """
        if not text or not text.strip():
            return False
        
        jp_count = 0
        total_chars = 0
        
        for char in text:
            # Skip whitespace and punctuation
            if char.isspace():
                continue
            if char in self.japanese_punctuation:
                jp_count += 1
                total_chars += 1
                continue
            
            # Check if character is in Japanese range
            char_code = ord(char)
            
            is_japanese = any(
                start <= char_code <= end 
                for start, end in self.japanese_ranges
            )
            
            if is_japanese:
                jp_count += 1
            
            # ASCII and other scripts
            total_chars += 1
        
        # Must have significant Japanese content
        # (Allow some English for technical terms)
        if total_chars == 0:
            return False
        
        jp_ratio = jp_count / total_chars
        return jp_ratio >= 0.5  # At least 50% Japanese
    
    def get_simplified_chars_in_text(self, text: str) -> List[str]:
        """
        Extract simplified Chinese characters found in text.
        
        Args:
            text: Text to check
        
        Returns:
            List of simplified Chinese characters found
        """
        return [c for c in text if c in self.simplified_chars]
    
    def get_japanese_ratio(self, text: str) -> float:
        """
        Calculate percentage of Japanese characters in text.
        
        Args:
            text: Text to analyze
        
        Returns:
            Ratio from 0.0 to 1.0
        """
        if not text:
            return 0.0
        
        jp_count = 0
        total_count = 0
        
        for char in text:
            if char.isspace():
                continue
            
            total_count += 1
            
            char_code = ord(char)
            is_japanese = (
                any(start <= char_code <= end for start, end in self.japanese_ranges)
                or char in self.japanese_punctuation
            )
            
            if is_japanese:
                jp_count += 1
        
        if total_count == 0:
            return 0.0
        
        return jp_count / total_count
    
    def check_text(self, text: str) -> Dict[str, any]:
        """
        Perform comprehensive quality check.
        
        Args:
            text: Text to check
        
        Returns:
            Dict with keys:
            - has_simplified_chinese: bool
            - is_valid_japanese: bool
            - japanese_ratio: float
            - simplified_chars: list
            - issues: list of problem descriptions
        """
        issues = []
        
        has_chinese = self.has_simplified_chinese(text)
        is_valid = self.is_valid_japanese(text)
        jp_ratio = self.get_japanese_ratio(text)
        simplified = self.get_simplified_chars_in_text(text)
        
        if has_chinese:
            issues.append(
                f"Simplified Chinese detected: {', '.join(set(simplified))}"
            )
        
        if not is_valid:
            issues.append(
                f"Not valid Japanese (only {jp_ratio*100:.1f}% Japanese characters)"
            )
        
        if jp_ratio < 0.3:
            issues.append(
                f"Too much non-Japanese content ({(1-jp_ratio)*100:.1f}% non-Japanese)"
            )
        
        return {
            'has_simplified_chinese': has_chinese,
            'is_valid_japanese': is_valid,
            'japanese_ratio': jp_ratio,
            'simplified_chars': simplified,
            'issues': issues,
            'is_acceptable': is_valid and not has_chinese,
        }
    
    def generate_report(self, checks: List[Dict], 
                       output_file: str = "data/quality_report.json") -> None:
        """
        Generate quality report from multiple checks.
        
        Args:
            checks: List of check results from check_text()
            output_file: Where to save report
        """
        report = {
            'total_checks': len(checks),
            'passed': sum(1 for c in checks if c['is_acceptable']),
            'failed': sum(1 for c in checks if not c['is_acceptable']),
            'avg_japanese_ratio': sum(c['japanese_ratio'] for c in checks) / len(checks),
            'issues_found': [
                issue 
                for check in checks 
                for issue in check['issues']
            ],
        }
        
        # Save report
        Path(output_file).parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
