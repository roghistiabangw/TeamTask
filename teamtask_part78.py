# === Stage 78: Refactor one large function into smaller helpers while preserving behavior ===
# Project: TeamTask
def _parse_priority(priority_str):
    mapping = {"high": 1, "medium": 2, "low": 3}
    return mapping.get(priority_str.lower(), 0) if priority_str else 0


def _format_task_summary(task):
    owner = task.get("owner", "") or ""
    prio = f"[{_parse_priority(task.get('priority', ''))}] "
    notes = (task.get("notes") or "").strip()[:50] + "..." if len((task.get("notes") or "").strip()) > 50 else (task.get("notes") or "")
    return f"{owner} | {prio}{notes}"


def _group_tasks_by_owner(tasks):
    groups = {}
    for task in tasks:
        owner = task.get("owner", "unassigned")
        if owner not in groups:
            groups[owner] = []
        groups[owner].append(task)
    return groups
