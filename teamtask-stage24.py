# === Stage 24: Add grouped summaries by category or status ===
# Project: TeamTask
def generate_grouped_summary(tasks):
    from collections import defaultdict
    groups = defaultdict(list)
    for task in tasks:
        key = f"{task.get('status', 'unknown')}/{task.get('category', 'general')}"
        groups[key].append(task)
    
    summary_lines = []
    for group_key, group_tasks in sorted(groups.items()):
        status, category = group_key.split('/', 1) if '/' in group_key else ('all', 'mixed')
        total_count = len(group_tasks)
        high_priority = sum(1 for t in group_tasks if t.get('priority') == 'high')
        
        summary_lines.append(f"\n### {status.title()} - {category}")
        summary_lines.append(f"- **Total**: {total_count} tasks")
        if high_priority > 0:
            summary_lines.append(f"- ⚠️ High Priority: {high_priority}")
        else:
            summary_lines.append("- ✅ No critical items")
        
        owners = set(t.get('owner') for t in group_tasks)
        if len(owners) > 1:
            summary_lines.append(f"- 👥 Owners involved: {', '.join(sorted(owners))}")
    
    return "\n".join(summary_lines)
