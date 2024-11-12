from abc import abstractmethod
from typing import Protocol

from social_network_kata.domain.post import Post


class MessageRepository(Protocol):
    @abstractmethod
    def add_post(self, user: str, post: str) -> None:
        pass
    @abstractmethod
    def get_timeline(self, user: str) -> list[Post]:
        pass
