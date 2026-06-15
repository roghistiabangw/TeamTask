# === Stage 19: Add undo support for the last simple mutation ===
# Project: TeamTask
class UndoManager:
    def __init__(self, max_history=10):
        self.history = []
        self.max_history = max_history

    def record(self, action_name, state_snapshot):
        if len(self.history) >= self.max_history:
            del self.history[0]
        self.history.append({
            "action": action_name,
            "state": state_snapshot.copy()
        })

    def undo(self):
        if not self.history:
            return None
        last = self.history.pop()
        return last["action"], last["state"]
