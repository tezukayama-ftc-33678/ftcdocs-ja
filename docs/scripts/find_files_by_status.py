#!/usr/bin/env python3
"""
Find Translation Files by Status

This script helps find RST files based on their translation status.
Useful for batch operations or assigning work to translators.

Usage:
    python docs/scripts/find_files_by_status.py --status untranslated
    python docs/scripts/find_files_by_status.py --status partial --directory programming_resources
    python docs/scripts/find_files_by_status.py --status completed --count
"""

import argparse
import sys
from pathlib import Path
from check_translation_progress import TranslationChecker

SOURCE_DIR = "docs/source"


def main():
    parser = argparse.ArgumentParser(
        description="Find RST files by translation status"
    )
    parser.add_argument(
        '--status',
        choices=['completed', 'partial', 'untranslated', 'all'],
        default='all',
        help='Translation status to filter by'
    )
    parser.add_argument(
        '--directory',
        type=str,
        default='',
        help='Subdirectory to search within (e.g., programming_resources)'
    )
    parser.add_argument(
        '--count',
        action='store_true',
        help='Only show count, not file list'
    )
    parser.add_argument(
        '--show-issues',
        action='store_true',
        help='Show issue counts for partial translations'
    )
    
    args = parser.parse_args()
    
    # Get repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent.parent
    
    # Create checker and scan files
    source_dir = repo_root / SOURCE_DIR
    print(f"Scanning {source_dir.relative_to(repo_root)}...", file=sys.stderr)
    checker = TranslationChecker(source_dir)
    checker.scan_directory()
    
    # Filter by directory if specified
    results = checker.results
    if args.directory:
        results = {
            path: result for path, result in results.items()
            if path.startswith(args.directory)
        }
    
    # Filter by status
    if args.status == 'completed':
        filtered = {p: r for p, r in results.items() if r['status'] == 'completed'}
    elif args.status == 'partial':
        filtered = {p: r for p, r in results.items() if r['status'] == 'partial'}
    elif args.status == 'untranslated':
        filtered = {p: r for p, r in results.items() if r['status'] == 'untranslated'}
    else:
        filtered = results
    
    # Sort by path
    sorted_files = sorted(filtered.items(), key=lambda x: x[0])
    
    # Display results
    if args.count:
        print(len(sorted_files))
    else:
        for path, result in sorted_files:
            if args.show_issues and result['status'] == 'partial':
                issue_count = len(result['issues'])
                print(f"{path} ({issue_count} issues)")
            else:
                print(path)
    
    # Print summary to stderr if not in count mode
    if not args.count:
        print(f"\nTotal files: {len(sorted_files)}", file=sys.stderr)


if __name__ == "__main__":
    main()
