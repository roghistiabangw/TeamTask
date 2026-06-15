# === Stage 22: Add favorite records and quick favorite listing ===
# Project: TeamTask
class FavoriteManager:
    def __init__(self, tasks):
        self.tasks = tasks
        self.favorites = set()

    def toggle_favorite(self, task_id):
        if task_id in self.favorites:
            self.favorites.remove(task_id)
            return False
        else:
            self.favorites.add(task_id)
            return True

    def is_favorite(self, task_id):
        return task_id in self.favorites

    def get_favorites(self):
        return [self.tasks[tid] for tid in sorted(self.favorites)]
