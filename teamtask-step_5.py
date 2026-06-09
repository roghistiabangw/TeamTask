# === Stage 5: Implement update operations with clear handling for missing records ===
# Project: TeamTask
def update_task(task_id, updates):
    tasks = load_tasks()
    if task_id not in tasks:
        print(f"Error: Task {task_id} not found.")
        return False
    for key, value in updates.items():
        if key in ["id", "created_at"]:
            continue
        tasks[task_id][key] = value
    save_tasks(tasks)
    print(f"Task {task_id} updated successfully.")
    return True

def delete_task(task_id):
    tasks = load_tasks()
    if task_id not in tasks:
        print(f"Error: Task {task_id} not found.")
        return False
    del tasks[task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted successfully.")
    return True

def handle_missing_record(task_id, action):
    if task_id not in load_tasks():
        print(f"Warning: Task {task_id} does not exist. Operation '{action}' skipped.")
        return False
    return True
