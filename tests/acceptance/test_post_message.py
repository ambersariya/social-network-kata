import pytest

from social_network_kata.domain.message import Message
from social_network_kata.domain.social_network import SocialNetwork
from social_network_kata.infrastructure.storage.inmemory_message_repository import InMemoryMessageRepository


class TestPostMessage:
    ALICE_EXPECTED_MESSAGE = "I love the weather today"

    @pytest.fixture
    def message_repository(self):
        return InMemoryMessageRepository()

    def test_user_can_post_message_to_timeline(self, message_repository):
        social_network = SocialNetwork(message_repository=message_repository)
        user = "Alice"

        social_network.post_message(user=user, message=self.ALICE_EXPECTED_MESSAGE)

        assert social_network.get_timeline(user=user) == [Message(user, self.ALICE_EXPECTED_MESSAGE)]
