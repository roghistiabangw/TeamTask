# === Stage 43: Add CSV import for the primary record type ===
# Project: TeamTask
import csv, json, sys
from pathlib import Path

def load_csv_tasks(csv_path: str) -> list[dict]:
    tasks = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            task = {
                'id': int(row['id']) if row.get('id') else None,
                'title': row.get('title', ''),
                'owner': row.get('owner', ''),
                'priority': row.get('priority', 'medium'),
                'notes': row.get('notes', ''),
                'status': row.get('status', 'todo')
            }
            tasks.append(task)
    return tasks

def merge_csv_tasks(csv_path: str, data_file: Path):
    existing = json.loads(data_file.read_text()) if data_file.exists() else {'tasks': [], 'metadata': {}}
    new_tasks = load_csv_tasks(csv_path)
    seen_ids = set(t['id'] for t in existing['tasks'])
    merged = [t for t in existing['tasks']] + [t for t in new_tasks if t.get('id') and t['id'] not in seen_ids]
    metadata = {'last_import': str(csv_path), 'import_count': len(new_tasks)}
    data_file.write_text(json.dumps({'tasks': merged, 'metadata': metadata}, indent=2))
