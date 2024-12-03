from dataclasses import dataclass
from datetime import datetime

__all__ = ["Post"]


@dataclass
class Post:
    username: str
    message: str
    timestamp: datetime
