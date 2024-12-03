from datetime import datetime

from .clock import Clock
from .models.post import Post
from .repos.posts import PostRepo
from .repos.users import UserRepo


class SocialNetworkService:
    def __init__(self, clock: Clock, post_repo: PostRepo, user_repo: UserRepo):
        self.clock = clock
        self.post_repo = post_repo
        self.user_repo = user_repo

    def create_post(self, message: str, username: str) -> None:
        post = Post(message=message, username=username, timestamp=self.clock.now())
        self.post_repo.add_post(post)

    def list_user_posts(self, username: str) -> list[str]:
        posts = self.post_repo.list_posts_by_user(username)
        messages = []
        now = datetime.now()
        for post in posts:
            delta = now - post.timestamp
            minutes = int(delta.total_seconds() // 60)
            messages.append(f"{post.message} ({minutes} minutes ago)")
        return messages

    def follow_user(self, follower: str, username: str) -> None:
        self.user_repo.follow_user(follower, username)

    def display_wall(self, username: str):
        raise NotImplementedError
