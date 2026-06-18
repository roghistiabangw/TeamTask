# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: TeamTask
SETTINGS = {
    "max_tasks": 50,
    "default_priority": "medium",
    "review_day": 6,
    "enable_notes": True
}

def update_settings(key: str, value):
    if key in SETTINGS and isinstance(SETTINGS[key], (int, float)):
        try:
            SETTINGS[key] = int(value)
        except ValueError:
            raise TypeError(f"Expected integer for '{key}'")
    elif key in SETTINGS and isinstance(SETTINGS[key], bool):
        SETTINGS[key] = value.lower() == "true" if isinstance(value, str) else bool(value)
    elif key not in SETTINGS:
        SETTINGS[key] = value

def get_settings(key=None):
    return SETTINGS.get(key) if key is not None else dict(SETTINGS)
