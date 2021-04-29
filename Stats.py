"""
Stats module; Consists of stats-related functions and variables
"""

# Imports
import json
import os
import Misc
# GUI-related Imports
from MainWindow import root
from tkinter import IntVar, Label, LabelFrame
from tkinter.constants import W, SW
from tkinter.ttk import Separator, Style
from Fonts import verdana_15, verdana_20, verdana_20_overstrike, verdana_25, verdana_25_overstrike


"""Variables"""

# Stats json data file path
STATS_JSON_PATH: str = os.path.join(os.getcwd(), "Dependencies", "Stats", "Stats.json")


# Read Stats From File
with open(file=STATS_JSON_PATH, encoding="utf-8") as read_stats_file:
    stats: dict = json.load(read_stats_file)

# Determines whether or not stats were initiated
stats_initiated: bool = False

# ttk style; only used to set theme to classic
style: Style = Style()
style.theme_use(themename="classic")


"""GUI Variables"""


# Notes Played - Total
notes_played_total: IntVar = IntVar(root)

# Notes Played - Piano
piano_notes_played_total: IntVar = IntVar(root)
# Long Notes
long_piano_notes_played_total: IntVar = IntVar(root)

long_do_1_piano_notes_played: IntVar = IntVar(root)
long_re_piano_notes_played: IntVar = IntVar(root)
long_mi_piano_notes_played: IntVar = IntVar(root)
long_fa_piano_notes_played: IntVar = IntVar(root)
long_sol_piano_notes_played: IntVar = IntVar(root)
long_la_piano_notes_played: IntVar = IntVar(root)
long_si_piano_notes_played: IntVar = IntVar(root)
long_do_2_piano_notes_played: IntVar = IntVar(root)
# Short Notes
short_piano_notes_played_total: IntVar = IntVar(root)

short_do_1_piano_notes_played: IntVar = IntVar(root)
short_re_piano_notes_played: IntVar = IntVar(root)
short_mi_piano_notes_played: IntVar = IntVar(root)
short_fa_piano_notes_played: IntVar = IntVar(root)
short_sol_piano_notes_played: IntVar = IntVar(root)
short_la_piano_notes_played: IntVar = IntVar(root)
short_si_piano_notes_played: IntVar = IntVar(root)
short_do_2_piano_notes_played: IntVar = IntVar(root)

# Notes Played - Flute
flute_notes_played_total: IntVar = IntVar(root)

c4_flute_notes_played: IntVar = IntVar(root)
c5_flute_notes_played: IntVar = IntVar(root)
c6_flute_notes_played: IntVar = IntVar(root)
g4_flute_notes_played: IntVar = IntVar(root)
g5_flute_notes_played: IntVar = IntVar(root)
g6_flute_notes_played: IntVar = IntVar(root)

# Notes Played - Trumpet
trumpet_notes_played_total: IntVar = IntVar(root)

c4_trumpet_notes_played: IntVar = IntVar(root)
c5_trumpet_notes_played: IntVar = IntVar(root)
c6_trumpet_notes_played: IntVar = IntVar(root)
g3_trumpet_notes_played: IntVar = IntVar(root)
g4_trumpet_notes_played: IntVar = IntVar(root)
g5_trumpet_notes_played: IntVar = IntVar(root)

# Notes Played - Violin
violin_notes_played_total: IntVar = IntVar(root)

c4_violin_notes_played: IntVar = IntVar(root)
c5_violin_notes_played: IntVar = IntVar(root)
c6_violin_notes_played: IntVar = IntVar(root)
g4_violin_notes_played: IntVar = IntVar(root)
g5_violin_notes_played: IntVar = IntVar(root)
g6_violin_notes_played: IntVar = IntVar(root)

# Settings Changed
settings_changed_total: IntVar = IntVar(root)

settings_changed_background_color: IntVar = IntVar(root)
settings_changed_text_color: IntVar = IntVar(root)
settings_changed_buttons_color: IntVar = IntVar(root)
settings_changed_buttons_text_color: IntVar = IntVar(root)
settings_changed_invalid_text_color: IntVar = IntVar(root)
settings_changed_gui_sound: IntVar = IntVar(root)
settings_changed_remember_settings: IntVar = IntVar(root)

# Main Menu Interactions
main_menu_interactions_total: IntVar = IntVar(root)

# Count Towards Total
main_menu_interactions_played_freely: IntVar = IntVar(root)
main_menu_interactions_recorded_compositions: IntVar = IntVar(root)
main_menu_interactions_listened_compositions: IntVar = IntVar(root)
main_menu_interactions_managed_compositions: IntVar = IntVar(root)
main_menu_interactions_entered_settings: IntVar = IntVar(root)
main_menu_interactions_viewed_stats: IntVar = IntVar(root)
# Don't Count Towards Total
main_menu_interactions_viewed_more_stats: IntVar = IntVar(root)
main_menu_interactions_logged_in: IntVar = IntVar(root)
main_menu_interactions_logged_out: IntVar = IntVar(root)
main_menu_interactions_registered: IntVar = IntVar(root)

# Accounts
accounts_total: IntVar = IntVar(root)

accounts_active: IntVar = IntVar(root)
accounts_deleted: IntVar = IntVar(root)

# Compositions
compositions_total: IntVar = IntVar(root)

compositions_active: IntVar = IntVar(root)
compositions_deleted: IntVar = IntVar(root)

# Instrument Changed
instrument_changed_total: IntVar = IntVar(root)

instrument_changed_successfully: IntVar = IntVar(root)
instrument_changed_decided_not_to: IntVar = IntVar(root)

# Returned To Main Menu
returned_to_main_menu: IntVar = IntVar(root)

# App used
app_used_counter: IntVar = IntVar(root)


"""Trace Functions"""
# Used to determine what happens when one of the stats variables changes value


# Instruments

# All Instruments total Notes

notes_played_total.trace("w", lambda *args: [config_text_value_stat_labelframe(title="Notes Played",
                                                                               value=notes_played_total.get(),
                                                                               labelframe=notes_played_labelframe),
                                             write_stats() if stats_initiated else None
                                             ])

# Piano

# Total Notes
piano_notes_played_total.trace("w", lambda *args: [notes_played_total.
                               set(recalculate_total_notes_played()),
                                                   piano_notes_number_label.
                               config(text=Misc.format_number(piano_notes_played_total.get()))
                               ])

# Total Long Notes
long_piano_notes_played_total.trace("w", lambda *args: [piano_notes_played_total.
                                    set(recalculate_total_piano_notes_played()),
                                                        long_piano_notes_number_label.
                                    config(text=Misc.format_number(long_piano_notes_played_total.get()))
                                    ])

# Total Short Notes
short_piano_notes_played_total.trace("w", lambda *args: [piano_notes_played_total.
                                     set(recalculate_total_piano_notes_played()),
                                                         short_piano_notes_number_label.
                                     config(text=Misc.format_number(short_piano_notes_played_total.get()))
                                     ])

# Individual Long Notes
long_do_1_piano_notes_played.trace("w", lambda *args: [long_piano_notes_played_total.
                                   set(recalculate_total_short_or_long_piano_notes_played("long")),
                                                       do_1_long_number_label.
                                   config(text=Misc.format_number(long_do_1_piano_notes_played.get())),
                                                       update_stats_dict() if stats_initiated else None
                                   ])
long_re_piano_notes_played.trace("w", lambda *args: [long_piano_notes_played_total.
                                 set(recalculate_total_short_or_long_piano_notes_played("long")),
                                                     re_long_number_label.
                                 config(text=Misc.format_number(long_re_piano_notes_played.get())),
                                                     update_stats_dict() if stats_initiated else None
                                 ])
long_mi_piano_notes_played.trace("w", lambda *args: [long_piano_notes_played_total.
                                 set(recalculate_total_short_or_long_piano_notes_played("long")),
                                                     mi_long_number_label.
                                 config(text=Misc.format_number(long_mi_piano_notes_played.get())),
                                                     update_stats_dict() if stats_initiated else None
                                 ])
