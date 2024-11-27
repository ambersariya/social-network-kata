from social_network_kata.printer_wrapper.printer_wrapper import PrinterWrapper
from social_network_kata.input_wrapper.input_wrapper import InputWrapper
from social_network_kata.social_network_service.social_network_service import SocialNetworkService
from social_network_kata.clock.clock_wrapper import ClockWrapper

class SocialNetworkCli:

    def __init__(self, social_network_service: SocialNetworkService, print_wrapper: PrinterWrapper, input_wrapper: InputWrapper):
        self.social_network_service = social_network_service
        self.print_wrapper = print_wrapper
        self.input_wrapper = input_wrapper
    
    def run(self) -> None:
        self.print_wrapper.output("Welcome to social network. Please type a command.")
        
        while True:
            command = self.input_wrapper.read_input()


            if command.lower() == "exit":
                self.print_wrapper.output("Leaving the social network.")
                break

            # currently only assuming perfect commands and splitting on -> e.g: input1 -> input2
            create_post_cmd = command.split("->")

            if len(create_post_cmd) == 2:
                username, message = create_post_cmd
                self.social_network_service.create_post(message, username)
            else:
                return



"""
User -> Message : create_post

str.split(' -> ')

user = regex(allowed as a user)
message = regex(allowed as a post)
"""
