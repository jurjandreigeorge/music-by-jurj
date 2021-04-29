"""
Contains Loading Screens and their required elements & variables
"""

import time
# GUI-related Imports
import tkinter as tk
import tkinter.ttk as ttk
from MainWindow import root


"""Required Function(s)"""

# Function used to get relative font size
# Copy-pasted from Misc module


def rule_of_3(x: float, a: float, b: float):
    """Returns the y of the following diagram
    ___________________
    | x.............a |
    | y.............b |
    | ________________|
    => y = (x * b) / a
    """
    y: float = (x * b) / a
    return y


"""Required Variables"""

# Also used in the Fonts module

# Variables used to get relative font size
SCREEN_WIDTH: int = root.winfo_screenwidth()
# 1920 is the screen width with which the app was designed
DEFAULT_SCREEN_WIDTH: int = 1920

# Relative font size variable
FONT_SIZE_34: int = int(rule_of_3(x=34, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH))
FONT_SIZE_50: int = int(rule_of_3(x=50, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH))
FONT_SIZE_100: int = int(rule_of_3(x=100, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH))

# Style element; Used by the Progressbar by default
style = ttk.Style()
style.theme_use(themename="classic")

# Represents the number of steps the app has to complete to properly launch
NUMBER_OF_STEPS: int = 7

# GUI Element; Must be here to avoid step trace error
step_labelframe = tk.LabelFrame(root, text="STEP X/N", labelanchor=tk.N, font=("Verdana", FONT_SIZE_50))

# Used to keep track of the loading step completed
step: tk.IntVar = tk.IntVar(root)
step.trace("w", lambda *args: step_labelframe.config(text=f"Step {step.get()} / {NUMBER_OF_STEPS}:"))
step.set(0)

# Used to keep track of the progressbar
progress: tk.IntVar = tk.IntVar(root)
progress.set(0)


"""GUI Elements"""


loading_menu_label = tk.Label(root, text="Loading...", font=("Courier", FONT_SIZE_100))

file_integrity_text: str = "Checking For Missing & Corrupt Files ..."
file_integrity_text_done: str = "Checked For Missing & Corrupt Files - DONE ✔"
checking_file_integrity_label = tk.Label(root, text=file_integrity_text, font=("Verdana", FONT_SIZE_34))

data_integrity_text: str = "Checking For Missing & Corrupt Data ..."
data_integrity_text_done: str = "Checked For Missing & Corrupt Data - DONE ✔"
checking_data_integrity_label = tk.Label(root, text=data_integrity_text, font=("Verdana", FONT_SIZE_34))

stats_data_text: str = "Loading Stats Data ..."
stats_data_text_done: str = "Loaded Stats Data - DONE ✔"
loading_stats_label = tk.Label(root, text=stats_data_text, font=("Verdana", FONT_SIZE_34))

gui_data_text: str = "Loading GUI Data ..."
gui_data_text_done: str = "Loaded GUI Data - DONE ✔"
loading_gui_label = tk.Label(root, text=gui_data_text, font=("Verdana", FONT_SIZE_34))

user_data_text: str = "Loading User Data ..."
user_data_text_done: str = "Loaded User Data - DONE ✔"
loading_users_label = tk.Label(root, text=user_data_text, font=("Verdana", FONT_SIZE_34))

settings_data_text: str = "Loading Settings Data ..."
settings_data_text_done: str = "Loaded Settings Data - DONE ✔"
loading_settings_label = tk.Label(root, text=settings_data_text, font=("Verdana", FONT_SIZE_34))

stats_config_text: str = "Configuring Stats GUI ..."
stats_config_text_done: str = "Configured Stats GUI - DONE ✔"
config_stats_label = tk.Label(root, text=stats_config_text, font=("Verdana", FONT_SIZE_34))

progress_bar = ttk.Progressbar(root, orient=tk.HORIZONTAL, maximum=NUMBER_OF_STEPS + 1, mode="determinate",
                               variable=progress)

"""Functions"""


def update_loading_menu():
    """Updates the Loading Menu
    """
    # Increment step by 1
    step.set(step.get() + 1)
    # Update progress_bar
    progress.set(progress.get() + 1)

    # Assign each label in its place
    label_1: tk.Label() = checking_file_integrity_label
    label_1_text: str = file_integrity_text_done

    label_2: tk.Label() = checking_data_integrity_label
    label_2_text: str = data_integrity_text_done

    label_3: tk.Label() = loading_stats_label
    label_3_text: str = stats_data_text_done

    label_4: tk.Label() = loading_gui_label
    label_4_text: str = gui_data_text_done

    label_5: tk.Label() = loading_users_label
    label_5_text: str = user_data_text_done

    label_6: tk.Label() = loading_settings_label
    label_6_text: str = settings_data_text_done

    label_7: tk.Label() = config_stats_label
    label_7_text: str = stats_config_text_done

    # Set rely
    rely: float = 0.3

    if step.get() == 1:  # Checking file integrity
        label_1.place(relheight=0.05, relwidth=0.7, relx=0.15, rely=rely)
    elif step.get() == 2:  # Checking data integrity
        label_1.config(text=label_1_text)
        rely += 0.075
        label_2.place(relheight=0.05, relwidth=0.7, relx=0.15, rely=rely)
    elif step.get() == 3:  # Loading stats data
        label_2.config(text=label_2_text)
        rely += 0.15
        label_3.place(relheight=0.05, relwidth=0.7, relx=0.15, rely=rely)
    elif step.get() == 4:  # Loading GUI data
        label_3.config(text=label_3_text)
        rely += 0.225
        label_4.place(relheight=0.05, relwidth=0.7, relx=0.15, rely=rely)
    elif step.get() == 5:  # Loading user data
        label_4.config(text=label_4_text)
        rely += 0.3
        label_5.place(relheight=0.05, relwidth=0.7, relx=0.15, rely=rely)
    elif step.get() == 6:  # Loading settings data
        label_5.config(text=label_5_text)
        rely += 0.375
        label_6.place(relheight=0.05, relwidth=0.7, relx=0.15, rely=rely)
    elif step.get() == 7:  # Configuring stats GUI elements
        label_6.config(text=label_6_text)
        rely += 0.45
        label_7.place(relheight=0.05, relwidth=0.7, relx=0.15, rely=rely)
    elif step.get() > NUMBER_OF_STEPS:
        step_labelframe.config(text="All Steps Completed!")
        label_7.config(text=label_7_text)
        root.update()
        time.sleep(1)
        return None
    root.update()
    time.sleep(.25)


def display_loading_menu():
    """Displays the Loading Menu
    """
    loading_menu_label.place(relheight=0.15, relwidth=0.8, relx=0.1, rely=0.025)
    step_labelframe.place(relheight=0.675, relwidth=0.8, relx=0.1, rely=0.175)
    progress_bar.place(relheight=0.05, relwidth=0.6, relx=0.2, rely=0.875)
