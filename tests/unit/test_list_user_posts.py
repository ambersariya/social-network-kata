from datetime import datetime
from social_network_kata.social_network_service import (
    SocialNetworkService,
)
from social_network_kata.models import Post
from social_network_kata.clock import Clock
from social_network_kata.repos import PostRepo, UserRepo
from unittest.mock import Mock


def test_can_list_user_posts():
    clock = Mock(Clock)
    timestamp = datetime.now()
    clock.now.return_value = timestamp
    post_repo = Mock(PostRepo)
    user_repo = UserRepo()
    message = "hellow hullo"
    username = "Grandrew"
    post = Post(username, message, timestamp=timestamp)
    post_repo.list_posts_by_user.return_value = [post]
    social_network = SocialNetworkService(
        clock=clock, post_repo=post_repo, user_repo=user_repo
    )

    result = social_network.list_user_posts(username=username)

    assert result == [f"{message} (0 minutes ago)"]
