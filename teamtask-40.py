# === Stage 40: Add plain text report export ===
# Project: TeamTask
def export_report(tasks, output_file="report.txt"):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("TeamTask Weekly Review Report\n")
        f.write("=" * 40 + "\n\n")
        for task in tasks:
            owner = task.get("owner", "Unknown")
            priority = task.get("priority", "Normal")
            notes = task.get("notes", "")
            status = task.get("status", "Open")
            f.write(f"[{status}] {task['id']}: [{priority}] Owner: {owner}\n")
            if notes:
                f.write(f"  Notes:\n    - {notes.strip()}\n")
        f.write("\n" + "=" * 40 + "\nEnd of Report\n")
