# === Stage 35: Add active user switching and user-specific records ===
# Project: TeamTask
class UserContext:
    def __init__(self, name): self.name = name
    @property
    def active(self): return f"[{self.name}]" if hasattr(UserContext, '_active') and UserContext._active == self else ""
    def set_active(cls, user): cls._active = user; print(f"Switched to {user}")

class TaskRecord:
    def __init__(self, title, owner=None, priority="medium", notes="", due_date=None):
        self.title = title
        self.owner = owner or UserContext.active.name if hasattr(UserContext, '_active') else "anonymous"
        self.priority = priority
        self.notes = notes
        self.due_date = due_date

class TaskBoard:
    def __init__(self): self.tasks = []
    def add(self, title, **kwargs): return self.tasks.append(TaskRecord(title, **kwargs))
    def list_tasks(self, user=None):
        if not hasattr(UserContext, '_active'): return "No active user set."
        tasks = [t for t in self.tasks if t.owner == UserContext._active.name] or self.tasks
        print(f"\n{UserContext.active} Tasks:")
        for i, t in enumerate(tasks): print(f"{i+1}. [{t.priority}] {t.title} (Due: {t.due_date})")

def main():
    board = TaskBoard()
    UserContext.set_active("Alice"); board.add("Fix login bug", owner="Alice", priority="high", notes="Critical path")
    UserContext.set_active("Bob"); board.add("Update docs", owner="Bob", priority="low", due_date="2024-12-31")
    print(board.list_tasks())

if __name__ == "__main__": main()
