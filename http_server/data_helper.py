from datetime import datetime


def get_timestamp() -> str:
    """Get current date and time in iso format"""
    return datetime.now().isoformat()
