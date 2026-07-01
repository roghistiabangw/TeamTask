# === Stage 74: Add a snapshot comparison helper for before/after states ===
# Project: TeamTask
def snapshot_diff(before: dict, after: dict) -> list[str]:
    """Generate a human-readable diff between two task state snapshots."""
    changes = []
    all_keys = set(before.keys()) | set(after.keys())
    for key in sorted(all_keys):
        b_val = before.get(key)
        a_val = after.get(key)
        if b_val != a_val:
            status = "DELETED" if b_val is None else ("ADDED" if a_val is None else "MODIFIED")
            changes.append(f"[{status}] {key}: {repr(b_val)} -> {repr(a_val)}")
    return changes

def compare_snapshots(before_path: str, after_path: str) -> list[str]:
    """Load two JSON snapshots and return a sorted list of textual differences."""
    import json
    try:
        with open(before_path, "r", encoding="utf-8") as f: before = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError): before = {}
    try:
        with open(after_path, "r", encoding="utf-8") as f: after = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError): after = {}
    return snapshot_diff(before, after)

if __name__ == "__main__":
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__)) or "."
    before_file = os.path.join(base_dir, "snapshots", "before.json")
    after_file = os.path.join(base_dir, "snapshots", "after.json")
    if not os.path.exists(before_file) or not os.path.exists(after_file):
        print("Snapshots not found. Run weekly review tool first.")
    else:
        diff = compare_snapshots(before_file, after_file)
        for line in diff:
            print(line)
