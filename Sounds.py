"""
Sounds module; Consists of Sounds-related functions and associated variables
"""


# Imports
import winsound
import wave
import contextlib
import copy
import typing
import os
import Stats
# GUI-related Imports
from MainWindow import root
from tkinter import StringVar


"""Variables"""


# List of the available instruments
INSTRUMENTS_TUPLE: tuple = ("Piano", "Flute", "Trumpet", "Violin")

# Used to count played notes for each available instrument
NUMBER_OF_NOTES_PLAYED_CLEAN_DICT: dict = {
    "Total": 0,
    "Piano": {
        "Short": 0,
        "Long": 0
    },
    "Flute": 0,
    "Trumpet": 0,
    "Violin": 0
}

# Used to count played notes in individual app session
number_of_notes_played_freely: dict = copy.deepcopy(NUMBER_OF_NOTES_PLAYED_CLEAN_DICT)
number_of_notes_recorded: dict = copy.deepcopy(NUMBER_OF_NOTES_PLAYED_CLEAN_DICT)

# Number of notes variables:
default_number_of_notes_played_label_text: str = "Played 0 notes:"
default_number_of_piano_notes_played_label_text: str = "- 0 piano notes, 0 short & 0 long"
default_number_of_flute_notes_played_label_text: str = "- 0 flute notes"
default_number_of_trumpet_notes_played_label_text: str = "- 0 trumpet notes"
default_number_of_violin_notes_played_label_text: str = "- 0 violin notes"

# Instrument descriptions and available notes
PIANO_DESCRIPTION: str = "\tThe piano is an acoustic, stringed musical instrument invented in Italy by " \
                         "Bartolomeo Cristofori around the year 1700 (the exact year is uncertain), in which the " \
                         "strings are struck by wooden hammers that are coated with a softer material " \
                         "(modern hammers are covered with dense wool felt; some early pianos used leather).\n" \
                         "\tIt is played using a keyboard, which is a row of keys (small levers) that the " \
                         "performer presses down or strikes with the fingers and thumbs of both hands to cause the " \
                         "hammers to strike the strings.\n" \
                         "\tThe word piano is a shortened form of pianoforte, the Italian term for the early " \
                         "1700s versions of the instrument, which in turn derives from gravicembalo col " \
                         "piano e forte (key cymbal with quieter and louder) and fortepiano. The Italian " \
                         "musical terms piano and forte indicate \"soft\" and \"loud\" respectively, in this " \
                         "context referring to the variations in volume (i.e., loudness) produced in response " \
                         "to a pianist's touch or pressure on the keys: the greater the velocity of a key press, " \
                         "the greater the force of the hammer hitting the strings, and the louder the sound of " \
                         "the note produced and the stronger the attack. The name was created as a contrast to " \
                         "harpsichord, a musical instrument that does not allow variation in volume; compared " \
                         "to the harpsichord, the first fortepianos in the 1700s had a quieter sound " \
                         "and smaller dynamic range." \
                          "\n\tSource: Wikipedia, the free encyclopedia"
PIANO_NOTES_TUPLE: tuple = ("Do 1", "Re", "Mi", "Fa", "Sol", "La", "Si", "Do 2")
PIANO_NOTES: str = '    '.join(PIANO_NOTES_TUPLE)

FLUTE_DESCRIPTION: str = "\tThe flute is a family of musical instruments in the woodwind group.\n" \
                         "\tUnlike woodwind instruments with reeds, a flute is an aerophone or reedless wind " \
                         "instrument that produces its sound from the flow of air across an opening.\n" \
                         "\tAccording to the instrument classification of Hornbostel–Sachs, flutes are " \
                         "categorized as edge-blown aerophones.\n" \
                         "\tA musician who plays the flute can be referred to as a flute player, flautist, " \
                         "flutist or, less commonly, fluter or flutenist.\n" \
                         "\tFlutes are the earliest known identifiable musical instruments, as paleolithic " \
                         "examples with hand-bored holes have been found. A number of flutes dating to about " \
                         "43,000 to 35,000 years ago have been found in the Swabian Jura region of " \
                         "present-day Germany. These flutes demonstrate that a developed musical tradition " \
                         "existed from the earliest period of modern human presence in Europe. While the " \
                         "oldest flutes currently known were found in Europe, Asia too has a long history with " \
                         "the instrument that has continued into the present day. In China, a playable bone " \
                         "flute was discovered, about 9000 years old. The Americas also had an ancient flute " \
                         "culture, with instruments found in Caral, Peru, dating back 5000 years and Labrador " \
                         "dating back approximately 7500 years." \
                          "\n\tSource: Wikipedia, the free encyclopedia"
