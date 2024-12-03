from datetime import datetime
from social_network_kata.social_network_service import (
    SocialNetworkService,
)
from social_network_kata.clock import Clock
from social_network_kata.repos import PostRepo, UserRepo
from unittest.mock import Mock


def test_can_follow_user():
    mock_clock = Mock(Clock)
    post_repo = PostRepo()
    user_repo = UserRepo()
    social_network = SocialNetworkService(
        clock=mock_clock, post_repo=post_repo, user_repo=user_repo
    )
    timestamp = datetime.now()
    mock_clock.now.return_value = timestamp

    social_network.follow_user("Alice", "Bob")
    social_network.follow_user("Alice", "Charlie")

    assert user_repo.list_users_that_user_follows("Alice") == ["Bob", "Charlie"]
