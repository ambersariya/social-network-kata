import datetime
from unittest.mock import Mock, call

from social_network_kata.clock import Clock
from social_network_kata.printer import Printer
from social_network_kata.input import Input
from social_network_kata.cli import SocialNetworkCli
from social_network_kata.social_network_service import SocialNetworkService
from social_network_kata.repos import PostRepo, UserRepo


class TestAcceptance:
    def test_user_can_post_message_to_timeline(self):
        clock = Mock(Clock)
        post_repo = PostRepo()
        user_repo = UserRepo()
        time_change = datetime.timedelta(minutes=5)
        alice_is_posting_timestamp = datetime.datetime.now() - datetime.timedelta(
            seconds=60 * 5 + 2
        )
        bob_is_reading_timestamp = alice_is_posting_timestamp + time_change
        clock.now.side_effect = [
            alice_is_posting_timestamp,
            bob_is_reading_timestamp,
        ]
        printer = Mock(Printer)
        input = Mock(Input)
        input.read_input.side_effect = [
            "Alice -> I love the weather today",
            "Alice",
            KeyboardInterrupt,
        ]
        cli = SocialNetworkCli(
            SocialNetworkService(clock=clock, post_repo=post_repo, user_repo=user_repo),
            printer,
            input,
        )

        cli.run()

        printer.output.assert_has_calls(
            [
                call("Welcome to social network. Please type a command."),
                call("I love the weather today (5 minutes ago)"),
                call("Leaving the social network."),
            ]
        )

    def test_user_can_follow_users_and_view_wall(self):
        clock = Mock(Clock)
        post_repo = PostRepo()
        user_repo = UserRepo()
        now = datetime.datetime.now()
        alice_posting_timestamp = now - datetime.timedelta(seconds=60 * 20 + 1)
        bob_posting_timestamp = now - datetime.timedelta(seconds=60 * 5 + 2)
        charlie_posting_timestamp = now
        clock.now.side_effect = [
            alice_posting_timestamp,
            bob_posting_timestamp,
            charlie_posting_timestamp,
            now,
        ]
        printer = Mock(Printer)
        input = Mock(Input)
        input.read_input.side_effect = [
            "Alice -> I love the weather today",
            "Charlie follows Alice",
            "Bob -> Me too",
            "Charlie follows Bob",
            "Charlie -> Bob I'm afraid I don't give a fuck.",
            "Charlie wall",
            KeyboardInterrupt,
        ]
        cli = SocialNetworkCli(
            SocialNetworkService(clock=clock, post_repo=post_repo, user_repo=user_repo),
            printer,
            input,
        )

        cli.run()

        printer.output.assert_has_calls(
            [
                call("Welcome to social network. Please type a command."),
                call("Charlie - Bob I'm afraid I don't give a fuck. (0 minutes ago)"),
                call("Bob - Me too (5 minutes ago)"),
                call("Alice - I love the weather today (20 minutes ago)"),
                call("Leaving the social network."),
            ]
        )
