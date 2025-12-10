#!/usr/bin/env python3
"""
Translation Progress Checker for FTC Documentation

This script scans all RST files in the docs/source directory and checks
if they have been completely translated to Japanese. It detects English text
remaining in files, especially in the middle or at the end of sentences.

Loads GLOSSARY.md to identify technical terms that should remain in English.

Output: TRANSLATION_PROGRESS.md (overwritten each time)
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Set


# Directory containing RST files to check
SOURCE_DIR = "docs/source"

# Output file (in repository root)
OUTPUT_FILE = "TRANSLATION_PROGRESS.md"

# Glossary file (in repository root)
GLOSSARY_FILE = "GLOSSARY.md"

# Minimum word length for glossary term matching
MIN_WORD_LENGTH = 2

# Detection flags (can be toggled)
DETECT_MIXED_TEXT = True  # Mixed Japanese and English text detection (often intentional)

# Patterns to detect Japanese text
HIRAGANA_PATTERN = re.compile(r'[\u3040-\u309F]')  # Hiragana
KATAKANA_PATTERN = re.compile(r'[\u30A0-\u30FF]')  # Katakana
KANJI_PATTERN = re.compile(r'[\u4E00-\u9FFF]')     # Kanji

# Pattern to detect English sentences/phrases (3+ consecutive English words)
ENGLISH_SENTENCE_PATTERN = re.compile(
    r'\b[A-Za-z]+\s+[A-Za-z]+\s+[A-Za-z]+(?:\s+[A-Za-z]+)*\b'
)

# Pattern to detect English at the end of a line (common AI translation mistake)
ENGLISH_AT_END_PATTERN = re.compile(
    r'[ぁ-んァ-ヶー一-龠、。].*[A-Za-z]+\s+[A-Za-z]+[.!?]?\s*$'
)

# RST code block markers
CODE_BLOCK_MARKERS = ['.. code-block::', '.. code::', '::']

# RST directives to exclude from English detection
RST_DIRECTIVES = [
    ':doc:', ':ref:', ':download:', ':class:', ':func:', ':meth:',
    ':attr:', ':mod:', ':obj:', ':any:', ':numref:', ':envvar:',
    ':token:', ':keyword:', ':option:', ':term:', ':guilabel:',
    ':file:', ':program:', ':command:', ':dfn:', ':kbd:', ':mailheader:',
    ':makevar:', ':manpage:', ':menuselection:', ':pep:', ':rfc:',
    ':samp:', ':abbr:', ':index:', '.. figure::', '.. image::',
    '.. note::', '.. warning::', '.. tip::', '.. important::',
    '.. caution::', '.. danger::', '.. error::', '.. hint::',
    '.. admonition::', '.. toctree::', '.. grid::', '.. grid-item-card::',
    '.. button-ref::', '.. meta::', '.. include::', '.. literalinclude::'
]


def load_glossary_terms(glossary_path: Path) -> Set[str]:
    """
    Load English terms from GLOSSARY.md that should remain in English.
    Returns a set of lowercase terms for case-insensitive matching.
    """
    terms = set()
    
    if not glossary_path.exists():
        print(f"Warning: Glossary file not found at {glossary_path}", file=sys.stderr)
        return terms
    
    try:
        with open(glossary_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract terms from markdown tables in the "和訳しない用語" section
        # Look for patterns like: | OpMode | **OpMode** | ...
        # or lines with English terms in the table
        in_no_translate_section = False
        
        for line in content.split('\n'):
            # Detect the "和訳しない用語" section
            if '和訳しない用語' in line or '英語のまま' in line:
                in_no_translate_section = True
                continue
            
            # Stop at the next major section
            if in_no_translate_section and line.startswith('###') and '和訳' in line:
                in_no_translate_section = False
                continue
            
            # Extract terms from table rows
            if in_no_translate_section and '|' in line:
                # Parse markdown table row
                parts = [p.strip() for p in line.split('|')]
                for part in parts:
                    # Remove markdown formatting like ** and ``
                    clean_part = re.sub(r'\*\*|``', '', part)
                    clean_part = clean_part.strip()
                    
                    # If it contains English words, add them
                    # Look for multi-word terms and single words
                    if clean_part and re.search(r'[A-Za-z]', clean_part):
                        # Add the full term
                        terms.add(clean_part.lower())
                        
                        # Also add individual words from multi-word terms
                        words = re.findall(r'\b[A-Za-z]+\b', clean_part)
                        for word in words:
                            if len(word) > MIN_WORD_LENGTH:  # Skip very short words
                                terms.add(word.lower())
        
        print(f"Loaded {len(terms)} glossary terms from {glossary_path.name}", file=sys.stderr)
        
    except Exception as e:
        print(f"Warning: Error reading glossary file: {e}", file=sys.stderr)
    
    return terms


class TranslationChecker:
    """Check translation progress of RST files."""
    
    def __init__(self, source_dir: str, glossary_terms: Set[str] = None):
        self.source_dir = Path(source_dir)
        self.total_files = 0
        self.translated_files = 0
        self.partially_translated = 0
        self.untranslated_files = 0
        self.results: Dict[str, Dict] = {}
        self.glossary_terms = glossary_terms or set()
        self.bold_terms_freq: Dict[str, int] = {}  # Track frequency of bold English terms
        
    def has_japanese(self, text: str) -> bool:
        """Check if text contains Japanese characters."""
        return bool(
            HIRAGANA_PATTERN.search(text) or
            KATAKANA_PATTERN.search(text) or
            KANJI_PATTERN.search(text)
        )
    
    def is_code_block_line(self, line: str, in_code_block: bool) -> Tuple[bool, bool]:
        """
        Check if line is part of a code block.
        Returns: (is_in_code_block, is_code_block_marker)
        """
        stripped = line.strip()
        
        # Check for code block markers
        for marker in CODE_BLOCK_MARKERS:
            if marker in stripped:
                return True, True
        
        # If we're in a code block, check if we're still indented
        if in_code_block:
            # Empty line or indented line continues the code block
            if not stripped or line.startswith('   ') or line.startswith('\t'):
                return True, False
            # Non-indented non-empty line ends the code block
            else:
                return False, False
        
        return False, False
    
    def is_rst_directive_line(self, line: str) -> bool:
        """Check if line contains RST directive syntax."""
        stripped = line.strip()
        for directive in RST_DIRECTIVES:
            if directive in stripped:
                return True
        return False
    
    def is_url_line(self, line: str) -> bool:
        """Check if line primarily contains a URL."""
        url_pattern = re.compile(r'https?://|www\.')
        return bool(url_pattern.search(line))
    
    def contains_only_glossary_terms(self, text: str) -> bool:
        """
        Check if English text contains only terms from the glossary.
        Returns True if all English words are in the glossary (allowed to remain in English).
        """
        if not self.glossary_terms:
            return False
        
        # Extract all English words from the text
        english_words = re.findall(r'\b[A-Za-z]+\b', text)
        
        if not english_words:
            return False
        
        # Check if all words are in the glossary
        for word in english_words:
            word_lower = word.lower()
            # Skip short words (length <= MIN_WORD_LENGTH) that are often articles or prepositions
            if len(word_lower) <= MIN_WORD_LENGTH:
                continue
            if word_lower not in self.glossary_terms:
                return False
        
        return True
    
    def extract_bold_terms(self, file_path: Path) -> None:
        """
        Extract frequently occurring bold English terms (**term**) from the file.
        Updates self.bold_terms_freq with term frequencies.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Pattern to match **EnglishTerm** (bold markdown syntax)
            bold_pattern = re.compile(r'\*\*([A-Z][A-Za-z0-9\s]+?)\*\*')
            matches = bold_pattern.findall(content)
            
            for term in matches:
                term = term.strip()
                # Only count multi-character English terms
                if len(term) > 1 and re.match(r'^[A-Za-z][A-Za-z0-9\s]*$', term):
                    self.bold_terms_freq[term] = self.bold_terms_freq.get(term, 0) + 1
        
        except Exception:
            pass  # Silently skip files with errors
    
    def remove_code_literals(self, text: str) -> str:
        """
        Remove inline code literals, backtick literals, quoted strings, and italic UI text from text.
        This prevents UI text and code from being flagged as English issues.
        """
        # Remove double backtick literals (``text``)
        text = re.sub(r'``[^`]+``', ' ', text)
        # Remove single backtick literals (`text`)
        text = re.sub(r'`[^`]+`', ' ', text)
        # Remove double-quoted text with straight quotes ("text")
        text = re.sub(r'"[^"]+"', ' ', text)
        # Remove double-quoted text with curly quotes ("text" or "text")
        text = re.sub(r'[""][^""]+[""]', ' ', text)
        # Remove single-quoted text with straight quotes ('text')
        text = re.sub(r"'[^']+'", ' ', text)
        # Remove single-quoted text with curly quotes ('text' or 'text')
        text = re.sub(r"[''][^'']+['']", ' ', text)
        # Remove italic text (*text*) - often used for UI page names and field names
        # But NOT bold italic (***text***) or bold (**text**)
        text = re.sub(r'(?<!\*)\*(?!\*)([^\*]+?)(?<!\*)\*(?!\*)', r' ', text)
        return text
    
    def detect_english_issues(self, file_path: Path) -> List[Dict]:
        """
        Detect English text remaining in the file.
        Returns list of issues with line numbers and details.
        """
        issues = []
        
        # Extract bold terms for glossary suggestions
        self.extract_bold_terms(file_path)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            return [{'line': 0, 'issue': f'Error reading file: {e}', 'text': ''}]
        
        in_code_block = False
        
        for i, line in enumerate(lines, 1):
            # Check if we're in a code block
            in_code_block, is_marker = self.is_code_block_line(line, in_code_block)
            
            if in_code_block:
                continue
            
            # Skip RST directive lines
            if self.is_rst_directive_line(line):
                continue
            
            # Skip URL lines
            if self.is_url_line(line):
                continue
            
            # Skip empty lines and lines with only RST markup
            stripped = line.strip()
            if not stripped or stripped.startswith('..') or stripped.startswith(':'):
                continue
            
            # Skip lines that are just symbols or numbers
            if re.match(r'^[=\-`~*#+\d\s.,;:!?()\[\]{}|/<>@&%$]*$', stripped):
                continue
            
            # Create a version of the line with code literals removed for checking
            line_without_literals = self.remove_code_literals(line)
            
            # Check for English at the end of a line (after Japanese text)
            if self.has_japanese(line_without_literals) and ENGLISH_AT_END_PATTERN.search(line_without_literals):
                # Extract the English part
                match = re.search(r'([A-Za-z]+(?:\s+[A-Za-z]+)*)[.!?]?\s*$', line_without_literals)
                if match:
                    english_part = match.group(1)
                    # Skip if it's only glossary terms (allowed technical terms)
                    if not self.contains_only_glossary_terms(english_part):
                        issues.append({
                            'line': i,
                            'issue': 'English text at end of line',
                            'text': f'...{line.strip()[-60:]}'
                        })
                    continue
            
            # Check for English sentences in the middle
            # Only flag if line has Japanese but also has long English phrases
            # This detection is OFF by default (DETECT_MIXED_TEXT = False)
            if DETECT_MIXED_TEXT and self.has_japanese(line_without_literals):
                english_matches = ENGLISH_SENTENCE_PATTERN.findall(line_without_literals)
                if english_matches:
                    # Filter out common technical terms that should stay in English
                    # and glossary terms
                    significant_english = []
                    for match in english_matches:
                        # Skip if phrase has fewer than 3 words
                        if len(match.split()) < 3:
                            continue
                        # Skip if all words are glossary terms
                        if self.contains_only_glossary_terms(match):
                            continue
                        # Skip if wrapped in asterisks (bold markdown: **term**)
                        # Check if this match appears within ** ** in the original line
                        escaped_match = re.escape(match)
                        if re.search(rf'\*\*[^*]*{escaped_match}[^*]*\*\*', line):
                            continue
                        significant_english.append(match)
                    
                    if significant_english:
                        issues.append({
                            'line': i,
                            'issue': 'Mixed Japanese and English text',
                            'text': line.strip()[:80]
                        })
                        continue
            
            # Check for lines that are entirely English (potential untranslated content)
            # Only flag if it's a substantial line (not just a title or short phrase)
            stripped_without_literals = self.remove_code_literals(stripped).strip()
            if not self.has_japanese(stripped) and len(stripped_without_literals.split()) >= 5:
                # Check if it's likely a paragraph or sentence (not a title)
                if any(c in stripped_without_literals for c in '.!?,;:'):
                    issues.append({
                        'line': i,
                        'issue': 'Untranslated English paragraph/sentence',
                        'text': stripped[:80]
                    })
        
        return issues
    
    def check_file(self, file_path: Path) -> Dict:
        """Check a single RST file for translation status."""
        rel_path = file_path.relative_to(self.source_dir)
        
        result = {
            'path': str(rel_path),
            'status': 'unknown',
            'issues': [],
            'has_japanese': False
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if file has Japanese content
            result['has_japanese'] = self.has_japanese(content)
            
            # Detect English issues
            issues = self.detect_english_issues(file_path)
            result['issues'] = issues
            
            # Determine status
            if not result['has_japanese']:
                result['status'] = 'untranslated'
            elif len(issues) == 0:
                result['status'] = 'completed'
            else:
                result['status'] = 'partial'
            
        except Exception as e:
            result['status'] = 'error'
            result['issues'] = [{'line': 0, 'issue': f'Error: {e}', 'text': ''}]
        
        return result
    
    def scan_directory(self) -> None:
        """Scan all RST files in the source directory."""
        rst_files = list(self.source_dir.rglob('*.rst'))
        self.total_files = len(rst_files)
        
        print(f"Scanning {self.total_files} RST files...")
        
        for file_path in rst_files:
            result = self.check_file(file_path)
            self.results[str(result['path'])] = result
            
            if result['status'] == 'completed':
                self.translated_files += 1
            elif result['status'] == 'partial':
                self.partially_translated += 1
            elif result['status'] == 'untranslated':
                self.untranslated_files += 1
    
    def suggest_glossary_additions(self, min_frequency: int = 5) -> List[Tuple[str, int]]:
        """
        Suggest bold English terms to add to GLOSSARY.md based on frequency.
        Returns list of (term, frequency) tuples sorted by frequency.
        """
        # Filter terms that appear frequently and aren't already in glossary
        suggestions = []
        for term, freq in self.bold_terms_freq.items():
            if freq >= min_frequency:
                # Check if term or any word in term is already in glossary
                term_lower = term.lower()
                words = term_lower.split()
                if not any(word in self.glossary_terms for word in words):
                    suggestions.append((term, freq))
        
        # Sort by frequency (descending)
        suggestions.sort(key=lambda x: x[1], reverse=True)
        return suggestions
    
    def generate_report(self, output_file: str) -> None:
        """Generate markdown report of translation progress."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        completion_rate = (self.translated_files / self.total_files * 100) if self.total_files > 0 else 0
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# 翻訳進捗状況レポート\n\n")
            f.write(f"**生成日時:** {timestamp}\n\n")
            f.write("このレポートは `docs/scripts/check_translation_progress.py` により自動生成されました。\n\n")
            f.write("---\n\n")
            
            # Summary statistics
            f.write("## 📊 統計サマリー\n\n")
            f.write(f"- **総ファイル数:** {self.total_files}\n")
            f.write(f"- **翻訳完了:** {self.translated_files} ({self.translated_files/self.total_files*100:.1f}%)\n")
            f.write(f"- **部分的に翻訳:** {self.partially_translated} ({self.partially_translated/self.total_files*100:.1f}%)\n")
            f.write(f"- **未翻訳:** {self.untranslated_files} ({self.untranslated_files/self.total_files*100:.1f}%)\n\n")
            
            # Progress bar
            completed_blocks = int(completion_rate / 2)
            remaining_blocks = 50 - completed_blocks
            progress_bar = '█' * completed_blocks + '░' * remaining_blocks
            f.write(f"**進捗:** `{progress_bar}` {completion_rate:.1f}%\n\n")
            f.write("---\n\n")
            
            # Completed files
            f.write("## ✅ 翻訳完了ファイル\n\n")
            completed = [path for path, result in self.results.items() if result['status'] == 'completed']
            if completed:
                completed.sort()
                f.write(f"完全に日本語化されているファイル: **{len(completed)}個**\n\n")
                f.write("<details>\n<summary>ファイルリストを表示</summary>\n\n")
                for path in completed:
                    f.write(f"- `{path}`\n")
                f.write("\n</details>\n\n")
            else:
                f.write("該当なし\n\n")
            
            f.write("---\n\n")
            
            # Partially translated files (with issues)
            f.write("## ⚠️ 部分的に翻訳されているファイル\n\n")
            partial = [(path, result) for path, result in self.results.items() if result['status'] == 'partial']
            if partial:
                partial.sort(key=lambda x: len(x[1]['issues']), reverse=True)
                f.write(f"英語が残っているファイル: **{len(partial)}個**\n\n")
                
                for path, result in partial:
                    issue_count = len(result['issues'])
                    f.write(f"### `{path}`\n\n")
                    f.write(f"**問題箇所:** {issue_count}件\n\n")
                    
                    # Show first 5 issues
                    for issue in result['issues'][:5]:
                        f.write(f"- **行 {issue['line']}:** {issue['issue']}\n")
                        if issue['text']:
                            f.write(f"  ```\n  {issue['text']}\n  ```\n")
                    
                    if issue_count > 5:
                        f.write(f"\n... 他 {issue_count - 5} 件の問題\n")
                    
                    f.write("\n")
            else:
                f.write("該当なし\n\n")
            
            f.write("---\n\n")
            
            # Untranslated files
            f.write("## 📝 未翻訳ファイル\n\n")
            untranslated = [path for path, result in self.results.items() if result['status'] == 'untranslated']
            if untranslated:
                untranslated.sort()
                f.write(f"日本語が含まれていないファイル: **{len(untranslated)}個**\n\n")
                f.write("<details>\n<summary>ファイルリストを表示</summary>\n\n")
                for path in untranslated:
                    f.write(f"- `{path}`\n")
                f.write("\n</details>\n\n")
            else:
                f.write("該当なし\n\n")
            
            f.write("---\n\n")
            
            # Instructions
            f.write("## 📖 このレポートの使い方\n\n")
            f.write("1. **部分的に翻訳されているファイル** セクションを確認し、英語が残っている箇所を修正してください。\n")
            f.write("2. **未翻訳ファイル** を確認し、優先度に基づいて翻訳を進めてください。\n")
            f.write("3. 翻訳作業後、このスクリプトを再実行して進捗を確認してください。\n\n")
            f.write("```bash\n")
            f.write("python docs/scripts/check_translation_progress.py\n")
            f.write("```\n\n")
            f.write("**注意:** このスクリプトは `GLOSSARY.md` を読み込み、英語のまま残すべき技術用語を自動的に除外します。\n\n")
            f.write("詳細な翻訳ガイドラインは `TRANSLATION_GUIDE.md` を参照してください。\n")
            f.write("作業効率化ツールについては `TRANSLATION_WORKFLOW_TOOLS.md` を参照してください。\n\n")
            
            # Glossary suggestions section
            suggestions = self.suggest_glossary_additions(min_frequency=5)
            if suggestions:
                f.write("---\n\n")
                f.write("## 💡 GLOSSARY.md への追加候補\n\n")
                f.write("以下の太字英語用語が頻繁に使用されています。GLOSSARY.md にコピー&ペーストして追加できます:\n\n")
                f.write("```markdown\n")
                f.write("| 英語 | 表記 | 備考 |\n")
                f.write("|------|------|------|\n")
                for term, freq in suggestions[:20]:  # Top 20 suggestions
                    f.write(f"| {term} | **{term}** | 出現回数: {freq} |\n")
                f.write("```\n\n")
                if len(suggestions) > 20:
                    f.write(f"**注:** 他に {len(suggestions) - 20} 件の候補があります（出現回数5回以上）。\n\n")
        
        print(f"\nReport generated: {output_file}")


def main():
    """Main entry point."""
    # Get repository root (assuming script is in docs/scripts/)
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    
    # Change to repository root
    os.chdir(repo_root)
    
    print("=" * 60)
    print("FTC Documentation Translation Progress Checker")
    print("=" * 60)
    print()
    
    # Check if source directory exists
    source_path = Path(SOURCE_DIR)
    if not source_path.exists():
        print(f"Source directory '{source_path.absolute()}' not found.")
        sys.exit(1)
    
    # Load glossary terms
    glossary_path = repo_root / GLOSSARY_FILE
    glossary_terms = load_glossary_terms(glossary_path)
    
    # Create checker and scan files
    checker = TranslationChecker(SOURCE_DIR, glossary_terms)
    checker.scan_directory()
    
    # Generate report
    checker.generate_report(OUTPUT_FILE)
    
    # Print summary
    print()
    print("=" * 60)
    print("Summary:")
    print(f"  Total files: {checker.total_files}")
    if checker.total_files > 0:
        print(f"  Completed: {checker.translated_files} ({checker.translated_files/checker.total_files*100:.1f}%)")
        print(f"  Partial: {checker.partially_translated} ({checker.partially_translated/checker.total_files*100:.1f}%)")
        print(f"  Untranslated: {checker.untranslated_files} ({checker.untranslated_files/checker.total_files*100:.1f}%)")
    else:
        print("  No RST files found to check.")
    print("=" * 60)
    print()
    print(f"✓ Report saved to: {OUTPUT_FILE}")
    print()


if __name__ == "__main__":
    main()
