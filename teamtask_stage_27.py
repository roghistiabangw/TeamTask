# === Stage 27: Add monthly summary calculations ===
# Project: TeamTask
def calculate_monthly_summary(tasks):
    from collections import defaultdict
    monthly_stats = defaultdict(lambda: {'total': 0, 'completed': 0, 'by_priority': defaultdict(int)})
    for task in tasks:
        if hasattr(task, 'created_at'):
            month_key = task.created_at.strftime('%Y-%m')
        else:
            continue
        monthly_stats[month_key]['total'] += 1
        if hasattr(task, 'status') and task.status == 'completed':
            monthly_stats[month_key]['completed'] += 1
        priority_map = {'high': 3, 'medium': 2, 'low': 1}
        p = getattr(task, 'priority', 'medium')
        monthly_stats[month_key]['by_priority'][p] += 1
    summary_list = []
    for month in sorted(monthly_stats.keys()):
        stats = monthly_stats[month]
        avg_priority = sum(k * v for k, v in priority_map.items() if v) / max(1, stats['total'])
        completion_rate = (stats['completed'] / max(1, stats['total'])) * 100
        summary_list.append({
            'month': month,
            'total_tasks': stats['total'],
            'completed_tasks': stats['completed'],
            'completion_rate': round(completion_rate, 2),
            'avg_priority_score': round(avg_priority, 2)
        })
    return summary_list
