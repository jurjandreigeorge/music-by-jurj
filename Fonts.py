"""
Fonts Module; Contains fonts for the GUI
"""


from tkinter.font import Font, nametofont, BOLD, ITALIC
from MainWindow import root
import Misc


"""Get Screen Width"""


SCREEN_WIDTH: int = root.winfo_screenwidth()
# 1920 is the screen width with which the app was designed
DEFAULT_SCREEN_WIDTH: int = 1920


"""Fonts"""


"""Fixed Font(s)"""

# Bold Fixed 25 Font
fixed_25: Font = nametofont("TkFixedFont")
fixed_25.configure(size=int(Misc.rule_of_3(x=25, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)), weight="bold")

"""Verdana Fonts"""
# Normal Verdana 10 Font
verdana_10: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=10, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 11 Font
verdana_11: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=11, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 13 Font
verdana_13: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=13, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 15 Font
verdana_15: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=15, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 17 Font
verdana_17: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=17, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 19 Font
verdana_19: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=19, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 20 Font
verdana_20: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=20, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Overstrike Verdana 20 Font
verdana_20_overstrike: Font = Font(root=root, family="Verdana", overstrike=1,
                                   size=int(Misc.rule_of_3(x=20, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 23 Font
verdana_23: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=23, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 25 Font
verdana_25: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=25, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Italic Verdana 25 Font
verdana_25_italic: Font = Font(root=root, family="Verdana", slant=ITALIC,
                               size=int(Misc.rule_of_3(x=25, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Overstrike Verdana 25 Font
verdana_25_overstrike: Font = Font(root=root, family="Verdana", overstrike=1,
                                   size=int(Misc.rule_of_3(x=25, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 28 Font
verdana_28: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=28, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 28 Underlined Font
verdana_28_underline: Font = Font(root=root, family="Verdana",
                                  size=int(Misc.rule_of_3(x=28, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)),
                                  underline=True)

# Normal Verdana 30 Font
verdana_30: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=30, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 32 Font
verdana_32: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=32, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 35 Font
verdana_35: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=35, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Italic Verdana 35 Font
verdana_35_italic: Font = Font(root=root, family="Verdana",
                               slant=ITALIC, size=int(Misc.rule_of_3(x=35, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 40 Font
verdana_40: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=40, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 45 Font
verdana_45: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=45, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Verdana 50 Font
verdana_50: Font = Font(root=root, family="Verdana",
                        size=int(Misc.rule_of_3(x=50, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

"""Times New Roman Font(s)"""

# Normal Times New Roman 25 Font
times_new_roman_25: Font = Font(root=root, family="Times New Roman",
                                size=int(Misc.rule_of_3(x=25, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

"""Tempus Sans ITC Font(s)"""

# Bold Tempus Sans ITC 20 Font
tempus_sans_itc_20_bold: Font = Font(root=root, family="Tempus Sans ITC",
                                     size=int(Misc.rule_of_3(x=20, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)),
                                     weight=BOLD)

# Bold Italic Tempus Sans ITC 43 Font
tempus_sans_itc_43_bold_italic: Font = Font(root=root, family="Tempus Sans ITC",
                                            size=int(Misc.rule_of_3(x=43, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)),
                                            weight=BOLD, slant=ITALIC)

# Bold Italic Tempus Sans ITC 50 Font
tempus_sans_itc_50_bold_italic: Font = Font(root=root, family="Tempus Sans ITC",
                                            size=int(Misc.rule_of_3(x=50, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)),
                                            weight=BOLD, slant=ITALIC)

"""Book Antiqua Font(s)"""

# Normal Book Antiqua 23 Font
book_antiqua_23: Font = Font(root=root, family="Book Antiqua",
                             size=int(Misc.rule_of_3(x=23, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Book Antiqua 35 Font
book_antiqua_35: Font = Font(root=root, family="Book Antiqua",
                             size=int(Misc.rule_of_3(x=35, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Italic Book Antiqua 49 Font
book_antiqua_49_italic: Font = Font(root=root, family="Book Antiqua",
                                    slant=ITALIC,
                                    size=int(Misc.rule_of_3(x=49, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

"""Main Title Font(s)"""

# Normal Courier 80 Font
courier_80: Font = Font(root=root, family="Courier",
                        size=int(Misc.rule_of_3(x=80, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))

# Normal Courier 100 Font
courier_100: Font = Font(root=root, family="Courier",
                         size=int(Misc.rule_of_3(x=100, a=DEFAULT_SCREEN_WIDTH, b=SCREEN_WIDTH)))
