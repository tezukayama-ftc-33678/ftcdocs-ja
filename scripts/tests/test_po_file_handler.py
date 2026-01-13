#!/usr/bin/env python3
"""
PO File Handlerのユニットテスト

POファイルの安全な読み書き、msgid保護、統計情報が正しく動作することを検証する。
"""

import unittest
import sys
import tempfile
import os
from pathlib import Path

# scriptsディレクトリをパスに追加
sys.path.insert(0, str(Path(__file__).parent.parent))

from core.po_file_handler import POFileHandler, POBatchHandler


class TestPOFileHandler(unittest.TestCase):
    """POFileHandlerクラスのテスト"""
    
    def setUp(self):
        """各テスト前の初期化"""
        self.handler = POFileHandler()
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """各テスト後のクリーンアップ"""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def create_test_po_file(self, content: str) -> str:
        """テスト用POファイルを作成"""
        po_path = os.path.join(self.temp_dir, "test.po")
        with open(po_path, 'w', encoding='utf-8') as f:
            f.write(content)
        return po_path
    
    def test_load_po_file(self):
        """POファイルの読み込み"""
        po_content = '''# Test PO file
msgid ""
msgstr ""
"Content-Type: text/plain; charset=UTF-8\\n"

msgid "Hello"
msgstr ""

msgid "World"
msgstr "世界"
'''
        po_path = self.create_test_po_file(po_content)
        po_file = self.handler.load(po_path)
        
        self.assertIsNotNone(po_file)
        # メタデータエントリを除いた実際のエントリ数
        entries = [e for e in po_file if e.msgid]
        self.assertEqual(len(entries), 2)
    
    def test_save_po_file(self):
        """POファイルの保存"""
        po_content = '''# Test PO file
msgid ""
msgstr ""

msgid "Test"
msgstr ""
'''
        po_path = self.create_test_po_file(po_content)
        po_file = self.handler.load(po_path)
        
        # msgstrを変更
        for entry in po_file:
            if entry.msgid == "Test":
                entry.msgstr = "テスト"
        
        # 保存
        self.handler.save(po_file, po_path)
        
        # 再読み込みして確認
        po_file2 = self.handler.load(po_path)
        for entry in po_file2:
            if entry.msgid == "Test":
                self.assertEqual(entry.msgstr, "テスト")
    
    def test_msgid_preservation(self):
        """msgidが決して変更されないことを確認"""
        po_content = '''msgid ""
msgstr ""

msgid "Original"
msgstr ""
'''
        po_path = self.create_test_po_file(po_content)
        po_file = self.handler.load(po_path)
        
        # msgidを変更しようとする（実際には変更されない）
        original_msgid = None
        for entry in po_file:
            if entry.msgid == "Original":
                original_msgid = entry.msgid
                entry.msgstr = "翻訳"
        
        # 保存
        self.handler.save(po_file, po_path)
        
        # 再読み込み
        po_file2 = self.handler.load(po_path)
        for entry in po_file2:
            if entry.msgid == "Original":
                # msgidは変更されていない
                self.assertEqual(entry.msgid, original_msgid)
                # msgstrは変更されている
                self.assertEqual(entry.msgstr, "翻訳")
    
    def test_get_untranslated_entries(self):
        """未翻訳エントリの取得"""
        po_content = '''msgid ""
msgstr ""

msgid "Translated"
msgstr "翻訳済み"

msgid "Untranslated"
msgstr ""

msgid "Also untranslated"
msgstr ""
'''
        po_path = self.create_test_po_file(po_content)
        po_file = self.handler.load(po_path)
        
        untranslated = self.handler.get_untranslated_entries(po_file)
        
        # 未翻訳は2つ
        self.assertEqual(len(untranslated), 2)
        msgids = [e.msgid for e in untranslated]
        self.assertIn("Untranslated", msgids)
        self.assertIn("Also untranslated", msgids)
    
    def test_get_entry_counts(self):
        """エントリ数の取得"""
        po_content = '''msgid ""
msgstr ""

msgid "Translated"
msgstr "翻訳済み"

msgid "Untranslated"
msgstr ""

#, fuzzy
msgid "Fuzzy"
msgstr "あいまい"
'''
        po_path = self.create_test_po_file(po_content)
        po_file = self.handler.load(po_path)
        
        translated = self.handler.get_translated_entries(po_file)
        untranslated = self.handler.get_untranslated_entries(po_file)
        
        # fuzzyもmsgstrがあるため翻訳済みとしてカウント
        self.assertEqual(len(translated), 2)
        self.assertEqual(len(untranslated), 1)
    
    def test_empty_po_file(self):
        """空のPOファイルの処理"""
        po_content = '''msgid ""
msgstr ""
'''
        po_path = self.create_test_po_file(po_content)
        po_file = self.handler.load(po_path)
        
        untranslated = self.handler.get_untranslated_entries(po_file)
        translated = self.handler.get_translated_entries(po_file)
        
        self.assertEqual(len(untranslated), 0)
        self.assertEqual(len(translated), 0)


class TestPOBatchHandler(unittest.TestCase):
    """POBatchHandlerクラスのテスト"""
    
    def setUp(self):
        """各テスト前の初期化"""
        self.batch_handler = POBatchHandler()
        self.temp_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """各テスト後のクリーンアップ"""
        import shutil
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
    
    def create_test_po_files(self):
        """複数のテスト用POファイルを作成"""
        po_content1 = '''msgid ""
msgstr ""

msgid "Test1"
msgstr ""
'''
        po_content2 = '''msgid ""
msgstr ""

msgid "Test2"
msgstr "テスト2"
'''
        
        po1 = os.path.join(self.temp_dir, "file1.po")
        po2 = os.path.join(self.temp_dir, "file2.po")
        
        with open(po1, 'w', encoding='utf-8') as f:
            f.write(po_content1)
        with open(po2, 'w', encoding='utf-8') as f:
            f.write(po_content2)
        
        return [po1, po2]
    
    def test_find_po_files(self):
        """POファイルの検索"""
        self.create_test_po_files()
        
        # exclude_translated=Falseで全ファイル取得
        po_files = self.batch_handler.find_po_files(self.temp_dir, exclude_translated=False)
        
        self.assertEqual(len(po_files), 2)
        # すべて.poファイル
        for po_file in po_files:
            self.assertTrue(str(po_file).endswith('.po'))
    
    def test_get_file_stats(self):
        """個別ファイルの統計情報の取得"""
        po_files = self.create_test_po_files()
        
        # 最初のファイルの統計
        stats = self.batch_handler.get_file_stats(po_files[0])
        
        self.assertIn('total', stats)
        self.assertIn('translated', stats)
        self.assertIn('untranslated', stats)
        self.assertGreater(stats['total'], 0)
    
    def test_empty_directory(self):
        """空ディレクトリの処理"""
        po_files = self.batch_handler.find_po_files(self.temp_dir)
        
        self.assertEqual(len(po_files), 0)


if __name__ == '__main__':
    unittest.main()
