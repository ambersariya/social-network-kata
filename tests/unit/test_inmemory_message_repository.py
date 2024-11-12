from social_network_kata.domain.message import Message
from social_network_kata.infrastructure.storage.inmemory_message_repository import InMemoryMessageRepository


class TestInMemoryMessageRepository:
    def test_get_timeline_for_a_user(self):
        user = "bob"
        message = "Hello world"
        message_repository = InMemoryMessageRepository()

        message_repository.add_message(user=user, message=message)

        assert message_repository.get_timeline(user=user) == [
            Message(user=user, message="Hello world")
        ]
