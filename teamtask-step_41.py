# === Stage 41: Add plain text import for a simple line-based format ===
# Project: TeamTask
def parse_simple_task(line):
    if not line.strip(): return None
    parts = line.split('|')
    if len(parts) < 4: raise ValueError(f"Invalid format: {line}")
    owner, priority, title, notes = [p.strip() for p in parts[:4]]
    due_date = parts[4].strip() if len(parts) > 4 else None
    status = 'todo' if not line.startswith('- ') else 'done'
    return {'owner': owner, 'priority': priority, 'title': title, 'notes': notes, 'due_date': due_date, 'status': status}

def write_simple_task(task, filename):
    header = f"{task['owner']}|{task['priority']}|{task['title']}|{task['notes']}"
    if task.get('due_date'): header += f"|{task['due_date']}"
    line = "-" + header if task['status'] == 'done' else header
    with open(filename, "a", encoding="utf-8") as f: f.write(line + "\n")

def load_simple_tasks(filename):
    tasks = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                task = parse_simple_task(line)
                if task: tasks.append(task)
    except FileNotFoundError: pass
    return tasks

def filter_by_priority(tasks, priority):
    return [t for t in tasks if t['priority'].lower() == priority.lower()]

# === Stage 41: Add plain text import for a simple line-based format ===
# Project: TeamTask
def parse_simple_task(text):
    lines = text.strip().split('\n')
    tasks = []
    for line in lines:
        if not line.startswith('#') and line.strip():
            parts = line.split('|', 3)
            if len(parts) >= 4:
                task = {
                    'id': int(parts[0]),
                    'title': parts[1],
                    'owner': parts[2].strip(),
                    'priority': parts[3]
                }
                tasks.append(task)
    return tasks

def write_simple_task(text, filename='tasks.txt'):
    with open(filename, 'w') as f:
        f.write(text)
