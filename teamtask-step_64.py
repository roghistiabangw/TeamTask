# === Stage 64: Add validation for relationship references ===
# Project: TeamTask
def validate_relationship_refs(tasks, relationships):
    task_ids = {t['id'] for t in tasks}
    rels_to_remove = []
    for i, rel in enumerate(relationships):
        if 'task_id' in rel and rel['task_id'] not in task_ids:
            rels_to_remove.append(i)
        elif 'related_task_id' in rel and rel['related_task_id'] not in task_ids:
            rels_to_remove.append(i)
    for i in reversed(rels_to_remove):
        relationships.pop(i)
