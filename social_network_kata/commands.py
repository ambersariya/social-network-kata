from dataclasses import dataclass

from tatsu import parse as _parse

__all__ = [
    "PostMessageCmd",
    "FollowUserCmd",
    "DisplayWallCmd",
    "ListUserPostsCmd",
    "parse_input",
]


@dataclass
class PostMessageCmd:
    username: str
    message: str


@dataclass
class FollowUserCmd:
    follower: str
    username: str


@dataclass
class DisplayWallCmd:
    username: str


@dataclass
class ListUserPostsCmd:
    username: str


Command = PostMessageCmd | FollowUserCmd | DisplayWallCmd | ListUserPostsCmd

_GRAMMAR = """
    start = expression $ ;

    expression
        =
        | username '->' message
        | username 'wall'
        | username 'follows' username
        | username
        ;

    username = /[A-z0-9]+/ ;
    message = /.+/ ;
"""


def parse_input(cmd: str) -> Command:
    ast = _parse(_GRAMMAR, cmd)
    ast = (ast,) if not isinstance(ast, tuple) else ast

    match ast:
        case (username, "->", message):
            return PostMessageCmd(username, message)
        case (username, "wall"):
            return DisplayWallCmd(username)
        case (follower, "follows", username):
            return FollowUserCmd(follower, username)
        case (username,):
            return ListUserPostsCmd(username)
        case _:
            raise Exception("Input not valid command")