long_fa_piano_notes_played.trace("w", lambda *args: [long_piano_notes_played_total.
                                 set(recalculate_total_short_or_long_piano_notes_played("long")),
                                                     fa_long_number_label.
                                 config(text=Misc.format_number(long_fa_piano_notes_played.get())),
                                                     update_stats_dict() if stats_initiated else None
                                 ])
long_sol_piano_notes_played.trace("w", lambda *args: [long_piano_notes_played_total.
                                  set(recalculate_total_short_or_long_piano_notes_played("long")),
                                                      sol_long_number_label.
                                  config(text=Misc.format_number(long_sol_piano_notes_played.get())),
                                                      update_stats_dict() if stats_initiated else None
                                  ])
long_la_piano_notes_played.trace("w", lambda *args: [long_piano_notes_played_total.
                                 set(recalculate_total_short_or_long_piano_notes_played("long")),
                                                     la_long_number_label.
                                 config(text=Misc.format_number(long_la_piano_notes_played.get())),
                                                     update_stats_dict() if stats_initiated else None
                                 ])
long_si_piano_notes_played.trace("w", lambda *args: [long_piano_notes_played_total.
                                 set(recalculate_total_short_or_long_piano_notes_played("long")),
                                                     si_long_number_label.
                                 config(text=Misc.format_number(long_si_piano_notes_played.get())),
                                                     update_stats_dict() if stats_initiated else None
                                 ])
long_do_2_piano_notes_played.trace("w", lambda *args: [long_piano_notes_played_total.
                                   set(recalculate_total_short_or_long_piano_notes_played("long")),
                                                       do_2_long_number_label.
                                   config(text=Misc.format_number(long_do_2_piano_notes_played.get())),
                                                       update_stats_dict() if stats_initiated else None
                                   ])

# Individual Short Notes
short_do_1_piano_notes_played.trace("w", lambda *args: [short_piano_notes_played_total.
                                    set(recalculate_total_short_or_long_piano_notes_played("short")),
                                                        do_1_short_number_label.
                                    config(text=Misc.format_number(short_do_1_piano_notes_played.get())),
                                                        update_stats_dict() if stats_initiated else None
                                    ])
short_re_piano_notes_played.trace("w", lambda *args: [short_piano_notes_played_total.
                                  set(recalculate_total_short_or_long_piano_notes_played("short")),
                                                      re_short_number_label.
                                  config(text=Misc.format_number(short_re_piano_notes_played.get())),
                                                      update_stats_dict() if stats_initiated else None
                                  ])
short_mi_piano_notes_played.trace("w", lambda *args: [short_piano_notes_played_total.
                                  set(recalculate_total_short_or_long_piano_notes_played("short")),
                                                      mi_short_number_label.
                                  config(text=Misc.format_number(short_mi_piano_notes_played.get())),
                                                      update_stats_dict() if stats_initiated else None
                                  ])
short_fa_piano_notes_played.trace("w", lambda *args: [short_piano_notes_played_total.
                                  set(recalculate_total_short_or_long_piano_notes_played("short")),
                                                      fa_short_number_label.
                                  config(text=Misc.format_number(short_fa_piano_notes_played.get())),
                                                      update_stats_dict() if stats_initiated else None
                                  ])
short_sol_piano_notes_played.trace("w", lambda *args: [short_piano_notes_played_total.
                                   set(recalculate_total_short_or_long_piano_notes_played("short")),
                                                       sol_short_number_label.
                                   config(text=Misc.format_number(short_sol_piano_notes_played.get())),
                                                       update_stats_dict() if stats_initiated else None
                                   ])
short_la_piano_notes_played.trace("w", lambda *args: [short_piano_notes_played_total.
                                  set(recalculate_total_short_or_long_piano_notes_played("short")),
                                                      la_short_number_label.
                                  config(text=Misc.format_number(short_la_piano_notes_played.get())),
                                                      update_stats_dict() if stats_initiated else None
                                  ])
short_si_piano_notes_played.trace("w", lambda *args: [short_piano_notes_played_total.
                                  set(recalculate_total_short_or_long_piano_notes_played("short")),
                                                      si_short_number_label.
                                  config(text=Misc.format_number(short_si_piano_notes_played.get())),
                                                      update_stats_dict() if stats_initiated else None
                                  ])
short_do_2_piano_notes_played.trace("w", lambda *args: [short_piano_notes_played_total.
                                    set(recalculate_total_short_or_long_piano_notes_played("short")),
                                                        do_2_short_number_label.
                                    config(text=Misc.format_number(short_do_2_piano_notes_played.get())),
                                                        update_stats_dict() if stats_initiated else None
                                    ])

# Flute

# Total Notes
flute_notes_played_total.trace("w", lambda *args: [notes_played_total.
                               set(recalculate_total_notes_played()),
                                                   flute_notes_number_label.
                               config(text=Misc.format_number(flute_notes_played_total.get()))
                               ])

# Individual Notes
c4_flute_notes_played.trace("w", lambda *args: [flute_notes_played_total.
                            set(recalculate_total_flute_notes_played()),
                                                c4_flute_number_label.
                            config(text=Misc.format_number(c4_flute_notes_played.get())),
                                                update_stats_dict() if stats_initiated else None
                            ])
c5_flute_notes_played.trace("w", lambda *args: [flute_notes_played_total.
                            set(recalculate_total_flute_notes_played()),
                                                c5_flute_number_label.
                            config(text=Misc.format_number(c5_flute_notes_played.get())),
                                                update_stats_dict() if stats_initiated else None
                            ])
c6_flute_notes_played.trace("w", lambda *args: [flute_notes_played_total.
                            set(recalculate_total_flute_notes_played()),
                                                c6_flute_number_label.
                            config(text=Misc.format_number(c6_flute_notes_played.get())),
                                                update_stats_dict() if stats_initiated else None
                            ])
g4_flute_notes_played.trace("w", lambda *args: [flute_notes_played_total.
                            set(recalculate_total_flute_notes_played()),
                                                g4_flute_number_label.
                            config(text=Misc.format_number(g4_flute_notes_played.get())),
                                                update_stats_dict() if stats_initiated else None
                            ])
g5_flute_notes_played.trace("w", lambda *args: [flute_notes_played_total.
                            set(recalculate_total_flute_notes_played()),
                                                g5_flute_number_label.
                            config(text=Misc.format_number(g5_flute_notes_played.get())),
                                                update_stats_dict() if stats_initiated else None
                            ])
g6_flute_notes_played.trace("w", lambda *args: [flute_notes_played_total.
                            set(recalculate_total_flute_notes_played()),
                                                g6_flute_number_label.
                            config(text=Misc.format_number(g6_flute_notes_played.get())),
                                                update_stats_dict() if stats_initiated else None
                            ])

# Trumpet

# Total Notes
trumpet_notes_played_total.trace("w", lambda *args: [notes_played_total.
                                 set(recalculate_total_notes_played()),
                                                     trumpet_notes_number_label.
                                 config(text=Misc.format_number(trumpet_notes_played_total.get()))
                                 ])

# Individual Notes
c4_trumpet_notes_played.trace("w", lambda *args: [trumpet_notes_played_total.
                              set(recalculate_total_trumpet_notes_played()),
                                                  c4_trumpet_number_label.
                              config(text=Misc.format_number(c4_trumpet_notes_played.get())),
                                                  update_stats_dict() if stats_initiated else None
                              ])
c5_trumpet_notes_played.trace("w", lambda *args: [trumpet_notes_played_total.
                              set(recalculate_total_trumpet_notes_played()),
                                                  c5_trumpet_number_label.
                              config(text=Misc.format_number(c5_trumpet_notes_played.get())),
                                                  update_stats_dict() if stats_initiated else None
                              ])
c6_trumpet_notes_played.trace("w", lambda *args: [trumpet_notes_played_total.
                              set(recalculate_total_trumpet_notes_played()),
                                                  c6_trumpet_number_label.
                              config(text=Misc.format_number(c6_trumpet_notes_played.get())),
                                                  update_stats_dict() if stats_initiated else None
                              ])
