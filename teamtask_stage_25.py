# === Stage 25: Add daily summary calculations ===
# Project: TeamTask
def calculate_daily_summary(tasks):
    from collections import defaultdict
    daily_stats = defaultdict(lambda: {'completed': 0, 'failed': 0, 'total_time': 0})
    for task in tasks:
        date_key = task.get('date') or datetime.now().strftime('%Y-%m-%d')
        if task.get('status') == 'done':
            daily_stats[date_key]['completed'] += 1
            duration = (task.get('end_time', datetime.now()) - task.get('start_time', datetime.now())).total_seconds() / 3600
            daily_stats[date_key]['total_time'] += max(0, duration)
        elif task.get('status') == 'failed':
            daily_stats[date_key]['failed'] += 1
    return dict(sorted(daily_stats.items()))
