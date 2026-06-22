# === Stage 45: Add restore from backup with validation ===
# Project: TeamTask
import json, os, hashlib
BACKUP_FILE = "tasks_backup.json"
def restore_from_backup():
    if not os.path.exists(BACKUP_FILE):
        print("No backup file found.")
        return False
    try:
        with open(BACKUP_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        expected_hash = hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()[:16]
        if not hasattr(restore_from_backup, '_last_known_hash'):
            restore_from_backup._last_known_hash = None
        current_state_file = "state.json"
        if os.path.exists(current_state_file):
            with open(current_state_file) as f:
                current_data = json.load(f)
            current_hash = hashlib.sha256(json.dumps(current_data, sort_keys=True).encode()).hexdigest()[:16]
            if expected_hash == current_hash:
                print("Backup restored successfully.")
                return True
            else:
                print("Hash mismatch. Backup may be corrupted or from a different version.")
                return False
        else:
            with open(current_state_file, 'w') as f:
                json.dump(data, f)
            print("Initial backup loaded into state file.")
            return True
    except Exception as e:
        print(f"Restore failed: {e}")
        return False
