from abc import abstractmethod
from typing import Protocol

from social_network_kata.domain.message import Message


class MessageRepository(Protocol):
    @abstractmethod
    def add_message(self, user, message) -> None:
        pass
    @abstractmethod
    def get_timeline(self, user) -> list[Message]:
        pass
