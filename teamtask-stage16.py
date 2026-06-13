# === Stage 16: Add argparse support for the most common commands ===
# Project: TeamTask
import argparse

def main():
    parser = argparse.ArgumentParser(description="TeamTask CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # List tasks
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument("--filter", choices=["active", "completed"], default="active", help="Filter by status")

    # Add task
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("-o", "--owner", required=True, help="Owner name or GitHub username")
    add_parser.add_argument("-p", "--priority", choices=["low", "medium", "high"], default="medium", help="Priority level")
    add_parser.add_argument("-n", "--note", help="Optional note description")

    # Edit task
    edit_parser = subparsers.add_parser("edit", help="Edit an existing task")
    edit_parser.add_argument("id", type=int, help="Task ID to edit")
    edit_parser.add_argument("--title", help="New title")
    edit_parser.add_argument("--owner", help="New owner")
    edit_parser.add_argument("--priority", choices=["low", "medium", "high"], help="New priority")
    edit_parser.add_argument("--note", help="New note (empty to clear)")

    # Review week
    review_parser = subparsers.add_parser("review", help="Run weekly review summary")
    review_parser.add_argument("--export", choices=["json", "csv"], default=None, help="Export report format")

    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Placeholder for actual logic implementation based on parsed arguments
    print(f"Command executed: {args.command}")
    if hasattr(args, 'title'):
        print(f"Adding task: {args.title} by {args.owner} (Priority: {args.priority})")
    elif hasattr(args, 'id'):
        print(f"Editing task ID {args.id}: Title={getattr(args, 'title', None)}, Owner={getattr(args, 'owner', None)}")
    elif args.command == "review":
        fmt = getattr(args, 'export', None) or "text"
        print(f"Generating weekly review report in {fmt} format...")

if __name__ == "__main__":
    main()
