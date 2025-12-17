# Phase 4-7 Translation Status and Guide

## Overview

This document tracks the progress of translating Phases 4-7 of the FTC documentation project, covering approximately 2,900 entries across 178 files.

## Current Status (2025-12-17)

### Overall Progress
- **Total Entries**: ~2,900
- **Translated**: 76 (2.6%)
- **Remaining**: ~2,824 (97.4%)
- **Files Completed**: 1/178 (0.56%)

### Phase Breakdown

#### Phase 4: Vision Processing (AprilTag & Color Processing)
- **Total**: 1,022 entries across 29 files
- **Completed**: 76 entries (7.4%)
- **Status**: IN PROGRESS

**Completed Files:**
- ✅ `apriltag/vision_portal/apriltag_intro/apriltag-intro.po` (63/63 entries)

**In Progress Files:**
- ⏳ `apriltag/vision_portal/visionportal_cpu_and_bandwidth/visionportal-cpu-and-bandwidth.po` (13/66 entries)

**Remaining High-Priority Files:**
- `apriltag/vision_portal/visionportal_overview/visionportal-overview.po`
- `apriltag/vision_portal/apriltag_pose/apriltag-pose.po`
- `color_processing/color-sensor/color-sensor.po` (64 entries)
- `color_processing/color-locator-round-blobs/color-locator-round-blobs.po` (70 entries)
- `devices/huskylens/huskylens.po` (81 entries)

#### Phase 5: Advanced Programming & IMU
- **Total**: ~700 entries across 70 files
- **Completed**: 0 entries (0%)
- **Status**: NOT STARTED

**High-Priority Files:**
- `programming_resources/imu/imu.po` (160 entries) ★ CRITICAL

#### Phase 6: Game-Specific Resources, FAQ, Tech Tips
- **Total**: 361 entries across 23 files
- **Completed**: 0 entries (0%)
- **Status**: NOT STARTED

**Files:**
- `faq/faqs.po` (11 entries)
- `tech_tips/` (3 files, 156 entries)
- `game_specific_resources/` (4 files, 43 entries)

#### Phase 7: Manufacturing & Contributors Documentation
- **Total**: 950 entries across 56 files
- **Completed**: 0 entries (0%)
- **Status**: NOT STARTED
- **Priority**: LOW (primarily for contributors)

## Translation Methodology

### Tools Available

1. **translate_helper.py** - List untranslated entries in a PO file
   ```bash
   python3 translate_helper.py locales/ja/LC_MESSAGES/<path>/<file>.po
   ```

2. **fix_po_auto.py** - Auto-fix simple translations from GLOSSARY.md
   ```bash
   cd docs/scripts
   python fix_po_auto.py --dry-run  # Preview changes
   python fix_po_auto.py            # Apply changes
   ```

3. **detect_untranslated_simple.py** - Detect untranslated English in built HTML
   ```bash
   cd docs/scripts
   python detect_untranslated_simple.py
   ```

### Translation Process

#### Step 1: Select File
Choose next priority file from the list above.

#### Step 2: List Untranslated Entries
```bash
python3 translate_helper.py locales/ja/LC_MESSAGES/<path>/<file>.po
```

#### Step 3: Translate Systematically
Use Python scripts or manual editing to translate entries. Follow these guidelines:

