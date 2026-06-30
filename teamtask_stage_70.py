# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: TeamTask
def clear_state():
    if input("Are you sure you want to reset all tasks? (y/n): ").lower() != "y":
        return
    global task_list, user_tasks
    task_list = []
    user_tasks = {}
    print("State cleared successfully.")
