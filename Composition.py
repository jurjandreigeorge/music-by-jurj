"""
Composition module; consists of recording / composition data and functions
"""


# Imports
import Misc
import Sounds
import User
import copy
import datetime
import winsound
import time
import threading
# GUI-related Imports
from MainWindow import root
from tkinter import Label, DoubleVar, BooleanVar, StringVar, IntVar, Button, Frame
from tkinter.constants import HORIZONTAL, DISABLED, NORMAL, RAISED
from tkinter.ttk import Progressbar, Style
from Fonts import verdana_30, verdana_35_italic


"""Variables"""


# Default composition format
DEFAULT_COMPOSITION: dict = {
    "Name": "",  # composition name (str)
    "Description": "",  # composition description (str)
    "Notes List": [],  # list of notes; contains note names (str list)
    "Delays List": [],  # list of delays; contains float values (float list)
    "Length": 0,  # total length of notes + delays (float)
    "Played": 0,  # number of times the composition was played (int)
    # TODO
    # "Critique": [],  # list of critique messages (str list)
    "Rating": {},  # dict numbers from 0 to 5 (ints); Starts as empty dict to represent no rating given (int dict)
    "Date Of Creation": {
        "Year": 0,  # current year (int)
        "Month": 0,  # current month (int)
        "Day": 0  # current day (int)
    }
}

# Variables used to initiate, create and update a new composition
# Used to create any and every composition
new_composition: dict = copy.deepcopy(DEFAULT_COMPOSITION)
notes_list: list = []
delay_list: list = []
length: float = 0

# Maximum length of composition description
MAXIMUM_DESCRIPTION_LENGTH: int = 250
# Used to set the maximum delay slider value
MAXIMUM_DELAY_SLIDER_VALUE: int = 3

# Composition count
composition_count: int = 0

# Composers list
composer_list: list = []

# Sorted compositions list
sorted_composition_list: list = []


# Composition to play name; Stores the name of the composition to be played (in playback composition)
composition_to_play_name: StringVar = StringVar(root)
composition_to_play_name.set("")

# Composition to play; stores the entire dict of the composition to be played
composition_to_play: dict = {}


"""GUI Variables"""


# Style
style = Style()
style.theme_use(themename="classic")
# Used to set and change the given name of any and every new composition
chosen_new_composition_name: StringVar = StringVar()
chosen_new_composition_name.set("")
# Composition description
new_composition_description: StringVar() = StringVar(root)
new_composition_description.set("")
# Used to keep track of the delay slider value
delay_scale_value: DoubleVar() = DoubleVar(root)
delay_scale_value.set(0)
# Used to determine whether at least 1 note was played in new composition or not
# Find its trace instruction in the GUI Module
at_least_1_note_recorded: BooleanVar() = BooleanVar(root)
at_least_1_note_recorded.set(False)
# Determines whether app is in the record composition menu or not
is_recording_composition: BooleanVar = BooleanVar(root)
is_recording_composition.set(False)
# Determines whether app is currently playing composition
is_playing_composition: BooleanVar = BooleanVar(root)
is_playing_composition.set(False)


# Strings used as the content of the invalid composition name label
whitespace_composition_name_error_message: str = "Invalid Composition Name: Name is whitespace!"
used_composition_name_error_message: str = "Invalid Composition Name: Name is already used by "
# Used to keep track of the username of the user who has already used an attempted new composition name
invalid_used_composition_name_owner_username: str = ""


"""Sort Composition Variables - Used in Playback Composition"""


# Any invalid sorting boolean determines whether the current selected sorting options set is valid or not
is_any_invalid_sorting_option: BooleanVar = BooleanVar(root)
is_any_invalid_sorting_option.set(False)

# User
sort_by_user: StringVar = StringVar(root)
sort_by_user.set("Any")

user_inclusive_exclusive: StringVar = StringVar(root)
user_inclusive_exclusive.set("Inclusive")

sort_user_selected_user: StringVar = StringVar(root)
sort_user_selected_user.set("")

# Invalid user sorting option boolean
is_invalid_user_sorting_option: BooleanVar = BooleanVar(root)
is_invalid_user_sorting_option.set(False)

# Length
sort_by_length: StringVar = StringVar(root)
sort_by_length.set("Any")

POSSIBLE_LENGTHS_TUPLE: tuple = ("Short", "Medium", "Long")

specific_length: StringVar = StringVar(root)
specific_length.set(POSSIBLE_LENGTHS_TUPLE[0])

short_length: IntVar = IntVar(root)
short_length.set(1)

medium_length: IntVar = IntVar(root)
medium_length.set(0)

long_length: IntVar = IntVar(root)
long_length.set(0)

# Invalid length sorting option boolean
is_invalid_length_sorting_option: BooleanVar = BooleanVar(root)
is_invalid_length_sorting_option.set(False)

# Date
sort_by_date: StringVar = StringVar(root)
sort_by_date.set("Any")

date_specific_inclusive_exclusive: StringVar = StringVar(root)
date_specific_inclusive_exclusive.set("Inclusive")

date_interval_inclusive_exclusive: StringVar = StringVar(root)
date_interval_inclusive_exclusive.set("Inclusive")

