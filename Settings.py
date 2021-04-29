"""
Settings Module; Consists of settings-related variables and functions
"""


# Imports
import json
import re
import os
import typing
import User
import Stats
import Colors
import Sounds
# GUI-related Imports
from MainWindow import root
from tkinter import StringVar, BooleanVar, Event
from tkinter.constants import DISABLED, NORMAL
from tkinter.colorchooser import askcolor


"""GUI Variables"""

# Setting data files paths
PRESET_SETTINGS_JSON_PATH: str = os.path.join(os.getcwd(), "Dependencies", "Settings", "PresetSettings.json")
REMEMBER_SETTINGS_VALUE_TXT_PATH: str = os.path.join(os.getcwd(),
                                                     "Dependencies", "Settings", "RememberSettingsValue.txt")

# Determines whether the app is currently displaying the Settings menu or not
is_in_settings_menu: BooleanVar = BooleanVar(root)
is_in_settings_menu.set(False)

# Find the trace methods for these variables in the GUI module


# Default GUI colors
default_background_color: str = "grey94"
default_text_color: str = "black"
default_buttons_color: str = "grey94"
default_button_text_color: str = "black"
default_invalid_text_color: str = "red"
# Default GUI sound option
default_gui_sound_option: bool = True


# Factors for getting lighter/darker (tinted/shaded) color variations
TINT_FACTOR: float = 1.2
SHADE_FACTOR: float = .9

# Hex standard colors variables
hexadecimal_grey: str = "#a0a0a0"
hexadecimal_white: str = "#ffffff"

# Other standard system-sourced color options
system_button_face: str = "SystemButtonFace"
system_disabled_text: str = "SystemDisabledText"
system_window_text: str = "SystemWindowText"
system_highlight: str = "SystemHighlight"
system_window: str = "SystemWindow"
system_scrollbar: str = "SystemScrollbar"


# Specific default GUI colors
default_active_background_color: str = system_button_face

default_disabled_text_color: str = system_disabled_text

default_active_foreground_color: str = system_window_text

default_optionmenu_active_background_color: str = system_button_face

default_menu_active_text_color: str = hexadecimal_white
default_menu_active_background_color: str = system_highlight

default_radiobutton_active_text_color: str = system_window

default_checkbutton_active_text_color: str = system_window

default_listbox_background_color: str = hexadecimal_white
default_listbox_active_color: str = system_highlight
default_listbox_logged_user_composition_background_color: str = "snow2"

default_text_select_text_color: str = hexadecimal_white
default_text_background_color: str = hexadecimal_white
default_text_select_background_color: str = system_highlight

default_notebook_tab_background_color: str = hexadecimal_white
default_notebook_tab_selected_background_color: str = hexadecimal_white

default_button_select_color: str = hexadecimal_white

default_entry_background_color: str = hexadecimal_white
default_entry_highlight_background_color: str = system_highlight
default_entry_highlight_text_color: str = hexadecimal_white

default_progress_bar_background_color: str = "SteelBlue"
default_progress_bar_trough_color: str = "#c3c3c3"

default_combobox_background_color: str = "#d9d9d9"
default_combobox_field_background_color: str = hexadecimal_white
default_combobox_select_background_color: str = system_highlight
default_combobox_select_text_color: str = hexadecimal_white
default_combobox_menu_background_color: str = hexadecimal_white
default_combobox_menu_select_background_color: str = system_highlight

default_slider_trough_color: str = system_scrollbar


# Used to set the "choose background color" option menu option
chosen_background_color: StringVar = StringVar(root)
chosen_background_color.set(default_background_color)
# Used to store the last "background color" setting
last_background_color_setting: str = chosen_background_color.get()


# Used to set the "choose text color" option menu option
chosen_text_color: StringVar = StringVar(root)
chosen_text_color.set(default_text_color)
# Used to store the last "text color" setting
last_text_color_setting: str = chosen_text_color.get()


# Used to set the "choose button color" option menu option
chosen_button_color: StringVar = StringVar(root)
chosen_button_color.set(default_buttons_color)
# Used to store the last "button color" setting
last_button_color_setting: str = chosen_button_color.get()


# Used to set the "choose buttons' text color" option menu option
chosen_button_text_color: StringVar = StringVar(root)
chosen_button_text_color.set(default_button_text_color)
# Used to store the last "buttons' text color" setting
last_button_text_color_setting: str = chosen_button_text_color.get()


