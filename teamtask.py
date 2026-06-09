# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: TeamTask
class TeamTaskBoard:
    def __init__(self):
        self.tasks = []
        self.weekly_reviews = []
        self.demo_data = [
            {"id": 1, "title": "Setup CI/CD", "owner": "Alice", "priority": "high", "notes": "Configure GitHub Actions"},
            {"id": 2, "title": "Write unit tests", "owner": "Bob", "priority": "medium", "notes": "Cover core module"},
            {"id": 3, "title": "Update docs", "owner": "Charlie", "priority": "low", "notes": "Add API reference"}
        ]

    def add_task(self, title, owner, priority="medium", notes=""):
        task = {"id": len(self.tasks) + 1, "title": title, "owner": owner, "priority": priority, "notes": notes}
        self.tasks.append(task)
        return task

    def get_tasks_by_owner(self, owner):
        return [t for t in self.tasks if t["owner"] == owner]

    def get_high_priority_tasks(self):
        return [t for t in self.tasks if t["priority"] == "high"]

    def run_weekly_review(self, completed_task_ids=None):
        review = {"date": "Weekly Review", "completed": [], "pending": []}
        if completed_task_ids:
            for tid in completed_task_ids:
                task = next((t for t in self.tasks if t["id"] == tid), None)
                if task:
                    review["completed"].append(task)
        else:
            review["pending"] = self.tasks.copy()
        self.weekly_reviews.append(review)
        return review

    def reset_demo(self):
        self.tasks = self.demo_data.copy()
        self.weekly_reviews = []
        return self.tasks