g3_trumpet_notes_played.trace("w", lambda *args: [trumpet_notes_played_total.
                              set(recalculate_total_trumpet_notes_played()),
                                                  g3_trumpet_number_label.
                              config(text=Misc.format_number(g3_trumpet_notes_played.get())),
                                                  update_stats_dict() if stats_initiated else None
                              ])
g4_trumpet_notes_played.trace("w", lambda *args: [trumpet_notes_played_total.
                              set(recalculate_total_trumpet_notes_played()),
                                                  g4_trumpet_number_label.
                              config(text=Misc.format_number(g4_trumpet_notes_played.get())),
                                                  update_stats_dict() if stats_initiated else None
                              ])
g5_trumpet_notes_played.trace("w", lambda *args: [trumpet_notes_played_total.
                              set(recalculate_total_trumpet_notes_played()),
                                                  g5_trumpet_number_label.
                              config(text=Misc.format_number(g5_trumpet_notes_played.get())),
                                                  update_stats_dict() if stats_initiated else None
                              ])

# Violin

# Total Notes
violin_notes_played_total.trace("w", lambda *args: [notes_played_total.
                                set(recalculate_total_notes_played()),
                                                    violin_notes_number_label.
                                config(text=Misc.format_number(violin_notes_played_total.get()))
                                ])

# Individual Notes
c4_violin_notes_played.trace("w", lambda *args: [violin_notes_played_total.
                             set(recalculate_total_violin_notes_played()),
                                                 c4_violin_number_label.
                             config(text=Misc.format_number(c4_violin_notes_played.get())),
                                                 update_stats_dict() if stats_initiated else None
                             ])
c5_violin_notes_played.trace("w", lambda *args: [violin_notes_played_total.
                             set(recalculate_total_violin_notes_played()),
                                                 c5_violin_number_label.
                             config(text=Misc.format_number(c5_violin_notes_played.get())),
                                                 update_stats_dict() if stats_initiated else None
                             ])
c6_violin_notes_played.trace("w", lambda *args: [violin_notes_played_total.
                             set(recalculate_total_violin_notes_played()),
                                                 c6_violin_number_label.
                             config(text=Misc.format_number(c6_violin_notes_played.get())),
                                                 update_stats_dict() if stats_initiated else None
                             ])
g4_violin_notes_played.trace("w", lambda *args: [violin_notes_played_total.
                             set(recalculate_total_violin_notes_played()),
                                                 g4_violin_number_label.
                             config(text=Misc.format_number(g4_violin_notes_played.get())),
                                                 update_stats_dict() if stats_initiated else None
                             ])
g5_violin_notes_played.trace("w", lambda *args: [violin_notes_played_total.
                             set(recalculate_total_violin_notes_played()),
                                                 g5_violin_number_label.
                             config(text=Misc.format_number(g5_violin_notes_played.get())),
                                                 update_stats_dict() if stats_initiated else None
                             ])
g6_violin_notes_played.trace("w", lambda *args: [violin_notes_played_total.
                             set(recalculate_total_violin_notes_played()),
                                                 g6_violin_number_label.
                             config(text=Misc.format_number(g6_violin_notes_played.get())),
                                                 update_stats_dict() if stats_initiated else None
                             ])

# Settings
settings_changed_total.trace("w", lambda *args: [config_text_value_times_stat_labelframe(
    title="Settings Changed", value=settings_changed_total.get(), labelframe=settings_changed_labelframe),
    write_stats() if stats_initiated else None
])

settings_changed_background_color.trace("w", lambda *args: [settings_changed_total.
                                        set(recalculate_total_setting_changes()),
                                                            background_color_changed_number_label.
                                        config(text=Misc.format_number(settings_changed_background_color.get())),
                                                            update_stats_dict() if stats_initiated else None
                                        ])
settings_changed_text_color.trace("w", lambda *args: [settings_changed_total.
                                  set(recalculate_total_setting_changes()),
                                                      text_color_changed_number_label.
                                  config(text=Misc.format_number(settings_changed_text_color.get())),
                                                      update_stats_dict() if stats_initiated else None
                                  ])
settings_changed_buttons_color.trace("w", lambda *args: [settings_changed_total.
                                     set(recalculate_total_setting_changes()),
                                                         button_color_changed_number_label.
                                     config(text=Misc.format_number(settings_changed_buttons_color.get())),
                                                         update_stats_dict() if stats_initiated else None
                                     ])
settings_changed_buttons_text_color.trace("w", lambda *args: [settings_changed_total.
                                          set(recalculate_total_setting_changes()),
                                                              button_text_color_changed_number_label.
                                          config(text=Misc.format_number(settings_changed_buttons_text_color.
                                                                         get())),
                                                              update_stats_dict() if stats_initiated else None
                                          ])
settings_changed_invalid_text_color.trace("w", lambda *args: [settings_changed_total.
                                          set(recalculate_total_setting_changes()),
                                                              invalid_text_color_changed_number_label.
                                          config(text=Misc.format_number(settings_changed_invalid_text_color.
                                                                         get())),
                                                              update_stats_dict() if stats_initiated else None
                                          ])
settings_changed_gui_sound.trace("w", lambda *args: [settings_changed_total.
                                 set(recalculate_total_setting_changes()),
                                                     gui_sound_changed_number_label.
                                 config(text=Misc.format_number(settings_changed_gui_sound.get())),
                                                     update_stats_dict() if stats_initiated else None
                                 ])
settings_changed_remember_settings.trace("w", lambda *args: [settings_changed_total.
                                         set(recalculate_total_setting_changes()),
                                                             remember_settings_changed_number_label.
                                         config(text=Misc.format_number(settings_changed_remember_settings.get())),
                                                             update_stats_dict() if stats_initiated else None
                                         ])

# Main Menu Interactions
main_menu_interactions_total.trace("w", lambda *args: [config_text_value_stat_labelframe(
    title="Main Menu Interactions", value=main_menu_interactions_total.get(), labelframe=main_menu_labelframe),
    write_stats() if stats_initiated else None
                                   ])

# Count towards total
main_menu_interactions_played_freely.trace("w", lambda *args: [main_menu_interactions_total.
                                           set(recalculate_total_main_menu_interactions()),
                                                               played_freely_number_label.
                                           config(text=Misc.format_number(main_menu_interactions_played_freely.get())),
                                                               update_stats_dict() if stats_initiated else None
                                           ])
main_menu_interactions_recorded_compositions.trace("w", lambda *args: [main_menu_interactions_total.
                                                   set(recalculate_total_main_menu_interactions()),
                                                                       recorded_compositions_number_label.
                                                   config(text=Misc.format_number(
                                                                           main_menu_interactions_recorded_compositions
                                                                           .get())),
                                                                       update_stats_dict() if stats_initiated else None
                                                   ])
main_menu_interactions_listened_compositions.trace("w", lambda *args: [main_menu_interactions_total.
                                                   set(recalculate_total_main_menu_interactions()),
                                                                       played_back_compositions_number_label.
                                                   config(text=Misc.format_number(
                                                                           main_menu_interactions_listened_compositions
                                                                           .get())),
                                                                       update_stats_dict() if stats_initiated else None
                                                   ])
main_menu_interactions_managed_compositions.trace("w", lambda *args: [main_menu_interactions_total.
                                                  set(recalculate_total_main_menu_interactions()),
                                                                      managed_compositions_number_label.
                                                  config(text=Misc.format_number(
                                                                          main_menu_interactions_managed_compositions
                                                                          .get())),
                                                                      update_stats_dict() if stats_initiated else None
                                                  ])
main_menu_interactions_entered_settings.trace("w", lambda *args: [main_menu_interactions_total.
                                              set(recalculate_total_main_menu_interactions()),
                                                                  entered_settings_number_label.
                                              config(text=Misc.format_number(
                                                                      main_menu_interactions_entered_settings.get())),
                                                                  update_stats_dict() if stats_initiated else None
                                              ])
