"""
User module; Consists of the user related dictionary and its related functions
"""


# Imports
import datetime
import json
import random
import string
import typing
import os
import Settings
import Misc
# GUI-related Imports
from MainWindow import root
from tkinter import IntVar, BooleanVar, StringVar
from tkinter.constants import NORMAL, DISABLED, CENTER, END
from tkinter.filedialog import asksaveasfile
from tkinter.messagebox import showinfo


"""Variables"""

# User data json file paths
USER_JSON_PATH: str = os.path.join(os.getcwd(), "Dependencies", "UserData", "UserData.json")
LAST_USER_JSON_PATH: str = os.path.join(os.getcwd(), "Dependencies", "UserData", "LastUser.json")

# Counts number of users
user_count: int = 0

# Starts out as empty dict, fills out with users read from UserData.json and new Users
user_dict: dict = {}

# Represents the user currently logged-in
logged_in_user: dict = {}

# Determines whether any user is logged in
is_logged_in: bool = False

# Determines whether logged in user is admin
is_admin: bool = False


# Account privacy
ACCOUNT_PRIVACY_OPTIONS: tuple = ("Public", "Private Details", "Private Compositions", "Private")


# Maximum name length
MAXIMUM_NAME_LENGTH: int = 30
# Minimum username length
MINIMUM_USERNAME_LENGTH: int = 4
MAXIMUM_USERNAME_LENGTH: int = 30
# Minimum password length
MINIMUM_PASSWORD_LENGTH: int = 6

# Password not recovered text
PASSWORD_NOT_RECOVERED_MESSAGE: str = "❌ PASSWORD NOT RECOVERED ❌"


"""GUI Variables"""
# Find the trace methods for these variables in the GUI module


# Determines whether the Remember Me checkbutton option is on or off
remember_me: BooleanVar = BooleanVar(root)
remember_me.set(False)

# Used when Registering a new user

# Used to get the chosen names and nickname
# First Name
chosen_first_name: StringVar = StringVar(root)
chosen_first_name.set("")
# Last Name
chosen_last_name: StringVar = StringVar(root)
chosen_last_name.set("")
# Nickname
chosen_nickname: StringVar = StringVar(root)
chosen_nickname.set("")
# Used to get the chosen gender
chosen_gender: StringVar = StringVar(root)
chosen_gender.set(Misc.GENDERS[-1])
# Used to get birth dates
# Day
chosen_birth_day: StringVar = StringVar(root)
chosen_birth_day.set(datetime.date.today().day)
# Month
chosen_birth_month: StringVar = StringVar(root)
chosen_birth_month.set(datetime.date.today().strftime("%B"))
# Year
chosen_birth_year: StringVar = StringVar(root)
chosen_birth_year.set(datetime.date.today().year)
# Used to get the country and state of origin and residence
# Country of origin
chosen_country_of_origin: StringVar = StringVar(root)
chosen_country_of_origin.set(Misc.COUNTRIES_NAMES[0])
# State of origin
chosen_state_of_origin: StringVar = StringVar(root)
chosen_state_of_origin.set("None")
# Country of residence
chosen_country_of_residence: StringVar = StringVar(root)
chosen_country_of_residence.set(Misc.COUNTRIES_NAMES[0])
# State of residence
chosen_state_of_residence: StringVar = StringVar(root)
chosen_state_of_residence.set("None")
# Used to get the chosen account privacy option
chosen_account_privacy: StringVar = StringVar(root)
chosen_account_privacy.set(ACCOUNT_PRIVACY_OPTIONS[0])
# Used to get the chosen username and password
# Username
chosen_username: StringVar = StringVar(root)
chosen_username.set("")
# Password
chosen_password: StringVar = StringVar(root)
chosen_password.set("")
chosen_confirm_password: StringVar = StringVar(root)
chosen_confirm_password.set("")

# Used in the login menu

