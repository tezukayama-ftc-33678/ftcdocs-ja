#!/usr/bin/env python3
"""
Fix Literal Newlines in PO Files

Removes literal `\n` strings in msgstr entries while preserving actual line breaks.
This handles cases where AI translation outputs actual '\n' characters instead of newlines.

Usage:
    python scripts/fix_literal_newlines.py locales/ja/LC_MESSAGES
    python scripts/fix_literal_newlines.py locales/ja/LC_MESSAGES/index.po
"""

import os
import sys
import re
from pathlib import Path
from typing import List, Tuple

try:
    from colorama import init, Fore, Style
except ImportError:
    print("Error: colorama not found. Install with: pip install colorama")
    sys.exit(1)

init(autoreset=True)


def find_po_files(path: str) -> List[Path]:
    """Find all .po files in path (file or directory)."""
    path_obj = Path(path)
    
    if path_obj.is_file() and path_obj.suffix == '.po':
        return [path_obj]
    
    if path_obj.is_dir():
        return sorted(path_obj.glob('**/*.po'))
    
    return []


def fix_po_file(po_path: str) -> Tuple[int, int]:
    """
    Fix literal \n in msgstr entries.
    
    Returns:
        (files_processed, total_fixes)
    """
    po_file = Path(po_path)
    
    if not po_file.exists():
        print(f"{Fore.RED}File not found: {po_path}")
        return 0, 0
    
    with open(po_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    fix_count = 0
    
    # Pattern: msgstr line(s) with literal \n
    # Match msgstr "..." or msgstr ""
    # followed by "..." lines with \n
    
    lines = content.split('\n')
    result_lines = []
    in_msgstr = False
    
    for i, line in enumerate(lines):
        if line.startswith('msgstr'):
            in_msgstr = True
            result_lines.append(line)
        elif in_msgstr:
            if line.startswith('"') and line.endswith('"'):
                # This is a continuation of msgstr
                # Replace literal \n with nothing
                new_line = line.replace('\\n', '')
                
                if new_line != line:
                    fix_count += 1
                    print(f"  {Fore.YELLOW}Fixed: {line} → {new_line}")
                
                result_lines.append(new_line)
            else:
                # End of msgstr
                in_msgstr = False
                result_lines.append(line)
        else:
            result_lines.append(line)
    
    new_content = '\n'.join(result_lines)
    
    # Only write if changes were made
    if new_content != original_content:
        with open(po_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"{Fore.GREEN}✓ Fixed: {po_file.name} ({fix_count} fixes)")
        return 1, fix_count
    else:
        print(f"{Fore.CYAN}• No changes: {po_file.name}")
        return 1, 0


def main():
    """Main function."""
    if len(sys.argv) < 2:
        print("Usage: python scripts/fix_literal_newlines.py <path>")
        print("  <path> can be a directory or a .po file")
        sys.exit(1)
    
    path = sys.argv[1]
    po_files = find_po_files(path)
    
    if not po_files:
        print(f"{Fore.RED}No PO files found in: {path}")
        sys.exit(1)
    
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.CYAN}Fixing Literal Newlines")
    print(f"{Fore.CYAN}{'='*60}")
    print(f"Found {len(po_files)} PO files\n")
    
    total_files = 0
    total_fixes = 0
    
    for po_file in po_files:
        files, fixes = fix_po_file(str(po_file))
        total_files += files
        total_fixes += fixes
    
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"{Fore.GREEN}✓ Completed!")
    print(f"{Fore.CYAN}Total files processed: {total_files}")
    print(f"{Fore.CYAN}Total fixes applied: {total_fixes}")
    print(f"{Fore.CYAN}{'='*60}\n")


if __name__ == '__main__':
    main()
