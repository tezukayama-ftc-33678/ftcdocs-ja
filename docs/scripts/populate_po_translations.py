#!/usr/bin/env python3
"""
Script to populate .po msgstr fields using TRANSLATION_MAPPING.md as reference.

This script reads the TRANSLATION_MAPPING.md file which contains extracted Japanese
translations from RST files, and uses them to populate the msgstr fields in .po files.
"""

import re
import os
from pathlib import Path
from typing import Dict, List, Tuple
import polib


def parse_translation_mapping(mapping_file: str) -> Dict[str, List[Tuple[int, str]]]:
    """
    Parse TRANSLATION_MAPPING.md and extract translations organized by file.
    
    Returns:
        Dict mapping file paths to list of (block_line, japanese_text) tuples
    """
    with open(mapping_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    translations = {}
    current_file = None
    
    # Split by file sections (## filename)
    file_sections = re.split(r'\n## (.+?\.rst)\n', content)
    
    for i in range(1, len(file_sections), 2):
        if i + 1 >= len(file_sections):
            break
            
        file_path = file_sections[i].strip()
        section_content = file_sections[i + 1]
        
        # Extract all blocks from this section
        blocks = []
        # Match ### Block N (line X) followed by ``` content ```
        block_pattern = r'### Block \d+ \(line (\d+)\)\s*\n\s*```\s*\n(.*?)\n```'
        
        for match in re.finditer(block_pattern, section_content, re.DOTALL):
            line_num = int(match.group(1))
            japanese_text = match.group(2).strip()
            blocks.append((line_num, japanese_text))
        
        if blocks:
            translations[file_path] = blocks
    
    return translations


def normalize_text(text: str) -> str:
    """
    Normalize text for comparison by removing extra whitespace and newlines.
    """
    # Replace multiple spaces/newlines with single space
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def find_matching_translation(msgid: str, translations: List[Tuple[int, str]], 
                              source_line: int = None) -> str:
    """
    Find the best matching Japanese translation for an English msgid.
    
    Args:
        msgid: The English text to translate
        translations: List of (line_num, japanese_text) tuples
        source_line: The line number in the source RST file (if available)
    
    Returns:
        The matching Japanese translation, or empty string if not found
    """
    if not translations:
        return ""
    
    # Normalize the msgid for comparison
    normalized_msgid = normalize_text(msgid)
    
    # If we have source line info, try to find translations near that line
    if source_line:
        # Look for translations within ±5 lines
        nearby = [t for line, t in translations if abs(line - source_line) <= 5]
        if nearby:
            # Return the first nearby translation
            return nearby[0]
    
    # If no source line or no nearby match, try exact text matching
    # This is tricky since we're comparing English to Japanese
    # For now, return the first translation if available
    # A more sophisticated approach would be needed for better matching
    
    return ""


def populate_po_file(po_file_path: str, translations: Dict[str, List[Tuple[int, str]]], 
                     dry_run: bool = False) -> Tuple[int, int]:
    """
    Populate msgstr fields in a .po file using translations from TRANSLATION_MAPPING.md
    
    Returns:
        Tuple of (total_entries, populated_entries)
    """
    try:
        po = polib.pofile(po_file_path)
    except Exception as e:
        print(f"Error loading {po_file_path}: {e}")
        return 0, 0
    
    # Extract the source RST file path from the .po file
    # .po files have comments like: #: ../../source/path/to/file.rst:line
    # We need to map this back to the format in TRANSLATION_MAPPING.md
    
    total_entries = 0
    populated_entries = 0
    
    # Build a mapping from source files to their translations indexed by line
    file_translation_map = {}
    
    for entry in po:
        if entry.msgid and not entry.msgstr:
            total_entries += 1
            
            # Get the source file and line from the entry
            if entry.occurrences:
                source_file, line_num = entry.occurrences[0]
                # Convert from ../../source/path/to/file.rst to path/to/file.rst
                source_file = source_file.replace('../../source/', '')
                
                # Look up translations for this file
                if source_file in translations:
                    # Build lookup map if we haven't already for this file
                    if source_file not in file_translation_map:
                        file_translation_map[source_file] = {}
                        for trans_line, trans_text in translations[source_file]:
                            file_translation_map[source_file][trans_line] = trans_text
                    
                    try:
                        source_line = int(line_num)
                    except (ValueError, TypeError):
                        continue
                    
                    # Try exact match first
                    if source_line in file_translation_map[source_file]:
                        if not dry_run:
                            entry.msgstr = file_translation_map[source_file][source_line]
                        populated_entries += 1
                    else:
                        # The .po file line numbers for titles point to the underline,
                        # but TRANSLATION_MAPPING points to the title text (one line above)
                        # So try looking one line back first for titles
                        if source_line - 1 in file_translation_map[source_file]:
                            if not dry_run:
                                entry.msgstr = file_translation_map[source_file][source_line - 1]
                            populated_entries += 1
                        else:
                            # Try to find nearby translation (within ±5 lines)
                            found = False
                            for offset in range(2, 6):
                                # Try below first
                                if source_line - offset in file_translation_map[source_file]:
                                    if not dry_run:
                                        entry.msgstr = file_translation_map[source_file][source_line - offset]
                                    populated_entries += 1
                                    found = True
                                    break
                                # Then try above
                                if source_line + offset in file_translation_map[source_file]:
                                    if not dry_run:
                                        entry.msgstr = file_translation_map[source_file][source_line + offset]
                                    populated_entries += 1
                                    found = True
                                    break
    
    if not dry_run and populated_entries > 0:
        po.save(po_file_path)
    
    return total_entries, populated_entries


def main():
    """Main function to populate all .po files."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Populate .po msgstr fields using TRANSLATION_MAPPING.md'
    )
    parser.add_argument('--dry-run', action='store_true',
                       help='Run without actually modifying files')
    parser.add_argument('--file', type=str,
                       help='Process only a specific .po file')
    parser.add_argument('--verbose', action='store_true',
                       help='Show detailed progress')
    
    args = parser.parse_args()
    
    # Get paths
    repo_root = Path(__file__).parent.parent.parent
    mapping_file = repo_root / 'TRANSLATION_MAPPING.md'
    locale_dir = repo_root / 'docs' / 'locale' / 'ja' / 'LC_MESSAGES'
    
    print(f"Loading translations from {mapping_file}...")
    translations = parse_translation_mapping(str(mapping_file))
    print(f"Loaded translations for {len(translations)} files")
    
    # Get list of .po files to process
    if args.file:
        po_files = [Path(args.file).resolve()]
    else:
        po_files = list(locale_dir.rglob('*.po'))
    
    print(f"\nProcessing {len(po_files)} .po files...")
    
    total_all = 0
    populated_all = 0
    processed_files = 0
    
    for po_file in sorted(po_files):
        if args.verbose:
            print(f"\nProcessing: {po_file.relative_to(repo_root)}")
        
        total, populated = populate_po_file(str(po_file), translations, args.dry_run)
        total_all += total
        populated_all += populated
        
        if total > 0:
            processed_files += 1
            if args.verbose or populated > 0:
                print(f"  {po_file.name}: {populated}/{total} entries populated")
    
    print(f"\n{'DRY RUN - ' if args.dry_run else ''}Summary:")
    print(f"  Files processed: {processed_files}/{len(po_files)}")
    print(f"  Total entries: {total_all}")
    print(f"  Populated entries: {populated_all}")
    if total_all > 0:
        print(f"  Coverage: {populated_all/total_all*100:.1f}%")


if __name__ == '__main__':
    main()
