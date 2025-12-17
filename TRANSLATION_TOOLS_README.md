# Translation Tools README

This directory contains tools to help with the Phase 4-7 translation work.

## Available Tools

### 1. translate_helper.py

**Purpose**: Quick utility to list untranslated entries in a PO file.

**Usage**:
```bash
python3 translate_helper.py <path_to_po_file>
```

**Example**:
```bash
python3 translate_helper.py locales/ja/LC_MESSAGES/apriltag/vision_portal/apriltag_intro/apriltag-intro.po
```

**Output**:
- Lists first 10-20 untranslated entries
- Shows total count of untranslated entries
- Displays location and English text preview

**Limitations**:
- Regex patterns work best for simple single-line entries
- May not correctly parse very complex multiline entries with many escaped quotes
- For complex entries, use manual inspection or the batch_translate.py tool

### 2. batch_translate.py

**Purpose**: Comprehensive translation workflow tool with multiple modes.

**Modes**:

#### Stats Mode
Shows translation statistics for a PO file.

```bash
python3 batch_translate.py <po_file> stats
```

Example output:
```
📊 Translation Stats for apriltag-intro.po
============================================================
Total entries:       63
Translated:          63 (100.0%)
Untranslated:        0 (0.0%)
============================================================
```

#### Template Mode
Generates a Python script template for batch translation.

```bash
python3 batch_translate.py <po_file> template
```

This creates a `translate_<filename>.py` file with:
- Pre-populated dictionary of untranslated entries
- Ready-to-fill Japanese translation placeholders
- Auto-apply functionality

#### Interactive Mode
Interactive translation entry (experimental).

```bash
python3 batch_translate.py <po_file> interactive
```

Shows entries one-by-one and prompts for Japanese translation.

**Limitations**:
- Works best for simple single-line msgid entries
- Complex multiline entries may need manual translation
- Interactive mode is suitable for small batches (10-20 entries)

### 3. Manual Translation Scripts

For complex multiline entries or when the helper tools don't work well, use direct Python scripts:

```python
import re

po_file = 'locales/ja/LC_MESSAGES/<path>/<file>.po'

with open(po_file, 'r', encoding='utf-8') as f:
    content = f.read()

translations = {
    'msgid "English text"\nmsgstr ""': 
        'msgid "English text"\nmsgstr "日本語テキスト"',
    # Add more translations...
}

count = 0
for old, new in translations.items():
    if old in content:
        content = content.replace(old, new)
        count += 1

with open(po_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Applied {count} translations")
```

## Translation Workflow

### Recommended Process

1. **Check status**:
   ```bash
   python3 batch_translate.py <po_file> stats
   ```

2. **List untranslated entries**:
   ```bash
   python3 translate_helper.py <po_file>
   ```

3. **Choose translation method**:
   - **Simple files**: Use template mode
   - **Complex files**: Write manual Python script
   - **Few entries**: Use interactive mode

4. **Translate**:
   - Fill in Japanese translations
   - Follow GLOSSARY.md for term consistency
   - Preserve RST markup
   - Keep product/API names in English

5. **Verify**:
   ```bash
   python3 batch_translate.py <po_file> stats
   ```

6. **Build test**:
   ```bash
   cd docs
   make clean
   make html-ja
   ```

7. **Commit**:
   ```bash
   git add <po_file>
   git commit -m "Phase X: Completed <filename> (X/Y entries)"
   git push
   ```

## Translation Standards

### Must Follow
- ✅ Preserve RST markup: `:doc:`, `:ref:`, `:download:`, `` ` `` for links, `**` for bold
- ✅ Keep product names in English: AprilTag, OpMode, Control Hub, Blocks, OnBot Java
- ✅ Keep API names in English: Telemetry, HardwareMap, LinearOpMode
- ✅ Use です・ます調 (polite form)
- ✅ Keep URLs unchanged
- ✅ Follow GLOSSARY.md for term translations

### Common Patterns

**Product/API Names** (keep in English):
- AprilTag, VisionPortal, EasyOpenCV
- OpMode, LinearOpMode, Telemetry, HardwareMap
- Control Hub, Driver Station, Robot Controller
- Blocks, OnBot Java, Android Studio
- FIRST, FTC

**Terms to Translate**:
- Team → チーム
- Robot → ロボット
- Competition → 競技
- Tutorial → チュートリアル
- Documentation → ドキュメント
- Configuration → 構成
- Installation → インストール

**Sentence Patterns**:
- "Click X" → "Xをクリックします"
- "Select X" → "Xを選択します"
- "For more information" → "詳細については"
- "Introduction" → "はじめに"
- "Summary" → "まとめ"

## Known Limitations

1. **Regex Patterns**: The tools use simple regex patterns that work well for most entries but may not handle:
   - Very complex multiline msgid entries with many continuation lines
   - Entries with multiple levels of escaped quotes
   - For these cases, use manual Python scripts with simple string replacement

2. **Interactive Mode**: Best for small batches (10-20 entries). For larger files, use template mode or manual scripts.

3. **Encoding**: Tools assume UTF-8 encoding. Ensure your PO files use UTF-8.

## Getting Help

- **Translation guidelines**: See `GLOSSARY.md`, `COPILOT_TRANSLATION_PROMPT.md`, `TRANSLATION_GUIDE.md`
- **Progress tracking**: See `PHASE4-7_TRANSLATION_STATUS.md`
- **Build documentation**: See `BUILD_JA.md`

## Examples

### Example 1: Quick Stats Check
```bash
$ python3 batch_translate.py locales/ja/LC_MESSAGES/apriltag/vision_portal/apriltag_intro/apriltag-intro.po stats

📊 Translation Stats for apriltag-intro.po
============================================================
Total entries:       63
Translated:          63 (100.0%)
Untranslated:        0 (0.0%)
============================================================
```

### Example 2: Generate Translation Template
```bash
$ python3 batch_translate.py locales/ja/LC_MESSAGES/color_processing/color-sensor/color-sensor.po template

📝 Created translation template: translate_color-sensor.py
   Edit the file to add Japanese translations, then run it to apply.
```

Then edit `translate_color-sensor.py` to fill in translations and run it:
```bash
$ python3 translate_color-sensor.py
Applied 25 translations to color-sensor.po
```

### Example 3: List Untranslated Entries
```bash
$ python3 translate_helper.py locales/ja/LC_MESSAGES/devices/huskylens/huskylens.po

======================================================================
Untranslated entries in huskylens.po
======================================================================

1. #: .../huskylens.rst:2
   EN: HuskyLens Introduction...

2. #: .../huskylens.rst:5
   EN: What is HuskyLens?...

... and 79 more untranslated entries

Total untranslated: 81
```

## Troubleshooting

**Issue**: Tool shows 0 untranslated but file isn't complete
- **Solution**: Check for multiline entries manually or use `grep 'msgstr ""' <po_file>`

**Issue**: Generated template has malformed entries
- **Solution**: Use manual Python script with simple string replacement

**Issue**: Translations not applying
- **Solution**: Check for exact string match, including line breaks and spacing

---

**Last Updated**: 2025-12-17
