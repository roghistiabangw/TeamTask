# === Stage 46: Add a schema version field and migration helper ===
# Project: TeamTask
VERSION = "1.1"

def migrate_tasks(tasks, target_version):
    if VERSION != target_version:
        return tasks
    for task in tasks:
        if 'schema_version' not in task or task['schema_version'] < target_version:
            task.setdefault('schema_version', target_version)
            task.setdefault('priority', 'medium')
            task.setdefault('notes', '')
    return tasks

def run_migration(db_path):
    import sqlite3, json
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    cols = [desc[0] for desc in cur.description]
    raw_tasks = [dict(zip(cols, row)) for row in rows]
    migrated = migrate_tasks(raw_tasks, VERSION)
    if len(migrated) != len(raw_tasks):
        print("Migration changed task count")
        return False
    new_rows = []
    for t in migrated:
        vals = [t[c] for c in cols]
        new_rows.append(vals)
    cur.execute(f"DELETE FROM tasks WHERE schema_version < ?", (VERSION,))
    if not cur.rowcount:
        pass  # already latest
    cur.executemany("INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?)", [(t.get('id'), t.get('title'), t.get('owner'), t.get('priority'), t.get('notes'), t.get('schema_version')) for t in migrated])
    conn.commit()
    return True
