# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: TeamTask
def run_final_validation():
    from datetime import date, timedelta
    print(f"=== TeamTask Self-Check: {date.today()} ===")
    tasks = [
        {"id": 1, "owner": "Alice", "priority": "high", "status": "open"},
        {"id": 2, "owner": "Bob", "priority": "medium", "status": "in_progress"},
        {"id": 3, "owner": "Charlie", "priority": "low", "status": "closed"}
    ]
    for t in tasks:
        print(f"Task {t['id']}: Owner={t['owner']}, Priority={t['priority'].upper()}, Status={t['status']}")
    
    today = date.today()
    week_start = (today - timedelta(days=today.weekday())).strftime("%Y-%m-%d")
    print(f"Week Review Period: {week_start} to {today.strftime('%Y-%m-%d')}")
    
    high_priority_open = [t for t in tasks if t['priority'] == 'high' and t['status'] != 'closed']
    if high_priority_open:
        print(f"ALERT: {len(high_priority_open)} High Priority task(s) still open.")
    else:
        print("All high priority tasks are resolved or closed.")
    
    owners = set(t['owner'] for t in tasks)
    print(f"Active Owners ({len(owners)}): {', '.join(sorted(owners))}")
    print("Validation complete. No external dependencies used.")
