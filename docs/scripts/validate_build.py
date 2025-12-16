#!/usr/bin/env python3
"""
Wrapper script to run Sphinx build, capture warnings, and analyze PO issues.
"""

import subprocess
import sys
import tempfile
from pathlib import Path

def run_sphinx_build(docs_dir: str, target: str = 'html-ja') -> Tuple[int, str, str]:
    """Run Sphinx build and capture stderr (warnings)."""
    cmd = ['make', target]
    
    print(f"🔨 Running: {' '.join(cmd)} in {docs_dir}")
    
    result = subprocess.run(
        cmd,
        cwd=docs_dir,
        capture_output=True,
        text=True
    )
    
    return result.returncode, result.stdout, result.stderr

def main():
    """Main entry point."""
    docs_dir = './docs'
    
    # Run build
    returncode, stdout, stderr = run_sphinx_build(docs_dir)
    
    # Capture warnings from stdout and stderr
    all_output = stdout + '\n' + stderr
    
    # Save build log
    log_file = Path('sphinx_build.log')
    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(all_output)
    
    print(f"📝 Build log saved to {log_file}")
    
    # Run PO validator
    print("\n🔍 Analyzing PO files...")
    validator_result = subprocess.run(
        [
            sys.executable, 'docs/scripts/check_and_fix_po.py',
            '--po-dir', 'locales/ja/LC_MESSAGES',
            '--output', 'po_issues.json',
            '--verbose'
        ],
        cwd='.'
    )
    
    sys.exit(returncode if returncode != 0 else validator_result.returncode)

if __name__ == '__main__':
    from typing import Tuple
    main()
