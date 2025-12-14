# .po-based Translation Workflow

## Quick Start (新しいワークフロー)

### Prerequisites

```bash
# Install dependencies
cd docs
pip install -r requirements.txt
```

### Daily Workflow

#### 1. Update from upstream (上流の変更を取得)

```bash
# Fetch changes from official English repository
git fetch upstream
git merge upstream/main

# Extract new/changed translatable strings
cd docs
make gettext

# Update Japanese PO files
make ja-update
```

#### 2. Translate (翻訳作業)

Edit PO files in `docs/locale/ja/LC_MESSAGES/`:

```po
# Example: docs/locale/ja/LC_MESSAGES/index.po

#: ../../source/index.rst:5
msgid "Welcome to FIRST Tech Challenge"
msgstr "FIRST Tech Challenge へようこそ"

#: ../../source/index.rst:10
msgid "This is the official documentation for *FIRST* Tech Challenge."
msgstr "これは **FIRST** Tech Challenge の公式ドキュメントです。"
```

**Translation Tools:**
- [Poedit](https://poedit.net/) - Desktop GUI editor
- VS Code with i18n Ally extension
- [Weblate](https://weblate.org/) - Online collaboration platform
- Any text editor (PO files are plain text)

#### 3. Build and Preview (ビルドとプレビュー)

```bash
# Build Japanese documentation
cd docs
make ja-build

# Preview in browser
python -m http.server 8000 --directory build/html/ja
# Then open http://localhost:8000
```

#### 4. Check Progress (進捗確認)

```bash
# Show translation statistics
make ja-stats

# Or use msgfmt for specific files
msgfmt --statistics locale/ja/LC_MESSAGES/index.po
```

#### 5. Commit (コミット)

```bash
# Add translated PO files
git add docs/locale/ja/

# Commit with descriptive message
git commit -m "翻訳: index, overview ページを更新"

# Push
git push origin your-branch
```

## Make Commands

### Core Commands

```bash
# Extract translatable strings to POT files
make gettext

# Update Japanese PO files from POT files
make ja-update

# Build Japanese HTML
make ja-build

# Show translation statistics
make ja-stats
```

### Combined Workflow

```bash
# Full update and build cycle
make gettext && make ja-update && make ja-build
```

### Legacy Commands (still work)

```bash
# Build English version
make html

# Clean build
make clean

# Build with specific language
make -e SPHINXOPTS="-D language='ja'" html
```

## PO File Structure

### Anatomy of a PO File

```po
# Translation comment (optional)
#: ../../source/index.rst:10
#: ../../source/intro.rst:5
msgid "Welcome to the documentation"
msgstr "ドキュメントへようこそ"

# Plural forms
msgid "You have %d robot"
msgid_plural "You have %d robots"
msgstr[0] "ロボットが %d 台あります"

# Fuzzy (needs review)
#, fuzzy
msgid "This text was changed upstream"
msgstr "この翻訳は古い可能性があります"

# Obsolete (commented out, removed from source)
#~ msgid "Old text that was removed"
#~ msgstr "削除されたテキスト"
```

### Translation States

| State | Meaning | Action |
|-------|---------|--------|
| Empty msgstr | Not translated | Translate it |
| Has msgstr | Translated | Done ✓ |
| Fuzzy flag (#, fuzzy) | Needs review | Review and update |
| Commented (#~) | Obsolete | Can be removed |

## Understanding Updates

When you run `make ja-update` after upstream changes:

### New Strings
```po
# New in upstream - needs translation
msgid "This is a new feature"
msgstr ""
```

### Changed Strings
```po
# Changed upstream - needs review
#, fuzzy
msgid "This feature has been updated"
msgstr "この機能は更新されました"  # Old translation
```

### Deleted Strings
```po
# Removed from source
#~ msgid "This feature was removed"
#~ msgstr "この機能は削除されました"
```

## Translation Guidelines

### 1. Technical Terms (技術用語)

Keep technical terms in English with bold formatting:

```po
msgid "Create a new OpMode"
msgstr "新しい **OpMode** を作成します"

msgid "Connect to Control Hub"
msgstr "**Control Hub** に接続してください"
```

### 2. Proper Names (固有名詞)

Don't translate:
- FIRST, Gracious Professionalism
- OpMode, TeleOp, Autonomous
- Control Hub, Driver Station
- Blocks, OnBot Java, Android Studio

### 3. Code and Literals

Don't translate code or file names:

```po
msgid "Edit the ``config.xml`` file"
msgstr "``config.xml`` ファイルを編集します"
```

### 4. Markup

Preserve RST markup:

```po
msgid "See :doc:`introduction <intro>` for details"
msgstr "詳細は :doc:`入門 <intro>` を参照してください"
```

## Tools and Editors

### Poedit (Recommended for Beginners)

Free desktop application with GUI:
- Download: https://poedit.net/
- Features: Translation memory, suggestions, validation

### VS Code

With i18n Ally extension:
```bash
# Install extension
code --install-extension lokalise.i18n-ally
```

### Command Line

```bash
# Edit with any text editor
vim docs/locale/ja/LC_MESSAGES/index.po

# Validate PO file
msgfmt -c -v docs/locale/ja/LC_MESSAGES/index.po

# Get statistics
msgfmt --statistics docs/locale/ja/LC_MESSAGES/index.po
```

### Weblate (For Teams)

Online platform for collaborative translation:
- Self-hosted or cloud
- Git integration
- Translation memory
- User management

## Troubleshooting

### Build Errors

```bash
# Error: locale directory not found
# Solution: Create it
mkdir -p docs/locale/ja/LC_MESSAGES

# Error: POT files not found
# Solution: Generate them
cd docs && make gettext

# Error: PO files not found
# Solution: Create them
make ja-update
```

### Translation Not Showing

```bash
# 1. Clean build
cd docs
make clean

# 2. Rebuild
make gettext
make ja-update
make ja-build

# 3. Check language setting in conf.py
grep -n "language" source/conf.py
```

### Merge Conflicts in PO Files

PO files can have merge conflicts. To resolve:

```bash
# Use msgcat to merge PO files
msgcat --use-first file1.po file2.po -o merged.po

# Or manually resolve in editor
# PO files are plain text
```

## File Organization

```
docs/
├── source/               # English RST source files
│   ├── index.rst
│   └── ...
├── locale/              # Translations
│   └── ja/             # Japanese
│       └── LC_MESSAGES/
│           ├── index.po
│           └── ...
└── build/
    ├── gettext/         # Generated POT files
    │   ├── index.pot
    │   └── ...
    └── html/
        ├── en/          # English HTML (optional)
        └── ja/          # Japanese HTML
```

## Best Practices

### 1. Commit Strategy

```bash
# Commit POT files separately (optional)
git add docs/build/gettext/
git commit -m "chore: update POT files"

# Commit PO translations
git add docs/locale/ja/
git commit -m "翻訳: index, tutorial を更新"
```

### 2. Review Fuzzy Entries

After upstream updates:

```bash
# Find fuzzy entries
grep -r "fuzzy" docs/locale/ja/LC_MESSAGES/

# Review each one and remove fuzzy flag when done
```

### 3. Regular Sync

```bash
# Weekly or bi-weekly
git fetch upstream
git merge upstream/main
make gettext && make ja-update
```

### 4. Translation Memory

Consider using translation memory tools:
- Poedit has built-in TM
- Weblate has server-side TM
- OmegaT for large projects

## Migration from Direct RST Translation

If you have existing Japanese RST files:

1. See `MIGRATION_NEXT_STEPS.md` for detailed steps
2. Use `TRANSLATION_MAPPING.md` as reference
3. Gradually migrate sections

## Resources

- [Sphinx i18n Guide](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html)
- [sphinx-intl Documentation](https://sphinx-intl.readthedocs.io/)
- [GNU gettext Manual](https://www.gnu.org/software/gettext/manual/)
- [PO File Format](https://www.gnu.org/software/gettext/manual/html_node/PO-Files.html)

## Support

- Issues: File on GitHub
- Questions: Check MIGRATION_TO_PO_GUIDE.md
- Community: FTC Discord, forums

---

**Remember**: The PO-based workflow separates English content from Japanese translations, making it much easier to sync with upstream changes!
