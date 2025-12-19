#!/usr/bin/env python3
r"""
Inline Markup Spacing Fix Script for .po Files

This script adds spaces around backticks (`) and single asterisks (*) in msgstr entries
of .po files to fix Sphinx inline literal/emphasis warnings when Japanese text is
adjacent to markup characters.

処理仕様:
- 対象ファイル: 指定したディレクトリ内のすべての .po ファイル
- 対象行: msgstr "..." の行のみ（msgid は絶対に書き換えない）
- 置換ルール:
  * バッククォート: ` の前後に半角スペースを挿入
  * シングルアスタリスク: * の前後に半角スペースを挿入
- 除外条件:
  * アスタリスクが2つ連続 ** は太字なのでそのまま（スペースを入れない）
  * エスケープされた \* や \` も対象外
- 重複防止: すでにスペースがある場合は二重にスペースを入れない
"""

import os
import re
import sys
from pathlib import Path
from collections import defaultdict


def count_patterns_in_msgstr(content):
    """
    msgstr内のパターンを数える（検証用）
    
    Returns:
        dict: パターン別のカウント
    """
    counts = defaultdict(int)
    lines = content.split('\n')
    in_msgstr = False
    
    for line in lines:
        # msgstrの開始を検出
        if line.startswith('msgstr'):
            in_msgstr = True
        # msgidの開始でmsgstrを終了
        elif line.startswith('msgid'):
            in_msgstr = False
        # 空行でmsgstrを終了
        elif in_msgstr and line.strip() == '':
            in_msgstr = False
        
        # msgstr内の行のみをカウント
        if in_msgstr:
            # 日本語文字に隣接するバッククォート（スペースなし）
            # [ひらがな、カタカナ、漢字]`  または  `[ひらがな、カタカナ、漢字]
            counts['backtick_no_space_before'] += len(re.findall(r'[ぁ-んァ-ヶー一-龠々]`', line))
            counts['backtick_no_space_after'] += len(re.findall(r'`[ぁ-んァ-ヶー一-龠々]', line))
            
            # 日本語文字に隣接するシングルアスタリスク（**は除外）
            # [ひらがな、カタカナ、漢字]*（直後が*でない） または *[ひらがな、カタカナ、漢字]（直前が*でない）
            counts['asterisk_no_space_before'] += len(re.findall(r'[ぁ-んァ-ヶー一-龠々]\*(?!\*)', line))
            counts['asterisk_no_space_after'] += len(re.findall(r'(?<!\*)\*[ぁ-んァ-ヶー一-龠々]', line))
    
    return counts


def fix_line_spacing(line):
    """
    1行内のバッククォートとアスタリスクの前後にスペースを追加
    
    処理順序:
    1. エスケープされた文字を一時的にプレースホルダーに置換
    2. バッククォートの前後にスペースを追加
    3. **（太字）を一時的にプレースホルダーに置換
    4. シングルアスタリスクの前後にスペースを追加
    5. プレースホルダーを元に戻す
    
    Args:
        line: 処理対象の行
        
    Returns:
        スペースが追加された行
    """
    # エスケープされた文字を一時的に保護
    ESCAPED_BACKTICK = "<<<ESCAPED_BACKTICK>>>"
    ESCAPED_ASTERISK = "<<<ESCAPED_ASTERISK>>>"
    
    line = line.replace(r'\`', ESCAPED_BACKTICK)
    line = line.replace(r'\*', ESCAPED_ASTERISK)
    
    # バッククォートの前後にスペースを追加
    # 前にスペースがない場合のみ追加（日本語文字、英数字、記号の後）
    line = re.sub(r'([^\s])`', r'\1 `', line)
    # 後にスペースがない場合のみ追加
    line = re.sub(r'`([^\s])', r'` \1', line)
    
    # **（太字）を一時的に保護
    DOUBLE_ASTERISK = "<<<DOUBLE_ASTERISK>>>"
    line = line.replace('**', DOUBLE_ASTERISK)
    
    # シングルアスタリスクの前後にスペースを追加
    # 前にスペースがない場合のみ追加
    line = re.sub(r'([^\s])\*', r'\1 *', line)
    # 後にスペースがない場合のみ追加
    line = re.sub(r'\*([^\s])', r'* \1', line)
    
    # プレースホルダーを元に戻す
    line = line.replace(DOUBLE_ASTERISK, '**')
    line = line.replace(ESCAPED_BACKTICK, r'\`')
    line = line.replace(ESCAPED_ASTERISK, r'\*')
    
    return line


def fix_po_file_spacing(content):
    """
    .poファイルのmsgstr行のみを処理してスペースを追加
    
    Args:
        content: .poファイルの内容
        
    Returns:
        修正された内容
    """
    lines = content.split('\n')
    result = []
    in_msgstr = False
    
    for line in lines:
        # msgstrの開始を検出
        if line.startswith('msgstr'):
            in_msgstr = True
            fixed_line = fix_line_spacing(line)
            result.append(fixed_line)
        # msgidの開始でmsgstrを終了
        elif line.startswith('msgid'):
            in_msgstr = False
            result.append(line)
        # msgstr内の継続行（引用符で始まる行）を処理
        elif in_msgstr and line.strip().startswith('"'):
            fixed_line = fix_line_spacing(line)
            result.append(fixed_line)
        # 空行でmsgstrを終了
        elif in_msgstr and line.strip() == '':
            in_msgstr = False
            result.append(line)
        else:
            result.append(line)
    
    return '\n'.join(result)


