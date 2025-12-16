#!/usr/bin/env python
# -*- coding: utf-8 -*-
from babel.messages import pofile
import io

po_path = r'locales\ja\LC_MESSAGES\gracious_professionalism\gp.po'

try:
    with io.open(po_path, 'r', encoding='utf-8') as f:
        catalog = pofile.read_po(f)
    
    print(f"✓ POファイルを読み込みました")
    print(f"エントリ数: {len(list(catalog))}")
    
    # メタデータを確認
    print("\nメタデータ:")
    for key, value in catalog.metadata.items():
        print(f"  {key}: {value}")
    
    # 各エントリを確認
    print("\nエントリ:")
    for i, msg in enumerate(catalog):
        if msg.id:
            msgid_preview = msg.id[:50] if len(msg.id) > 50 else msg.id
            msgstr_preview = msg.string[:50] if msg.string and len(msg.string) > 50 else msg.string
            print(f"  {i+1}. msgid: {msgid_preview}...")
            if not msg.string:
                print(f"     WARNING: msgstr が空です")

except Exception as e:
    print(f"✗ エラー: {e}")
    import traceback
    traceback.print_exc()