# Username
entered_login_username: StringVar = StringVar(root)
entered_login_username.set("")
# Password
entered_login_password: StringVar = StringVar(root)
entered_login_password.set("")

# Used when recovering password

# Recovery Key number of recovery attempts
failed_recovery_attempts: IntVar = IntVar(root)
failed_recovery_attempts.set(0)
# Used to keep track of the revealed password label
recovered_password: StringVar = StringVar(root)
recovered_password.set("")
# Recovery Key Username input
recovery_key_username: StringVar = StringVar(root)
recovery_key_username.set("")
# Recovery Key parts
recovery_key_part_1: StringVar = StringVar(root)
recovery_key_part_2: StringVar = StringVar(root)
recovery_key_part_3: StringVar = StringVar(root)
recovery_key_part_4: StringVar = StringVar(root)
# Set all of them to empty strings
recovery_key_part_1.set("")
recovery_key_part_2.set("")
recovery_key_part_3.set("")
recovery_key_part_4.set("")

# User Profile

user_profile_user: dict = {}

# Booleans

# Determines whether the password should be shown or not in the register menu
show_password_register: BooleanVar = BooleanVar(root)
show_password_register.set(False)
# Determines whether the password should be shown or not in the login menu
show_password_login: BooleanVar = BooleanVar(root)
show_password_login.set(False)
# Determines whether the password should be shown or not in the forgot password (recovery key) menu
show_password_recovery_key: BooleanVar = BooleanVar(root)
show_password_recovery_key.set(False)
# Determines whether app is in the register user menus or not
is_in_register_user_menu_general_data: BooleanVar = BooleanVar(root)
is_in_register_user_menu_general_data.set(False)
# Determines whether app is in the final register user menu
is_in_registration_successful: BooleanVar = BooleanVar(root)
is_in_registration_successful.set(False)
# Determines whether the display of the register user general data screen comes from the main menu
came_from_main_menu: BooleanVar = BooleanVar(root)
came_from_main_menu.set(False)


"""Functions"""


def get_user_age(year: int, month: int, day: int):
    """Return current age of user, in years
    """
    # Inspired from the answers found here: https://stackoverflow.com/q/2217488/15454571
    today: datetime.date = datetime.date.today()
    years: int = today.year - year
    if today.month < month or (today.month == month and today.day < day):
        return years - 1
    return years


def generate_new_recovery_key():
    """Generates random recovery key
    """
    # Create set of existing keys
    recovery_keys_set: set = {user_dict[user]["Credentials"]["Recovery Key"] for user in user_dict}
    # Generate random new key
    recovery_key: str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
    recovery_key = recovery_key[:4] + "-" + recovery_key[4:8] + "-" + recovery_key[8:12] + "-" + recovery_key[12:]
    # While key is duplicate, generate new key until it is not
    while recovery_key in recovery_keys_set:
        recovery_key: str = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))
        recovery_key = recovery_key[:4] + "-" + recovery_key[4:8] + "-" + recovery_key[8:12] + "-" + recovery_key[12:]
    return recovery_key


def is_valid_register_user_data(first_name: str, last_name: str, year: str, month: str, day: str):
    """Verifies input data when attempting to proceed with registering a new user account
    """
    if Misc.empty_string(first_name):
        return False
    if Misc.empty_string(last_name):
        return False
    if not Misc.is_valid_date(year=year, month=month, day=day):
        return False
    return True


