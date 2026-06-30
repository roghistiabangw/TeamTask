# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: TeamTask
import json, random, uuid
from datetime import date, timedelta

def reset_demo_data():
    tasks = [
        {"id": str(uuid.uuid4())[:8], "title": "Setup project repo", "owner": "alice", "priority": 1, "status": "done", "notes": "Initial commit"},
        {"id": str(uuid.uuid4())[:8], "title": "Design board UI", "owner": "bob", "priority": 2, "status": "in_progress", "notes": "Wireframes ready"},
        {"id": str(uuid.uuid4())[:8], "title": "Implement review tool", "owner": "charlie", "priority": 1, "status": "todo", "notes": ""},
    ]
    
    try:
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
        print(f"Demo data reset. {len(tasks)} tasks loaded.")
    except Exception as e:
        print(f"Error resetting demo data: {e}")

if __name__ == "__main__":
    reset_demo_data()
