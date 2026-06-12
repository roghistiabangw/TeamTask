# === Stage 11: Add JSON export for the current application state ===
# Project: TeamTask
def export_state(tasks):
    """Export current task board state to JSON."""
    import json
    from datetime import datetime
    data = {
        "timestamp": datetime.now().isoformat(),
        "tasks": tasks,
        "metadata": {"version": 1.0}
    }
    filename = f"teamtask_backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"State exported to {filename}")
