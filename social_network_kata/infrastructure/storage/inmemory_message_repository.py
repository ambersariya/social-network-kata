from social_network_kata.domain.message import Message
from social_network_kata.domain.message_repository import MessageRepository


class InMemoryMessageRepository(MessageRepository):
    def __init__(self):
        self.__messages = []

    def add_message(self, user: str, message: str) -> None:
        self.__messages.append(Message(user=user, message=message))

    def get_timeline(self, user: str) -> list[Message]:
        filter_by_user = lambda message: message.user == user
        return list(filter(filter_by_user, self.__messages))
