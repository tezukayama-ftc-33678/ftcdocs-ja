# Phase 4 Completion Roadmap

## Current Status (2025-12-17)

**Progress**: 152/1,011 entries (15.0%)  
**Files Complete**: 2/29 (7%)  
**Remaining**: 859 entries (~12-15 hours)

## Completed Files ✅

1. **apriltag-intro.po** (63/63) - AprilTag introduction and concepts
2. **apriltags.po** (6/6) - Booklet reference

## Files by Completion Priority

### Tier 1: Nearly Complete (>70%)
- **color_processing/index.po** - 10/11 (91%) - 1 entry left

### Tier 2: Significant Progress (15-30%)
- **visionportal-previews.po** - 4/19 (21%) - 15 entries left
- **visionportal-cpu-and-bandwidth.po** - 11/62 (18%) - 51 entries left
- **apriltag-localization.po** - 8/50 (16%) - 42 entries left

### Tier 3: Started (5-15%)
- understanding-apriltag-detection-values.po - 3/22 (14%)
- vision-processor-init.po - 3/21 (14%)
- apriltag-library.po - 5/47 (11%)
- apriltag-advanced-use.po - 2/23 (9%)
- huskylens.po - 7/81 (9%)
- color-locator-discover.po - 3/44 (7%)
- color-locator-explore.po - 3/43 (7%)
- color-sensor.po - 4/62 (6%)
- color-spaces.po - 1/21 (5%)
- apriltag-metadata.po - 1/22 (5%)
- opmode-test-images.po - 1/19 (5%)
- color-blob-concepts.po - 1/25 (4%)
- color-locator-round-blobs.po - 3/70 (4%)
- color-locator-challenge.po - 2/55 (4%)
- visionportal-webcams.po - 3/47 (6%)
- apriltag-reference-frame.po - 1/15 (7%)
- apriltag-pose.po - 1/14 (7%)
- visionportal-init.po - 1/16 (6%)

### Tier 4: Minimal/No Progress (<5%)
- apriltag-camera-calibration.po - 0/22
- apriltag-id-code.po - 1/10
- vision-multiportal.po - 0/14
- visionportal-camera-controls.po - 1/54
- visionportal-overview.po - 1/27
- decode-apriltag.po - 0/26

## Recommended Completion Strategy

### Option A: Sequential Completion (Recommended)
Complete files in order from smallest remaining work:

1. **Quick Wins** (Complete in 1-2 hours):
   - color_processing/index.po (1 entry)
   - apriltag-id-code.po (9 entries)
   - vision-multiportal.po (14 entries)
   - apriltag-pose.po (13 entries)
   - apriltag-reference-frame.po (14 entries)

2. **Small Files** (2-3 hours):
   - visionportal-init.po (15 entries)
   - visionportal-previews.po (15 entries)
   - opmode-test-images.po (18 entries)
   - vision-processor-init.po (18 entries)

3. **Medium Files** (4-5 hours):
   - understanding-apriltag-detection-values.po (19 entries)
   - color-spaces.po (20 entries)
   - apriltag-advanced-use.po (21 entries)
   - apriltag-metadata.po (21 entries)
   - apriltag-camera-calibration.po (22 entries)

4. **Large Files** (6-8 hours):
   - All remaining files with 40+ entries

### Option B: High-Priority Focus
Focus on most important documentation pages:

1. **Critical for Users**:
   - visionportal-overview.po (portal overview)
   - color-sensor.po (color detection basics)
   - huskylens.po (popular sensor)

2. **Complete Tutorial Sequences**:
   - color_processing/* files (complete the color processing tutorial)
   - apriltag vision_portal/* files (complete vision portal docs)

### Option C: Hybrid Approach
1. Complete all Tier 1 & 2 files first (quick wins)
2. Then focus on high-priority files
3. Fill in remaining files systematically

## Tools Available

### For Quick Translation
```bash
python3 batch_translate.py <po_file> template
# Edit generated script
python3 translate_<filename>.py
```

### For Status Checking
```bash
python3 batch_translate.py <po_file> stats
python3 translate_helper.py <po_file>
```

## Time Estimates

| Task | Entries | Est. Time |
|------|---------|-----------|
| Tier 1 completion | 1 | 0.5 hours |
| Tier 2 completion | 108 | 2-3 hours |
| Tier 3 completion | ~400 | 6-8 hours |
| Tier 4 completion | ~350 | 5-6 hours |
| **Total** | **859** | **12-15 hours** |

## Quality Standards (Must Maintain)

- ✅ Follow GLOSSARY.md for term consistency
- ✅ Preserve RST markup (`:doc:`, `:ref:`, `:download:`, etc.)
- ✅ Keep product/API names in English
- ✅ Use です・ます調 polite form
- ✅ Keep URLs unchanged
- ✅ Preserve formatting and line breaks

## Next Session Checklist

- [ ] Review current progress (b21bf40)
- [ ] Choose completion strategy (A, B, or C)
- [ ] Start with Tier 1 for quick wins
- [ ] Use batch_translate.py for efficiency
- [ ] Commit after each file completion
- [ ] Update this roadmap as files complete

## Success Metrics

- **Short-term**: Complete Tier 1 & 2 (109 entries) → 26% total
- **Mid-term**: Complete Tier 3 (~400 entries) → 65% total
- **Long-term**: Complete Phase 4 (859 entries) → 100%

---

**Last Updated**: 2025-12-17  
**Current Commit**: b21bf40  
**Status**: In Progress - 15.0% Complete
