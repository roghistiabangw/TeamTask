# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: TeamTask
from dataclasses import dataclass, field
from typing import Optional
from datetime import date

@dataclass
class Task:
    id: str
    title: str
    owner: str
    priority: int  # 1=High, 2=Medium, 3=Low
    notes: str = ""
    status: str = "open"
    due_date: Optional[date] = None

@dataclass
class TeamMember:
    name: str
    github_profile: str
    tasks: list[Task] = field(default_factory=list)

def get_priority_label(p: int) -> str:
    labels = {"1": "🔴 High", "2": "🟡 Medium", "3": "🟢 Low"}
    return labels.get(str(p), "⚪ Unknown")

def filter_by_owner(tasks: list[Task], owner_name: str) -> list[Task]:
    return [t for t in tasks if t.owner == owner_name]

def sort_by_priority(tasks: list[Task]) -> list[Task]:
    return sorted(tasks, key=lambda t: t.priority)
