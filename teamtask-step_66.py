# === Stage 66: Add export of a short status dashboard ===
# Project: TeamTask
def export_status_dashboard(tasks):
    from datetime import date, timedelta
    today = date.today()
    week_start = (today - timedelta(days=today.weekday())).strftime("%Y-%m-%d")
    week_end = (week_start + timedelta(days=6)).strftime("%Y-%m-%d")
    
    summary = {
        "report_date": today.strftime("%Y-%m-%d"),
        "review_period": f"{week_start} to {week_end}",
        "total_tasks": len(tasks),
        "by_priority": {},
        "by_owner": {}
    }
    
    for task in tasks:
        p = task.get("priority", "medium")
        o = task.get("owner", "unknown")
        
        summary["by_priority"].setdefault(p, 0)
        summary["by_owner"].setdefault(o, 0)
        
        summary["by_priority"][p] += 1
        summary["by_owner"][o] += 1
    
    print("=" * 40)
    print("TEAMTASK STATUS DASHBOARD")
    print(f"Generated: {summary['report_date']}")
    print(f"Week Review: {summary['review_period']}")
    print("-" * 40)
    
    for p, count in sorted(summary["by_priority"].items()):
        print(f"[{p.upper()}]: {count} tasks")
        
    print("-" * 40)
    print("Owners:")
    for o, count in sorted(summary["by_owner"].items()):
        print(f"  - {o}: {count}")
    
    print("=" * 40)