# For specific date
sort_date_selected_day: StringVar = StringVar(root)
sort_date_selected_day.set(datetime.date.today().day)

sort_date_selected_month: StringVar = StringVar(root)
sort_date_selected_month.set(datetime.date.today().strftime("%B"))

sort_date_selected_year: StringVar = StringVar(root)
sort_date_selected_year.set(datetime.date.today().year)

# For date interval
# From ...
sort_date_selected_day_from: StringVar = StringVar(root)
sort_date_selected_day_from.set(1)

sort_date_selected_month_from: StringVar = StringVar(root)
sort_date_selected_month_from.set(Misc.MONTHS_NAMES[0])

sort_date_selected_year_from: StringVar = StringVar(root)
sort_date_selected_year_from.set(datetime.date.today().year)

# ... to
sort_date_selected_day_to: StringVar = StringVar(root)
sort_date_selected_day_to.set(datetime.date.today().day)

sort_date_selected_month_to: StringVar = StringVar(root)
sort_date_selected_month_to.set(datetime.date.today().strftime("%B"))

sort_date_selected_year_to: StringVar = StringVar(root)
sort_date_selected_year_to.set(datetime.date.today().year)

# Invalid date sorting option boolean
is_invalid_date_sorting_option: BooleanVar = BooleanVar(root)
is_invalid_date_sorting_option.set(False)

# Rating
sort_by_rating: StringVar = StringVar(root)
sort_by_rating.set("Any")

# Also Misc.no_rating for no rating given to composition
POSSIBLE_RATINGS_TUPLE: tuple = (Misc.STAR_1, Misc.STAR_2, Misc.STAR_3, Misc.STAR_4, Misc.STAR_5)

specific_rating: StringVar = StringVar(root)
specific_rating.set(5)

no_rating: IntVar = IntVar(root)
no_rating.set(0)

star_1_rating: IntVar = IntVar(root)
star_1_rating.set(0)

star_2_rating: IntVar = IntVar(root)
star_2_rating.set(0)

star_3_rating: IntVar = IntVar(root)
star_3_rating.set(0)

star_4_rating: IntVar = IntVar(root)
star_4_rating.set(0)

star_5_rating: IntVar = IntVar(root)
star_5_rating.set(1)

# Invalid rating sorting option boolean
is_invalid_rating_sorting_option: BooleanVar = BooleanVar(root)
is_invalid_rating_sorting_option.set(False)

# At least 1 composition in entire app
at_least_1_public_composition: BooleanVar = BooleanVar(root)
at_least_1_public_composition.set(False)

# Preselect option
preselect_option: StringVar = StringVar(root)
preselect_option.set("First")


# Sorted Menu Variables
sorted_5_star_var: IntVar = IntVar(root)
sorted_5_star_var.set(0)

sorted_4_star_var: IntVar = IntVar(root)
sorted_4_star_var.set(0)

sorted_3_star_var: IntVar = IntVar(root)
sorted_3_star_var.set(0)

sorted_2_star_var: IntVar = IntVar(root)
sorted_2_star_var.set(0)

sorted_1_star_var: IntVar = IntVar(root)
sorted_1_star_var.set(0)

is_in_sorted_menu: BooleanVar = BooleanVar(root)
is_in_sorted_menu.set(False)


# Rating Variable(s)
given_rating: StringVar = StringVar(root)
given_rating.set(Misc.NO_RATING)
# Boolean needed for rating compositions
is_in_start_playback_menu: BooleanVar = BooleanVar(root)
is_in_start_playback_menu.set(False)


"""Threading Variable(s)"""

stop_event: threading.Event = threading.Event()


"""Playback Composition GUI Elements"""

start_stop_button_positions: dict = {"relheight": .8, "relwidth": .9625, "relx": .01875, "rely": .1}

start_stop_label_positions: dict = {"relheight": .125, "relwidth": .9, "relx": .05, "rely": .515}


start_stop_playing_button_frame = Frame(root, borderwidth=3, relief=RAISED)

# No GUI sound for these buttons
start_playing_button = Button(start_stop_playing_button_frame, text="Start Audition", font=verdana_30, borderwidth=3,
                              command=lambda: initiate_play_composition_thread(composition_to_play_name.get()))

stop_playing_button = Button(start_stop_playing_button_frame, text="Stop Audition", font=verdana_30, borderwidth=3,
                             command=lambda: [stop_event.set(),
                                              playing_label.place_forget(),
                                              stopping_playing_label.config(text=stopping_playing_label_special_text)
                                              if stopped_counter.get() > 3
                                              else
                                              stopping_playing_label.config(text=stopping_playing_label_default_text),
                                              stopping_playing_label.place(**start_stop_label_positions),
                                              stop_playing_button.config(state=DISABLED,
                                                                         text="Stopping Audition")
                                              ])

idle_composition_label_text: str = "Everything is cued up & ready to go!\nJust hit the Start Audition button, " \
                                   "sit back, relax & enjoy!"
