from social_network_kata.domain.post import Post
from social_network_kata.domain.message_repository import MessageRepository


class SocialNetwork:
    def __init__(self, message_repository: MessageRepository):
        self.message_repository = message_repository

    # ... rest of the class definition ...
    def create_post(self, user: str, post: str) -> None:
        self.message_repository.add_post(user, post)

    def get_timeline(self, user) -> list[Post]:
        return self.message_repository.get_timeline(user)
