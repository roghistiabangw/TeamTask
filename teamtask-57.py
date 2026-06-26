# === Stage 57: Add structured result objects for command handlers ===
# Project: TeamTask
class TaskResult(BaseModel):
    task_id: int
    status: Literal["created", "updated", "deleted"]
    message: str
    owner_name: Optional[str] = None
    priority_level: Optional[int] = None
    review_date: Optional[datetime.date] = None