# Used to set the "invalid text color" option menu option
chosen_invalid_text_color: StringVar = StringVar(root)
chosen_invalid_text_color.set(default_invalid_text_color)
# Used to store the last "invalid text color" setting
last_invalid_text_color_setting: str = chosen_invalid_text_color.get()


# Used to set the "GUI sound" setting
chosen_gui_sound_setting: BooleanVar = BooleanVar(root)
chosen_gui_sound_setting.set(True)
# Used to store the last "GUI sound" setting
last_gui_sound_setting: bool = chosen_gui_sound_setting.get()


# Used to set the "remember settings" setting
remember_settings_setting: StringVar = StringVar(root)
remember_settings_setting.set("Default")
# Used to store the last "remember settings" setting
last_remember_settings_setting: str = remember_settings_setting.get()


# Represents the remember_settings_setting value read from RememberSettingsValue.txt
read_remember_settings: str = "Default"
# Dict of preset app settings; starts out with default settings
preset_settings: dict = {
    "Background Color": default_background_color,
    "Text Color": default_text_color,
    "Buttons' Color": default_buttons_color,
    "Buttons' Text Color": default_button_text_color,
    "Invalid Text Color": default_invalid_text_color,
    "GUI Sound": "On"
}


"""Functions"""


def set_settings_vars(target: str):
    """Sets settings variables depending on the target parameter
    """
    if target == "User":
        chosen_background_color.set(User.logged_in_user["Settings"]["Background Color"])
        chosen_text_color.set(User.logged_in_user["Settings"]["Text Color"])
        chosen_button_color.set(User.logged_in_user["Settings"]["Buttons' Color"])
        chosen_button_text_color.set(User.logged_in_user["Settings"]["Buttons' Text Color"])
        chosen_invalid_text_color.set(User.logged_in_user["Settings"]["Invalid Text Color"])
        chosen_gui_sound_setting.set(User.logged_in_user["Settings"]["GUI Sound"])
    elif target == "Preset":
        chosen_background_color.set(preset_settings["Background Color"])
        chosen_text_color.set(preset_settings["Text Color"])
        chosen_button_color.set(preset_settings["Buttons' Color"])
        chosen_button_text_color.set(preset_settings["Buttons' Text Color"])
        chosen_invalid_text_color.set(preset_settings["Invalid Text Color"])
        chosen_gui_sound_setting.set(preset_settings["GUI Sound"])
    else:
        chosen_background_color.set(default_background_color)
        chosen_text_color.set(default_text_color)
        chosen_button_color.set(default_buttons_color)
        chosen_button_text_color.set(default_button_text_color)
        chosen_invalid_text_color.set(default_invalid_text_color)
        chosen_gui_sound_setting.set(True)


def update_preset_setting_dict(target: str, setting_value: str):
    """Updates the app_settings dict with the current setting"""
    global preset_settings
    preset_settings.update({target: setting_value})


def set_initial_settings():
    """Sets initial app settings depending on the read remember_settings value
    Call only after reading User data
    """
    if read_remember_settings == "Preset":
        set_settings_vars(target="Preset")
        remember_settings_setting.set("Preset")
    elif User.is_logged_in and read_remember_settings == "User":
        set_settings_vars(target="User")
        remember_settings_setting.set("User")


def read_remember_settings_value():
    """Reads the remember_settings value form .txt file
    """
    global read_remember_settings
    with open(file=REMEMBER_SETTINGS_VALUE_TXT_PATH, encoding="utf-8") as remember_settings_file:
        read_remember_settings = remember_settings_file.read()


def read_preset_settings():
    """Reads the preset settings from file
    """
    global preset_settings
    with open(file=PRESET_SETTINGS_JSON_PATH, encoding="utf-8") as file:
        preset_settings = json.load(file)


def write_remember_settings_value():
    """Writes the remember_settings value in .txt file
    """
    with open(file=REMEMBER_SETTINGS_VALUE_TXT_PATH, mode="w", encoding="utf-8") as remember_settings_file:
        remember_settings_file.write(remember_settings_setting.get())


def write_preset_settings():
    """Writes preset settings in .json file
    """
    with open(file=PRESET_SETTINGS_JSON_PATH, mode="w", encoding="utf-8") as file:
        json.dump(obj=preset_settings, fp=file, indent=2)


