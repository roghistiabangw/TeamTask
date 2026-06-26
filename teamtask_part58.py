# === Stage 58: Add bulk update behavior for selected records ===
# Project: TeamTask
def bulk_update_selected(tasks, selected_ids, updates):
    """Update multiple tasks at once by ID."""
    if not selected_ids:
        return 0
    updated = []
    for task in tasks:
        if task['id'] in selected_ids and task.get('status') == 'active':
            new_task = task.copy()
            new_task.update(updates)
            updated.append(new_task)
    return len(updated)
