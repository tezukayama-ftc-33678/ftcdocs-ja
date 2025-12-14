#!/usr/bin/env python3
"""
Batch extract untranslated entries from multiple .po files.

This script processes multiple .po files and creates organized
extraction files for batch AI translation.

Usage:
    python batch_extract.py --top 10 --entries 30
    # Extracts top 10 files with most untranslated entries, 30 entries each
"""

import argparse
import polib
import sys
from pathlib import Path
from typing import List, Tuple


def get_translation_stats(po_file: Path) -> Tuple[int, int]:
    """
    Get translation statistics for a .po file.
    
    Returns:
        (untranslated_count, total_count)
    """
    try:
        po = polib.pofile(str(po_file))
        untranslated = len([e for e in po if e.msgid and not e.msgstr and not e.obsolete])
        total = len([e for e in po if e.msgid and not e.obsolete])
        return untranslated, total
    except (IOError, OSError) as e:
        print(f"Warning: Failed to read {po_file}: {e}", file=sys.stderr)
        return 0, 0
    except Exception as e:
        print(f"Warning: Failed to parse {po_file}: {e}", file=sys.stderr)
        return 0, 0


def find_files_needing_translation(locale_dir: Path, top_n: int = None) -> List[Tuple[Path, int, int]]:
    """
    Find .po files that need translation, sorted by number of untranslated entries.
    
    Returns:
        List of (filepath, untranslated_count, total_count) tuples
    """
    po_files = list(locale_dir.rglob('*.po'))
    
    files_with_stats = []
    for po_file in po_files:
        untrans, total = get_translation_stats(po_file)
        if untrans > 0:
            files_with_stats.append((po_file, untrans, total))
    
    # Sort by untranslated count (descending)
    files_with_stats.sort(key=lambda x: x[1], reverse=True)
    
    if top_n:
        files_with_stats = files_with_stats[:top_n]
    
    return files_with_stats


def extract_for_file(po_file: Path, output_dir: Path, max_entries: int, file_num: int, total_files: int):
    """
    Extract untranslated entries from a single file.
    
    Note: This function imports extract_for_translation locally to avoid circular imports
    and to ensure it's only loaded when needed.
    """
    # Import here to avoid issues when the script is run from different directories
    sys.path.insert(0, str(Path(__file__).parent))
    from extract_for_translation import extract_untranslated
    
    output_file = output_dir / f"{file_num:03d}_{po_file.stem}_to_translate.txt"
    
    print(f"\n[{file_num}/{total_files}] {po_file.name}")
    extract_untranslated(str(po_file), str(output_file), max_entries)


def main():
    parser = argparse.ArgumentParser(
        description='Batch extract untranslated entries from .po files',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Extract from top 10 files with most untranslated entries
  python batch_extract.py --top 10 --entries 30
  
  # Extract from all files with untranslated entries
  python batch_extract.py --entries 50
  
  # Extract from specific directory
  python batch_extract.py --dir docs/locale/ja/LC_MESSAGES/programming_resources --entries 40
        """
    )
    
    parser.add_argument('--top', type=int,
                       help='Extract from top N files with most untranslated entries')
    parser.add_argument('--entries', type=int, default=30,
                       help='Maximum entries per file (default: 30)')
    parser.add_argument('--dir', type=str,
                       help='Directory containing .po files (default: docs/locale/ja/LC_MESSAGES)')
    parser.add_argument('--output-dir', type=str, default='translation_batches',
                       help='Output directory for extraction files (default: translation_batches)')
    
    args = parser.parse_args()
    
    # Setup paths
    repo_root = Path(__file__).parent.parent.parent
    
    if args.dir:
        locale_dir = Path(args.dir)
    else:
        locale_dir = repo_root / 'docs' / 'locale' / 'ja' / 'LC_MESSAGES'
    
    output_dir = repo_root / args.output_dir
    output_dir.mkdir(exist_ok=True)
    
    # Find files needing translation
    print(f"スキャン中: {locale_dir}")
    files_to_process = find_files_needing_translation(locale_dir, args.top)
    
    if not files_to_process:
        print("未翻訳エントリを含むファイルが見つかりませんでした")
        return
    
    print(f"\n見つかりました: {len(files_to_process)}ファイル")
    print(f"出力先: {output_dir}\n")
    
    # Display summary
    print("=" * 80)
    print(f"{'ファイル':<60} {'未翻訳':>8} {'合計':>8}")
    print("=" * 80)
    
    total_untrans = 0
    total_entries = 0
    
    for po_file, untrans, total in files_to_process[:20]:  # Show first 20
        rel_path = po_file.relative_to(locale_dir)
        print(f"{str(rel_path):<60} {untrans:>8} {total:>8}")
        total_untrans += untrans
        total_entries += total
    
    if len(files_to_process) > 20:
        # Sum remaining
        for po_file, untrans, total in files_to_process[20:]:
            total_untrans += untrans
            total_entries += total
        print(f"... and {len(files_to_process) - 20} more files")
    
    print("=" * 80)
    print(f"{'合計':<60} {total_untrans:>8} {total_entries:>8}")
    print("=" * 80)
    
    # Extract entries
    print(f"\n抽出開始: 各ファイルから最大{args.entries}エントリ")
    
    for i, (po_file, untrans, total) in enumerate(files_to_process, 1):
        extract_for_file(po_file, output_dir, args.entries, i, len(files_to_process))
    
    print("\n" + "=" * 80)
    print("✓ バッチ抽出完了")
    print("=" * 80)
    print(f"\n出力ディレクトリ: {output_dir}")
    print(f"抽出ファイル数: {len(files_to_process)}")
    print(f"\n次のステップ:")
    print(f"  1. {output_dir}/の各ファイルをAIツールで翻訳")
    print(f"  2. 翻訳結果を同じファイル名で保存（例: 001_index_translated.txt）")
    print(f"  3. 各ファイルをimport_translations.pyで個別にインポート:")
    print(f"     python import_translations.py {output_dir}/001_..._translated.txt <対応する.po>")


if __name__ == '__main__':
    main()
