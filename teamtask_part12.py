# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: TeamTask
import json, sys

def load_tasks(path):
    try:
        with open(path) as f:
            data = json.load(f)
        if isinstance(data, list):
            return {t['id']: t for t in data}
        raise ValueError("Expected a JSON array of tasks")
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Malformed JSON in '{path}'. Details: {e}")
        sys.exit(1)