def setting_variable_trace_wrapper(setting_value: typing.Union[str, bool], target: str):
    """To be used when tracing setting variables in the GUI module
    """
    if target not in ("GUI Sound", "Remember Settings"):
        config_default_setting_buttons(setting_value=setting_value, target=target)

    if target == "Remember Settings":
        update_last_used_setting(target=target, setting=setting_value)
        return None

    if User.is_logged_in and remember_settings_setting.get() == "User":
        User.update_logged_user_setting(target=target, setting_value=setting_value)

    if remember_settings_setting.get() == "Preset":
        update_preset_setting_dict(target=target, setting_value=setting_value)

    # Last used setting
    update_last_used_setting(target=target, setting=setting_value)

    # Change proper GUI elements
    if target != "GUI Sound":
        from GUI import change_gui_elements
        change_gui_elements(target=target, setting_value=setting_value)


def change_setting_with_event(event: Event):
    """Changes the Remember Settings setting option based on the event received
    """
    if not is_in_settings_menu.get():
        return None
    # Preset
    if event.keysym.lower() == "p" and remember_settings_setting.get() != "Preset":
        Sounds.play_gui_sound(sound_file_path=Sounds.CLEAR_SOUND_PATH)
        remember_settings_setting.set("Preset")
        set_settings_vars(target="Preset")
    # User
    elif event.keysym.lower() == "u" and remember_settings_setting.get() != "User" and User.is_logged_in:
        Sounds.play_gui_sound(sound_file_path=Sounds.CLEAR_SOUND_PATH)
        remember_settings_setting.set("User")
        set_settings_vars(target="User")
    # Default
    elif event.keysym.lower() == "d" and not is_all_settings_default():
        Sounds.play_gui_sound(sound_file_path=Sounds.CLEAR_SOUND_PATH)
        remember_settings_setting.set("Default")
        set_settings_vars(target="Default")


def is_all_settings_default():
    """Returns boolean representing if all selected settings are default settings or not
    """
    if chosen_text_color.get() != default_text_color:
        return False
    if chosen_background_color.get() != default_background_color:
        return False
    if chosen_button_color.get() != default_buttons_color:
        return False
    if chosen_button_text_color.get() != default_button_text_color:
        return False
    if chosen_invalid_text_color.get() != default_invalid_text_color:
        return False
    if chosen_gui_sound_setting.get() != default_gui_sound_option:
        return False
    if remember_settings_setting.get() != "Default":
        return False
    return True


def config_default_setting_buttons(setting_value: str, target: str):
    """Disables or Re-enables Default settings buttons from the Settings Menu
    """
    from GUI import default_background_color_button, default_text_color_button, \
        default_button_color_button, default_buttons_text_color_button, \
        default_invalid_text_color_button
    # Disable Default buttons if setting is default
    if target == "Background Color":
        default_background_color_button.config(state=DISABLED if setting_value == default_background_color else NORMAL)
    if target == "Text Color":
        default_text_color_button.config(state=DISABLED if setting_value == default_text_color else NORMAL)
    if target == "Buttons' Color":
        default_button_color_button.config(state=DISABLED if setting_value == default_buttons_color else NORMAL)
    if target == "Buttons' Text Color":
        default_buttons_text_color_button.\
            config(state=DISABLED if setting_value == default_button_text_color else NORMAL)
    if target == "Invalid Text Color":
        default_invalid_text_color_button.\
            config(state=DISABLED if setting_value == default_invalid_text_color else NORMAL)


def get_custom_color(target: str, setting_value: StringVar):
    """Opens up the color chooser and returns the selected color
    """
    # Ask color
    returned_color: list = askcolor(title=f"Select Custom {target}", initialcolor=setting_value.get(),
                                    parent=root)

    # If color not returned
    if returned_color == (None, None):
        return None

    current_hex: str = ""
    # Get hex code of currently set color
    for color_bundle in Colors.COLORS_WITH_HEX:
        if color_bundle[1] == setting_value.get():
            current_hex = color_bundle[0].lower()
            break
    # If same color already set, return None
    if current_hex == returned_color[1]:
        return None
    # If different returned color, try searching its name
    for color_bundle in Colors.COLORS_WITH_HEX:
        # If hex codes match, set variable to found color name
        if returned_color[1] == color_bundle[0].lower():
            setting_value.set(color_bundle[1])
            return None
    setting_value.set(returned_color[1])