FLUTE_NOTES_TUPLE: tuple = ("C4", "C5", "C6", "G4", "G5", "G6")
FLUTE_NOTES: str = '    '.join(FLUTE_NOTES_TUPLE)

TRUMPET_DESCRIPTION: str = "\tThe trumpet is a brass instrument commonly used in classical and jazz ensembles. " \
                           "The trumpet group ranges from the piccolo trumpet with the highest register in " \
                           "the brass family, to the bass trumpet, which is pitched one octave below the " \
                           "standard B♭ or C Trumpet.\n" \
                           "\tTrumpet-like instruments have historically been used as signalling devices in " \
                           "battle or hunting, with examples dating back to at least 1500 BCE. They began to be " \
                           "used as musical instruments only in the late 14th or early 15th century.\n" \
                           "\tTrumpets are used in art music styles, for instance in orchestras, concert bands, " \
                           "and jazz ensembles, as well as in popular music.\n" \
                           "\tThey are played by blowing air " \
                           "through nearly-closed lips (called the player's embouchure), producing a \"buzzing\" " \
                           "sound that starts a standing wave vibration in the air column inside the instrument. " \
                           "Since the late 15th century, trumpets have primarily been constructed of brass tubing, " \
                           "usually bent twice into a rounded rectangular shape." \
                          "\n\tSource: Wikipedia, the free encyclopedia"
TRUMPET_NOTES_TUPLE: tuple = ("C4", "C5", "C6", "G3", "G4", "G5")
TRUMPET_NOTES: str = '    '.join(TRUMPET_NOTES_TUPLE)

VIOLIN_DESCRIPTION: str = "\tThe violin, sometimes known as a fiddle, is a wooden chordophone (string instrument) " \
                          "in the violin family. Most violins have a hollow wooden body. It is the smallest and " \
                          "thus highest-pitched instrument (soprano) in the family in regular use. The violin " \
                          "typically has four strings, usually tuned in perfect fifths with notes G3, D4, A4, E5, " \
                          "and is most commonly played by drawing a bow across its strings. It can also be " \
                          "played by plucking the strings with the fingers (pizzicato) and, in specialized " \
                          "cases, by striking the strings with the wooden side of the bow (col legno).\n" \
                          "\tViolins are important instruments in a wide variety of musical genres. They are most " \
                          "prominent in the Western classical tradition, both in ensembles (from chamber " \
                          "music to orchestras) and as solo instruments. Violins are also important in many " \
                          "varieties of folk music, including country music, bluegrass music and in jazz. " \
                          "Electric violins with solid bodies and piezoelectric pickups are used in some forms of " \
                          "rock music and jazz fusion, with the pickups plugged into instrument amplifiers and " \
                          "speakers to produce sound. The violin has come to be incorporated in many non-Western " \
                          "music cultures, including Indian music and Iranian music. The name fiddle is often " \
                          "used regardless of the type of music played on it.\n" \
                          "\tThe violin was first known in 16th-century Italy, with some further modifications " \
                          "occurring in the 18th and 19th centuries to give the instrument a more powerful " \
                          "sound and projection. In Europe, it served as the basis for the development of " \
                          "other stringed instruments used in Western classical music, such as the viola." \
                          "\n\tSource: Wikipedia, the free encyclopedia"
VIOLIN_NOTES_TUPLE: tuple = ("C4", "C5", "C6", "G4", "G5", "G6")
VIOLIN_NOTES: str = '    '.join(VIOLIN_NOTES_TUPLE)


"""GUI Sounds (Not Notes)"""

# GUI elements sounds
BUTTON_SOUND_PATH: str = os.path.join(os.getcwd(), "Dependencies", "Sounds", "GUI", "Button.wav")
RADIOBUTTON_SOUND_PATH: str = os.path.join(os.getcwd(), "Dependencies", "Sounds", "GUI", "Radiobutton.wav")
# Also used for OptionMenus (checkbutton)
CHECKBUTTON_SOUND_PATH: str = os.path.join(os.getcwd(), "Dependencies", "Sounds", "GUI", "Checkbutton.wav")

