# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: TeamTask
def filter_tasks(tasks, filters=None):
    if filters is None:
        filters = {}
    filtered = tasks
    for key, value in filters.items():
        if key == "status":
            filtered = [t for t in filtered if t.get("status") == value]
        elif key == "category":
            filtered = [t for t in filtered if t.get("category") == value]
        elif key == "owner":
            filtered = [t for t in filtered if t.get("owner") == value]
        elif key == "tag":
            filtered = [t for t in filtered if value in t.get("tags", [])]
    return filtered

def get_weekly_review_summary(tasks):
    today = datetime.date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)
    this_week_tasks = [t for t in tasks if t.get("created_at", today) >= week_start]
    overdue = [t for t in this_week_tasks if t.get("status") != "done" and t.get("due_date", today) < today]
    summary = {
        "total": len(this_week_tasks),
        "pending": len([t for t in this_week_tasks if t.get("status") != "done"]),
        "overdue": len(overdue),
        "tasks": this_week_tasks
    }
    return summary
