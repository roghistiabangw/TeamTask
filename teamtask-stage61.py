# === Stage 61: Add performance timing for core list and search operations ===
# Project: TeamTask
import time
from functools import wraps

def timed_operation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"[{func.__name__}] took {elapsed:.2f}ms")
        return result
    return wrapper

@timed_operation
def filter_tasks_by_priority(tasks: list, priority: str):
    return [t for t in tasks if t.get("priority") == priority]

@timed_operation
def find_task_by_owner(tasks: list, owner_name: str):
    return next((t for t in tasks if t.get("owner") == owner_name), None)
