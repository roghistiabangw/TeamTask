# === Stage 38: Add data integrity checks for broken references ===
# Project: TeamTask
def validate_references(tasks, owners):
    valid_owner_ids = {o['id'] for o in owners}
    broken_refs = []
    for task in tasks:
        if task.get('owner_id') and task['owner_id'] not in valid_owner_ids:
            broken_refs.append(f"Task #{task['id']} references unknown owner {task['owner_id']}")
    return broken_refs
