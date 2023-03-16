import os

# Logging settings
LOGGING_CONFIG = {
    'filename': 'gpt3_cmd.log',
    'level': 'INFO'
}

# WebDriver settings
WEBDRIVER_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'webdriver', 'geckodriver')
CHAT_WEBSITE_URL = "https://chat.openai.com/chat"

# Restricted keywords
RESTRICTED_KEYWORDS = [
    "rm -rf",  # Deleting files and directories
    "format",  # Formatting a disk
    "del",     # Deleting files in Windows
    "rmdir",   # Removing directories in Windows
]
