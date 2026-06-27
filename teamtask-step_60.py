# === Stage 60: Add saved views for frequently used filters ===
# Project: TeamTask
class SavedViewManager:
    def __init__(self, tasks):
        self.tasks = tasks
        self.views = {}

    def save_view(self, name, filters=None, sort_key='priority'):
        if filters is None:
            filters = {'status': 'open'}
        self.views[name] = {
            'name': name,
            'filters': filters,
            'sort_key': sort_key
        }

    def load_view(self, name):
        return self.views.get(name)

    def apply_saved_view(self, name):
        view = self.load_view(name)
        if not view:
            print(f"View '{name}' not found.")
            return []
        filtered_tasks = [t for t in self.tasks if all(t[k] == v for k, v in view['filters'].items())]
        filtered_tasks.sort(key=lambda x: getattr(x, view['sort_key']))
        return filtered_tasks

    def list_views(self):
        return list(self.views.keys())
