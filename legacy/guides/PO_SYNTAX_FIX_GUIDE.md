# 🚨 緊急対処：PO構文エラーの一括修正

## 現状

- **PO構文エラー**: 70ファイル（エスケープされていないダブルクォート）
- **品質問題**: 346件（emphasis_mismatch 304, inconsistent_ref 37, missing_doc_ref 5）

**最優先**: PO構文エラーを修正しないと、正規化もLLM修正も実行できない。

---

## 実行手順：構文エラーの一括修正

### **ステップ1: 構文エラーファイル一覧を出力**

```powershell
cd h:\ftcdocs-ja
python -c "
import polib
from pathlib import Path

errors = []
for po_file in Path('locales/ja/LC_MESSAGES').rglob('*.po'):
    try:
        polib.pofile(str(po_file))
    except Exception as e:
        errors.append(str(po_file))

with open('po_syntax_errors.txt', 'w', encoding='utf-8') as f:
    for p in errors:
        f.write(p + '\n')

print(f'{len(errors)} ファイルに構文エラー')
print('出力: po_syntax_errors.txt')
"
```

---

### **ステップ2: 自動修正スクリプトを実行**

```powershell
cd h:\ftcdocs-ja
python fix_po_syntax.py
```

（スクリプトは次のセクションで作成）

---

### **ステップ3: 修正後の確認**

```powershell
# 構文チェック
python -c "
import polib
from pathlib import Path
errors = 0
for po in Path('locales/ja/LC_MESSAGES').rglob('*.po'):
    try:
        polib.pofile(str(po))
    except:
        errors += 1
print(f'{errors} ファイルに構文エラー（目標: 0）')
"

# 品質チェック
cd docs
python tools/po-fixing/check_and_fix_po.py --po-dir ../locales/ja/LC_MESSAGES --output ../po_issues_fixed.json --verbose
```

---

## 自動修正スクリプト

以下のスクリプトを `fix_po_syntax.py` として保存：

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PO 構文エラーの自動修正
- エスケープされていないダブルクォートを修正
- msgid/msgstr内の " を \" に置換（既にエスケープされている場合は除く）
"""

import re
from pathlib import Path

def fix_po_quotes(content: str) -> tuple[str, int]:
    """PO ファイルの msgstr 内のダブルクォートをエスケープ"""
    lines = content.split('\n')
    fixed_lines = []
    fixes = 0
    
    in_msgstr = False
    for line in lines:
        # msgid/msgstr の開始を検出
        if line.startswith('msgid ') or line.startswith('msgstr '):
            in_msgstr = True
            fixed_lines.append(line)
            continue
        
        # 空行で msgid/msgstr ブロック終了
        if not line.strip():
            in_msgstr = False
            fixed_lines.append(line)
            continue
        
        # msgstr ブロック内の継続行
        if in_msgstr and line.startswith('"') and line.endswith('"'):
            # 行内のエスケープされていない " を \" に変更
            # ただし、行頭と行末の " は除外
            inner = line[1:-1]  # 行頭・行末の " を除外
            
            # すでにエスケープされている \" は一時的に置換
            inner = inner.replace(r'\"', '\x00ESCAPED_QUOTE\x00')
            # エスケープされていない " を \" に変更
            inner = inner.replace('"', r'\"')
            # 一時置換を戻す
            inner = inner.replace('\x00ESCAPED_QUOTE\x00', r'\"')
            
            new_line = f'"{inner}"'
            if new_line != line:
                fixes += 1
            fixed_lines.append(new_line)
        else:
            fixed_lines.append(line)
    
    return '\n'.join(fixed_lines), fixes

def main():
    repo = Path(__file__).parent
    po_dir = repo / 'locales' / 'ja' / 'LC_MESSAGES'
    
    total_fixes = 0
    fixed_files = 0
    
    for po_file in po_dir.rglob('*.po'):
        try:
            content = po_file.read_text(encoding='utf-8')
            fixed_content, fixes = fix_po_quotes(content)
            
            if fixes > 0:
                po_file.write_text(fixed_content, encoding='utf-8')
                fixed_files += 1
                total_fixes += fixes
                print(f'✓ {po_file.relative_to(repo)}: {fixes} 箇所修正')
        except Exception as e:
            print(f'✗ {po_file.relative_to(repo)}: {e}')
    
    print(f'\n合計: {fixed_files} ファイル, {total_fixes} 箇所修正')

if __name__ == '__main__':
    main()
```

---

## 実行フロー（完全版）

```powershell
cd h:\ftcdocs-ja

# 1. 構文エラー修正
python fix_po_syntax.py

# 2. 正規化
python tools/po-fixing/normalize_po_whitespace.py --po-dir locales/ja/LC_MESSAGES

# 3. 品質チェック
python tools/po-fixing/check_and_fix_po.py --po-dir locales/ja/LC_MESSAGES --output po_issues_clean.json --verbose

# 4. 問題数を確認
python -c "import json; print(f\"{len(json.load(open('po_issues_clean.json')))} 件\")"

# 5. 重要問題を修正（missing_doc_ref, inconsistent_ref）
python tools/po-fixing/fix_po_with_llm.py --issues po_issues_clean.json --types missing_doc_ref inconsistent_ref --limit 50

# 6. 再正規化
python tools/po-fixing/normalize_po_whitespace.py --po-dir locales/ja/LC_MESSAGES

# 7. 最終チェック
python tools/po-fixing/check_and_fix_po.py --po-dir locales/ja/LC_MESSAGES --output po_issues_final.json --verbose

# 8. ビルド
cd docs
make clean && make html && make html-ja
```

---

## 期待される結果

| ステップ | 問題数 |
|---------|-------|
| 初期状態 | 346 |
| 構文エラー修正 | 346（変わらず、ただし正規化可能に） |
| 正規化 | ~300 |
| LLM修正（50件） | ~250 |
| 再正規化 | ~230 |

**目標**: 200件以下 → ビルド警告大幅削減

---

## すぐに実行

```powershell
cd h:\ftcdocs-ja

# fix_po_syntax.py を作成（上記スクリプトをコピー）

# 実行
python fix_po_syntax.py
python tools/po-fixing/normalize_po_whitespace.py --po-dir locales/ja/LC_MESSAGES
python tools/po-fixing/check_and_fix_po.py --po-dir locales/ja/LC_MESSAGES --output po_issues_clean.json --verbose
```

この3ステップで状況が劇的に改善します。