playing_composition_label_text: str = "The bar below keeps track of your audition's progress.\nEnjoy!"
stopping_playing_label_default_text: str = "Stopping audition...\nWait for current note to finish playing!"
stopped_playing_label_default_text: str = "Audition forcefully stopped!"
ended_playing_label_default_text: str = "The End!"
stopped_and_ended_playing_label_default_text: str = "Audition stopped right at the last note!\nHow disappointing..."

stopping_playing_label_special_text: str = "Stopping audition... ...again...\nYou really like to do this, don't you?"
stopped_playing_label_special_text: str = "Audition forcefully stopped!\n" \
                                          "It's very inappropriate to stop so many compositions!"
ended_playing_label_special_text: str = "The End!\nWe hope you enjoy what you're hearing so far!"
stopped_and_ended_playing_label_special_text: str = "Audition stopped right at the last note!\n" \
                                                    "You should cultivate your patience and finish what you started!"

idle_playing_label = Label(root, text=idle_composition_label_text, font=verdana_35_italic)
playing_label = Label(root, text=playing_composition_label_text, font=verdana_35_italic)
stopping_playing_label = Label(root, text=stopping_playing_label_default_text, font=verdana_35_italic)
stopped_playing_label = Label(root, text=stopped_playing_label_default_text, font=verdana_35_italic)
ended_playing_label = Label(root, text=ended_playing_label_default_text, font=verdana_35_italic)
stopped_and_ended_playing_label = Label(root, text=stopped_and_ended_playing_label_default_text, font=verdana_35_italic)

# Play progress keeps track of the composition progress while playing
play_progress: IntVar = IntVar(root)
play_progress.set(0)

# Create progressbar
playback_composition_progressbar: Progressbar = Progressbar(root, orient=HORIZONTAL, maximum=0,
                                                            mode="determinate", variable=play_progress)

# Keeps track of how many times the composition was stopped
stopped_counter: IntVar = IntVar(root)
stopped_counter.set(0)

# Keeps track of how many times the composition ended naturally
ended_counter: IntVar = IntVar(root)
ended_counter.set(0)

# Keeps track of how many times the composition was stopped when the last note was playing
stopped_and_ended_counter: IntVar = IntVar(root)
stopped_and_ended_counter.set(0)

# Keeps track of the last cause of composition stop
last_cause: StringVar = StringVar(root)
last_cause.set(None)


"""Functions"""


def add_note_and_delay(instrument: str, note_name: str, delay: float, note_length: str = "None"):
    """Adds note and delay to their respective lists; updates length parameter
    """
    from GUI import composition_length_label

    global length
    at_least_1_note_recorded.set(True)
    # Get full note name
    if note_length == "None":
        full_note_name: str = f"{note_name} {instrument}"
    else:
        full_note_name: str = f"{note_name} {note_length} {instrument}"
    # Append note and delay to corresponding lists
    notes_list.append(full_note_name)
    delay_list.append(delay)
    # Update new composition dict lists
    # Append note name and delay to notes and delays list
    new_composition.update({"Notes List": notes_list, "Delays List": delay_list})
    # Get file path of given note
    file_path: str = Sounds.get_instrument_sound_file_path(instrument=instrument,
                                                           note_name=note_name,
                                                           note_length=note_length)
    # Only count delay if there's another note coming after (don't count last delay towards length)
    if len(delay_list) == 1:
        length += Sounds.get_wav_file_length(file_path=file_path)
    else:
        length += Sounds.get_wav_file_length(file_path=file_path) + delay_list[-1]
    # Round length to 2 decimals
    length = round(length, 2)
    # Config length label
    composition_length_label.config(text=f"Length: {Misc.format_duration(duration=length)}")


def save_new_composition(composition_name: str, composition_description: str):
    """Creates new composition and appends it to the logged_in_user's composition_list
    """
    # Modify new_composition with input variables
    new_composition.update({
        "Name": composition_name,
        "Description": composition_description,
        # Note and Delay Lists get updated in the add_note_and_delay function (the function above this)
        "Length": length,
        "Played": 0,
        # "Critique": [],  TODO: Add Composition Critique System
        "Rating": {"5": 0, "4": 0, "3": 0, "2": 0, "1": 0},
        "Date Of Creation": {
            "Year": datetime.date.today().year,
            "Month": datetime.date.today().month,
            "Day": datetime.date.today().day
        }
    })
    # Add new_composition to user_dict
    for user in User.user_dict:
        if User.logged_in_user["Credentials"]["Username"] == User.user_dict[user]["Credentials"]["Username"]:
            User.user_dict[user]["Compositions"].append(copy.deepcopy(new_composition))
            # Update logged in user dict
            User.logged_in_user["Compositions"] = User.user_dict[user]["Compositions"]
            break
    # Write updated user_dict and logged_in_user in file
    User.write_users_in_file()
    User.write_logged_in_user_in_file(True)
    # New composition variables shall be cleared after calling this function
    # Find the clear_new_composition_variables function in the GUI module
    # The update_composer_list() also needs to be called after executing this function