**Translation Standards:**
- ✅ Follow GLOSSARY.md for term consistency
- ✅ Preserve RST markup (:doc:, :download:, :ref:, `` ` `` for links, ** for bold, * for italic)
- ✅ Keep product names in English (AprilTag, OpMode, Control Hub, Blocks, OnBot Java, etc.)
- ✅ Keep API names in English (Telemetry, HardwareMap, LinearOpMode, etc.)
- ✅ Use です・ます調 for consistent polite tone
- ✅ Keep URLs and external links unchanged
- ✅ Preserve line breaks and spacing in multiline entries

**Example Translation Patterns:**
```python
# Simple single-line
'msgid "Introduction"\nmsgstr ""' → 
'msgid "Introduction"\nmsgstr "はじめに"'

# With RST markup
'msgid ":doc:`Guide <path/to/guide>`"\nmsgstr ""' → 
'msgid ":doc:`Guide <path/to/guide>`"\nmsgstr ":doc:`ガイド <path/to/guide>`"'

# Multiline entry
'msgid ""\n"First line "\n"second line."\nmsgstr ""' → 
'msgid ""\n"First line "\n"second line."\nmsgstr ""\n"最初の行 "\n"2番目の行。"'
```

#### Step 4: Validate
After translating, check:
```bash
# Count untranslated entries
python3 translate_helper.py <po_file>

# Build and check for warnings
cd docs
make clean
make html-ja
```

#### Step 5: Commit Progress
```bash
git add <translated_file>
git commit -m "Phase X: Completed <filename> (X/Y entries)"
git push
```

### Efficient Batch Translation Script Template

```python
import re

po_file = 'locales/ja/LC_MESSAGES/<path>/<file>.po'

with open(po_file, 'r', encoding='utf-8') as f:
    content = f.read()

translations = {
    'msgid "English text"\nmsgstr ""': 
        'msgid "English text"\nmsgstr "日本語テキスト"',
    # Add more...
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

## Estimated Time Requirements

Based on current progress:
- **apriltag-intro.po**: 63 entries took ~45 minutes
- **Average rate**: ~1.4 entries/minute (including quality checks)
- **Remaining entries**: ~2,824
- **Estimated time**: **30-40 hours** of focused translation work

### Recommended Approach

1. **Solo translator**: 4-6 weeks at 1-2 hours/day
2. **Team of 3 translators**: 2-3 weeks (parallel work on different phases)
3. **Intensive sprint**: 1 week full-time

## Priority Order for Completion

### High Priority (Weeks 1-2)
1. Complete Phase 4 AprilTag files (critical for vision processing)
2. `imu.po` from Phase 5 (critical for navigation)
3. `color_processing` files from Phase 4
4. FAQ and tech tips from Phase 6

### Medium Priority (Weeks 3-4)
5. Remaining Phase 5 programming resources
6. Phase 6 game-specific and team resources

### Low Priority (Week 5+)
7. Phase 7 manufacturing documentation
8. Phase 7 contributor guidelines

## Common Translation Patterns

### Technical Terms (Keep in English)
- OpMode, LinearOpMode
- Telemetry, HardwareMap
- AprilTag, VisionPortal, EasyOpenCV
- Control Hub, Driver Station, Robot Controller
- Blocks, OnBot Java, Android Studio
- FIRST, FTC, FTC Blocks

### Terms to Translate
- Team → チーム
- Robot → ロボット
- Competition → 競技
- Game Manual → 競技マニュアル
- Tutorial → チュートリアル
- Documentation → ドキュメント
- Configuration → 構成
- Installation → インストール
- Download → ダウンロード

### Sentence Patterns
- "Click the button" → "ボタンをクリックします"
- "Select the option" → "オプションを選択します"
- "Install the software" → "ソフトウェアをインストールします"
- "For more information, see..." → "詳細については、...を参照してください"

## Quality Checklist

Before marking a file as complete:
- [ ] All msgstr fields are filled (no empty translations)
- [ ] RST markup preserved (:doc:, :ref:, :download:, etc.)
- [ ] URLs and links unchanged
- [ ] Product/API names in English
- [ ] Consistent use of です・ます調
- [ ] Run translate_helper.py shows 0 untranslated
- [ ] Build completes without new warnings

## Contact and Collaboration

For questions about translation:
- Check GLOSSARY.md for term definitions
- Review COPILOT_TRANSLATION_PROMPT.md for guidelines
- Refer to TRANSLATION_GUIDE.md for style guide

## File Locations

- **Source PO files**: `locales/ja/LC_MESSAGES/`
- **Translation scripts**: `docs/scripts/`
- **Helper script**: `translate_helper.py` (project root)
- **Guidelines**: `GLOSSARY.md`, `COPILOT_TRANSLATION_PROMPT.md`, `TRANSLATION_GUIDE.md`

---

**Last Updated**: 2025-12-17
**Status**: Phase 4 in progress, 2.6% overall completion
