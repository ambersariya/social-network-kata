from datetime import datetime, timedelta
from social_network_kata.social_network_service import (
    SocialNetworkService,
)
from social_network_kata.models import Post
from social_network_kata.clock import Clock
from social_network_kata.repos import PostRepo, UserRepo
from unittest.mock import Mock


def test_display_wall():
    mock_clock = Mock(Clock)
    now = datetime.now()
    post_repo = Mock(PostRepo)
    post_repo.list_posts_by_user.side_effect = [
        Post("Bob", "Hello", now - timedelta(seconds=60 * 5 + 1)),
        Post("Charlie", "What??", now - timedelta(seconds=60 * 3 + 1)),
    ]
    user_repo = Mock(UserRepo)
    user_repo.list_users_that_user_follows.return_value = ["Bob", "Charlie"]
    social_network = SocialNetworkService(
        clock=mock_clock, post_repo=post_repo, user_repo=user_repo
    )

    messages = social_network.display_wall(username="Alice")

    assert messages == [
        "Charlie - What?? (3 minutes ago)",
        "Bob - Hello (5 minutes ago)",
    ]
