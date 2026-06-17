# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: TeamTask
from datetime import datetime, timedelta
import re

def parse_date(date_str: str) -> datetime | None:
    """Parse date from string with clear error messages."""
    if not date_str.strip():
        return None
    formats = ["%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"Unable to parse date '{date_str}'. Supported formats: YYYY-MM-DD, DD.MM.YYYY.")

def get_week_number(dt: datetime | None = None) -> int:
    """Get ISO week number for current or given date."""
    if dt is None:
        dt = datetime.now()
    return dt.isocalendar()[1]

def parse_duration(duration_str: str) -> timedelta:
    """Parse duration string like '2d', '3h 30m' into timedelta."""
    pattern = r"(\d+)\s*(d|h|m|w)?\s*([^\d])?"
    match = re.search(pattern, duration_str.strip(), re.IGNORECASE)
    if not match:
        raise ValueError(f"Invalid duration format: '{duration_str}'")
    
    value = int(match.group(1))
    unit = (match.group(2) or "").lower()
    extra = (match.group(3) or "").strip().lower()
    
    multipliers = {"d": 86400, "h": 3600, "m": 60, "w": 604800}
    seconds = value * multipliers.get(unit, 1)
    
    if extra:
        raise ValueError(f"Unsupported character in duration: '{extra}'")
        
    return timedelta(seconds=seconds)
