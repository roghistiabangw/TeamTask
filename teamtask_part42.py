# === Stage 42: Add CSV export without external dependencies ===
# Project: TeamTask
def export_tasks_to_csv(tasks, filename="tasks.csv"):
    import csv
    if not tasks: return False
    headers = ["id", "title", "owner", "priority", "status", "notes"]
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        for t in tasks:
            row = {h: getattr(t, h, "") for h in headers}
            if not row["notes"]: row["notes"] = ""
            writer.writerow(row)
    return True
