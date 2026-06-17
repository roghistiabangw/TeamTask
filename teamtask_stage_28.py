# === Stage 28: Add overdue item detection based on due dates ===
# Project: TeamTask
def detect_overdue_tasks(tasks, current_date=None):
    if current_date is None:
        from datetime import date
        current_date = date.today()
    overdue = []
    for task in tasks:
        due_str = task.get('due_date') or task.get('deadline')
        if not due_str:
            continue
        try:
            due = datetime.strptime(due_str, '%Y-%m-%d').date()
            if due < current_date:
                overdue.append({**task, 'days_over': (current_date - due).days})
        except ValueError:
            pass
    return overdue
