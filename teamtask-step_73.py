# === Stage 73: Add a lightweight HTML report export ===
# Project: TeamTask
import json, os, datetime

def export_html_report(tasks_file="tasks.json", output_file="report.html"):
    if not os.path.exists(tasks_file):
        return "<html><body><p>No tasks found.</p></body></html>"
    
    with open(tasks_file) as f:
        data = json.load(f)
    
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    html_parts = [
        '<!DOCTYPE html>',
        '<html><head><meta charset="UTF-8"><title>TeamTask Report</title>',
        '<style>body{font-family:sans-serif;padding:20px}.task{border:1px solid #ccc;margin:10px 0;padding:10px;border-radius:4px}</style></head><body>'
    ]
    
    html_parts.append(f'<h1>TeamTask Report - {now}</h1>')
    html_parts.append('<table border="1" cellpadding="5"><tr><th>ID</th><th>Title</th><th>Owner</th><th>Priority</th><th>Status</th></tr>')
    
    for t in data.get("tasks", []):
        row = f'<tr><td>{t["id"]}</td><td>{t["title"]}</td><td>{t["owner"] or "Unassigned"}</td><td>{t["priority"]}</td><td>{t["status"]}</td></tr>'
        html_parts.append(row)
    
    html_parts.extend(['</table>', '</body></html>'])
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(html_parts))