def register_new_user(first_name: str, last_name: str, nickname: str,
                      username: str, password: str,
                      gender: str,
                      year: int, month: int, day: int,
                      country_of_origin: str, state_of_origin: str, country_of_residence: str, state_of_residence: str,
                      privacy: str,
                      # Settings
                      background_color: str, text_color: str,
                      button_color: str, button_text_color: str,
                      invalid_text_color: str, gui_sound: bool):
    """Creates a new user
    """
    global user_count, logged_in_user, is_logged_in
    # Create new user name dict
    new_user_name: dict = {
        "First Name": first_name,
        "Last Name": last_name,
        "Nickname": nickname
    }
    # Create new user login credentials
    new_user_credentials: dict = {
        "Username": username,
        "Password": password,
        "Recovery Key": generate_new_recovery_key()
    }
    # Create new user location dict
    new_user_location: dict = {
        "Country Of Origin": country_of_origin,
        "State Of Origin": state_of_origin,
        "Country Of Residence": country_of_residence,
        "State Of Residence": state_of_residence
    }
    # Create new user settings dict
    new_user_settings: dict = {
        "Background Color": background_color,
        "Text Color": text_color,
        "Buttons' Color": button_color,
        "Buttons' Text Color": button_text_color,
        "Invalid Text Color": invalid_text_color,
        "GUI Sound": gui_sound
    }
    # TODO: Create user stats system
    # Create new user stats dict
    # new_user_stats: dict = {
    #     "Total": 0,
    #     "Piano": {
    #         "Total": 0,
    #         "Short": 0,
    #         "Long": 0
    #     },
    #     "Flute": 0,
    #     "Trumpet": 0,
    #     "Violin": 0
    # }
    # Increment user count
    user_count += 1
    # Add new user to user_dict
    user_dict.update({f"User {str(user_count)}": {
        "Name": new_user_name,
        "Credentials": new_user_credentials,
        "Gender": gender,
        "Birth Date": {
            "Year": year,
            "Month": month,
            "Day": day
        },
        "Location": new_user_location,
        "Privacy": privacy,
        "Settings": new_user_settings,
        # TODO
        # "Stats": new_user_stats,
        "Compositions": [],  # empty compositions list
        "Given Ratings": []
    }})
    # Set new_user as logged_in_user
    logged_in_user = user_dict[f"User {str(user_count)}"]
    is_logged_in = True


def login_user(username: str, password: str):
    """Logs in user
    """
    global logged_in_user, is_logged_in, is_admin
    # TODO: Add Admin account & system
    # if username == "Admin" and password == "Admin":
    #     logged_in_user = {"Admin": None}
    #     is_logged_in = True
    #     is_admin = True
    #     return None
    for user in user_dict:
        if user_dict[user]["Credentials"]["Username"] == username \
                and user_dict[user]["Credentials"]["Password"] == password:
            logged_in_user = user_dict[user]
            is_logged_in = True
            return None
    # If Username of Password is/are incorrect
    logged_in_user = {}
    is_logged_in = False
    
    
def logout_user():
    """Logs out user
    """
    global logged_in_user, is_logged_in, is_admin
    # TODO: Add Admin account & system
    # if logged_in_user == {"Admin": None}:
    #     is_admin = False
    logged_in_user = {}
    is_logged_in = False
    remember_me.set(False)
    if Settings.remember_settings_setting.get() == "User":
        Settings.set_settings_vars("Default")
        Settings.remember_settings_setting.set("Default")


def update_logged_user_setting(target: str, setting_value: typing.Union[str, bool]):
    """Updates the logged_in_user's statistics dictionary
    """
    logged_in_user["Settings"].update({target: setting_value})
    write_logged_in_user_in_file(True)
    for user in user_dict:
        if user_dict[user]["Credentials"]["Username"] == logged_in_user["Credentials"]["Username"]:
            user_dict[user]["Settings"].update({target: setting_value})
            write_users_in_file()
            break


