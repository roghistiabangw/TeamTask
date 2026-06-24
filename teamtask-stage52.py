# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: TeamTask
def get_task_summary(task: dict) -> str:
    """Generate a concise summary string for a task."""
    owner = task.get("owner", "Unassigned")
    priority = task.get("priority", "Normal").capitalize()
    notes = task.get("notes", "")[:50] + "..." if len(task.get("notes", "")) > 50 else task.get("notes", "")
    return f"[{priority}] {owner}: {notes}"

def format_weekly_review(tasks: list[dict], date: str) -> dict[str, list]:
    """Group tasks by priority for weekly review."""
    groups = {"High": [], "Medium": [], "Low": []}
    for task in tasks:
        p = task.get("priority", "Normal")
        if p not in groups:
            groups[p] = []
        groups[p].append(get_task_summary(task))
    return {k: sorted(v, key=lambda x: len(x), reverse=True) for k, v in groups.items()}

def filter_by_owner(tasks: list[dict], owner_name: str) -> list[dict]:
    """Return tasks owned by a specific person."""
    if not owner_name:
        return []
    return [t for t in tasks if t.get("owner", "").lower() == owner_name.lower()]

def calculate_completion_rate(tasks: list[dict]) -> float:
    """Calculate the percentage of completed tasks."""
    if not tasks:
        return 0.0
    total = len(tasks)
    completed = sum(1 for t in tasks if t.get("status") == "done")
    return round((completed / total) * 100, 2)

def sort_tasks_by_priority_and_date(tasks: list[dict]) -> list[dict]:
    """Sort tasks by priority (High > Medium > Low) then by due date."""
    order = {"High": 0, "Medium": 1, "Low": 2}
    return sorted(tasks, key=lambda t: (order.get(t.get("priority", "Normal"), 3), t.get("due_date", "")))

def get_task_details(task_id: str, tasks: list[dict]) -> dict | None:
    """Retrieve full details for a task by ID."""
    return next((t for t in tasks if t.get("id") == task_id), None)