main_menu_interactions_viewed_stats.trace("w", lambda *args: [main_menu_interactions_total.
                                          set(recalculate_total_main_menu_interactions()),
                                                              viewed_stats_number_label.
                                          config(text=Misc.format_number(
                                                                  main_menu_interactions_viewed_stats.get())),
                                                              update_stats_dict() if stats_initiated else None
                                          ])

# Don't count towards total
main_menu_interactions_viewed_more_stats.trace("w", lambda *args: [viewed_more_stats_number_label.
                                               config(text=Misc.format_number(
                                                                        main_menu_interactions_viewed_more_stats
                                                                        .get())),
                                                                   [update_stats_dict(),
                                                                    write_stats()] if stats_initiated else None
                                               ])
main_menu_interactions_logged_in.trace("w", lambda *args: [logged_in_number_label.
                                       config(text=Misc.format_number(main_menu_interactions_logged_in.get())),
                                                           [update_stats_dict(),
                                                            write_stats()] if stats_initiated else None
                                       ])
main_menu_interactions_logged_out.trace("w", lambda *args: [logged_out_number_label.
                                        config(text=Misc.format_number(main_menu_interactions_logged_out.get())),
                                                            [update_stats_dict(),
                                                             write_stats()] if stats_initiated else None
                                        ])
main_menu_interactions_registered.trace("w", lambda *args: [registered_number_label.
                                        config(text=Misc.format_number(main_menu_interactions_registered.get())),
                                                            [update_stats_dict(),
                                                             write_stats()] if stats_initiated else None
                                        ])

# Accounts
accounts_total.trace("w", lambda *args: [config_text_value_stat_labelframe(title="Accounts",
                                                                           value=accounts_total.get(),
                                                                           labelframe=accounts_labelframe),
                                         write_stats() if stats_initiated else None
                                         ])

accounts_active.trace("w", lambda *args: [accounts_total.
                      set(recalculate_total_accounts()), active_accounts_number_label.
                      config(text=Misc.format_number(accounts_active.get())),
                      update_stats_dict() if stats_initiated else None
                      ])
accounts_deleted.trace("w", lambda *args: [accounts_total.
                       set(recalculate_total_accounts()), deleted_accounts_number_label.
                       config(text=Misc.format_number(accounts_deleted.get())),
                       update_stats_dict() if stats_initiated else None
                       ])

# Compositions
compositions_total.trace("w", lambda *args: [config_text_value_stat_labelframe(
    title="Compositions", value=compositions_total.get(), labelframe=compositions_labelframe),
    write_stats() if stats_initiated else None
                         ])

compositions_active.trace("w", lambda *args: [compositions_total.
                          set(recalculate_total_compositions()), active_compositions_number_label.
                          config(text=Misc.format_number(compositions_active.get())),
                          update_stats_dict() if stats_initiated else None
                          ])
compositions_deleted.trace("w", lambda *args: [compositions_total.
                           set(recalculate_total_compositions()), deleted_compositions_number_label.
                           config(text=Misc.format_number(compositions_deleted.get())),
                           update_stats_dict() if stats_initiated else None
                           ])

# Instrument Changed
instrument_changed_total.trace("w", lambda *args: [config_text_value_times_stat_labelframe(
    title="Instrument Changed", value=instrument_changed_total.get(),
    labelframe=instrument_changed_labelframe), write_stats() if stats_initiated else None
                               ])

instrument_changed_successfully.trace("w", lambda *args: [instrument_changed_total.
                                      set(recalculate_total_instrument_changes()),
                                                          instrument_changed_successfully_number_label.
                                      config(text=Misc.format_number(instrument_changed_successfully.get())),
                                                          update_stats_dict() if stats_initiated else None
                                      ])
instrument_changed_decided_not_to.trace("w", lambda *args: [instrument_changed_total.
                                        set(recalculate_total_instrument_changes()),
                                                            instrument_changed_unsuccessfully_number_label.
                                        config(text=Misc.format_number(instrument_changed_decided_not_to.get())),
                                                            update_stats_dict() if stats_initiated else None
                                        ])

# Returned To Main Menu

returned_to_main_menu.trace("w", lambda *args: [returned_to_main_menu_number_label.
                            config(text=f"{Misc.format_number(returned_to_main_menu.get())} Time")
                                                if returned_to_main_menu.get() == 1
                                                else returned_to_main_menu_number_label.
                            config(text=f"{Misc.format_number(returned_to_main_menu.get())} Times"),
                                                stats.update({"Returned to Main Menu": returned_to_main_menu.get()}),
                                                write_stats() if stats_initiated else None
                            ])

# App Used

app_used_counter.trace("w", lambda *args: [app_used_label.
                       config(text=f"App used for the {'{:,}'.format(app_used_counter.get())}" +
                                   Misc.get_suffix(app_used_counter.get()) + " time"),
                                           stats.update({"App Used": app_used_counter.get()}),
                                           write_stats() if stats_initiated else None
                       ])


"""GUI Elements"""


# Main Menu

app_used_label = Label(text="App used for the Xth time", font=verdana_15, anchor=SW)

# Stats


# Note-related
notes_played_labelframe = LabelFrame(text="Notes Played: X", font=verdana_25)

piano_notes_label = Label(notes_played_labelframe, text=" Piano", font=verdana_25, anchor=W)
piano_notes_number_label = Label(notes_played_labelframe, text="X", font=verdana_25,
                                 anchor=W)

short_piano_notes_label = Label(notes_played_labelframe, text="  ~  Short", font=verdana_25,
                                anchor=W)
short_piano_notes_number_label = Label(notes_played_labelframe, text="X", font=verdana_25, anchor=W)

long_piano_notes_label = Label(notes_played_labelframe, text="  ~  Long", font=verdana_25,
                               anchor=W)
long_piano_notes_number_label = Label(notes_played_labelframe, text="X", font=verdana_25, anchor=W)

flute_notes_label = Label(notes_played_labelframe, text=" Flute", font=verdana_25, anchor=W)
flute_notes_number_label = Label(notes_played_labelframe, text="X", font=verdana_25, anchor=W)

trumpet_notes_label = Label(notes_played_labelframe, text=" Trumpet", font=verdana_25, anchor=W)
trumpet_notes_number_label = Label(notes_played_labelframe, text="X", font=verdana_25, anchor=W)

violin_notes_label = Label(notes_played_labelframe, text=" Violin", font=verdana_25, anchor=W)
violin_notes_number_label = Label(notes_played_labelframe, text="X", font=verdana_25, anchor=W)

# Account-related
accounts_labelframe = LabelFrame(text="Accounts: X", font=verdana_25)

active_accounts_label = Label(accounts_labelframe, text=" Active", font=verdana_25, anchor=W)
active_accounts_number_label = Label(accounts_labelframe,
                                     text="X", font=verdana_25, anchor=W)

deleted_accounts_label = Label(accounts_labelframe, text=" Deleted", font=verdana_25_overstrike, anchor=W)
deleted_accounts_number_label = Label(accounts_labelframe,
                                      text="X", font=verdana_25_overstrike, anchor=W)

admin_accounts_label = Label(accounts_labelframe, text=" Admin", font=verdana_25_overstrike, anchor=W)
admin_accounts_number_label = Label(accounts_labelframe, text=" Will always be 1",
                                    font=verdana_25_overstrike, anchor=W)

# Composition-related
compositions_labelframe = LabelFrame(text="Compositions: X", font=verdana_25)

active_compositions_label = Label(compositions_labelframe, text=" Active", font=verdana_25,
                                  anchor=W)
active_compositions_number_label = Label(compositions_labelframe, text="X", font=verdana_25,
                                         anchor=W)

deleted_compositions_label = Label(compositions_labelframe, text=" Deleted", font=verdana_25_overstrike,
                                   anchor=W)
deleted_compositions_number_label = Label(compositions_labelframe, text="X", font=verdana_25_overstrike,
                                          anchor=W)

# Settings-related
settings_changed_labelframe = LabelFrame(text="Settings Changed: X Times", font=verdana_25)

background_color_changed_label = Label(settings_changed_labelframe, text=" Background Color",
                                       font=verdana_20, anchor=W)