def create_recovery_key_txt_file(username: str, recovery_key: str):
    """Creates a new .txt file containing the new registered user's recovery key
    """
    from GUI import create_recovery_key_txt_file_button
    # Get possessive form
    possessive_form: str = Misc.get_possessive(username[-1])
    # Get nicely formatted current date and time
    current_datetime: str = datetime.datetime.now().strftime("%A, %d-%B-%Y, %H:%M:%S")
    # Create file content
    file_content: str = f"Recovery Key: {recovery_key}\nFile created: {current_datetime}"
    # Get app current working directory
    initial_dir: str = os.path.join(os.getcwd(), "Recovery Keys")
    # Create proper file
    file = asksaveasfile(defaultextension=".txt", filetypes=(("Text Documents (*.txt)", "*.txt"), ("All Files", "*.*")),
                         initialdir=initial_dir, title="Save Recovery Key",
                         initialfile=f"{username}{possessive_form} Recovery Key", parent=root)
    # Write content to file
    if file:
        file.write(file_content)
        file.close()
        create_recovery_key_txt_file_button.config(text="Saved In File", state=DISABLED)
        showinfo(title="File Information",
                 message="This file will not be deleted upon using the provided uninstaller. "
                         "Manual deletion is required to remove it.", parent=root)


def create_recovered_password_txt_file(username: str, password: str):
    """Creates a new .txt file containing the user's recovered password
    """
    from GUI import create_recovered_password_file_button
    # Get possessive form
    possessive_form: str = Misc.get_possessive(username[-1])
    # Get nicely formatted current date and time
    current_datetime: str = datetime.datetime.now().strftime("%A, %d-%B-%Y, %H:%M:%S")
    # Create file content
    file_content: str = f"Recovered Password: {password}\nFile created: {current_datetime}"
    # Get app current working directory
    initial_dir: str = os.path.join(os.getcwd(), "Recovered Passwords")
    # Create proper file
    file = asksaveasfile(defaultextension=".txt", filetypes=(("Text Documents (*.txt)", "*.txt"), ("All Files", "*.*")),
                         initialdir=initial_dir, title="Save Recovered Password",
                         initialfile=f"{username}{possessive_form} Recovered Password", parent=root)
    # Write content to file
    if file:
        file.write(file_content)
        file.close()
        create_recovered_password_file_button.config(state=DISABLED, text="Saved In File")
        showinfo(title="File Information",
                 message="This file will not be deleted upon using the provided uninstaller. "
                         "Manual deletion is required to remove it.", parent=root)
    else:
        create_recovered_password_file_button.config(state=NORMAL, text="Create .txt File")


def read_users_from_file():
    """Reads all users from UserData.json
    Call when starting app
    """
    global user_count
    with open(file=USER_JSON_PATH, encoding="utf-8") as file:
        file_data: dict = json.load(file)
    if not file_data:
        return None
    for user in file_data:
        # Increment user count
        user_count += 1
        # Add new User object to user_dict dictionary
        user_dict.update({f"User {str(user_count)}": {
            "Name": file_data[user]["Name"],
            "Credentials": file_data[user]["Credentials"],
            "Gender": file_data[user]["Gender"],
            "Birth Date": {
                "Year": file_data[user]["Birth Date"]["Year"],
                "Month": file_data[user]["Birth Date"]["Month"],
                "Day": file_data[user]["Birth Date"]["Day"]
            },
            "Location": file_data[user]["Location"],
            "Privacy": file_data[user]["Privacy"],
            "Settings": file_data[user]["Settings"],
            # "Stats": file_data[user]["Stats"],
            "Compositions": file_data[user]["Compositions"],
            "Given Ratings": file_data[user]["Given Ratings"]
        }})


def write_users_in_file():
    """Writes all users in UserData.json
    """
    with open(file=USER_JSON_PATH, mode="w", encoding="utf-8") as file:
        json.dump(user_dict, file, indent=4)


def read_logged_user_from_file():
    """Reads the logged_in_user form file
    Call when starting app
    """
    global logged_in_user, is_logged_in
    with open(file=LAST_USER_JSON_PATH, encoding="utf-8") as file:
        read_user: dict = json.load(file)
        if not read_user:
            # Plain return; is_logged in remains false and logged_in_user stays as empty dict
            # Works without reassigning these 2 variables, but I do it just to be safe
            logged_in_user = {}
            is_logged_in = False
            return None
        logged_in_user = read_user["Last User"]
        is_logged_in = True


