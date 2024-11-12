from abc import abstractmethod
from typing import Protocol

from social_network_kata.domain.post import Post


class MessageRepository(Protocol):
    @abstractmethod
    def add_post(self, user, message) -> None:
        pass
    @abstractmethod
    def get_timeline(self, user) -> list[Post]:
        pass
