import unittest
from unittest.mock import Mock, call
from social_network_kata.cli import SocialNetworkCli
from social_network_kata.social_network_service import (
    SocialNetworkService,
)
from social_network_kata.printer import Printer
from social_network_kata.input import Input


class TestSocialNetworkCLI(unittest.TestCase):
    def test_cli_start_service_has_welcome_message(self):
        social_network_service = Mock(SocialNetworkService)
        printer = Mock(Printer)
        input = Mock(Input)

        cli = SocialNetworkCli(
            social_network_service=social_network_service,
            printer=printer,
            input=input,
        )
        input.read_input.side_effect = [
            "Alice -> I love the weather today",
            KeyboardInterrupt,
        ]

        cli.run()

        expected_calls = [
            call("Welcome to social network. Please type a command."),
            call("Leaving the social network."),
        ]

        printer.output.assert_has_calls(expected_calls)

    def test_cli_takes_input_creates_post(self):
        mock_social_network_service = Mock(SocialNetworkService)
        mock_printer_wrapper = Mock(Printer)
        mock_input_wrapper = Mock(Input)

        cli = SocialNetworkCli(
            social_network_service=mock_social_network_service,
            printer=mock_printer_wrapper,
            input=mock_input_wrapper,
        )
        username = "Alice"
        message = "I love the weather today"
        mock_input_wrapper.read_input.side_effect = [
            "Alice -> I love the weather today",
            KeyboardInterrupt,
        ]

        cli.run()

        mock_social_network_service.create_post.assert_called_once_with(
            message, username
        )

    # def test_cli_output_from_user_inputs(self):
