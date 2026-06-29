# === Stage 67: Add a function that returns key project metrics ===
# Project: TeamTask
def get_project_metrics(tasks):
    """Calculate key metrics from the task list."""
    if not tasks:
        return {"total": 0, "completed": 0, "in_progress": 0, "blocked": 0, "completion_rate": 0.0}
    
    total = len(tasks)
    completed = sum(1 for t in tasks if t.get("status") == "done")
    in_progress = sum(1 for t in tasks if t.get("status") == "in_progress")
    blocked = sum(1 for t in tasks if t.get("status") == "blocked")
    
    completion_rate = (completed / total * 100) if total > 0 else 0.0
    
    return {
        "total": total,
        "completed": completed,
        "in_progress": in_progress,
        "blocked": blocked,
        "completion_rate": round(completion_rate, 2),
        "priority_breakdown": sum(1 for t in tasks if t.get("priority") == "high"),
    }
