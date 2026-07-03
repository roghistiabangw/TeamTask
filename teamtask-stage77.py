# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: TeamTask
from typing import Optional, List, Dict, Any, Callable
import re


def normalize_task_id(task_id: str) -> str:
    """Convert task ID to a normalized string."""
    return task_id.strip().lower() if task_id else ""


def parse_priority(priority_str: str) -> int:
    """Map priority strings to numeric values for sorting."""
    mapping = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    return mapping.get(normalize_task_id(priority_str).strip(), 4)


def group_tasks_by_owner(tasks: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Group tasks by their owner name."""
    grouped = {}
    for task in tasks:
        owner = task.get("owner", "unassigned") or "unassigned"
        if owner not in grouped:
            grouped[owner] = []
        grouped[owner].append(task)
    return grouped


def filter_tasks_by_priority(tasks: List[Dict[str, Any]], min_priority: int) -> List[Dict[str, Any]]:
    """Return tasks with priority less than or equal to the given value."""
    return [task for task in tasks if parse_priority(task.get("priority", "low")) <= min_priority]


def extract_notes(tasks: List[Dict[str, Any]]) -> Dict[str, str]:
    """Create a dictionary of owner names to their combined notes."""
    notes_map = {}
    for task in tasks:
        owner = task.get("owner", "unassigned") or "unassigned"
        note = task.get("notes", "") or ""
        if not note:
            continue
        current_notes = notes_map.get(owner, [])
        combined = f"{current_notes} {note}" if current_notes else note
        notes_map[owner] = combined
    return notes_map


def validate_task_data(task: Dict[str, Any]) -> bool:
    """Ensure a task has required fields with non-empty values."""
    required_fields = ["title", "priority"]
    for field in required_fields:
        value = task.get(field)
        if not isinstance(value, str) or not value.strip():
            return False
    return True


def generate_weekly_summary(tasks: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Generate a summary report of tasks grouped by status and priority."""
    stats = {"total": 0, "by_priority": {}, "by_owner": {}}
    for task in tasks:
        if not validate_task_data(task):
            continue
        stats["total"] += 1
        priority_key = parse_priority(task.get("priority", "low"))
        owner = task.get("owner", "unassigned") or "unassigned"
        
        current_by_prio = stats["by_priority"].get(priority_key, [])
        current_by_prio.append({"title": task.get("title"), "notes": task.get("notes", "")})
        stats["by_priority"][priority_key] = current_by_prio
        
        current_owner_notes = stats["by_owner"].get(owner, [])
        current_owner_notes.append(task)
        stats["by_owner"][owner]
