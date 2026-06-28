# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: TeamTask
def calculate_priority_score(task: dict) -> int:
    """Calculate a numeric priority score based on owner reputation, task age, and note urgency."""
    base_score = 10
    
    # Owner contribution weight (higher for more active owners)
    owner_contributions = len(task.get("owner_tasks", []))
    if owner_contributions > 3:
        base_score += 5
    elif owner_contributions == 2:
        base_score += 2
        
    # Age penalty (older tasks get higher priority to be reviewed)
    days_old = task.get("created_at", "now")
    if isinstance(days_old, int):
        age_factor = min(10, days_old // 7)  # Cap at 1 week worth of points
        base_score += age_factor
        
    # Note urgency keywords
    notes_lower = (task.get("notes", "") or "").lower()
    urgent_keywords = ["urgent", "critical", "firefighting"]
    if any(kw in notes_lower for kw in urgent_keywords):
        base_score += 15
        
    return min(base_score, 100)
