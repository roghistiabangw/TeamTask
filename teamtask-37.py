# === Stage 37: Add recommendations for the next useful action ===
# Project: TeamTask
def get_next_action(tasks):
    urgent = [t for t in tasks if t['priority'] == 'high' and (not t.get('status') or t['status'] != 'done')]
    if urgent: return f"Focus on high priority task: {urgent[0]['title']} ({urgent[0].get('owner', 'unassigned')})"
    pending = [t for t in tasks if not t.get('status') and t.get('due_date')]
    if pending: return f"Review upcoming due dates: {len(pending)} items need attention soon."
    review_needed = any(t['priority'] == 'medium' and (not t.get('last_reviewed', 0) < 7) for t in tasks)
    if review_needed: return "Schedule a weekly review session to reassess medium priority backlog."
    completed_today = [t for t in tasks if t.get('status') == 'done']
    if completed_today: return f"Great job! {len(completed_today)} tasks completed today. Plan next batch."
    return "No specific action identified; consider adding new tasks or re-evaluating priorities."