background_color_changed_number_label = Label(settings_changed_labelframe,
                                              text="X", font=verdana_20, anchor=W)

text_color_changed_label = Label(settings_changed_labelframe, text=" Text Color",
                                 font=verdana_20, anchor=W)
text_color_changed_number_label = Label(settings_changed_labelframe, text="X",
                                        font=verdana_20, anchor=W)

button_color_changed_label = Label(settings_changed_labelframe, text=" Buttons' Color",
                                   font=verdana_20, anchor=W)
button_color_changed_number_label = Label(settings_changed_labelframe, text="X",
                                          font=verdana_20, anchor=W)

button_text_color_changed_label = Label(settings_changed_labelframe, text=" Buttons' Text Color",
                                        font=verdana_20, anchor=W)
button_text_color_changed_number_label = Label(settings_changed_labelframe, text="X",
                                               font=verdana_20, anchor=W)

invalid_text_color_changed_label = Label(settings_changed_labelframe, text=" Invalid Text Color",
                                         font=verdana_20, anchor=W)
invalid_text_color_changed_number_label = Label(settings_changed_labelframe, text="X",
                                                font=verdana_20, anchor=W)

gui_sound_changed_label = Label(settings_changed_labelframe, text=" GUI Sound",
                                font=verdana_20, anchor=W)
gui_sound_changed_number_label = Label(settings_changed_labelframe, text="X",
                                       font=verdana_20, anchor=W)

remember_settings_changed_label = Label(settings_changed_labelframe, text=" Remember Settings",
                                        font=verdana_20, anchor=W)
remember_settings_changed_number_label = Label(settings_changed_labelframe, text="X",
                                               font=verdana_20, anchor=W)

# Menu-related
main_menu_labelframe = LabelFrame(text="Main Menu Interactions: X", font=verdana_25)

played_freely_label = Label(main_menu_labelframe, text=" Played Freely", font=verdana_20, anchor=W)
played_freely_number_label = Label(main_menu_labelframe, text="X", font=verdana_20, anchor=W)

recorded_compositions_label = Label(main_menu_labelframe, text=" Recorded Compositions",
                                    font=verdana_20, anchor=W)
recorded_compositions_number_label = Label(main_menu_labelframe, text="X", font=verdana_20, anchor=W)

played_back_compositions_label = Label(main_menu_labelframe, text=" Played Back Compositions",
                                       font=verdana_20, anchor=W)
played_back_compositions_number_label = Label(main_menu_labelframe, text="X", font=verdana_20,
                                              anchor=W)

managed_compositions_label = Label(main_menu_labelframe, text=" Managed Compositions", font=verdana_20_overstrike,
                                   anchor=W)
managed_compositions_number_label = Label(main_menu_labelframe, text="X", font=verdana_20_overstrike, anchor=W)

entered_settings_label = Label(main_menu_labelframe, text=" Entered Settings", font=verdana_20,
                               anchor=W)
entered_settings_number_label = Label(main_menu_labelframe, text="X", font=verdana_20, anchor=W)

viewed_stats_label = Label(main_menu_labelframe, text=" Viewed Stats", font=verdana_20, anchor=W)
viewed_stats_number_label = Label(main_menu_labelframe, text="X", font=verdana_20, anchor=W)

viewed_more_stats_label = Label(main_menu_labelframe, text=" Viewed More Stats*", font=verdana_20,
                                anchor=W)
viewed_more_stats_number_label = Label(main_menu_labelframe, text="X", font=verdana_20, anchor=W)

logged_in_label = Label(main_menu_labelframe, text=" Logged In*", font=verdana_20, anchor=W)
logged_in_number_label = Label(main_menu_labelframe, text="X", font=verdana_20, anchor=W)

logged_out_label = Label(main_menu_labelframe, text=" Logged Out*", font=verdana_20, anchor=W)
logged_out_number_label = Label(main_menu_labelframe, text="X", font=verdana_20, anchor=W)

registered_label = Label(main_menu_labelframe, text=" Signed Up*", font=verdana_20, anchor=W)
registered_number_label = Label(main_menu_labelframe, text="X", font=verdana_20, anchor=W)

# Separator
separator: Separator = Separator(main_menu_labelframe)

# More Stats


# Piano Notes
piano_labelframe = LabelFrame(text="Piano:", font=verdana_25)

do_1_short_label = Label(piano_labelframe, text=" Do 1 Short", font=verdana_25, anchor=W)
re_short_label = Label(piano_labelframe, text=" Re Short", font=verdana_25, anchor=W)
mi_short_label = Label(piano_labelframe, text=" Mi Short", font=verdana_25, anchor=W)
fa_short_label = Label(piano_labelframe, text=" Fa Short", font=verdana_25, anchor=W)
sol_short_label = Label(piano_labelframe, text=" Sol Short", font=verdana_25, anchor=W)
la_short_label = Label(piano_labelframe, text=" La Short", font=verdana_25, anchor=W)
si_short_label = Label(piano_labelframe, text=" Si Short", font=verdana_25, anchor=W)
do_2_short_label = Label(piano_labelframe, text=" Do 2 Short", font=verdana_25, anchor=W)

do_1_long_label = Label(piano_labelframe, text="Do 1 Long", font=verdana_25, anchor=W)
re_long_label = Label(piano_labelframe, text="Re Long", font=verdana_25, anchor=W)
mi_long_label = Label(piano_labelframe, text="Mi Long", font=verdana_25, anchor=W)
fa_long_label = Label(piano_labelframe, text="Fa Long", font=verdana_25, anchor=W)
sol_long_label = Label(piano_labelframe, text="Sol Long", font=verdana_25, anchor=W)
la_long_label = Label(piano_labelframe, text="La Long", font=verdana_25, anchor=W)
si_long_label = Label(piano_labelframe, text="Si Long", font=verdana_25, anchor=W)
do_2_long_label = Label(piano_labelframe, text="Do 2 Long", font=verdana_25, anchor=W)

# Piano Number Labels
do_1_short_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)
re_short_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)
mi_short_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)
fa_short_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)
sol_short_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)
la_short_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)
si_short_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)
do_2_short_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)

do_1_long_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)
re_long_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)
mi_long_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)
fa_long_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)
sol_long_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)
la_long_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)
si_long_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)
do_2_long_number_label = Label(piano_labelframe, text="X", font=verdana_25, anchor=W)

# Flute Notes
flute_labelframe = LabelFrame(text="Flute:", font=verdana_25)

c4_flute_label = Label(flute_labelframe, text=" C4", font=verdana_25, anchor=W)
c5_flute_label = Label(flute_labelframe, text=" C5", font=verdana_25, anchor=W)
c6_flute_label = Label(flute_labelframe, text=" C6", font=verdana_25, anchor=W)

g4_flute_label = Label(flute_labelframe, text=" G4", font=verdana_25, anchor=W)
g5_flute_label = Label(flute_labelframe, text=" G5", font=verdana_25, anchor=W)
g6_flute_label = Label(flute_labelframe, text=" G6", font=verdana_25, anchor=W)

# Flute Number Labels
c4_flute_number_label = Label(flute_labelframe, text="X", font=verdana_25, anchor=W)
c5_flute_number_label = Label(flute_labelframe, text="X", font=verdana_25, anchor=W)
c6_flute_number_label = Label(flute_labelframe, text="X", font=verdana_25, anchor=W)

g4_flute_number_label = Label(flute_labelframe, text="X", font=verdana_25, anchor=W)
g5_flute_number_label = Label(flute_labelframe, text="X", font=verdana_25, anchor=W)
g6_flute_number_label = Label(flute_labelframe, text="X", font=verdana_25, anchor=W)

# Trumpet Notes
trumpet_labelframe = LabelFrame(text="Trumpet:", font=verdana_25)

c4_trumpet_label = Label(trumpet_labelframe, text=" C4", font=verdana_25, anchor=W)
c5_trumpet_label = Label(trumpet_labelframe, text=" C5", font=verdana_25, anchor=W)
c6_trumpet_label = Label(trumpet_labelframe, text=" C6", font=verdana_25, anchor=W)

