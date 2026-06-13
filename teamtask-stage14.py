# === Stage 14: Add file load support with fallback demo data ===
# Project: TeamTask
def load_tasks_from_file(path: str) -> list[dict]:
    """Load tasks from a JSON file, falling back to demo data if missing."""
    import json
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        pass
    demo = [
        {"id": 1, "title": "Setup repo", "owner": "alice", "priority": "high"},
        {"id": 2, "title": "Add board UI", "owner": "bob", "priority": "medium"}
    ]
    return demo