def get_color_variation(color: str, factor: float):
    """Returns a hex color code representing a lighter (tinted) or darker (shaded) variation of the given color,
    depending on the given factor
    Factor > 1 => Tinted color
    Factor < 1 => Shaded color
    """

    def hex_to_rgb(hex_color: str):
        """Converts a hexadecimal color code to a tuple of integers corresponding to its RGB components
        """
        # Taken from https://stackoverflow.com/a/29643643/15454571
        return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))

    def rgb_to_hex(r: int, g: int, b: int):
        """Converts an RGB tuple of integers to its corresponding hexadecimal color code
        """
        # Taken from https://stackoverflow.com/a/43572620/15454571
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    def redistribute_rgb(r: float, g: float, b: float):
        """Redistributes given RGB color tuple to keep it in the RGB range (0 - 255)
        """
        # Taken from https://stackoverflow.com/a/141943/15454571
        threshold: float = 255.999
        m: float = max(r, g, b)
        if m <= threshold:
            return int(r), int(g), int(b)
        total: float = r + g + b
        if total >= 3 * threshold:
            return int(threshold), int(threshold), int(threshold)
        x: float = (3 * threshold - total) / (3 * m - total)
        gray: float = threshold - x * m
        return int(gray + x * r), int(gray + x * g), int(gray + x * b)

    # Check if given color str is valid hex color code
    # Regex expression taken from https://stackoverflow.com/a/30241753/15454571
    compiled_expression: re.Pattern = re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$')
    match: re.Match = compiled_expression.search(color)

    # If no match, get the color hex code from COLORS_WITH_HEX
    if match is None:
        for color_bundle in Colors.COLORS_WITH_HEX:
            if color_bundle[1] == color:
                color = color_bundle[0].lower()
                break

    # Get RGB color, as a tuple
    rgb_color: list = list(hex_to_rgb(hex_color=color.lstrip("#")))

    # Modify created list
    for index, color in enumerate(rgb_color):
        rgb_color[index] = color * factor

    # Redistribute RGB values of the modified RGB color list
    rgb_color = list(redistribute_rgb(*rgb_color))

    # Convert new RGB color value to hexadecimal color code
    new_color: str = rgb_to_hex(*rgb_color)

    # Return hexadecimal color code
    return new_color


"""Stats-involved Function(s)"""


def update_last_used_setting(target: str, setting: typing.Union[str, bool]):
    """Updates the last_used_setting variable corresponding to the given setting
    """
    global last_background_color_setting, last_text_color_setting, last_button_color_setting, \
        last_button_text_color_setting, last_gui_sound_setting, last_remember_settings_setting, \
        last_invalid_text_color_setting

    if target == "Background Color":
        if last_background_color_setting == setting:
            return None
        else:
            last_background_color_setting = setting
            Stats.settings_changed_background_color.set(Stats.settings_changed_background_color.get() + 1)
            return None

    elif target == "Text Color":
        if last_text_color_setting == setting:
            return None
        else:
            last_text_color_setting = setting
            Stats.settings_changed_text_color.set(Stats.settings_changed_text_color.get() + 1)
            return None

    elif target == "Buttons' Color":
        if last_button_color_setting == setting:
            return None
        else:
            last_button_color_setting = setting
            Stats.settings_changed_buttons_color.set(Stats.settings_changed_buttons_color.get() + 1)
            return None

    elif target == "Buttons' Text Color":
        if last_button_text_color_setting == setting:
            return None
        else:
            last_button_text_color_setting = setting
            Stats.settings_changed_buttons_text_color.set(Stats.settings_changed_buttons_text_color.get() + 1)
            return None

    elif target == "Invalid Text Color":
        if last_invalid_text_color_setting == setting:
            return None
        else:
            last_invalid_text_color_setting = setting
            Stats.settings_changed_invalid_text_color.set(Stats.settings_changed_invalid_text_color.get() + 1)
            return None

    elif target == "GUI Sound":
        if last_gui_sound_setting == setting:
            return None
        else:
            last_gui_sound_setting = setting
            Stats.settings_changed_gui_sound.set(Stats.settings_changed_gui_sound.get() + 1)
            return None

    # elif target == "Remember Settings":
    if last_remember_settings_setting == setting:
        return None
    # else:
    last_remember_settings_setting = setting
    Stats.settings_changed_remember_settings.set(Stats.settings_changed_remember_settings.get() + 1)
    return None