g3_trumpet_label = Label(trumpet_labelframe, text=" G3", font=verdana_25, anchor=W)
g4_trumpet_label = Label(trumpet_labelframe, text=" G4", font=verdana_25, anchor=W)
g5_trumpet_label = Label(trumpet_labelframe, text=" G5", font=verdana_25, anchor=W)

# Trumpet Number Labels
c4_trumpet_number_label = Label(trumpet_labelframe, text="X", font=verdana_25, anchor=W)
c5_trumpet_number_label = Label(trumpet_labelframe, text="X", font=verdana_25, anchor=W)
c6_trumpet_number_label = Label(trumpet_labelframe, text="X", font=verdana_25, anchor=W)

g3_trumpet_number_label = Label(trumpet_labelframe, text="X", font=verdana_25, anchor=W)
g4_trumpet_number_label = Label(trumpet_labelframe, text="X", font=verdana_25, anchor=W)
g5_trumpet_number_label = Label(trumpet_labelframe, text="X", font=verdana_25, anchor=W)

# Violin Notes
violin_labelframe = LabelFrame(text="Violin:", font=verdana_25)

c4_violin_label = Label(violin_labelframe, text=" C4", font=verdana_25, anchor=W)
c5_violin_label = Label(violin_labelframe, text=" C5", font=verdana_25, anchor=W)
c6_violin_label = Label(violin_labelframe, text=" C6", font=verdana_25, anchor=W)

g4_violin_label = Label(violin_labelframe, text=" G4", font=verdana_25, anchor=W)
g5_violin_label = Label(violin_labelframe, text=" G5", font=verdana_25, anchor=W)
g6_violin_label = Label(violin_labelframe, text=" G6", font=verdana_25, anchor=W)

# Violin Number Labels
c4_violin_number_label = Label(violin_labelframe, text="X", font=verdana_25, anchor=W)
c5_violin_number_label = Label(violin_labelframe, text="X", font=verdana_25, anchor=W)
c6_violin_number_label = Label(violin_labelframe, text="X", font=verdana_25, anchor=W)

g4_violin_number_label = Label(violin_labelframe, text="X", font=verdana_25, anchor=W)
g5_violin_number_label = Label(violin_labelframe, text="X", font=verdana_25, anchor=W)
g6_violin_number_label = Label(violin_labelframe, text="X", font=verdana_25, anchor=W)

# Changed Instrument
instrument_changed_labelframe = LabelFrame(text="Instrument Changed: X Times", font=verdana_25)

instrument_changed_successfully_label = Label(instrument_changed_labelframe, text="     Successfully",
                                              font=verdana_25, anchor=W)
instrument_changed_successfully_number_label = Label(instrument_changed_labelframe,
                                                     text="X", font=verdana_25, anchor=W)

instrument_changed_unsuccessfully_label = Label(instrument_changed_labelframe,
                                                text="     Decided Not To", font=verdana_25, anchor=W)
instrument_changed_unsuccessfully_number_label = Label(instrument_changed_labelframe,
                                                       text="X", font=verdana_25, anchor=W)

# Returned To Main Menu
returned_to_main_menu_labelframe = LabelFrame(text="Returned to Main Menu:", font=verdana_25)
returned_to_main_menu_number_label = Label(text="X Times", font=verdana_25)

# Colon Labels - Stats Menu
stats_colon_label1 = Label(notes_played_labelframe, text="   :         ", font=verdana_25)
stats_colon_label2 = Label(notes_played_labelframe, text="   :         ", font=verdana_25)
stats_colon_label3 = Label(notes_played_labelframe, text="   :         ", font=verdana_25)
stats_colon_label4 = Label(notes_played_labelframe, text="   :         ", font=verdana_25)
stats_colon_label5 = Label(notes_played_labelframe, text="   :         ", font=verdana_25)
stats_colon_label6 = Label(notes_played_labelframe, text="   :         ", font=verdana_25)

stats_colon_label7 = Label(accounts_labelframe, text="    :   ", font=verdana_25)
stats_colon_label8 = Label(accounts_labelframe, text="    :   ", font=verdana_25)
stats_colon_label9 = Label(accounts_labelframe, text="    :   ", font=verdana_25)

stats_colon_label10 = Label(settings_changed_labelframe, text="      :      ", font=verdana_20)
stats_colon_label11 = Label(settings_changed_labelframe, text="      :      ", font=verdana_20)
stats_colon_label12 = Label(settings_changed_labelframe, text="      :      ", font=verdana_20)
stats_colon_label13 = Label(settings_changed_labelframe, text="      :      ", font=verdana_20)
stats_colon_label14 = Label(settings_changed_labelframe, text="      :      ", font=verdana_20)
stats_colon_label15 = Label(settings_changed_labelframe, text="      :      ", font=verdana_20)
stats_colon_label16 = Label(settings_changed_labelframe, text="      :      ", font=verdana_20)

stats_colon_label17 = Label(main_menu_labelframe, text="   :   ", font=verdana_20)
stats_colon_label18 = Label(main_menu_labelframe, text="   :   ", font=verdana_20)
stats_colon_label19 = Label(main_menu_labelframe, text="   :   ", font=verdana_20)
stats_colon_label20 = Label(main_menu_labelframe, text="   :   ", font=verdana_20)
stats_colon_label21 = Label(main_menu_labelframe, text="   :   ", font=verdana_20)
stats_colon_label22 = Label(main_menu_labelframe, text="   :   ", font=verdana_20)
stats_colon_label23 = Label(main_menu_labelframe, text="   :   ", font=verdana_20)
stats_colon_label24 = Label(main_menu_labelframe, text="   :   ", font=verdana_20)
stats_colon_label25 = Label(main_menu_labelframe, text="   :   ", font=verdana_20)
stats_colon_label26 = Label(main_menu_labelframe, text="   :   ", font=verdana_20)

stats_colon_label27 = Label(compositions_labelframe, text="   :   ", font=verdana_25)
stats_colon_label28 = Label(compositions_labelframe, text="   :   ", font=verdana_25)