def get_composition_notes_and_delays(composition: dict):
    """Generator function that yields a composition's notes and delays
    """
    note_number: int = 0
    for note_name, delay in zip(composition["Notes List"], composition["Delays List"]):
        # Increment note number
        note_number += 1
        # Calculate spacing amount and create spacing string
        # "Do 1/2 Short Piano" are the longest possible note names; They're 16 characters long
        spacing_amount: int = 17 - len(note_name)  # Make this automatically calculated
        spacing: str = " " * spacing_amount
        # Yield calculated "note & delay" line
        yield f"{note_number}. {note_name}{spacing}| {delay}s"


def update_composer_list():
    """Initiates list of users with at least 1 composition bound to their account
    Only call if User.is_logged_in is True; will throw assertion exception otherwise
    Call when starting app, when saving a new composition, when deleting a composition and when deleting a user (only
    when Admin) and when logging in
    """
    assert User.is_logged_in

    from GUI import sort_user_choose_user_combobox
    
    global composition_count, composer_list

    # Required variables
    is_logged_or_public_composer: bool = False
    combobox_list: list = []

    # Clear these global variables so they can be recalculated freshly
    composition_count = 0
    composer_list.clear()

    # Start iterating over user_dict, searching for composers & public composers
    for user in User.user_dict:
        composer: dict = User.user_dict[user]
        # Get number of compositions; saved in variable so it doesn't have to be calculated twice
        number_of_compositions: int = len(composer["Compositions"])
        is_composer: bool = number_of_compositions > 0
        # Skip current user if it's not a composer
        if not is_composer:
            continue
        # Append composer to composers list
        composer_list.append(composer)
        composition_count += number_of_compositions
        # Determine if logged in user has at least 1 composition or if found composer has public compositions
        if composer["Credentials"]["Username"] == User.logged_in_user["Credentials"]["Username"] \
                or composer["Privacy"] in ("Public", "Private Details"):
            is_logged_or_public_composer = True
            combobox_list.append(composer["Credentials"]["Username"])

    # Public composition only if composer is logged in user or composer has public compositions
    if is_logged_or_public_composer:
        at_least_1_public_composition.set(True)
    else:
        at_least_1_public_composition.set(False)

    # Configure sort_user_choose_user_combobox values list
    if at_least_1_public_composition.get():
        sort_user_choose_user_combobox["values"] = sorted(combobox_list)
        # Set the preselected specific user
        if len(User.logged_in_user["Compositions"]):
            sort_user_selected_user.set(User.logged_in_user["Credentials"]["Username"])
        elif len(sort_user_choose_user_combobox["values"]):
            sort_user_selected_user.set(sort_user_choose_user_combobox["values"][0])
        else:
            raise ValueError("Impossible to reach this code branch in normal conditions!")


def get_composition_from_name(composition_name: str):
    """Gets the composition dict from its name
    """
    for user in User.user_dict:
        for composition in User.user_dict[user]["Compositions"]:
            if composition_name == composition["Name"]:
                return composition
    raise ValueError(f"No composition with name {composition_name} in database!")


def get_number_of_eligible_compositions():
    """Gets the total number of compositions that can be played back
    """
    number_of_compositions: int = 0
    for user in User.user_dict:
        if User.user_dict[user]["Privacy"] in ("Public", "Private Details") \
                or User.user_dict[user] == User.logged_in_user:
            number_of_compositions += len(User.user_dict[user]["Compositions"])
    return number_of_compositions


def initiate_play_composition_thread(composition_name: str):
    """Starts playing the given composition
    Uses threads to avoid locking up the GUI
    """
    # Get composition dict from name
    if Misc.empty_string(name=composition_name):
        raise ValueError
    else:
        composition_dict: dict = get_composition_from_name(composition_name=composition_name)
    # If no composition with given name found
    if not composition_dict:
        raise ValueError
    # Clear stop event
    stop_event.clear()
    # Set is_playing_composition to True
    is_playing_composition.set(True)
    # Stop any currently playing sound from running
    winsound.PlaySound(None, winsound.SND_PURGE)
    # Create play composition thread
    # Set to daemon to allow the app to exit and kill the thread instantly (not wait for it to finish)
    play_thread: threading.Thread = threading.Thread(target=play_composition, args=(composition_dict, ), daemon=True)
    # Start play composition thread
    play_thread.start()


