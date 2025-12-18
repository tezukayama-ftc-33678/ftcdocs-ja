#!/usr/bin/env python3
"""
Inline Markup 修正スクリプト

POファイル内のInline markup（**, *, `）の不一致を検出して修正します。
"""

import polib
import argparse
from pathlib import Path
from collections import defaultdict


def fix_inline_markup_in_text(text, markup_char, description):
    """
    テキスト内のインラインマークアップを修正
    
    Args:
        text: 修正対象のテキスト
        markup_char: マークアップ文字 ('**', '*', '`')
        description: マークアップの説明（ログ用）
    
    Returns:
        修正されたテキスト、変更があったかどうか
    """
    count = text.count(markup_char)
    
    if count % 2 == 0:
        # すでに偶数なので修正不要
        return text, False
    
    # 奇数の場合、最後の出現箇所を削除
    # （より安全な方法は、最後のマークアップを削除すること）
    last_index = text.rfind(markup_char)
    if last_index != -1:
        # 最後のマークアップを削除
        text = text[:last_index] + text[last_index + len(markup_char):]
        return text, True
    
    return text, False


def fix_po_file(po_file_path, dry_run=False):
    """
    POファイル内のインラインマークアップを修正
    
    Returns:
        修正した項目数
    """
    try:
        po = polib.pofile(str(po_file_path))
    except Exception as e:
        print(f"エラー: {po_file_path} の読み込み失敗: {e}")
        return 0
    
    fixes_made = 0
    
    for entry in po:
        if not entry.msgstr:
            continue
        
        original_msgstr = entry.msgstr
        modified_msgstr = entry.msgstr
        changes = []
        
        # バッククォート（`）を修正
        backtick_count = modified_msgstr.count('`')
        if backtick_count % 2 != 0:
            modified_msgstr, changed = fix_inline_markup_in_text(modified_msgstr, '`', 'backtick')
            if changed:
                changes.append('backtick')
        
        # 強調（**）を修正
        bold_count = modified_msgstr.count('**')
        if bold_count % 2 != 0:
            modified_msgstr, changed = fix_inline_markup_in_text(modified_msgstr, '**', 'bold')
            if changed:
                changes.append('bold')
        
        # イタリック（*）を修正（ただし**は除外）
        text_no_bold = modified_msgstr.replace('**', '  ')
        star_count = text_no_bold.count('*')
        if star_count % 2 != 0:
            modified_msgstr, changed = fix_inline_markup_in_text(modified_msgstr, '*', 'italic')
            if changed:
                changes.append('italic')
        
        if changes:
            fixes_made += 1
            if not dry_run:
                entry.msgstr = modified_msgstr
            
            print(f"  Line {entry.linenum}: 修正 ({', '.join(changes)})")
            print(f"    元: {original_msgstr[:100]}...")
            print(f"    後: {modified_msgstr[:100]}...")
    
    if fixes_made > 0 and not dry_run:
        try:
            po.save(str(po_file_path))
        except Exception as e:
            print(f"エラー: {po_file_path} の保存失敗: {e}")
            return 0
    
    return fixes_made


def main():
    parser = argparse.ArgumentParser(
        description='POファイル内のインラインマークアップを修正'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='実際の変更は行わず、検出のみを実行'
    )
    parser.add_argument(
        '--locales-dir',
        type=Path,
        default=Path('locales/ja/LC_MESSAGES'),
        help='localesディレクトリのパス'
    )
    
    args = parser.parse_args()
    
    locales_dir = args.locales_dir
    
    if not locales_dir.exists():
        print(f"エラー: {locales_dir} が見つかりません")
        return 1
    
    print("=" * 70)
    print("Inline Markup 修正スクリプト")
    print("=" * 70)
    
    if args.dry_run:
        print("\n*** DRY-RUN モード: 実際の変更は行いません ***")
    
    # POファイルを検索
    po_files = list(locales_dir.rglob("*.po"))
    print(f"\n{len(po_files)} 個のPOファイルをスキャン中...")
    
    total_fixes = 0
    files_fixed = 0
    
    for po_file in po_files:
        fixes = fix_po_file(po_file, dry_run=args.dry_run)
        if fixes > 0:
            files_fixed += 1
            total_fixes += fixes
            short_path = str(po_file).replace('locales/ja/LC_MESSAGES/', '')
            print(f"\n{short_path}: {fixes} 項目を修正")
    
    print("\n" + "=" * 70)
    print("修正統計")
    print("=" * 70)
    print(f"修正したファイル数:   {files_fixed}")
    print(f"修正した項目数:       {total_fixes}")
    
    return 0


if __name__ == '__main__':
    exit(main())
