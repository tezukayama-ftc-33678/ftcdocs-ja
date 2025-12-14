#!/usr/bin/env python3
"""
Import translated entries back into .po files.

This script reads AI-translated entries from a text file and
updates the corresponding .po file.

Usage:
    python import_translations.py translated.txt target.po
"""

import sys
import re
import polib
from pathlib import Path


def parse_translated_file(translated_file: str):
    """
    Parse a file containing translated msgid/msgstr pairs.
    
    Handles simple single-line msgid/msgstr pairs.
    For complex multiline strings, use polib directly.
    
    Returns:
        Dictionary mapping msgid to msgstr
    """
    with open(translated_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    translations = {}
    
    # Simple pattern for single-line msgid/msgstr pairs
    # This handles the most common case from AI translation output
    # For multiline or complex .po files, use polib instead
    pattern = r'msgid\s+"([^"\\]*(?:\\.[^"\\]*)*)"\s*\nmsgstr\s+"([^"\\]*(?:\\.[^"\\]*)*)"'
    
    for match in re.finditer(pattern, content, re.MULTILINE):
        msgid = match.group(1)
        msgstr = match.group(2)
        
        if msgstr:  # Only include if translation exists
            translations[msgid] = msgstr
    
    return translations


def import_translations(po_file_path: str, translations: dict):
    """
    Import translations into a .po file.
    
    Args:
        po_file_path: Path to the .po file to update
        translations: Dictionary of msgid -> msgstr mappings
    """
    po = polib.pofile(po_file_path)
    
    updated_count = 0
    not_found_count = 0
    
    for entry in po:
        if entry.msgid in translations:
            if not entry.msgstr:  # Only update if currently empty
                entry.msgstr = translations[entry.msgid]
                updated_count += 1
    
    # Check for translations that couldn't be matched
    matched_ids = {entry.msgid for entry in po if entry.msgid in translations}
    unmatched = set(translations.keys()) - matched_ids
    not_found_count = len(unmatched)
    
    if updated_count > 0:
        po.save(po_file_path)
        print(f"✓ 更新完了: {po_file_path}")
        print(f"  更新: {updated_count}エントリ")
        if not_found_count > 0:
            print(f"  警告: {not_found_count}エントリがファイルに見つかりませんでした")
            if not_found_count <= 10:
                print("\n見つからなかったエントリ:")
                for msgid in list(unmatched)[:10]:
                    print(f"  - {msgid[:60]}...")
    else:
        print("更新するエントリがありません（すべて既に翻訳済みか、一致するmsgidが見つかりませんでした）")
    
    return updated_count


def main():
    if len(sys.argv) < 3:
        print("Usage: python import_translations.py TRANSLATED.txt TARGET.po")
        print("\nExample:")
        print("  python import_translations.py index_translated.txt index.po")
        sys.exit(1)
    
    translated_file = sys.argv[1]
    po_file = sys.argv[2]
    
    if not Path(translated_file).exists():
        print(f"Error: File not found: {translated_file}")
        sys.exit(1)
    
    if not Path(po_file).exists():
        print(f"Error: File not found: {po_file}")
        sys.exit(1)
    
    print(f"翻訳ファイルを読み込み中: {translated_file}")
    translations = parse_translated_file(translated_file)
    print(f"  {len(translations)}個の翻訳を読み込みました\n")
    
    if not translations:
        print("警告: 翻訳が見つかりませんでした")
        sys.exit(1)
    
    print(f".poファイルに反映中: {po_file}")
    updated = import_translations(po_file, translations)
    
    if updated > 0:
        print(f"\n次のステップ:")
        print(f"  1. 翻訳を確認: msgfmt -c {po_file}")
        print(f"  2. ビルドしてテスト: cd docs && make ja-build")


if __name__ == '__main__':
    main()
