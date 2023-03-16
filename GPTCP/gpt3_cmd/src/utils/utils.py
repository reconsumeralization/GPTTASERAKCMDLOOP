import re
from typing import List

# Define a list of restricted commands or keywords
RESTRICTED_KEYWORDS = [
    "rm -rf",  # Deleting files and directories
    "format",  # Formatting a disk
    "del",  # Deleting files in Windows
    "rmdir",  # Removing directories in Windows
]

def is_command_safe(command: str) -> bool:
    """
    Checks if a command contains any restricted commands or keywords.
    """
    for keyword in RESTRICTED_KEYWORDS:
        if re.search(rf"\b{keyword}\b", command, re.IGNORECASE):
            return False
    return True

def stopping_condition(output: str) -> bool:
    """
    Defines the stopping condition for the main loop.
    """
    return "done" in output.lower()

def split_commands(action_text: str) -> List[str]:
    """
    Splits action text into individual commands.
    """
    return action_text.split(';')
