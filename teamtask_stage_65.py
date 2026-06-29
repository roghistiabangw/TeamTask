# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: TeamTask
def merge_imports(existing, new):
    seen = set()
    merged = []
    for line in existing:
        if line.startswith('import ') or line.startswith('from '):
            parts = line.replace(',', '').strip().split()
            name = parts[0].replace('"', '').replace("'", "")
            if not seen.add(name) and not any(name in x for x in merged):
                merged.append(line)
        else:
            merged.append(line)
    return merged
