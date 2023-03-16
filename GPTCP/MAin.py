from src.classes.language import Language
from src.classes.communication_platform import CommunicationPlatform
from src.utils.ai_interaction import interact_with_chat_website, initialize_driver
from src.utils.approval import get_command_approval
from src.utils.error_handling import request_alternative_command, execute_command
from src.utils.utils import is_command_safe, stopping_condition, split_commands
from src.settings import LOGGING_CONFIG
import logging

logging.basicConfig(**LOGGING_CONFIG)

python = Language("Python", {"print": ["echo", "echo."]})
bash = Language("Bash", {"echo.": ["\n"]})

communication_platform = CommunicationPlatform([python, bash])

driver = initialize_driver()

def main() -> None:
    """
    Main function that runs the GPT-3 CMD program.
    """
    # Initialize output variable
    output = ""

    # Loop until stopping condition is met
    while not stopping_condition(output):
        # Get input message from GPT-3
        input_message = interact_with_chat_website(driver, output)

        # Translate input message into a command for the command prompt
        command = communication_platform.translate_message(input_message, python, bash)

        # Execute command on the command prompt and capture output
        output, command_approval_required = execute_command(driver, command)

        # Send output back to GPT-3 for processing
        output_message = interact_with_chat_website(driver, output)

        # Execute computer actions based on generated output message
        result, success = execute_command(driver, output_message, command_approval_required)

        # Log any errors or warnings
        if not success:
            logging.warning(result)
        elif result:
            logging.info(result)

if __name__ == '__main__':
    main()
