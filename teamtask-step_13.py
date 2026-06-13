# === Stage 13: Add file save support using a configurable path ===
# Project: TeamTask
import os, json, sys
from pathlib import Path
try:
    CONFIG = {
        "data_dir": Path.home() / ".teamtask" / "data",
        "backup_ext": ".bak",
        "auto_backup": True
    }
except Exception:
    CONFIG["data_dir"] = Path("teamtask_data")

def ensure_dirs():
    d = CONFIG["data_dir"]
    if not d.exists():
        d.mkdir(parents=True, exist_ok=True)
    return d

def save_tasks(tasks):
    ensure_dirs()
    path = CONFIG["data_dir"] / "tasks.json"
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(tasks, f, indent=2, ensure_ascii=False)
        if CONFIG.get("auto_backup"):
            backup_path = path.with_suffix(path.suffix + CONFIG["backup_ext"])
            if backup_path.exists():
                os.replace(backup_path, path.parent / (path.stem + "_old" + path.suffix))
    except Exception as e:
        print(f"[ERROR] Failed to save tasks: {e}")

def load_tasks():
    d = ensure_dirs()
    path = CONFIG["data_dir"] / "tasks.json"
    if not path.exists():
        return []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            elif isinstance(data, dict) and "tasks" in data:
                return data["tasks"]
            else:
                print("[WARN] Invalid tasks.json format")
                return []
    except Exception as e:
        print(f"[ERROR] Failed to load tasks: {e}")
        return []

if __name__ == "__main__":
    # Demo usage for CLI entry point if run directly
    current_tasks = load_tasks()
    new_task = {"id": 1, "title": "Demo Task", "owner": "demo", "priority": 2}
    current_tasks.append(new_task)
    save_tasks(current_tasks)
    print(f"Saved {len(load_tasks())} tasks to: {CONFIG['data_dir'] / 'tasks.json'}")
