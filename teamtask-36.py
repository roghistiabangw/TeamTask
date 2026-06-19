# === Stage 36: Add templates for quickly creating common records ===
# Project: TeamTask
def create_task_template(name, priority="medium", owner=None):
    return {
        "id": f"{name}_{int(time.time())}",
        "title": name.capitalize(),
        "description": f"Template task for {name} workflow.",
        "priority": priority,
        "owner": owner or None,
        "status": "todo",
        "due_date": datetime.now() + timedelta(days=7),
        "tags": ["template"],
        "created_at": datetime.now().isoformat(),
    }

def create_weekly_review_template():
    return {
        "id": f"review_{int(time.time())}",
        "title": "Weekly Review",
        "description": "Review completed tasks and plan next week.",
        "priority": "high",
        "owner": None,
        "status": "todo",
        "due_date": datetime.now() + timedelta(days=7),
        "tags": ["review"],
        "created_at": datetime.now().isoformat(),
    }
