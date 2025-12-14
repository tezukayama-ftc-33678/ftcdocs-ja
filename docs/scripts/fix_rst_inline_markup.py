#!/usr/bin/env python3
"""
RST Inline Markup Auto-Fixer
Automatically fixes common inline markup spacing issues with Japanese text.
"""

import sys
import re
from pathlib import Path
from typing import Tuple

def fix_inline_markup_spacing(content: str) -> Tuple[str, int]:
    """
    Fix inline markup spacing issues with Japanese text.
    Returns: (fixed_content, number_of_fixes)
    """
    fixes = 0
    original = content
    
    # Pattern for Japanese characters
    # Hiragana (3040-309F), Katakana (30A0-30FF), Kanji (4E00-9FAF), punctuation
    japanese = r'([ぁ-んァ-ヶー一-龯、。！？「」（）])'
    
    # Fix `` literal``と -> `` literal`` と
    new_content = re.sub(r'``([^`]+)``' + japanese, r'``\1`` \2', content)
    if new_content != content:
        fixes += content.count('``') - new_content.count('``')
        content = new_content
    
    # Fix **bold**と -> **bold** と
    new_content = re.sub(r'\*\*([^*]+)\*\*' + japanese, r'**\1** \2', content)
    if new_content != content:
        fixes += 1
        content = new_content
    
    # Fix *italic*と -> *italic* と (but not part of **)
    new_content = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)' + japanese, r'*\1* \2', content)
    if new_content != content:
        fixes += 1
        content = new_content
    
    # Fix hyperlink >`__の -> >`__ の
    new_content = re.sub(r'>`__' + japanese, r'>`__ \1', content)
    if new_content != content:
        fixes += 1
        content = new_content
    
    # Fix :doc:`...`**bold -> :doc:`...` **bold
    new_content = re.sub(r':doc:`([^`]+)`(\*\*)', r':doc:`\1` \2', content)
    if new_content != content:
        fixes += 1
        content = new_content
    
    # Fix :ref:`...`**bold -> :ref:`...` **bold
    new_content = re.sub(r':ref:`([^`]+)`(\*\*)', r':ref:`\1` \2', content)
    if new_content != content:
        fixes += 1
        content = new_content
    
    return content, fixes

def process_file(filepath: Path, dry_run: bool = False) -> Tuple[int, bool]:
    """
    Process a single RST file.
    Returns: (number_of_fixes, success)
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        fixed_content, fixes = fix_inline_markup_spacing(original_content)
        
        if fixes > 0:
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
            return fixes, True
        
        return 0, True
        
    except Exception as e:
        print(f"ERROR processing {filepath}: {e}", file=sys.stderr)
        return 0, False

def main():
    """Main function to process RST files."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Fix inline markup spacing issues in RST files'
    )
    parser.add_argument(
        'files',
        nargs='*',
        help='RST files to process (default: all .rst files in docs/source)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be fixed without modifying files'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show details for each file processed'
    )
    
    args = parser.parse_args()
    
    if args.files:
        files = [Path(f) for f in args.files]
    else:
        docs_dir = Path(__file__).parent.parent / 'source'
        files = list(docs_dir.rglob('*.rst'))
    
    total_files = 0
    total_fixes = 0
    files_modified = 0
    
    print(f"{'DRY RUN: ' if args.dry_run else ''}Processing {len(files)} RST files...\n")
    
    for filepath in sorted(files):
        total_files += 1
        fixes, success = process_file(filepath, args.dry_run)
        
        if not success:
            continue
        
        if fixes > 0:
            files_modified += 1
            total_fixes += fixes
            
            if args.verbose or args.dry_run:
                rel_path = filepath.relative_to(Path.cwd()) if filepath.is_absolute() else filepath
                print(f"{'WOULD FIX' if args.dry_run else 'FIXED'}: {rel_path} ({fixes} issues)")
    
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Files processed: {total_files}")
    print(f"Files {'that would be ' if args.dry_run else ''}modified: {files_modified}")
    print(f"Total fixes {'that would be ' if args.dry_run else ''}applied: {total_fixes}")
    
    if args.dry_run and files_modified > 0:
        print("\n💡 Run without --dry-run to apply these fixes.")
    elif files_modified > 0:
        print("\n✅ Fixes applied successfully!")
    else:
        print("\n✅ No issues found!")

if __name__ == '__main__':
    main()
