from social_network_kata.domain.post import Post
from social_network_kata.infrastructure.storage.inmemory_message_repository import InMemoryMessageRepository


class TestInMemoryMessageRepository:
    def test_get_timeline_for_a_user(self):
        user = "bob"
        message = "Hello world"
        message_repository = InMemoryMessageRepository()

        message_repository.add_post(user=user, post=message)

        assert message_repository.get_timeline(user=user) == [
            Post(user=user, message="Hello world")
        ]
