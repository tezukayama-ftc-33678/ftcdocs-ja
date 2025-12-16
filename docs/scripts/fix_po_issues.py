#!/usr/bin/env python3
"""
Auto-fix script for missing :doc: references in PO files.

Reads po_issues.json and applies fixes to restore missing :doc: references.
"""

import json
import re
import sys
from pathlib import Path
from typing import List, Dict, Tuple

def load_issues(json_file: str) -> List[Dict]:
    """Load issues from JSON file."""
    with open(json_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def read_po_file(po_file: str) -> List[str]:
    """Read PO file lines."""
    with open(po_file, 'r', encoding='utf-8') as f:
        return f.readlines()

def write_po_file(po_file: str, lines: List[str]):
    """Write PO file lines."""
    with open(po_file, 'w', encoding='utf-8', newline='\n') as f:
        f.writelines(lines)

def find_msgid_msgstr_at_line(lines: List[str], start_line: int) -> Tuple[str, str, int, int]:
    """
    Find msgid/msgstr pair starting at given line.
    Returns (msgid, msgstr, msgid_line, msgstr_line).
    """
    # Lines are 0-indexed, but line numbers in issues are 1-indexed
    i = start_line - 1
    
    # Find msgid
    while i < len(lines) and not lines[i].strip().startswith('msgid'):
        i += 1
    
    if i >= len(lines):
        return "", "", -1, -1
    
    msgid_line = i
    msgid_parts = []
    
    # Extract msgid
    line = lines[i].strip()
    match = re.match(r'msgid\s+"(.*)"', line)
    if match:
        msgid_parts.append(match.group(1))
    
    i += 1
    while i < len(lines) and lines[i].strip().startswith('"'):
        match = re.match(r'^"(.*)"', lines[i].strip())
        if match:
            msgid_parts.append(match.group(1))
        i += 1
    
    msgid = ''.join(msgid_parts)
    
    # Find msgstr
    if i < len(lines) and lines[i].strip().startswith('msgstr'):
        msgstr_line = i
        msgstr_parts = []
        
        line = lines[i].strip()
        match = re.match(r'msgstr\s+"(.*)"', line)
        if match:
            msgstr_parts.append(match.group(1))
        
        i += 1
        while i < len(lines) and lines[i].strip().startswith('"'):
            match = re.match(r'^"(.*)"', lines[i].strip())
            if match:
                msgstr_parts.append(match.group(1))
            i += 1
        
        msgstr = ''.join(msgstr_parts)
        
        return msgid, msgstr, msgid_line, msgstr_line
    
    return msgid, "", msgid_line, -1

def restore_doc_references(msgid: str, msgstr: str) -> str:
    """
    Restore missing :doc: references from msgid to msgstr.
    Simple heuristic: if msgid contains :doc:`path`, ensure msgstr has it too.
    """
    if not msgstr:
        return msgstr
    
    # Find all :doc: references in msgid
    msgid_docs = re.findall(r':doc:`[^`]+`', msgid)
    msgstr_docs = re.findall(r':doc:`[^`]+`', msgstr)
    
    missing = [d for d in msgid_docs if d not in msgstr_docs]
    
    if not missing:
        return msgstr
    
    # Simple strategy: append missing docs at end, before punctuation
    new_msgstr = msgstr
    for doc_ref in missing:
        # Try to find the text associated with this doc reference in msgid
        # Pattern: :doc:`path` or some text before/after
        # For now, just append the reference
        if new_msgstr.endswith('.'):
            new_msgstr = new_msgstr[:-1] + ' ' + doc_ref + '.'
        else:
            new_msgstr += ' ' + doc_ref
    
    return new_msgstr

def apply_fixes(issues: List[Dict], dry_run: bool = True) -> Dict[str, int]:
    """Apply fixes to PO files."""
    stats = {
        'total': 0,
        'fixed': 0,
        'skipped': 0,
        'errors': 0
    }
    
    # Group by file
    by_file = {}
    for issue in issues:
        if issue['type'] == 'missing_doc_ref':
            po_file = issue['file']
            by_file.setdefault(po_file, []).append(issue)
    
    print(f"[FIX] Processing {len(by_file)} files with missing :doc: references...")
    
    for po_file, file_issues in by_file.items():
        stats['total'] += len(file_issues)
        
        try:
            # Normalize path - handle both forward/backward slashes
            # Remove leading ..\ or ../ prefix
            po_file_clean = po_file.replace('..\\', '').replace('../', '').replace('\\', '/')
            
            # Build full path from repo root
            po_path = Path('..') / po_file_clean
            
            if not po_path.exists():
                print(f"  [WARN] File not found: {po_path}")
                stats['errors'] += len(file_issues)
                continue
            
            lines = read_po_file(str(po_path))
            modified = False
            
            for issue in file_issues:
                line_num = issue['line']
                msgid, msgstr, msgid_line, msgstr_line = find_msgid_msgstr_at_line(lines, line_num)
                
                if msgstr_line == -1:
                    print(f"  [WARN] Could not find msgstr at line {line_num}")
                    stats['skipped'] += 1
                    continue
                
                # Apply fix
                new_msgstr = restore_doc_references(msgid, msgstr)
                
                if new_msgstr != msgstr:
                    if not dry_run:
                        # Replace msgstr line(s)
                        # This is simplified - assumes msgstr is on single line
                        lines[msgstr_line] = f'msgstr "{new_msgstr}"\n'
                        modified = True
                    
                    stats['fixed'] += 1
                    print(f"  [OK] {po_path.name}:{line_num} - Added :doc: reference")
                else:
                    stats['skipped'] += 1
            
            if modified and not dry_run:
                write_po_file(str(po_path), lines)
                print(f"  [SAVE] Saved {po_path}")
        
        except Exception as e:
            print(f"  [ERROR] Error processing {po_file}: {e}")
            stats['errors'] += len(file_issues)
    
    return stats

def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Auto-fix missing :doc: references in PO files'
    )
    parser.add_argument(
        '--issues',
        default='po_issues.json',
        help='JSON file with issues (default: po_issues.json)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be fixed without modifying files'
    )
    parser.add_argument(
        '--type',
        choices=['missing_doc_ref', 'emphasis_mismatch', 'inconsistent_ref', 'all'],
        default='missing_doc_ref',
        help='Type of issues to fix (default: missing_doc_ref)'
    )
    
    args = parser.parse_args()
    
    if not Path(args.issues).exists():
        print(f"Error: Issues file not found: {args.issues}", file=sys.stderr)
        sys.exit(1)
    
    issues = load_issues(args.issues)
    
    if args.type != 'all':
        issues = [i for i in issues if i['type'] == args.type]
    
    print(f"[INFO] Loaded {len(issues)} issues of type '{args.type}'")
    
    if args.dry_run:
        print("[DRY-RUN] No files will be modified\n")
    
    stats = apply_fixes(issues, dry_run=args.dry_run)
    
    print(f"\n[SUMMARY]")
    print(f"  Total issues: {stats['total']}")
    print(f"  Fixed: {stats['fixed']}")
    print(f"  Skipped: {stats['skipped']}")
    print(f"  Errors: {stats['errors']}")
    
    if args.dry_run and stats['fixed'] > 0:
        print(f"\n[TIP] Run without --dry-run to apply fixes")

if __name__ == '__main__':
    main()
