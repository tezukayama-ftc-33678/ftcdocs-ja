#!/usr/bin/env python3
"""
Validate all PO files using polib.
"""

import sys
from pathlib import Path
import polib

def validate_po_file(file_path):
    """Validate a single PO file."""
    try:
        po = polib.pofile(str(file_path))
        return True, len(po), None
    except Exception as e:
        return False, 0, str(e)

def validate_all_po_files(directory):
    """Validate all PO files in directory."""
    po_files = list(Path(directory).rglob('*.po'))
    print(f"Validating {len(po_files)} PO files...\n")
    
    valid_count = 0
    invalid_files = []
    
    for po_file in po_files:
        is_valid, entry_count, error = validate_po_file(po_file)
        if is_valid:
            valid_count += 1
        else:
            invalid_files.append((po_file, error))
            print(f"[X] {po_file.relative_to(Path(directory).parent.parent)}")
            print(f"  Error: {error}\n")
    
    print(f"\n{'='*60}")
    print(f"Valid: {valid_count}/{len(po_files)}")
    if invalid_files:
        print(f"Invalid: {len(invalid_files)}/{len(po_files)}")
        print(f"\nInvalid files:")
        for file, error in invalid_files:
            print(f"  - {file.name}: {error.split(chr(10))[0][:80]}")
    else:
        print("[OK] All PO files are valid!")
    print(f"{'='*60}")
    
    return len(invalid_files) == 0

if __name__ == '__main__':
    if len(sys.argv) > 1:
        directory = sys.argv[1]
    else:
        script_dir = Path(__file__).parent
        repo_root = script_dir.parent.parent
        directory = repo_root / 'locales' / 'ja' / 'LC_MESSAGES'
    
    success = validate_all_po_files(directory)
    sys.exit(0 if success else 1)
