# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: TeamTask
class SearchFilter:
    def __init__(self, tasks):
        self.tasks = tasks
    
    def search(self, query):
        if not query:
            return list(self.tasks)
        q = query.lower()
        results = []
        for task in self.tasks:
            fields = [task.get('owner', '').lower(), 
                      str(task.get('priority', '')).lower(), 
                      task.get('notes', '').lower()]
            if any(q in f for f in fields):
                results.append(task)
        return results
