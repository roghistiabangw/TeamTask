# === Stage 9: Add sorting by title, date, priority, and last update time ===
# Project: TeamTask
def sort_tasks(tasks, key='last_update'):
    reverse = True if key in ('title', 'priority') else False
    priority_map = {'high': 0, 'medium': 1, 'low': 2}
    return sorted(
        tasks,
        key=lambda t: (t.get(key) or '', priority_map.get(t.get('priority'), 1), t.get('owner', '')),
        reverse=reverse if key in ('title', 'priority') else False
    )
