# === Stage 63: Add relationships between records where useful ===
# Project: TeamTask
from typing import Optional, List, Dict, Any
import uuid
from datetime import date, timedelta

class Task:
    def __init__(self, id: str = None, title: str = "", owner_id: str = "", priority: int = 3, notes: str = ""):
        self.id = id or str(uuid.uuid4())[:8]
        self.title = title
        self.owner_id = owner_id
        self.priority = max(1, min(5, priority))
        self.notes = notes
        self.created_at = date.today()

class TeamTaskBoard:
    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self.owners: Dict[str, str] = {}  # owner_id -> name
        self.weekly_reviews: List[Dict[str, Any]] = []

    def add_task(self, title: str, owner_name: str, priority: int = 3) -> Task:
        if not owner_name or owner_name.strip() == "":
            raise ValueError("Owner name cannot be empty")
        
        # Normalize owner ID to ensure consistent relationships
        normalized_owner_id = self._get_or_create_owner(owner_name).id
        
        task = Task(
            title=title,
            owner_id=normalized_owner_id,
            priority=priority
        )
        self.tasks[task.id] = task
        return task

    def _get_or_create_owner(self, name: str) -> 'Owner':
        if not self.owners.get(name):
            new_owner = Owner(id=str(uuid.uuid4())[:8], name=name)
            self.owners[name] = new_owner
        return self.owners[name]

    def get_tasks_by_owner(self, owner_name: str) -> List[Task]:
        owner_obj = self.owners.get(owner_name)
        if not owner_obj:
            return []
        return [t for t in self.tasks.values() if t.owner_id == owner_obj.id]

    def get_high_priority_tasks(self, threshold: int = 2) -> List[Task]:
        return [t for t in self.tasks.values() if t.priority <= threshold]

    def add_weekly_review_note(self, summary: str, date_str: str = None):
        review_date = date.fromisoformat(date_str) if date_str else date.today()
        self.weekly_reviews.append({
            "date": review_date.isoformat(),
            "summary": summary,
            "high_priority_count": len(self.get_high_priority_tasks())
        })

    def get_owner_stats(self, owner_name: str) -> Dict[str, Any]:
        tasks = self.get_tasks_by_owner(owner_name)
        return {
            "total_tasks": len(tasks),
            "avg_priority": sum(t.priority for t in tasks) / max(1, len(tasks)),
            "recent_review_count": len(self.weekly_reviews[-7:]) if self.weekly_reviews else 0
        }

class Owner:
    def __init__(self, id: str = None, name: str = ""):
        self.id = id or str(uuid.uuid4())[:8]
        self.name = name
