# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: TeamTask
from datetime import datetime, timedelta
def get_upcoming_tasks(tasks: list[dict], days_ahead: int = 7) -> list[dict]:
    now = datetime.now()
    upcoming = []
    for task in tasks:
        due = datetime.strptime(task.get("due_date", ""), "%Y-%m-%d")
        if (now <= due < now + timedelta(days=days_ahead)):
            overdue = False
            if due < now:
                overdue = True
            upcoming.append({**task, "is_overdue": overdue})
    return sorted(upcoming, key=lambda x: x["due_date"])

def get_weekly_review_summary(tasks: list[dict]) -> dict[str, any]:
    today = datetime.now().date()
    week_start = (today - timedelta(days=today.weekday())).isoformat()
    week_end = (week_start + timedelta(days=6)).isoformat()
    completed = sum(1 for t in tasks if t.get("status") == "done" and t["due_date"] >= week_start)
    overdue = [t for t in tasks if t.get("due_date", "") < today.isoformat()]
    high_priority = [t for t in tasks if t.get("priority") == "high"]
    return {
        "week_range": (week_start, week_end),
        "completed_this_week": completed,
        "total_overdue": len(overdue),
        "high_priority_count": len(high_priority)
    }
