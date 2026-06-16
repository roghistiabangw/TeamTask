# === Stage 26: Add weekly summary calculations ===
# Project: TeamTask
def calculate_weekly_summary(tasks, start_date):
    from datetime import timedelta, date
    today = date.today()
    week_start = (today - timedelta(days=today.weekday())).isoformat()
    week_end = (week_start + timedelta(days=6)).isoformat()
    summary = {"total": 0, "completed": 0, "overdue": 0}
    for task in tasks:
        if start_date <= task["created_at"] <= today and task["status"] == "done":
            summary["completed"] += 1
        elif task["deadline"] < week_start and task["status"] != "done":
            summary["overdue"] += 1
    summary["total"] = len([t for t in tasks if start_date <= t["created_at"] <= today])
    return summary
