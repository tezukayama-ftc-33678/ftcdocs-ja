#!/usr/bin/env python3
"""
RST マークアップ抽出・保護ユーティリティ

日本語翻訳時にマークアップの前後の空白を保証し、
マークアップ自体を保護して翻訳対象から除外する。
"""

import re
from typing import Dict, List, Tuple


class RSTMarkupProtector:
    """RST マークアップを保護し、翻訳後に復元する"""
    
    def __init__(self):
        self.placeholders = {}
        self.counter = 0
        
        # 保護すべきRSTパターン（順序重要 - より具体的なパターンから先に処理）
        self.patterns = [
            # 1. 外部リンク（`text <url>`_）- URLを含むため先に処理
            (r'`[^<`]+<[^>`]+>`_', 'extlink'),
            
            # 2. ロール全般（:ref:`text`、:doc:`text`、:download:`file` など）
            (r':[a-z_]+:`[^`]+`', 'role'),
            
            # 3. URL（http/https）- 単独のURL
            (r'https?://[^\s<>`\[\]()]+', 'url'),
            
            # 4. ファイルパス（拡張子付き: .png, .pdf, .rst, .py など）
            (r'[a-zA-Z0-9_\-./]+\.(png|jpg|jpeg|gif|svg|pdf|rst|py|java|md|txt|zip|tar|gz|bmp|ico)', 'filepath'),
            
            # 5. インラインリテラル（``code``）
            (r'``[^`]+``', 'literal'),
            
            # 6. 強調（**bold**、*italic*）
            (r'\*\*[^\*]+\*\*', 'strong'),
            (r'\*[^\*\s][^\*]*[^\*\s]\*', 'emphasis'),
            
            # 7. 内部リンク（`text`_）
            (r'`[^`]+`_', 'intlink'),
            
            # 8. 置換参照（|name|）
            (r'\|[^\|]+\|', 'substitution'),
        ]
    
    def protect(self, text: str) -> Tuple[str, Dict[str, str]]:
        """
        マークアップをプレースホルダーで置換
        
        Returns:
            (保護されたテキスト, プレースホルダーマップ)
        """
        protected_text = text
        self.placeholders = {}
        self.counter = 0
        
        for pattern, markup_type in self.patterns:
            protected_text = self._protect_pattern(protected_text, pattern, markup_type)
        
        return protected_text, self.placeholders
    
    def _protect_pattern(self, text: str, pattern: str, markup_type: str) -> str:
        """特定のパターンを保護"""
        def replace_match(match):
            placeholder = f"__RST_{markup_type.upper()}_{self.counter}__"
            self.placeholders[placeholder] = match.group(0)
            self.counter += 1
            return placeholder
        
        return re.sub(pattern, replace_match, text)
    
    def restore(self, text: str, placeholders: Dict[str, str]) -> str:
        """
        プレースホルダーを元のマークアップに復元し、
        日本語文字の隣にマークアップがある場合は前後に空白を追加
        
        RST形式のマークアップは日本語テキストとの間にスペースが必須
        """
        if not placeholders:
            return text
        
        # Unicode範囲をここで定義
        def is_japanese(c):
            if not c:
                return False
            try:
                code = ord(c)
                # ひらがな、カタカナ、漢字、日本語句読点
                is_hiragana = '\u3040' <= c <= '\u309f'  # U+3040-U+309F
                is_katakana = '\u30a0' <= c <= '\u30ff'  # U+30A0-U+30FF
                is_kanji = '\u4e00' <= c <= '\u9fff'      # U+4E00-U+9FFF
                is_punctuation = c in '、。（）【】「」『』'
                return is_hiragana or is_katakana or is_kanji or is_punctuation
            except (TypeError, ValueError):
                return False
        
        result = text
        
        for placeholder, original in placeholders.items():
            pos = 0
            while True:
                # プレースホルダーの位置を検索
                pos = result.find(placeholder, pos)
                if pos == -1:
                    break
                
                # 前後の文字を確認
                before_char = result[pos-1] if pos > 0 else ''
                after_pos = pos + len(placeholder)
                after_char = result[after_pos] if after_pos < len(result) else ''
                
                # 前後に空白追加が必要か判定
                need_space_before = is_japanese(before_char) and before_char not in ' \n\t'
                need_space_after = is_japanese(after_char) and after_char not in ' \n\t'
                
                # 復元（前後の空白を含める）
                restored_with_space = ''
                if need_space_before:
                    restored_with_space += ' '
                restored_with_space += original
                if need_space_after:
                    restored_with_space += ' '
                
                # テキストを置換
                result = result[:pos] + restored_with_space + result[after_pos:]
                
                # 次の検索位置を更新（復元したテキストの後ろから再開）
                pos = pos + len(restored_with_space)
        
        return result
    

