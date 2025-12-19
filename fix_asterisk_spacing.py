#!/usr/bin/env python3
"""
Script to add spaces around ** (double asterisks) in .po file msgstr entries.
This fixes Sphinx warnings: "Inline strong start-string without end-string."

The script:
1. Only modifies msgstr fields, never msgid fields
2. Adds a space after ** when followed by non-whitespace
3. Adds a space before ** when preceded by non-whitespace
4. Handles multi-line msgstr entries
"""

import os
import re
import sys
from pathlib import Path


def fix_asterisk_spacing(content):
    """
    Fix spacing around ** in msgstr entries.
    
    Args:
        content: The content of a .po file
        
    Returns:
        Fixed content with proper spacing around **
    """
    lines = content.split('\n')
    result = []
    in_msgstr = False
    
    for line in lines:
        # Check if we're starting a msgstr entry
        if line.startswith('msgstr'):
            in_msgstr = True
            # Fix the first line of msgstr
            fixed_line = fix_line_spacing(line)
            result.append(fixed_line)
        # Check if we're in a continuation of msgstr (quoted string)
        elif in_msgstr and line.strip().startswith('"') and not line.startswith('msgid'):
            # Fix continuation lines
            fixed_line = fix_line_spacing(line)
            result.append(fixed_line)
        else:
            # If we hit a non-continuation line, we're out of msgstr
            if in_msgstr and not (line.strip().startswith('"') or line.strip() == ''):
                in_msgstr = False
            result.append(line)
    
    return '\n'.join(result)


def fix_line_spacing(line):
    """
    Fix spacing around ** in a single line.
    
    Args:
        line: A line from the .po file
        
    Returns:
        Line with fixed spacing around **
    """
    # First pass: Add space before ** when preceded by non-whitespace (but not another *)
    # This must be done first to avoid conflicts
    line = re.sub(r'([^\s\*])\*\*', r'\1 **', line)
    
    # Second pass: Add space after ** when followed by non-whitespace (but not another *)
    line = re.sub(r'\*\*([^\s\*])', r'** \1', line)
    
    return line


def process_po_file(filepath):
    """
    Process a single .po file to fix asterisk spacing.
    
    Args:
        filepath: Path to the .po file
        
    Returns:
        True if file was modified, False otherwise
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        fixed_content = fix_asterisk_spacing(original_content)
        
        # Only write if content changed
        if fixed_content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            return True
        
        return False
    except Exception as e:
        print(f"Error processing {filepath}: {e}", file=sys.stderr)
        return False


def main():
    """Main function to process all .po files in the locales directory."""
    # Find the repository root
    script_dir = Path(__file__).parent
    locales_dir = script_dir / 'locales' / 'ja' / 'LC_MESSAGES'
    
    if not locales_dir.exists():
        print(f"Error: Directory {locales_dir} does not exist", file=sys.stderr)
        sys.exit(1)
    
    # Find all .po files
    po_files = list(locales_dir.rglob('*.po'))
    
    if not po_files:
        print(f"No .po files found in {locales_dir}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Found {len(po_files)} .po files to process")
    
    modified_count = 0
    for po_file in po_files:
        if process_po_file(po_file):
            modified_count += 1
            print(f"Modified: {po_file.relative_to(script_dir)}")
    
    print(f"\nProcessed {len(po_files)} files, modified {modified_count} files")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
