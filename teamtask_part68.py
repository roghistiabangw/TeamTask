# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: TeamTask
def generate_changelog(activity_log, output_file="CHANGELOG.md"):
    from datetime import datetime
    entries = sorted(activity_log, key=lambda x: x["timestamp"], reverse=True)
    grouped = {}
    for entry in entries:
        date_key = entry["date"].split("T")[0]
        if date_key not in grouped:
            grouped[date_key] = {"changes": [], "owners": set()}
        grouped[date_key]["changes"].append(entry)
        grouped[date_key]["owners"].add(entry.get("owner", "unknown"))

    lines = ["# TeamTask Changelog\n"]
    for date, data in sorted(grouped.items()):
        lines.append(f"## {date}\n")
        owners_str = ", ".join(sorted(data["owners"])) if data["owners"] else "Unknown"
        lines.append(f"**Owners:** {owners_str}\n")
        for change in data["changes"]:
            status_icon = "[x]" if change.get("completed", False) else "[ ]"
            priority_marker = f"[{change['priority']}]"
            note_preview = change.get("note", "")[:50] + "..." if len(change.get("note", "")) > 50 else change.get("note", "")
            lines.append(f"- {status_icon} **{priority_marker}** {change.get('task', 'Task')} - *{note_preview}*")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