def play_composition(composition_to_be_played: dict):
    """Plays the given composition
    """
    # Hide the Idle label
    idle_playing_label.place_forget()
    # Place Playing label
    playing_label.place(**start_stop_label_positions)
    # Create required variables for ease of access and memory efficiency
    notes_to_play_list: list = composition_to_be_played["Notes List"]
    # Note list index keeps track of the played note's position in the note list
    note_list_index: int = 0
    # Fetch the length of the notes list;
    # Used to configure relevant GUI elements, get out of function and ignore the last (redundant) delay
    note_list_length: int = len(notes_to_play_list)
    # Place & config the necessary GUI elements
    place_and_config_play_composition_gui_elements(progressbar_length=note_list_length)
    # Begin iterating over lists while playing the read note & waiting the read delay
    for full_note, delay in zip(notes_to_play_list, composition_to_be_played["Delays List"]):
        # Split full_note from notes list
        note_parts_list: list = full_note.split()
        note_parts_list_length: int = len(note_parts_list)
        # Create note variables
        instrument: str = "Piano"
        note_length: str = "None"
        # This means it is a piano note, but not a Do 1 or Do 2
        if note_parts_list_length == 3:
            note_name: str = note_parts_list[0]
            note_length = note_parts_list[1]
        # This means it is a Do 1 or Do 2 (piano)
        elif note_parts_list_length == 4:
            note_name: str = " ".join(note_parts_list[:2])
            note_length = note_parts_list[2]
        # This means it is a non-piano note
        else:
            instrument = note_parts_list[-1]
            note_name: str = note_parts_list[0]
        # Get path of note form note variables
        note_path: str = Sounds.get_instrument_sound_file_path(instrument=instrument,
                                                               note_name=note_name,
                                                               note_length=note_length)
        # Play sound
        winsound.PlaySound(note_path, winsound.SND_NOSTOP)
        # Increment progressbar value
        play_progress.set(play_progress.get() + 1)
        # Increment note list index by 1
        note_list_index += 1
        # Get out of function if the last note was played, thus ignoring the last delay
        # Also exit function if stop_event was set
        if note_list_index == note_list_length or stop_event.isSet():
            playing_label.place_forget()  # Hide Playing label
            if note_list_index == note_list_length and stop_event.isSet():
                cause: str = "Both"
            elif note_list_index == note_list_length:
                cause: str = "End"
            else:  # if stop_event.isSet()
                cause: str = "Event"
            stop_play_composition(cause)
            return None
        # Wait the delay, if it exists
        if delay > 0:
            time.sleep(delay)


def stop_play_composition(cause: str):
    """Stops playing composition
    """
    from GUI import config_sorted_menu

    # Place_forget composition playing GUI elements
    playing_label.place_forget()
    stopping_playing_label.place_forget()
    # Disable stop playing button
    stop_playing_button.config(state=DISABLED)

    # Boolean to sleep longer if the label text is longer
    sleep_long: bool = False

    # Update cause tracking variables
    if last_cause.get() == cause:
        if cause == "Event":
            stopped_counter.set(stopped_counter.get() + 1)
        elif cause == "End":
            ended_counter.set(ended_counter.get() + 1)
        else:  # cause == "Both"
            stopped_and_ended_counter.set(stopped_and_ended_counter.get() + 1)
    else:
        reset_composition_stop_cause_counters()

    # Configure & place message labels
    if cause == "Event":
        if stopped_counter.get() > 3:
            stopped_playing_label.config(text=stopped_playing_label_special_text)
            sleep_long = True
        else:
            stopped_playing_label.config(text=stopped_playing_label_default_text)
        stopped_playing_label.place(**start_stop_label_positions)
    elif cause == "End":
        if ended_counter.get() > 3:
            ended_playing_label.config(text=ended_playing_label_special_text)
        else:
            ended_playing_label.config(text=ended_playing_label_default_text)
        ended_playing_label.place(**start_stop_label_positions)
    else:  # cause == "Both"
        if stopped_and_ended_counter.get() > 3:
            stopped_and_ended_playing_label.config(text=stopped_and_ended_playing_label_special_text)
            sleep_long = True
        else:
            stopped_and_ended_playing_label.config(text=stopped_and_ended_playing_label_default_text)
        stopped_and_ended_playing_label.place(**start_stop_label_positions)

    # Increment Times Played stat of composition to play; Also updates GUI sorted menu
    # Only happens if composition got to the end of playing
    if cause == "End" or cause == "Both":
        increment_composition_times_played_stat()
        config_sorted_menu(composition=composition_to_play)

    # Set last cause to cause
    last_cause.set(cause)
    # Sleep for 2 seconds to allow the user to read the displayed label
    time.sleep(4 if sleep_long else 2.25)
    # Place forget stop button
    stop_playing_button.place_forget()
    # Place forget all labels
    stopped_playing_label.place_forget()
    ended_playing_label.place_forget()
    stopped_and_ended_playing_label.place_forget()
    # Place play button back on screen
    start_playing_button.place(**start_stop_button_positions)
    # Place Idle label back on screen
    idle_playing_label.place(**start_stop_label_positions)
    # Reset progressbar variable "progress"
    play_progress.set(0)
    # Set this boolean to false, re-enabling the composition playing GUI buttons
    is_playing_composition.set(False)


def reset_composition_stop_cause_counters():
    """Sets all the cause counter IntVar variables to 0
    Used in stop_play_composition and as a return_to_main_menu button command
    """
    stopped_counter.set(0)
    ended_counter.set(0)
    stopped_and_ended_counter.set(0)


def place_and_config_play_composition_gui_elements(progressbar_length: int):
    """Places & configures the necessary GUI elements for composition playing
    """
    # Place & configure the stop playing button
    start_playing_button.place_forget()
    stop_playing_button.place(**start_stop_button_positions)
    stop_playing_button.config(state=NORMAL, text="Stop Audition")
    # Configure & place progressbar
    playback_composition_progressbar.config(maximum=progressbar_length)


def is_new_composition_name_valid(composition_name: StringVar):
    """Checks if a new composition name is original/unused
    """
    # Remove leading and trailing whitespaces
    composition_name.set(composition_name.get().lstrip().rstrip())
    # Get name
    name: str = composition_name.get()
    # Check if name is not space nor already used/taken
    if Misc.empty_string(name):
        return False
    if is_composition_name_already_used(name):
        return False
    return True


