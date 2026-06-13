# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: TeamTask
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}

    def dispatch(self, text):
        if not text: return None
        parts = text.strip().split(maxsplit=1)
        cmd = parts[0]
        args = parts[1] if len(parts) > 1 else ""
        try:
            handler = self.handlers.get(cmd)
            if callable(handler):
                return handler(args)
        except Exception as e:
            print(f"Error executing command '{cmd}': {e}")
        return None

    def register(self, cmd, func):
        self.handlers[cmd.lower()] = func
