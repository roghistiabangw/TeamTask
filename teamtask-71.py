# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: TeamTask
def seed_demo_data(tasks, owners):
    if not tasks: tasks = []
    if not owners: owners = ["Alice", "Bob"]
    priorities = ["High", "Medium", "Low"]
    notes_pool = ["Review needed", "Blocked by API", "In progress", "Waiting for feedback"]
    import random; random.seed(42)
    demo_tasks = []
    for i in range(5):
        owner = owners[i % len(owners)]
        priority = priorities[i % 3]
        note = notes_pool[i % len(notes_pool)]
        task_id = f"TASK-{100+i}"
        demo_task = {
            "id": task_id,
            "title": f"Demonstration Task #{i+1}",
            "owner": owner,
            "priority": priority,
            "status": "Open",
            "notes": note,
            "created_at": "2024-01-01T09:00:00"
        }
        demo_tasks.append(demo_task)
    return demo_tasks
