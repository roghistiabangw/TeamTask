# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: TeamTask
def colorize(text, style=""):
    codes = {"reset": "\u001b[0m", "bold": "\u001b[1m", "red": "\u001b[31m", "green": "\u001b[32m", "yellow": "\u001b[33m", "blue": "\u001b[34m", "magenta": "\u001b[35m", "cyan": "\u001b[36m"}
    if not style: return text
    prefix = codes.get(style, "") + codes["bold"]
    suffix = codes["reset"]
    return f"{prefix}{text}{suffix}"

def print_task(task):
    owner_color = "cyan" if task.get("owner") else "yellow"
    priority_color = {"high": "red", "medium": "yellow", "low": "green"}.get(task.get("priority"), "white")
    status_color = {"done": "green", "pending": "blue", "review": "magenta"}.get(task.get("status"), "white")
    print(f"{colorize('=== TASK ===', 'bold')} | {task['id']}: {task['title']}")
    print(f"{colorize('', owner_color)} Owner: {task.get('owner', 'Unassigned')}{colorize('', 'reset')}")
    print(f"{colorize('', priority_color)} Priority: {task.get('priority', 'N/A')}{colorize('', 'reset')}")
    print(f"{colorize('', status_color)} Status: {task.get('status', 'Unknown')}{colorize('', 'reset')}")
    if task.get("notes"):
        print(f"Notes:\n{task['notes']}")

def review_weekly(tasks):
    today = __import__('datetime').date.today()
    week_start = (today - __import__('datetime').timedelta(days=today.weekday())).isoformat()
    week_end = (today + __import__('datetime').timedelta(days=7-today.weekday())).isoformat()
    print(f"\n{colorize('--- WEEKLY REVIEW ---', 'bold')}")
    for t in tasks:
        if t.get("status") == "done":
            continue
        created = t.get("created_at", "")
        try:
            date_created = __import__('datetime').date.fromisoformat(created)
            if week_start <= date_created.isoformat() <= week_end:
                print(f"{colorize('  [NEW THIS WEEK]', 'yellow')} {t['id']}: {t['title']}")
        except ValueError:
            pass
