from datetime import datetime
from social_network_kata.social_network_service import (
    SocialNetworkService,
)
from social_network_kata.models import Post
from social_network_kata.clock import Clock
from social_network_kata.repos import PostRepo, UserRepo
from unittest.mock import Mock


def test_user_can_post_message():
    mock_clock = Mock(Clock)
    post_repo = PostRepo()
    user_repo = UserRepo()

    social_network = SocialNetworkService(
        clock=mock_clock, post_repo=post_repo, user_repo=user_repo
    )
    timestamp = datetime.now()
    mock_clock.now.return_value = timestamp
    message = "hellow hullo"
    username = "Grandrew"

    social_network.create_post(message=message, username=username)

    assert post_repo.list_posts() == [
        Post(message=message, username=username, timestamp=timestamp)
    ]
