import pytest

from social_network_kata.domain.message_repository import MessageRepository
from social_network_kata.domain.social_network import SocialNetwork


class TestSocialNetwork:
    @pytest.fixture
    def message_repository(self, mocker):
        return mocker.Mock(MessageRepository)

    def test_post_message(self, message_repository):
        social_network = SocialNetwork(message_repository=message_repository)
        user = "Alice"
        message = "I love the weather today"

        social_network.create_post(user=user, post=message)

        message_repository.add_post.assert_called_once_with(user, message)

    def test_get_timeline(self, message_repository):
        message_repository.get_timeline.return_value = ["I love the weather today"]
        social_network = SocialNetwork(message_repository=message_repository)
        user = "Alice"

        social_network.get_timeline(user=user)

        message_repository.get_timeline.assert_called_once_with(user)
        assert social_network.get_timeline(user=user) == ["I love the weather today"]
