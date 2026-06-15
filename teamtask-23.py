# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: TeamTask
def manage_tags(tasks, tag_name):
    for task in tasks:
        if tag_name in task['tags']:
            task['tags'].remove(tag_name)
        else:
            task['tags'].append(tag_name)
    
    summary = f"Tag '{tag_name}' status:"
    tagged_count = sum(1 for t in tasks if tag_name in t['tags'])
    untagged_count = len(tasks) - tagged_count
    
    if tagged_count > 0:
        summary += f"\n- Tasks with {tag_name}: {tagged_count}"
    
    if untagged_count > 0:
        summary += f"\n- Tasks without {tag_name}: {untagged_count}"
        
    return summary
