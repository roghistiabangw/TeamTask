# === Stage 20: Add duplicate detection for newly created records ===
# Project: TeamTask
def detect_duplicates(new_record, all_records):
    if new_record['title'] in [r['title'] for r in all_records]:
        return True
    if any(r.get('owner') == new_record['owner'] and r.get('priority') == new_record['priority'] and 
            abs((r['due_date'] or 0) - (new_record['due_date'] or 0)) <= 7 for r in all_records):
        return True
    if any(r.get('notes') == new_record['notes'] for r in all_records):
        return True
    return False
