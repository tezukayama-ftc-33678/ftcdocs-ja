#!/usr/bin/env python3
"""
Batch translation helper for PO files.
Provides templates and utilities for efficient translation workflows.
"""

import sys
import re
from pathlib import Path

def translate_file_interactive(po_file_path):
    """
    Interactive mode: Shows untranslated entries and allows batch input.
    """
    with open(po_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all untranslated msgid/msgstr pairs
    pattern = r'msgid\s+"([^"]+)"\nmsgstr\s+""'
    matches = list(re.finditer(pattern, content))
    
    if not matches:
        print("✅ File is fully translated!")
        return
    
    print(f"\n📝 Found {len(matches)} untranslated entries in {Path(po_file_path).name}")
    print("\nShowing first 10 entries to translate:\n")
    
    translations = {}
    for i, match in enumerate(matches[:10], 1):
        english = match.group(1)
        print(f"{i}. EN: {english}")
        japanese = input(f"   JA: ")
        if japanese:
            translations[match.group(0)] = f'msgid "{english}"\nmsgstr "{japanese}"'
        print()
    
    # Apply translations
    if translations:
        for old, new in translations.items():
            content = content.replace(old, new)
        
        with open(po_file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Applied {len(translations)} translations to {po_file_path}")
    else:
        print("❌ No translations applied")


def create_translation_template(po_file_path):
    """
    Create a Python script template for batch translation of a PO file.
    """
    with open(po_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find untranslated entries
    pattern = r'msgid\s+"([^"]+)"\nmsgstr\s+""'
    matches = list(re.finditer(pattern, content))
    
    if not matches:
        print("✅ File is fully translated!")
        return
    
    # Generate template
    template = f'''#!/usr/bin/env python3
"""
Auto-generated translation template for {Path(po_file_path).name}
Fill in the Japanese translations in the translations dict below.
"""

import re

po_file = '{po_file_path}'

with open(po_file, 'r', encoding='utf-8') as f:
    content = f.read()

# TODO: Fill in Japanese translations
translations = {{
'''
    
    for match in matches[:20]:  # First 20 entries
        english = match.group(1)
        template += f'    \'msgid "{english}"\\nmsgstr ""\': \n'
        template += f'        \'msgid "{english}"\\nmsgstr "TODO: 翻訳"\',\n\n'
    
    if len(matches) > 20:
        template += f'    # ... and {len(matches) - 20} more entries\n'
    
    template += '''}}

# Apply translations
count = 0
for old, new in translations.items():
    if 'TODO' not in new and old in content:
        content = content.replace(old, new)
        count += 1

with open(po_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Applied {{count}} translations to {Path(po_file_path).name}")
'''
    
    # Save template
    output_file = f"translate_{Path(po_file_path).stem}.py"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"📝 Created translation template: {output_file}")
    print(f"   Edit the file to add Japanese translations, then run it to apply.")


def show_stats(po_file_path):
    """
    Show translation statistics for a PO file.
    """
    with open(po_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count all msgid/msgstr pairs (excluding header)
    all_pattern = r'msgid\s+"([^"]+)"\nmsgstr\s+"([^"]*)"'
    all_matches = re.findall(all_pattern, content)
    all_matches = [(m, s) for m, s in all_matches if m]  # Exclude header
    
    total = len(all_matches)
    translated = len([m for m, s in all_matches if s])
    untranslated = total - translated
    
    percent = (translated / total * 100) if total > 0 else 0
    
    print(f"\n📊 Translation Stats for {Path(po_file_path).name}")
    print(f"{'='*60}")
    print(f"Total entries:       {total}")
    print(f"Translated:          {translated} ({percent:.1f}%)")
    print(f"Untranslated:        {untranslated} ({100-percent:.1f}%)")
    print(f"{'='*60}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python batch_translate.py <po_file> stats    # Show translation statistics")
        print("  python batch_translate.py <po_file> template # Create translation template")
        print("  python batch_translate.py <po_file> interactive # Interactive translation")
        print("\nExample:")
        print("  python batch_translate.py locales/ja/LC_MESSAGES/apriltag/.../file.po stats")
        sys.exit(1)
    
    po_file = sys.argv[1]
    mode = sys.argv[2] if len(sys.argv) > 2 else 'stats'
    
    if not Path(po_file).exists():
        print(f"❌ Error: File not found: {po_file}")
        sys.exit(1)
    
    if mode == 'stats':
        show_stats(po_file)
    elif mode == 'template':
        create_translation_template(po_file)
    elif mode == 'interactive':
        translate_file_interactive(po_file)
    else:
        print(f"❌ Unknown mode: {mode}")
        print("Valid modes: stats, template, interactive")
        sys.exit(1)


if __name__ == "__main__":
    main()
