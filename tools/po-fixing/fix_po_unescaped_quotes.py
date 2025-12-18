#!/usr/bin/env python3
"""
Fix unescaped quotes and malformed msgid/msgstr in PO files.

This script fixes the following issues:
1. Lines with msgid/msgstr content that have unescaped quote at start
2. Continuation lines ending with msgid/msgstr declaration
"""

import os
import re
import sys
from pathlib import Path

def fix_po_file(file_path):
    """Fix PO file with unescaped quote issues."""
    print(f"Checking: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    fixed_lines = []
    changes_made = 0
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Pattern 1: msgid/msgstr content on previous line ending with quote  
        # followed by line starting with "msgstr "" or "msgid ""
        # Example: "content"\n"msgstr ""\n"translated"
        # Should be: "content"\nmsgstr ""\n"translated"
        match = re.match(r'^"(.*?)"\s*$', line)
        if match and i + 1 < len(lines):
            next_line = lines[i + 1]
            # Check if next line starts with "msgstr "" or "msgid ""  (with leading quote)
            if re.match(r'^"(msgstr|msgid)\s+""', next_line):
                # Remove the leading quote from the next line
                fixed_next = re.sub(r'^"(msgstr|msgid)\s+""', r'\1 ""', next_line)
                fixed_lines.append(line)
                fixed_lines.append(fixed_next)
                print(f"  Line {i+2}: Fixed msgid/msgstr with leading quote")
                changes_made += 1
                i += 2
                continue
        
        # Pattern 2: msgstr/msgid followed by content with quote on next line and then ""
        # Example: msgid "Foo"\n"msgstr ""\n"translated"\n""
        # The "" at the end should be removed
        match = re.match(r'^(msgid|msgstr)\s+"(.*)"\s*$', line)
        if match and i + 1 < len(lines):
            next_line = lines[i + 1]
            # Check if next line is "msgstr "" or "msgid "" (with leading quote)
            if re.match(r'^"(msgstr|msgid)\s+""', next_line):
                # Remove the leading quote
                fixed_next = re.sub(r'^"(msgstr|msgid)\s+""', r'\1 ""', next_line)
                fixed_lines.append(line)
                fixed_lines.append(fixed_next)
                print(f"  Line {i+2}: Fixed msgid/msgstr with leading quote after single-line entry")
                changes_made += 1
                i += 2
                continue
        
        # Pattern 3: Standalone quote after msgstr "" or msgid ""
        # Example: msgstr ""\n""\n
        if line.strip() in ['msgid ""', 'msgstr ""']:
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                if next_line.strip() == '""':
                    # This is fine (empty multi-line string), skip both
                    fixed_lines.append(line)
                    fixed_lines.append(next_line)
                    i += 2
                    continue
                elif next_line.strip() == '"':
                    # Standalone quote (invalid), remove it
                    fixed_lines.append(line)
                    print(f"  Line {i+2}: Removed standalone quote")
                    changes_made += 1
                    i += 2
                    continue
        
        fixed_lines.append(line)
        i += 1
    
    if changes_made > 0:
        with open(file_path, 'w', encoding='utf-8', newline='\n') as f:
            f.writelines(fixed_lines)
        print(f"  [OK] Fixed {changes_made} issues in {file_path}")
        return True
    
    return False

def process_directory(directory):
    """Process all PO files in directory."""
    po_files = list(Path(directory).rglob('*.po'))
    print(f"Found {len(po_files)} PO files\n")
    
    fixed_count = 0
    for po_file in po_files:
        try:
            if fix_po_file(str(po_file)):
                fixed_count += 1
        except Exception as e:
            print(f"  [ERROR] Error processing {po_file}: {e}")
    
    print(f"\n{'='*60}")
    print(f"Fixed {fixed_count} files out of {len(po_files)} total")
    print(f"{'='*60}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        # Default to locales directory
        script_dir = Path(__file__).parent
        repo_root = script_dir.parent.parent
        directory = repo_root / 'locales' / 'ja' / 'LC_MESSAGES'
    
    if not os.path.exists(directory):
        print(f"Error: Directory not found: {directory}")
        sys.exit(1)
    
    process_directory(directory)