def process_po_file(filepath, dry_run=False):
    """
    1つの.poファイルを処理
    
    Args:
        filepath: .poファイルのパス
        dry_run: Trueの場合、ファイルを変更せずに検出のみ実行
        
    Returns:
        (bool, dict): (変更があったか, 統計情報)
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # 変更前のパターン数をカウント
        before_counts = count_patterns_in_msgstr(original_content)
        
        # スペースを追加
        fixed_content = fix_po_file_spacing(original_content)
        
        # 変更後のパターン数をカウント
        after_counts = count_patterns_in_msgstr(fixed_content)
        
        # 統計情報を作成
        stats = {
            'before': before_counts,
            'after': after_counts,
            'fixed': {
                'backtick_before': before_counts['backtick_no_space_before'] - after_counts['backtick_no_space_before'],
                'backtick_after': before_counts['backtick_no_space_after'] - after_counts['backtick_no_space_after'],
                'asterisk_before': before_counts['asterisk_no_space_before'] - after_counts['asterisk_no_space_before'],
                'asterisk_after': before_counts['asterisk_no_space_after'] - after_counts['asterisk_no_space_after'],
            }
        }
        
        # 変更があったか確認
        if fixed_content != original_content:
            if not dry_run:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
            return True, stats
        
        return False, stats
        
    except Exception as e:
        print(f"エラー: {filepath} の処理中にエラーが発生しました: {e}", file=sys.stderr)
        return False, None


def main():
    """メイン処理"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='POファイルのmsgstr内でバッククォートとアスタリスクの前後にスペースを追加',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使用例:
  # locales/ja/LC_MESSAGESディレクトリ内のすべての.poファイルを処理
  python %(prog)s
  
  # カスタムディレクトリを指定
  python %(prog)s --po-dir /path/to/locales/ja/LC_MESSAGES
  
  # Dry-runモード（変更なしで検出のみ）
  python %(prog)s --dry-run
  
  # 詳細なログを表示
  python %(prog)s --verbose
"""
    )
    
    parser.add_argument(
        '--po-dir',
        type=Path,
        default=Path('locales/ja/LC_MESSAGES'),
        help='処理対象の.poファイルがあるディレクトリ（デフォルト: locales/ja/LC_MESSAGES）'
    )
    
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Dry-runモード: ファイルを変更せず、検出のみ実行'
    )
    
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='詳細なログを表示'
    )
    
    args = parser.parse_args()
    
    # ディレクトリの存在確認
    po_dir = args.po_dir
    if not po_dir.exists():
        print(f"エラー: ディレクトリが存在しません: {po_dir}", file=sys.stderr)
        sys.exit(1)
    
    # .poファイルを検索
    po_files = list(po_dir.rglob('*.po'))
    
    if not po_files:
        print(f"警告: {po_dir} 内に.poファイルが見つかりませんでした", file=sys.stderr)
        sys.exit(0)
    
    # ヘッダー表示
    print("=" * 80)
    print("Inline Markup Spacing Fix Script")
    print("バッククォート（`）とシングルアスタリスク（*）の前後にスペースを追加")
    print("=" * 80)
    print(f"\n処理対象ディレクトリ: {po_dir}")
    print(f"検出された.poファイル数: {len(po_files)}")
    
    if args.dry_run:
        print("\n⚠️  DRY-RUN モード: ファイルは変更されません")
    
    print("\n処理開始...\n")
    
    # 統計情報
    total_files_modified = 0
    total_fixes = defaultdict(int)
    
    # 各ファイルを処理
    for po_file in po_files:
        modified, stats = process_po_file(po_file, dry_run=args.dry_run)
        
        if modified and stats:
            total_files_modified += 1
            relative_path = po_file.relative_to(po_dir)
            
            # 修正内容を集計
            for key, value in stats['fixed'].items():
                total_fixes[key] += value
            
            if args.verbose or any(stats['fixed'].values()):
                print(f"✓ {relative_path}")
                if args.verbose:
                    print(f"  バッククォート前スペース追加: {stats['fixed']['backtick_before']} 箇所")
                    print(f"  バッククォート後スペース追加: {stats['fixed']['backtick_after']} 箇所")
                    print(f"  アスタリスク前スペース追加: {stats['fixed']['asterisk_before']} 箇所")
                    print(f"  アスタリスク後スペース追加: {stats['fixed']['asterisk_after']} 箇所")
                    print()
    
    # 結果サマリー
    print("\n" + "=" * 80)
    print("処理完了")
    print("=" * 80)
    print(f"処理ファイル数:         {len(po_files)}")
    print(f"変更されたファイル数:   {total_files_modified}")
    print(f"\n修正内容:")
    print(f"  バッククォート前にスペース追加:     {total_fixes['backtick_before']} 箇所")
    print(f"  バッククォート後にスペース追加:     {total_fixes['backtick_after']} 箇所")
    print(f"  シングルアスタリスク前にスペース追加: {total_fixes['asterisk_before']} 箇所")
    print(f"  シングルアスタリスク後にスペース追加: {total_fixes['asterisk_after']} 箇所")
    print(f"  合計修正箇所:                        {sum(total_fixes.values())} 箇所")
    
    if args.dry_run:
        print("\n⚠️  DRY-RUNモードで実行されたため、ファイルは変更されていません")
        print("実際にファイルを変更するには、--dry-runオプションを外して再実行してください")
    else:
        print("\n✓ ファイルの変更が完了しました")
        print("\n次のステップ:")
        print("1. ビルドを実行して警告が減少したか確認:")
        print("   cd docs && make clean && make html-ja")
        print("2. 変更内容をgitで確認:")
        print("   git diff locales/")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
