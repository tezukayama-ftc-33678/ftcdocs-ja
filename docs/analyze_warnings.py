import re
from collections import defaultdict

warnings = []
with open('build_warnings.txt', 'r') as f:
    for line in f:
        if 'WARNING' in line:
            warnings.append(line.strip())

# Categorize warnings
categories = defaultdict(list)

for warning in warnings:
    if 'reading error' in warning and 'list index out of range' in warning:
        po_file = re.search(r'/([^/]+\.po),', warning)
        if po_file:
            categories['PO file reading errors'].append(po_file.group(1))
    elif 'Inline strong start-string without end-string' in warning:
        categories['Inline strong markup errors'].append(warning)
    elif 'Inline emphasis start-string without end-string' in warning:
        categories['Inline emphasis markup errors'].append(warning)
    elif "document isn't included in any toctree" in warning:
        categories['Documents not in toctree'].append(warning)
    elif 'undefined label' in warning:
        categories['Undefined label references'].append(warning)
    elif 'unknown document' in warning:
        categories['Unknown document references'].append(warning)
    elif 'term not in glossary' in warning:
        categories['Glossary term errors'].append(warning)
    elif 'inconsistent term references' in warning:
        categories['Inconsistent term references'].append(warning)
    elif 'inconsistent references' in warning:
        categories['Inconsistent references'].append(warning)
    elif 'duplicate term description' in warning:
        categories['Duplicate term descriptions'].append(warning)
    elif 'Title underline too short' in warning:
        categories['Title formatting errors'].append(warning)
    else:
        categories['Other warnings'].append(warning)

# Print summary
print("=" * 80)
print("WARNING ANALYSIS SUMMARY")
print("=" * 80)
print(f"\nTotal warnings: {len(warnings)}")
print("\n" + "=" * 80)
print("BREAKDOWN BY CATEGORY:")
print("=" * 80)

for category, items in sorted(categories.items(), key=lambda x: -len(x[1])):
    print(f"\n{category}: {len(items)}")
    if len(items) <= 10:
        for item in items[:10]:
            if isinstance(item, str) and len(item) > 150:
                print(f"  - {item[:147]}...")
            else:
                print(f"  - {item}")
    else:
        print(f"  (showing first 10 of {len(items)})")
        for item in items[:10]:
            if isinstance(item, str) and len(item) > 150:
                print(f"  - {item[:147]}...")
            else:
                print(f"  - {item}")