def write_logged_in_user_in_file(boolean: bool):  # boolean represents the remember_me.get() value
    """Writes the logged_in_user in LastUser.json
    """
    with open(file=LAST_USER_JSON_PATH, mode="w", encoding="utf-8") as file:
        if is_logged_in and boolean:
            json.dump({"Last User": logged_in_user}, file, indent=4)
        else:
            json.dump(None, file, indent=4)


"""GUI-involved Functions"""


def check_create_account_condition(username: str, password: str, confirm_password: str):
    """Checks whether the given input data allows for a new user account to be created
    """
    from GUI import taken_username_label, create_account_button

    new_username: bool = True
    # Check if username is non-repeating
    for user in user_dict:
        if username == user_dict[user]["Credentials"]["Username"]:
            new_username = False
            break
    # Place / Forget the taken username label
    if not new_username:
        taken_username_label.place(relheight=0.05, relwidth=0.64, relx=0.18, rely=0.655)
    else:
        taken_username_label.place_forget()
    # Check the rest of the required conditions
    if new_username and len(username) >= MINIMUM_USERNAME_LENGTH and \
            len(password) >= MINIMUM_PASSWORD_LENGTH and password == confirm_password:
        create_account_button.config(state=NORMAL)
    else:
        create_account_button.config(state=DISABLED)


def check_username_and_key_validity(username: str, key_part_1: str, key_part_2: str, key_part_3: str, key_part_4: str):
    """Check Username & Recovery Key validity
    """
    from GUI import create_recovered_password_file_button, recovered_password_text,\
        show_password_checkbutton_recovery_key, recovery_key_invalid_inputs_label

    # Clear previous invalid inputs message label
    recovery_key_invalid_inputs_label.place_forget()

    # Create the recovery key from given key parts
    final_key: str = f"{key_part_1}-{key_part_2}-{key_part_3}-{key_part_4}"

    # Create bool variable to determine the inputs' validity
    matching_credentials: bool = False

    # Check if given Username matches the account's Recovery Key
    for user in user_dict:
        if username == user_dict[user]["Credentials"]["Username"] and \
                final_key == user_dict[user]["Credentials"]["Recovery Key"]:
            matching_credentials = True
            recovered_password.set(user_dict[user]["Credentials"]["Password"])
            break

    # Determine outcome
    if matching_credentials:
        Misc.copy_var_value_to_disabled_text_widget(text_text="•" * len(recovered_password.get()),
                                                    text_widget=recovered_password_text)

        show_password_recovery_key.set(False)
        show_password_checkbutton_recovery_key.config(state=NORMAL, text="Show Password")

        create_recovered_password_file_button.config(state=NORMAL, text="Create .txt File")
    else:
        # Clear the recovered_password variable
        recovered_password.set("")

        failed_recovery_attempts.set(failed_recovery_attempts.get() + 1)
        error_message: str = "Invalid Username or Recovery Key!"
        if failed_recovery_attempts.get() > 3:
            error_message += "\nPlease try again, or stop trying..."

        recovered_password_text.tag_configure(CENTER, justify=CENTER)
        Misc.copy_var_value_to_disabled_text_widget(text_text=PASSWORD_NOT_RECOVERED_MESSAGE,
                                                    text_widget=recovered_password_text)
        recovered_password_text.tag_add(CENTER, "1.0", END)

        show_password_recovery_key.set(False)
        show_password_checkbutton_recovery_key.config(state=DISABLED, text="Show Password")

        create_recovered_password_file_button.config(state=DISABLED, text="Create .txt File")

        recovery_key_invalid_inputs_label.config(text=error_message)
        recovery_key_invalid_inputs_label.place(relheight=0.1, relwidth=0.55, relx=0.225, rely=0.495)