# Colon Labels - More Stats Menu
more_stats_colon_label1 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label2 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label3 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label4 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label5 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label6 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label7 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label8 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label9 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label10 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label11 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label12 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label13 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label14 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label15 = Label(piano_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label16 = Label(piano_labelframe, text="   :   ", font=verdana_25)

more_stats_colon_label17 = Label(flute_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label18 = Label(flute_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label19 = Label(flute_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label20 = Label(flute_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label21 = Label(flute_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label22 = Label(flute_labelframe, text="   :   ", font=verdana_25)

more_stats_colon_label23 = Label(trumpet_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label24 = Label(trumpet_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label25 = Label(trumpet_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label26 = Label(trumpet_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label27 = Label(trumpet_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label28 = Label(trumpet_labelframe, text="   :   ", font=verdana_25)

more_stats_colon_label29 = Label(violin_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label30 = Label(violin_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label31 = Label(violin_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label32 = Label(violin_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label33 = Label(violin_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label34 = Label(violin_labelframe, text="   :   ", font=verdana_25)

more_stats_colon_label35 = Label(instrument_changed_labelframe, text="   :   ", font=verdana_25)
more_stats_colon_label36 = Label(instrument_changed_labelframe, text="   :   ", font=verdana_25)

# Space Labels - More Stats Menu
space_label0 = Label(flute_labelframe, text=" ", font=verdana_25)

space_label1 = Label(piano_labelframe, text="     ", font=verdana_25)
space_label2 = Label(piano_labelframe, text="     ", font=verdana_25)
space_label3 = Label(piano_labelframe, text="     ", font=verdana_25)
space_label4 = Label(piano_labelframe, text="     ", font=verdana_25)
space_label5 = Label(piano_labelframe, text="     ", font=verdana_25)
space_label6 = Label(piano_labelframe, text="     ", font=verdana_25)
space_label7 = Label(piano_labelframe, text="     ", font=verdana_25)
space_label8 = Label(piano_labelframe, text="     ", font=verdana_25)


"""Functions"""


def write_stats():
    """Writes stats in Stats.json file
    """
    with open(file=STATS_JSON_PATH, mode="w", encoding="utf-8") as write_stats_file:
        json.dump(stats, write_stats_file, indent=4)


def recalculate_total_main_menu_interactions():
    """Recalculates the total amount of main menu interactions
    """
    recalculated_number_of_main_menu_interactions: int = (main_menu_interactions_played_freely.get() +
                                                          main_menu_interactions_recorded_compositions.get() +
                                                          main_menu_interactions_listened_compositions.get() +
                                                          main_menu_interactions_managed_compositions.get() +
                                                          main_menu_interactions_entered_settings.get() +
                                                          main_menu_interactions_viewed_stats.get())
    return recalculated_number_of_main_menu_interactions


def recalculate_total_setting_changes():
    """Recalculates the total amount of setting changes
    """
    recalculated_number_of_setting_changes: int = (settings_changed_background_color.get() +
                                                   settings_changed_text_color.get() +
                                                   settings_changed_buttons_color.get() +
                                                   settings_changed_buttons_text_color.get() +
                                                   settings_changed_invalid_text_color.get() +
                                                   settings_changed_gui_sound.get() +
                                                   settings_changed_remember_settings.get())
    return recalculated_number_of_setting_changes


def recalculate_total_violin_notes_played():
    """Recalculates the total amount of violin notes played
    """
    recalculated_number_of_violin_notes_played: int = (c4_violin_notes_played.get() +
                                                       c5_violin_notes_played.get() +
                                                       c6_violin_notes_played.get() +
                                                       g4_violin_notes_played.get() +
                                                       g5_violin_notes_played.get() +
                                                       g6_violin_notes_played.get())
    return recalculated_number_of_violin_notes_played


def recalculate_total_trumpet_notes_played():
    """Recalculates the total amount of trumpet notes played
    """
    recalculated_number_of_trumpet_notes_played: int = (c4_trumpet_notes_played.get() +
                                                        c5_trumpet_notes_played.get() +
                                                        c6_trumpet_notes_played.get() +
                                                        g3_trumpet_notes_played.get() +
                                                        g4_trumpet_notes_played.get() +
                                                        g5_trumpet_notes_played.get())
    return recalculated_number_of_trumpet_notes_played


def recalculate_total_flute_notes_played():
    """Recalculates the total amount of flute notes played
    """
    recalculated_number_of_flute_notes_played: int = (c4_flute_notes_played.get() +
                                                      c5_flute_notes_played.get() +
                                                      c6_flute_notes_played.get() +
                                                      g4_flute_notes_played.get() +
                                                      g5_flute_notes_played.get() +
                                                      g6_flute_notes_played.get())
    return recalculated_number_of_flute_notes_played


def recalculate_total_short_or_long_piano_notes_played(note_length: str):
    """Recalculates the total amount of short piano notes played
    """
    if note_length == "short":
        recalculated_number_of_short_piano_notes_played: int = (short_do_1_piano_notes_played.get() +
                                                                short_re_piano_notes_played.get() +
                                                                short_mi_piano_notes_played.get() +
                                                                short_fa_piano_notes_played.get() +
                                                                short_sol_piano_notes_played.get() +
                                                                short_la_piano_notes_played.get() +
                                                                short_si_piano_notes_played.get() +
                                                                short_do_2_piano_notes_played.get())
        return recalculated_number_of_short_piano_notes_played
    # elif note_length == "long"
    recalculated_number_of_long_piano_notes_played: int = (long_do_1_piano_notes_played.get() +
                                                           long_re_piano_notes_played.get() +
                                                           long_mi_piano_notes_played.get() +
                                                           long_fa_piano_notes_played.get() +
                                                           long_sol_piano_notes_played.get() +
                                                           long_la_piano_notes_played.get() +
                                                           long_si_piano_notes_played.get() +
                                                           long_do_2_piano_notes_played.get())
    return recalculated_number_of_long_piano_notes_played


def recalculate_total_piano_notes_played():
    """Recalculates the total amount of piano notes played (both long & short)
    """
    recalculated_number_of_total_piano_notes_played: int = (short_piano_notes_played_total.get() +
                                                            long_piano_notes_played_total.get())
    return recalculated_number_of_total_piano_notes_played


def recalculate_total_notes_played():
    """Recalculates the total amount of notes played
    """
    recalculated_number_of_notes_played: int = (piano_notes_played_total.get() +
                                                flute_notes_played_total.get() +
                                                trumpet_notes_played_total.get() +
                                                violin_notes_played_total.get())
    return recalculated_number_of_notes_played


def recalculate_total_accounts():
    """Recalculates the total amount of accounts
    """
    recalculated_number_of_accounts: int = accounts_active.get() + accounts_deleted.get()  # + 1 TODO
    # Account for admin account   ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔ ➔     Λ
    return recalculated_number_of_accounts


def recalculate_total_compositions():
    """Recalculates the total amount of compositions
    """
    recalculated_number_of_compositions: int = compositions_active.get() + compositions_deleted.get()
    return recalculated_number_of_compositions


def recalculate_total_instrument_changes():
    """Recalculates the total amount of instrument changes
    """
    recalculated_number_of_instrument_changes: int = (instrument_changed_successfully.get() +
                                                      instrument_changed_decided_not_to.get())
    return recalculated_number_of_instrument_changes


"""GUI-involved Functions"""


def initiate_stats():
    """Initiates all stats Labels & LabelFrames
    """
    global stats_initiated

    # Long Piano Notes

    long_do_1_piano_notes_played.set(stats["Notes Played"]["Piano"]["Long"]["Do 1"])
    long_re_piano_notes_played.set(stats["Notes Played"]["Piano"]["Long"]["Re"])
    long_mi_piano_notes_played.set(stats["Notes Played"]["Piano"]["Long"]["Mi"])
    long_fa_piano_notes_played.set(stats["Notes Played"]["Piano"]["Long"]["Fa"])
    long_sol_piano_notes_played.set(stats["Notes Played"]["Piano"]["Long"]["Sol"])
    long_la_piano_notes_played.set(stats["Notes Played"]["Piano"]["Long"]["La"])
    long_si_piano_notes_played.set(stats["Notes Played"]["Piano"]["Long"]["Si"])
    long_do_2_piano_notes_played.set(stats["Notes Played"]["Piano"]["Long"]["Do 2"])

    # Short Piano Notes

    short_do_1_piano_notes_played.set(stats["Notes Played"]["Piano"]["Short"]["Do 1"])
    short_re_piano_notes_played.set(stats["Notes Played"]["Piano"]["Short"]["Re"])
    short_mi_piano_notes_played.set(stats["Notes Played"]["Piano"]["Short"]["Mi"])
    short_fa_piano_notes_played.set(stats["Notes Played"]["Piano"]["Short"]["Fa"])
    short_sol_piano_notes_played.set(stats["Notes Played"]["Piano"]["Short"]["Sol"])
    short_la_piano_notes_played.set(stats["Notes Played"]["Piano"]["Short"]["La"])
    short_si_piano_notes_played.set(stats["Notes Played"]["Piano"]["Short"]["Si"])
    short_do_2_piano_notes_played.set(stats["Notes Played"]["Piano"]["Short"]["Do 2"])

    # Flute Notes

    c4_flute_notes_played.set(stats["Notes Played"]["Flute"]["C4"])
    c5_flute_notes_played.set(stats["Notes Played"]["Flute"]["C5"])
    c6_flute_notes_played.set(stats["Notes Played"]["Flute"]["C6"])
    g4_flute_notes_played.set(stats["Notes Played"]["Flute"]["G4"])
    g5_flute_notes_played.set(stats["Notes Played"]["Flute"]["G5"])
    g6_flute_notes_played.set(stats["Notes Played"]["Flute"]["G6"])

    # Trumpet Notes

    c4_trumpet_notes_played.set(stats["Notes Played"]["Trumpet"]["C4"])
    c5_trumpet_notes_played.set(stats["Notes Played"]["Trumpet"]["C5"])
    c6_trumpet_notes_played.set(stats["Notes Played"]["Trumpet"]["C6"])
    g3_trumpet_notes_played.set(stats["Notes Played"]["Trumpet"]["G3"])
    g4_trumpet_notes_played.set(stats["Notes Played"]["Trumpet"]["G4"])
    g5_trumpet_notes_played.set(stats["Notes Played"]["Trumpet"]["G5"])

    # Violin Notes

    c4_violin_notes_played.set(stats["Notes Played"]["Violin"]["C4"])
    c5_violin_notes_played.set(stats["Notes Played"]["Violin"]["C5"])
    c6_violin_notes_played.set(stats["Notes Played"]["Violin"]["C6"])
    g4_violin_notes_played.set(stats["Notes Played"]["Violin"]["G4"])
    g5_violin_notes_played.set(stats["Notes Played"]["Violin"]["G5"])
    g6_violin_notes_played.set(stats["Notes Played"]["Violin"]["G6"])

    # Settings Changed

    settings_changed_background_color.set(stats["Settings Changed"]["Background Color"])
    settings_changed_text_color.set(stats["Settings Changed"]["Text Color"])
    settings_changed_buttons_color.set(stats["Settings Changed"]["Buttons' Color"])
    settings_changed_buttons_text_color.set(stats["Settings Changed"]["Buttons' Text Color"])
    settings_changed_invalid_text_color.set(stats["Settings Changed"]["Invalid Text Color"])
    settings_changed_gui_sound.set(stats["Settings Changed"]["GUI Sound"])
    settings_changed_remember_settings.set(stats["Settings Changed"]["Remember Settings"])

    # Main Menu Interactions

    # Count Towards Total
    main_menu_interactions_played_freely.set(stats["Main Menu Interactions"]["Played Freely"])
    main_menu_interactions_recorded_compositions.set(stats["Main Menu Interactions"]["Recorded Compositions"])
    main_menu_interactions_listened_compositions.set(stats["Main Menu Interactions"]["Listened Compositions"])
    main_menu_interactions_managed_compositions.set(stats["Main Menu Interactions"]["Managed Compositions"])
    main_menu_interactions_entered_settings.set(stats["Main Menu Interactions"]["Entered Settings"])
    main_menu_interactions_viewed_stats.set(stats["Main Menu Interactions"]["Viewed Stats"])
    # Don't Count Towards Total
    main_menu_interactions_viewed_more_stats.set(stats["Main Menu Interactions"]["Viewed More Stats"])
    main_menu_interactions_logged_in.set(stats["Main Menu Interactions"]["Logged In"])
    main_menu_interactions_logged_out.set(stats["Main Menu Interactions"]["Logged Out"])
    main_menu_interactions_registered.set(stats["Main Menu Interactions"]["Registered"])

    # Accounts

    accounts_active.set(stats["Accounts"]["Active"])
    accounts_deleted.set(stats["Accounts"]["Deleted"])

    # Compositions

    compositions_active.set(stats["Compositions"]["Active"])
    compositions_deleted.set(stats["Compositions"]["Deleted"])

    # Instrument Changed

    instrument_changed_successfully.set(stats["Instrument Changed"]["Successfully"])
    instrument_changed_decided_not_to.set(stats["Instrument Changed"]["Decided not to"])

    # Returned To Main Menu

    returned_to_main_menu.set(stats["Returned to Main Menu"])

    # App Used

    app_used_counter.set(stats["App Used"])

    # Set stats_initiated to True
    stats_initiated = True


def update_stats_dict():
    """Updates all the values of the stats label
    """
    stats.update({"Notes Played": {
                    "Piano": {
                        "Short": {
                            "Do 1": short_do_1_piano_notes_played.get(),
                            "Re": short_re_piano_notes_played.get(),
                            "Mi": short_mi_piano_notes_played.get(),
                            "Fa": short_fa_piano_notes_played.get(),
                            "Sol": short_sol_piano_notes_played.get(),
                            "La": short_la_piano_notes_played.get(),
                            "Si": short_si_piano_notes_played.get(),
                            "Do 2": short_do_2_piano_notes_played.get()
                        },
                        "Long": {
                            "Do 1": long_do_1_piano_notes_played.get(),
                            "Re": long_re_piano_notes_played.get(),
                            "Mi": long_mi_piano_notes_played.get(),
                            "Fa": long_fa_piano_notes_played.get(),
                            "Sol": long_sol_piano_notes_played.get(),
                            "La": long_la_piano_notes_played.get(),
                            "Si": long_si_piano_notes_played.get(),
                            "Do 2": long_do_2_piano_notes_played.get()
                        }
                    },
                    "Flute": {
                        "C4": c4_flute_notes_played.get(),
                        "C5": c5_flute_notes_played.get(),
                        "C6": c6_flute_notes_played.get(),
                        "G4": g4_flute_notes_played.get(),
                        "G5": g5_flute_notes_played.get(),
                        "G6": g6_flute_notes_played.get(),
                    },
                    "Trumpet": {
                        "C4": c4_trumpet_notes_played.get(),
                        "C5": c5_trumpet_notes_played.get(),
                        "C6": c6_trumpet_notes_played.get(),
                        "G3": g3_trumpet_notes_played.get(),
                        "G4": g4_trumpet_notes_played.get(),
                        "G5": g5_trumpet_notes_played.get(),
                    },
                    "Violin": {
                        "C4": c4_violin_notes_played.get(),
                        "C5": c5_violin_notes_played.get(),
                        "C6": c6_violin_notes_played.get(),
                        "G4": g4_violin_notes_played.get(),
                        "G5": g5_violin_notes_played.get(),
                        "G6": g6_violin_notes_played.get(),
                    }
                 },
                 "Settings Changed": {
                    "Background Color": settings_changed_background_color.get(),
                    "Text Color": settings_changed_text_color.get(),
                    "Buttons' Color": settings_changed_buttons_color.get(),
                    "Buttons' Text Color": settings_changed_buttons_text_color.get(),
                    "Invalid Text Color": settings_changed_invalid_text_color.get(),
                    "GUI Sound": settings_changed_gui_sound.get(),
                    "Remember Settings": settings_changed_remember_settings.get()
                 },
                 "Main Menu Interactions": {
                    "Played Freely": main_menu_interactions_played_freely.get(),
                    "Recorded Compositions": main_menu_interactions_recorded_compositions.get(),
                    "Listened Compositions": main_menu_interactions_listened_compositions.get(),
                    "Managed Compositions": main_menu_interactions_managed_compositions.get(),
                    "Entered Settings": main_menu_interactions_entered_settings.get(),
                    "Viewed Stats": main_menu_interactions_viewed_stats.get(),
                    "Viewed More Stats": main_menu_interactions_viewed_more_stats.get(),
                    "Logged In": main_menu_interactions_logged_in.get(),
                    "Logged Out": main_menu_interactions_logged_out.get(),
                    "Registered": main_menu_interactions_registered.get()
                 },
                 "Accounts": {
                    "Active": accounts_active.get(),
                    "Deleted": accounts_deleted.get()
                 },
                 "Compositions": {
                    "Active": compositions_active.get(),
                    "Deleted": compositions_deleted.get()
                 },
                 "Instrument Changed": {
                    "Successfully": instrument_changed_successfully.get(),
                    "Decided not to": instrument_changed_decided_not_to.get()
                 }
             })


def config_text_value_times_stat_labelframe(title: str, value: int, labelframe: LabelFrame):
    """Configures text: value + time(s) labels/labelframes
    """
    if value == 1:
        labelframe_text: str = f"{title}: 1 Time"
    else:
        labelframe_text: str = f"{title}: {Misc.format_number(value)} Times"
    labelframe.config(text=labelframe_text)


def config_text_value_stat_labelframe(title: str, value: int, labelframe: LabelFrame):
    """Configures text: value labels/labelframes
    """
    labelframe_text: str = f"{title}: {Misc.format_number(value)}"
    labelframe.config(text=labelframe_text)
