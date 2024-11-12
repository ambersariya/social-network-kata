from dataclasses import dataclass

@dataclass(frozen=True)
class Post:
    user: str
    message: str
