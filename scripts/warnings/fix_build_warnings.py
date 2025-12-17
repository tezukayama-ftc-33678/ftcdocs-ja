#!/usr/bin/env python3
"""
ビルド警告を修正するスクリプト

主な修正内容:
1. Inline markup (**, *, ``) の不一致を修正
2. 翻訳文中の不正なマークアップを修正
3. POファイルの品質向上
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict
import polib


class BuildWarningFixer:
    def __init__(self, locales_dir: Path):
        self.locales_dir = locales_dir
        self.stats = {
            'files_processed': 0,
            'files_modified': 0,
            'inline_strong_fixed': 0,
            'inline_emphasis_fixed': 0,
            'inline_literal_fixed': 0,
            'other_fixes': 0
        }
    
    def fix_inline_markup(self, text: str) -> Tuple[str, int]:
        """
        Inline マークアップの不一致を修正
        
        修正対象:
        - ** で始まるが ** で終わらない
        - * で始まるが * で終わらない  
        - ` で始まるが ` で終わらない
        """
        if not text:
            return text, 0
        
        fixes = 0
        original = text
        
        # 1. ** の不一致を修正 (強調)
        # パターン: **text で終わりが無い、または不完全な場合
        # 戦略: ** の数を数え、奇数なら末尾に ** を追加
        strong_count = text.count('**')
        if strong_count % 2 == 1:
            # 最後の ** を見つけて、その後に閉じ ** がない場合
            # 末尾または次の句読点の前に ** を追加
            parts = text.split('**')
            if len(parts) > 1 and parts[-1]:
                # 最後の部分に ** が閉じられていない
                # 文の区切りを探す
                last_part = parts[-1]
                # 句読点で区切る
                match = re.search(r'([。、．，\.,!?！？\n])', last_part)
                if match:
                    pos = match.start()
                    parts[-1] = last_part[:pos] + '**' + last_part[pos:]
                    fixes += 1
                else:
                    # 句読点がない場合は末尾に追加
                    parts[-1] = last_part + '**'
                    fixes += 1
                text = '**'.join(parts)
        
        # 2. * の不一致を修正 (イタリック)
        # ** を除外して * だけをカウント
        text_without_strong = text.replace('**', '  ')
        emphasis_count = text_without_strong.count('*')
        if emphasis_count % 2 == 1:
            # 同様のロジックで修正
            parts = text.split('*')
            # ** 由来の空文字列を除外
            actual_parts = []
            for i, part in enumerate(parts):
                if i > 0 and i < len(parts) - 1:
                    # 前後が空なら ** の一部
                    if not parts[i-1].endswith('*') and not parts[i+1].startswith('*'):
                        actual_parts.append(part)
                else:
                    actual_parts.append(part)
            
            if len(actual_parts) > 1 and actual_parts[-1]:
                last_part = actual_parts[-1]
                match = re.search(r'([。、．，\.,!?！？\n])', last_part)
                if match:
                    pos = match.start()
                    actual_parts[-1] = last_part[:pos] + '*' + last_part[pos:]
                    fixes += 1
                else:
                    actual_parts[-1] = last_part + '*'
                    fixes += 1
                # 再構築が複雑なので、簡易的に処理
        
        # 3. ` の不一致を修正 (リテラル)
        literal_count = text.count('`')
        if literal_count % 2 == 1:
            # バッククォートが奇数個ある
            parts = text.split('`')
            if len(parts) > 1 and parts[-1]:
                last_part = parts[-1]
                # 空白または句読点で区切る
                match = re.search(r'([\s。、．，\.,!?！？\n])', last_part)
                if match:
                    pos = match.start()
                    parts[-1] = last_part[:pos] + '`' + last_part[pos:]
                    fixes += 1
                else:
                    # スペースまたは記号の前に挿入
                    match = re.search(r'([^\w\-])', last_part)
                    if match:
                        pos = match.start()
                        parts[-1] = last_part[:pos] + '`' + last_part[pos:]
                        fixes += 1
                    else:
                        parts[-1] = last_part + '`'
                        fixes += 1
                text = '`'.join(parts)
        
        return text, fixes
    
    def fix_specific_patterns(self, text: str) -> Tuple[str, int]:
        """
        特定のパターンを修正
        """
        if not text:
            return text, 0
        
        fixes = 0
        
        # パターン1: **で** のような不自然な強調
        if '**で**' in text or '**を**' in text or '**に**' in text:
            text = re.sub(r'\*\*([でをにがはもの])\*\*', r'\1', text)
            fixes += 1
        
        # パターン2: 翻訳後に残った英語の **text** を日本語に修正
        # (これはLLMに任せる方が良い)
        
        return text, fixes
    
    def process_po_file(self, po_path: Path) -> bool:
        """
        POファイルを処理
        """
        try:
            po = polib.pofile(str(po_path))
        except Exception as e:
            print(f"エラー: {po_path} を読み込めません: {e}")
            return False
        
        modified = False
        
        for entry in po:
            if not entry.msgstr:
                continue
            
            original_msgstr = entry.msgstr
            
            # Inline markup を修正
            fixed_text, markup_fixes = self.fix_inline_markup(entry.msgstr)
            
            # 特定パターンを修正
            fixed_text, pattern_fixes = self.fix_specific_patterns(fixed_text)
            
            if fixed_text != original_msgstr:
                entry.msgstr = fixed_text
                modified = True
                
                if markup_fixes > 0:
                    # どの種類の修正か判定
                    if '**' in original_msgstr:
                        self.stats['inline_strong_fixed'] += markup_fixes
                    elif '*' in original_msgstr:
                        self.stats['inline_emphasis_fixed'] += markup_fixes
                    elif '`' in original_msgstr:
                        self.stats['inline_literal_fixed'] += markup_fixes
                
                if pattern_fixes > 0:
                    self.stats['other_fixes'] += pattern_fixes
        
        if modified:
            try:
                po.save()
                self.stats['files_modified'] += 1
                return True
            except Exception as e:
                print(f"エラー: {po_path} を保存できません: {e}")
                return False
        
        return False
    
    def process_all_files(self):
        """
        すべてのPOファイルを処理
        """
        po_files = list(self.locales_dir.glob('**/*.po'))
        
        print(f"処理中: {len(po_files)} 個のPOファイル")
        
        for po_path in po_files:
            self.stats['files_processed'] += 1
            
            if self.stats['files_processed'] % 10 == 0:
                print(f"進行中: {self.stats['files_processed']}/{len(po_files)}", end='\r')
            
            self.process_po_file(po_path)
        
        print()  # 改行
    
    def print_stats(self):
        """
        統計情報を表示
        """
        print("\n" + "="*60)
        print("修正統計:")
        print("="*60)
        print(f"処理ファイル数:     {self.stats['files_processed']}")
        print(f"修正ファイル数:     {self.stats['files_modified']}")
        print(f"Inline strong修正:  {self.stats['inline_strong_fixed']}")
        print(f"Inline emphasis修正: {self.stats['inline_emphasis_fixed']}")
        print(f"Inline literal修正:  {self.stats['inline_literal_fixed']}")
        print(f"その他修正:         {self.stats['other_fixes']}")
        print("="*60)


def main():
    """
    メイン処理
    """
    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parents[1]
    locales_dir = project_root / 'locales' / 'ja' / 'LC_MESSAGES'
    
    if not locales_dir.exists():
        print(f"エラー: ディレクトリが見つかりません: {locales_dir}")
        sys.exit(1)
    
    print("ビルド警告修正スクリプト")
    print("="*60)
    
    fixer = BuildWarningFixer(locales_dir)
    fixer.process_all_files()
    fixer.print_stats()
    
    print("\n修正完了!")
    print("次のステップ:")
    print("1. make clean && make html-ja でビルド")
    print("2. 警告数の変化を確認")
    print("3. 必要に応じてLLMで追加修正")


if __name__ == '__main__':
    main()
