#!/usr/bin/env python3
"""
Translation Progress Checker for FTC Documentation

This script scans all RST files in the docs/source directory and checks
if they have been completely translated to Japanese. It detects English text
remaining in files, especially in the middle or at the end of sentences.

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


class TranslationChecker:
    """Check translation progress of RST files."""
    
    def __init__(self, source_dir: str):
        self.source_dir = Path(source_dir)
        self.total_files = 0
        self.translated_files = 0
        self.partially_translated = 0
        self.untranslated_files = 0
        self.results: Dict[str, Dict] = {}
        
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
    
    def detect_english_issues(self, file_path: Path) -> List[Dict]:
        """
        Detect English text remaining in the file.
        Returns list of issues with line numbers and details.
        """
        issues = []
        
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
            
            # Check for English at the end of a line (after Japanese text)
            if self.has_japanese(line) and ENGLISH_AT_END_PATTERN.search(line):
                # Extract the English part
                match = re.search(r'([A-Za-z]+(?:\s+[A-Za-z]+)*)[.!?]?\s*$', line)
                if match:
                    english_part = match.group(1)
                    issues.append({
                        'line': i,
                        'issue': 'English text at end of line',
                        'text': f'...{line.strip()[-60:]}'
                    })
                    continue
            
            # Check for English sentences in the middle
            # Only flag if line has Japanese but also has long English phrases
            if self.has_japanese(line):
                english_matches = ENGLISH_SENTENCE_PATTERN.findall(line)
                if english_matches:
                    # Filter out common technical terms that should stay in English
                    significant_english = [
                        match for match in english_matches
                        if len(match.split()) >= 3  # 3+ word phrases
                    ]
                    if significant_english:
                        issues.append({
                            'line': i,
                            'issue': 'Mixed Japanese and English text',
                            'text': line.strip()[:80]
                        })
                        continue
            
            # Check for lines that are entirely English (potential untranslated content)
            # Only flag if it's a substantial line (not just a title or short phrase)
            if not self.has_japanese(stripped) and len(stripped.split()) >= 5:
                # Check if it's likely a paragraph or sentence (not a title)
                if any(c in stripped for c in '.!?,;:'):
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
            f.write("詳細な翻訳ガイドラインは `TRANSLATION_GUIDE.md` を参照してください。\n")
            f.write("作業効率化ツールについては `TRANSLATION_WORKFLOW_TOOLS.md` を参照してください。\n")
        
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
    if not Path(SOURCE_DIR).exists():
        print(f"Error: Source directory '{SOURCE_DIR}' not found.")
        sys.exit(1)
    
    # Create checker and scan files
    checker = TranslationChecker(SOURCE_DIR)
    checker.scan_directory()
    
    # Generate report
    checker.generate_report(OUTPUT_FILE)
    
    # Print summary
    print()
    print("=" * 60)
    print("Summary:")
    print(f"  Total files: {checker.total_files}")
    print(f"  Completed: {checker.translated_files} ({checker.translated_files/checker.total_files*100:.1f}%)")
    print(f"  Partial: {checker.partially_translated} ({checker.partially_translated/checker.total_files*100:.1f}%)")
    print(f"  Untranslated: {checker.untranslated_files} ({checker.untranslated_files/checker.total_files*100:.1f}%)")
    print("=" * 60)
    print()
    print(f"✓ Report saved to: {OUTPUT_FILE}")
    print()


if __name__ == "__main__":
    main()