def split_into_chunks(text: str, max_length: int = 500) -> List[str]:
    """
    テキストを翻訳に適した小さなチャンクに分割
    
    Args:
        text: 分割するテキスト
        max_length: 最大チャンク長（文字数）
    
    Returns:
        チャンクのリスト
    """
    # 段落で分割（空行で区切られた部分）
    paragraphs = re.split(r'\n\s*\n', text)
    
    chunks = []
    current_chunk = []
    current_length = 0
    
    for para in paragraphs:
        para_length = len(para)
        
        # 段落が最大長を超える場合、文で分割
        if para_length > max_length:
            sentences = re.split(r'([.!?。！？])\s*', para)
            for i in range(0, len(sentences), 2):
                sentence = sentences[i]
                if i + 1 < len(sentences):
                    sentence += sentences[i + 1]
                
                if current_length + len(sentence) > max_length and current_chunk:
                    chunks.append('\n\n'.join(current_chunk))
                    current_chunk = [sentence]
                    current_length = len(sentence)
                else:
                    current_chunk.append(sentence)
                    current_length += len(sentence)
        else:
            # 現在のチャンクに追加できるか確認
            if current_length + para_length > max_length and current_chunk:
                chunks.append('\n\n'.join(current_chunk))
                current_chunk = [para]
                current_length = para_length
            else:
                current_chunk.append(para)
                current_length += para_length
    
    # 残りを追加
    if current_chunk:
        chunks.append('\n\n'.join(current_chunk))
    
    return chunks


def should_skip_translation(text: str) -> bool:
    """
    翻訳をスキップすべきテキストか判定
    
    - コードブロック
    - URLのみ
    - 数字のみ
    - 記号のみ
    """
    # 空文字または空白のみ
    if not text or not text.strip():
        return True
    
    # URLのみ（http/https で始まる）
    if re.match(r'^https?://', text.strip()):
        return True
    
    # 数字と記号のみ
    if re.match(r'^[\d\s\-_.,:;!?()[\]{}]+$', text.strip()):
        return True
    
    # コードブロックマーカー
    if text.strip().startswith('```') or text.strip().startswith('::'):
        return True
    
    return False


if __name__ == '__main__':
    # テスト
    protector = RSTMarkupProtector()
    
    test_text = """
    これは :doc:`ドキュメント </path/to/doc>` へのリンクです。
    **強調テキスト** や ``コード`` も含まれています。
    `外部リンク <https://example.com>`_ もあります。
    画像は images/sample.png にあり、PDFは files/manual.pdf です。
    ダウンロードは :download:`こちら <downloads/file.zip>` から。
    公式サイト: https://ftc-docs.firstinspires.org を参照。
    
    置換参照（画像表示）:
    |robot_image| や |ftc_logo| などが表示されます。
    |status-badge| もあります。
    
    複雑な例: |image-name_with-dashes| も対応しています。
    """
    
    print("=" * 60)
    print("元のテキスト:")
    print("=" * 60)
    print(test_text)
    print()
    
    protected, placeholders = protector.protect(test_text)
    print("=" * 60)
    print("保護されたテキスト:")
    print("=" * 60)
    print(protected)
    print()
    
    print("=" * 60)
    print("プレースホルダー:")
    print("=" * 60)
    for ph, orig in placeholders.items():
        print(f"  {ph} → {orig}")
    print()
    
    # 翻訳後を想定（日本語が続いている）
    translated = protected.replace("これは", "このドキュメントは")
    restored = protector.restore(translated, placeholders)
    
    print("=" * 60)
    print("復元されたテキスト:")
    print("=" * 60)
    print(restored)
    print()
    
    # URLとパスが保護されているか確認
    print("=" * 60)
    print("保護チェック:")
    print("=" * 60)
    urls_found = [v for v in placeholders.values() if 'http' in v]
    paths_found = [v for v in placeholders.values() if any(ext in v for ext in ['.png', '.pdf', '.zip'])]
    print(f"✓ URL保護: {len(urls_found)} 個")
    print(f"✓ パス保護: {len(paths_found)} 個")
    
    if urls_found:
        print("\nURL:")
        for url in urls_found:
            print(f"  - {url}")
    
    if paths_found:
        print("\nパス:")
        for path in paths_found:
            print(f"  - {path}")
    print()
    
    # 翻訳後を想定（日本語が続いている）
    translated = protected.replace("これは", "このドキュメントは")
    restored = protector.restore(translated, placeholders)
    
    print("復元されたテキスト:")
    print(restored)