# Key events (settings change with key presses)
CLEAR_SOUND_PATH: str = os.path.join(os.getcwd(), "Dependencies", "Sounds", "GUI", "Clear.wav")
SELECT_SOUND_PATH: str = os.path.join(os.getcwd(), "Dependencies", "Sounds", "GUI", "Select.wav")
# Rating events (1 star rating / 5 star rating)
BAD_RATE_SOUND_PATH: str = os.path.join(os.getcwd(), "Dependencies", "Sounds", "GUI", "BadRating.wav")
GOOD_RATE_SOUND_PATH: str = os.path.join(os.getcwd(), "Dependencies", "Sounds", "GUI", "GoodRating.wav")


"""GUI Variables"""


# Used to set the "choose instrument" option menu option
chosen_instrument: StringVar = StringVar(root)
chosen_instrument.set(INSTRUMENTS_TUPLE[0])

# Used to store the last used instrument
last_used_instrument: typing.Union[str, None] = None

# Used to set the length of piano notes
piano_note_length: StringVar = StringVar(root)
piano_note_length.set("Short")

# Used to determine the description of the current chosen instrument
chosen_instrument_description: StringVar = StringVar(root)
chosen_instrument_description.set("")

# Used to determine the available notes of the current chosen instrument
chosen_instrument_available_notes: StringVar = StringVar(root)
chosen_instrument_available_notes.set("")


"""Functions"""


def play_gui_sound(sound_file_path: str):
    """Plays the GUI sound given at the given path
    """
    # Play sound
    winsound.PlaySound(sound_file_path, winsound.SND_ASYNC)


def play_note(instrument: str, note_name: str, note_length: str = "None"):
    """Plays the desired musical note
    """
    # Get file name
    sound_file_path: str = get_instrument_sound_file_path(instrument=instrument,
                                                          note_name=note_name,
                                                          note_length=note_length)
    # Play sound
    winsound.PlaySound(sound_file_path, winsound.SND_ASYNC)


def get_wav_file_length(file_path: str):
    """Returns the length of a .wav file, in seconds
    """
    # Taken from https://stackoverflow.com/a/7833963/15454571
    with contextlib.closing(wave.open(f=file_path, mode='r')) as wav_file:
        frames: int = wav_file.getnframes()
        rate: float = wav_file.getframerate()
        duration: float = frames / float(rate)
    return round(duration, 2)


def get_instrument_sound_file_path(instrument: str, note_name: str, note_length: str = "None"):
    """Returns file path depending on the given instrument, note name and note length (if instrument is piano)
    """
    # Initiate base file path
    file_path: str = os.path.join(os.getcwd(), "Dependencies", "Sounds", "Instruments")
    # Complete file path depending on the given variables
    if instrument == "Piano":
        if note_length in ("Short", "Long"):
            file_path = os.path.join(file_path, "Piano", note_length, f"{note_name} {note_length[0]} Piano")
        else:
            raise ValueError(f"Incorrect note_length argument: {note_length}. Must be either \"Short\" or \"Long\"!")
    else:
        file_path = os.path.join(file_path, instrument, f"{note_name} {instrument}")
    # Add file extension to name; Any sound file must be of .wav type
    file_path += ".wav"
    return file_path


# def get_piano_note_full_length(note_name: str):
#     """Returns the full name of the given piano note
#     Only call on piano notes
#     """
#     note_name_list: list = note_name.split()
#     # Any note besides Do 1 or Do 2
#     if len(note_name_list) == 3:
#         index: int = 1
#     # Do 1 and Do 2 get split into lists with 4 elements
#     else:  # len(note_name_list) == 4
#         index: int = 2
#     # Replace initial letter of note length with full word
#     if note_name_list[index].upper() == "S":
#         note_name_list[index] = "Short"
#     else:  # note_name_list[1].upper() == "L"
#         note_name_list[index] = "Long"
#     # Return string concatenated from list elements
#     return " ".join(note_name_list)


"""Stats-involved Function(s)"""


def update_last_used_instrument(instrument: str):
    """Updates the last_used_instrument instrument variable
    """
    global last_used_instrument
    if last_used_instrument is None:
        # This branch gets executed when playing the first instrument once app started
        last_used_instrument = instrument
        return None
    if last_used_instrument == instrument:
        Stats.instrument_changed_decided_not_to.set(Stats.instrument_changed_decided_not_to.get() + 1)
    else:
        Stats.instrument_changed_successfully.set(Stats.instrument_changed_successfully.get() + 1)
    # Update last_used_instrument
    last_used_instrument = instrument
