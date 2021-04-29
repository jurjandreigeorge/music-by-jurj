"""
Miscellaneous Module; Contains general functions and variables that serve diverse unspecific purposes thorought the app
"""


# Imports
import datetime
import calendar
import re
import os
import json
from typing import Union
# GUI-related Imports
from tkinter import StringVar, Text
from tkinter.constants import INSERT, END, NORMAL, DISABLED


"""Variables"""


# Genders tuple
GENDERS: tuple = ("Male", "Female", "Other", "Unspecified")


# Date variables
DAYS_TUPLE: tuple = tuple(day for day in range(1, 32))
WEEKDAYS_NAMES: tuple = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
MONTHS_NAMES: tuple = (
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
    "December"
)
MONTHS_DICT: dict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}


# Countries
with open(file=os.path.join(os.getcwd(), "Dependencies", "Countries", "Countries.json"),
          encoding="utf-8") as countries_file:
    COUNTRIES_DICT: dict = json.load(countries_file)
with open(file=os.path.join(os.getcwd(), "Dependencies", "Countries", "US_States.json"),
          encoding="utf-8") as us_states_file:
    US_STATES_DICT: dict = json.load(us_states_file)

COUNTRIES_NAMES: tuple = tuple(COUNTRIES_DICT.keys())
US_STATES_NAMES: tuple = tuple(US_STATES_DICT.values())


# Star Strings
NO_RATING: str = "None"
STAR_1: str = "★☆☆☆☆"
STAR_2: str = "★★☆☆☆"
STAR_3: str = "★★★☆☆"
STAR_4: str = "★★★★☆"
STAR_5: str = "★★★★★"

# Possible Ratings Tuple
POSSIBLE_RATINGS: tuple = (NO_RATING, STAR_1, STAR_2, STAR_3, STAR_4, STAR_5)

# Musical Note Icon Bitmap
NOTE_ICON_PATH: str = os.path.join(os.getcwd(), "Dependencies", "Others", "note.ico")


"""Functions"""


def get_percentage_by_part(part: float, whole: float):
    """Returns percentage by given amount of total
    """
    if not whole:
        return 0
    return 100 * float(part) / float(whole)


# def get_part_by_percentage(percent: float, whole: float):
#     """Returns amount of total by given percentage
#     """
#     return (percent * whole) / 100.0


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


def get_suffix(number: int):
    """Returns the corresponding number suffix
    """
    if number > 10:
        if number % 100 == 11 or number % 100 == 12 or number % 100 == 13:
            return "th"
    if number % 10 == 1:
        return "st"
    if number % 10 == 2:
        return "nd"
    if number % 10 == 3:
        return "rd"
    return "th"


def get_possessive(string: str):
    """Returns the corresponding possessive form
    """
    if string[-1].lower() == "s":
        return "\'"
    return "\'s"


def get_number_from_rating(rating: str):
    """Returns the number of stars in a rating as an int, except for None"""
    if rating == NO_RATING:
        return NO_RATING
    elif rating == STAR_1:
        return 1
    elif rating == STAR_2:
        return 2
    elif rating == STAR_3:
        return 3
    elif rating == STAR_4:
        return 4
    elif rating == STAR_5:
        return 5
    else:
        raise ValueError


def format_duration(duration: float, with_suggestion: bool = True):
    """Formats given duration (from seconds) to millennia, centuries, decades, years, days, hours, minutes and seconds
    """

    seconds: int = round(duration)

    if seconds == 0:
        return "≈ 0 seconds"

    minutes: int = seconds // 60
    if minutes > 0:
        seconds -= minutes * 60

    hours: int = minutes // 60
    if hours > 0:
        minutes -= hours * 60

    days: int = hours // 24
    if days > 0:
        hours -= days * 24

    years: int = days // 365
    if years > 0:
        days -= years * 365

    decades: int = years // 10
    if decades > 0:
        years -= decades * 10

    centuries: int = decades // 10
    if centuries > 0:
        decades -= centuries * 10

    millennia: int = centuries // 10
    if millennia > 0:
        centuries -= millennia * 10

    if millennia > 999 and with_suggestion:
        return "At least 1,000,000 years long! We suggest you take a break and go outside. Seriously."

    unit_values: list = [millennia, centuries, decades, years, days, hours, minutes, seconds]
    units: list = ["millennium", "century", "decade", "year", "day", "hour", "minute", "second"]
    final_result: list = []

    for number, unit in zip(unit_values, units):
        if number > 0:
            if number == 1:
                final_result.append(f"1 {unit}")
            else:
                if unit == "century":
                    unit = "centuries"
                elif unit == "millennium":
                    unit = "millennia"
                else:
                    unit += "s"
                final_result.append(f"{number} {unit}")

    if len(final_result) > 1:
        final_result = final_result[:-1] + ["and"] + final_result[-1:]
        return f"≈ {', '.join(final_result[:-2])} {' '.join(final_result[-2:])}"
    return f"≈ {final_result[0]}"