def is_composition_name_already_used(composition_name: str):
    """Checks if given composition name is already used by another user (or same user)
    """
    global invalid_used_composition_name_owner_username
    # Check if name is already used or not
    for user in User.user_dict:
        for composition in User.user_dict[user]["Compositions"]:
            if composition_name == composition["Name"]:
                if User.user_dict[user]["Credentials"]["Username"] == User.logged_in_user["Credentials"]["Username"]:
                    invalid_used_composition_name_owner_username = "yourself"
                    return True
                # Imaginary elif; is just an if
                if User.user_dict[user]["Privacy"] == "Private" or \
                        User.user_dict[user]["Privacy"] == "Private Compositions":
                    invalid_used_composition_name_owner_username = "a private user"
                    return True
                # Imaginary else:
                invalid_used_composition_name_owner_username = User.user_dict[user]["Credentials"]["Username"]
                return True
    invalid_used_composition_name_owner_username = ""
    return False


def give_composition_rating():
    """Gives selected rating to composition
    """
    global composition_to_play

    # Get formatted rating str; is of type int if rating exists, str otherwise
    given_rating_formatted: str = Misc.get_number_from_rating(rating=given_rating.get())

    # Required boolean variables
    is_modified: bool = False
    is_rated: bool = False

    # Start iterating through all given ratings
    for rating in User.logged_in_user["Given Ratings"]:

        # Sanity checks
        assert type(rating) == dict
        assert len(rating.keys()) == 1

        # If rating exists
        if rating.get(composition_to_play["Name"]) is not None:
            is_rated = True
            if rating[composition_to_play["Name"]] != given_rating_formatted:

                # Will change existing rating
                if given_rating_formatted != Misc.NO_RATING:

                    # Start searching the composition
                    found: bool = False
                    for user in User.user_dict:
                        for index, composition in enumerate(User.user_dict[user]["Compositions"]):
                            if composition["Name"] == composition_to_play["Name"]:
                                # Accessibility variables
                                change_from_rating_key: str = str(rating[composition_to_play["Name"]])
                                change_to_rating_key: str = str(given_rating_formatted)
                                change_from_rating_value: int = composition["Rating"][change_from_rating_key]
                                change_to_rating_value: int = composition["Rating"][change_to_rating_key]

                                # Calculate new values
                                change_from_new_rating_value: int = change_from_rating_value - 1
                                change_to_new_rating_value: int = change_to_rating_value + 1

                                # If user is logged_in_user, update its dictionary
                                if User.user_dict[user]["Credentials"]["Username"] == \
                                        User.logged_in_user["Credentials"]["Username"]:
                                    # Remove 1 from old rating
                                    User.logged_in_user["Compositions"][index]["Rating"].update(
                                        {change_from_rating_key: change_from_new_rating_value})
                                    # Add 1 to current rating
                                    User.logged_in_user["Compositions"][index]["Rating"].update(
                                        {change_to_rating_key: change_to_new_rating_value})
                                # Else update user dict
                                else:
                                    # Remove 1 from old rating
                                    User.user_dict[user]["Compositions"][index]["Rating"].update(
                                        {change_from_rating_key: change_from_new_rating_value})
                                    # Add 1 to current rating
                                    User.user_dict[user]["Compositions"][index]["Rating"].update(
                                        {change_to_rating_key: change_to_new_rating_value})
                                found = True
                                break
                        if found:
                            break

                    # Change rating from logged in user dict
                    rating[composition_to_play["Name"]] = given_rating_formatted
                    assert type(rating[composition_to_play["Name"]]) == int  # Just to be sure
                    is_modified = True
                    break

                # Will remove existing rating
                else:

                    # Start searching the composition
                    found: bool = False
                    for user in User.user_dict:
                        for index, composition in enumerate(User.user_dict[user]["Compositions"]):
                            if composition["Name"] == composition_to_play["Name"]:
                                # Accessibility variables
                                change_from_rating_key: str = str(rating[composition_to_play["Name"]])
                                change_from_rating_value: int = composition["Rating"][change_from_rating_key]

                                # Calculate new value
                                change_from_new_rating_value: int = change_from_rating_value - 1

                                # If user is logged_in_user, update its dictionary
                                if User.user_dict[user]["Credentials"]["Username"] == \
                                        User.logged_in_user["Credentials"]["Username"]:
                                    # Remove 1 from old rating
                                    User.logged_in_user["Compositions"][index]["Rating"].update(
                                        {change_from_rating_key: change_from_new_rating_value})
                                # Else update user dict
                                else:
                                    # Remove 1 from old rating
                                    User.user_dict[user]["Compositions"][index]["Rating"].update(
                                        {change_from_rating_key: change_from_new_rating_value})
                                found = True
                                break
                        if found:
                            break

                    # Remove rating from logged in user dict
                    User.logged_in_user["Given Ratings"].remove(rating)
                    is_modified = True
                    break

    # Will add rating if it was not existent
    if not is_rated and given_rating_formatted != Misc.NO_RATING:

        # Start searching the composition
        found: bool = False
        for user in User.user_dict:
            for index, composition in enumerate(User.user_dict[user]["Compositions"]):
                if composition["Name"] == composition_to_play["Name"]:
                    # Accessibility variables
                    change_to_rating_key: str = str(given_rating_formatted)
                    change_to_rating_value: int = composition["Rating"][change_to_rating_key]

                    # Calculate new value
                    change_to_new_rating_value: int = change_to_rating_value + 1

                    # If user is logged_in_user, update its dictionary
                    if User.user_dict[user]["Credentials"]["Username"] == \
                            User.logged_in_user["Credentials"]["Username"]:
                        # Add 1 to current rating
                        User.logged_in_user["Compositions"][index]["Rating"].update(
                            {change_to_rating_key: change_to_new_rating_value})
                    # Else update user dict
                    else:
                        # Add 1 to current rating
                        User.user_dict[user]["Compositions"][index]["Rating"].update(
                            {change_to_rating_key: change_to_new_rating_value})
                    found = True
                    break
            if found:
                break

        # Add given rating to logged in user dict
        User.logged_in_user["Given Ratings"].append({composition_to_play["Name"]: given_rating_formatted})
        is_modified = True

    # Copy logged in user to user dict
    if is_modified:
        for user in User.user_dict:
            if User.user_dict[user]["Credentials"]["Username"] == User.logged_in_user["Credentials"]["Username"]:
                # Copy logged in user dict to user dict element of logged in user
                # Creates strange behaviour with numbers if not done (non-matching numbers)
                User.user_dict[user] = User.logged_in_user
                User.write_users_in_file()
                User.write_logged_in_user_in_file(True)
                break
        for user in User.user_dict:
            for index, composition in enumerate(User.user_dict[user]["Compositions"]):
                if composition["Name"] == composition_to_play["Name"]:
                    composition_to_play = copy.deepcopy(composition)


