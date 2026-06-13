# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: TeamTask
def dry_run_mode():
    import sys, json
    
    def get_flag(flag_name):
        return "--dry-run" in sys.argv and flag_name == "state"
    
    if get_flag("state"):
        print("[DRY-RUN] State mutation disabled. No file changes will be made.")
        return True
        
    try:
        with open(".teamtask_state.json", "r") as f:
            state = json.load(f)
    except FileNotFoundError:
        state = {"tasks": [], "owners": {}, "priorities": []}
        
    if get_flag("state"):
        print("[DRY-RUN] Would update tasks:", len(state["tasks"]))
        return False
        
    return False
