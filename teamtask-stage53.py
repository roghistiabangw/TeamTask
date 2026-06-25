# === Stage 53: Add command help text and usage examples ===
# Project: TeamTask
def print_help():
    """Print usage instructions and examples for TeamTask CLI."""
    help_text = f"""TeamTask - Compact team task board with owners, priorities, notes, and weekly review tools.

Usage:
  python main.py <command> [options]

Commands:
  add       Add a new task (requires owner name, priority level, optional note)
  list      List all tasks sorted by due date or priority
  edit      Edit an existing task ID (update status, notes, or assignee)
  review    Run weekly review to highlight overdue items and pending high-priority tasks
  export    Export current board state to JSON file

Examples:
  python main.py add --owner "Alice" --priority "high" --note "Fix login bug"
  python main.py list --sort priority
  python main.py edit task_123 --status completed
  python main.py review --output report.txt

Options (global):
  -h, --help     Show this help message and exit"""
    print(help_text)