def increment_composition_times_played_stat():
    """Increments the "Number of Times Played" stat of the currently playing composition
    """
    global composition_to_play

    # Required boolean variables
    modify_logged_user: bool = False
    found: bool = False

    # Start searching the composition
    for user in User.user_dict:
        for index, composition in enumerate(User.user_dict[user]["Compositions"]):

            if composition["Name"] == composition_to_play["Name"]:

                assert type(composition["Played"]) == int and composition["Played"] >= 0

                # Increment played stat in user dict
                User.user_dict[user]["Compositions"][index]["Played"] += 1

                # If composition belongs to logged in user
                if User.user_dict[user]["Credentials"]["Username"] == User.logged_in_user["Credentials"]["Username"]:
                    # Update played stat in logged in user dict
                    User.logged_in_user["Compositions"][index]["Played"] = \
                        User.user_dict[user]["Compositions"][index]["Played"]
                    modify_logged_user = True

                # Update composition to play with the incremented stat one
                composition_to_play = copy.deepcopy(composition)

                found = True
                break
        if found:
            break

    assert found  # Sanity check

    # Update user files
    User.write_users_in_file()
    if modify_logged_user:
        User.write_logged_in_user_in_file(True)


"""Composition Sorting-Related Functions"""


def is_any_invalid_sorting_option_get():
    """Recalculates the truth value of the any_invalid_sorting_option boolean variable
    """
    # Returns True if at least one sorting option is invalid; False if all none are True
    any_invalid_option_bool: bool = is_invalid_user_sorting_option.get() or is_invalid_length_sorting_option.get() \
        or is_invalid_date_sorting_option.get() or is_invalid_rating_sorting_option.get()
    return any_invalid_option_bool


def get_sort_by_user_option(combobox_values: list, listbox_values: list):
    """Sorts by User
    """
    if sort_by_user.get() == "Any":
        return combobox_values
    elif sort_by_user.get() == "Specific":
        return [sort_user_selected_user.get()]  # list
    else:  # sort_by_user.get() == "Multiple"
        if user_inclusive_exclusive.get() == "Inclusive":
            return listbox_values
        else:  # user_inclusive_exclusive.get() == "Exclusive"
            return list(set(combobox_values) - set(listbox_values))  # Users in all_users, but not in list_box_values


def get_sort_by_length_option():
    """Sorts by Length
    """
    if sort_by_length.get() == "Any":
        return list(POSSIBLE_LENGTHS_TUPLE)
    elif sort_by_length.get() == "Specific":
        return [specific_length.get()]
    else:  # sort_by_length.get() == "Multiple"
        selection_list: list = []
        if short_length.get():
            selection_list.append("Short")
        if medium_length.get():
            selection_list.append("Medium")
        if long_length.get():
            selection_list.append("Long")
        return selection_list


