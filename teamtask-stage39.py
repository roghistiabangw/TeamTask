# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: TeamTask
def repair_data_integrity(tasks):
    """Fix common data issues: missing owners, invalid priorities, empty notes."""
    valid_priorities = {'low', 'medium', 'high'}
    for task in tasks:
        if not task.get('owner'):
            task['owner'] = 'unassigned'
        priority = task.get('priority', '').lower().strip()
        if priority and priority not in valid_priorities:
            task['priority'] = 'medium'
        elif not task.get('priority'):
            task['priority'] = 'low'
        notes = task.get('notes', '')
        if notes and len(notes) > 500:
            task['notes'] = notes[:500] + '[truncated]'
    return tasks