def format_number(value: int, with_plural: bool = False):
    """Properly formats the given int value; returns str
    """
    million: int = 1_000_000

    if value < million:
        return f"{'{:,}'.format(value)}"

    billion: int = 1_000_000_000

    if value < billion:
        millions: int = value // million
        if with_plural:
            if millions == 1:
                unit: str = "Million"
            else:
                unit: str = "Millions"
        else:
            unit: str = "Million"
        return f"{millions} {unit}"

    trillion: int = 1_000_000_000_000

    if value < trillion:
        billions: int = value // billion
        if with_plural:
            if billions == 1:
                unit: str = "Billion"
            else:
                unit: str = "Billions"
        else:
            unit: str = "Billion"
        return f"{billions} {unit}"

    quadrillion: int = 1_000_000_000_000_000

    if value < quadrillion:
        trillions: int = value // trillion
        if with_plural:
            if trillions == 1:
                unit: str = "Trillion"
            else:
                unit: str = "Trillions"
        else:
            unit: str = "Trillion"
        return f"{trillions} {unit}"

    quintillion: int = 1_000_000_000_000_000_000

    if value < quintillion:
        quadrillions: int = value // quadrillion
        if with_plural:
            if quadrillions == 1:
                unit: str = "Quadrillion"
            else:
                unit: str = "Quadrillions"
        else:
            unit: str = "Quadrillion"
        return f"{quadrillions} {unit}"

    sextillion: int = 1_000_000_000_000_000_000_000

    if value < sextillion:
        quintillions: int = value // quintillion
        if with_plural:
            if quintillions == 1:
                unit: str = "Quintillion"
            else:
                unit: str = "Quintillions"
        else:
            unit: str = "Quintillion"
        return f"{quintillions} {unit}"

    septillion: int = 1_000_000_000_000_000_000_000_000

    if value < septillion:
        sextillions: int = value // sextillion
        if with_plural:
            if sextillions == 1:
                unit: str = "Sextillion"
            else:
                unit: str = "Sextillions"
        else:
            unit: str = "Sextillion"
        return f"{sextillions} {unit}"

    return "Number → ∞"


def is_valid_date(year: str, month: str, day: str):
    """Validates given date
    """
    try:
        datetime.date(year=int(year), month=MONTHS_DICT[month], day=int(day))
    except (ValueError, KeyError):
        return False
    if datetime.date(year=int(year), month=MONTHS_DICT[month], day=int(day)) > datetime.date.today():
        return False
    return True


def is_date_1_bigger_than_date_2(date_1_year: str, date_1_month: str, date_1_day: str,
                                 date_2_year: str, date_2_month: str, date_2_day: str):
    """Checks if date 1 is bigger than date 2; Returns boolean
    """
    # Check if given parameters are valid dates; return None if not
    if not is_valid_date(year=date_1_year, month=date_1_month, day=date_1_day) \
            or not is_valid_date(year=date_2_year, month=date_2_month, day=date_2_day):
        return None
    # Create date variables
    date_1: datetime.date = datetime.date(year=int(date_1_year), month=MONTHS_DICT[date_1_month], day=int(date_1_day))
    date_2: datetime.date = datetime.date(year=int(date_2_year), month=MONTHS_DICT[date_2_month], day=int(date_2_day))
    # Return True if date 1 is bigger than date 2
    if date_1 > date_2:
        return True
    # Else return False
    return False


def format_date(year: int, month: int, day: int, with_day: bool = False):
    """Nicely formats the given date
    """
    date: str = f"The {day}{get_suffix(day)} of {calendar.month_name[month]}, {year}"
    if with_day:
        is_or_was: str = "is" if datetime.date.today() == datetime.date(year=year, month=month, day=day) else "was a"
        date += f"; It {is_or_was} {WEEKDAYS_NAMES[calendar.weekday(year=year, month=month, day=day)]}."
    return date


def clear_white_spaces(*args):
    """Clears any whitespace present in the given StringVar
    """
    compiled_expression: re.Pattern = re.compile(r'\s+')
    for var in args:
        var.set(compiled_expression.sub('', var.get()))


def clear_non_digit_nor_letter(*args):
    """Clears any character that's not a digit nor a letter from the given StringVar
    """
    compiled_expression: re.Pattern = re.compile(r'[\W_]+')
    for var in args:
        var.set(compiled_expression.sub('', var.get()))


