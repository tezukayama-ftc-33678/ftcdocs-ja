#!/usr/bin/env python3
"""
Sphinx Build Warning Analyzer
Analyzes and categorizes Sphinx build warnings.
"""

import sys
import re
import subprocess
from pathlib import Path
from collections import defaultdict

def run_sphinx_build(docs_dir: Path) -> str:
    """Run Sphinx build and capture output."""
    try:
        result = subprocess.run(
            ['make', 'clean'],
            cwd=docs_dir,
            capture_output=True,
            text=True
        )
        
        result = subprocess.run(
            ['make', 'html'],
            cwd=docs_dir,
            capture_output=True,
            text=True
        )
        
        return result.stdout + result.stderr
        
    except Exception as e:
        print(f"Error running Sphinx build: {e}", file=sys.stderr)
        sys.exit(1)

def categorize_warnings(output: str) -> dict:
    """Categorize warnings by type."""
    categories = defaultdict(list)
    
    warning_pattern = r'(.+?\.rst):(\d+): (WARNING|ERROR): (.+)'
    
    for line in output.split('\n'):
        match = re.search(warning_pattern, line)
        if match:
            filepath, lineno, severity, message = match.groups()
            
            # Categorize by message type
            if 'inline' in message.lower():
                category = 'inline_markup'
            elif 'underline' in message.lower():
                category = 'title_underline'
            elif 'undefined label' in message.lower():
                category = 'undefined_label'
            elif 'duplicate label' in message.lower():
                category = 'duplicate_label'
            elif 'not included in any toctree' in message.lower():
                category = 'missing_toctree'
            elif 'grid-item' in message.lower():
                category = 'grid_design'
            elif 'explicit markup' in message.lower():
                category = 'explicit_markup'
            elif 'block quote' in message.lower():
                category = 'block_quote'
            elif 'bullet list' in message.lower():
                category = 'bullet_list'
            elif 'image file not readable' in message.lower():
                category = 'missing_image'
            elif 'hyperlink' in message.lower():
                category = 'hyperlink'
            else:
                category = 'other'
            
            categories[category].append({
                'file': filepath,
                'line': lineno,
                'severity': severity,
                'message': message
            })
    
    return categories

def print_report(categories: dict, verbose: bool = False):
    """Print categorized warning report."""
    total_warnings = sum(len(warnings) for warnings in categories.values())
    
    print("\n" + "=" * 80)
    print("SPHINX BUILD WARNING ANALYSIS")
    print("=" * 80)
    
    # Priority categories
    critical = ['inline_markup', 'title_underline', 'explicit_markup', 
                'block_quote', 'bullet_list', 'duplicate_label']
    
    important = ['missing_image', 'hyperlink']
    
    low_priority = ['undefined_label', 'missing_toctree', 'grid_design', 'other']
    
    def print_category(category: str, warnings: list, priority: str):
        """Print warnings for a category."""
        if not warnings:
            return
        
        severity_counts = defaultdict(int)
        for w in warnings:
            severity_counts[w['severity']] += 1
        
        severity_str = ', '.join(f"{count} {sev}" for sev, count in sorted(severity_counts.items()))
        
        print(f"\n{priority} {category.replace('_', ' ').title()}: {len(warnings)} ({severity_str})")
        print("-" * 80)
        
        if verbose:
            # Show first 5 examples
            for warning in warnings[:5]:
                print(f"  {warning['file']}:{warning['line']}")
                print(f"    {warning['message']}")
            
            if len(warnings) > 5:
                print(f"  ... and {len(warnings) - 5} more")
        else:
            # Show unique messages count
            unique_messages = {}
            for w in warnings:
                msg_key = re.sub(r':[^:]+$', '', w['message'])  # Remove file-specific part
                unique_messages[msg_key] = unique_messages.get(msg_key, 0) + 1
            
            for msg, count in sorted(unique_messages.items(), key=lambda x: -x[1])[:3]:
                print(f"  {count}x: {msg[:70]}...")
    
    # Print critical issues
    print("\n🔴 CRITICAL ISSUES (Must Fix)")
    for cat in critical:
        if cat in categories:
            print_category(cat, categories[cat], "🔴")
    
    # Print important issues
    print("\n🟡 IMPORTANT ISSUES (Should Fix)")
    for cat in important:
        if cat in categories:
            print_category(cat, categories[cat], "🟡")
    
    # Print low priority issues
    print("\n🟢 LOW PRIORITY ISSUES (Optional)")
    for cat in low_priority:
        if cat in categories:
            print_category(cat, categories[cat], "🟢")
    
    print("\n" + "=" * 80)
    print(f"TOTAL WARNINGS: {total_warnings}")
    print("=" * 80)
    
    # Summary by priority
    critical_count = sum(len(categories.get(cat, [])) for cat in critical)
    important_count = sum(len(categories.get(cat, [])) for cat in important)
    low_count = sum(len(categories.get(cat, [])) for cat in low_priority)
    
    print(f"\n🔴 Critical: {critical_count}")
    print(f"🟡 Important: {important_count}")
    print(f"🟢 Low Priority: {low_count}")
    
    if critical_count > 0:
        print("\n❌ Build has critical issues that should be fixed!")
        return 1
    elif important_count > 0:
        print("\n⚠️  Build has important issues to consider.")
        return 0
    else:
        print("\n✅ Build quality is good!")
        return 0

def main():
    """Main function."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Analyze Sphinx build warnings'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed warning information'
    )
    parser.add_argument(
        '--docs-dir',
        type=Path,
        default=Path(__file__).parent.parent,
        help='Path to docs directory (default: parent of scripts dir)'
    )
    
    args = parser.parse_args()
    
    print("Running Sphinx build...")
    output = run_sphinx_build(args.docs_dir)
    
    print("Analyzing warnings...")
    categories = categorize_warnings(output)
    
    exit_code = print_report(categories, args.verbose)
    sys.exit(exit_code)

if __name__ == '__main__':
    main()
