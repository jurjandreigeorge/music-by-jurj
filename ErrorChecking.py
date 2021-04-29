"""
ErrorChecking Module; Checks various data for errors
"""

import platform
import sys
from tkinter.messagebox import showerror


def check_os():
    """Determines the OS and exits if it's not compatible with the winsound module (if it's not Windows)
    """
    # Save in variable so there's no need to get it twice
    current_platform: str = platform.system()
    if current_platform == "Windows":
        return None
    showerror(title="Incompatible Operating System",
              message=f"Your operating system ({current_platform} {platform.release()}, version "
                      f"{platform.version()}) is incompatible with the sound library of this app!")
    sys.exit()
