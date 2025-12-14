#!/usr/bin/env python3
"""
RST Syntax Validator
Checks for common RST syntax issues in Japanese FTC documentation.
"""

import sys
import re
from pathlib import Path
from typing import List, Tuple

class RSTValidator:
    def __init__(self):
        self.errors = []
        self.warnings = []
        
    def validate_file(self, filepath: Path) -> Tuple[List[str], List[str]]:
        """Validate a single RST file."""
        self.errors = []
        self.warnings = []
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            self._check_inline_markup_spacing(lines, filepath)
            self._check_title_underlines(lines, filepath)
            self._check_explicit_markup_spacing(lines, filepath)
            self._check_bullet_list_spacing(lines, filepath)
            self._check_duplicate_labels(lines, filepath)
            
        except Exception as e:
            self.errors.append(f"Error reading file: {e}")
        
        return self.errors, self.warnings
    
    def _check_inline_markup_spacing(self, lines: List[str], filepath: Path):
        """Check for inline markup spacing issues with Japanese text."""
        japanese_pattern = r'[ぁ-んァ-ヶー一-龯、。！？「」]'
        
        for i, line in enumerate(lines, 1):
            # Check for `` literal``と pattern (missing space)
            if re.search(r'``[^`]+``' + japanese_pattern, line):
                self.warnings.append(
                    f"{filepath}:{i}: Inline literal followed immediately by Japanese character. "
                    f"Add space after closing backticks."
                )
            
            # Check for **bold**と pattern (missing space)
            if re.search(r'\*\*[^*]+\*\*' + japanese_pattern, line):
                self.warnings.append(
                    f"{filepath}:{i}: Bold markup followed immediately by Japanese character. "
                    f"Add space after closing asterisks."
                )
            
            # Check for *italic*と pattern (missing space)
            if re.search(r'(?<!\*)\*[^*]+\*(?!\*)' + japanese_pattern, line):
                self.warnings.append(
                    f"{filepath}:{i}: Italic markup followed immediately by Japanese character. "
                    f"Add space after closing asterisk."
                )
            
            # Check for >`__の pattern (missing space)
            if re.search(r'>`__' + japanese_pattern, line):
                self.warnings.append(
                    f"{filepath}:{i}: Hyperlink followed immediately by Japanese character. "
                    f"Add space after closing hyperlink."
                )
            
            # Check for :doc:`...`**bold (missing space)
            if re.search(r':doc:`[^`]+`\*\*', line):
                self.warnings.append(
                    f"{filepath}:{i}: :doc: directive followed immediately by bold markup. "
                    f"Add space between them."
                )
    
    def _check_title_underlines(self, lines: List[str], filepath: Path):
        """Check for title underline length issues."""
        for i in range(len(lines) - 1):
            title_line = lines[i].rstrip()
            next_line = lines[i + 1].rstrip()
            
            # Check if next line is an underline (all same character)
            if next_line and len(set(next_line)) == 1 and next_line[0] in '=-~^"\'':
                # Calculate display width of title (Japanese chars = 2, ASCII = 1)
                title_width = sum(2 if ord(c) > 127 else 1 for c in title_line)
                underline_width = len(next_line)
                
                if underline_width < title_width:
                    self.errors.append(
                        f"{filepath}:{i+1}: Title underline too short. "
                        f"Title width: {title_width}, Underline width: {underline_width}. "
                        f"Title: '{title_line[:50]}...'"
                    )
    
    def _check_explicit_markup_spacing(self, lines: List[str], filepath: Path):
        """Check for explicit markup (directives) spacing issues."""
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check for directives (.. directive::)
            if re.match(r'^\.\.\ +\w+::', line):
                # Find end of directive block
                j = i + 1
                while j < len(lines) and (lines[j].startswith('   ') or lines[j].strip() == ''):
                    j += 1
                
                # Check if there's a blank line after directive
                if j < len(lines) and lines[j].strip() != '' and j > i + 1:
                    if lines[j-1].strip() != '':
                        self.warnings.append(
                            f"{filepath}:{j}: Directive block should end with blank line. "
                            f"Add blank line after line {j-1}."
                        )
                i = j
            else:
                i += 1
    
    def _check_bullet_list_spacing(self, lines: List[str], filepath: Path):
        """Check for bullet list spacing issues."""
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Check for bullet list items
            if re.match(r'^-\ +\S', line):
                # Find end of list
                j = i + 1
                while j < len(lines):
                    if lines[j].strip() == '':
                        j += 1
                        break
                    elif re.match(r'^-\ +\S', lines[j]):
                        j += 1
                    elif lines[j].startswith('  '):
                        j += 1
                    else:
                        # End of list without blank line
                        if lines[j].strip() != '':
                            self.warnings.append(
                                f"{filepath}:{j}: Bullet list should end with blank line. "
                                f"Add blank line before line {j}."
                            )
                        break
                i = j
            else:
                i += 1
    
    def _check_duplicate_labels(self, lines: List[str], filepath: Path):
        """Check for duplicate labels in the file."""
        labels = {}
        for i, line in enumerate(lines, 1):
            # Find labels (.. _label:)
            match = re.match(r'^\.\. _([^:]+):', line)
            if match:
                label = match.group(1)
                if label in labels:
                    self.errors.append(
                        f"{filepath}:{i}: Duplicate label '{label}'. "
                        f"First occurrence at line {labels[label]}."
                    )
                else:
                    labels[label] = i

def main():
    """Main function to validate all RST files."""
    if len(sys.argv) > 1:
        # Validate specific files
        files = [Path(f) for f in sys.argv[1:]]
    else:
        # Validate all RST files in docs/source
        docs_dir = Path(__file__).parent.parent / 'source'
        files = list(docs_dir.rglob('*.rst'))
    
    validator = RSTValidator()
    total_errors = 0
    total_warnings = 0
    files_with_issues = 0
    
    print(f"Validating {len(files)} RST files...\n")
    
    for filepath in sorted(files):
        errors, warnings = validator.validate_file(filepath)
        
        if errors or warnings:
            files_with_issues += 1
            print(f"\n{filepath.relative_to(Path.cwd()) if filepath.is_absolute() else filepath}")
            print("=" * 80)
            
            for error in errors:
                print(f"ERROR: {error}")
                total_errors += 1
            
            for warning in warnings:
                print(f"WARNING: {warning}")
                total_warnings += 1
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Files validated: {len(files)}")
    print(f"Files with issues: {files_with_issues}")
    print(f"Total errors: {total_errors}")
    print(f"Total warnings: {total_warnings}")
    
    if total_errors > 0:
        print("\n❌ Validation failed with errors!")
        sys.exit(1)
    elif total_warnings > 0:
        print("\n⚠️  Validation completed with warnings.")
        sys.exit(0)
    else:
        print("\n✅ All files validated successfully!")
        sys.exit(0)

if __name__ == '__main__':
    main()
