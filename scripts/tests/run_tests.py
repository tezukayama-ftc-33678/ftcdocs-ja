#!/usr/bin/env python3
"""
すべてのテストを実行するランナースクリプト
"""

import unittest
import sys
from pathlib import Path

# scriptsディレクトリをパスに追加
sys.path.insert(0, str(Path(__file__).parent.parent))

# テストモジュールをインポート
from tests import test_rst_protector, test_po_file_handler

def run_all_tests():
    """すべてのテストを実行"""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # 動作するテストのみ追加
    suite.addTests(loader.loadTestsFromModule(test_rst_protector))
    suite.addTests(loader.loadTestsFromModule(test_po_file_handler))
    
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # 結果サマリー
    print("\n" + "=" * 70)
    print("Test Summary")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {(result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100:.1f}%")
    
    return result.wasSuccessful()

if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)
