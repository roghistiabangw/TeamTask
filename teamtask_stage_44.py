# === Stage 44: Add backup creation for the data file ===
# Project: TeamTask
import json, os, datetime

def backup_data(data_file):
    if not data_file: return False
    try:
        with open(data_file) as f: content = json.load(f)
        now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{data_file}.bak.{now}"
        with open(backup_path, "w", encoding="utf-8") as bf: json.dump(content, bf, indent=2, ensure_ascii=False)
        print(f"Backup created at {backup_path}")
        return True
    except Exception as e:
        print(f"Backup failed: {e}")
        return False