def get_sort_by_date_option():
    """Sorts by Date
    """
    if sort_by_date.get() == "Any":
        return ["Any"]
    elif sort_by_date.get() == "Specific":
        return [datetime.date(year=int(sort_date_selected_year.get()),
                              month=Misc.MONTHS_DICT[sort_date_selected_month.get()],
                              day=int(sort_date_selected_day.get())),
                date_specific_inclusive_exclusive.get()]
    else:  # sort_by_date.get() == "Interval"
        return [datetime.date(year=int(sort_date_selected_year_from.get()),
                              month=Misc.MONTHS_DICT[sort_date_selected_month_from.get()],
                              day=int(sort_date_selected_day_from.get())),
                datetime.date(year=int(sort_date_selected_year_to.get()),
                              month=Misc.MONTHS_DICT[sort_date_selected_month_to.get()],
                              day=int(sort_date_selected_day_to.get())),
                date_interval_inclusive_exclusive.get()]


def get_sort_by_rating_option():
    """Sorts by Rating
    """
    if sort_by_rating.get() == "Any":
        return ["None", 1, 2, 3, 4, 5]
    elif sort_by_rating.get() == "Specific":
        if specific_rating.get() == "None":
            return ["None"]
        else:
            return [int(specific_rating.get())]
    else:  # sort_by_rating.get() == "Multiple"
        selection_list: list = []
        if no_rating.get():
            selection_list.append("None")
        if star_1_rating.get():
            selection_list.append(1)
        if star_2_rating.get():
            selection_list.append(2)
        if star_3_rating.get():
            selection_list.append(3)
        if star_4_rating.get():
            selection_list.append(4)
        if star_5_rating.get():
            selection_list.append(5)
        return selection_list


def is_length_selection_match(composition: dict, selection: list):
    """Returns True if composition matches selection; False otherwise
    """
    assert composition["Length"] >= 0
    if composition["Length"] < 60:
        composition_length: str = "Short"
    elif 60 <= composition["Length"] <= 60 * 5:
        composition_length: str = "Medium"
    else:  # composition["Length"] > 60 * 5
        composition_length: str = "Long"
    for possible_length in selection:
        if possible_length == composition_length:
            return True
    return False


def is_date_selection_match(composition_creation_date: datetime.date, selection: list):
    """Returns True if composition matches selection; False otherwise
    """
    if len(selection) == 1:
        return True
    elif len(selection) == 2:
        if selection[-1] == "Inclusive":
            if selection[0] == composition_creation_date:
                return True
            return False
        else:  # selection[-1] == "Exclusive"
            if selection[0] != composition_creation_date:
                return True
            return False
    else:  # len(selection) == 3
        if selection[-1] == "Inclusive":
            if selection[0] <= composition_creation_date <= selection[1]:
                return True
            return False
        else:  # selection[-1] == "Exclusive"
            if composition_creation_date < selection[0] or composition_creation_date > selection[1]:
                return True
            return False


def is_rating_selection_match(composition: dict, selection: list):
    """Returns True if composition matches selection; False otherwise
    """
    if len(selection) == 6:
        return True
    else:
        # Start getting overall composition rating
        total_ratings: int = 0
        total_rating_points: int = 0
        for rating in composition["Rating"]:
            total_ratings += composition["Rating"][rating]
            total_rating_points += int(rating) * composition["Rating"][rating]
        if total_ratings:
            overall_rating: float = total_rating_points / total_ratings
        else:  # If no total_ratings (no ratings at all), it means the composition has no ratings
            overall_rating: str = "None"
        # Check if given ratings list matches the overall rating
        for rating in selection:
            if type(overall_rating) == str:
                assert overall_rating == "None"  # Just to be sure
                if overall_rating == rating:
                    return True
            elif int(overall_rating) == rating:
                return True
        return False


def sort_by_all_parameters(combobox_values: list, listbox_values: list):
    """Sorts by all possible parameters
    """
    global sorted_composition_list
    # Clear previous sorted compositions list
    sorted_composition_list = []
    # Get lists of all attributes
    usernames_list: list = get_sort_by_user_option(combobox_values=combobox_values, listbox_values=listbox_values)
    lengths_list: list = get_sort_by_length_option()
    date_option: list = get_sort_by_date_option()
    ratings_list: list = get_sort_by_rating_option()
    # Get actual user dicts from usernames
    users_list: list = []
    for username in usernames_list:
        for user in User.user_dict:
            if username == User.user_dict[user]["Credentials"]["Username"]:
                users_list.append(user)
    # Start sorting
    for user in users_list:
        for composition in User.user_dict[user]["Compositions"]:
            # Sort by length
            is_matching_length: bool = is_length_selection_match(composition=composition, selection=lengths_list)
            # Sort by date
            composition_creation_date: datetime.date = datetime.date(year=composition["Date Of Creation"]["Year"],
                                                                     month=composition["Date Of Creation"]["Month"],
                                                                     day=composition["Date Of Creation"]["Day"])
            is_matching_date: bool = is_date_selection_match(composition_creation_date=composition_creation_date,
                                                             selection=date_option)
            # Sort by rating
            is_matching_rating: bool = is_rating_selection_match(composition=composition, selection=ratings_list)
            if is_matching_length and is_matching_date and is_matching_rating:
                # Check not to have duplicates, just for safety
                is_duplicate: bool = False
                for already_sorted_composition in sorted_composition_list:
                    if already_sorted_composition["Name"] == composition["Name"]:
                        is_duplicate = True
                        break
                if not is_duplicate:
                    sorted_composition_list.append(composition)
