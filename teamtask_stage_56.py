# === Stage 56: Add compact error classes for domain failures ===
# Project: TeamTask
class TaskError(Exception): pass
class OwnerNotFoundError(TaskError): pass
class PriorityInvalidError(TaskError): pass
class NoteValidationError(TaskError): pass
class ReviewCycleSkippedError(TaskError): pass
class WeeklyReviewFailedError(TaskError): pass
class TeamTaskException(RuntimeError): pass
