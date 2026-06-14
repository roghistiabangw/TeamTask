# === Stage 18: Add an activity log with timestamps and action names ===
# Project: TeamTask
class ActivityLog:
    def __init__(self, log_file="teamtask.log"):
        self.file = open(log_file, "a", encoding="utf-8")

    def record(self, action_name, details=None):
        timestamp = datetime.now().isoformat()
        entry = f"[{timestamp}] {action_name}"
        if details:
            entry += f" - {details}"
        self.file.write(entry + "\n")
        self.file.flush()

    def close(self):
        self.file.close()
