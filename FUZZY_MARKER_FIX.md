# 翻訳が反映されない問題の解決方法

## 問題の概要

`make clean && make html-ja` を実行しても、`.po` ファイルに日本語訳が完全に記載されているにもかかわらず、ビルドされた HTML に部分的に英語が残ってしまう問題が発生していました。

## 根本原因

`.po` ファイルのヘッダー（メタデータセクション）に `#, fuzzy` というマーカーが存在していたことが原因でした。

### fuzzy マーカーとは

`#, fuzzy` マーカーは gettext において「翻訳が不確実である」ことを示すフラグです。このフラグが設定されていると、たとえ翻訳が完全に記載されていても、gettext はその翻訳を「確定していない」と判断し、翻訳を適用せずに元の英語テキストを使用します。

### ヘッダーの fuzzy マーカーの影響

特にヘッダー（最初の `msgid ""` / `msgstr ""` ペア）に fuzzy マーカーがある場合、**ファイル全体の翻訳が無効化**されます。これは、ヘッダーメタデータの信頼性が低いと判断されるためです。

## 発見した状況

- 全体で 256 個の `.po` ファイルが存在
- そのうち 250 個のファイルのヘッダーに `#, fuzzy` マーカーが存在
- これが原因で、完全な翻訳があっても英語が表示されていた

## 解決方法

### 実施した修正

以下のPythonスクリプトを作成・実行し、すべての `.po` ファイルのヘッダーから `#, fuzzy` マーカーを削除しました：

```python
#!/usr/bin/env python3
"""
Remove #, fuzzy markers from .po file headers.
"""

import os
from pathlib import Path

def remove_header_fuzzy_marker(po_file_path):
    """Remove the fuzzy marker from the header of a .po file."""
    with open(po_file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find the fuzzy marker in the header (should be around line 7)
    in_header = True
    header_fuzzy_line = -1
    
    for i, line in enumerate(lines):
        # The header ends when we find the first non-empty msgid
        if in_header and line.startswith('msgid') and not line.strip().endswith('msgid ""'):
            in_header = False
            break
        
        # Look for fuzzy marker in header section
        if in_header and line.strip() == '#, fuzzy':
            header_fuzzy_line = i
            break
    
    # If we found a fuzzy marker in the header, remove it
    if header_fuzzy_line >= 0:
        lines.pop(header_fuzzy_line)
        
        with open(po_file_path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
        
        return True
    
    return False

def main():
    """Process all .po files in the locales/ja directory."""
    repo_root = Path('/home/runner/work/ftcdocs-ja/ftcdocs-ja')
    locales_dir = repo_root / 'locales' / 'ja'
    
    po_files = list(locales_dir.rglob('*.po'))
    modified_count = 0
    
    for po_file in po_files:
        if remove_header_fuzzy_marker(po_file):
            modified_count += 1
    
    print(f"Modified {modified_count} out of {len(po_files)} files")

if __name__ == '__main__':
    main()
```

### 実行結果

- 250 個のファイルから fuzzy マーカーを削除
- 修正後、`make clean && make html-ja` を実行して日本語翻訳が正しく適用されることを確認

## 検証方法

修正が正しく適用されたことを以下の方法で検証しました：

1. **ビルドの実行**:
   ```bash
   cd docs
   make clean
   make html-ja
   ```

2. **HTML ファイルの確認**:
   ```bash
   # 日本語テキストが含まれているか確認
   grep "GitHubから分岐し、クローンする" docs/build/html-ja/programming_resources/tutorial_specific/android_studio/fork_and_clone_github_repository/Fork-and-Clone-From-GitHub.html
   
   # 英語テキストが残っていないか確認
   grep "Fork and Clone from GitHub" docs/build/html-ja/programming_resources/tutorial_specific/android_studio/fork_and_clone_github_repository/Fork-and-Clone-From-GitHub.html
   ```

3. **結果**:
   - ✅ 日本語翻訳が正しく表示される
   - ✅ 英語テキストが残っていない

## 今後の対応

### 新しい .po ファイルを追加する際の注意点

今後、新しい `.po` ファイルを作成または更新する際は、以下の点に注意してください：

1. **fuzzy マーカーの確認**: ファイルのヘッダーに `#, fuzzy` が含まれていないか確認する
2. **翻訳後の削除**: 翻訳が完了した後、必ず fuzzy マーカーを削除する

### fuzzy マーカーの確認コマンド

```bash
# すべての .po ファイルでヘッダーの fuzzy マーカーを確認
find locales/ja -name "*.po" -exec sh -c 'head -20 "$1" | grep -q "^#, fuzzy" && echo "$1"' _ {} \;
```

### fuzzy マーカーの一括削除

もし将来的に再び fuzzy マーカーが追加された場合は、上記のスクリプトを `/tmp` に保存して実行してください：

```bash
python3 /tmp/remove_fuzzy_markers.py
```

## 参考情報

### gettext と fuzzy マーカーについて

- fuzzy マーカーは、翻訳支援ツールが「自動的に推測した翻訳」や「元のテキストが変更されたため確認が必要な翻訳」に自動的に付与します
- 翻訳者が翻訳内容を確認し、正しいと判断した後に fuzzy マーカーを削除する必要があります
- ヘッダーの fuzzy マーカーは特に注意が必要で、これが存在すると**ファイル全体の翻訳が無効化**されます

### 関連するファイル

- 修正対象: `locales/ja/LC_MESSAGES/**/*.po` (250 ファイル)
- ビルド設定: `docs/Makefile`
- Sphinx 設定: `docs/source/conf.py`

## まとめ

この問題は、`.po` ファイルのヘッダーに含まれる `#, fuzzy` マーカーが原因で、完全な翻訳があっても適用されない状態でした。すべてのファイルから fuzzy マーカーを削除することで、日本語翻訳が正しく表示されるようになりました。

今後、新しい翻訳を追加する際は、fuzzy マーカーが含まれていないことを確認してください。
