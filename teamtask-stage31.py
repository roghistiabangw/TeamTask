# === Stage 31: Add compact table rendering for long lists ===
# Project: TeamTask
def render_compact_table(tasks, max_rows=15):
    if len(tasks) > max_rows:
        tasks = tasks[:max_rows] + [f"... ({len(tasks)-max_rows} more)"]
    header = f"{'ID':<6} {'Owner':<20} {'Priority':<10} {'Status':<15}"
    print(header)
    for t in tasks:
        row = f"{t['id']:<6} {t.get('owner','')[:19]:<20} {t.get('priority','').upper():<10} {t.get('status','PENDING'):>15}"
        print(row)

def render_weekly_review(tasks, review_date=None):
    if not review_date:
        from datetime import date; review_date = date.today()
    today_str = str(review_date).replace('-', '/')
    header = f"{'ID':<6} {'Owner':<20} {'Priority':<10} {'Status':<15} {'Due Date':<12}"
    print(header)
    for t in tasks:
        due_str = str(t.get('due_date','')).replace('-', '/') if t.get('due_date') else 'N/A'
        row = f"{t['id']:<6} {t.get('owner','')[:19]:<20} {t.get('priority','').upper():<10} {t.get('status','PENDING'):>15} {due_str:<12}"
        print(row)
