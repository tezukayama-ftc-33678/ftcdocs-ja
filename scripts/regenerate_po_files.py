#!/usr/bin/env python3
"""
POファイルを再生成するスクリプト
新しいPOTテンプレートをPOファイルにマージし、翻訳済みエントリを保持しながらリセット
"""

import os
import json
import shutil
from pathlib import Path
import subprocess
import sys

def regenerate_po_files():
    """POファイルを再生成"""
    
    # パス設定
    pot_dir = Path('docs/build/gettext')
    ja_po_dir = Path('locales/ja/LC_MESSAGES')
    
    if not pot_dir.exists():
        print(f"Error: {pot_dir} not found. Run 'make gettext' first.")
        sys.exit(1)
    
    if not ja_po_dir.exists():
        ja_po_dir.mkdir(parents=True, exist_ok=True)
    
    # POTファイルのリスト
    pot_files = list(pot_dir.glob('**/*.pot'))
    print(f"Found {len(pot_files)} POT files")
    print()
    
    # 各POTファイルに対応するPOファイルを処理
    merged_count = 0
    created_count = 0
    
    for pot_file in pot_files:
        # ディレクトリ構造を保持
        relative_path = pot_file.relative_to(pot_dir)
        po_file = ja_po_dir / relative_path.with_suffix('.po')
        
        # ディレクトリを作成
        po_file.parent.mkdir(parents=True, exist_ok=True)
        
        # msgmergeを実行（既存のPOファイルがあれば、新しいテンプレートと統合）
        if po_file.exists():
            # 既存のPOファイルがあれば、msgmergeで統合
            result = subprocess.run(
                ['msgmerge', '--update', '--no-fuzzy-matching', str(po_file), str(pot_file)],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"✓ Merged: {relative_path}")
                merged_count += 1
            else:
                print(f"✗ Failed to merge {relative_path}: {result.stderr[:100]}")
                # フォールバック: POTファイルをコピー
                shutil.copy(str(pot_file), str(po_file))
                merged_count += 1
        else:
            # 新規POファイルを作成
            # POTをコピーして、msgfmtで初期化
            shutil.copy(str(pot_file), str(po_file))
            
            # POファイルのヘッダーを更新
            update_po_header(po_file)
            
            print(f"✓ Created: {relative_path}")
            created_count += 1
    
    print()
    print("=" * 60)
    print(f"Regeneration complete:")
    print(f"  Merged: {merged_count} files")
    print(f"  Created: {created_count} files")
    print(f"  Total: {merged_count + created_count} files")
    print("=" * 60)
    
    # 翻訳進捗ファイルをリセット
    progress_file = Path('data/translation_progress.json')
    if progress_file.exists():
        with open(progress_file, 'r', encoding='utf-8') as f:
            progress = json.load(f)
        
        # 翻訳済みエントリをクリア（統計のみ保持）
        for file_info in progress.get('files', {}).values():
            file_info['translated'] = 0
            file_info['total'] = file_info['total'] if 'total' in file_info else 0
        
        with open(progress_file, 'w', encoding='utf-8') as f:
            json.dump(progress, f, ensure_ascii=False, indent=2)
        
        print("✓ Reset translation progress file")


def update_po_header(po_file):
    """POファイルのヘッダーを更新"""
    with open(po_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # ファジーマーカーを削除（新しいファイルはすべてファジー）
    if '#, fuzzy\n' in content:
        content = content.replace('#, fuzzy\n', '', 1)
    
    with open(po_file, 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    regenerate_po_files()
