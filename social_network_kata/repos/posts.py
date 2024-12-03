from ..models.post import Post


class PostRepo:
    def __init__(self) -> None:
        self._posts: list[Post] = []

    def add_post(self, post: Post):
        self._posts.append(post)

    def list_posts(self) -> list[Post]:
        return self._posts

    def list_posts_by_user(self, username: str) -> list[Post]:
        return [post for post in self._posts if post.username == username]
