#!/usr/bin/env python3
"""
Sphinx gettext のデバッグ用スクリプト
line が None になっているメッセージを検出する
"""
import sys
from pathlib import Path
from sphinx.application import Sphinx
from sphinx.builders.gettext import MessageCatalogBuilder

# Monkey patch to catch the error
original_iter = MessageCatalogBuilder.MessageCatalog.__iter__

def debug_iter(self):
    """デバッグ用の __iter__ - None行番号を検出"""
    for message in self.messages:
        # 各メッセージの positions をチェック
        try:
            positions_set = set((source, line) for source, line, uuid in message.locations)
            # ソート前に None を検出
            for source, line in positions_set:
                if line is None:
                    print(f"WARNING: None line found in {source}", file=sys.stderr)
                    print(f"  Message: {message.text[:100]}", file=sys.stderr)
            sorted_positions = sorted(positions_set)
        except TypeError as e:
            print(f"ERROR in message: {message.text[:100]}", file=sys.stderr)
            print(f"  Locations: {message.locations}", file=sys.stderr)
            raise
    return original_iter(self)

# パッチ適用
MessageCatalogBuilder.MessageCatalog.__iter__ = debug_iter

if __name__ == '__main__':
    # 通常の sphinx-build gettext を実行
    from sphinx.cmd.build import main
    sys.exit(main(sys.argv[1:]))
