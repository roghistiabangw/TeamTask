# === Stage 34: Add support for multiple local user profiles ===
# Project: TeamTask
import json, os
from pathlib import Path

class ProfileManager:
    def __init__(self, base_path="."):
        self.base = Path(base_path) / ".teamtask_profiles"
        self.profiles_file = self.base / "profiles.json"
        if not self.profiles_file.exists():
            self._init_profiles()

    def _init_profiles(self):
        data = {"default": {"name": "Default", "color": "#3b82f6"}}
        with open(self.profiles_file, "w") as f:
            json.dump(data, f)

    def add_profile(self, name, color="#00ff00"):
        if not self.base.exists():
            self.base.mkdir()
        data = {}
        try:
            with open(self.profiles_file) as f:
                data = json.load(f)
        except FileNotFoundError:
            pass
        data[name] = {"name": name, "color": color}
        with open(self.profiles_file, "w") as f:
            json.dump(data, f, indent=2)

    def get_profile(self, name):
        try:
            with open(self.profiles_file) as f:
                profiles = json.load(f)
            return profiles.get(name) or profiles.get("default")
        except (FileNotFoundError, json.JSONDecodeError):
            return None

    def list_profiles(self):
        try:
            with open(self.profiles_file) as f:
                return list(json.load(f).keys())
        except FileNotFoundError:
            return []
