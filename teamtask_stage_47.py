# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: TeamTask
from datetime import date, timedelta
import random

def run_demo():
    tasks = [
        {"id": 1, "owner": "Alice", "priority": "High", "status": "Open"},
        {"id": 2, "owner": "Bob", "priority": "Medium", "status": "In Progress"},
        {"id": 3, "owner": "Charlie", "priority": "Low", "status": "Done"}
    ]
    
    print(f"=== Weekly Review: {date.today()} ===")
    for task in tasks:
        if task["status"] == "Open":
            print(f"[{task['id']}] {task['owner']} | Prio: {task['priority']} -> Action Required")
        
    # Simulate random status updates mimicking human workflow
    for i, task in enumerate(tasks):
        if random.random() > 0.5 and task["status"] != "Done":
            new_status = ["Open", "In Progress"][random.randint(0,1)]
            tasks[i]["status"] = new_status
            print(f"[{task['id']}] Status updated to {new_status}")

    # Simulate adding a note
    if tasks[0]["owner"] == "Alice":
        print("Note: Alice reminded team about the deadline.")
        
    print("\nDemo completed successfully.")
