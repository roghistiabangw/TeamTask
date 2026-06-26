# === Stage 55: Add a setting to disable colorized output ===
# Project: TeamTask
class ColorMode:
    def __init__(self, enabled=True):
        self.enabled = enabled
    
    @property
    def is_enabled(self):
        return self.enabled and os.environ.get("NO_COLOR") != "1" and sys.stdout.isatty()
    
    def colorize(self, text, style=""):
        if not self.is_enabled:
            return text
        codes = {"bold": 1, "red": 31, "green": 32, "yellow": 33, "blue": 34}
        code = ""
        for s in [style]:
            if s.lower() in codes:
                code += f"\033[{codes[s]}m"
        return f"{code}{text}\033[0m"

def get_color_mode():
    mode_file = Path("teamtask_config.txt")
    try:
        with open(mode_file, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content == "color":
                return ColorMode(enabled=True)
            elif content == "no_color":
                return ColorMode(enabled=False)
    except FileNotFoundError:
        pass
    return ColorMode(enabled=sys.stdout.isatty())

def save_color_mode(mode):
    mode_file = Path("teamtask_config.txt")
    with open(mode_file, "w", encoding="utf-8") as f:
        if mode.enabled:
            f.write("color")
        else:
            f.write("no_color")
