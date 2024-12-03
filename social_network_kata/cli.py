from .commands import (
    PostMessageCmd,
    ListUserPostsCmd,
    FollowUserCmd,
    parse_input,
)
from .printer import Printer
from .input import Input
from .social_network_service import SocialNetworkService


class SocialNetworkCli:
    def __init__(
        self,
        social_network_service: SocialNetworkService,
        printer: Printer,
        input: Input,
    ):
        self.social_network_service = social_network_service
        self.printer = printer
        self.input = input

    def run(self) -> None:
        self.printer.output("Welcome to social network. Please type a command.")

        while True:
            try:
                input_str = self.input.read_input()
            except KeyboardInterrupt:
                self.printer.output("Leaving the social network.")
                break

            cmd = parse_input(input_str)

            # TODO: command pattern - add .execute() method to commands?
            match cmd:
                case PostMessageCmd(username, message):
                    self.social_network_service.create_post(message, username)

                case ListUserPostsCmd(username):
                    messages = self.social_network_service.list_user_posts(username)
                    for message in messages:
                        self.printer.output(message)

                case FollowUserCmd(follower, username):
                    self.social_network_service.follow_user(follower, username)
