# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: TeamTask
class BulkDeleteGuard:
    def __init__(self, tasks):
        self.tasks = tasks
        self.confirm_flag = False

    def set_confirmation(self, flag=True):
        if len(self.tasks) > 1 and not flag:
            raise ValueError("Bulk delete requires confirmation")
        self.confirm_flag = flag

    def execute_delete(self):
        if not self.confirm_flag:
            return "Deletion cancelled"
        deleted_count = sum(1 for t in self.tasks if t.status == 'completed')
        self.tasks[:] = [t for t in self.tasks if t.status != 'completed'] or self.tasks
        return f"{deleted_count} tasks removed from board"
