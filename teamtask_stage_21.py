# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: TeamTask
def archive_and_restore(tasks, cutoff_days=7):
    from datetime import datetime, timedelta
    now = datetime.now()
    threshold = now - timedelta(days=cutoff_days)
    archived = []
    for task in tasks:
        if task.get('completed') or task['created_at'] < threshold:
            task['_archived'] = True
            archived.append(task)
        else:
            task['_archived'] = False
    return [t for t in tasks if not t.pop('_archived', False)], archived
