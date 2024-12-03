class UserRepo:
    def __init__(self) -> None:
        self._follows: dict[str, list[str]] = {}

    def follow_user(self, follower: str, username: str) -> None:
        if follower not in self._follows:
            self._follows[follower] = []
        self._follows[follower].append(username)

    def list_users_that_user_follows(self, follower: str) -> list[str]:
        return self._follows[follower] if follower in self._follows else []
