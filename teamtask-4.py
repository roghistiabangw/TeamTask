# === Stage 4: Implement create operations for the primary records ===
# Project: TeamTask
def create_task(task_id, title, owner, priority, notes):
    task = {
        "id": task_id,
        "title": title,
        "owner": owner,
        "priority": priority,
        "notes": notes,
        "status": "open",
        "created_at": datetime.now().isoformat()
    }
    tasks[task_id] = task
    return task

def create_member(member_id, name, role):
    member = {
        "id": member_id,
        "name": name,
        "role": role
    }
    members[member_id] = member
    return member

def create_review(review_id, date, summary):
    review = {
        "id": review_id,
        "date": date,
        "summary": summary,
        "status": "draft"
    }
    reviews[review_id] = review
    return review
