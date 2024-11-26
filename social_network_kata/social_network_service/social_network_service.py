from social_network_kata.clock.clock_wrapper import ClockWrapper
from social_network_kata.printer_wrapper.printer_wrapper import PrinterWrapper
from social_network_kata.input_wrapper.input_wrapper import InputWrapper


class SocialNetworkService:
    def __init__(self, clock: ClockWrapper):
        self.clock_wrapper = ClockWrapper()

    def create_post(self, time, message, username):
        raise NotImplementedError
    
    def display_wall(self, username):
        raise NotImplementedError
    