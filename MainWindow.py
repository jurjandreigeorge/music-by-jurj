"""
Contains the Main Window (root)
"""


# GUI-related Imports
from tkinter import Tk
from Misc import NOTE_ICON_PATH

"""Main Window"""
# Create Main Window (root)
root = Tk()
# Make root full screen, add icon bitmap & title
root.attributes('-fullscreen', True)
root.iconbitmap(bitmap=NOTE_ICON_PATH)
root.title("Music by Jurj v2.0")

# # Remove focus from any widget on mouse double click
# root.bind("<Double-Button>", lambda *args: root.focus())


"""Function(s)"""


def forget_all_widgets(window: Tk):
    """Removes all widgets from the given window and its children
    """
    # Inspired from https://stackoverflow.com/q/7290071/15454571
    widget_list: list = window.winfo_children()
    for item in widget_list:
        if item.winfo_children():
            widget_list.extend(item.winfo_children())
    for item in widget_list:
        item.place_forget()


"""Debug Only Function(s)"""


# def sink_all_labels(window: Tk):
#     """Sinks all widgets of the explicitly stated type from the given window and its children
#     """
#     from tkinter import Label, SUNKEN, Scale, Checkbutton
#     widget_list: list = window.winfo_children()
#     for item in widget_list:
#         if item.winfo_children():
#             widget_list.extend(item.winfo_children())
#     for item in widget_list:
#         if type(item) == Label or type(item) == Scale or type(item) == Checkbutton:
#             item.config(relief=SUNKEN)
