from dataclasses import dataclass

@dataclass(frozen=True)
class Message:
    user: str
    message: str
