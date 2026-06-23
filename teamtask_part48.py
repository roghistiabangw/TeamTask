# === Stage 48: Add small unit tests for creation and validation helpers ===
# Project: TeamTask
from typing import Optional, List
import re
from datetime import date

def validate_task_id(task_id: str) -> bool:
    return bool(re.match(r'^TASK-\d{4}$', task_id))

def validate_priority(priority: int) -> bool:
    return priority in (1, 2, 3, 4, 5)

def create_task_entry(owner: str, title: str, priority: int = 3, notes: Optional[str] = None) -> dict:
    if not owner or not title:
        raise ValueError("Owner and Title are required")
    if not validate_priority(priority):
        raise ValueError(f"Priority must be between 1 and 5. Got {priority}")
    
    entry = {
        "id": f"TASK-{date.today().strftime('%Y%m%d%H%M%S')}",
        "owner": owner,
        "title": title,
        "priority": priority,
        "notes": notes or "",
        "status": "open",
        "created_at": date.today().isoformat()
    }
    return entry

def validate_task_entry(entry: dict) -> bool:
    required_keys = {"id", "owner", "title", "priority", "status"}
    if not all(key in entry for key in required_keys):
        return False
    
    if not validate_task_id(entry["id"]):
        return False
    if not validate_priority(entry["priority"]):
        return False
    if entry["owner"].strip() == "" or entry["title"].strip() == "":
        return False
        
    valid_statuses = {"open", "in_progress", "review", "done"}
    if entry["status"] not in valid_statuses:
        return False
        
    return True

def filter_tasks_by_priority(tasks: List[dict], min_priority: int) -> List[dict]:
    return [t for t in tasks if t.get("priority", 5) <= min_priority]
