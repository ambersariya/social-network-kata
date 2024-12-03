from social_network_kata.commands import parse_input
from social_network_kata.commands import (
    PostMessageCmd,
    FollowUserCmd,
    DisplayWallCmd,
    ListUserPostsCmd,
)


def test_can_parse_post_command():
    parsed_command = parse_input("Alice -> I love the weather today")

    assert parsed_command == PostMessageCmd(
        username="Alice", message="I love the weather today"
    )


def test_can_parse_follow_user_command():
    parsed_command = parse_input("Charlie follows Alice")

    assert parsed_command == FollowUserCmd(follower="Charlie", username="Alice")


def test_can_parse_display_wall_command():
    parsed_command = parse_input("Charlie wall")

    assert parsed_command == DisplayWallCmd(username="Charlie")


def test_can_parse_list_user_posts_command():
    parsed_command = parse_input("Charlie")

    assert parsed_command == ListUserPostsCmd(username="Charlie")
