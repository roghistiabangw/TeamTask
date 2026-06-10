# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: TeamTask
def format_task(task):
    status = task.get("status", "unknown")
    priority = task.get("priority", "medium")
    owner = task.get("owner", "unassigned")
    notes = task.get("notes", "")
    lines = [f"[{status.upper():8}] [{priority:7}] {task.get('id', '?')}: {task.get('title', 'No title')}"]
    if owner:
        lines.append(f"  Owner: {owner}")
    if notes:
        lines.append(f"  Notes: {notes}")
    return "\n".join(lines)

def format_weekly_review(tasks):
    today = datetime.date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)
    review_lines = [f"Weekly Review: {week_start} to {week_end}", "=" * 40]
    for task in tasks:
        if task.get("due_date"):
            due = datetime.strptime(task["due_date"], "%Y-%m-%d").date()
            if week_start <= due <= week_end:
                review_lines.append(format_task(task))
    return "\n".join(review_lines)