def clear_non_letters(*args):
    """Clears every non-letter character from the given StringVar
    """
    compiled_expression: re.Pattern = re.compile(r'[^A-Za-z]+')
    for var in args:
        var.set(compiled_expression.sub('', var.get()))


def clear_non_digits(*args):
    """Clears every non-digit character from the given StringVar
    """
    compiled_expression: re.Pattern = re.compile(r'[^0-9]+')
    for var in args:
        var.set(compiled_expression.sub('', var.get()))


def clear_leading_and_trailing_whitespace(*args):
    """Clears the leading and trailing whitespaces of the StringVar variables given in the list
    """
    for var in args:
        var.set(var.get().strip())


def clear_extra_whitespaces(*args):
    """Clears any more than 1 consecutive space from the given StringVar
    """
    compiled_expression: re.Pattern = re.compile(r' +')
    for var in args:
        var.set(compiled_expression.sub(' ', var.get()))


def empty_string(name: str):
    """Validates given name and also checks
    """
    if not name or name.isspace():
        return True
    return False


def entry_character_length_limit(var: StringVar, amount: int):
    """Limits the amount of characters an entry text variable can have
    """
    if len(var.get()) > amount:
        var.set(var.get()[:amount])


def text_character_length_limit(text_text: StringVar, amount: int, text_widget: Text):
    """Limits the amount of characters a text widget text can have
    """
    if len(text_text.get()) > amount:
        # Cut the text to the maximum allowed length
        text_text.set(text_text.get()[:amount])
        # Get the current index of the cursor
        index: str = text_widget.index(index=INSERT)
        # Delete the old (too long) text and place the new one (maximum length or shorter) in it's place
        text_widget.delete(index1="1.0", index2=END)
        text_widget.insert(index="1.0", chars=text_text.get())
        # Insert the cursor back in its original position from before deleting the text
        text_widget.mark_set(markName=INSERT, index=index)


def remove_text_widget_leading_and_trailing_whitespaces(text_text: StringVar, text_widget: Text):
    """Removes leading and trailing whitespaces form the given text widget's text
    """
    # Clear whitespaces from text variable
    text_text.get().lstrip().rstrip()
    # Delete the old text and insert the new one in its place
    text_widget.delete(index1="1.0", index2=END)
    text_widget.insert(index="1.0", chars=text_text.get())
    # Insert the cursor to the end
    text_widget.mark_set(markName=INSERT, index=END)


def copy_var_value_to_text_widget(text_text: StringVar, text_widget: Text):
    """Copies a StringVar value to the given text widget's contents
    """
    # Get the current index of the cursor
    index: str = text_widget.index(index=INSERT)
    # Delete the text contents and insert the variable contents
    text_widget.delete(index1="1.0", index2=END)
    text_widget.insert(index="1.0", chars=text_text.get())
    # Insert the cursor back in its original position from before deleting the text
    text_widget.mark_set(markName=INSERT, index=index)


def copy_var_value_to_disabled_text_widget(text_text: Union[str, StringVar], text_widget: Text):
    """Copies the given value in the given text widget and disables said text widget
    """
    # Enable text_widget so it is possible to edit contents
    text_widget.config(state=NORMAL)
    # Delete all text in text_widget
    text_widget.delete(index1="1.0", index2=END)
    # Insert text_text in text_widget
    if type(text_text) == str:
        text_widget.insert(index="1.0", chars=text_text)
    else:  # type(text_text) == StringVar
        text_widget.insert(index="1.0", chars=text_text.get())
    # Disable text_widget to make any other value edits impossible
    text_widget.config(state=DISABLED)


# def copy_var_value_to_readonly_entry_widget(entry_text: Union[str, StringVar], entry_widget: Entry):
#     """Copies the given value in the given entry widget and makes said entry widget readonly
#     """
#     # Enable text_widget so it is possible to edit contents
#     entry_widget.config(state=NORMAL)
#     # Delete all text in text_widget
#     entry_widget.delete(first=0, last=END)
#     # Insert text_text in text_widget
#     if type(entry_text) == str:
#         entry_widget.insert(index=0, string=entry_text)
#     else:  # type(text_text) == StringVar
#         entry_widget.insert(index=0, string=entry_text.get())
#     # Disable text_widget to make any other value edits impossible
#     entry_widget.config(state="readonly")


# def get_file_name_from_path(file_path: str):
#     """Returns the file name form the given file path
#     """
#     # File name must not contain any slashes/backslashes in its name for this function to properly work
#     file_name, file_extension = os.path.splitext(file_path)
#     file_name = os.path.basename(file_name)
#     return file_name, file_extension
