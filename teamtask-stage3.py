# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: TeamTask
def validate_task(task: dict) -> tuple[bool, str]:
    errors = []
    if not task.get("id"):
        errors.append("Missing required field: id")
    elif not isinstance(task["id"], (str, int)) or len(str(task["id"])) > 20:
        errors.append(f"Invalid id format: {task['id']}")

    if not task.get("title"):
        errors.append("Missing required field: title")
    elif len(task["title"]) < 3 or len(task["title"]) > 100:
        errors.append(f"Title length must be between 3 and 100 characters: {task['title']}")

    if not task.get("owner"):
        errors.append("Missing required field: owner")
    elif not isinstance(task["owner"], str) or len(task["owner"]) > 50:
        errors.append(f"Invalid owner name: {task['owner']}")

    if "priority" in task and task["priority"] not in ("low", "medium", "high"):
        errors.append("Priority must be one of: low, medium, high")

    if "notes" in task:
        if not isinstance(task["notes"], str):
            errors.append("Notes must be a string")
        elif len(task["notes"]) > 500:
            errors.append("Notes exceed 500 characters limit")

    return len(errors) == 0, "; ".join(errors)
