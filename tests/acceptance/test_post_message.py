import subprocess
import unittest
import datetime
from unittest.mock import Mock

from social_network_kata.clock.clock_wrapper import ClockWrapper
from social_network_kata.printer_wrapper.printer_wrapper import PrinterWrapper
from social_network_kata.input_wrapper.input_wrapper import InputWrapper
from social_network_kata.social_network_cli.social_network_cli import SocialNetworkCli
from social_network_kata.social_network_service.social_network_service import SocialNetworkService

class TestPostMessage:
    def test_user_can_post_message_to_timeline(self):
        mock_clock_wrapper = Mock(ClockWrapper)
        time_change = datetime.timedelta(minutes=5)
        alice_is_posting_timestamp = datetime.datetime(
            year=2021, month=8, day=22, hour=11, minute=2, second=5
        )
        bob_is_reading_timestamp = alice_is_posting_timestamp + time_change
        mock_clock_wrapper.clock.side_effect = [
            alice_is_posting_timestamp, 
            bob_is_reading_timestamp
        ] 
        mock_printer_wrapper = Mock(PrinterWrapper)
        mock_input_wrapper = Mock(InputWrapper)
        mock_input_wrapper.read_input.side_effect = [
            "Alice -> I love the weather today",
            "Alice"
        ]
        cli = SocialNetworkCli(
            SocialNetworkService(mock_clock_wrapper), 
            mock_printer_wrapper, 
            mock_input_wrapper
        ) 

        cli.run()

        mock_printer_wrapper.print.assert_called_once_with("I love the weather today (5 minutes ago)")

    # def test_user_can_read_post_by_id(self):
    #     pass
