# === Stage 72: Add Markdown report export ===
# Project: TeamTask
def export_markdown_report(tasks, output_path):
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("# TeamTask Weekly Report\n")
        f.write(f"**Generated:** {tasks.get('generated_at', 'N/A')}\n\n")
        
        if not tasks['items']:
            f.write("No tasks recorded.\n")
            return
        
        f.write("| ID | Owner | Priority | Status | Notes |\n")
        f.write("|----|-------|----------|--------|-------|\n")
        for item in tasks['items']:
            owner = item.get('owner', 'Unassigned')
            priority = item.get('priority', 'Medium')
            status = item.get('status', 'Open')
            notes = item.get('notes', '') or '-'
            f.write(f"| {item['id']} | {owner} | {priority} | {status} | {notes} |\n")
        
        f.write("\n## Summary\n")
        total = len(tasks['items'])
        completed = sum(1 for i in tasks['items'] if i.get('status') == 'Done')
        open_count = total - completed
        f.write(f"- **Total Tasks:** {total}\n")
        f.write(f"- **Completed:** {completed}\n")
        f.write(f"- **Open:** {open_count}\n\n")
