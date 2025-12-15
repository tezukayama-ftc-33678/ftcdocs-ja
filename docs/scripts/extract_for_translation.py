#!/usr/bin/env python3
"""
Extract untranslated entries from .po files for batch AI translation.

This script extracts untranslated entries in a format suitable for
AI translation tools (ChatGPT, Claude, DeepL, etc.).

Usage:
    python extract_for_translation.py input.po output.txt
    # Then paste output.txt content to AI tool
    # Save AI response and use import_translations.py
"""

import sys
import polib
from pathlib import Path


def extract_untranslated(po_file_path: str, output_file: str, max_entries: int = 50):
    """
    Extract untranslated entries from a .po file.
    
    Args:
        po_file_path: Path to the .po file
        output_file: Path to output file for AI translation
        max_entries: Maximum number of entries to extract (default: 50)
    """
    po = polib.pofile(po_file_path)
    
    # Find untranslated entries
    untranslated = [entry for entry in po if entry.msgid and not entry.msgstr and not entry.obsolete]
    
    if not untranslated:
        print(f"No untranslated entries found in {po_file_path}")
        return
    
    # Limit to max_entries
    entries_to_process = untranslated[:max_entries]
    
    print(f"Found {len(untranslated)} untranslated entries")
    print(f"Extracting {len(entries_to_process)} entries to {output_file}")
    
    # Write extraction file with AI prompt
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("=" * 80 + "\n")
        f.write("FTC日本語翻訳タスク\n")
        f.write("=" * 80 + "\n\n")
        
        f.write("以下の.poファイルエントリを日本語に翻訳してください。\n\n")
        
        f.write("【翻訳ルール】\n")
        f.write("1. 文体: 「です・ます」調で統一\n")
        f.write("2. 句読点: 全角の「、」と「。」を使用\n")
        f.write("3. 長音: カタカナ語の長音（ー）は省略しない\n")
        f.write("4. 技術用語: 以下は **太字の英語** で残す\n")
        f.write("   - OpMode, LinearOpMode, TeleOp, Autonomous\n")
        f.write("   - Control Hub, Driver Station, Robot Controller\n")
        f.write("   - HuskyLens, AprilTag, VisionPortal, Blocks\n")
        f.write("   - その他のAPI名、クラス名、製品名\n")
        f.write("5. コード: ``コード``は翻訳しない\n")
        f.write("6. RSTマークアップ: :doc:`...`、:ref:`...`などは保持\n")
        f.write("7. 固有名詞: FIRST、Gracious Professionalismは翻訳しない\n\n")
        
        f.write("【出力形式】\n")
        f.write("各エントリに対して、以下の形式で出力してください：\n")
        f.write('msgid "English text"\n')
        f.write('msgstr "日本語訳"\n\n')
        
        f.write("=" * 80 + "\n")
        f.write(f"翻訳対象: {len(entries_to_process)}エントリ\n")
        f.write(f"ソース: {Path(po_file_path).name}\n")
        f.write("=" * 80 + "\n\n")
        
        # Write entries
        for i, entry in enumerate(entries_to_process, 1):
            f.write(f"# Entry {i}/{len(entries_to_process)}\n")
            if entry.occurrences:
                f.write(f"# Source: {entry.occurrences[0][0]}:{entry.occurrences[0][1]}\n")
            f.write(f'msgid "{entry.msgid}"\n')
            f.write(f'msgstr ""\n\n')
        
        f.write("=" * 80 + "\n")
        f.write("翻訳完了後、このファイルを保存して\n")
        f.write("import_translations.pyで.poファイルに反映してください。\n")
        f.write("=" * 80 + "\n")
    
    print(f"\n✓ 抽出完了: {output_file}")
    print(f"  残り: {len(untranslated) - len(entries_to_process)}エントリ")
    print(f"\n次のステップ:")
    print(f"  1. {output_file}の内容をAIツールに貼り付け")
    print(f"  2. AI翻訳結果を保存")
    print(f"  3. python import_translations.py {output_file} {po_file_path}")


def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_for_translation.py INPUT.po OUTPUT.txt [MAX_ENTRIES]")
        print("\nExample:")
        print("  python extract_for_translation.py index.po index_to_translate.txt 50")
        sys.exit(1)
    
    po_file = sys.argv[1]
    output_file = sys.argv[2]
    max_entries = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    
    if not Path(po_file).exists():
        print(f"Error: File not found: {po_file}")
        sys.exit(1)
    
    extract_untranslated(po_file, output_file, max_entries)


if __name__ == '__main__':
    main()
