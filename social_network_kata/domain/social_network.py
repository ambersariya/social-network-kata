from social_network_kata.domain.message import Message
from social_network_kata.domain.message_repository import MessageRepository


class SocialNetwork:
    def __init__(self, message_repository: MessageRepository):
        self.message_repository = message_repository

    # ... rest of the class definition ...
    def post_message(self, user: str, message: str) -> None:
        self.message_repository.add_message(user, message)

    def get_timeline(self, user) -> list[Message]:
        return self.message_repository.get_timeline(user)
