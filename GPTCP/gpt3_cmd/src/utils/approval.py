import re
import tkinter as tk
from tkinter import messagebox

# Define a list of restricted commands or keywords
RESTRICTED_KEYWORDS = [
    "rm -rf",  # Deleting files and directories
    "format",  # Formatting a disk
    "del",  # Deleting files in Windows
    "rmdir",  # Removing directories in Windows
]

def is_command_safe(command: str) -> bool:
    for keyword in RESTRICTED_KEYWORDS:
        if re.search(rf"\b{keyword}\b", command, re.IGNORECASE):
            return False
    return True

def get_command_approval(command: str) -> bool:
    """
    Opens a popup window to ask the user for command approval.
    """
    root = tk.Tk()
    root.withdraw()
    return messagebox.askyesno("Command Approval", f"Do you approve the following command?\n\n{command}")
