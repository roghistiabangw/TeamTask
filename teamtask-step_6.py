# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: TeamTask
def delete_task(task_id, confirm_flag):
    if not confirm_flag:
        print(f"Task #{task_id} deletion cancelled by user.")
        return False
    
    try:
        task = tasks[task_id]
        if task:
            del tasks[task_id]
            print(f"Task #{task_id} successfully deleted.")
            return True
        else:
            print(f"Task #{task_id} not found.")
            return False
    except KeyError:
        print(f"Error: Task ID '{task_id}' does not exist in the database.")
        return False
