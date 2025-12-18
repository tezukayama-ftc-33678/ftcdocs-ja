#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sphinxの英語出力(docs/build/html)と日本語出力(docs/build/html-ja)の構造差分を作成
- 片方のみに存在するファイル一覧を出力
- 結果を build_structure_diff.txt に書き出し
"""

from pathlib import Path
import argparse

def list_files(base: Path):
    return {p.relative_to(base) for p in base.rglob('*') if p.is_file()}


def main():
    parser = argparse.ArgumentParser(description='Sphinx英語/日本語ビルド構造比較')
    parser.add_argument('--docs-dir', help='docsディレクトリのパス（省略時はスクリプト位置から推定）')
    args = parser.parse_args()

    # スクリプト位置からレポジトリルートを推定
    script_dir = Path(__file__).resolve().parent
    default_docs = script_dir.parent  # docs/scripts -> docs
    docs_dir = Path(args.docs_dir) if args.docs_dir else default_docs

    html_dir = docs_dir / 'build' / 'html'
    html_ja_dir = docs_dir / 'build' / 'html-ja'
    if not html_dir.exists() or not html_ja_dir.exists():
        print('⚠ buildディレクトリが不足しているため、比較をスキップ')
        return
    en_files = list_files(html_dir)
    ja_files = list_files(html_ja_dir)

    extra_ja = sorted(ja_files - en_files)
    missing_ja = sorted(en_files - ja_files)

    report_lines = ['[Extra in html-ja]'] + [str(p) for p in extra_ja]
    report_lines += ['', '[Missing in html-ja]'] + [str(p) for p in missing_ja]

    report_path = docs_dir / 'build' / 'build_structure_diff.txt'
    report_path.write_text('\n'.join(report_lines), encoding='utf-8')
    print(f'✓ 構造比較完了: {report_path} に出力しました')

if __name__ == '__main__':
    main()
