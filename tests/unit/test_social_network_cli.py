import unittest
from unittest.mock import Mock, MagicMock
from social_network_kata.social_network_cli.social_network_cli import SocialNetworkCli
from social_network_kata.social_network_service.social_network_service import SocialNetworkService
from social_network_kata.printer_wrapper.printer_wrapper import PrinterWrapper
from social_network_kata.input_wrapper.input_wrapper import InputWrapper

class TestSocialNetworkCLI(unittest.TestCase):

    def test_cli_start_service_has_welcome_message(self):
        """
        given we receive input from a user
        we expect a string output
        """
        mock_social_network_service = Mock(SocialNetworkService)
        mock_printer_wrapper = Mock(PrinterWrapper)
        mock_input_wrapper = Mock(InputWrapper)

        cli = SocialNetworkCli(social_network_service=mock_social_network_service, print_wrapper=mock_printer_wrapper, input_wrapper=mock_input_wrapper)
        mock_input_wrapper.read_input.side_effect = ["Alice-> I love the weather today", "exit"]

        cli.run()

        expected_calls = [
            unittest.mock.call("Welcome to social network. Please type a command."),
            unittest.mock.call("Leaving the social network.")
        ]
        
        mock_printer_wrapper.output.assert_has_calls(expected_calls)


    def test_cli_takes_input_creates_post(self):
        mock_social_network_service = Mock(SocialNetworkService)
        mock_printer_wrapper = Mock(PrinterWrapper)
        mock_input_wrapper = Mock(InputWrapper)

        cli = SocialNetworkCli(social_network_service=mock_social_network_service, print_wrapper=mock_printer_wrapper, input_wrapper=mock_input_wrapper)
        username = "Alice"
        message = " I love the weather today"
        mock_input_wrapper.read_input.side_effect = ["Alice-> I love the weather today", "exit"]

        cli.run()
        # "{username} -> {message}"
        mock_social_network_service.create_post.assert_called_once_with(message, username)
        


    # def test_cli_output_from_user_inputs(self):
