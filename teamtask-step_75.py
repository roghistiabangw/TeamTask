# === Stage 75: Add a validation report that lists warnings and errors ===
# Project: TeamTask
def validate_tasks(tasks):
    warnings = []
    errors = []
    for task in tasks:
        if not task.get('owner'):
            errors.append(f"Task {task['id']}: missing owner")
        elif isinstance(task['owner'], str) and '@' not in task['owner']:
            warnings.append(f"Task {task['id']}: owner '{task['owner']}' looks like a username, not an email or URL")
        if task.get('priority') not in ['low', 'medium', 'high', 'critical']:
            errors.append(f"Task {task['id']}: invalid priority '{task['priority']}'")
        if task.get('due_date'):
            try:
                from datetime import datetime
                due = datetime.strptime(task['due_date'], '%Y-%m-%d')
                if due < datetime.now():
                    warnings.append(f"Task {task['id']}: overdue by {(datetime.now() - due).days} days")
            except ValueError:
                errors.append(f"Task {task['id']}: invalid date format '{task['due_date']}'")
        notes = task.get('notes', '')
        if notes and len(notes) > 500:
            warnings.append(f"Task {task['id']}: notes too long ({len(notes)} chars)")
    return {'errors': errors, 'warnings': warnings}
