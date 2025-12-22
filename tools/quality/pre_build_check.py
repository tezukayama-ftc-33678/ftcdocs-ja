#!/usr/bin/env python3
"""
Pre-Build Validation Script
ビルド前検証スクリプト

ビルド前に翻訳品質をチェックし、問題があれば警告を表示します。

使用方法:
    python tools/quality/pre_build_check.py
    python tools/quality/pre_build_check.py --strict  # エラーがあれば終了
"""

import sys
import argparse
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from translation_quality_checker import TranslationQualityChecker


def main():
    parser = argparse.ArgumentParser(
        description='Pre-Build Validation - ビルド前検証'
    )
    parser.add_argument(
        '--strict',
        action='store_true',
        help='エラーがある場合は終了コード1で終了'
    )
    parser.add_argument(
        '--auto-fix',
        action='store_true',
        help='自動修正可能な問題を修正してからビルド'
    )
    parser.add_argument(
        '--report',
        action='store_true',
        help='詳細レポートを生成'
    )
    
    args = parser.parse_args()
    
    print("="*60)
    print("ビルド前翻訳品質チェック")
    print("="*60)
    
    # チェッカーを初期化
    checker = TranslationQualityChecker(use_llm=False, verbose=False)
    
    # チェック実行
    print("翻訳品質をチェック中...")
    checker.check_all_files()
    
    # 結果表示
    print("\n" + "="*60)
    print("チェック結果")
    print("="*60)
    print(f"チェック済みファイル: {checker.stats['total_files']}")
    print(f"チェック済みエントリー: {checker.stats['total_entries']}")
    print(f"検出された問題: {len(checker.issues)}")
    
    if len(checker.issues) > 0:
        print(f"\n問題の内訳:")
        print(f"  - 未翻訳: {checker.stats['empty_entries']}")
        print(f"  - 構文エラー: {checker.stats['syntax_errors']}")
        print(f"  - 警告: {checker.stats['warnings']}")
        print(f"  - 自動修正可能: {checker.stats['auto_fixable']}")
    
    # 自動修正
    if args.auto_fix and checker.stats['auto_fixable'] > 0:
        print("\n自動修正を実行中...")
        fixed_count = checker.apply_fixes(dry_run=False)
        print(f"修正完了: {fixed_count} 件")
        
        # 再チェック
        print("\n修正後の再チェック...")
        checker = TranslationQualityChecker(use_llm=False, verbose=False)
        checker.check_all_files()
        print(f"残りの問題: {len(checker.issues)} 件")
    
    # レポート生成
    if args.report:
        print("\nレポートを生成中...")
        json_path = checker.generate_report_json()
        html_path = checker.generate_report_html()
        print(f"JSONレポート: {json_path}")
        print(f"HTMLレポート: {html_path}")
    
    # 判定
    print("\n" + "="*60)
    
    # エラーのみをカウント（警告は含めない）
    error_count = sum(1 for issue in checker.issues if issue.severity == 'error')
    
    if error_count == 0:
        print("✅ 品質チェック完了: 重大な問題は検出されませんでした")
        print("="*60)
        return 0
    else:
        print(f"⚠️  警告: {error_count} 件の構文エラーが検出されました")
        
        if checker.stats['auto_fixable'] > 0:
            print(f"\n💡 ヒント: {checker.stats['auto_fixable']} 件は自動修正可能です")
            print("   修正するには: python tools/quality/translation_quality_checker.py --fix")
        
        if args.report:
            print(f"\n詳細はレポートを確認してください:")
            print(f"   {html_path}")
        
        print("="*60)
        
        if args.strict:
            print("\nStrictモードが有効なため、エラーで終了します")
            return 1
        else:
            print("\nビルドは続行されますが、問題を確認することをお勧めします")
            return 0


if __name__ == '__main__':
    sys.exit(main())
