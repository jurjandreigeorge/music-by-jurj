"""
GUI module; Consists of all GUI elements and their associate functions
"""


# GUI-related Imports
from MainWindow import forget_all_widgets
from tkinter import *
from tkinter.ttk import Separator, Combobox, Notebook, Progressbar, Style
from Fonts import *
from tkinter.scrolledtext import ScrolledText
# Imports
import datetime
import copy
import sys
import random
import Misc
import Colors
import Sounds
import Stats
import User
import Composition
import Settings


"""Create & Configure ttk Style"""


style = Style()

style.theme_use(themename="classic")
style.configure('Sort.TNotebook.Tab', font=verdana_25, background=Settings.default_notebook_tab_background_color)
style.configure('Sorted.TNotebook.Tab', font=verdana_17, background=Settings.default_notebook_tab_background_color)
style.configure('TNotebook', background=Settings.chosen_background_color.get())

# Error color combobox
style.configure("TCombobox", selectbackground=Settings.default_combobox_select_background_color,
                selectforeground=Settings.default_combobox_select_text_color)
style.configure("Error.TCombobox", foreground=Settings.chosen_invalid_text_color.get(),
                selectbackground=Settings.default_combobox_select_background_color,
                selectforeground=Settings.default_combobox_select_text_color)

# Configure combobox list fonts
root.option_add("*TCombobox*Listbox*Font", verdana_25)
root.option_add('*TCombobox*Listbox.Justify', CENTER)


"""Trace Functions"""


# Sounds Variable(s)
Sounds.chosen_instrument.trace("w", lambda *args: config_about_chosen_instrument_text(Sounds.chosen_instrument.get()))


# Settings Variables
Settings.chosen_background_color.trace("w", lambda *args: Settings.setting_variable_trace_wrapper(
    setting_value=Settings.chosen_background_color.get(), target="Background Color"))

Settings.chosen_text_color.trace("w", lambda *args: Settings.setting_variable_trace_wrapper(
    setting_value=Settings.chosen_text_color.get(), target="Text Color"))

Settings.chosen_button_color.trace("w", lambda *args: Settings.setting_variable_trace_wrapper(
    setting_value=Settings.chosen_button_color.get(), target="Buttons' Color"))

Settings.chosen_button_text_color.trace("w", lambda *args: Settings.setting_variable_trace_wrapper(
    setting_value=Settings.chosen_button_text_color.get(), target="Buttons' Text Color"))

Settings.chosen_invalid_text_color.trace("w", lambda *args: Settings.setting_variable_trace_wrapper(
    setting_value=Settings.chosen_invalid_text_color.get(), target="Invalid Text Color"))

Settings.chosen_gui_sound_setting.trace("w", lambda *args: Settings.setting_variable_trace_wrapper(
    setting_value=Settings.chosen_gui_sound_setting.get(), target="GUI Sound"))

Settings.remember_settings_setting.trace("w", lambda *args: Settings.setting_variable_trace_wrapper(
    setting_value=Settings.remember_settings_setting.get(), target="Remember Settings"))


# Login, Password Recovery & Register User Variables
User.chosen_birth_day.trace("w", lambda *args: config_date_selection_comboboxes(var=User.chosen_birth_day,
                                                                                target="Register",
                                                                                day_var=User.chosen_birth_day,
                                                                                month_var=User.chosen_birth_month,
                                                                                year_var=User.chosen_birth_year))
User.chosen_birth_month.trace("w", lambda *args: config_date_selection_comboboxes(var=User.chosen_birth_month,
                                                                                  target="Register",
                                                                                  day_var=User.chosen_birth_day,
                                                                                  month_var=User.chosen_birth_month,
                                                                                  year_var=User.chosen_birth_year))
User.chosen_birth_year.trace("w", lambda *args: config_date_selection_comboboxes(var=User.chosen_birth_year,
                                                                                 target="Register",
                                                                                 day_var=User.chosen_birth_day,
                                                                                 month_var=User.chosen_birth_month,
                                                                                 year_var=User.chosen_birth_year))

User.chosen_first_name.trace("w", lambda *args: [Misc.clear_extra_whitespaces(User.chosen_first_name),
                                                 Misc.entry_character_length_limit(User.chosen_first_name,
                                                                                   User.MAXIMUM_NAME_LENGTH),
                                                 first_name_entry_field.configure(fg=Settings.
                                                                                  chosen_button_text_color.get())
                                                 if User.chosen_first_name.get() != "First Name"
                                                 else None
                                                 ])
User.chosen_last_name.trace("w", lambda *args: [Misc.clear_extra_whitespaces(User.chosen_last_name),
                                                Misc.entry_character_length_limit(User.chosen_last_name,
                                                                                  User.MAXIMUM_NAME_LENGTH),
                                                last_name_entry_field.configure(fg=Settings.
                                                                                chosen_button_text_color.get())
                                                if User.chosen_last_name.get() != "Last Name"
                                                else None
                                                ])
User.chosen_nickname.trace("w", lambda *args: [Misc.clear_extra_whitespaces(User.chosen_nickname),
                                               Misc.entry_character_length_limit(User.chosen_nickname,
                                                                                 User.MAXIMUM_NAME_LENGTH)])

User.chosen_username.trace("w", lambda *args: [Misc.clear_white_spaces(User.chosen_username),
                                               Misc.entry_character_length_limit(User.chosen_username,
                                                                                 User.MAXIMUM_USERNAME_LENGTH),
                                               User.check_create_account_condition(User.chosen_username.get(),
                                                                                   User.chosen_password.get(),
                                                                                   User.chosen_confirm_password.get())
                                               ])
User.chosen_password.trace("w", lambda *args: [Misc.clear_non_digit_nor_letter(User.chosen_password),
                                               User.check_create_account_condition(User.chosen_username.get(),
                                                                                   User.chosen_password.get(),
                                                                                   User.chosen_confirm_password.get())
                                               ])
User.chosen_confirm_password.trace("w", lambda *args: [Misc.clear_non_digit_nor_letter(User.chosen_confirm_password),
                                                       User.check_create_account_condition(User.chosen_username.get(),
                                                                                           User.chosen_password.get(),
                                                                                           User.chosen_confirm_password
                                                                                           .get())
                                                       ])

User.recovery_key_part_1.trace("w", lambda *args: [Misc.clear_non_digit_nor_letter(User.recovery_key_part_1),
                                                   Misc.clear_white_spaces(User.recovery_key_part_1),
                                                   User.recovery_key_part_1.set(User.recovery_key_part_1.get().upper()),
                                                   Misc.entry_character_length_limit(User.recovery_key_part_1, 4),
                                                   [recovery_key_entry_field_2.focus(),
                                                    recovery_key_entry_field_2.icursor(0)]
                                                   if len(User.recovery_key_part_1.get()) == 4 and
                                                   recovery_key_entry_field_1.index(INSERT) == 4 else None,
                                                   recovery_key_invalid_inputs_label.place_forget()
                                                   ])
User.recovery_key_part_2.trace("w", lambda *args: [Misc.clear_non_digit_nor_letter(User.recovery_key_part_2),
                                                   Misc.clear_white_spaces(User.recovery_key_part_2),
                                                   User.recovery_key_part_2.set(User.recovery_key_part_2.get().upper()),
                                                   Misc.entry_character_length_limit(User.recovery_key_part_2, 4),
                                                   [recovery_key_entry_field_3.focus(),
                                                    recovery_key_entry_field_3.icursor(0)]
                                                   if len(User.recovery_key_part_2.get()) == 4 and
                                                   recovery_key_entry_field_2.index(INSERT) == 4 else None,
                                                   recovery_key_invalid_inputs_label.place_forget()
                                                   ])
User.recovery_key_part_3.trace("w", lambda *args: [Misc.clear_non_digit_nor_letter(User.recovery_key_part_3),
                                                   Misc.clear_white_spaces(User.recovery_key_part_3),
                                                   User.recovery_key_part_3.set(User.recovery_key_part_3.get().upper()),
                                                   Misc.entry_character_length_limit(User.recovery_key_part_3, 4),
                                                   [recovery_key_entry_field_4.focus(),
                                                    recovery_key_entry_field_4.icursor(0)]
                                                   if len(User.recovery_key_part_3.get()) == 4 and
                                                   recovery_key_entry_field_3.index(INSERT) == 4 else None,
                                                   recovery_key_invalid_inputs_label.place_forget()
                                                   ])
User.recovery_key_part_4.trace("w", lambda *args: [Misc.clear_non_digit_nor_letter(User.recovery_key_part_4),
                                                   Misc.clear_white_spaces(User.recovery_key_part_4),
                                                   User.recovery_key_part_4.set(User.recovery_key_part_4.get().upper()),
                                                   Misc.entry_character_length_limit(User.recovery_key_part_4, 4),
                                                   recovery_key_invalid_inputs_label.place_forget()
                                                   ])

User.entered_login_username.trace("w", lambda *args: [Misc.clear_white_spaces(User.entered_login_username),
                                                      Misc.entry_character_length_limit(User.entered_login_username,
                                                                                        User.MAXIMUM_USERNAME_LENGTH)
                                                      ])
User.entered_login_password.trace("w", lambda *args: Misc.clear_non_digit_nor_letter(User.entered_login_password))
User.recovery_key_username.trace("w", lambda *args: [Misc.clear_white_spaces(User.recovery_key_username),
                                                     Misc.entry_character_length_limit(User.recovery_key_username,
                                                                                       User.MAXIMUM_USERNAME_LENGTH),
                                                     recovery_key_invalid_inputs_label.place_forget()
                                                     ])

# Composition Variables
Composition.chosen_new_composition_name.trace("w", lambda *args: [Misc
                                              .clear_extra_whitespaces(Composition.chosen_new_composition_name),
                                                                  Misc
                                              .entry_character_length_limit(Composition.chosen_new_composition_name,
                                                                            User.MAXIMUM_NAME_LENGTH),
                                              process_invalid_composition_name_gui_elements()
                                                                  ])
Composition.new_composition_description.trace("w", lambda *args: [Misc
                                              .clear_extra_whitespaces(Composition.new_composition_description),
                                                                  Misc
                                              .copy_var_value_to_text_widget(Composition.new_composition_description,
                                                                             new_composition_description_text),
                                                                  Misc
                                              .text_character_length_limit(Composition.new_composition_description,
                                                                           Composition.MAXIMUM_DESCRIPTION_LENGTH,
                                                                           new_composition_description_text),
                                                                  new_composition_description_length_label
                                              .config(text=f"{len(Composition.new_composition_description.get())} / "
                                                           f"{Composition.MAXIMUM_DESCRIPTION_LENGTH}")
                                                                  ])

Composition.at_least_1_note_recorded.trace("w", lambda *args: [
    [start_recording_button.config(text="Continue Recording"), go_to_save_composition_button.config(state=NORMAL),
     return_to_main_menu_button.place_forget(), abandon_composition_button.place(
        relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)
     ] if Composition.at_least_1_note_recorded.get()
    else
    [start_recording_button.config(text="Start Recording"), go_to_save_composition_button.config(state=DISABLED)]])

Composition.is_playing_composition.trace("w",
                                         lambda *args: [return_to_main_menu_button.config(state=DISABLED),
                                                        return_to_composition_sorting_button.config(state=DISABLED),
                                                        return_to_composition_sorted_button.config(state=DISABLED),
                                                        Composition.start_playing_button.config
                                                        (state=DISABLED)] if Composition.is_playing_composition.get()
                                         else [return_to_main_menu_button.config(state=NORMAL),
                                               return_to_composition_sorting_button.config(state=NORMAL),
                                               return_to_composition_sorted_button.config(state=NORMAL),
                                               Composition.start_playing_button.config(state=NORMAL)])

# Composition Sorting Variables
# Config frames
Composition.sort_by_user.trace("w", lambda *args: config_sort_by_user_frame())
Composition.sort_by_length.trace("w", lambda *args: config_sort_by_length_frame())
Composition.sort_by_date.trace("w", lambda *args: config_sort_by_date_frame())
Composition.sort_by_rating.trace("w", lambda *args: config_sort_by_rating_frame())
# Trace length variables
Composition.short_length.trace("w", lambda *args: sort_compositions_invalid_length_selection())
Composition.medium_length.trace("w", lambda *args: sort_compositions_invalid_length_selection())
Composition.long_length.trace("w", lambda *args: sort_compositions_invalid_length_selection())
# Trace date variables
# Specific date
Composition.sort_date_selected_day.trace("w", lambda *args: [config_date_selection_comboboxes(
    var=Composition.sort_date_selected_day, target="Specific",
    day_var=Composition.sort_date_selected_day,
    month_var=Composition.sort_date_selected_month,
    year_var=Composition.sort_date_selected_year),
    sort_compositions_invalid_date_input()])
Composition.sort_date_selected_month.trace("w", lambda *args: [config_date_selection_comboboxes(
    var=Composition.sort_date_selected_month, target="Specific",
    day_var=Composition.sort_date_selected_day,
    month_var=Composition.sort_date_selected_month,
    year_var=Composition.sort_date_selected_year),
    sort_compositions_invalid_date_input()])
Composition.sort_date_selected_year.trace("w", lambda *args: [config_date_selection_comboboxes(
    var=Composition.sort_date_selected_year, target="Specific",
    day_var=Composition.sort_date_selected_day,
    month_var=Composition.sort_date_selected_month,
    year_var=Composition.sort_date_selected_year),
    sort_compositions_invalid_date_input()])
# Date interval
# From ...
Composition.sort_date_selected_day_from.trace("w", lambda *args: [config_date_selection_comboboxes(
    var=Composition.sort_date_selected_day_from, target="Interval From",
    day_var=Composition.sort_date_selected_day_from,
    month_var=Composition.sort_date_selected_month_from,
    year_var=Composition.sort_date_selected_year_from),
    sort_compositions_invalid_date_input()])
Composition.sort_date_selected_month_from.trace("w", lambda *args: [config_date_selection_comboboxes(
    var=Composition.sort_date_selected_month_from, target="Interval From",
    day_var=Composition.sort_date_selected_day_from,
    month_var=Composition.sort_date_selected_month_from,
    year_var=Composition.sort_date_selected_year_from),
    sort_compositions_invalid_date_input()])
Composition.sort_date_selected_year_from.trace("w", lambda *args: [config_date_selection_comboboxes(
    var=Composition.sort_date_selected_year_from, target="Interval From",
    day_var=Composition.sort_date_selected_day_from,
    month_var=Composition.sort_date_selected_month_from,
    year_var=Composition.sort_date_selected_year_from),
    sort_compositions_invalid_date_input()])
# ... to
Composition.sort_date_selected_day_to.trace("w", lambda *args: [config_date_selection_comboboxes(
    var=Composition.sort_date_selected_day_to, target="Interval To",
    day_var=Composition.sort_date_selected_day_to,
    month_var=Composition.sort_date_selected_month_to,
    year_var=Composition.sort_date_selected_year_to),
    sort_compositions_invalid_date_input()])
Composition.sort_date_selected_month_to.trace("w", lambda *args: [config_date_selection_comboboxes(
    var=Composition.sort_date_selected_month_to, target="Interval To",
    day_var=Composition.sort_date_selected_day_to,
    month_var=Composition.sort_date_selected_month_to,
    year_var=Composition.sort_date_selected_year_to),
    sort_compositions_invalid_date_input()])
Composition.sort_date_selected_year_to.trace("w", lambda *args: [config_date_selection_comboboxes(
    var=Composition.sort_date_selected_year_to, target="Interval To",
    day_var=Composition.sort_date_selected_day_to,
    month_var=Composition.sort_date_selected_month_to,
    year_var=Composition.sort_date_selected_year_to),
    sort_compositions_invalid_date_input()])
# Trace rating variables
Composition.no_rating.trace("w", lambda *args: sort_compositions_invalid_rating_selection())
Composition.star_1_rating.trace("w", lambda *args: sort_compositions_invalid_rating_selection())
Composition.star_2_rating.trace("w", lambda *args: sort_compositions_invalid_rating_selection())
Composition.star_3_rating.trace("w", lambda *args: sort_compositions_invalid_rating_selection())
Composition.star_4_rating.trace("w", lambda *args: sort_compositions_invalid_rating_selection())
Composition.star_5_rating.trace("w", lambda *args: sort_compositions_invalid_rating_selection())
# In playback composition
Composition.given_rating.trace("w", lambda *args: [config_current_rating_label(),
                                                   [Composition.give_composition_rating(),
                                                    config_sorted_menu(composition=Composition.composition_to_play),
                                                    Sounds.play_gui_sound(Sounds.GOOD_RATE_SOUND_PATH)
                                                    if Settings.chosen_gui_sound_setting.get()
                                                       and not Composition.is_playing_composition.get()
                                                       and Composition.given_rating.get() == Misc.STAR_5
                                                    else Sounds.play_gui_sound(Sounds.BAD_RATE_SOUND_PATH)
                                                    if Settings.chosen_gui_sound_setting.get()
                                                       and not Composition.is_playing_composition.get()
                                                       and Composition.given_rating.get() == Misc.STAR_1
                                                    else None
                                                    ]
                                                   if Composition.is_in_start_playback_menu.get() else None])
# Inclusive / Exclusive variables
# User
Composition.user_inclusive_exclusive.trace("w", lambda *args: sort_compositions_invalid_user_selection(
    Composition.sort_user_selected_user.get()
))
# Date
Composition.date_specific_inclusive_exclusive.trace("w", lambda *args: sort_compositions_invalid_date_input())
Composition.date_interval_inclusive_exclusive.trace("w", lambda *args: sort_compositions_invalid_date_input())
# Trace invalid sorting options variables
# Any invalid sorting option
Composition.is_any_invalid_sorting_option.trace("w", lambda *args: proceed_to_sorted_button.config(state=DISABLED)
                                                if Composition.is_any_invalid_sorting_option.get()
                                                else proceed_to_sorted_button.config(state=NORMAL))
# Specific invalid sorting options
Composition.is_invalid_user_sorting_option.trace("w", lambda *args: Composition.
                                                 is_any_invalid_sorting_option.
                                                 set(Composition.is_any_invalid_sorting_option_get()))
Composition.is_invalid_length_sorting_option.trace("w", lambda *args: Composition.
                                                   is_any_invalid_sorting_option.
                                                   set(Composition.is_any_invalid_sorting_option_get()))
Composition.is_invalid_date_sorting_option.trace("w", lambda *args: Composition.
                                                 is_any_invalid_sorting_option.
                                                 set(Composition.is_any_invalid_sorting_option_get()))
Composition.is_invalid_rating_sorting_option.trace("w", lambda *args: Composition.
                                                   is_any_invalid_sorting_option.
                                                   set(Composition.is_any_invalid_sorting_option_get()))
# Specific selected user variable
Composition.sort_user_selected_user.trace("w", lambda *args: [Misc.clear_white_spaces(
                                                              Composition.sort_user_selected_user),
                                                              Misc.entry_character_length_limit(
                                                              Composition.sort_user_selected_user,
                                                              User.MAXIMUM_USERNAME_LENGTH),
                                                              sort_compositions_invalid_user_selection(
                                                              Composition.sort_user_selected_user.get()),
                                                              check_if_selected_user_in_listbox(
                                                              Composition.sort_user_selected_user.get())
                                                              ])


"""General Elements"""


quit_button = Button(text="QUIT", bg="red", font=verdana_25, command=lambda: quit_app())  # No sound command needed
return_to_main_menu_button = Button(text="Return to Main Menu", font=verdana_25,
                                    command=lambda: [display_main_menu(),
                                                     Stats.returned_to_main_menu.set(
                                                         Stats.returned_to_main_menu.get() + 1),
                                                     clear_register_user_variables(),
                                                     clear_login_menu_variables(),
                                                     clear_password_recovery_variables(),
                                                     clear_new_composition_variables(),
                                                     clear_sorting_composition_variables()
                                                     if User.is_logged_in
                                                     and Composition.at_least_1_public_composition.get() else None,
                                                     [User.is_in_registration_successful.set(False),
                                                      create_recovery_key_txt_file_button.config(
                                                          text="Create .txt File", state=NORMAL)]
                                                     if User.is_in_registration_successful.get() else None,
                                                     Composition.reset_composition_stop_cause_counters(),
                                                     Composition.composition_to_play.clear(),
                                                     Composition.is_in_start_playback_menu.set(False),
                                                     Composition.is_in_sorted_menu.set(False),
                                                     Settings.is_in_settings_menu.set(False),
                                                     Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                     if Settings.chosen_gui_sound_setting.get() else None
                                                     ])
return_to_login_button = Button(text="Return to Login", font=verdana_25,
                                command=lambda: [display_login(), clear_password_recovery_variables(),
                                                 Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                 if Settings.chosen_gui_sound_setting.get() else None
                                                 ])
return_to_choose_instrument_button = Button(text="Change Instrument", font=verdana_25,
                                            command=lambda: [display_choose_instrument(),
                                                             Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                             if Settings.chosen_gui_sound_setting.get()
                                                             else None])
return_to_stats_menu_button = Button(text="Return to Stats", font=verdana_25,
                                     command=lambda: [display_stats(),
                                                      Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                      if Settings.chosen_gui_sound_setting.get() else None])
return_to_composition_sorting_button = Button(text="Return to Sorting", font=verdana_25,
                                              command=lambda: [display_playback_composition_sort(),
                                                               Composition.composition_to_play.clear(),
                                                               Composition.is_in_start_playback_menu.set(False),
                                                               Composition.is_in_sorted_menu.set(False),
                                                               Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                               if Settings.chosen_gui_sound_setting.get()
                                                               else None
                                                               ])
return_to_composition_sorted_button = Button(root, text="Return to Sorted", font=verdana_25,
                                             command=lambda: [display_playback_composition_sorted(),
                                                              Composition.composition_to_play.clear(),
                                                              Composition.is_in_start_playback_menu.set(False),
                                                              Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                              if Settings.chosen_gui_sound_setting.get()
                                                              else None
                                                              ])
next_button = Button(text="Next", font=verdana_25,
                     command=lambda: [Misc.clear_leading_and_trailing_whitespace(
                         User.chosen_first_name, User.chosen_last_name, User.chosen_nickname),
                         User.chosen_nickname.set("") if Misc.empty_string(User.chosen_nickname.get()) else None,
                         display_register_user_username_password()
                         if User.is_valid_register_user_data(first_name=User.chosen_first_name.get(),
                                                             last_name=User.chosen_last_name.get(),
                                                             year=User.chosen_birth_year.get(),
                                                             month=User.chosen_birth_month.get(),
                                                             day=User.chosen_birth_day.get())
                         else highlight_invalid_register_user_names(first_name=User.chosen_first_name.get(),
                                                                    last_name=User.chosen_last_name.get()),
                         Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                         if Settings.chosen_gui_sound_setting.get() else None
                     ])
# back_to_previous_menu_button is used in the Help menu
back_to_previous_menu_button = Button(text="Back to Previous Menu", font=verdana_25,
                                      command=lambda: [display_register_user_general_data()
                                                       if User.is_in_register_user_menu_general_data.get()
                                                       else display_register_user_username_password(),
                                                       Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                       if Settings.chosen_gui_sound_setting.get()
                                                       else None])
# back_button is used in the Register user (username and password) menu
back_button = Button(text="Back", font=verdana_25,
                     command=lambda: [display_register_user_general_data(),
                                      Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                      if Settings.chosen_gui_sound_setting.get() else None])
help_button = Button(text="Help", font=verdana_25,
                     command=lambda: [display_help(),
                                      Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                      if Settings.chosen_gui_sound_setting.get() else None])
# Login First Label is used to tell the user to log in before being able to access a particular feature
login_first_label = Label(text="Please Log In or Register to access this feature!",
                          font=verdana_20, fg=Settings.chosen_invalid_text_color.get())


"""Main Menu Elements"""

music_by_jurj_label = Label(root, text="Music by Jurj - Beta_v2", font=verdana_15, anchor=NW)

main_menu_label = Label(text="Main Menu", font=courier_100)

play_freely_button = Button(text="Play Freely", font=verdana_25,
                            command=lambda: [display_choose_instrument(),
                                             Stats.main_menu_interactions_played_freely.set(
                                                 Stats.main_menu_interactions_played_freely.get() + 1),
                                             Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None
                                             ])

record_composition_button = Button(text="Record Composition", font=verdana_25,
                                   command=lambda: [[Composition.is_recording_composition.set(True),
                                                     display_new_composition_id_card(),
                                                     Stats.main_menu_interactions_recorded_compositions.set(
                                                         Stats.main_menu_interactions_recorded_compositions.get() + 1)
                                                     ]
                                                    if User.is_logged_in else login_first_label.place(
                                       relheight=0.05, relwidth=0.5, relx=0.25, rely=0.85),
                                                    Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                    if Settings.chosen_gui_sound_setting.get() else None
                                                    ])

playback_composition_button = Button(text="Playback Composition", font=verdana_25,
                                     command=lambda: [
                                         [display_playback_composition_sort()
                                          if Composition.at_least_1_public_composition.get()
                                          else no_compositions_label.place(
                                             relheight=0.05, relwidth=0.35, relx=0.625, rely=.25 + .08 * 2),
                                          Stats.main_menu_interactions_listened_compositions.set(
                                             Stats.main_menu_interactions_listened_compositions.get() + 1)
                                          ]
                                         if User.is_logged_in else login_first_label.place(
                                             relheight=0.05, relwidth=0.5, relx=0.25, rely=0.85),
                                         Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                         if Settings.chosen_gui_sound_setting.get() else None
                                     ])

# TODO: Add composition manager
# composition_manager_button = Button(text="Composition Manager", font=verdana_25,
#                                     command=lambda: [
#                                         [Stats.main_menu_interactions_managed_compositions.set(
#                                             Stats.main_menu_interactions_managed_compositions.get() + 1)
#                                          ]
#                                         if User.is_logged_in else login_first_label.place(
#                                             relheight=0.05, relwidth=0.5, relx=0.25, rely=0.85)
#                                     ])

settings_button = Button(text="Settings", font=verdana_25,
                         command=lambda: [display_settings(),
                                          Stats.main_menu_interactions_entered_settings.set(
                                              Stats.main_menu_interactions_entered_settings.get() + 1),
                                          Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                          if Settings.chosen_gui_sound_setting.get() else None
                                          ])

stats_button = Button(text="Stats", font=verdana_25,
                      command=lambda: [display_stats(),
                                       Stats.main_menu_interactions_viewed_stats.set(
                                           Stats.main_menu_interactions_viewed_stats.get() + 1),
                                       Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                       if Settings.chosen_gui_sound_setting.get() else None
                                       ])

go_to_login_button = Button(text="Log In", font=verdana_25,
                            command=lambda: [display_login(),
                                             Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None
                                             ])

go_to_logout_button = Button(text="Log Out", font=verdana_25,
                             command=lambda: [display_sure_logout(),
                                              Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                              if Settings.chosen_gui_sound_setting.get() else None
                                              ])

go_to_register_button = Button(text="Sign Up", font=verdana_25,
                               command=lambda: [User.came_from_main_menu.set(True),
                                                display_register_user_general_data(),
                                                Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                if Settings.chosen_gui_sound_setting.get() else None
                                                ])

go_to_profile_button = Button(text="Profile", font=verdana_25,
                              command=lambda: [display_user_profile(user=User.logged_in_user),
                                               Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                               if Settings.chosen_gui_sound_setting.get() else None])

logged_in_user_username_label = Label(text="Logged In User: USERNAME", font=verdana_25)

remember_me_checkbutton = Checkbutton(text="Remember Me", font=verdana_25, variable=User.remember_me, onvalue=True,
                                      offvalue=False,
                                      command=lambda: Sounds.play_gui_sound(Sounds.CHECKBUTTON_SOUND_PATH)
                                      if Settings.chosen_gui_sound_setting.get() else None)


"""Choose Instrument Menu Elements"""


choose_instrument_labelframe = LabelFrame(root, text="Choose Instrument:", font=verdana_28, labelanchor=N)

choose_instrument_option_menu = OptionMenu(root, Sounds.chosen_instrument, *Sounds.INSTRUMENTS_TUPLE,
                                           command=lambda *args: Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                           if Settings.chosen_gui_sound_setting.get() else None)
choose_instrument_option_menu.config(font=verdana_28_underline, borderwidth=4, indicatoron=0, highlightthickness=0)
choose_instrument_option_menu["menu"].config(font=verdana_28)

about_chosen_instrument_label = Label(text="About Chosen Instrument:", font=verdana_28)
about_chosen_instrument_text = ScrolledText(root, font=times_new_roman_25, spacing1=10, spacing2=5, spacing3=5,
                                            wrap=WORD, state=DISABLED, borderwidth=3)

available_notes_labelframe = LabelFrame(root, text="Available Notes:", font=verdana_28, labelanchor=N)
available_notes_label = Label(text="NOTES", font=verdana_30)
# For Piano only
note_length_mention_label = Label(text="Both Long & Short Versions!", font=verdana_25)

play_instrument_button = Button(text="Play Instrument", font=verdana_25,
                                command=lambda: [Sounds.update_last_used_instrument(Sounds.chosen_instrument.get()),
                                                 display_play_notes(Sounds.chosen_instrument.get()),
                                                 Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                 if Settings.chosen_gui_sound_setting.get() else None
                                                 ])

# Used both in Play Freely and Record Composition
currently_playing_label = Label(text="Currently Playing: None", font=verdana_30)

# Separators
# The top line of the menu
choose_instrument_separator_1 = Separator(root)
choose_instrument_separator_2 = Separator(root)
# Around the "about instrument" label
choose_instrument_separator_3 = Separator(root)
choose_instrument_separator_4 = Separator(root)
# The vertical sidelines of the menu
choose_instrument_separator_5 = Separator(root, orient=VERTICAL)
choose_instrument_separator_6 = Separator(root, orient=VERTICAL)
# The bottom line of the menu
choose_instrument_separator_7 = Separator(root)
choose_instrument_separator_8 = Separator(root)


"""New Composition Record Composition Menu Elements"""


record_new_composition_label = Label(text="New Composition", font=courier_100)

new_composition_intro_label = Label(text="Before proceeding to record your new masterpiece, "
                                         "please provide a few details about your work & vision!",
                                    font=verdana_25)
new_composition_number_label = Label(text="This would be your Xth composition!", font=verdana_25)

new_composition_labelframe = LabelFrame(text="New Composition ID Card:", font=verdana_30, labelanchor=N)

new_composition_composer_label = Label(text="Composer  :", font=verdana_25, anchor=E)
new_composition_composer_data_label = Label(text="USERNAME", font=verdana_25, anchor=W)

new_composition_name_label = Label(text="Composition Name  :", font=verdana_25, anchor=E)
new_composition_name_entry = Entry(root, font=verdana_25, justify=CENTER, borderwidth=3,
                                   textvariable=Composition.chosen_new_composition_name)
new_composition_name_help_label = Label(text=f"Min. 1 - Max. {User.MAXIMUM_NAME_LENGTH} characters",
                                        font=verdana_11)

new_composition_description_label = Label(text="Description  :\n(Optional)   ", font=verdana_25, anchor=E)
new_composition_description_text = ScrolledText(root, font=tempus_sans_itc_20_bold, spacing1=10, spacing2=5,
                                                spacing3=5, wrap=WORD, borderwidth=3)
new_composition_description_text.bind("<KeyRelease>",
                                      lambda *args: Composition.new_composition_description
                                      .set(new_composition_description_text.get('1.0', 'end-1c')))
new_composition_description_length_label = Label(text=f"0 / {Composition.MAXIMUM_DESCRIPTION_LENGTH}",
                                                 font=verdana_15, anchor=E)

new_composition_input_warning_label = Label(text="Warning: Returning to the Main Menu will clear all input data "
                                                 "from here.",
                                            font=verdana_15)

invalid_composition_name_label = Label(text="INVALID MESSAGE", font=verdana_25,
                                       fg=Settings.chosen_invalid_text_color.get())

start_recording_button = Button(text="Start Recording", font=verdana_25, state=DISABLED,
                                command=lambda:
                                [Misc.remove_text_widget_leading_and_trailing_whitespaces(
                                    Composition.new_composition_description, new_composition_description_text),
                                 display_choose_instrument()
                                 if Composition.is_new_composition_name_valid(
                                     composition_name=Composition.chosen_new_composition_name)
                                 else None,
                                 Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                 if Settings.chosen_gui_sound_setting.get() else None
                                 ])


"""Play Freely Menu Elements"""


play_freely_label = Label(text="Play Freely", font=courier_100)


"""Record Composition Menu Elements"""


record_composition_label = Label(text="Record Composition", font=courier_100)

return_to_composition_id_card_button = Button(text="Return to ID Card", font=verdana_25,
                                              command=lambda: [display_new_composition_id_card(),
                                                               Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                               if Settings.chosen_gui_sound_setting.get()
                                                               else None
                                                               ])

delay_scale = Scale(root, variable=Composition.delay_scale_value, from_=0, to=Composition.MAXIMUM_DELAY_SLIDER_VALUE,
                    tickinterval=0.5, orient=HORIZONTAL, resolution=0.01, width=25, font=verdana_13, bd=4)

go_to_save_composition_button = Button(root, text="Save Composition", font=verdana_25, state=DISABLED,
                                       command=lambda: [display_save_composition(),
                                                        Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                        if Settings.chosen_gui_sound_setting.get() else None
                                                        ])

abandon_composition_button = Button(text="Abandon Composition", font=verdana_25,
                                    command=lambda: [display_abandon_composition(),
                                                     Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                     if Settings.chosen_gui_sound_setting.get() else None
                                                     ])


"""Sure Abandon Composition Elements"""


abandon_composition_label = Label(text="Abandon Composition?", font=courier_100)

sure_abandon_composition_label = Label(text="Are you sure you want to abandon your current masterpiece?\n"
                                            "Your awesome work will not be saved if decide to do such...",
                                       font=tempus_sans_itc_43_bold_italic)

abandon_composition_labelframe = LabelFrame(root, text="Abandon Composition?", font=verdana_40, labelanchor=N,
                                            borderwidth=5)

abandon_composition_return_to_composition_id_card_button = Button(text="Return to ID Card", font=verdana_32,
                                                                  borderwidth=3,
                                                                  command=lambda: [display_new_composition_id_card(),
                                                                                   Sounds.play_gui_sound(
                                                                                       Sounds.BUTTON_SOUND_PATH)
                                                                                   if Settings.
                                                                                   chosen_gui_sound_setting.
                                                                                   get() else None])

abandon_composition_save_composition_button = Button(root, text="Save Composition", font=verdana_32,
                                                     borderwidth=3,
                                                     command=lambda: [display_save_composition(),
                                                                      Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                                      if Settings.
                                                                      chosen_gui_sound_setting.get()
                                                                      else None])

yes_abandon_composition_button = Button(text="Yes, Abandon Composition", font=verdana_32, borderwidth=3,
                                        command=lambda: [clear_new_composition_variables(), display_main_menu(),
                                                         Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                         if Settings.chosen_gui_sound_setting.get() else None
                                                         ])


"""Save Composition Elements"""


save_composition_menu_label = Label(text="Save Composition", font=courier_100)

save_composition_intro_label = Label(text="Your masterpiece is ready to make history in the world of music!",
                                     font=verdana_25)

save_composition_labelframe = LabelFrame(text="Composition ID Card:", font=verdana_30, labelanchor=N)

save_composition_composer_label = Label(text="Composer : ", font=verdana_25, anchor=E)
save_composition_composer_text = ScrolledText(root, font=fixed_25, wrap=WORD, borderwidth=3)

save_composition_name_label = Label(text="Composition Name : ", font=verdana_25, anchor=E)
save_composition_name_text = ScrolledText(root, font=fixed_25, wrap=WORD, borderwidth=3)

save_composition_description_label = Label(text="Description : ", font=verdana_25, anchor=E)
save_composition_description_text = ScrolledText(root, font=tempus_sans_itc_20_bold, spacing1=10, spacing2=5,
                                                 spacing3=5, wrap=WORD, borderwidth=3)
save_composition_description_length_label = Label(text=f"Description Length : \n"
                                                       f"XXX / {Composition.MAXIMUM_DESCRIPTION_LENGTH}",
                                                  anchor=E, font=verdana_25)

# Separator
save_composition_separator = Separator(root)

save_composition_notes_and_delays_label = Label(text="Notes And Delays : ", font=verdana_25, anchor=E)
save_composition_notes_and_delays_text = ScrolledText(root, font=fixed_25, wrap=WORD, borderwidth=3)
save_composition_composition_length_label = Label(text="Composition Length : ", font=verdana_25, anchor=E)
save_composition_composition_length_text = ScrolledText(root, font=fixed_25, wrap=WORD, borderwidth=3)

save_composition_button = Button(text="Save Composition", font=verdana_25,
                                 command=lambda: [Composition.save_new_composition(
                                     composition_name=Composition.chosen_new_composition_name.get(),
                                     composition_description=Composition.new_composition_description.get()),
                                                  Composition.update_composer_list(),
                                                  display_saved_composition(),
                                                  clear_new_composition_variables(),
                                                  Stats.compositions_active.set(Stats.compositions_active.get() + 1),
                                                  Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                  if Settings.chosen_gui_sound_setting.get() else None
                                 ])

save_composition_back_label = Label(text="Want to make some final adjustments? You're free to go back before saving!",
                                    font=verdana_25)


"""Saved Composition Elements"""


saved_composition_menu_label = Label(text="Saved Composition", font=courier_100)

saved_composition_intro_labelframe = LabelFrame(text="Composition Saved Successfully!", font=verdana_50,
                                                labelanchor=N)

saved_composition_one_of_many_label = Label(saved_composition_intro_labelframe, text="You are 1 of X proud composers!",
                                            font=verdana_30)
saved_composition_public_label = Label(saved_composition_intro_labelframe, text="X of them have public compositions!",
                                       font=verdana_30)
saved_composition_private_label = Label(saved_composition_intro_labelframe, text="X of them have private "
                                        "compositions...", font=verdana_30)
saved_composition_left_to_join_label = Label(saved_composition_intro_labelframe,
                                             text="X users have yet to compose at least 1 masterpiece!",
                                             font=verdana_30)


"""Play Freely Number Of Notes Labels"""


number_of_notes_played_freely_labelframe = LabelFrame(text=Sounds.default_number_of_notes_played_label_text,
                                                      font=verdana_25)
number_of_piano_notes_played_freely_label = Label(text=Sounds.default_number_of_piano_notes_played_label_text,
                                                  font=verdana_25, anchor=W)
number_of_flute_notes_played_freely_label = Label(text=Sounds.default_number_of_flute_notes_played_label_text,
                                                  font=verdana_25, anchor=W)
number_of_trumpet_notes_played_freely_label = Label(text=Sounds.default_number_of_trumpet_notes_played_label_text,
                                                    font=verdana_25, anchor=W)
number_of_violin_notes_played_freely_label = Label(text=Sounds.default_number_of_violin_notes_played_label_text,
                                                   font=verdana_25, anchor=W)

last_note_played_freely_label = Label(text="Last note played: None", font=verdana_25, anchor=W)

# Reset note count labels
reset_note_count_button = Button(text="Reset Note Count", font=verdana_25, state=DISABLED,
                                 command=lambda: [clear_note_count_dict_and_labels(),
                                                  reset_note_count_button.config(state=DISABLED),
                                                  Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                  if Settings.chosen_gui_sound_setting.get() else None
                                                  ])


"""Record Composition Number Of Notes Labels"""


composition_length_label = Label(root, text="Length: 0 seconds", font=verdana_25, anchor=W)

delay_label = Label(root, text="Delay* : ", font=verdana_25, anchor=E)
delay_star_label = Label(root, text=f"*Determines the length of the pause between the current and "
                                    f"next note to be played.\nCalculated in seconds; Min. 0 - "
                                    f"Max. {Composition.MAXIMUM_DELAY_SLIDER_VALUE}", font=verdana_13)

number_of_notes_played_record_labelframe = LabelFrame(text=Sounds.default_number_of_notes_played_label_text,
                                                      font=verdana_25)
number_of_piano_notes_played_record_label = Label(text=Sounds.default_number_of_piano_notes_played_label_text,
                                                  font=verdana_25,
                                                  anchor=W)
number_of_flute_notes_played_record_label = Label(text=Sounds.default_number_of_flute_notes_played_label_text,
                                                  font=verdana_25, anchor=W)
number_of_trumpet_notes_played_record_label = Label(text=Sounds.default_number_of_trumpet_notes_played_label_text,
                                                    font=verdana_25, anchor=W)
number_of_violin_notes_played_record_label = Label(text=Sounds.default_number_of_violin_notes_played_label_text,
                                                   font=verdana_25, anchor=W)

last_note_played_record_label = Label(text="Last note played: None", font=verdana_25, anchor=W)


"""Piano Elements"""


do_1_button = Button(text="Do 1", font=verdana_45,
                     command=lambda: [
                         Sounds.play_note("Piano", "Do 1", Sounds.piano_note_length.get()),
                         Composition.add_note_and_delay("Piano", "Do 1", delay_scale.get(),
                                                        Sounds.piano_note_length.get())
                         if Composition.is_recording_composition.get() else None,
                         config_last_note_played_label("Do 1", "Piano", Sounds.piano_note_length.get()),
                         increment_number_of_notes("Piano", Sounds.piano_note_length.get()),
                         Stats.short_do_1_piano_notes_played.set(Stats.short_do_1_piano_notes_played.get() + 1)
                         if Sounds.piano_note_length.get() == "Short"
                         else Stats.long_do_1_piano_notes_played.set(Stats.long_do_1_piano_notes_played.get() + 1)
                     ])
re_button = Button(text="Re", font=verdana_45,
                   command=lambda: [
                       Sounds.play_note("Piano", "Re", Sounds.piano_note_length.get()),
                       Composition.add_note_and_delay("Piano", "Re", delay_scale.get(),
                                                      Sounds.piano_note_length.get())
                       if Composition.is_recording_composition.get() else None,
                       config_last_note_played_label("Re", "Piano", Sounds.piano_note_length.get()),
                       increment_number_of_notes("Piano", Sounds.piano_note_length.get()),
                       Stats.short_re_piano_notes_played.set(Stats.short_re_piano_notes_played.get() + 1)
                       if Sounds.piano_note_length.get() == "Short"
                       else Stats.long_re_piano_notes_played.set(Stats.long_re_piano_notes_played.get() + 1)
                   ])
mi_button = Button(text="Mi", font=verdana_45,
                   command=lambda: [
                       Sounds.play_note("Piano", "Mi", Sounds.piano_note_length.get()),
                       Composition.add_note_and_delay("Piano", "Mi", delay_scale.get(),
                                                      Sounds.piano_note_length.get())
                       if Composition.is_recording_composition.get() else None,
                       config_last_note_played_label("Mi", "Piano", Sounds.piano_note_length.get()),
                       increment_number_of_notes("Piano", Sounds.piano_note_length.get()),
                       Stats.short_mi_piano_notes_played.set(Stats.short_mi_piano_notes_played.get() + 1)
                       if Sounds.piano_note_length.get() == "Short"
                       else Stats.long_mi_piano_notes_played.set(Stats.long_mi_piano_notes_played.get() + 1)
                   ])
fa_button = Button(text="Fa", font=verdana_45,
                   command=lambda: [
                       Sounds.play_note("Piano", "Fa", Sounds.piano_note_length.get()),
                       Composition.add_note_and_delay("Piano", "Fa", delay_scale.get(),
                                                      Sounds.piano_note_length.get())
                       if Composition.is_recording_composition.get() else None,
                       config_last_note_played_label("Fa", "Piano", Sounds.piano_note_length.get()),
                       increment_number_of_notes("Piano", Sounds.piano_note_length.get()),
                       Stats.short_fa_piano_notes_played.set(Stats.short_fa_piano_notes_played.get() + 1)
                       if Sounds.piano_note_length.get() == "Short"
                       else Stats.long_fa_piano_notes_played.set(Stats.long_fa_piano_notes_played.get() + 1)
                   ])
sol_button = Button(text="Sol", font=verdana_45,
                    command=lambda: [
                        Sounds.play_note("Piano", "Sol", Sounds.piano_note_length.get()),
                        Composition.add_note_and_delay("Piano", "Sol", delay_scale.get(),
                                                       Sounds.piano_note_length.get())
                        if Composition.is_recording_composition.get() else None,
                        config_last_note_played_label("Sol", "Piano", Sounds.piano_note_length.get()),
                        increment_number_of_notes("Piano", Sounds.piano_note_length.get()),
                        Stats.short_sol_piano_notes_played.set(Stats.short_sol_piano_notes_played.get() + 1)
                        if Sounds.piano_note_length.get() == "Short"
                        else Stats.long_sol_piano_notes_played.set(Stats.long_sol_piano_notes_played.get() + 1)
                    ])
la_button = Button(text="La", font=verdana_45,
                   command=lambda: [
                       Sounds.play_note("Piano", "La", Sounds.piano_note_length.get()),
                       Composition.add_note_and_delay("Piano", "La", delay_scale.get(),
                                                      Sounds.piano_note_length.get())
                       if Composition.is_recording_composition.get() else None,
                       config_last_note_played_label("La", "Piano", Sounds.piano_note_length.get()),
                       increment_number_of_notes("Piano", Sounds.piano_note_length.get()),
                       Stats.short_la_piano_notes_played.set(Stats.short_la_piano_notes_played.get() + 1)
                       if Sounds.piano_note_length.get() == "Short"
                       else Stats.long_la_piano_notes_played.set(Stats.long_la_piano_notes_played.get() + 1)
                   ])
si_button = Button(text="Si", font=verdana_45,
                   command=lambda: [
                       Sounds.play_note("Piano", "Si",
                                        Sounds.piano_note_length.get()),
                       Composition.add_note_and_delay("Piano", "Si", delay_scale.get(),
                                                      Sounds.piano_note_length.get())
                       if Composition.is_recording_composition.get() else None,
                       config_last_note_played_label("Si", "Piano", Sounds.piano_note_length.get()),
                       increment_number_of_notes("Piano", Sounds.piano_note_length.get()),
                       Stats.short_si_piano_notes_played.set(Stats.short_si_piano_notes_played.get() + 1)
                       if Sounds.piano_note_length.get() == "Short"
                       else Stats.long_si_piano_notes_played.set(Stats.long_si_piano_notes_played.get() + 1)
                   ])
do_2_button = Button(text="Do 2", font=verdana_45,
                     command=lambda: [
                         Sounds.play_note("Piano", "Do 2", Sounds.piano_note_length.get()),
                         Composition.add_note_and_delay("Piano", "Do 2", delay_scale.get(),
                                                        Sounds.piano_note_length.get())
                         if Composition.is_recording_composition.get() else None,
                         config_last_note_played_label("Do 2", "Piano", Sounds.piano_note_length.get()),
                         increment_number_of_notes("Piano", Sounds.piano_note_length.get()),
                         Stats.short_do_2_piano_notes_played.set(Stats.short_do_2_piano_notes_played.get() + 1)
                         if Sounds.piano_note_length.get() == "Short"
                         else Stats.long_do_2_piano_notes_played.set(Stats.long_do_2_piano_notes_played.get() + 1)
                     ])

note_length_label = Label(text="Note length:", font=verdana_25)

short_note_radiobutton = Radiobutton(text="Short", font=verdana_25, variable=Sounds.piano_note_length,
                                     value="Short", indicatoron=0,
                                     command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                     if Settings.chosen_gui_sound_setting.get() else None)
long_note_radiobutton = Radiobutton(text="Long", font=verdana_25, variable=Sounds.piano_note_length,
                                    value="Long", indicatoron=0,
                                    command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                    if Settings.chosen_gui_sound_setting.get() else None)


"""Flute, Trumpet & Violin Elements"""


c4_button = Button(text="C4", font=verdana_45,
                   command=lambda: [
                       Sounds.play_note(Sounds.chosen_instrument.get(), "C4"),
                       Composition.add_note_and_delay(Sounds.chosen_instrument.get(), "C4", delay_scale.get())
                       if Composition.is_recording_composition.get() else None,
                       config_last_note_played_label("C4", Sounds.chosen_instrument.get(),
                                                     Sounds.piano_note_length.get()),
                       increment_number_of_notes(Sounds.chosen_instrument.get(),
                                                 Sounds.piano_note_length.get()),
                       Stats.c4_flute_notes_played.set(Stats.c4_flute_notes_played.get() + 1)
                       if Sounds.chosen_instrument.get() == "Flute"
                       else Stats.c4_trumpet_notes_played.set(Stats.c4_trumpet_notes_played.get() + 1)
                       if Sounds.chosen_instrument.get() == "Trumpet"
                       else Stats.c4_violin_notes_played.set(Stats.c4_violin_notes_played.get() + 1)
                   ])
c5_button = Button(text="C5", font=verdana_45,
                   command=lambda: [
                       Sounds.play_note(Sounds.chosen_instrument.get(), "C5"),
                       Composition.add_note_and_delay(Sounds.chosen_instrument.get(), "C5", delay_scale.get())
                       if Composition.is_recording_composition.get() else None,
                       config_last_note_played_label("C5", Sounds.chosen_instrument.get(),
                                                     Sounds.piano_note_length.get()),
                       increment_number_of_notes(Sounds.chosen_instrument.get(),
                                                 Sounds.piano_note_length.get()),
                       Stats.c5_flute_notes_played.set(Stats.c5_flute_notes_played.get() + 1)
                       if Sounds.chosen_instrument.get() == "Flute"
                       else Stats.c5_trumpet_notes_played.set(Stats.c5_trumpet_notes_played.get() + 1)
                       if Sounds.chosen_instrument.get() == "Trumpet"
                       else Stats.c5_violin_notes_played.set(Stats.c5_violin_notes_played.get() + 1)
                   ])
c6_button = Button(text="C6", font=verdana_45,
                   command=lambda: [
                       Sounds.play_note(Sounds.chosen_instrument.get(), "C6"),
                       Composition.add_note_and_delay(Sounds.chosen_instrument.get(), "C6", delay_scale.get())
                       if Composition.is_recording_composition.get() else None,
                       config_last_note_played_label("C6", Sounds.chosen_instrument.get(),
                                                     Sounds.piano_note_length.get()),
                       increment_number_of_notes(Sounds.chosen_instrument.get(),
                                                 Sounds.piano_note_length.get()),
                       Stats.c6_flute_notes_played.set(Stats.c6_flute_notes_played.get() + 1)
                       if Sounds.chosen_instrument.get() == "Flute"
                       else Stats.c6_trumpet_notes_played.set(Stats.c6_trumpet_notes_played.get() + 1)
                       if Sounds.chosen_instrument.get() == "Trumpet"
                       else Stats.c6_violin_notes_played.set(Stats.c6_violin_notes_played.get() + 1)
                   ])
g3_button = Button(text="G3", font=verdana_45,
                   command=lambda: [
                       Sounds.play_note(Sounds.chosen_instrument.get(), "G3"),
                       Composition.add_note_and_delay(Sounds.chosen_instrument.get(), "G3", delay_scale.get())
                       if Composition.is_recording_composition.get() else None,
                       config_last_note_played_label("G3", Sounds.chosen_instrument.get(),
                                                     Sounds.piano_note_length.get()),
                       increment_number_of_notes(Sounds.chosen_instrument.get(),
                                                 Sounds.piano_note_length.get()),
                       Stats.g3_trumpet_notes_played.set(Stats.g3_trumpet_notes_played.get() + 1)
                   ])
g4_button = Button(text="G4", font=verdana_45,
                   command=lambda: [
                       Sounds.play_note(Sounds.chosen_instrument.get(), "G4"),
                       Composition.add_note_and_delay(Sounds.chosen_instrument.get(), "G4", delay_scale.get())
                       if Composition.is_recording_composition.get() else None,
                       config_last_note_played_label("G4", Sounds.chosen_instrument.get(),
                                                     Sounds.piano_note_length.get()),
                       increment_number_of_notes(Sounds.chosen_instrument.get(),
                                                 Sounds.piano_note_length.get()),
                       Stats.g4_flute_notes_played.set(Stats.g4_flute_notes_played.get() + 1)
                       if Sounds.chosen_instrument.get() == "Flute"
                       else Stats.g4_trumpet_notes_played.set(Stats.g4_trumpet_notes_played.get() + 1)
                       if Sounds.chosen_instrument.get() == "Trumpet"
                       else Stats.g4_violin_notes_played.set(Stats.g4_violin_notes_played.get() + 1)
                   ])
g5_button = Button(text="G5", font=verdana_45,
                   command=lambda: [
                       Sounds.play_note(Sounds.chosen_instrument.get(), "G5"),
                       Composition.add_note_and_delay(Sounds.chosen_instrument.get(), "G5", delay_scale.get())
                       if Composition.is_recording_composition.get() else None,
                       config_last_note_played_label("G5", Sounds.chosen_instrument.get(),
                                                     Sounds.piano_note_length.get()),
                       increment_number_of_notes(Sounds.chosen_instrument.get(),
                                                 Sounds.piano_note_length.get()),
                       Stats.g5_flute_notes_played.set(Stats.g5_flute_notes_played.get() + 1)
                       if Sounds.chosen_instrument.get() == "Flute"
                       else Stats.g5_trumpet_notes_played.set(Stats.g5_trumpet_notes_played.get() + 1)
                       if Sounds.chosen_instrument.get() == "Trumpet"
                       else Stats.g5_violin_notes_played.set(Stats.g5_violin_notes_played.get() + 1)
                   ])
g6_button = Button(text="G6", font=verdana_45,
                   command=lambda: [
                       Sounds.play_note(Sounds.chosen_instrument.get(), "G6"),
                       Composition.add_note_and_delay(Sounds.chosen_instrument.get(), "G6", delay_scale.get())
                       if Composition.is_recording_composition.get() else None,
                       config_last_note_played_label("G6", Sounds.chosen_instrument.get(),
                                                     Sounds.piano_note_length.get()),
                       increment_number_of_notes(Sounds.chosen_instrument.get(),
                                                 Sounds.piano_note_length.get()),
                       Stats.g6_flute_notes_played.set(Stats.g6_flute_notes_played.get() + 1)
                       if Sounds.chosen_instrument.get() == "Flute"
                       else Stats.g6_violin_notes_played.set(Stats.g6_violin_notes_played.get() + 1)
                   ])


"""Playback Composition Sorting Menu Elements"""

# No compositions label
no_compositions_label = Label(text="No Accessible Compositions Found!", font=verdana_25,
                              fg=Settings.chosen_invalid_text_color.get())


playback_composition_menu_label = Label(text="Playback Composition", font=courier_100)

playback_composition_labelframe = LabelFrame(text="Sorting Options:", font=verdana_25, labelanchor=N)

sort_criteria_notebook = Notebook(playback_composition_labelframe, style="Sort.TNotebook")

sort_by_user_frame = Frame(sort_criteria_notebook)
sort_by_length_frame = Frame(sort_criteria_notebook)
sort_by_date_frame = Frame(sort_criteria_notebook)
sort_by_rating_frame = Frame(sort_criteria_notebook)

sort_criteria_notebook.add(sort_by_user_frame, text="By User")
sort_criteria_notebook.add(sort_by_length_frame, text="By Length")
sort_criteria_notebook.add(sort_by_date_frame, text="By Date")
sort_criteria_notebook.add(sort_by_rating_frame, text="By Rating")

"""Sort by User elements"""

sort_user_buttons_labelframe = LabelFrame(sort_by_user_frame, text="Sorting Criteria:", labelanchor=N, font=verdana_20,
                                          relief=RIDGE, borderwidth=2)

sort_user_any_user_radiobutton = Radiobutton(sort_user_buttons_labelframe, text="Any User", font=verdana_25,
                                             variable=Composition.sort_by_user, value="Any", indicatoron=0,
                                             command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None)
sort_user_specific_user_radiobutton = Radiobutton(sort_user_buttons_labelframe, text="Specific User", font=verdana_25,
                                                  variable=Composition.sort_by_user, value="Specific", indicatoron=0,
                                                  command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                                  if Settings.chosen_gui_sound_setting.get() else None)
sort_user_specific_users_radiobutton = Radiobutton(sort_user_buttons_labelframe, text="Multiple Users", font=verdana_25,
                                                   variable=Composition.sort_by_user, value="Multiple", indicatoron=0,
                                                   command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                                   if Settings.chosen_gui_sound_setting.get() else None)

sort_user_choose_any_frame = Frame(sort_by_user_frame, relief=RIDGE, borderwidth=2)

sort_user_choose_any_label = Label(sort_user_choose_any_frame, text="Compositions will not be sorted by user.",
                                   font=verdana_25)

sort_user_choose_user_frame = Frame(sort_by_user_frame, relief=RIDGE, borderwidth=2)

sort_user_choose_user_label = Label(sort_user_choose_user_frame, text="Specific User:", font=verdana_25)
# Combobox values get configured in update_composers_list() from the Compositions module
sort_user_choose_user_combobox = Combobox(sort_user_choose_user_frame, textvariable=Composition.sort_user_selected_user,
                                          justify=CENTER, font=verdana_25)
sort_user_choose_user_combobox.bind("<<ComboboxSelected>>", lambda *args: Sounds.play_gui_sound(
    Sounds.CHECKBUTTON_SOUND_PATH) if Settings.chosen_gui_sound_setting.get() else None)

sort_user_choose_users_container_frame = Frame(sort_by_user_frame, relief=RIDGE, borderwidth=2)

sort_user_choose_users_content_frame = Frame(sort_user_choose_users_container_frame)

sort_user_add_all_button = Button(sort_user_choose_users_content_frame, text="Add All", font=verdana_25,
                                  command=lambda: [add_all_usernames_to_listbox(),
                                                   Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                   if Settings.chosen_gui_sound_setting.get() else None
                                                   ])
sort_user_remove_all_button = Button(sort_user_choose_users_content_frame, text="Remove All", font=verdana_25,
                                     state=DISABLED,
                                     command=lambda: [remove_all_usernames_from_listbox(),
                                                      Sounds.play_gui_sound(Sounds.CLEAR_SOUND_PATH)
                                                      if Settings.chosen_gui_sound_setting.get() else None
                                                      ])

sort_user_add_selected_button = Button(sort_user_choose_users_content_frame, text="Add Specific", font=verdana_25,
                                       command=lambda: [add_specific_username_to_listbox(
                                           Composition.sort_user_selected_user.get()),
                                           Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                           if Settings.chosen_gui_sound_setting.get() else None
                                       ])
sort_user_remove_selected_button = Button(sort_user_choose_users_content_frame, text="Remove Selected", font=verdana_25,
                                          command=lambda: [remove_selected_usernames_from_listbox(),
                                                           Sounds.play_gui_sound(Sounds.CLEAR_SOUND_PATH)
                                                           if Settings.chosen_gui_sound_setting.get() else None
                                                           ])

sort_user_inclusive_radiobutton = Radiobutton(sort_user_choose_users_content_frame, text="Inclusive", font=verdana_25,
                                              variable=Composition.user_inclusive_exclusive, value="Inclusive",
                                              indicatoron=0,
                                              command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                              if Settings.chosen_gui_sound_setting.get()
                                              else None)
sort_user_exclusive_radiobutton = Radiobutton(sort_user_choose_users_content_frame, text="Exclusive", font=verdana_25,
                                              variable=Composition.user_inclusive_exclusive, value="Exclusive",
                                              indicatoron=0,
                                              command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                              if Settings.chosen_gui_sound_setting.get()
                                              else None)

sort_user_separator = Separator(sort_user_choose_users_content_frame, orient=VERTICAL)

sort_user_scrolled_list_box_frame = Frame(sort_user_choose_users_content_frame)

sort_user_listbox = Listbox(sort_user_scrolled_list_box_frame, borderwidth=3, font=verdana_20, selectmode=MULTIPLE,
                            activestyle="none", selectborderwidth=2)
sort_user_listbox.bind("<<ListboxSelect>>", lambda *args: Sounds.play_gui_sound(
    sound_file_path=Sounds.SELECT_SOUND_PATH) if Settings.chosen_gui_sound_setting.get()
    and sort_user_listbox.curselection() else None)
sort_user_listbox_scroll_bar = Scrollbar(sort_user_scrolled_list_box_frame)
# Add scroll bar to list box
sort_user_listbox.config(yscrollcommand=sort_user_listbox_scroll_bar.set)
sort_user_listbox_scroll_bar.config(command=sort_user_listbox.yview)

sort_user_tip_labelframe_1 = LabelFrame(sort_by_user_frame, text="Tip 1:", labelanchor=N, font=verdana_20,
                                        relief=RIDGE, borderwidth=2)
sort_user_tip_message_1 = Message(sort_user_tip_labelframe_1, text="The Add Specific operates on the currently "
                                                                   "selected specific user.\nThe Remove Selected "
                                                                   "operates on the currently selected list box "
                                                                   "user(s).",
                                  font=verdana_15, aspect=230, justify=LEFT)

sort_user_tip_labelframe_2 = LabelFrame(sort_by_user_frame, text="Tip 2:", labelanchor=N, font=verdana_20,
                                        relief=RIDGE, borderwidth=2)
sort_user_tip_message_2 = Message(sort_user_tip_labelframe_2, text="The Any option will not sort by users at all; "
                                                                   "while it is selected, the GUI elements and "
                                                                   "widgets for sorting by specific & multiple "
                                                                   "users will be disabled.",
                                  font=verdana_15, aspect=230, justify=LEFT)

sort_user_reserved_label = Label(sort_user_choose_users_container_frame,
                                 text="This GUI section is reserved for sorting by Multiple Users.\n"
                                 "It will become active when you do so.", font=verdana_30)

# Invalid selection labels
sort_user_invalid_composer_name_label = Label(sort_user_choose_users_container_frame,
                                              text="Invalid specific composer name!\nSelect a valid name from the "
                                                   "drop-down menu!",
                                              font=verdana_30, fg=Settings.chosen_invalid_text_color.get())

# no_public_composers_label

"""Sort by Composition Length elements"""

sort_length_buttons_labelframe = LabelFrame(sort_by_length_frame, text="Sorting Criteria:", labelanchor=N,
                                            font=verdana_20, relief=RIDGE, borderwidth=2)

sort_length_any_length_radiobutton = Radiobutton(sort_length_buttons_labelframe, text="Any Length",
                                                 font=verdana_25,
                                                 variable=Composition.sort_by_length,
                                                 value="Any", indicatoron=0,
                                                 command=lambda: Sounds.play_gui_sound(
                                                     Sounds.RADIOBUTTON_SOUND_PATH)
                                                 if Settings.chosen_gui_sound_setting.get() else None)
sort_length_specific_length_radiobutton = Radiobutton(sort_length_buttons_labelframe, text="Specific Length",
                                                      font=verdana_25,
                                                      variable=Composition.sort_by_length,
                                                      value="Specific", indicatoron=0,
                                                      command=lambda: Sounds.play_gui_sound(
                                                          Sounds.RADIOBUTTON_SOUND_PATH)
                                                      if Settings.chosen_gui_sound_setting.get() else None)
sort_length_specific_lengths_radiobutton = Radiobutton(sort_length_buttons_labelframe, text="Multiple Lengths",
                                                       font=verdana_25,
                                                       variable=Composition.sort_by_length,
                                                       value="Multiple", indicatoron=0,
                                                       command=lambda: Sounds.play_gui_sound(
                                                           Sounds.RADIOBUTTON_SOUND_PATH)
                                                       if Settings.chosen_gui_sound_setting.get() else None)

sort_length_choose_any_frame = Frame(sort_by_length_frame, relief=RIDGE, borderwidth=2)

sort_length_choose_any_label = Label(sort_length_choose_any_frame, text="Compositions will not be sorted by length.",
                                     font=verdana_40)

sort_length_choose_length_frame = Frame(sort_by_length_frame, relief=RIDGE, borderwidth=2)

sort_length_choose_length_label = Label(sort_length_choose_length_frame, text="Select Specific Length:",
                                        font=verdana_25)
sort_length_short_radiobutton = Radiobutton(sort_length_choose_length_frame, text="Short", font=verdana_25,
                                            variable=Composition.specific_length, indicatoron=0, value="Short",
                                            command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                            if Settings.chosen_gui_sound_setting.get() else None)
sort_length_medium_radiobutton = Radiobutton(sort_length_choose_length_frame, text="Medium", font=verdana_25,
                                             variable=Composition.specific_length, indicatoron=0, value="Medium",
                                             command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None)
sort_length_long_radiobutton = Radiobutton(sort_length_choose_length_frame, text="Long", font=verdana_25,
                                           variable=Composition.specific_length, indicatoron=0, value="Long",
                                           command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                           if Settings.chosen_gui_sound_setting.get() else None)

sort_length_choose_lengths_frame = Frame(sort_by_length_frame, relief=RIDGE, borderwidth=2)

sort_length_choose_lengths_label = Label(sort_length_choose_lengths_frame, text="Select Multiple Lengths:",
                                         font=verdana_25)
sort_length_short_checkbutton = Checkbutton(sort_length_choose_lengths_frame, text="Short", font=verdana_25,
                                            variable=Composition.short_length, indicatoron=0,
                                            command=lambda: Sounds.play_gui_sound(Sounds.CHECKBUTTON_SOUND_PATH)
                                            if Settings.chosen_gui_sound_setting.get() else None)
sort_length_medium_checkbutton = Checkbutton(sort_length_choose_lengths_frame, text="Medium", font=verdana_25,
                                             variable=Composition.medium_length, indicatoron=0,
                                             command=lambda: Sounds.play_gui_sound(Sounds.CHECKBUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None)
sort_length_long_checkbutton = Checkbutton(sort_length_choose_lengths_frame, text="Long", font=verdana_25,
                                           variable=Composition.long_length, indicatoron=0,
                                           command=lambda: Sounds.play_gui_sound(Sounds.CHECKBUTTON_SOUND_PATH)
                                           if Settings.chosen_gui_sound_setting.get() else None)

sort_length_tip_labelframe = LabelFrame(sort_by_length_frame, text="Useful Information:", labelanchor=N,
                                        font=verdana_20, relief=RIDGE, borderwidth=2)
sort_length_tip_message = Message(sort_length_tip_labelframe, text="The Any Length option will not sort "
                                                                   "by length; while this option is set the GUI "
                                                                   "elements and widgets for sorting by length "
                                                                   "will be hidden. The Specific Length option will "
                                                                   "allow you to sort by 1 length parameter. "
                                                                   "The Multiple Lengths option enables sorting "
                                                                   "by multiple length parameters.\n"
                                                                   "These are the time intervals by which composition "
                                                                   "length is classified:\n"
                                                                   "Short - under 1 minute\t"
                                                                   "Medium - between 1 and 5 minutes\t"
                                                                   "Long - over 5 minutes",
                                  font=verdana_15, aspect=1300, justify=CENTER)

# Invalid selection label
sort_length_invalid_selection_label = Label(sort_by_length_frame, text="Invalid selection! Select at least 1 "
                                                                       "length option!",
                                            font=verdana_25, fg=Settings.chosen_invalid_text_color.get())

"""Sort by Date elements"""

sort_date_buttons_labelframe = LabelFrame(sort_by_date_frame, text="Sorting Criteria:", labelanchor=N, font=verdana_20,
                                          relief=RIDGE, borderwidth=2)

sort_date_any_date_radiobutton = Radiobutton(sort_date_buttons_labelframe, text="Any Date",
                                             font=verdana_25, variable=Composition.sort_by_date,
                                             value="Any", indicatoron=0,
                                             command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None)
sort_date_specific_date_radiobutton = Radiobutton(sort_date_buttons_labelframe, text="Specific Date",
                                                  font=verdana_25, variable=Composition.sort_by_date,
                                                  value="Specific", indicatoron=0,
                                                  command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                                  if Settings.chosen_gui_sound_setting.get() else None)
sort_date_date_interval_radiobutton = Radiobutton(sort_date_buttons_labelframe, text="Date Interval",
                                                  font=verdana_25, variable=Composition.sort_by_date,
                                                  value="Interval", indicatoron=0,
                                                  command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                                  if Settings.chosen_gui_sound_setting.get() else None)

sort_date_specific_labelframe = LabelFrame(sort_by_date_frame, text="Select Specific Date:", labelanchor=N,
                                           font=verdana_25, relief=RIDGE, borderwidth=2)

sort_date_specific_date_combobox_frame = Frame(sort_date_specific_labelframe)

sort_date_specific_date_day_combobox = Combobox(sort_date_specific_date_combobox_frame,
                                                textvariable=Composition.sort_date_selected_day,
                                                justify=CENTER, font=verdana_25)
sort_date_specific_date_day_combobox.bind("<<ComboboxSelected>>", lambda *args: Sounds.play_gui_sound(
    Sounds.CHECKBUTTON_SOUND_PATH) if Settings.chosen_gui_sound_setting.get() else None)
sort_date_specific_date_day_combobox["values"] = Misc.DAYS_TUPLE

sort_date_specific_date_month_combobox = Combobox(sort_date_specific_date_combobox_frame,
                                                  textvariable=Composition.sort_date_selected_month,
                                                  justify=CENTER, font=verdana_25)
sort_date_specific_date_month_combobox.bind("<<ComboboxSelected>>", lambda *args: Sounds.play_gui_sound(
    Sounds.CHECKBUTTON_SOUND_PATH) if Settings.chosen_gui_sound_setting.get() else None)
sort_date_specific_date_month_combobox["values"] = Misc.MONTHS_NAMES

sort_date_specific_date_year_combobox = Combobox(sort_date_specific_date_combobox_frame,
                                                 textvariable=Composition.sort_date_selected_year,
                                                 justify=CENTER, font=verdana_25)
sort_date_specific_date_year_combobox.bind("<<ComboboxSelected>>", lambda *args: Sounds.play_gui_sound(
    Sounds.CHECKBUTTON_SOUND_PATH) if Settings.chosen_gui_sound_setting.get() else None)
sort_date_specific_date_year_combobox["values"] = [year for year in range(1, datetime.date.today().year + 1)]

sort_date_interval_labelframe = LabelFrame(sort_by_date_frame, text="Select Date Interval:",  labelanchor=N,
                                           font=verdana_25, relief=RIDGE, borderwidth=2)

sort_date_interval_content_frame = Frame(sort_date_interval_labelframe)

sort_date_date_interval_from_label = Label(sort_date_interval_content_frame, text="From", font=verdana_25)
sort_date_date_interval_to_label = Label(sort_date_interval_content_frame, text="To", font=verdana_25)

sort_date_from_date_combobox_frame = Frame(sort_date_interval_content_frame)

sort_date_from_date_day_combobox = Combobox(sort_date_from_date_combobox_frame,
                                            textvariable=Composition.sort_date_selected_day_from,
                                            justify=CENTER, font=verdana_25)
sort_date_from_date_day_combobox.bind("<<ComboboxSelected>>", lambda *args: Sounds.play_gui_sound(
    Sounds.CHECKBUTTON_SOUND_PATH) if Settings.chosen_gui_sound_setting.get() else None)
sort_date_from_date_day_combobox["values"] = Misc.DAYS_TUPLE

sort_date_from_date_month_combobox = Combobox(sort_date_from_date_combobox_frame,
                                              textvariable=Composition.sort_date_selected_month_from,
                                              justify=CENTER, font=verdana_25)
sort_date_from_date_month_combobox.bind("<<ComboboxSelected>>", lambda *args: Sounds.play_gui_sound(
    Sounds.CHECKBUTTON_SOUND_PATH) if Settings.chosen_gui_sound_setting.get() else None)
sort_date_from_date_month_combobox["values"] = Misc.MONTHS_NAMES

sort_date_from_date_year_combobox = Combobox(sort_date_from_date_combobox_frame,
                                             textvariable=Composition.sort_date_selected_year_from,
                                             justify=CENTER, font=verdana_25)
sort_date_from_date_year_combobox.bind("<<ComboboxSelected>>", lambda *args: Sounds.play_gui_sound(
    Sounds.CHECKBUTTON_SOUND_PATH) if Settings.chosen_gui_sound_setting.get() else None)
sort_date_from_date_year_combobox["values"] = [year for year in range(1, datetime.date.today().year + 1)]

sort_date_to_date_combobox_frame = Frame(sort_date_interval_content_frame)

sort_date_to_date_day_combobox = Combobox(sort_date_to_date_combobox_frame,
                                          textvariable=Composition.sort_date_selected_day_to,
                                          justify=CENTER, font=verdana_25)
sort_date_to_date_day_combobox.bind("<<ComboboxSelected>>", lambda *args: Sounds.play_gui_sound(
    Sounds.CHECKBUTTON_SOUND_PATH) if Settings.chosen_gui_sound_setting.get() else None)
sort_date_to_date_day_combobox["values"] = Misc.DAYS_TUPLE

sort_date_to_date_month_combobox = Combobox(sort_date_to_date_combobox_frame,
                                            textvariable=Composition.sort_date_selected_month_to,
                                            justify=CENTER, font=verdana_25)
sort_date_to_date_month_combobox.bind("<<ComboboxSelected>>", lambda *args: Sounds.play_gui_sound(
    Sounds.CHECKBUTTON_SOUND_PATH) if Settings.chosen_gui_sound_setting.get() else None)
sort_date_to_date_month_combobox["values"] = Misc.MONTHS_NAMES

sort_date_to_date_year_combobox = Combobox(sort_date_to_date_combobox_frame,
                                           textvariable=Composition.sort_date_selected_year_to,
                                           justify=CENTER, font=verdana_25)
sort_date_to_date_year_combobox.bind("<<ComboboxSelected>>", lambda *args: Sounds.play_gui_sound(
    Sounds.CHECKBUTTON_SOUND_PATH) if Settings.chosen_gui_sound_setting.get() else None)
sort_date_to_date_year_combobox["values"] = [year for year in range(1, datetime.date.today().year + 1)]

# Any date label frame and label
sort_date_any_date_labelframe = LabelFrame(sort_by_date_frame, text="Any Date Selected:",
                                           labelanchor=N, font=verdana_25, relief=RIDGE, borderwidth=2)
sort_date_choose_any_date_label = Label(sort_date_any_date_labelframe, text="Compositions will not be sorted by date.",
                                        font=verdana_25)

# Specific date inclusive / exclusive
sort_date_specific_inclusive_exclusive_labelframe = LabelFrame(sort_by_date_frame, text="Specific Date Inclusivity:",
                                                               labelanchor=N, font=verdana_25, relief=RIDGE,
                                                               borderwidth=2)

sort_date_specific_inclusive_radiobutton = Radiobutton(sort_date_specific_inclusive_exclusive_labelframe,
                                                       text="Inclusive", font=verdana_25,
                                                       variable=Composition.date_specific_inclusive_exclusive,
                                                       value="Inclusive", indicatoron=0,
                                                       command=lambda: Sounds.play_gui_sound(
                                                           Sounds.RADIOBUTTON_SOUND_PATH)
                                                       if Settings.chosen_gui_sound_setting.get() else None)
sort_date_specific_exclusive_radiobutton = Radiobutton(sort_date_specific_inclusive_exclusive_labelframe,
                                                       text="Exclusive", font=verdana_25,
                                                       variable=Composition.date_specific_inclusive_exclusive,
                                                       value="Exclusive", indicatoron=0,
                                                       command=lambda: Sounds.play_gui_sound(
                                                           Sounds.RADIOBUTTON_SOUND_PATH)
                                                       if Settings.chosen_gui_sound_setting.get() else None)

# Date interval inclusive / exclusive
sort_date_interval_inclusive_exclusive_labelframe = LabelFrame(sort_by_date_frame, text="Date Interval Inclusivity:",
                                                               labelanchor=N, font=verdana_25, relief=RIDGE,
                                                               borderwidth=2)

sort_date_interval_inclusive_radiobutton = Radiobutton(sort_date_interval_inclusive_exclusive_labelframe,
                                                       text="Inclusive", font=verdana_25,
                                                       variable=Composition.date_interval_inclusive_exclusive,
                                                       value="Inclusive", indicatoron=0,
                                                       command=lambda: Sounds.play_gui_sound(
                                                           Sounds.RADIOBUTTON_SOUND_PATH)
                                                       if Settings.chosen_gui_sound_setting.get() else None)
sort_date_interval_exclusive_radiobutton = Radiobutton(sort_date_interval_inclusive_exclusive_labelframe,
                                                       text="Exclusive", font=verdana_25,
                                                       variable=Composition.date_interval_inclusive_exclusive,
                                                       value="Exclusive", indicatoron=0,
                                                       command=lambda: Sounds.play_gui_sound(
                                                           Sounds.RADIOBUTTON_SOUND_PATH)
                                                       if Settings.chosen_gui_sound_setting.get() else None)

# Invalid date labels
# Specific
sort_date_invalid_specific_label = Label(sort_by_date_frame,
                                         text="Invalid specific date! Select a valid date!",
                                         font=verdana_25, fg=Settings.chosen_invalid_text_color.get())
# Interval
sort_date_invalid_interval_label = Label(sort_by_date_frame,
                                         text="Invalid date interval! The \"From\" date exceeds the \"to\" date! "
                                              "Select a valid date interval!",
                                         font=verdana_25, fg=Settings.chosen_invalid_text_color.get())
sort_date_invalid_from_date_label = Label(sort_by_date_frame,
                                          text="Invalid date interval! The \"From\" date is invalid! "
                                               "Select a valid date!",
                                          font=verdana_25, fg=Settings.chosen_invalid_text_color.get())
sort_date_invalid_to_date_label = Label(sort_by_date_frame,
                                        text="Invalid date interval! The \"To\" date is invalid! "
                                             "Select a valid date!",
                                        font=verdana_25, fg=Settings.chosen_invalid_text_color.get())
sort_date_invalid_from_and_to_date_label = Label(sort_by_date_frame,
                                                 text="Invalid date interval! The \"From\" and the \"To\" dates "
                                                      "are invalid! Select valid dates!",
                                                 font=verdana_25, fg=Settings.chosen_invalid_text_color.get())

"""Sort by Composition Rating elements"""

sort_rating_buttons_labelframe = LabelFrame(sort_by_rating_frame, text="Sorting Criteria:", labelanchor=N,
                                            font=verdana_20, relief=RIDGE, borderwidth=2)

sort_rating_any_rating_radiobutton = Radiobutton(sort_rating_buttons_labelframe, text="Any Rating",
                                                 font=verdana_25, variable=Composition.sort_by_rating,
                                                 value="Any", indicatoron=0,
                                                 command=lambda: Sounds.play_gui_sound(
                                                     Sounds.RADIOBUTTON_SOUND_PATH)
                                                 if Settings.chosen_gui_sound_setting.get() else None)
sort_rating_specific_rating_radiobutton = Radiobutton(sort_rating_buttons_labelframe, text="Specific Rating",
                                                      font=verdana_25, variable=Composition.sort_by_rating,
                                                      value="Specific", indicatoron=0,
                                                      command=lambda: Sounds.play_gui_sound(
                                                          Sounds.RADIOBUTTON_SOUND_PATH)
                                                      if Settings.chosen_gui_sound_setting.get() else None)
sort_rating_specific_ratings_radiobutton = Radiobutton(sort_rating_buttons_labelframe, text="Multiple Ratings",
                                                       font=verdana_25, variable=Composition.sort_by_rating,
                                                       value="Multiple", indicatoron=0,
                                                       command=lambda: Sounds.play_gui_sound(
                                                           Sounds.RADIOBUTTON_SOUND_PATH)
                                                       if Settings.chosen_gui_sound_setting.get() else None)

sort_rating_choose_any_frame = Frame(sort_by_rating_frame, relief=RIDGE, borderwidth=2)

sort_rating_choose_any_label = Label(sort_rating_choose_any_frame, text="Compositions will not be sorted by rating.",
                                     font=verdana_40)

sort_rating_choose_rating_labelframe = LabelFrame(sort_by_rating_frame, text="Select Specific Rating:", labelanchor=N,
                                                  font=verdana_25, relief=RIDGE, borderwidth=2)

sort_rating_no_rating_radiobutton = Radiobutton(sort_rating_choose_rating_labelframe, text=Misc.NO_RATING,
                                                font=verdana_25, variable=Composition.specific_rating,
                                                indicatoron=0, value=Misc.NO_RATING,
                                                command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                                if Settings.chosen_gui_sound_setting.get() else None)
sort_rating_1_star_radiobutton = Radiobutton(sort_rating_choose_rating_labelframe, text=Misc.STAR_1, font=verdana_25,
                                             variable=Composition.specific_rating, indicatoron=0, value=1,
                                             command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None)
sort_rating_2_star_radiobutton = Radiobutton(sort_rating_choose_rating_labelframe, text=Misc.STAR_2, font=verdana_25,
                                             variable=Composition.specific_rating, indicatoron=0, value=2,
                                             command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None)
sort_rating_3_star_radiobutton = Radiobutton(sort_rating_choose_rating_labelframe, text=Misc.STAR_3, font=verdana_25,
                                             variable=Composition.specific_rating, indicatoron=0, value=3,
                                             command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None)
sort_rating_4_star_radiobutton = Radiobutton(sort_rating_choose_rating_labelframe, text=Misc.STAR_4, font=verdana_25,
                                             variable=Composition.specific_rating, indicatoron=0, value=4,
                                             command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None)
sort_rating_5_star_radiobutton = Radiobutton(sort_rating_choose_rating_labelframe, text=Misc.STAR_5, font=verdana_25,
                                             variable=Composition.specific_rating, indicatoron=0, value=5,
                                             command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None)

sort_rating_choose_ratings_labelframe = LabelFrame(sort_by_rating_frame, text="Select Multiple Ratings:",
                                                   labelanchor=N, font=verdana_25, relief=RIDGE, borderwidth=2)

sort_rating_no_rating_checkbutton = Checkbutton(sort_rating_choose_ratings_labelframe, text=Misc.NO_RATING,
                                                font=verdana_25, variable=Composition.no_rating, indicatoron=0,
                                                command=lambda: Sounds.play_gui_sound(Sounds.CHECKBUTTON_SOUND_PATH)
                                                if Settings.chosen_gui_sound_setting.get() else None)
sort_rating_1_star_checkbutton = Checkbutton(sort_rating_choose_ratings_labelframe, text=Misc.STAR_1,
                                             font=verdana_25, variable=Composition.star_1_rating, indicatoron=0,
                                             command=lambda: Sounds.play_gui_sound(Sounds.CHECKBUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None)
sort_rating_2_star_checkbutton = Checkbutton(sort_rating_choose_ratings_labelframe, text=Misc.STAR_2,
                                             font=verdana_25, variable=Composition.star_2_rating, indicatoron=0,
                                             command=lambda: Sounds.play_gui_sound(Sounds.CHECKBUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None)
sort_rating_3_star_checkbutton = Checkbutton(sort_rating_choose_ratings_labelframe, text=Misc.STAR_3,
                                             font=verdana_25, variable=Composition.star_3_rating, indicatoron=0,
                                             command=lambda: Sounds.play_gui_sound(Sounds.CHECKBUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None)
sort_rating_4_star_checkbutton = Checkbutton(sort_rating_choose_ratings_labelframe, text=Misc.STAR_4,
                                             font=verdana_25, variable=Composition.star_4_rating, indicatoron=0,
                                             command=lambda: Sounds.play_gui_sound(Sounds.CHECKBUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None)
sort_rating_5_star_checkbutton = Checkbutton(sort_rating_choose_ratings_labelframe, text=Misc.STAR_5,
                                             font=verdana_25, variable=Composition.star_5_rating, indicatoron=0,
                                             command=lambda: Sounds.play_gui_sound(Sounds.CHECKBUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None)

sort_rating_tip_labelframe = LabelFrame(sort_by_rating_frame, text="Useful Information:", labelanchor=N,
                                        font=verdana_20, relief=RIDGE, borderwidth=2)
sort_rating_tip_message = Message(sort_rating_tip_labelframe, text="The sorted list will include compositions whose "
                                                                   "rounded rating matches the given rating "
                                                                   "selections.\nThe \"None\" option will yield "
                                                                   "compositions that are not rated at the "
                                                                   "time of list creation.",
                                  font=verdana_15, aspect=1200, justify=CENTER)

# Invalid selection label
sort_rating_invalid_selection_label = Label(sort_by_rating_frame, text="Invalid selection! Select at least 1 "
                                                                       "rating option!",
                                            font=verdana_25, fg=Settings.chosen_invalid_text_color.get())

"""Current Sorting Parameters"""
current_sorting_parameters_label = Label(playback_composition_labelframe, text="Current Sorting Parameters:",
                                         font=verdana_25)
sorting_separator_1 = Separator(playback_composition_labelframe)
sorting_separator_2 = Separator(playback_composition_labelframe)

current_sorting_by_container_frame = Frame(playback_composition_labelframe, relief=GROOVE, borderwidth=2)

current_sorting_by_user_frame = Frame(current_sorting_by_container_frame, relief=GROOVE, borderwidth=2)
current_sorting_by_length_frame = Frame(current_sorting_by_container_frame, relief=GROOVE, borderwidth=2)
current_sorting_by_date_frame = Frame(current_sorting_by_container_frame, relief=GROOVE, borderwidth=2)
current_sorting_by_rating_frame = Frame(current_sorting_by_container_frame, relief=GROOVE, borderwidth=2)

current_sorting_by_user_label = Label(current_sorting_by_user_frame, text="User:", font=verdana_25, relief=SUNKEN)
current_sorting_by_length_label = Label(current_sorting_by_length_frame, text="Length:", font=verdana_25, relief=SUNKEN)
current_sorting_by_date_label = Label(current_sorting_by_date_frame, text="Date:", font=verdana_25, relief=SUNKEN)
current_sorting_by_rating_label = Label(current_sorting_by_rating_frame, text="Rating:", font=verdana_25, relief=SUNKEN)

current_sorting_by_user_data_label = Label(current_sorting_by_user_frame, text="DATA", font=verdana_25, relief=SUNKEN)
current_sorting_by_length_data_label = Label(current_sorting_by_length_frame, text="DATA",
                                             font=verdana_25, relief=SUNKEN)
current_sorting_by_date_data_label = Label(current_sorting_by_date_frame, text="DATA", font=verdana_25, relief=SUNKEN)
current_sorting_by_rating_data_label = Label(current_sorting_by_rating_frame, text="DATA",
                                             font=verdana_25, relief=SUNKEN)

# Preselect frame & content
preselect_composition_frame = Frame(root, relief=GROOVE, borderwidth=2)
preselect_composition_label = Label(preselect_composition_frame, text="Preselect Composition:", font=verdana_20)
preselect_first_radiobutton = Radiobutton(preselect_composition_frame, text="First", font=verdana_20, indicatoron=0,
                                          variable=Composition.preselect_option, value="First",
                                          command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                          if Settings.chosen_gui_sound_setting.get() else None)
preselect_last_radiobutton = Radiobutton(preselect_composition_frame, text="Last", font=verdana_20, indicatoron=0,
                                         variable=Composition.preselect_option, value="Last",
                                         command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                         if Settings.chosen_gui_sound_setting.get() else None)
preselect_random_radiobutton = Radiobutton(preselect_composition_frame, text="Random", font=verdana_20, indicatoron=0,
                                           variable=Composition.preselect_option, value="Random",
                                           command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                           if Settings.chosen_gui_sound_setting.get() else None)

# Proceed Button
proceed_to_sorted_button = Button(root, text="Proceed", font=verdana_25,
                                  command=lambda: [Composition.sort_by_all_parameters(
                                                   combobox_values=sort_user_choose_user_combobox["values"],
                                                   listbox_values=sort_user_listbox.get(first=0, last=END)),
                                                   populate_sorted_listbox(),
                                                   display_playback_composition_sorted(),
                                                   Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                   if Settings.chosen_gui_sound_setting.get() else None
                                                   ])


"""Sorted Compositions"""


sorted_compositions_labelframe = LabelFrame(root, text="Compositions Sorted by the Given Options:", labelanchor=N,
                                            font=verdana_25)

sorted_compositions_content_frame = Frame(sorted_compositions_labelframe, relief=RIDGE, borderwidth=2)

sorted_compositions_separator = Separator(sorted_compositions_content_frame, orient=VERTICAL)

# Left side of separator
sorted_compositions_listbox = Listbox(sorted_compositions_content_frame, borderwidth=3, font=verdana_20,
                                      selectmode=SINGLE, activestyle="none", selectborderwidth=2)
sorted_compositions_listbox_scroll_bar = Scrollbar(sorted_compositions_content_frame)
# Add scroll bar to list box
sorted_compositions_listbox.config(yscrollcommand=sorted_compositions_listbox_scroll_bar.set)
sorted_compositions_listbox_scroll_bar.config(command=sorted_compositions_listbox.yview)

sorted_compositions_listbox.bind("<<ListboxSelect>>",
                                 lambda *args: [[config_sorted_menu(composition=Composition.get_composition_from_name
                                                                    (composition_name=sorted_compositions_listbox.get
                                                                     (sorted_compositions_listbox.curselection()))),
                                                 Composition.composition_to_play_name.set(
                                                     sorted_compositions_listbox.get(
                                                         sorted_compositions_listbox.curselection())),
                                                 Sounds.play_gui_sound(sound_file_path=Sounds.SELECT_SOUND_PATH)
                                                 if Settings.chosen_gui_sound_setting.get()
                                                 and sorted_compositions_listbox.curselection() else None
                                                 ]
                                                if User.is_logged_in and Composition.is_in_sorted_menu.get() else None
                                                ])

# Right side of separator
# Content frame
sorted_compositions_right_frame = Frame(sorted_compositions_content_frame, relief=RIDGE, borderwidth=2)
# No compositions matching sorting criteria label
sorted_no_match_label = Label(sorted_compositions_labelframe,
                              text="Whoops...\n\nNo current compositions match the given sorting criteria.\n"
                                   "Change the sorting criteria and try again.", font=verdana_35)
# Content frame content
sorted_compositions_about_label = Label(sorted_compositions_right_frame, text="About Selected Composition:",
                                        font=verdana_25)
sorted_compositions_notebook = Notebook(sorted_compositions_right_frame, style="Sorted.TNotebook")

sorted_compositions_composer_and_description_frame = Frame(sorted_compositions_notebook)
sorted_compositions_notes_and_delays_frame = Frame(sorted_compositions_notebook)
sorted_compositions_ratings_frame = Frame(sorted_compositions_notebook)
sorted_compositions_misc_frame = Frame(sorted_compositions_notebook)

sorted_compositions_notebook.add(sorted_compositions_composer_and_description_frame, text="Composer & Description")
sorted_compositions_notebook.add(sorted_compositions_notes_and_delays_frame, text="Notes & Delays")
sorted_compositions_notebook.add(sorted_compositions_ratings_frame, text="Ratings")
sorted_compositions_notebook.add(sorted_compositions_misc_frame, text="Miscellaneous")

# Composer & Description frame
sorted_composer_labelframe = LabelFrame(sorted_compositions_composer_and_description_frame, text="Composer:",
                                        labelanchor=N, font=verdana_20)
sorted_composer_scrolled_text = ScrolledText(sorted_composer_labelframe, font=verdana_25, borderwidth=3,
                                             state=DISABLED, spacing1=2)
sorted_description_labelframe = LabelFrame(sorted_compositions_composer_and_description_frame, text="Description:",
                                           labelanchor=N, font=verdana_20)
sorted_description_scrolled_text = ScrolledText(sorted_description_labelframe, font=tempus_sans_itc_20_bold,
                                                borderwidth=3, wrap=WORD, state=DISABLED, spacing1=5)

# Notes & Delays frame
sorted_notes_and_delays_labelframe = LabelFrame(sorted_compositions_notes_and_delays_frame, text="Notes & Delays:",
                                                labelanchor=N, font=verdana_20)
sorted_notes_and_delays_scrolled_text = ScrolledText(sorted_notes_and_delays_labelframe, borderwidth=3, wrap=WORD,
                                                     state=DISABLED, spacing1=1)
sorted_length_labelframe = LabelFrame(sorted_compositions_notes_and_delays_frame, text="Length:", labelanchor=N,
                                      font=verdana_20)
sorted_length_data_scrolled_text = ScrolledText(sorted_length_labelframe, borderwidth=3, wrap=WORD, state=DISABLED,
                                                spacing1=3)

# Ratings frame
sorted_ratings_labelframe = LabelFrame(sorted_compositions_ratings_frame, text="Given Ratings:", labelanchor=N,
                                       font=verdana_20)
sorted_5_star_rating_label = Label(sorted_ratings_labelframe, text=Misc.STAR_5 + " : ", font=verdana_20, anchor=E)
sorted_4_star_rating_label = Label(sorted_ratings_labelframe, text=Misc.STAR_4[::-1] + " : ", font=verdana_20, anchor=E)
sorted_3_star_rating_label = Label(sorted_ratings_labelframe, text=Misc.STAR_3[::-1] + " : ", font=verdana_20, anchor=E)
sorted_2_star_rating_label = Label(sorted_ratings_labelframe, text=Misc.STAR_2[::-1] + " : ", font=verdana_20, anchor=E)
sorted_1_star_rating_label = Label(sorted_ratings_labelframe, text=Misc.STAR_1[::-1] + " : ", font=verdana_20, anchor=E)

sorted_5_star_bar = Progressbar(sorted_ratings_labelframe, orient=HORIZONTAL, mode="determinate",
                                variable=Composition.sorted_5_star_var)
sorted_4_star_bar = Progressbar(sorted_ratings_labelframe, orient=HORIZONTAL, mode="determinate",
                                variable=Composition.sorted_4_star_var)
sorted_3_star_bar = Progressbar(sorted_ratings_labelframe, orient=HORIZONTAL, mode="determinate",
                                variable=Composition.sorted_3_star_var)
sorted_2_star_bar = Progressbar(sorted_ratings_labelframe, orient=HORIZONTAL, mode="determinate",
                                variable=Composition.sorted_2_star_var)
sorted_1_star_bar = Progressbar(sorted_ratings_labelframe, orient=HORIZONTAL, mode="determinate",
                                variable=Composition.sorted_1_star_var)

sorted_5_star_data_label = Label(sorted_ratings_labelframe, text="DATA", font=verdana_25)
sorted_4_star_data_label = Label(sorted_ratings_labelframe, text="DATA", font=verdana_25)
sorted_3_star_data_label = Label(sorted_ratings_labelframe, text="DATA", font=verdana_25)
sorted_2_star_data_label = Label(sorted_ratings_labelframe, text="DATA", font=verdana_25)
sorted_1_star_data_label = Label(sorted_ratings_labelframe, text="DATA", font=verdana_25)

sorted_overall_rating_labelframe = LabelFrame(sorted_compositions_ratings_frame, text="Overall Rating:", labelanchor=N,
                                              font=verdana_20)
sorted_overall_rating_data_label = Label(sorted_overall_rating_labelframe, text="DATA", font=verdana_35)

sorted_your_rating_labelframe = LabelFrame(sorted_compositions_ratings_frame, text="Your Rating:", labelanchor=N,
                                           font=verdana_20)
sorted_your_rating_data_label = Label(sorted_your_rating_labelframe, text="DATA", font=verdana_35)

# Miscellaneous frame
sorted_times_played_labelframe = LabelFrame(sorted_compositions_misc_frame, text="Composition Fully Auditioned:",
                                            labelanchor=N, font=verdana_25)
sorted_times_played_data_label = Label(sorted_times_played_labelframe, text="DATA Time(s)", font=verdana_25)

sorted_date_of_creation_labelframe = LabelFrame(sorted_compositions_misc_frame, text="Date of Creation:", labelanchor=N,
                                                font=verdana_25)
sorted_date_of_creation_data_label = Label(sorted_date_of_creation_labelframe, text="FORMATTED DATE", font=verdana_20)

sorted_total_ratings_labelframe = LabelFrame(sorted_compositions_misc_frame, text="Other Rating Data:",
                                             labelanchor=N, font=verdana_25)

sorted_total_ratings_label = Label(sorted_total_ratings_labelframe, text="Number of Ratings Received",
                                   font=verdana_17)
sorted_total_ratings_scrolled_text = ScrolledText(sorted_total_ratings_labelframe, borderwidth=3, wrap=WORD,
                                                  font=fixed_25, state=DISABLED, spacing1=1)

sorted_current_maximum_rating_label = Label(sorted_total_ratings_labelframe, text="Total Rating Points Received\n"
                                            "(Current / Maximum)", font=verdana_17)
sorted_current_maximum_rating_scrolled_text = ScrolledText(sorted_total_ratings_labelframe, borderwidth=3, wrap=WORD,
                                                           font=fixed_25, state=DISABLED, spacing1=1)

sorted_ratings_colon_label_1 = Label(sorted_total_ratings_labelframe, text=":", font=verdana_17)
sorted_ratings_colon_label_2 = Label(sorted_total_ratings_labelframe, text=":", font=verdana_17)

# Numbers frame
sorted_compositions_numbers_frame = Frame(root, relief=RIDGE, borderwidth=2)

sorted_compositions_total_label = Label(sorted_compositions_numbers_frame, text="Number of eligible compositions:",
                                        font=verdana_25, relief=SUNKEN)
sorted_compositions_total_data_label = Label(sorted_compositions_numbers_frame, text="DATA", font=verdana_25,
                                             relief=SUNKEN)

sorted_compositions_matching_label = Label(sorted_compositions_numbers_frame, text="Matching your sorting criteria:",
                                           font=verdana_25, relief=SUNKEN)
sorted_compositions_matching_data_label = Label(sorted_compositions_numbers_frame, text="DATA", font=verdana_25,
                                                relief=SUNKEN)

proceed_to_play_button = Button(root, text="Proceed", font=verdana_25,
                                command=lambda: [Composition.composition_to_play.update(
                                    Composition.get_composition_from_name(
                                        composition_name=Composition.composition_to_play_name.get())),
                                    config_composition_table_and_composer_labels(),
                                    display_playback_composition(),
                                    Composition.is_in_sorted_menu.set(False),
                                    Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                    if Settings.chosen_gui_sound_setting.get() else None
                                ])


"""Playback Composition Playback Menu Elements"""
# Most widgets this menu uses while playing compositions are found in the Composition module

composition_to_play_name_label = Label(root, text="DATA", font=book_antiqua_49_italic)
composition_to_play_composer_name_label = Label(root, text="By DATA", font=book_antiqua_35)

rate_composition_labelframe = LabelFrame(root, text="Rate Composition:", font=verdana_30,
                                         labelanchor=N, relief=GROOVE, borderwidth=3)

rate_composition_content_frame = Frame(rate_composition_labelframe)

rate_composition_given_label = Label(rate_composition_content_frame, text="Your Given Rating:", font=verdana_30)
rate_composition_option_menu = OptionMenu(rate_composition_content_frame, Composition.given_rating,
                                          *Misc.POSSIBLE_RATINGS)
rate_composition_option_menu.config(font=verdana_25, indicatoron=0, highlightthickness=0)
rate_composition_option_menu["menu"].config(font=verdana_25)
rate_composition_current_label = Label(rate_composition_content_frame, text="X / 5", font=verdana_30)

# Top part
playback_separator_1 = Separator(root)
playback_separator_2 = Separator(root, orient=VERTICAL)
playback_separator_3 = Separator(root, orient=VERTICAL)
playback_separator_4 = Separator(root)
playback_separator_5 = Separator(root)
# Bottom part
playback_separator_6 = Separator(root)
playback_separator_7 = Separator(root)
playback_separator_8 = Separator(root, orient=VERTICAL)
playback_separator_9 = Separator(root, orient=VERTICAL)
playback_separator_10 = Separator(root)


"""Settings Menu Elements"""

# Bind Key Press events to Remember Settings variable
# Lowercase
root.bind("p", lambda event: Settings.change_setting_with_event(event=event))
root.bind("u", lambda event: Settings.change_setting_with_event(event=event))
root.bind("d", lambda event: Settings.change_setting_with_event(event=event))
# Uppercase
root.bind("P", lambda event: Settings.change_setting_with_event(event=event))
root.bind("U", lambda event: Settings.change_setting_with_event(event=event))
root.bind("D", lambda event: Settings.change_setting_with_event(event=event))


settings_menu_label = Label(text="Settings", font=courier_100)

settings_menu_content_labelframe = LabelFrame(root, text="Current Settings:", font=verdana_25, labelanchor=N,
                                              relief=GROOVE, borderwidth=2)

background_color_label = Label(settings_menu_content_labelframe, text="Background Color:", font=verdana_25, anchor=E)
background_color_menu = OptionMenu(settings_menu_content_labelframe, Settings.chosen_background_color, *Colors.COLORS,
                                   command=lambda *args: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                   if Settings.chosen_gui_sound_setting.get() else None)
background_color_menu.config(font=verdana_25, indicatoron=0, highlightthickness=0)
background_color_menu["menu"].config(font=verdana_25)
default_background_color_button = Button(settings_menu_content_labelframe, text="Default", font=verdana_25,
                                         state=DISABLED,
                                         command=lambda: [Settings.chosen_background_color.set(
                                             Settings.default_background_color),
                                             Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                             if Settings.chosen_gui_sound_setting.get() else None
                                         ])
custom_background_color_button = Button(settings_menu_content_labelframe, text="Custom", font=verdana_25,
                                        command=lambda: [Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                         if Settings.chosen_gui_sound_setting.get() else None,
                                                         Settings.get_custom_color(
                                                             setting_value=Settings.chosen_background_color,
                                                             target="Background Color")
                                                         ])


text_color_label = Label(settings_menu_content_labelframe, text="Text Color:", font=verdana_25, anchor=E)
text_color_menu = OptionMenu(settings_menu_content_labelframe, Settings.chosen_text_color, *Colors.COLORS,
                             command=lambda *args: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                             if Settings.chosen_gui_sound_setting.get() else None)
text_color_menu.config(font=verdana_25, indicatoron=0, highlightthickness=0)
text_color_menu["menu"].config(font=verdana_25)
default_text_color_button = Button(settings_menu_content_labelframe, text="Default", font=verdana_25, state=DISABLED,
                                   command=lambda: [Settings.chosen_text_color.set(Settings.default_text_color),
                                                    Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                    if Settings.chosen_gui_sound_setting.get() else None
                                                    ])
custom_text_color_button = Button(settings_menu_content_labelframe, text="Custom", font=verdana_25,
                                  command=lambda: [Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                   if Settings.chosen_gui_sound_setting.get() else None,
                                                   Settings.get_custom_color(
                                                       setting_value=Settings.chosen_text_color,
                                                       target="Text Color")
                                                   ])


buttons_color_label = Label(settings_menu_content_labelframe, text="Buttons' Color:", font=verdana_25, anchor=E)
buttons_color_menu = OptionMenu(settings_menu_content_labelframe, Settings.chosen_button_color, *Colors.COLORS,
                                command=lambda *args: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                if Settings.chosen_gui_sound_setting.get() else None)
buttons_color_menu.config(font=verdana_25, indicatoron=0, highlightthickness=0)
buttons_color_menu["menu"].config(font=verdana_25)
default_button_color_button = Button(settings_menu_content_labelframe, text="Default", font=verdana_25, state=DISABLED,
                                     command=lambda: [Settings.chosen_button_color.set(Settings.default_buttons_color),
                                                      Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                      if Settings.chosen_gui_sound_setting.get() else None
                                                      ])
custom_button_color_button = Button(settings_menu_content_labelframe, text="Custom", font=verdana_25,
                                    command=lambda: [Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                     if Settings.chosen_gui_sound_setting.get() else None,
                                                     Settings.get_custom_color(
                                                         setting_value=Settings.chosen_button_color,
                                                         target="Buttons' Color")
                                                     ])


buttons_text_color_label = Label(settings_menu_content_labelframe, text="Buttons' Text Color:",
                                 font=verdana_25, anchor=E)
buttons_text_color_menu = OptionMenu(settings_menu_content_labelframe, Settings.chosen_button_text_color,
                                     *Colors.COLORS,
                                     command=lambda *args: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                     if Settings.chosen_gui_sound_setting.get() else None)
buttons_text_color_menu.config(font=verdana_25, indicatoron=0, highlightthickness=0)
buttons_text_color_menu["menu"].config(font=verdana_25)
default_buttons_text_color_button = Button(settings_menu_content_labelframe, text="Default", font=verdana_25,
                                           state=DISABLED,
                                           command=lambda: [Settings.chosen_button_text_color.set(
                                               Settings.default_button_text_color),
                                                            Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                            if Settings.chosen_gui_sound_setting.get()
                                                            else None
                                                            ])
custom_buttons_text_color_button = Button(settings_menu_content_labelframe, text="Custom", font=verdana_25,
                                          command=lambda: [Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                           if Settings.chosen_gui_sound_setting.get()
                                                           else None,
                                                           Settings.get_custom_color(
                                                               setting_value=Settings.chosen_button_text_color,
                                                               target="Buttons' Text Color")
                                                           ])

invalid_text_color_label = Label(settings_menu_content_labelframe, text="Invalid Text Color:",
                                 font=verdana_25, anchor=E)
invalid_text_color_menu = OptionMenu(settings_menu_content_labelframe, Settings.chosen_invalid_text_color,
                                     *Colors.COLORS,
                                     command=lambda *args: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                     if Settings.chosen_gui_sound_setting.get() else None)
invalid_text_color_menu.config(font=verdana_25, indicatoron=0, highlightthickness=0)
invalid_text_color_menu["menu"].config(font=verdana_25)
default_invalid_text_color_button = Button(settings_menu_content_labelframe, text="Default", font=verdana_25,
                                           state=DISABLED,
                                           command=lambda: [Settings.chosen_invalid_text_color.set(
                                               Settings.default_invalid_text_color),
                                                            Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                            if Settings.chosen_gui_sound_setting.get()
                                                            else None
                                                            ])
custom_invalid_text_color_button = Button(settings_menu_content_labelframe, text="Custom", font=verdana_25,
                                          command=lambda: [Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                           if Settings.chosen_gui_sound_setting.get()
                                                           else None,
                                                           Settings.get_custom_color(
                                                               setting_value=Settings.chosen_invalid_text_color,
                                                               target="Invalid Text Color")
                                                           ])


gui_sound_label = Label(settings_menu_content_labelframe, text="GUI Sound:", font=verdana_25, anchor=E)
gui_sound_on_radiobutton = Radiobutton(settings_menu_content_labelframe, text="On", font=verdana_25,
                                       variable=Settings.chosen_gui_sound_setting,
                                       value=True, indicatoron=0,
                                       command=lambda: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                       if Settings.chosen_gui_sound_setting.get() else None)
gui_sound_off_radiobutton = Radiobutton(settings_menu_content_labelframe, text="Off", font=verdana_25,
                                        variable=Settings.chosen_gui_sound_setting,
                                        value=False, indicatoron=0)  # No need to have sound command; Won't execute

remember_settings_label = Label(settings_menu_content_labelframe, text="Remember Settings:",
                                font=verdana_25, anchor=E)
preset_settings_radiobutton = Radiobutton(settings_menu_content_labelframe, text="Preset",
                                          font=verdana_25, indicatoron=0,
                                          variable=Settings.remember_settings_setting, value="Preset",
                                          command=lambda: [Settings.set_settings_vars("Preset"),
                                                           Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                                           if Settings.chosen_gui_sound_setting.get()
                                                           else None
                                                           ])
user_settings_radiobutton = Radiobutton(settings_menu_content_labelframe, text="User",
                                        font=verdana_25, indicatoron=0,
                                        variable=Settings.remember_settings_setting, value="User",
                                        command=lambda: [Settings.set_settings_vars("User") if User.is_logged_in
                                                         else None,
                                                         Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                                         if Settings.chosen_gui_sound_setting.get()
                                                         else None
                                                         ])
default_settings_radiobutton = Radiobutton(settings_menu_content_labelframe, text="Default",
                                           font=verdana_25, indicatoron=0,
                                           variable=Settings.remember_settings_setting, value="Default",
                                           command=lambda: [Settings.set_settings_vars("Default"),
                                                            Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                                            if Settings.chosen_gui_sound_setting.get()
                                                            else None
                                                            ])

settings_info_labelframe = LabelFrame(settings_menu_content_labelframe, text="About Remember Settings:",
                                      labelanchor=N, font=verdana_25)
settings_info_scrolled_text = ScrolledText(settings_info_labelframe, font=verdana_15, spacing1=5, state=DISABLED,
                                           wrap=WORD)
settings_info_text_text: str = "     If User is selected and you quit the app with \"Remember Me\" ticked, this " \
                               "setting will remember your account's settings on startup.\n     Alternatively, " \
                               "if you do not have an account, use the Preset option, which will do the same.\n" \
                               "     Use the Default option to get fresh default settings on startup.\n     " \
                               "You can freely transition between any of these options at any time while " \
                               "using the app, and they will have their corresponding effect."
Misc.copy_var_value_to_disabled_text_widget(text_text=settings_info_text_text,
                                            text_widget=settings_info_scrolled_text)

settings_wrecked_label = Label(root, text="Press keys P, U or D to switch to Preset, User or Default settings.\n"
                                          "Use especially when messing up the colors so bad that you can't "
                                          "see the buttons anymore.",
                               font=verdana_20)


"""Stats Menu Elements"""


stats_menu_label = Label(text="Stats", font=courier_100)

stats_star_label = Label(text="*These options don't add up to the total amount of \"Main Menu Interactions\"",
                         font=verdana_15)

# Didn't have enough
stats_more_stats_button = Button(text="More Stats Here", font=verdana_25,
                                 command=lambda: [display_more_stats(),
                                                  Stats.main_menu_interactions_viewed_more_stats.set(
                                                      Stats.main_menu_interactions_viewed_more_stats.get() + 1),
                                                  Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                  if Settings.chosen_gui_sound_setting.get()
                                                  else None
                                                  ])


"""More Stats Element(s)"""


more_stats_menu_label = Label(text="More Stats", font=courier_100)


"""Login Menu Elements"""


login_menu_label = Label(text="Login", font=courier_100)

login_menu_labelframe = LabelFrame(text="Welcome back!", font=verdana_35, labelanchor=N)

login_menu_main_content_frame = Frame(login_menu_labelframe, relief=SUNKEN, borderwidth=3)

name_label = Label(login_menu_main_content_frame, text="Account Username :", font=verdana_25, anchor=E)
name_entry_field = Entry(login_menu_main_content_frame, textvariable=User.entered_login_username,
                         font=verdana_25, justify=CENTER, borderwidth=3)

password_label = Label(login_menu_main_content_frame, text="Account Password :", font=verdana_25, anchor=E)
password_entry_field = Entry(login_menu_main_content_frame, textvariable=User.entered_login_password,
                             font=verdana_25, justify=CENTER, show="•", borderwidth=3)

login_button = Button(login_menu_main_content_frame, text="Log In", font=verdana_25, borderwidth=3,
                      command=lambda: [User.login_user(User.entered_login_username.get(),
                                                       User.entered_login_password.get()),
                                       [logged_in_user_username_label.config
                                        (text=f"Logged In User: {User.logged_in_user['Credentials']['Username']}"),
                                        display_main_menu(),
                                        Composition.update_composer_list(),
                                        Stats.main_menu_interactions_logged_in.set(
                                            Stats.main_menu_interactions_logged_in.get() + 1)
                                        ]
                                       if User.is_logged_in
                                       else incorrect_account_data_label.place(  # Use dimensions from display_login
                                           relheight=.2, relwidth=.9, relx=.05, rely=.075 + .2 * 2 + .025 * 2),
                                       clear_login_menu_variables(),
                                       Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                       if Settings.chosen_gui_sound_setting.get() else None
                                       ])
show_password_checkbutton_login = Checkbutton(login_menu_main_content_frame, text="Show Password", font=verdana_25,
                                              indicatoron=0, borderwidth=3, variable=User.show_password_login,
                                              onvalue=True, offvalue=False,
                                              command=lambda: [show_hide_password_login(User.show_password_login.
                                                                                        get()),
                                                               Sounds.play_gui_sound(Sounds.CHECKBUTTON_SOUND_PATH)
                                                               if Settings.chosen_gui_sound_setting.get()
                                                               else None])

incorrect_account_data_label = Label(login_menu_main_content_frame,
                                     text="Incorrect Username or Password! Please try again!",
                                     font=verdana_25, fg=Settings.chosen_invalid_text_color.get())

forgot_password_labelframe = LabelFrame(text="Can't remember your password?", font=verdana_25, labelanchor=N)
forgot_password_button = Button(forgot_password_labelframe, text="Recover Password", font=verdana_25, borderwidth=3,
                                command=lambda: [display_forgot_password(),
                                                 clear_login_menu_variables(),
                                                 Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                 if Settings.chosen_gui_sound_setting.get() else None
                                                 ])

no_account_labelframe = LabelFrame(text="Don't have an account yet?", font=verdana_25, labelanchor=N)
register_button_2 = Button(no_account_labelframe, text="Create Account", font=verdana_25, borderwidth=3,
                           command=lambda: [User.came_from_main_menu.set(True), display_register_user_general_data(),
                                            Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                            if Settings.chosen_gui_sound_setting.get() else None])


"""Logout Menu Elements"""


logout_menu_label = Label(text="Log Out?", font=courier_100)

whoa_label = Label(text="Whoa... Do you really want to do that?", font=tempus_sans_itc_50_bold_italic)

sure_logout_labelframe = LabelFrame(text="Are you sure you want to Log Out?", font=verdana_40,
                                    labelanchor=N, borderwidth=5)
yes_button = Button(text="Yes, I'm sure...", font=verdana_40, borderwidth=3,
                    command=lambda: [User.logout_user(), display_main_menu(),
                                     Stats.main_menu_interactions_logged_out.set(
                                         Stats.main_menu_interactions_logged_out.get() + 1),
                                     Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                     if Settings.chosen_gui_sound_setting.get() else None])
no_button = Button(text="No, take me back", font=verdana_40, borderwidth=3,
                   command=lambda: [display_main_menu(),
                                    Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                    if Settings.chosen_gui_sound_setting.get() else None])


"""Recovery Key Menu Elements"""


recover_password_label = Label(text="Recover Password", font=courier_100)

recover_key_labelframe = LabelFrame(text="Enter your account's Recovery Key:", font=verdana_25, labelanchor=N)

recovery_key_username_label = Label(text="Account Username:", font=verdana_25)
recovery_key_username_entry = Entry(root, textvariable=User.recovery_key_username, font=verdana_25, justify=CENTER)

recovery_key_invalid_inputs_label = Label(text="DATA", font=verdana_25, fg=Settings.chosen_invalid_text_color.get())

recovery_key_entry_field_1 = Entry(root, textvariable=User.recovery_key_part_1, font=verdana_35, justify=CENTER)
recovery_key_entry_field_2 = Entry(root, textvariable=User.recovery_key_part_2, font=verdana_35, justify=CENTER)
recovery_key_entry_field_3 = Entry(root, textvariable=User.recovery_key_part_3, font=verdana_35, justify=CENTER)
recovery_key_entry_field_4 = Entry(root, textvariable=User.recovery_key_part_4, font=verdana_35, justify=CENTER)
recovery_key_dash_label_1 = Label(text="-", font=verdana_50)
recovery_key_dash_label_2 = Label(text="-", font=verdana_50)
recovery_key_dash_label_3 = Label(text="-", font=verdana_50)

recover_password_button = Button(text="Recover Password",
                                 font=verdana_25,
                                 command=lambda: [User.check_username_and_key_validity(
                                     User.recovery_key_username.get(), User.recovery_key_part_1.get(),
                                     User.recovery_key_part_2.get(), User.recovery_key_part_3.get(),
                                     User.recovery_key_part_4.get()),
                                                  Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                  if Settings.chosen_gui_sound_setting.get() else None])

recovered_password_labelframe = LabelFrame(text="Your account's password is:", font=verdana_25, labelanchor=N)

recovered_password_text = Text(recovered_password_labelframe, font=verdana_35, spacing1=15, spacing2=15, spacing3=15,
                               state=DISABLED, wrap=NONE)

recovered_password_text.tag_configure(CENTER, justify=CENTER)
Misc.copy_var_value_to_disabled_text_widget(text_text=User.PASSWORD_NOT_RECOVERED_MESSAGE,
                                            text_widget=recovered_password_text)
recovered_password_text.tag_add(CENTER, "1.0", END)

recovered_password_text_scrollbar = Scrollbar(recovered_password_labelframe, orient=HORIZONTAL)

# Add scroll bar to text box
recovered_password_text.config(xscrollcommand=recovered_password_text_scrollbar.set)
recovered_password_text_scrollbar.config(command=recovered_password_text.xview)

show_password_checkbutton_recovery_key = Checkbutton(text="Show Password", font=verdana_25, indicatoron=0,
                                                     variable=User.show_password_recovery_key, onvalue=True,
                                                     offvalue=False, state=DISABLED, command=lambda:
                                                     [show_hide_password_recovery_key(
                                                         User.show_password_recovery_key.get()),
                                                      Sounds.play_gui_sound(Sounds.CHECKBUTTON_SOUND_PATH)
                                                      if Settings.chosen_gui_sound_setting.get() else None])

create_recovered_password_file_button = Button(text="Create .txt File", font=verdana_25, state=DISABLED,
                                               command=lambda: [Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                                if Settings.chosen_gui_sound_setting.get()
                                                                else None,
                                                                User.create_recovered_password_txt_file(
                                                                    username=User.recovery_key_username.get(),
                                                                    password=User.recovered_password.get())
                                                                ])


"""Register Menu General Data Elements"""


register_menu_label = Label(text="Sign Up", font=courier_100)

# Initial Data Requirements

welcome_label = Label(text="Welcome!\n"
                           "In order to enjoy the outstanding features put at our users' disposal, "
                           "let's get to know each other better!", font=book_antiqua_23)

input_your_data_labelframe = LabelFrame(root, text="Input your data to create an account:", labelanchor=N,
                                        font=verdana_25)

first_name_label = Label(text="First Name:", font=verdana_25, anchor=E)
first_name_entry_field = Entry(root, textvariable=User.chosen_first_name, font=verdana_25, justify=CENTER,
                               borderwidth=3)

last_name_label = Label(text="Last Name:", font=verdana_25, anchor=E)
last_name_entry_field = Entry(root, textvariable=User.chosen_last_name, font=verdana_25, justify=CENTER,
                              borderwidth=3)

nickname_label = Label(text="Nickname:", font=verdana_25, anchor=E)
nickname_entry_field = Entry(root, textvariable=User.chosen_nickname, font=verdana_25, justify=CENTER)
nickname_help_label = Label(text="Leave empty if nickname not desired", font=verdana_11)

gender_label = Label(text="Gender:", font=verdana_25, anchor=E)
gender_option_menu = OptionMenu(root, User.chosen_gender, *Misc.GENDERS,
                                command=lambda *args: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                if Settings.chosen_gui_sound_setting.get() else None)
gender_option_menu.config(font=verdana_25, indicatoron=0, highlightthickness=0)
gender_option_menu["menu"].config(font=verdana_25)

birth_date_label = Label(text="Birth Date:", font=verdana_25, anchor=E)

birth_day_combobox = Combobox(root, textvariable=User.chosen_birth_day, justify=CENTER, font=verdana_25)
birth_day_combobox.bind("<<ComboboxSelected>>", lambda *args: Sounds.play_gui_sound(
    Sounds.CHECKBUTTON_SOUND_PATH) if Settings.chosen_gui_sound_setting.get() else None)
birth_day_combobox["values"] = Misc.DAYS_TUPLE
birth_day_label = Label(text="DAY", font=verdana_11)

birth_month_combobox = Combobox(root, textvariable=User.chosen_birth_month, justify=CENTER, font=verdana_25)
birth_month_combobox.bind("<<ComboboxSelected>>", lambda *args: Sounds.play_gui_sound(
    Sounds.CHECKBUTTON_SOUND_PATH) if Settings.chosen_gui_sound_setting.get() else None)
birth_month_combobox["values"] = Misc.MONTHS_NAMES
birth_month_label = Label(text="MONTH", font=verdana_11)

birth_year_combobox = Combobox(root, textvariable=User.chosen_birth_year, justify=CENTER, font=verdana_25)
birth_year_combobox.bind("<<ComboboxSelected>>", lambda *args: Sounds.play_gui_sound(
    Sounds.CHECKBUTTON_SOUND_PATH) if Settings.chosen_gui_sound_setting.get() else None)
birth_year_combobox["values"] = [year for year in range(1, datetime.date.today().year + 1)]
birth_year_label = Label(text="YEAR", font=verdana_11)

country_of_origin_label = Label(text="Country Of Origin:", font=verdana_25, anchor=E)
country_of_origin_option_menu = OptionMenu(root, User.chosen_country_of_origin, *Misc.COUNTRIES_NAMES,
                                           command=lambda x: [config_state_option_menu(
                                               User.chosen_country_of_origin.get(), "origin"),
                                               Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                               if Settings.chosen_gui_sound_setting.get() else None
                                           ])
country_of_origin_option_menu.config(font=verdana_13, indicatoron=0, highlightthickness=0)
country_of_origin_option_menu["menu"].config(font=verdana_10)

# Only if the USA gets chosen as the country of origin
state_of_origin_label = Label(text="State Of Origin:", font=verdana_25, anchor=E)
state_of_origin_option_menu = OptionMenu(root, User.chosen_state_of_origin, *Misc.US_STATES_NAMES,
                                         command=lambda *args: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                         if Settings.chosen_gui_sound_setting.get() else None)
state_of_origin_option_menu.config(font=verdana_13, state=DISABLED, indicatoron=0, highlightthickness=0)
state_of_origin_option_menu["menu"].config(font=verdana_10)

country_of_residence_label = Label(text="Country Of Residence:", font=verdana_25, anchor=E)
country_of_residence_option_menu = OptionMenu(root, User.chosen_country_of_residence, *Misc.COUNTRIES_NAMES,
                                              command=lambda x: [config_state_option_menu(
                                                  User.chosen_country_of_residence.get(), "residence"),
                                                  Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                                  if Settings.chosen_gui_sound_setting.get() else None
                                              ])
country_of_residence_option_menu.config(font=verdana_13, indicatoron=0, highlightthickness=0)
country_of_residence_option_menu["menu"].config(font=verdana_10)

# Only if the USA gets chosen as the current country of residence
state_of_residence_label = Label(text="State Of Residence:", font=verdana_25, anchor=E)
state_of_residence_option_menu = OptionMenu(root, User.chosen_state_of_residence, *Misc.US_STATES_NAMES,
                                            command=lambda *args: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                            if Settings.chosen_gui_sound_setting.get() else None)
state_of_residence_option_menu.config(font=verdana_13, state=DISABLED, indicatoron=0, highlightthickness=0)
state_of_residence_option_menu["menu"].config(font=verdana_10)

account_privacy_label = Label(text="Account Privacy:", font=verdana_25, anchor=E)
account_privacy_option_menu = OptionMenu(root, User.chosen_account_privacy, *User.ACCOUNT_PRIVACY_OPTIONS,
                                         command=lambda *args: Sounds.play_gui_sound(Sounds.RADIOBUTTON_SOUND_PATH)
                                         if Settings.chosen_gui_sound_setting.get() else None)
account_privacy_option_menu.config(font=verdana_25, indicatoron=0, highlightthickness=0)
account_privacy_option_menu["menu"].config(font=verdana_25)

lookup_help_label = Label(text="For any unclarity you may have concerning these options, have a glimpse in here ►",
                          font=verdana_20, anchor=E)

# Slash Labels
slash_label1 = Label(text="/", font=verdana_25)  # Between birth day - birth month
slash_label2 = Label(text="/", font=verdana_25)  # Between birth month - birth year


"""Register Menu Username & Password Elements"""


hello_new_user_label = Label(text="Hello, PRONOUN LAST NAME!\nYour account is almost ready, last step to go!",
                             font=book_antiqua_23)

register_menu_labelframe = LabelFrame(root, text="Please choose your account username and password:",
                                      font=verdana_25, labelanchor=N)

choose_username_label = Label(text="Choose Username:", font=verdana_25, anchor=E)
choose_username_entry_field = Entry(root, textvariable=User.chosen_username, font=verdana_25, justify=CENTER,
                                    borderwidth=3)
username_help_label = Label(text=f"Min. {User.MINIMUM_USERNAME_LENGTH} - Max. {User.MAXIMUM_USERNAME_LENGTH}"
                                 f" characters, no spaces",
                            font=verdana_11)
taken_username_label = Label(text="Username taken! Please choose another one!",
                             font=verdana_25, fg=Settings.chosen_invalid_text_color.get())

choose_password_label = Label(text="Choose Password:", font=verdana_25, anchor=E)
choose_password_entry_field = Entry(root, textvariable=User.chosen_password, font=verdana_25, justify=CENTER,
                                    show="•", borderwidth=3)
password_help_label = Label(text=f"Min. {User.MINIMUM_PASSWORD_LENGTH} characters, only digits and letters",
                            font=verdana_11)

confirm_password_label = Label(text="Confirm Password:", font=verdana_25, anchor=E)
confirm_password_entry_field = Entry(root, textvariable=User.chosen_confirm_password, font=verdana_25,
                                     justify=CENTER, show="•", borderwidth=3)
confirm_password_help_label = Label(text="Must be the same as your password", font=verdana_11)

show_password_checkbutton_register = Checkbutton(text="Show Password", font=verdana_25, indicatoron=0,
                                                 variable=User.show_password_register, onvalue=True, offvalue=False,
                                                 command=lambda: [show_hide_password_register(
                                                     User.show_password_register.get()),
                                                     Sounds.play_gui_sound(Sounds.CHECKBUTTON_SOUND_PATH)
                                                     if Settings.chosen_gui_sound_setting.get() else None])

create_account_button = Button(text="Create Account", font=verdana_25, state=DISABLED,
                               command=lambda:
                               [Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                if Settings.chosen_gui_sound_setting.get() else None,
                                User.register_new_user(first_name=User.chosen_first_name.get(),
                                                       last_name=User.chosen_last_name.get(),
                                                       nickname=User.chosen_nickname.get(),
                                                       username=User.chosen_username.get(),
                                                       password=User.chosen_password.get(),
                                                       gender=User.chosen_gender.get(),
                                                       year=int(User.chosen_birth_year.get()),
                                                       month=Misc.MONTHS_DICT[User.chosen_birth_month.get()],
                                                       day=int(User.chosen_birth_day.get()),
                                                       country_of_origin=User.chosen_country_of_origin.get(),
                                                       state_of_origin=User.chosen_state_of_origin.get(),
                                                       country_of_residence=User.chosen_country_of_residence.get(),
                                                       state_of_residence=User.chosen_state_of_residence.get(),
                                                       privacy=User.chosen_account_privacy.get(),
                                                       background_color=Settings.chosen_background_color.get(),
                                                       text_color=Settings.chosen_text_color.get(),
                                                       button_color=Settings.chosen_button_color.get(),
                                                       button_text_color=Settings.chosen_button_text_color.get(),
                                                       invalid_text_color=Settings.chosen_invalid_text_color.get(),
                                                       gui_sound=Settings.chosen_gui_sound_setting.get()),
                                display_registration_successful(),
                                clear_register_user_variables(),
                                User.write_users_in_file(),
                                logged_in_user_username_label.config
                                (text=f"Logged In User: {User.logged_in_user['Credentials']['Username']}"),
                                Composition.update_composer_list(),
                                Stats.accounts_active.set(Stats.accounts_active.get() + 1),
                                Stats.main_menu_interactions_registered.set(
                                    Stats.main_menu_interactions_registered.get() + 1)
                                ])


"""Successful Registration Menu Elements (Recovery Key)"""


registration_successful_menu_label = Label(text="Registration Successful", font=courier_80)

congratulations_label = Label(text="Congratulations PRONOUN USERNAME, your account registration is now complete!\n"
                                   "You are the XXXth user to join us!",
                              font=verdana_25)

recovery_key_labelframe = LabelFrame(text="This is your account recovery key:", font=verdana_25,
                                     labelanchor=N)

recovery_key_info_label = Label(text="It will come in handy if you ever forget your password!",
                                font=verdana_25)

given_recovery_key_label = Label(root, font=verdana_50, text="XXXX-XXXX-XXXX-XXXX")

create_recovery_key_txt_file_button = Button(text="Create .txt File", font=verdana_25,
                                             command=lambda: [Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                              if Settings.chosen_gui_sound_setting.get()
                                                              else None,
                                                              User.create_recovery_key_txt_file(
                                               username=User.logged_in_user['Credentials']['Username'],
                                               recovery_key=User.logged_in_user['Credentials']['Recovery Key'])
                                             ])

gained_powers_labelframe = LabelFrame(text="You are now able to:", font=verdana_25, labelanchor=N)
gained_powers_label1 = Label(text="→ Record your very own compositions!", font=verdana_25, anchor=W)
gained_powers_label2 = Label(text="→ Listen to other users\' compositions!",
                             font=verdana_25, anchor=W)
gained_powers_label3 = Label(text="→ Leave feedback on (rate) other users\' compositions!",
                             font=verdana_25, anchor=W)
gained_powers_label4 = Label(text="→ Become a famous composer & make history in the world of music!",
                             font=verdana_25, anchor=W)


"""Register Help Menu Elements"""


help_menu_label = Label(text="Help", font=courier_100)

help_text_labelframe1 = LabelFrame(text="Your Account Privacy determines whether other users can see your "
                                        "personal data*:",
                                   font=verdana_20, labelanchor=N)
help_text_label1 = Label(text="► Having a Public setting will allow other users to see your personal data and your "
                              "compositions.", font=verdana_19, anchor=W)
help_text_label2 = Label(text="► Having a Private Details setting will not allow other users to see your "
                              "personal data, but will allow them to see your compositions.",
                         font=verdana_19, anchor=W)
help_text_label3 = Label(text="► Having a Private Compositions setting will allow other users to see your personal "
                              "data, but will not allow them to see your compositions.",
                         font=verdana_19, anchor=W)
help_text_label4 = Label(text="► Having a Private setting will not allow any users to see your personal data "
                              "nor your compositions.", font=verdana_19, anchor=W)

help_text_labelframe2 = LabelFrame(text="Recovery Key:", font=verdana_20, labelanchor=N)
help_text_label6 = Label(text="► Once registered, you will receive a unique Recovery Key. "
                              "It is advised to note it down somewhere safe (or create a .txt file).",
                         font=verdana_20, anchor=W)
help_text_label7 = Label(text="► You will need to input your Recovery Key if you ever forget your Password.",
                         font=verdana_20, anchor=W)

help_text_labelframe3 = LabelFrame(text="Miscellaneous:", font=verdana_20, labelanchor=N)
help_text_label8 = Label(text="► Logging in will be done with your account\'s Username and Password.",
                         font=verdana_20, anchor=W)
help_text_label9 = Label(text=f"► Username must be between {User.MINIMUM_USERNAME_LENGTH} and "
                              f"{User.MAXIMUM_USERNAME_LENGTH} characters long and must also not contain any spaces.",
                         font=verdana_20, anchor=W)
help_text_label10 = Label(text=f"► Password must be at least {User.MINIMUM_PASSWORD_LENGTH} characters long and "
                               "must also contain only numerical and alphabetical characters.",
                          font=verdana_20, anchor=W)
help_text_label11 = Label(text="► Returning to the Main Menu while not having successfully created an account "
                               "will clear all your input data.", font=verdana_20, anchor=W)

help_wip_label = Label(root, text="* Feature is still WIP and is unavailable as of this app version.",
                       font=verdana_25_italic, anchor=W)


"""User Profile Menu Elements"""


user_profile_menu_label = Label(text="User Profile", font=courier_100)

user_profile_labelframe = LabelFrame(text="My Profile/USERNAME's Profile:", font=verdana_25, labelanchor=N)

user_profile_first_name_label = Label(text="First Name : ", font=verdana_25, anchor=E)
user_profile_last_name_label = Label(text="Last Name : ", font=verdana_25, anchor=E)
user_profile_nickname_label = Label(text="Nickname : ", font=verdana_25, anchor=E)
user_profile_gender_label = Label(text="Gender : ", font=verdana_25, anchor=E)
user_profile_country_origin_label = Label(text="Country Of Origin : ", font=verdana_25, anchor=E)
user_profile_state_origin_label = Label(text="State Of Origin : ", font=verdana_25, anchor=E)
user_profile_country_residence_label = Label(text="Country Of Residence : ", font=verdana_25, anchor=E)
user_profile_state_residence_label = Label(text="State Of Residence : ", font=verdana_25, anchor=E)
user_profile_birth_date_label = Label(text="Birth Date : ", font=verdana_25, anchor=E)
user_profile_current_age_label = Label(text="Current Age : ", font=verdana_25, anchor=E)
user_profile_hidden_word_found_label = Label(text="Hidden Words Found : ", font=verdana_25, anchor=E)

user_profile_first_name_data_label = Label(text="DATA", font=verdana_25, anchor=W)
user_profile_last_name_data_label = Label(text="DATA", font=verdana_25, anchor=W)
user_profile_nickname_data_label = Label(text="DATA", font=verdana_25, anchor=W)
user_profile_gender_data_label = Label(text="DATA", font=verdana_25, anchor=W)
user_profile_country_origin_data_label = Label(text="DATA", font=verdana_25, anchor=W)
user_profile_state_origin_data_label = Label(text="DATA", font=verdana_25, anchor=W)
user_profile_country_residence_data_label = Label(text="DATA", font=verdana_25, anchor=W)
user_profile_state_residence_data_label = Label(text="DATA", font=verdana_25, anchor=W)
user_profile_birth_date_data_label = Label(text="DATA", font=verdana_25, anchor=W)
user_profile_current_age_data_label = Label(text="DATA", font=verdana_25, anchor=W)
user_profile_hidden_word_found_data_label = Label(text="DATA", font=verdana_25, anchor=W)

user_profile_options_label = Label(text="Options:", font=verdana_25)

# Separators
# Separates name labels & data labels form the rest of the labels & data labels
user_profile_separator_1 = Separator(root)
# used to separate data labels form option button "box"
user_profile_separator_2 = Separator(root)
user_profile_separator_3 = Separator(root)

view_country_details_button = Button(text="View Country Details", font=verdana_25,
                                     command=lambda: [display_country_details(),
                                                      Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                      if Settings.chosen_gui_sound_setting.get() else None
                                                      ])

# TODO: Add more user-related functionality
# view_compositions_button = Button(text="View Compositions", font=verdana_25)
# view_user_stats_button = Button(text="View User Stats", font=verdana_25)
# send_message_button = Button(text="Send Message", font=verdana_25)
# edit_account_button = Button(text="Edit Account", font=verdana_25)
# delete_account_button = Button(text="Delete Account", font=verdana_25)


"""Country Details Menu"""


country_details_menu_label = Label(text="Country Details", font=courier_100)

# When the country of origin is the same as the country of residence
same_country_label = Label(root, text="This user's country of origin & residence are the same.",
                           font=verdana_25)

# Country of origin
country_details_origin_labelframe = LabelFrame(text="Country of Origin:", font=verdana_25, labelanchor=N)

# Title labels
country_details_origin_name_label = Label(text="Name :", font=verdana_25, anchor=E)
country_details_origin_capital_label = Label(text="Capital :", font=verdana_25, anchor=E)
country_details_origin_continent_label = Label(text="Continent :", font=verdana_25, anchor=E)
country_details_origin_currency_label = Label(text="Currency :", font=verdana_25, anchor=E)
country_details_origin_phone_prefix_label = Label(text="Phone Prefix :", font=verdana_25, anchor=E)
country_details_origin_name_ISO2_label = Label(text="ISO 3166-1 Alpha-2 Code :", font=verdana_25, anchor=E)
country_details_origin_name_ISO3_label = Label(text="ISO 3166-1 Alpha-3 Code :", font=verdana_25, anchor=E)
country_details_origin_continent_ISO2_label = Label(text="Continent Code (CC) :", font=verdana_25, anchor=E)

# For the United States title labels
country_details_origin_state_name_label = Label(text="State :", font=verdana_25, anchor=E)
country_details_origin_state_name_ISO2_label = Label(text="ISO 3166-2:US Code :", font=verdana_25, anchor=E)

# Data labels
country_details_origin_name_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_origin_capital_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_origin_continent_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_origin_currency_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_origin_phone_prefix_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_origin_name_ISO2_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_origin_name_ISO3_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_origin_continent_ISO2_data_label = Label(text="DATA", font=verdana_25, anchor=W)

# For the United States data labels
country_details_origin_state_name_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_origin_state_name_ISO2_data_label = Label(text="DATA", font=verdana_25, anchor=W)

# Country of residence
country_details_residence_labelframe = LabelFrame(text="Country of Residence:", font=verdana_25, labelanchor=N)

# Title labels
country_details_residence_name_label = Label(text="Name :", font=verdana_25, anchor=E)
country_details_residence_capital_label = Label(text="Capital :", font=verdana_25, anchor=E)
country_details_residence_continent_label = Label(text="Continent :", font=verdana_25, anchor=E)
country_details_residence_currency_label = Label(text="Currency :", font=verdana_25, anchor=E)
country_details_residence_phone_prefix_label = Label(text="Phone Prefix :", font=verdana_25, anchor=E)
country_details_residence_name_ISO2_label = Label(text="ISO 3166-1 Alpha-2 Code :", font=verdana_25, anchor=E)
country_details_residence_name_ISO3_label = Label(text="ISO 3166-1 Alpha-3 Code :", font=verdana_25, anchor=E)
country_details_residence_continent_ISO2_label = Label(text="Continent Code (CC) :", font=verdana_25, anchor=E)

# For the United States title labels
country_details_residence_state_name_label = Label(text="State :", font=verdana_25, anchor=E)
country_details_residence_state_name_ISO2_label = Label(text="ISO 3166-2:US Code :", font=verdana_25, anchor=E)

# Data labels
country_details_residence_name_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_residence_capital_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_residence_continent_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_residence_currency_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_residence_phone_prefix_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_residence_name_ISO2_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_residence_name_ISO3_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_residence_continent_ISO2_data_label = Label(text="DATA", font=verdana_25, anchor=W)

# For the United States data labels
country_details_residence_state_name_data_label = Label(text="DATA", font=verdana_25, anchor=W)
country_details_residence_state_name_ISO2_data_label = Label(text="DATA", font=verdana_25, anchor=W)

return_to_profile_button = Button(text="Return to Profile", font=verdana_25,
                                  command=lambda: [display_user_profile(User.user_profile_user),
                                                   Sounds.play_gui_sound(Sounds.BUTTON_SOUND_PATH)
                                                   if Settings.chosen_gui_sound_setting.get() else None
                                                   ])


"""Tuple containing all the error widgets"""

ERROR_WIDGETS_TUPLE: tuple = (login_first_label, invalid_composition_name_label, no_compositions_label,
                              sort_user_invalid_composer_name_label, sort_length_invalid_selection_label,
                              sort_date_invalid_specific_label, sort_date_invalid_interval_label,
                              sort_date_invalid_from_date_label, sort_date_invalid_to_date_label,
                              sort_date_invalid_from_and_to_date_label, sort_rating_invalid_selection_label,
                              incorrect_account_data_label, recovery_key_invalid_inputs_label, taken_username_label)


"""Functions"""


def quit_app():
    """Quits App
    """
    Settings.write_remember_settings_value()
    if Settings.remember_settings_setting.get():
        Settings.write_preset_settings()
    User.write_logged_in_user_in_file(User.remember_me.get())
    sys.exit()


def change_gui_elements(target: str, setting_value: str):
    """Changes various GUI elements' appearance, based on the settings target and value
    """
    # Prepare full widget list
    widget_list: list = root.winfo_children()
    for item in widget_list:
        if item.winfo_children():
            widget_list.extend(item.winfo_children())

    # Get lighter and darker variants of the given color
    lighter_color: str = Settings.get_color_variation(color=setting_value, factor=Settings.TINT_FACTOR)

    if target == "Background Color":
        # Get more colors needed for this setting change
        even_lighter_color: str = Settings.get_color_variation(color=setting_value, factor=Settings.TINT_FACTOR * 1.7)
        darker_color: str = Settings.get_color_variation(color=setting_value, factor=Settings.SHADE_FACTOR)
        # Do color changes
        change_background_color(widget_list=widget_list, setting_value=setting_value, lighter_color=lighter_color,
                                even_lighter_color=even_lighter_color, darker_color=darker_color)

    elif target == "Text Color":
        # Do color changes
        change_text_color(widget_list=widget_list, setting_value=setting_value, lighter_color=lighter_color)

    elif target == "Buttons' Color":
        # Get more colors needed for this setting change
        darker_color: str = Settings.get_color_variation(color=setting_value, factor=Settings.SHADE_FACTOR)
        # Do color changes
        change_button_color(widget_list=widget_list, setting_value=setting_value, lighter_color=lighter_color,
                            darker_color=darker_color)

    elif target == "Buttons' Text Color":
        # Get more colors needed for this setting change
        even_lighter_color: str = Settings.get_color_variation(color=setting_value, factor=Settings.TINT_FACTOR * 1.7)
        # Do color changes
        change_button_text_color(widget_list=widget_list, setting_value=setting_value, lighter_color=lighter_color,
                                 even_lighter_color=even_lighter_color)

    elif target == "Invalid Text Color":
        # Do color changes
        change_invalid_text_color(setting_value=setting_value, lighter_color=lighter_color)

    else:
        # If stupid value was passed
        raise ValueError(f"Invalid Setting Option: {target}")


def change_background_color(widget_list: list, setting_value: str, lighter_color: str, even_lighter_color: str,
                            darker_color: str):
    """Changes the background color of all relevant widgets
    """
    widget_types: tuple = (Label, Message, Frame, LabelFrame, Checkbutton, Text, ScrolledText, Listbox, Scale)

    default: bool = True if setting_value == Settings.default_background_color else False

    root.config(bg=setting_value)

    # Config ttk styles
    style.configure("TSeparator", background=setting_value)
    style.configure('Sort.TNotebook.Tab',
                    background=Settings.default_notebook_tab_background_color if default else lighter_color)
    style.configure('Sorted.TNotebook.Tab',
                    background=Settings.default_notebook_tab_background_color if default else lighter_color)
    style.configure("TNotebook", background=setting_value)
    style.configure("Horizontal.TProgressbar",
                    troughcolor=Settings.default_progress_bar_trough_color if default else lighter_color,
                    background=Settings.default_progress_bar_background_color if default else darker_color)

    for widget in widget_list:
        if type(widget) in widget_types:
            # Checkbuttons
            if type(widget) == Checkbutton and widget.cget("indicatoron") == 1:
                widget.config(bg=setting_value, activebackground=setting_value, selectcolor=lighter_color)
                continue
            # Scrolled texts or Texts
            if type(widget) == ScrolledText or type(widget) == Text:
                widget.config(bg=Settings.default_text_background_color if default else lighter_color,
                              selectbackground=Settings.default_text_select_background_color if default
                              else even_lighter_color)
                continue
            # Listboxes
            if type(widget) == Listbox:
                widget.config(bg=Settings.default_listbox_background_color if default else lighter_color,
                              selectbackground=Settings.default_listbox_active_color if default else darker_color,
                              highlightbackground=setting_value)
                continue
            # Scales
            if type(widget) == Scale:
                widget.config(bg=setting_value, highlightbackground=setting_value,
                              troughcolor=Settings.default_slider_trough_color if default else lighter_color,
                              activebackground=setting_value if default else darker_color)
                continue
            # Everything else
            widget.config(bg=setting_value)


def change_text_color(widget_list: list, setting_value: str, lighter_color: str):
    """Changes the text color of all relevant widgets
    """
    widget_types: tuple = (Label, Message, LabelFrame, Checkbutton, Text, ScrolledText, Scale)

    default: bool = True if setting_value == Settings.default_text_color else False

    for widget in widget_list:
        if type(widget) in widget_types:
            # If error widget found, continue
            if widget in ERROR_WIDGETS_TUPLE:
                continue
            # Checkbuttons
            if type(widget) == Checkbutton and widget.cget("indicatoron") == 1:
                widget.config(fg=setting_value, activeforeground=setting_value)
                continue
            # Scrolled texts or Texts
            if type(widget) == ScrolledText or type(widget) == Text:
                widget.config(fg=setting_value,
                              selectforeground=Settings.default_text_select_text_color if default else lighter_color)
                continue
            # Scales
            if type(widget) == Scale:
                widget.config(fg=setting_value)
                continue
            # Everything else
            widget.config(fg=setting_value)


def change_button_color(widget_list: list, setting_value: str, lighter_color: str, darker_color: str):
    """Changes the text color of all relevant widgets
    """
    widget_types: tuple = (Button, Radiobutton, Checkbutton, OptionMenu, Entry)

    default: bool = True if setting_value == Settings.default_buttons_color else False

    # Config ttk styles
    combobox_options: dict = {
        "background": Settings.default_combobox_background_color if default else darker_color,
        "selectbackground": Settings.default_combobox_select_background_color if default else lighter_color,
        "fieldbackground": Settings.default_combobox_field_background_color if default else setting_value
    }
    style.configure('TCombobox', **combobox_options)
    style.configure('Error.TCombobox', **combobox_options)

    style.configure("TEntry", background=setting_value, fieldbackground=setting_value, selectbackground=lighter_color)
    style.configure("Error.TEntry", background=setting_value, fieldbackground=setting_value,
                    selectbackground=lighter_color)

    for widget in widget_list:
        if type(widget) in widget_types:
            # Radiobuttons
            if type(widget) == Radiobutton:
                widget.config(bg=Settings.default_active_background_color if default else setting_value,
                              activebackground=Settings.default_active_background_color if default else setting_value,
                              selectcolor=Settings.default_radiobutton_active_text_color if default else lighter_color)
                continue
            # Checkbuttons
            if type(widget) == Checkbutton:
                if widget.cget("indicatoron") == 1:
                    continue
                widget.configure(bg=Settings.default_active_background_color if default else setting_value,
                                 activebackground=setting_value,
                                 selectcolor=Settings.default_checkbutton_active_text_color if default
                                 else lighter_color)
                continue
            # Optionmenus
            if type(widget) == OptionMenu:
                widget.config(bg=Settings.default_active_background_color if default else setting_value,
                              activebackground=Settings.default_optionmenu_active_background_color if default
                              else setting_value)
                widget["menu"].configure(bg=setting_value,
                                         activebackground=Settings.default_menu_active_background_color if default
                                         else lighter_color)
                continue
            # Entries
            if type(widget) == Entry:
                widget.config(bg=Settings.default_entry_background_color if default else setting_value,
                              selectbackground=Settings.default_entry_highlight_background_color
                              if default else lighter_color)
                continue
            # Quit button
            if widget is quit_button:
                continue
            # Everything else
            widget.config(bg=Settings.default_active_background_color if default else setting_value,
                          activebackground=Settings.default_button_select_color if default else lighter_color)


def change_button_text_color(widget_list: list, setting_value: str, lighter_color: str, even_lighter_color: str):
    """Changes the text color of all relevant widgets
    """
    widget_types: tuple = (Button, Radiobutton, Checkbutton, OptionMenu, Entry)

    default: bool = True if setting_value == Settings.default_button_text_color else False

    # Config ttk styles
    combobox_options: dict = {
        "foreground": setting_value,
        "selectforeground": Settings.default_combobox_select_text_color if default else lighter_color
    }
    style.configure('TCombobox', **combobox_options)

    style.configure('Sort.TNotebook.Tab', foreground=setting_value)
    style.configure('Sorted.TNotebook.Tab', foreground=setting_value)

    for widget in widget_list:
        if type(widget) in widget_types:
            # Radiobuttons
            if type(widget) == Radiobutton:
                widget.config(fg=setting_value, activeforeground=setting_value,
                              disabledforeground=Settings.default_disabled_text_color if default
                              else even_lighter_color)
                continue
            # Checkbuttons
            if type(widget) == Checkbutton and widget.cget("indicatoron"):
                continue
            # Optionmenus
            if type(widget) == OptionMenu:
                widget.config(fg=setting_value, activeforeground=setting_value,
                              disabledforeground=Settings.default_disabled_text_color if default
                              else even_lighter_color)
                widget["menu"].configure(fg=setting_value,
                                         activeforeground=Settings.default_menu_active_text_color if default
                                         else lighter_color)
                continue
            # Entries
            if type(widget) == Entry:
                widget.config(fg=setting_value,
                              selectforeground=Settings.default_entry_highlight_text_color
                              if default else lighter_color)
                continue
            # Quit button
            if widget is quit_button:
                continue
            # Everything else
            widget.config(fg=setting_value, activeforeground=setting_value,
                          disabledforeground=Settings.default_disabled_text_color if default else even_lighter_color)


def change_invalid_text_color(setting_value: str, lighter_color: str):
    """Changes the text color of all relevant widgets
    """

    # Config ttk style
    style.configure('Error.TCombobox', foreground=setting_value, selectforeground=lighter_color)

    for widget in ERROR_WIDGETS_TUPLE:
        widget.config(fg=setting_value)


def config_about_chosen_instrument_text(instrument: str):
    """Configures the instrument description Text widget contents
    """
    # Get description, available notes and font size
    # Place relevant labels on screen
    if instrument == "Piano":
        Sounds.chosen_instrument_description.set(Sounds.PIANO_DESCRIPTION)
        Sounds.chosen_instrument_available_notes.set(Sounds.PIANO_NOTES)
        available_notes_label.place(relheight=0.06, relwidth=0.48, relx=0.26, rely=0.70)
        note_length_mention_label.place(relheight=0.04, relwidth=0.48, relx=0.26, rely=0.76)
    elif instrument == "Flute":
        Sounds.chosen_instrument_description.set(Sounds.FLUTE_DESCRIPTION)
        Sounds.chosen_instrument_available_notes.set(Sounds.FLUTE_NOTES)
        available_notes_label.place(relheight=0.07, relwidth=0.48, relx=0.26, rely=0.715)
        note_length_mention_label.place_forget()
    elif instrument == "Trumpet":
        Sounds.chosen_instrument_description.set(Sounds.TRUMPET_DESCRIPTION)
        Sounds.chosen_instrument_available_notes.set(Sounds.TRUMPET_NOTES)
        available_notes_label.place(relheight=0.07, relwidth=0.48, relx=0.26, rely=0.715)
        note_length_mention_label.place_forget()
    else:  # instrument == "Violin"
        Sounds.chosen_instrument_description.set(Sounds.VIOLIN_DESCRIPTION)
        Sounds.chosen_instrument_available_notes.set(Sounds.VIOLIN_NOTES)
        available_notes_label.place(relheight=0.07, relwidth=0.48, relx=0.26, rely=0.715)
        note_length_mention_label.place_forget()
    # Config text widget text (contents)
    Misc.copy_var_value_to_disabled_text_widget(text_text=Sounds.chosen_instrument_description,
                                                text_widget=about_chosen_instrument_text)
    if instrument == "Piano":
        font: Font = verdana_30
    else:
        font: Font = verdana_40
    # Config available notes label
    available_notes_label.config(text=Sounds.chosen_instrument_available_notes.get(), font=font)


def process_invalid_composition_name_gui_elements():
    """Places or forgets the invalid composition labels, depending on the given input
    """
    if Composition.is_composition_name_already_used(Composition.chosen_new_composition_name.get()):
        new_composition_name_entry.config(fg=Settings.chosen_invalid_text_color.get())
        invalid_composition_name_label.config(text=Composition.used_composition_name_error_message +
                                              Composition.invalid_used_composition_name_owner_username + "!")
        invalid_composition_name_label.place(relheight=0.055, relwidth=0.975, relx=0.0125, rely=0.835)
        go_to_save_composition_button.config(state=DISABLED)
        start_recording_button.config(state=DISABLED)
    elif Misc.empty_string(Composition.chosen_new_composition_name.get()):
        invalid_composition_name_label.config(text=Composition.whitespace_composition_name_error_message)
        invalid_composition_name_label.place(relheight=0.055, relwidth=0.975, relx=0.0125, rely=0.835)
        go_to_save_composition_button.config(state=DISABLED)
        start_recording_button.config(state=DISABLED)
    else:
        new_composition_name_entry.config(fg=Settings.chosen_button_text_color.get())
        invalid_composition_name_label.place_forget()
        start_recording_button.config(state=NORMAL)
        if Composition.at_least_1_note_recorded.get():
            go_to_save_composition_button.config(state=NORMAL)


def highlight_invalid_register_user_names(first_name: str, last_name: str):
    """Highlights the GUI elements containing bad input data in the Register Menu
    """
    root.focus()
    # from string import punctuation
    if Misc.empty_string(first_name):
        User.chosen_first_name.set("First Name")
        first_name_entry_field.configure(fg=Settings.chosen_invalid_text_color.get())
    if Misc.empty_string(last_name):
        User.chosen_last_name.set("Last Name")
        last_name_entry_field.configure(fg=Settings.chosen_invalid_text_color.get())


def config_state_option_menu(variable: str, tag: str):
    """Configures state of origin/residence option menus
    """
    if variable == "United States":
        if tag == "origin":
            User.chosen_state_of_origin.set(Misc.US_STATES_NAMES[0])
            state_of_origin_option_menu.configure(state=NORMAL)
        elif tag == "residence":
            User.chosen_state_of_residence.set(Misc.US_STATES_NAMES[0])
            state_of_residence_option_menu.configure(state=NORMAL)
    else:
        if tag == "origin":
            User.chosen_state_of_origin.set("None")
            state_of_origin_option_menu.configure(state=DISABLED)
        elif tag == "residence":
            User.chosen_state_of_residence.set("None")
            state_of_residence_option_menu.configure(state=DISABLED)


def show_hide_password_register(boolean: bool):
    """Shows or hides the current password input in the register menu
    """
    if boolean:
        show_password_checkbutton_register.config(text="Hide Password")
        choose_password_entry_field.config(show="")
        confirm_password_entry_field.config(show="")
    else:
        show_password_checkbutton_register.config(text="Show Password")
        choose_password_entry_field.config(show="•")
        confirm_password_entry_field.config(show="•")


def show_hide_password_login(boolean: bool):
    """Shows or hides the current password input in the login menu
    """
    if boolean:
        show_password_checkbutton_login.config(text="Hide Password")
        password_entry_field.config(show="")
    else:
        show_password_checkbutton_login.config(text="Show Password")
        password_entry_field.config(show="•")


def show_hide_password_recovery_key(boolean: bool):
    """Shows or hides the recovered password output in the forgot password (recovery key) menu
    """
    if boolean:
        show_password_checkbutton_recovery_key.config(text="Hide Password")
        Misc.copy_var_value_to_disabled_text_widget(text_text=User.recovered_password.get(),
                                                    text_widget=recovered_password_text)
    else:
        show_password_checkbutton_recovery_key.config(text="Show Password")
        Misc.copy_var_value_to_disabled_text_widget(text_text="•" * len(User.recovered_password.get()),
                                                    text_widget=recovered_password_text)


def clear_login_menu_variables():
    """Clears login menu variables & sets the show/hide password checkbutton to off & hides password
    """
    root.focus()

    User.entered_login_username.set("")
    User.entered_login_password.set("")

    User.show_password_login.set(False)
    show_password_checkbutton_login.config(text="Show Password")
    password_entry_field.config(show="•")


def clear_register_user_variables():
    """Clears register user menu variables & sets the show/hide password checkbutton to off & hides password
    """

    User.is_in_register_user_menu_general_data.set(False)

    User.chosen_first_name.set("")
    User.chosen_last_name.set("")
    User.chosen_nickname.set("")

    User.chosen_gender.set(Misc.GENDERS[-1])

    User.chosen_birth_day.set(datetime.date.today().day)
    User.chosen_birth_month.set(datetime.date.today().strftime("%B"))
    User.chosen_birth_year.set(datetime.date.today().year)

    User.chosen_country_of_origin.set(Misc.COUNTRIES_NAMES[0])
    User.chosen_state_of_origin.set("None")
    state_of_origin_option_menu.configure(state=DISABLED)

    User.chosen_country_of_residence.set(Misc.COUNTRIES_NAMES[0])
    User.chosen_state_of_residence.set("None")
    state_of_residence_option_menu.configure(state=DISABLED)

    User.chosen_account_privacy.set(User.ACCOUNT_PRIVACY_OPTIONS[0])

    User.chosen_username.set("")
    User.chosen_password.set("")
    User.chosen_confirm_password.set("")

    User.show_password_register.set(False)
    show_password_checkbutton_register.config(text="Show Password")
    choose_password_entry_field.config(show="•")
    confirm_password_entry_field.config(show="•")


def clear_password_recovery_variables():
    """Clears forgot password menu variables & sets the show/hide password checkbutton to off
    """
    root.focus()

    User.recovered_password.set("")

    User.recovery_key_username.set("")

    User.recovery_key_part_1.set("")
    User.recovery_key_part_2.set("")
    User.recovery_key_part_3.set("")
    User.recovery_key_part_4.set("")

    User.failed_recovery_attempts.set(0)

    recovered_password_text.tag_configure(CENTER, justify=CENTER)
    Misc.copy_var_value_to_disabled_text_widget(text_text=User.PASSWORD_NOT_RECOVERED_MESSAGE,
                                                text_widget=recovered_password_text)
    recovered_password_text.tag_add(CENTER, "1.0", END)

    User.show_password_recovery_key.set(False)
    show_password_checkbutton_recovery_key.config(state=DISABLED, text="Show Password")

    create_recovered_password_file_button.config(state=DISABLED, text="Create .txt File")


def clear_new_composition_variables():
    """"Clears the New Composition Menu variables & hides labels
    """
    Composition.is_recording_composition.set(False)
    Composition.at_least_1_note_recorded.set(False)

    Composition.chosen_new_composition_name.set("")
    Composition.new_composition_description.set("")

    Composition.new_composition = copy.deepcopy(Composition.DEFAULT_COMPOSITION)  # Likely this isn't needed
    Composition.notes_list = []
    Composition.delay_list = []
    Composition.length = 0
    Composition.delay_scale_value.set(0)

    invalid_composition_name_label.place_forget()

    last_note_played_record_label.config(text="Last note played: None")
    composition_length_label.config(text="Length: 0 seconds")
    clear_note_count_dict_and_labels(target="Record")


def clear_sorting_composition_variables():
    """Clears the Composition Sorting variables
    """

    # Any invalid sorting boolean determines whether the current selected sorting options set is valid or not
    Composition.is_any_invalid_sorting_option.set(False)

    # User
    Composition.sort_by_user.set("Any")

    Composition.user_inclusive_exclusive.set("Inclusive")

    Composition.sort_user_selected_user.set(User.logged_in_user["Credentials"]["Username"]
                                            if User.is_logged_in and len(User.logged_in_user["Compositions"])
                                            else sort_user_choose_user_combobox["values"][0])

    # Invalid user sorting option boolean
    Composition.is_invalid_user_sorting_option.set(False)

    # Length
    Composition.sort_by_length.set("Any")

    Composition.specific_length.set(Composition.POSSIBLE_LENGTHS_TUPLE[0])

    Composition.short_length.set(1)
    Composition.medium_length.set(0)
    Composition.long_length.set(0)

    # Invalid length sorting option boolean
    Composition.is_invalid_length_sorting_option.set(False)

    # Date
    Composition.sort_by_date.set("Any")
    Composition.date_specific_inclusive_exclusive.set("Inclusive")
    Composition.date_interval_inclusive_exclusive.set("Inclusive")

    # For specific date
    Composition.sort_date_selected_day.set(datetime.date.today().day)
    Composition.sort_date_selected_month.set(datetime.date.today().strftime("%B"))
    Composition.sort_date_selected_year.set(datetime.date.today().year)

    # For date interval
    # From ...
    Composition.sort_date_selected_day_from.set(1)
    Composition.sort_date_selected_month_from.set(Misc.MONTHS_NAMES[0])
    Composition.sort_date_selected_year_from.set(datetime.date.today().year)

    # ... to
    Composition.sort_date_selected_day_to.set(datetime.date.today().day)
    Composition.sort_date_selected_month_to.set(datetime.date.today().strftime("%B"))
    Composition.sort_date_selected_year_to.set(datetime.date.today().year)

    # Invalid date sorting option boolean
    Composition.is_invalid_date_sorting_option.set(False)

    # Rating
    Composition.sort_by_rating.set("Any")

    Composition.specific_rating.set(5)

    Composition.no_rating.set(0)
    Composition.star_1_rating.set(0)
    Composition.star_2_rating.set(0)
    Composition.star_3_rating.set(0)
    Composition.star_4_rating.set(0)
    Composition.star_5_rating.set(1)

    # Invalid rating sorting option boolean
    Composition.is_invalid_rating_sorting_option.set(False)

    # Preselect option
    Composition.preselect_option.set("First")


def increment_number_of_notes(instrument: str, switch: str):
    """Increases the number of notes played values for each matching key
    """

    if Composition.is_recording_composition.get():
        Sounds.number_of_notes_recorded["Total"] += 1
        if instrument == "Piano":
            if switch == "Short":
                Sounds.number_of_notes_recorded["Piano"]["Short"] += 1
            else:
                Sounds.number_of_notes_recorded["Piano"]["Long"] += 1
        elif instrument == "Flute":
            Sounds.number_of_notes_recorded["Flute"] += 1
        elif instrument == "Trumpet":
            Sounds.number_of_notes_recorded["Trumpet"] += 1
        elif instrument == "Violin":
            Sounds.number_of_notes_recorded["Violin"] += 1
    else:
        Sounds.number_of_notes_played_freely["Total"] += 1
        if instrument == "Piano":
            if switch == "Short":
                Sounds.number_of_notes_played_freely["Piano"]["Short"] += 1
            else:
                Sounds.number_of_notes_played_freely["Piano"]["Long"] += 1
        elif instrument == "Flute":
            Sounds.number_of_notes_played_freely["Flute"] += 1
        elif instrument == "Trumpet":
            Sounds.number_of_notes_played_freely["Trumpet"] += 1
        elif instrument == "Violin":
            Sounds.number_of_notes_played_freely["Violin"] += 1
    # Config all labels
    config_note_number_labels()


def config_note_number_labels():
    """Configs all labels
    """

    if Composition.is_recording_composition.get():
        # Total
        if Sounds.number_of_notes_recorded["Total"] == 1:
            number_of_notes_played_record_labelframe["text"] = "Played 1 note:"
        else:
            number_of_notes_played_record_labelframe["text"] = "Played " + str(
                Sounds.number_of_notes_recorded["Total"]) + " notes:"

        # Piano
        if Sounds.number_of_notes_recorded["Piano"]["Short"] + Sounds.number_of_notes_recorded["Piano"]["Long"] == 1:
            number_of_piano_notes_played_record_label["text"] = "- 1 piano note, " + \
                                                                str(Sounds.number_of_notes_recorded["Piano"][
                                                                        "Short"]) + " short & " + \
                                                                str(Sounds.number_of_notes_recorded["Piano"][
                                                                        "Long"]) + " long"
        else:
            number_of_piano_notes_played_record_label["text"] = "- " + str(
                Sounds.number_of_notes_recorded["Piano"]["Short"] +
                Sounds.number_of_notes_recorded["Piano"]["Long"]) + \
                                                                " piano notes, " + \
                                                                str(Sounds.number_of_notes_recorded["Piano"][
                                                                        "Short"]) + " short & " + \
                                                                str(Sounds.number_of_notes_recorded["Piano"][
                                                                        "Long"]) + " long"

        # Flute
        if Sounds.number_of_notes_recorded["Flute"] == 1:
            number_of_flute_notes_played_record_label["text"] = "- 1 flute note"
        else:
            number_of_flute_notes_played_record_label["text"] = "- " + str(
                Sounds.number_of_notes_recorded["Flute"]) + \
                                                                " flute notes"

        # Trumpet
        if Sounds.number_of_notes_recorded["Trumpet"] == 1:
            number_of_trumpet_notes_played_record_label["text"] = "- 1 trumpet note"
        else:
            number_of_trumpet_notes_played_record_label["text"] = "- " + str(
                Sounds.number_of_notes_recorded["Trumpet"]) + \
                                                                  " trumpet notes"

        # Violin
        if Sounds.number_of_notes_recorded["Violin"] == 1:
            number_of_violin_notes_played_record_label["text"] = "- 1 violin note"
        else:
            number_of_violin_notes_played_record_label["text"] = "- " + str(
                Sounds.number_of_notes_recorded["Violin"]) + \
                                                                 " violin notes"
    else:
        if Sounds.number_of_notes_played_freely["Total"] == 1:
            number_of_notes_played_freely_labelframe["text"] = "Played 1 note:"
        else:
            number_of_notes_played_freely_labelframe["text"] = "Played " + str(
                Sounds.number_of_notes_played_freely["Total"]) + " notes:"

        # Piano
        if Sounds.number_of_notes_played_freely["Piano"]["Short"] + Sounds.number_of_notes_played_freely["Piano"][
                "Long"] == 1:
            number_of_piano_notes_played_freely_label["text"] = "- 1 piano note, " + \
                                                                str(Sounds.number_of_notes_played_freely["Piano"][
                                                                        "Short"]) + " short & " + \
                                                                str(Sounds.number_of_notes_played_freely["Piano"][
                                                                        "Long"]) + " long"
        else:
            number_of_piano_notes_played_freely_label["text"] = "- " + str(
                Sounds.number_of_notes_played_freely["Piano"]["Short"] +
                Sounds.number_of_notes_played_freely["Piano"]["Long"]) + \
                                                                " piano notes, " + \
                                                                str(Sounds.number_of_notes_played_freely["Piano"][
                                                                        "Short"]) + " short & " + \
                                                                str(Sounds.number_of_notes_played_freely["Piano"][
                                                                        "Long"]) + " long"

        # Flute
        if Sounds.number_of_notes_played_freely["Flute"] == 1:
            number_of_flute_notes_played_freely_label["text"] = "- 1 flute note"
        else:
            number_of_flute_notes_played_freely_label["text"] = "- " + str(
                Sounds.number_of_notes_played_freely["Flute"]) + \
                                                                " flute notes"

        # Trumpet
        if Sounds.number_of_notes_played_freely["Trumpet"] == 1:
            number_of_trumpet_notes_played_freely_label["text"] = "- 1 trumpet note"
        else:
            number_of_trumpet_notes_played_freely_label["text"] = "- " + str(
                Sounds.number_of_notes_played_freely["Trumpet"]) + \
                                                                  " trumpet notes"

        # Violin
        if Sounds.number_of_notes_played_freely["Violin"] == 1:
            number_of_violin_notes_played_freely_label["text"] = "- 1 violin note"
        else:
            number_of_violin_notes_played_freely_label["text"] = "- " + str(
                Sounds.number_of_notes_played_freely["Violin"]) + \
                                                                 " violin notes"
        # Re-enable reset note count button
        reset_note_count_button.config(state=NORMAL)


def config_last_note_played_label(note: str, instrument: str, switch: str):
    """Configures last note played label
    """

    if Composition.is_recording_composition.get():
        if instrument == "Piano":
            if switch == "Short":
                last_note_played_record_label.config(text=f"Last note played: {note} Short Piano")
            else:
                last_note_played_record_label.config(text=f"Last note played: {note} Long Piano")
        else:
            last_note_played_record_label.config(text=f"Last note played: {note} {instrument}")
    else:
        if instrument == "Piano":
            if switch == "Short":
                last_note_played_freely_label.config(text=f"Last note played: {note} Short Piano")
            else:
                last_note_played_freely_label.config(text=f"Last note played: {note} Long Piano")
        else:
            last_note_played_freely_label.config(text=f"Last note played: {note} {instrument}")


def config_save_composition_labels_and_text():
    """Configures the save composition GUI elements (labels and text widgets)
    """
    # Label(s)
    save_composition_description_length_label.config(text=f"Description Length : \n"
                                                          f"{len(Composition.new_composition_description.get())} / "
                                                          f"{Composition.MAXIMUM_DESCRIPTION_LENGTH}")
    # Get composition notes and delays text for its corresponding text widget
    composition_notes_and_delays: str = \
        "\n".join(Composition.get_composition_notes_and_delays(Composition.new_composition))
    composition_notes_and_delays += " - Last delay will not be used."
    # Text Widgets
    Misc.copy_var_value_to_disabled_text_widget(text_text=User.logged_in_user["Credentials"]["Username"],
                                                text_widget=save_composition_composer_text)
    Misc.copy_var_value_to_disabled_text_widget(text_text=Composition.chosen_new_composition_name,
                                                text_widget=save_composition_name_text)
    Misc.copy_var_value_to_disabled_text_widget(text_text=Composition.new_composition_description,
                                                text_widget=save_composition_description_text)
    Misc.copy_var_value_to_disabled_text_widget(text_text=composition_notes_and_delays,
                                                text_widget=save_composition_notes_and_delays_text)
    Misc.copy_var_value_to_disabled_text_widget(text_text=Misc.format_duration(duration=Composition.length,
                                                                               with_suggestion=False),
                                                text_widget=save_composition_composition_length_text)


def clear_note_count_dict_and_labels(target: str = "Free"):
    """Clears note count dict and labels
    """
    if target == "Free":
        Sounds.number_of_notes_played_freely = copy.deepcopy(Sounds.NUMBER_OF_NOTES_PLAYED_CLEAN_DICT)
        # Reset labels
        number_of_notes_played_freely_labelframe.config(text=Sounds.default_number_of_notes_played_label_text)

        number_of_piano_notes_played_freely_label.config(text=Sounds.default_number_of_piano_notes_played_label_text)
        number_of_flute_notes_played_freely_label.config(text=Sounds.default_number_of_flute_notes_played_label_text)
        number_of_trumpet_notes_played_freely_label.config(
            text=Sounds.default_number_of_trumpet_notes_played_label_text)
        number_of_violin_notes_played_freely_label.config(text=Sounds.default_number_of_violin_notes_played_label_text)
    else:
        Sounds.number_of_notes_recorded = copy.deepcopy(Sounds.NUMBER_OF_NOTES_PLAYED_CLEAN_DICT)
        # Reset labels
        number_of_notes_played_record_labelframe.config(text=Sounds.default_number_of_notes_played_label_text)

        number_of_piano_notes_played_record_label.config(text=Sounds.default_number_of_piano_notes_played_label_text)
        number_of_flute_notes_played_record_label.config(text=Sounds.default_number_of_flute_notes_played_label_text)
        number_of_trumpet_notes_played_record_label.config(
            text=Sounds.default_number_of_trumpet_notes_played_label_text)
        number_of_violin_notes_played_record_label.config(text=Sounds.default_number_of_violin_notes_played_label_text)


def config_country_details_labels(country_of_origin: str, state_of_origin: str,
                                  country_of_residence: str, state_of_residence: str):
    """Configures the country details' menu data labels
    """

    # Initialise text variables
    # Country of origin
    country_of_origin_capital: str = ""
    country_of_origin_continent: str = ""
    country_of_origin_currency: str = ""
    country_of_origin_phone_prefix: str = ""
    state_of_origin_iso2: str = ""
    has_state_of_origin: bool = False
    country_of_origin_continent_iso2: str = ""
    country_of_origin_iso2: str = ""
    country_of_origin_iso3: str = ""
    # Country of residence
    country_of_residence_capital: str = ""
    country_of_residence_continent: str = ""
    country_of_residence_currency: str = ""
    country_of_residence_phone_prefix: str = ""
    state_of_residence_iso2: str = ""
    has_state_of_residence: bool = False
    country_of_residence_continent_iso2: str = ""
    country_of_residence_iso2: str = ""
    country_of_residence_iso3: str = ""

    # Get country data
    for country in Misc.COUNTRIES_DICT:
        if country_of_origin == country:  # Origin
            country_of_origin_capital = Misc.COUNTRIES_DICT[country]["Capital"]
            country_of_origin_continent = Misc.COUNTRIES_DICT[country]["Continent"]
            country_of_origin_currency = Misc.COUNTRIES_DICT[country]["Currency"]
            country_of_origin_phone_prefix = Misc.COUNTRIES_DICT[country]["Phone"]
            country_of_origin_continent_iso2 = Misc.COUNTRIES_DICT[country]["ISO2_Continent"]
            country_of_origin_iso2 = Misc.COUNTRIES_DICT[country]["ISO2"]
            country_of_origin_iso3 = Misc.COUNTRIES_DICT[country]["ISO3"]
        if country_of_residence == country:  # Residence
            country_of_residence_capital = Misc.COUNTRIES_DICT[country]["Capital"]
            country_of_residence_continent = Misc.COUNTRIES_DICT[country]["Continent"]
            country_of_residence_currency = Misc.COUNTRIES_DICT[country]["Currency"]
            country_of_residence_phone_prefix = Misc.COUNTRIES_DICT[country]["Phone"]
            country_of_residence_continent_iso2 = Misc.COUNTRIES_DICT[country]["ISO2_Continent"]
            country_of_residence_iso2 = Misc.COUNTRIES_DICT[country]["ISO2"]
            country_of_residence_iso3 = Misc.COUNTRIES_DICT[country]["ISO3"]

    # Get state data
    # Origin
    if state_of_origin != "None":
        has_state_of_origin = True
    # Residence
    if state_of_residence != "None":
        has_state_of_residence = True
    # Get state iso2
    if has_state_of_origin or has_state_of_residence:
        for state in Misc.US_STATES_DICT:
            if state_of_origin == Misc.US_STATES_DICT[state] and has_state_of_origin:  # Origin
                state_of_origin_iso2 = state
            if state_of_residence == Misc.US_STATES_DICT[state] and has_state_of_residence:  # Residence
                state_of_residence_iso2 = state

    # Configure text values for missing data
    # Country of origin
    if not country_of_origin_capital:
        country_of_origin_capital = "N/A"
    if not country_of_origin_continent:
        country_of_origin_continent = "N/A"
    if not country_of_origin_currency:
        country_of_origin_currency = "N/A"
    if not country_of_origin_phone_prefix:
        country_of_origin_phone_prefix = "N/A"
    if not state_of_origin_iso2:
        state_of_origin_iso2 = "None"
    else:
        state_of_origin_iso2 = f"US-{state_of_origin_iso2}"
    if not country_of_origin_continent_iso2:
        country_of_origin_continent_iso2 = "N/A"
    if not country_of_origin_iso2:
        country_of_origin_iso2 = "N/A"
    if not country_of_origin_iso3:
        country_of_origin_iso3 = "N/A"
    # Country of residence
    if not country_of_residence_capital:
        country_of_residence_capital = "N/A"
    if not country_of_residence_continent:
        country_of_residence_continent = "N/A"
    if not country_of_residence_currency:
        country_of_residence_currency = "N/A"
    if not country_of_residence_phone_prefix:
        country_of_residence_phone_prefix = "N/A"
    if not state_of_residence_iso2:
        state_of_residence_iso2 = "None"
    else:
        state_of_residence_iso2 = f"US-{state_of_residence_iso2}"
    if not country_of_residence_continent_iso2:
        country_of_residence_continent_iso2 = "N/A"
    if not country_of_residence_iso2:
        country_of_residence_iso2 = "N/A"
    if not country_of_residence_iso3:
        country_of_residence_iso3 = "N/A"

    # Config labels
    # Country of origin
    # Row 1
    country_details_origin_name_data_label.config(text=country_of_origin)
    country_details_origin_capital_data_label.config(text=country_of_origin_capital)
    country_details_origin_state_name_data_label.config(text=state_of_origin)
    country_details_origin_continent_data_label.config(text=country_of_origin_continent)
    country_details_origin_currency_data_label.config(text=country_of_origin_currency)
    country_details_origin_phone_prefix_data_label.config(text=country_of_origin_phone_prefix)
    # Row 2
    country_details_origin_state_name_ISO2_data_label.config(text=state_of_origin_iso2)
    country_details_origin_continent_ISO2_data_label.config(text=country_of_origin_continent_iso2)
    country_details_origin_name_ISO2_data_label.config(text=country_of_origin_iso2)
    country_details_origin_name_ISO3_data_label.config(text=country_of_origin_iso3)

    # Country of residence
    # Row 1
    country_details_residence_name_data_label.config(text=country_of_residence)
    country_details_residence_capital_data_label.config(text=country_of_residence_capital)
    country_details_residence_state_name_data_label.config(text=state_of_residence)
    country_details_residence_continent_data_label.config(text=country_of_residence_continent)
    country_details_residence_currency_data_label.config(text=country_of_residence_currency)
    country_details_residence_phone_prefix_data_label.config(text=country_of_residence_phone_prefix)
    # Row 2
    country_details_residence_state_name_ISO2_data_label.config(text=state_of_residence_iso2)
    country_details_residence_continent_ISO2_data_label.config(text=country_of_residence_continent_iso2)
    country_details_residence_name_ISO2_data_label.config(text=country_of_residence_iso2)
    country_details_residence_name_ISO3_data_label.config(text=country_of_residence_iso3)


def config_sort_by_user_frame():
    """Configures the Sort by User Frame in Playback Composition
    """
    if Composition.sort_by_user.get() == "Any":
        # Place the reserved GUI section label
        sort_user_reserved_label.place(relheight=1, relwidth=1)
        # Forget sorting by multiple users content frame (contains all elements)
        sort_user_choose_users_content_frame.place_forget()
        sort_user_invalid_composer_name_label.place_forget()
        # Config data label
        current_sorting_by_user_data_label.config(text=Composition.sort_by_user.get())
        # Place / Forget relevant frames
        sort_user_choose_any_frame.place(relheight=.175, relwidth=.5, relx=.25, rely=.275)
        sort_user_choose_user_frame.place_forget()
    elif Composition.sort_by_user.get() == "Specific":
        # Place the reserved GUI section label
        sort_user_reserved_label.place(relheight=1, relwidth=1)
        # Forget sorting by multiple users content frame (contains all elements)
        sort_user_choose_users_content_frame.place_forget()
        # Config data label
        current_sorting_by_user_data_label.config(text=Composition.sort_by_user.get())
        # Place / Forget relevant frames
        sort_user_choose_any_frame.place_forget()
        sort_user_choose_user_frame.place(relheight=.175, relwidth=.5, relx=.25, rely=.275)
    else:
        # Forget the reserved GUI section label
        sort_user_reserved_label.place_forget()
        # Place sorting by multiple users content frame (contains all elements)
        sort_user_choose_users_content_frame.place(relheight=1, relwidth=1)
        # Config data label
        current_sorting_by_user_data_label.config(text=Composition.sort_by_user.get() + " " +
                                                  Composition.user_inclusive_exclusive.get())
        # Place / Forget relevant frames
        sort_user_choose_any_frame.place_forget()
        sort_user_choose_user_frame.place(relheight=.175, relwidth=.5, relx=.25, rely=.275)
    # Place the invalid length selection label & config relevant data label, if necessary
    sort_compositions_invalid_user_selection(Composition.sort_user_selected_user.get())


def config_sort_by_length_frame():
    """Configures the Sort by Length Frame in Playback Composition
    """
    if Composition.sort_by_length.get() == "Any":
        # Config data label
        current_sorting_by_length_data_label.config(text=Composition.sort_by_length.get())
        # Place / Forget relevant frames
        sort_length_choose_any_frame.place(relheight=.225, relwidth=.8, relx=.1, rely=.275)
        sort_length_choose_length_frame.place_forget()
        sort_length_choose_lengths_frame.place_forget()
    elif Composition.sort_by_length.get() == "Specific":
        # Config data label
        current_sorting_by_length_data_label.config(text=Composition.sort_by_length.get())
        # Place / Forget relevant frames
        sort_length_choose_any_frame.place_forget()
        sort_length_choose_length_frame.place(relheight=.225, relwidth=.8, relx=.1, rely=.275)
        sort_length_choose_lengths_frame.place_forget()
    else:
        # Config data label
        current_sorting_by_length_data_label.config(text=Composition.sort_by_length.get())
        # Place / Forget relevant frames
        sort_length_choose_any_frame.place_forget()
        sort_length_choose_length_frame.place_forget()
        sort_length_choose_lengths_frame.place(relheight=.225, relwidth=.8, relx=.1, rely=.275)
    # Place the invalid length selection label & config relevant data label, if necessary
    sort_compositions_invalid_length_selection()


def config_sort_by_date_frame():
    """Configures the Sort by Date Frame in Playback Composition
    """
    if Composition.sort_by_date.get() == "Any":
        # Config data label
        current_sorting_by_date_data_label.config(text=Composition.sort_by_date.get())
        # Any / Inclusive / Exclusive label frame
        sort_date_any_date_labelframe.place(relheight=.285, relwidth=.45, relx=.025, rely=.6)
        sort_date_specific_inclusive_exclusive_labelframe.place_forget()
        sort_date_interval_inclusive_exclusive_labelframe.place_forget()
        # Specific date
        sort_date_specific_date_day_combobox.config(state=DISABLED)
        sort_date_specific_date_month_combobox.config(state=DISABLED)
        sort_date_specific_date_year_combobox.config(state=DISABLED)
        # From - to labels
        sort_date_date_interval_from_label.config(state=DISABLED)
        sort_date_date_interval_to_label.config(state=DISABLED)
        # From date
        sort_date_from_date_day_combobox.config(state=DISABLED)
        sort_date_from_date_month_combobox.config(state=DISABLED)
        sort_date_from_date_year_combobox.config(state=DISABLED)
        # To date
        sort_date_to_date_day_combobox.config(state=DISABLED)
        sort_date_to_date_month_combobox.config(state=DISABLED)
        sort_date_to_date_year_combobox.config(state=DISABLED)
    elif Composition.sort_by_date.get() == "Specific":
        # Config data label
        current_sorting_by_date_data_label.config(text=Composition.sort_by_date.get())
        # Any / Inclusive / Exclusive label frame
        sort_date_any_date_labelframe.place_forget()
        sort_date_specific_inclusive_exclusive_labelframe.place(relheight=.285, relwidth=.45, relx=.025, rely=.6)
        sort_date_interval_inclusive_exclusive_labelframe.place_forget()
        # Specific date
        sort_date_specific_date_day_combobox.config(state=NORMAL)
        sort_date_specific_date_month_combobox.config(state=NORMAL)
        sort_date_specific_date_year_combobox.config(state=NORMAL)
        # From - to labels
        sort_date_date_interval_from_label.config(state=DISABLED)
        sort_date_date_interval_to_label.config(state=DISABLED)
        # From date
        sort_date_from_date_day_combobox.config(state=DISABLED)
        sort_date_from_date_month_combobox.config(state=DISABLED)
        sort_date_from_date_year_combobox.config(state=DISABLED)
        # To date
        sort_date_to_date_day_combobox.config(state=DISABLED)
        sort_date_to_date_month_combobox.config(state=DISABLED)
        sort_date_to_date_year_combobox.config(state=DISABLED)
    else:
        # Config data label
        current_sorting_by_date_data_label.config(text=Composition.sort_by_date.get())
        # Any / Inclusive / Exclusive label frame
        sort_date_any_date_labelframe.place_forget()
        sort_date_specific_inclusive_exclusive_labelframe.place_forget()
        sort_date_interval_inclusive_exclusive_labelframe.place(relheight=.285, relwidth=.45, relx=.025, rely=.6)
        # Specific date
        sort_date_specific_date_day_combobox.config(state=DISABLED)
        sort_date_specific_date_month_combobox.config(state=DISABLED)
        sort_date_specific_date_year_combobox.config(state=DISABLED)
        # From - to labels
        sort_date_date_interval_from_label.config(state=NORMAL)
        sort_date_date_interval_to_label.config(state=NORMAL)
        # From date
        sort_date_from_date_day_combobox.config(state=NORMAL)
        sort_date_from_date_month_combobox.config(state=NORMAL)
        sort_date_from_date_year_combobox.config(state=NORMAL)
        # To date
        sort_date_to_date_day_combobox.config(state=NORMAL)
        sort_date_to_date_month_combobox.config(state=NORMAL)
        sort_date_to_date_year_combobox.config(state=NORMAL)
    # Place the relevant invalid date interval label & config relevant data label, if necessary
    sort_compositions_invalid_date_input()
    # Invalid interval takes priority over invalid specific date


def config_sort_by_rating_frame():
    """Configures the Sort by Date Frame in Playback Composition
    """
    if Composition.sort_by_rating.get() == "Any":
        # Config data label
        current_sorting_by_rating_data_label.config(text=Composition.sort_by_rating.get())
        # Place / Forget relevant frames
        sort_rating_choose_any_frame.place(relheight=.285, relwidth=.8, relx=.1, rely=.275)
        sort_rating_choose_rating_labelframe.place_forget()
        sort_rating_choose_ratings_labelframe.place_forget()
    elif Composition.sort_by_rating.get() == "Specific":
        # Config data label
        current_sorting_by_rating_data_label.config(text=Composition.sort_by_rating.get())
        # Place / Forget relevant frames
        sort_rating_choose_any_frame.place_forget()
        sort_rating_choose_rating_labelframe.place(relheight=.285, relwidth=.8, relx=.1, rely=.275)
        sort_rating_choose_ratings_labelframe.place_forget()
    else:
        # Config data label
        current_sorting_by_rating_data_label.config(text=Composition.sort_by_rating.get())
        # Place / Forget relevant frames
        sort_rating_choose_any_frame.place_forget()
        sort_rating_choose_rating_labelframe.place_forget()
        sort_rating_choose_ratings_labelframe.place(relheight=.285, relwidth=.8, relx=.1, rely=.275)
    # Place the invalid rating selection label & config relevant data label, if necessary
    sort_compositions_invalid_rating_selection()


def sort_compositions_invalid_user_selection(given_username: str):
    """Places or forgets the invalid user selection label from composition sorting by user
    Modifies the current sorting option label
    Sets the invalid option variable, which in turn enables or disables the proceed button
    """
    if Composition.sort_by_user.get() == "Any":
        # Config data label
        current_sorting_by_user_data_label.config(text=Composition.sort_by_user.get(),
                                                  fg=Settings.chosen_text_color.get())
        # Set invalid user option to False
        Composition.is_invalid_user_sorting_option.set(False)
    elif Composition.sort_by_user.get() == "Specific":
        # Check given username validity
        if not valid_composer_name(given_username):
            sort_user_choose_user_label.config(fg=Settings.chosen_invalid_text_color.get())
            sort_user_choose_user_combobox.config(style="Error.TCombobox")
            sort_user_invalid_composer_name_label.place(relwidth=1, relheight=1)
            sort_user_choose_users_content_frame.place_forget()
            # Config data label
            current_sorting_by_user_data_label.config(text="Invalid Username Input",
                                                      fg=Settings.chosen_invalid_text_color.get())
            # Set invalid user option to True
            Composition.is_invalid_user_sorting_option.set(True)
        else:
            sort_user_choose_user_label.config(fg=Settings.chosen_text_color.get())
            sort_user_choose_user_combobox.config(style="TCombobox")
            sort_user_invalid_composer_name_label.place_forget()
            sort_user_choose_users_content_frame.place(relwidth=1, relheight=1)
            # Config data label
            current_sorting_by_user_data_label.config(text=Composition.sort_by_user.get(),
                                                      fg=Settings.chosen_text_color.get())
            # Set invalid user option to False
            Composition.is_invalid_user_sorting_option.set(False)
    else:
        sort_user_invalid_composer_name_label.place_forget()
        # Check given username validity
        if not valid_composer_name(given_username):
            sort_user_choose_user_label.config(fg=Settings.chosen_invalid_text_color.get())
            sort_user_choose_user_combobox.config(style="Error.TCombobox")
            sort_user_add_selected_button.config(state=DISABLED)
        else:
            sort_user_choose_user_label.config(fg=Settings.chosen_text_color.get())
            sort_user_choose_user_combobox.config(style="TCombobox")
            check_if_selected_user_in_listbox(given_username=given_username)
        if not sort_user_listbox.get(first=0, last=END):  # i.e. listbox contents are empty
            # Config data label
            current_sorting_by_user_data_label.config(text="None " + Composition.user_inclusive_exclusive.get(),
                                                      fg=Settings.chosen_invalid_text_color.get())
            # Set invalid user option to True
            Composition.is_invalid_user_sorting_option.set(True)
        elif combobox_values_match_listbox_values() and Composition.user_inclusive_exclusive.get() == "Exclusive":
            # Config data label
            current_sorting_by_user_data_label.config(text="All Exclusive",
                                                      fg=Settings.chosen_invalid_text_color.get())
            # Set invalid user option to True
            Composition.is_invalid_user_sorting_option.set(True)
        else:
            # Config data label
            current_sorting_by_user_data_label.config(text=Composition.sort_by_user.get() + " " +
                                                      Composition.user_inclusive_exclusive.get(),
                                                      fg=Settings.chosen_text_color.get())
            # Set invalid user option to False
            Composition.is_invalid_user_sorting_option.set(False)


def sort_compositions_invalid_length_selection():
    """Places or forgets the invalid selection label from composition sorting by length
    Modifies the current sorting option label
    Sets the invalid option variable, which in turn enables or disables the proceed button
    """

    def config_sort_length_checkbutton_fg_color(text_color: str, button_text_color: str):
        """Configures the fg color of the sort length checkbuttons AND LABEL
        """
        sort_length_choose_lengths_label.config(fg=text_color)
        sort_length_short_checkbutton.config(fg=button_text_color)
        sort_length_medium_checkbutton.config(fg=button_text_color)
        sort_length_long_checkbutton.config(fg=button_text_color)

    if Composition.sort_by_length.get() == "Multiple":
        if not Composition.short_length.get() \
                and not Composition.medium_length.get() and not Composition.long_length.get():
            sort_length_invalid_selection_label.place(relheight=.1, relwidth=.99, relx=.005, rely=.89)
            current_sorting_by_length_data_label.config(text="Invalid Multiple Selection",
                                                        fg=Settings.chosen_invalid_text_color.get())
            config_sort_length_checkbutton_fg_color(Settings.chosen_invalid_text_color.get(),
                                                    Settings.chosen_invalid_text_color.get())
            # Set invalid length option to True
            Composition.is_invalid_length_sorting_option.set(True)
        else:
            sort_length_invalid_selection_label.place_forget()
            current_sorting_by_length_data_label.config(text=Composition.sort_by_length.get(),
                                                        fg=Settings.chosen_text_color.get())
            config_sort_length_checkbutton_fg_color(Settings.chosen_text_color.get(),
                                                    Settings.chosen_button_text_color.get())
            # Set invalid length option to False
            Composition.is_invalid_length_sorting_option.set(False)
    else:
        sort_length_invalid_selection_label.place_forget()
        current_sorting_by_length_data_label.config(text=Composition.sort_by_length.get(),
                                                    fg=Settings.chosen_text_color.get())
        config_sort_length_checkbutton_fg_color(Settings.chosen_text_color.get(),
                                                Settings.chosen_button_text_color.get())
        # Set invalid length option to False
        Composition.is_invalid_length_sorting_option.set(False)


def sort_compositions_invalid_date_input():
    """Places or forgets the invalid date interval label from composition sorting by date
    Modifies the current sorting option label
    Sets the invalid option variable, which in turn enables or disables the proceed button
    """
    if Composition.sort_by_date.get() == "Specific":
        # Forget labels from date interval selection while selecting specific date
        sort_date_invalid_interval_label.place_forget()
        sort_date_invalid_from_date_label.place_forget()
        sort_date_invalid_to_date_label.place_forget()
        sort_date_invalid_from_and_to_date_label.place_forget()
        if not Misc.is_valid_date(year=Composition.sort_date_selected_year.get(),
                                  month=Composition.sort_date_selected_month.get(),
                                  day=Composition.sort_date_selected_day.get()):
            sort_date_invalid_specific_label.place(relheight=.1, relwidth=.99, relx=.005, rely=.89)
            current_sorting_by_date_data_label.config(text="Invalid Specific Date",
                                                      fg=Settings.chosen_invalid_text_color.get())
            # If not valid date, set invalid date sorting option to True
            Composition.is_invalid_date_sorting_option.set(True)
            return None
        else:
            sort_date_invalid_specific_label.place_forget()
            current_sorting_by_date_data_label.config(text=Composition.sort_by_date.get() + " " +
                                                      Composition.date_specific_inclusive_exclusive.get(),
                                                      fg=Settings.chosen_text_color.get())
            # If valid date, set invalid date sorting option to False
            Composition.is_invalid_date_sorting_option.set(False)
            return None
    elif Composition.sort_by_date.get() == "Interval":
        # Forget label from specific date selection while selecting date interval
        sort_date_invalid_specific_label.place_forget()
        # Presume both dates are invalid
        from_date_valid: bool = False
        to_date_valid: bool = False
        # If from date is valid, alter corresponding boolean variable
        if Misc.is_valid_date(year=Composition.sort_date_selected_year_from.get(),
                              month=Composition.sort_date_selected_month_from.get(),
                              day=Composition.sort_date_selected_day_from.get()):
            from_date_valid = True
        # If to date is valid, alter corresponding boolean variable
        if Misc.is_valid_date(year=Composition.sort_date_selected_year_to.get(),
                              month=Composition.sort_date_selected_month_to.get(),
                              day=Composition.sort_date_selected_day_to.get()):
            to_date_valid = True
        # If both dates are valid, check the interval
        if from_date_valid and to_date_valid:
            # If valid interval
            if not Misc.is_date_1_bigger_than_date_2(date_1_year=Composition.sort_date_selected_year_from.get(),
                                                     date_1_month=Composition.sort_date_selected_month_from.get(),
                                                     date_1_day=Composition.sort_date_selected_day_from.get(),
                                                     date_2_year=Composition.sort_date_selected_year_to.get(),
                                                     date_2_month=Composition.sort_date_selected_month_to.get(),
                                                     date_2_day=Composition.sort_date_selected_day_to.get()):
                # Configure from and to text labels foreground
                sort_date_date_interval_from_label.config(fg=Settings.chosen_text_color.get())
                sort_date_date_interval_to_label.config(fg=Settings.chosen_text_color.get())
                # Place and place_forget relevant labels
                sort_date_invalid_interval_label.place_forget()
                sort_date_invalid_from_date_label.place_forget()
                sort_date_invalid_to_date_label.place_forget()
                sort_date_invalid_from_and_to_date_label.place_forget()
                # Config data label
                current_sorting_by_date_data_label.config(text=Composition.sort_by_date.get() + " " +
                                                          Composition.date_interval_inclusive_exclusive.get(),
                                                          fg=Settings.chosen_text_color.get())
                Composition.is_invalid_date_sorting_option.set(False)
                return None
            # If not valid interval
            else:
                # Configure from and to text labels foreground
                sort_date_date_interval_from_label.config(fg=Settings.chosen_invalid_text_color.get())
                sort_date_date_interval_to_label.config(fg=Settings.chosen_invalid_text_color.get())
                # Place and place_forget relevant labels
                sort_date_invalid_interval_label.place(relheight=.1, relwidth=.99, relx=.005, rely=.89)
                sort_date_invalid_from_date_label.place_forget()
                sort_date_invalid_to_date_label.place_forget()
                sort_date_invalid_from_and_to_date_label.place_forget()
                # Config data label
                current_sorting_by_date_data_label.config(text="Invalid Date Interval",
                                                          fg=Settings.chosen_invalid_text_color.get())
                # If not valid interval, set invalid date sorting option to True
                Composition.is_invalid_date_sorting_option.set(True)
                return None
        # If date/s is/are not valid, set invalid date sorting option to True
        Composition.is_invalid_date_sorting_option.set(True)
        # Both dates invalid
        if not (from_date_valid or to_date_valid):
            # Configure from and to text labels foreground
            sort_date_date_interval_from_label.config(fg=Settings.chosen_text_color.get())
            sort_date_date_interval_to_label.config(fg=Settings.chosen_text_color.get())
            # Place and place_forget relevant labels
            sort_date_invalid_interval_label.place_forget()
            sort_date_invalid_from_date_label.place_forget()
            sort_date_invalid_to_date_label.place_forget()
            sort_date_invalid_from_and_to_date_label.place(relheight=.1, relwidth=.99, relx=.005, rely=.89)
            # Config data label
            current_sorting_by_date_data_label.config(text="Invalid \"From\" & \"To\" Date",
                                                      fg=Settings.chosen_invalid_text_color.get())
            return None
        # Only from date invalid
        if not from_date_valid and to_date_valid:
            # Configure from and to text labels foreground
            sort_date_date_interval_from_label.config(fg=Settings.chosen_text_color.get())
            sort_date_date_interval_to_label.config(fg=Settings.chosen_text_color.get())
            sort_date_invalid_interval_label.place_forget()
            # Place and place_forget relevant labels
            sort_date_invalid_from_date_label.place(relheight=.1, relwidth=.99, relx=.005, rely=.89)
            sort_date_invalid_to_date_label.place_forget()
            sort_date_invalid_from_and_to_date_label.place_forget()
            # Config data label
            current_sorting_by_date_data_label.config(text="Invalid \"From\" Date",
                                                      fg=Settings.chosen_invalid_text_color.get())
            return None
        # Only to date invalid
        if from_date_valid and not to_date_valid:
            # Configure from and to text labels foreground
            sort_date_date_interval_from_label.config(fg=Settings.chosen_text_color.get())
            sort_date_date_interval_to_label.config(fg=Settings.chosen_invalid_text_color.get())
            sort_date_invalid_interval_label.place_forget()
            sort_date_invalid_from_date_label.place_forget()
            # Place and place_forget relevant labels
            sort_date_invalid_to_date_label.place(relheight=.1, relwidth=.99, relx=.005, rely=.89)
            sort_date_invalid_from_and_to_date_label.place_forget()
            # Config data label
            current_sorting_by_date_data_label.config(text="Invalid \"To\" Date",
                                                      fg=Settings.chosen_invalid_text_color.get())
            return None
    else:
        # Configure from and to text labels foreground
        sort_date_date_interval_from_label.config(fg=Settings.chosen_text_color.get())
        sort_date_date_interval_to_label.config(fg=Settings.chosen_text_color.get())
        # Place and place_forget specific and interval labels while the "any" date option is selected
        sort_date_invalid_specific_label.place_forget()
        sort_date_invalid_interval_label.place_forget()
        sort_date_invalid_from_date_label.place_forget()
        sort_date_invalid_to_date_label.place_forget()
        sort_date_invalid_from_and_to_date_label.place_forget()
        # Config data label
        current_sorting_by_date_data_label.config(text=Composition.sort_by_date.get(),
                                                  fg=Settings.chosen_text_color.get())
        # Set invalid date sorting option to False
        Composition.is_invalid_date_sorting_option.set(False)


def sort_compositions_invalid_rating_selection():
    """Places or forgets the invalid selection label from composition sorting by rating
    Modifies the current sorting option label
    Sets the invalid option variable, which in turn enables or disables the proceed button
    """

    def config_sort_rating_checkbutton_fg_color(text_color: str):
        """Configures the fg color of the sort rating checkbuttons
        """
        sort_rating_no_rating_checkbutton.config(fg=text_color)
        sort_rating_1_star_checkbutton.config(fg=text_color)
        sort_rating_2_star_checkbutton.config(fg=text_color)
        sort_rating_3_star_checkbutton.config(fg=text_color)
        sort_rating_4_star_checkbutton.config(fg=text_color)
        sort_rating_5_star_checkbutton.config(fg=text_color)

    if Composition.sort_by_rating.get() == "Multiple":
        if not Composition.no_rating.get() and not Composition.star_1_rating.get() \
                and not Composition.star_2_rating.get() and not Composition.star_3_rating.get() \
                and not Composition.star_4_rating.get() and not Composition.star_5_rating.get():
            sort_rating_invalid_selection_label.place(relheight=.1, relwidth=.99, relx=.005, rely=.89)
            current_sorting_by_rating_data_label.config(text="Invalid Multiple Selection",
                                                        fg=Settings.chosen_invalid_text_color.get())
            config_sort_rating_checkbutton_fg_color(Settings.chosen_invalid_text_color.get())
            # Set invalid rating option to True
            Composition.is_invalid_rating_sorting_option.set(True)
        else:
            sort_rating_invalid_selection_label.place_forget()
            current_sorting_by_rating_data_label.config(text=Composition.sort_by_rating.get(),
                                                        fg=Settings.chosen_text_color.get())
            config_sort_rating_checkbutton_fg_color(Settings.chosen_button_text_color.get())
            # Set invalid rating option to False
            Composition.is_invalid_rating_sorting_option.set(False)
    else:
        sort_rating_invalid_selection_label.place_forget()
        current_sorting_by_rating_data_label.config(text=Composition.sort_by_rating.get(),
                                                    fg=Settings.chosen_text_color.get())
        config_sort_rating_checkbutton_fg_color(Settings.chosen_button_text_color.get())
        # Set invalid rating option to False
        Composition.is_invalid_rating_sorting_option.set(False)


def config_date_comboboxes_styles(target: str, given_style: str):
    """Changes the styles of the composition sorting comboboxes (by date)
    """
    if target == "Specific":
        sort_date_specific_date_day_combobox.config(style=given_style)
        sort_date_specific_date_month_combobox.config(style=given_style)
        sort_date_specific_date_year_combobox.config(style=given_style)
    elif target == "Interval From":
        # From ...
        sort_date_from_date_day_combobox.config(style=given_style)
        sort_date_from_date_month_combobox.config(style=given_style)
        sort_date_from_date_year_combobox.config(style=given_style)
    elif target == "Interval To":
        # ... to
        sort_date_to_date_day_combobox.config(style=given_style)
        sort_date_to_date_month_combobox.config(style=given_style)
        sort_date_to_date_year_combobox.config(style=given_style)
    else:  # target == "Register"
        birth_day_combobox.configure(style=given_style)
        birth_month_combobox.configure(style=given_style)
        birth_year_combobox.configure(style=given_style)


"""Composition-Sorting Related Functions"""


def add_all_usernames_to_listbox():
    """Adds all usernames to listbox
    """
    # First remove all list content
    sort_user_listbox.delete(first=0, last=END)
    # Then add every user; automatically in alphabetical order
    for index, username in enumerate(sort_user_choose_user_combobox["values"]):
        sort_user_listbox.insert(index, username)
    # Config buttons
    if combobox_values_match_listbox_values():
        sort_user_add_all_button.config(state=DISABLED)
    else:
        sort_user_add_all_button.config(state=NORMAL)
    if len(sort_user_listbox.get(first=0, last=END)):  # > 0
        sort_user_remove_all_button.config(state=NORMAL)
    else:
        sort_user_remove_all_button.config(state=DISABLED)
    sort_compositions_invalid_user_selection(Composition.sort_user_selected_user.get())
    check_if_selected_user_in_listbox(Composition.sort_user_selected_user.get())


def remove_all_usernames_from_listbox():
    """Removes all usernames from listbox
    """
    sort_user_listbox.delete(first=0, last=END)
    # Config buttons
    if combobox_values_match_listbox_values():
        sort_user_add_all_button.config(state=DISABLED)
    else:
        sort_user_add_all_button.config(state=NORMAL)
    if len(sort_user_listbox.get(first=0, last=END)):  # > 0
        sort_user_remove_all_button.config(state=NORMAL)
    else:
        sort_user_remove_all_button.config(state=DISABLED)
    sort_compositions_invalid_user_selection(Composition.sort_user_selected_user.get())
    check_if_selected_user_in_listbox(Composition.sort_user_selected_user.get())


def add_specific_username_to_listbox(username: str):
    """Adds given specific username to listbox
    """
    # Insert given username
    sort_user_listbox.insert(END, username)
    # Get all values from listbox
    listbox_values: list = sort_user_listbox.get(first=0, last=END)
    # Delete all values from listbox
    sort_user_listbox.delete(first=0, last=END)
    # Insert sorted values back into listbox
    sort_user_listbox.insert(END, *sorted(listbox_values))
    # Config buttons
    if combobox_values_match_listbox_values():
        sort_user_add_all_button.config(state=DISABLED)
    else:
        sort_user_add_all_button.config(state=NORMAL)
    if len(sort_user_listbox.get(first=0, last=END)):  # > 0
        sort_user_remove_all_button.config(state=NORMAL)
    else:
        sort_user_remove_all_button.config(state=DISABLED)
    sort_compositions_invalid_user_selection(Composition.sort_user_selected_user.get())
    check_if_selected_user_in_listbox(Composition.sort_user_selected_user.get())


def remove_selected_usernames_from_listbox():
    """Adds all usernames to listbox
    """
    index_list: list = sort_user_listbox.curselection()
    for index in reversed(index_list):
        sort_user_listbox.delete(index)
    # Config buttons
    if combobox_values_match_listbox_values():
        sort_user_add_all_button.config(state=DISABLED)
    else:
        sort_user_add_all_button.config(state=NORMAL)
    if len(sort_user_listbox.get(first=0, last=END)):  # > 0
        sort_user_remove_all_button.config(state=NORMAL)
    else:
        sort_user_remove_all_button.config(state=DISABLED)
    sort_compositions_invalid_user_selection(Composition.sort_user_selected_user.get())
    check_if_selected_user_in_listbox(Composition.sort_user_selected_user.get())


def check_if_selected_user_in_listbox(given_username: str):
    """Checks if the given user username is in multiple users listbox
    """
    if not valid_composer_name(given_username=given_username):
        sort_user_add_selected_button.config(state=DISABLED)
        return None
    for username in sort_user_listbox.get(first=0, last=END):
        if username == given_username:
            sort_user_add_selected_button.config(state=DISABLED)
            return None
    # If username was not in list, enable button
    sort_user_add_selected_button.config(state=NORMAL)


def combobox_values_match_listbox_values():
    """Returns True if values from combobox match listbox values; False otherwise
    """
    return set(sort_user_choose_user_combobox["values"]) == set(sort_user_listbox.get(first=0, last=END))


def valid_composer_name(given_username: str):
    """Checks if the given username is a composer's username; Returns boolean
    """
    for composer in Composition.composer_list:
        # Get necessary booleans one by one, for better readability
        if composer["Credentials"]["Username"] == given_username:
            name_match: bool = True
        else:
            name_match: bool = False
        if composer["Privacy"] in ("Public", "Private Details"):
            is_public: bool = True
        else:
            is_public: bool = False
        if composer["Credentials"]["Username"] == User.logged_in_user["Credentials"]["Username"]:
            is_logged_in_user: bool = True
        else:
            is_logged_in_user: bool = False
        # Evaluate final condition
        if name_match and (is_public or is_logged_in_user):
            return True
    # If username not found, return False
    return False


def populate_sorted_listbox():
    """Populates the Sorted Compositions listbox with the sorted compositions' titles
    """
    # If no compositions match the given sorting criteria, return None
    if not Composition.sorted_composition_list:
        proceed_to_play_button.config(state=DISABLED)
        # Config numbers frame
        sorted_compositions_total_data_label.config(text=Misc.format_number(value=Composition.
                                                                            get_number_of_eligible_compositions()))
        sorted_compositions_matching_data_label.config(text="0")
        return None
    # Clear previous listbox values
    sorted_compositions_listbox.delete(first=0, last=END)
    # Enable proceed button
    proceed_to_play_button.config(state=NORMAL)
    # Populate listbox with new values
    for composition in Composition.sorted_composition_list:
        sorted_compositions_listbox.insert(END, composition["Name"])
        for user_composition in User.logged_in_user["Compositions"]:
            if user_composition == composition:
                sorted_compositions_listbox.\
                    itemconfig(
                        index=END,
                        background=Settings.default_listbox_logged_user_composition_background_color
                        if Settings.chosen_background_color.get() == Settings.default_background_color
                        else Settings.get_color_variation(color=Settings.chosen_background_color.get(), factor=.875))
                # Factor < 1 => Shaded (darker) color ----------------------------------------------------------|||
    # Select one of the available listbox values
    if Composition.preselect_option.get() == "First":
        sorted_compositions_listbox.selection_set(first=0)
    elif Composition.preselect_option.get() == "Last":
        sorted_compositions_listbox.selection_set(first=END)
    else:  # Composition.preselect_option.get() == "Random":
        listbox_len: int = sorted_compositions_listbox.size()
        if listbox_len == 1:
            sorted_compositions_listbox.selection_set(first=0)
        else:
            random_selection: int = random.randint(0, listbox_len - 1)
            sorted_compositions_listbox.selection_set(first=random_selection)
            # Get composition name
    composition_name: str = sorted_compositions_listbox.get(sorted_compositions_listbox.curselection())
    Composition.composition_to_play_name.set(composition_name)
    config_sorted_menu(composition=Composition.get_composition_from_name(composition_name=composition_name))


def config_sorted_menu(composition: dict):
    """Configures the Sorted Compositions Menu
    """
    # Composer & Description frame
    for user in User.user_dict:
        for composition_iterator in User.user_dict[user]["Compositions"]:
            if composition["Name"] == composition_iterator["Name"]:
                Misc.copy_var_value_to_disabled_text_widget(text_text=User.user_dict[user]["Credentials"]["Username"],
                                                            text_widget=sorted_composer_scrolled_text)
    Misc.copy_var_value_to_disabled_text_widget(text_text=composition["Description"],
                                                text_widget=sorted_description_scrolled_text)
    # Notes & Delays frame
    notes_and_delays: str = "\n".join(Composition.get_composition_notes_and_delays(composition=composition))
    notes_and_delays += " - Last delay will not be used."
    Misc.copy_var_value_to_disabled_text_widget(text_text=notes_and_delays,
                                                text_widget=sorted_notes_and_delays_scrolled_text)
    Misc.copy_var_value_to_disabled_text_widget(text_text=Misc.format_duration(duration=composition["Length"],
                                                                               with_suggestion=False),
                                                text_widget=sorted_length_data_scrolled_text)
    # Ratings frame
    total_ratings: int = 0
    total_rating_points: int = 0
    total_potential_rating_points: int = 0

    for rating in composition["Rating"]:
        assert composition["Rating"][rating] >= 0
        total_ratings += composition["Rating"][rating]
        total_rating_points += int(rating) * composition["Rating"][rating]
        total_potential_rating_points += 5 * composition["Rating"][rating]

    if total_ratings:
        overall_rating: float = total_rating_points / total_ratings
    else:
        overall_rating: float = 0

    for rating in composition["Rating"]:
        if int(rating) == 5:
            sorted_5_star_bar.config(maximum=total_ratings)
            Composition.sorted_5_star_var.set(composition["Rating"][rating])
            sorted_5_star_data_label.config(text="{:.2f}%".format(Misc.get_percentage_by_part(
                part=composition["Rating"][rating], whole=total_ratings)) if composition["Rating"][rating] else "None")
        elif int(rating) == 4:
            sorted_4_star_bar.config(maximum=total_ratings)
            Composition.sorted_4_star_var.set(composition["Rating"][rating])
            sorted_4_star_data_label.config(text="{:.2f}%".format(Misc.get_percentage_by_part(
                part=composition["Rating"][rating], whole=total_ratings)) if composition["Rating"][rating] else "None")
        elif int(rating) == 3:
            sorted_3_star_bar.config(maximum=total_ratings)
            Composition.sorted_3_star_var.set(composition["Rating"][rating])
            sorted_3_star_data_label.config(text="{:.2f}%".format(Misc.get_percentage_by_part(
                part=composition["Rating"][rating], whole=total_ratings)) if composition["Rating"][rating] else "None")
        elif int(rating) == 2:
            sorted_2_star_bar.config(maximum=total_ratings)
            Composition.sorted_2_star_var.set(composition["Rating"][rating])
            sorted_2_star_data_label.config(text="{:.2f}%".format(Misc.get_percentage_by_part(
                part=composition["Rating"][rating], whole=total_ratings)) if composition["Rating"][rating] else "None")
        elif int(rating) == 1:
            sorted_1_star_bar.config(maximum=total_ratings)
            Composition.sorted_1_star_var.set(composition["Rating"][rating])
            sorted_1_star_data_label.config(text="{:.2f}%".format(Misc.get_percentage_by_part(
                part=composition["Rating"][rating], whole=total_ratings)) if composition["Rating"][rating] else "None")
        else:
            raise KeyError("Invalid Rating Key")

    black_star: str = "★"
    white_star: str = "☆"
    overall_rating_star_text: str = ""
    your_rating_star_text: str = ""

    # Create star string for overall rating
    for rating in range(1, 6):
        if overall_rating >= rating:
            overall_rating_star_text += black_star
        else:
            overall_rating_star_text += white_star

    # Overall Rating
    if overall_rating:
        sorted_overall_rating_data_label.\
            config(text=f"{overall_rating_star_text}\n{'{:.2f}'.format(overall_rating)} / 5")
    else:
        sorted_overall_rating_data_label.config(text=f"{overall_rating_star_text}\nNone")

    # Your Rating
    is_rated: bool = False
    for given_rating in User.logged_in_user["Given Ratings"]:
        assert type(given_rating) == dict
        if given_rating.get(composition["Name"]) is not None:
            # Create star string for your rating
            for rating in range(1, 6):
                if given_rating[composition["Name"]] >= rating:
                    your_rating_star_text += black_star
                else:
                    your_rating_star_text += white_star
            sorted_your_rating_data_label.\
                config(text=f"{your_rating_star_text}\n{given_rating[composition['Name']]} / 5")
            Composition.given_rating.set(your_rating_star_text)
            is_rated = True
            break
    if not is_rated:
        sorted_your_rating_data_label.config(text=f"{white_star * 5}\n{'None'}")
        Composition.given_rating.set(Misc.NO_RATING)

    # Miscellaneous frame
    assert composition["Played"] >= 0

    time_or_times: str = "Time" if composition["Played"] == 1 else "Times"
    sorted_times_played_data_label.config(text=f"{Misc.format_number(value=composition['Played'])} {time_or_times}")
    sorted_date_of_creation_data_label.config(text=Misc.format_date(year=composition["Date Of Creation"]["Year"],
                                                                    month=composition["Date Of Creation"]["Month"],
                                                                    day=composition["Date Of Creation"]["Day"],
                                                                    with_day=True))
    Misc.copy_var_value_to_disabled_text_widget(text_text=str(total_ratings),
                                                text_widget=sorted_total_ratings_scrolled_text)
    Misc.copy_var_value_to_disabled_text_widget(text_text=f"{Misc.format_number(value=total_rating_points)} / "
                                                          f"{Misc.format_number(value=total_potential_rating_points)}",
                                                text_widget=sorted_current_maximum_rating_scrolled_text)

    # Numbers frame
    sorted_compositions_total_data_label.\
        config(text=Misc.format_number(value=Composition.get_number_of_eligible_compositions()))
    sorted_compositions_matching_data_label.\
        config(text=Misc.format_number(value=len(Composition.sorted_composition_list)))


def config_current_rating_label():
    """Configures the current given rating label
    """
    if Composition.given_rating.get() == "None":
        text: str = "N/A"
    elif Composition.given_rating.get() == Misc.STAR_1:
        text: str = "1 / 5"
    elif Composition.given_rating.get() == Misc.STAR_2:
        text: str = "2 / 5"
    elif Composition.given_rating.get() == Misc.STAR_3:
        text: str = "3 / 5"
    elif Composition.given_rating.get() == Misc.STAR_4:
        text: str = "4 / 5"
    elif Composition.given_rating.get() == Misc.STAR_5:
        text: str = "5 / 5"
    else:
        raise ValueError
    rate_composition_current_label.config(text=text)


def config_composition_table_and_composer_labels():
    """Configures the composition title and composition author labels
    """
    composition_to_play_name_label.config(text=Composition.composition_to_play["Name"])
    for user in User.user_dict:
        for composition in User.user_dict[user]["Compositions"]:
            if composition["Name"] == Composition.composition_to_play["Name"]:
                gender_txt: str = ""
                if User.user_dict[user]["Gender"] == "Male":
                    gender_txt = "Mr. "
                elif User.user_dict[user]["Gender"] == "Female":
                    gender_txt = "Ms. "
                name_txt: str = f"{gender_txt}{User.user_dict[user]['Credentials']['Username']}"
                composition_to_play_composer_name_label.config(text=f"By {name_txt}")
                break


"""Set Composition Sorting Variables"""


Composition.sort_by_user.set("Any")
Composition.sort_by_length.set("Any")
Composition.sort_by_date.set("Any")
Composition.sort_by_rating.set("Any")

Composition.given_rating.set(Misc.POSSIBLE_RATINGS[0])


"""Packed Trace Functions"""


def config_date_selection_comboboxes(var: StringVar, target: str,
                                     day_var: StringVar, month_var: StringVar, year_var: StringVar):
    """Configures all the necessary elements of date selection comboboxes
    """
    # Clear any whitespace present in input variable
    Misc.clear_white_spaces(var)
    if var is day_var:
        len_limit: int = 2
        Misc.clear_non_digits(var)
    elif var is year_var:
        len_limit: int = 4
        Misc.clear_non_digits(var)
    else:  # var is month_var
        len_limit: int = 10
        Misc.clear_non_letters(var)
        var.set(var.get().title())
    # Set input variable length limit
    Misc.entry_character_length_limit(var=var, amount=len_limit)
    if Misc.is_valid_date(year=year_var.get(),
                          month=month_var.get(),
                          day=day_var.get()):
        config_date_comboboxes_styles(target=target, given_style="TCombobox")
    else:
        config_date_comboboxes_styles(target=target, given_style="Error.TCombobox")


"""Bind command(s) to root window"""


def check_if_listbox_item_selected():
    """Checks if any listbox item is selected
    Used to change the state of the "Remove Selected" button
    """
    if len(sort_user_listbox.curselection()) > 0:
        sort_user_remove_selected_button.config(state=NORMAL)
    else:
        sort_user_remove_selected_button.config(state=DISABLED)


root.bind("<ButtonRelease>", lambda *args: check_if_listbox_item_selected())
check_if_listbox_item_selected()


"""GUI Display Functions"""


def display_main_menu():
    """Displays the Main Menu
    """

    forget_all_widgets(root)
    root.focus()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    music_by_jurj_label.place(relheight=.05, relwidth=.15, relx=.01, rely=.015)

    main_menu_label.place(relheight=0.15, relwidth=0.5, relx=0.25, rely=.075)

    rely: float = .25

    play_freely_button.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=rely)

    record_composition_button.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=rely + .08)

    playback_composition_button.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=rely + .08 * 2)

    # TODO
    # composition_manager_button.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=rely + .08 * 3)

    settings_button.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=rely + .08 * 3)

    stats_button.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=rely + .08 * 4)

    if User.is_logged_in:
        logged_in_user_username_label.config(text=f"Logged in user: {User.logged_in_user['Credentials']['Username']}")
        go_to_logout_button.place(relheight=0.05, relwidth=0.1, relx=0.375, rely=rely + .08 * 5)
        go_to_profile_button.place(relheight=0.05, relwidth=0.1, relx=0.525, rely=rely + .08 * 5)
        logged_in_user_username_label.place(relheight=0.05, relwidth=0.8, relx=0.1, rely=rely + .08 * 6)
        remember_me_checkbutton.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=rely + .08 * 7 - .025)
    else:
        go_to_login_button.place(relheight=0.05, relwidth=0.1, relx=0.375, rely=rely + .08 * 5)
        go_to_register_button.place(relheight=0.05, relwidth=0.1, relx=0.525, rely=rely + .08 * 5)

    Stats.app_used_label.place(relheight=.05, relwidth=.975, relx=.0125, rely=.925)


def display_new_composition_id_card():
    """Displays the Create New Composition Menu
    """

    users_next_composition_number: int = len(User.logged_in_user["Compositions"]) + 1

    new_composition_number_label.config(text=f"This would be your {users_next_composition_number}"
                                             f"{Misc.get_suffix(users_next_composition_number)} composition!")
    new_composition_composer_data_label.config(text=User.logged_in_user["Credentials"]["Username"])

    forget_all_widgets(root)
    root.focus()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    record_new_composition_label.place(relheight=0.125, relwidth=0.8, relx=0.1, rely=0.05)

    new_composition_intro_label.place(relheight=0.05, relwidth=0.975, relx=0.0125, rely=0.21)
    new_composition_number_label.place(relheight=0.05, relwidth=0.975, relx=0.0125, rely=0.26)

    new_composition_labelframe.place(relheight=0.51, relwidth=0.8, relx=0.1, rely=0.32)

    new_composition_composer_label.place(relheight=0.05, relwidth=0.2, relx=0.11, rely=0.37)
    new_composition_composer_data_label.place(relheight=0.05, relwidth=0.57, relx=0.32, rely=0.37)

    new_composition_name_label.place(relheight=0.05, relwidth=0.2, relx=0.11, rely=0.44)
    new_composition_name_entry.place(relheight=0.05, relwidth=0.555, relx=0.32, rely=0.44)
    new_composition_name_help_label.place(relheight=0.02, relwidth=0.555, relx=0.32, rely=0.49)

    new_composition_description_label.place(relheight=0.075, relwidth=0.2, relx=0.11, rely=0.52)
    new_composition_description_text.place(relheight=0.235, relwidth=0.555, relx=0.32, rely=0.52)
    new_composition_description_length_label.place(relheight=0.03, relwidth=0.555, relx=0.32, rely=0.7575)

    go_to_save_composition_button.place(relheight=0.05, relwidth=0.2, relx=0.325, rely=0.9)
    start_recording_button.place(relheight=0.05, relwidth=0.2, relx=0.55, rely=0.9)

    if Composition.at_least_1_note_recorded.get():
        abandon_composition_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)
    else:
        new_composition_input_warning_label.place(relheight=0.035, relwidth=0.78, relx=0.11, rely=0.79)
        return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)


def display_choose_instrument():
    """Displays the Choose Instrument Menu to record composition
    """

    forget_all_widgets(root)
    root.focus()

    config_about_chosen_instrument_text(Sounds.chosen_instrument.get())

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    if Composition.is_recording_composition.get():
        record_composition_label.place(relheight=0.125, relwidth=0.8, relx=0.1, rely=0.05)

        go_to_save_composition_button.place(relheight=0.05, relwidth=0.2, relx=0.55, rely=0.825)
        return_to_composition_id_card_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.825)
    else:
        play_freely_label.place(relheight=0.125, relwidth=0.8, relx=0.1, rely=0.05)

    choose_instrument_separator_1.place(relheight=0.0001, relwidth=0.3, relx=0.075, rely=0.26)
    choose_instrument_separator_2.place(relheight=0.0001, relwidth=0.301, relx=0.624, rely=0.26)

    choose_instrument_labelframe.place(relheight=0.15, relwidth=0.25, relx=0.375, rely=0.2)
    choose_instrument_option_menu.place(relheight=0.06, relwidth=0.2, relx=0.4, rely=0.26)

    choose_instrument_separator_3.place(relheight=0.0001, relwidth=0.25, relx=0.1, rely=0.385)
    choose_instrument_separator_4.place(relheight=0.0001, relwidth=0.25, relx=0.65, rely=0.385)

    about_chosen_instrument_label.place(relheight=0.05, relwidth=0.275, relx=0.3625, rely=0.36)
    about_chosen_instrument_text.place(relheight=0.225, relwidth=0.8, relx=0.1, rely=0.42)

    choose_instrument_separator_5.place(relheight=0.5, relwidth=0.0001, relx=0.075, rely=0.26)
    choose_instrument_separator_6.place(relheight=0.5, relwidth=0.0001, relx=0.925, rely=0.26)

    choose_instrument_separator_7.place(relheight=0.0001, relwidth=0.175, relx=0.075, rely=0.76)
    choose_instrument_separator_8.place(relheight=0.0001, relwidth=0.1765, relx=0.749, rely=0.76)

    available_notes_labelframe.place(relheight=0.15, relwidth=0.5, relx=0.25, rely=0.66)

    play_instrument_button.place(relheight=0.05, relwidth=0.2, relx=0.55, rely=0.9)

    return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)

    if Composition.is_recording_composition.get() and Composition.at_least_1_note_recorded.get():
        abandon_composition_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)
    else:
        return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)


def display_play_notes(instrument: str):
    """Displays one of the 2 play notes menus - Play Freely or Record Composition
    """

    forget_all_widgets(root)
    root.focus()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    currently_playing_label.config(text=f"Currently Playing: {Sounds.chosen_instrument.get()}")

    if Composition.is_recording_composition.get():
        record_composition_label.place(relheight=0.125, relwidth=0.8, relx=0.1, rely=0.05)

        currently_playing_label.place(relheight=0.05, relwidth=0.3, relx=0.35, rely=0.195)

        last_note_played_record_label.place(relheight=0.05, relwidth=0.925, relx=0.05, rely=0.45)

        composition_length_label.place(relheight=0.05, relwidth=0.945, relx=0.05, rely=0.5)

        number_of_notes_played_record_labelframe.place(relheight=0.26, relwidth=0.925, relx=0.05, rely=0.55)

        number_of_piano_notes_played_record_label.place(relheight=0.05, relwidth=0.9, relx=0.06, rely=0.6)
        number_of_flute_notes_played_record_label.place(relheight=0.05, relwidth=0.9, relx=0.06, rely=0.65)
        number_of_trumpet_notes_played_record_label.place(relheight=0.05, relwidth=0.9, relx=0.06, rely=0.7)
        number_of_violin_notes_played_record_label.place(relheight=0.05, relwidth=0.9, relx=0.06, rely=0.75)

        delay_label.place(relheight=0.075, relwidth=0.1, relx=0.025, rely=0.825)
        delay_scale.place(relheight=0.1, relwidth=0.4, relx=0.125, rely=0.821)
        delay_star_label.place(relheight=0.05, relwidth=0.475, relx=0.05, rely=0.921)

        go_to_save_composition_button.place(relheight=0.05, relwidth=0.2, relx=0.55, rely=0.825)
        return_to_composition_id_card_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.825)

        if Composition.at_least_1_note_recorded.get():
            abandon_composition_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)
        else:
            return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)
    else:
        play_freely_label.place(relheight=0.125, relwidth=0.8, relx=0.1, rely=0.05)

        currently_playing_label.place(relheight=0.05, relwidth=0.3, relx=0.35, rely=0.225)

        last_note_played_freely_label.place(relheight=0.05, relwidth=0.925, relx=0.05, rely=0.5)

        number_of_notes_played_freely_labelframe.place(relheight=0.26, relwidth=0.925, relx=0.05, rely=0.575)

        number_of_piano_notes_played_freely_label.place(relheight=0.05, relwidth=0.9, relx=0.06, rely=0.625)
        number_of_flute_notes_played_freely_label.place(relheight=0.05, relwidth=0.9, relx=0.06, rely=0.675)
        number_of_trumpet_notes_played_freely_label.place(relheight=0.05, relwidth=0.9, relx=0.06, rely=0.725)
        number_of_violin_notes_played_freely_label.place(relheight=0.05, relwidth=0.9, relx=0.06, rely=0.775)

        reset_note_count_button.place(relheight=0.05, relwidth=0.2, relx=0.05, rely=0.9)

        return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)

    return_to_choose_instrument_button.place(relheight=0.05, relwidth=0.2, relx=0.55, rely=0.9)

    if instrument == "Piano":

        button_size: float = 0.1
        if Composition.is_recording_composition.get():
            rely: float = 0.275
        else:
            rely: float = 0.3

        do_1_button.place(relheight=button_size, relwidth=button_size, relx=0.1, rely=rely)
        re_button.place(relheight=button_size, relwidth=button_size, relx=0.2, rely=rely)
        mi_button.place(relheight=button_size, relwidth=button_size, relx=0.3, rely=rely)
        fa_button.place(relheight=button_size, relwidth=button_size, relx=0.4, rely=rely)
        sol_button.place(relheight=button_size, relwidth=button_size, relx=0.5, rely=rely)
        la_button.place(relheight=button_size, relwidth=button_size, relx=0.6, rely=rely)
        si_button.place(relheight=button_size, relwidth=button_size, relx=0.7, rely=rely)
        do_2_button.place(relheight=button_size, relwidth=button_size, relx=0.8, rely=rely)

        note_length_label.place(relheight=0.05, relwidth=0.15, relx=0.35, rely=rely + 0.125)

        short_note_radiobutton.place(relheight=0.05, relwidth=0.1, relx=0.5, rely=rely + 0.125)
        long_note_radiobutton.place(relheight=0.05, relwidth=0.1, relx=0.6, rely=rely + 0.125)

    elif instrument == "Flute":

        button_size: float = 0.125
        if Composition.is_recording_composition.get():
            rely: float = 0.3
        else:
            rely: float = 0.325

        c4_button.place(relheight=button_size, relwidth=button_size, relx=0.125, rely=rely)
        c5_button.place(relheight=button_size, relwidth=button_size, relx=0.25, rely=rely)
        c6_button.place(relheight=button_size, relwidth=button_size, relx=0.375, rely=rely)
        g4_button.place(relheight=button_size, relwidth=button_size, relx=0.5, rely=rely)
        g5_button.place(relheight=button_size, relwidth=button_size, relx=0.625, rely=rely)
        g6_button.place(relheight=button_size, relwidth=button_size, relx=0.75, rely=rely)

    elif instrument == "Trumpet":

        button_size: float = 0.125
        if Composition.is_recording_composition.get():
            rely: float = 0.3
        else:
            rely: float = 0.325

        c4_button.place(relheight=button_size, relwidth=button_size, relx=0.125, rely=rely)
        c5_button.place(relheight=button_size, relwidth=button_size, relx=0.25, rely=rely)
        c6_button.place(relheight=button_size, relwidth=button_size, relx=0.375, rely=rely)
        g3_button.place(relheight=button_size, relwidth=button_size, relx=0.5, rely=rely)
        g4_button.place(relheight=button_size, relwidth=button_size, relx=0.625, rely=rely)
        g5_button.place(relheight=button_size, relwidth=button_size, relx=0.75, rely=rely)

    elif instrument == "Violin":

        button_size: float = 0.125
        if Composition.is_recording_composition.get():
            rely: float = 0.3
        else:
            rely: float = 0.325

        c4_button.place(relheight=button_size, relwidth=button_size, relx=0.125, rely=rely)
        c5_button.place(relheight=button_size, relwidth=button_size, relx=0.25, rely=rely)
        c6_button.place(relheight=button_size, relwidth=button_size, relx=0.375, rely=rely)
        g4_button.place(relheight=button_size, relwidth=button_size, relx=0.5, rely=rely)
        g5_button.place(relheight=button_size, relwidth=button_size, relx=0.625, rely=rely)
        g6_button.place(relheight=button_size, relwidth=button_size, relx=0.75, rely=rely)


def display_abandon_composition():
    """Displays the Abandon Composition Menu
    """

    forget_all_widgets(root)
    root.focus()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    abandon_composition_label.place(relheight=0.125, relwidth=0.85, relx=0.075, rely=0.05)

    sure_abandon_composition_label.place(relheight=0.15, relwidth=0.9, relx=0.05, rely=0.3)

    abandon_composition_labelframe.place(relheight=0.275, relwidth=0.6, relx=0.2, rely=0.5)

    abandon_composition_return_to_composition_id_card_button.place(relheight=0.075, relwidth=0.25, relx=0.225,
                                                                   rely=0.575)
    abandon_composition_save_composition_button.place(relheight=0.075, relwidth=0.25, relx=0.525, rely=0.575)

    yes_abandon_composition_button.place(relheight=0.075, relwidth=0.325, relx=0.3375, rely=0.675)


def display_save_composition():
    """Displays the Save Composition Menu
    """

    forget_all_widgets(root)
    root.focus()

    config_save_composition_labels_and_text()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    save_composition_menu_label.place(relheight=0.125, relwidth=0.85, relx=0.075, rely=0.05)

    save_composition_intro_label.place(relheight=0.05, relwidth=0.9, relx=0.05, rely=0.185)

    save_composition_labelframe.place(relheight=0.64, relwidth=0.9, relx=0.05, rely=0.235)

    # Constants
    relheight: float = .05
    relx: float = .0525
    rely: float = .285

    save_composition_composer_label.place(relheight=relheight, relwidth=0.2, relx=relx, rely=rely)
    save_composition_composer_text.place(relheight=relheight - .005, relwidth=0.6885,
                                         relx=relx + .2, rely=rely + .0025)

    save_composition_name_label.place(relheight=relheight, relwidth=0.2, relx=relx, rely=rely + relheight)
    save_composition_name_text.place(relheight=relheight - .005, relwidth=0.6885,
                                     relx=relx + .2, rely=rely + relheight + .0025)

    save_composition_description_label.place(relheight=relheight, relwidth=0.2,
                                             relx=relx, rely=rely + relheight * 2)
    save_composition_description_text.place(relheight=relheight * 3 - .005, relwidth=0.6885,
                                            relx=relx + .2, rely=rely + relheight * 2 + .0025)
    save_composition_description_length_label.place(relheight=relheight * 2, relwidth=0.2,
                                                    relx=relx, rely=rely + relheight * 3)

    save_composition_separator.place(relheight=0.001, relwidth=0.8995,
                                     relx=0.05, rely=rely + relheight * 5 + 0.002)

    save_composition_composition_length_label.place(relheight=relheight, relwidth=0.2,
                                                    relx=relx, rely=rely + relheight * 5 + 0.005)
    save_composition_composition_length_text.place(relheight=relheight - .005, relwidth=0.6885,
                                                   relx=relx + .2, rely=rely + relheight * 5 + .0075)

    save_composition_notes_and_delays_label.place(relheight=relheight, relwidth=0.2,
                                                  relx=relx, rely=rely + relheight * 6 + 0.005)
    save_composition_notes_and_delays_text.place(relheight=relheight * 4.2, relwidth=0.6885,
                                                 relx=relx + .2, rely=rely + relheight * 6 + .0075)

    save_composition_button.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=0.81)

    save_composition_back_label.place(relheight=0.05, relwidth=0.9, relx=0.05, rely=0.875)

    return_to_composition_id_card_button.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=0.925)


def display_saved_composition():
    """Displays the Saved Composition Menu
    """

    forget_all_widgets(root)
    root.focus()

    # Create label texts
    # Number values
    total_composers_count: int = len(Composition.composer_list)
    public_composers_count: int = len([_ for _ in Composition.composer_list  # _ represents a composer dict
                                       if _["Privacy"] in ("Public", "Private Details")])
    private_composers_count: int = total_composers_count - public_composers_count
    non_composers_count: int = User.user_count - total_composers_count

    # Determine logged_in_user's privacy option
    you_public_composer: bool = False
    if User.logged_in_user["Privacy"] in ("Public", "Private Details"):
        you_public_composer = True
    # Create user location mention str with determined boolean
    you_public, you_private = (" You are in here.", "") if you_public_composer else ("", " You are in here.")

    # Do some assertions to show that I'm a good programmer
    assert total_composers_count > 0
    assert public_composers_count >= 0
    assert private_composers_count >= 0
    assert non_composers_count >= 0
    # Enough assertions :)

    # Total composers
    if total_composers_count > 1:
        one_of_many_text: str = f"You are 1 of {Misc.format_number(value=total_composers_count)} proud composers!"
    else:  # total_composers_count == 1
        one_of_many_text: str = f"You are the first user to be a composer!"

    # Public composers
    # Grammatical form(s)
    has_or_have: str = "have" if public_composers_count > 1 else "has"
    if public_composers_count > 0:
        public_number_text: str = f"{Misc.format_number(value=public_composers_count)} of them {has_or_have} " \
                                  f"public compositions!{you_public}"
    else:  # public_composers_count == 0
        public_number_text: str = f"None of them have public compositions..."

    # Private composers
    # Grammatical form(s)
    has_or_have: str = "have" if private_composers_count > 1 else "has"
    if private_composers_count > 0:
        private_number_text: str = f"{Misc.format_number(value=private_composers_count)} of them {has_or_have} " \
                                   f"private compositions...{you_private}"
    else:  # private_composers_count == 0
        private_number_text: str = f"None of them have private compositions!"

    # Non-composers
    # Grammatical forms
    plural_s, has_or_have = ("s", "have") if non_composers_count > 1 else ("", "has")
    if User.user_count > total_composers_count:
        left_to_join_text: str = f"{Misc.format_number(value=non_composers_count)} user{plural_s} {has_or_have} " \
                                 f"yet to compose at least 1 masterpiece!"
    elif User.user_count == total_composers_count and total_composers_count == 1:
        left_to_join_text: str = f"And also the only user... Hopefully others will join soon!"
    else:  # (User.user_count == total_composers_count) > 1
        left_to_join_text: str = f"Every user has at least 1 masterpiece bound to their account!"

    # Config labels with generated texts
    saved_composition_one_of_many_label.config(text=one_of_many_text)
    saved_composition_public_label.config(text=public_number_text)
    saved_composition_private_label.config(text=private_number_text)
    saved_composition_left_to_join_label.config(text=left_to_join_text)

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    saved_composition_menu_label.place(relheight=0.125, relwidth=0.85, relx=0.075, rely=0.05)

    saved_composition_intro_labelframe.place(relheight=0.5, relwidth=0.95, relx=0.025, rely=0.25)

    if total_composers_count > 1:
        saved_composition_one_of_many_label.place(relheight=0.25, relwidth=1)
        saved_composition_public_label.place(relheight=0.25, relwidth=1, rely=0.25)
        saved_composition_private_label.place(relheight=0.25, relwidth=1, rely=0.5)
        saved_composition_left_to_join_label.place(relheight=0.25, relwidth=1, rely=0.75)
    else:  # total_composers_count == 1
        saved_composition_one_of_many_label.place(relheight=0.5, relwidth=1)
        saved_composition_left_to_join_label.place(relheight=0.5, relwidth=1, rely=0.5)

    return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=0.8)


def display_playback_composition_sort():
    """Displays the Playback Composition Sorting Menu
    """

    forget_all_widgets(root)
    root.focus()

    playback_composition_menu_label.place(relheight=.125, relwidth=.85, relx=.075, rely=.05)

    playback_composition_labelframe.place(relheight=.715, relwidth=.9, relx=.05, rely=.175)

    sort_criteria_notebook.place(relheight=.7, relwidth=.99, relx=.005, rely=.01)

    """Sort by User Frame"""

    display_sort_by_user_frame()

    """Sort by Composition Length Frame"""

    display_sort_by_composition_length()

    """Sort by Date Frame"""

    display_sort_by_date()

    """Sort by Rating Frame"""

    display_sort_by_rating()

    """Current Sorting Parameters Label, Separators & Frame"""

    display_current_sorting_parameters()

    # Preselect Frame
    preselect_composition_frame.place(relheight=.05, relwidth=.475, relx=.05, rely=.9)

    preselect_composition_label.place(relheight=1, relwidth=.375)
    preselect_first_radiobutton.place(relheight=1, relwidth=.208333, relx=.375)
    preselect_last_radiobutton.place(relheight=1, relwidth=.208333, relx=.375 + .208333)
    preselect_random_radiobutton.place(relheight=1, relwidth=.208333, relx=.375 + .208333 * 2)

    # Proceed Button
    proceed_to_sorted_button.place(relheight=.05, relwidth=.2, relx=.55, rely=.9)

    quit_button.place(relheight=.05, relwidth=.05, relx=.925, rely=.05)

    return_to_main_menu_button.place(relheight=.05, relwidth=.2, relx=.775, rely=.9)


def display_playback_composition_sorted():
    """Displays the Sorted Compositions Menu
    """
    Composition.is_in_sorted_menu.set(True)

    forget_all_widgets(root)
    root.focus()

    playback_composition_menu_label.place(relheight=0.125, relwidth=0.85, relx=0.075, rely=0.05)

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    sorted_compositions_labelframe.place(relheight=.6, relwidth=.975, relx=.0125, rely=.2)

    if not Composition.sorted_composition_list:
        # Place_forget the content frame
        sorted_compositions_content_frame.place_forget()
        # Place the no match label
        sorted_no_match_label.place(relheight=.9, relwidth=.9, relx=.05, rely=.05)
    else:
        # Place_forget the no match label
        sorted_no_match_label.place_forget()
        # Content frame
        sorted_compositions_content_frame.place(relheight=.95, relwidth=.975, relx=.0125, rely=.025)
        sorted_compositions_separator.place(relheight=1, relwidth=.0001, relx=.5)
        # Left side of separator
        sorted_compositions_listbox.place(relheight=.95, relwidth=.465, relx=.0125, rely=.025)
        sorted_compositions_listbox_scroll_bar.place(relheight=.95, relwidth=.01, relx=.0125 + .465, rely=.025)
        # Right side of separator
        sorted_compositions_right_frame.place(relheight=.95, relwidth=.475, relx=.5125, rely=.025)
        sorted_compositions_about_label.place(relheight=.1, relwidth=1)
        sorted_compositions_notebook.place(relheight=.9, relwidth=1, rely=.1)
        # Composer & Description
        sorted_composer_labelframe.place(relheight=.3, relwidth=.975, relx=.0125)
        sorted_composer_scrolled_text.place(relheight=.9, relwidth=.975, relx=.0125, rely=.05)
        sorted_description_labelframe.place(relheight=.675, relwidth=.975, relx=.0125, rely=.3)
        sorted_description_scrolled_text.place(relheight=.95, relwidth=.975, relx=.0125, rely=.025)
        # Notes & Delays
        sorted_notes_and_delays_labelframe.place(relheight=.7, relwidth=.975, relx=.0125)
        sorted_notes_and_delays_scrolled_text.place(relheight=.95, relwidth=.975, relx=.0125, rely=.025)
        sorted_length_labelframe.place(relheight=.275, relwidth=.975, relx=.0125, rely=.7)
        sorted_length_data_scrolled_text.place(relheight=.9, relwidth=.975, relx=.0125, rely=.05)
        # Ratings
        sorted_ratings_labelframe.place(relheight=.6, relwidth=.975, relx=.0125)

        sorted_5_star_rating_label.place(relwidth=.225, relheight=.2)
        sorted_4_star_rating_label.place(relwidth=.225, relheight=.2, rely=.2)
        sorted_3_star_rating_label.place(relwidth=.225, relheight=.2, rely=.4)
        sorted_2_star_rating_label.place(relwidth=.225, relheight=.2, rely=.6)
        sorted_1_star_rating_label.place(relwidth=.225, relheight=.2, rely=.8)

        sorted_5_star_bar.place(relwidth=.55, relheight=.175, relx=.225, rely=.0125)
        sorted_4_star_bar.place(relwidth=.55, relheight=.175, relx=.225, rely=.2125)
        sorted_3_star_bar.place(relwidth=.55, relheight=.175, relx=.225, rely=.4125)
        sorted_2_star_bar.place(relwidth=.55, relheight=.175, relx=.225, rely=.6125)
        sorted_1_star_bar.place(relwidth=.55, relheight=.175, relx=.225, rely=.8125)

        sorted_5_star_data_label.place(relwidth=.225, relheight=.2, relx=.775)
        sorted_4_star_data_label.place(relwidth=.225, relheight=.2, relx=.775, rely=.2)
        sorted_3_star_data_label.place(relwidth=.225, relheight=.2, relx=.775, rely=.4)
        sorted_2_star_data_label.place(relwidth=.225, relheight=.2, relx=.775, rely=.6)
        sorted_1_star_data_label.place(relwidth=.225, relheight=.2, relx=.775, rely=.8)

        sorted_overall_rating_labelframe.place(relheight=.375, relwidth=.475, relx=.0125, rely=.6)
        sorted_overall_rating_data_label.place(relheight=1, relwidth=1)

        sorted_your_rating_labelframe.place(relheight=.375, relwidth=.475, relx=.0125 + .025 + .475, rely=.6)
        sorted_your_rating_data_label.place(relheight=1, relwidth=1)

        # Miscellaneous
        sorted_times_played_labelframe.place(relheight=.3, relwidth=.975, relx=.0125)
        sorted_times_played_data_label.place(relheight=.9, relwidth=.975, relx=.0125, rely=.05)

        sorted_date_of_creation_labelframe.place(relheight=.3, relwidth=.975, relx=.0125, rely=.3)
        sorted_date_of_creation_data_label.place(relheight=.95, relwidth=.975, relx=.0125, rely=.025)

        sorted_total_ratings_labelframe.place(relheight=.375, relwidth=.975, relx=.0125, rely=.6)

        sorted_total_ratings_label.place(relheight=.375, relwidth=.4875, rely=.025)
        sorted_ratings_colon_label_1.place(relheight=.375, relwidth=.025, relx=.4875, rely=.025)
        sorted_total_ratings_scrolled_text.place(relheight=.375, relwidth=.455, relx=.5325, rely=.025)

        sorted_current_maximum_rating_label.place(relheight=.6, relwidth=.4875, rely=.4)
        sorted_ratings_colon_label_2.place(relheight=.6, relwidth=.025, relx=.4875, rely=.4)
        sorted_current_maximum_rating_scrolled_text.place(relheight=.55, relwidth=.455, relx=.5325, rely=.425)

    # Numbers frame
    sorted_compositions_numbers_frame.place(relheight=.125, relwidth=.5125, relx=.0125, rely=.825)

    sorted_compositions_total_label.place(relheight=.5, relwidth=.6)
    sorted_compositions_total_data_label.place(relheight=.5, relwidth=.4, relx=.6)

    sorted_compositions_matching_label.place(relheight=.5, relwidth=.6, rely=.5)
    sorted_compositions_matching_data_label.place(relheight=.5, relwidth=.4, relx=.6, rely=.5)

    # Buttons

    proceed_to_play_button.place(relheight=0.05, relwidth=0.2, relx=0.55, rely=0.865)

    return_to_composition_sorting_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.825)

    return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)


def display_playback_composition():
    """Displays the Playback Composition Menu
    """
    Composition.is_in_start_playback_menu.set(True)

    forget_all_widgets(root)
    root.focus()

    playback_composition_menu_label.place(relheight=.125, relwidth=.85, relx=.075, rely=.05)

    quit_button.place(relheight=.05, relwidth=.05, relx=.925, rely=.05)

    composition_to_play_name_label.place(relheight=.11, relwidth=.965, relx=.0175, rely=.1975)
    composition_to_play_composer_name_label.place(relheight=.075, relwidth=.965, relx=.0175, rely=.31)

    Composition.start_stop_playing_button_frame.place(relheight=.1, relwidth=.3, relx=.35, rely=.3875)
    Composition.start_playing_button.place(**Composition.start_stop_button_positions)

    Composition.idle_playing_label.place(**Composition.start_stop_label_positions)

    Composition.playback_composition_progressbar.place(relheight=.05, relwidth=.9, relx=.05, rely=.675)

    rate_composition_labelframe.place(relheight=.145, relwidth=.5, relx=.025, rely=.8055)

    rate_composition_content_frame.place(relheight=.9, relwidth=.975, relx=.0125, rely=.05)

    rate_composition_given_label.place(relheight=1, relwidth=.45)
    rate_composition_option_menu.place(relheight=.8, relwidth=.355, relx=.45, rely=.1)
    rate_composition_current_label.place(relheight=1, relwidth=.195, relx=.45 + .355)

    return_to_main_menu_button.place(relheight=.05, relwidth=.2, relx=.775, rely=.9)

    return_to_composition_sorting_button.place(relheight=.05, relwidth=.2, relx=.775, rely=.825)

    return_to_composition_sorted_button.place(relheight=.05, relwidth=.2, relx=.55, rely=.865)

    # Place separators
    # Top part
    playback_separator_1.place(relheight=.0001, relwidth=.97505, relx=.0125, rely=.1825)
    playback_separator_2.place(relheight=.425 - .1825, relwidth=.0001, relx=.0125, rely=.1825)
    playback_separator_3.place(relheight=.425 - .1825, relwidth=.0001, relx=.9875, rely=.1825)
    playback_separator_4.place(relheight=.0001, relwidth=.35 - .0125, relx=.0125, rely=.425)
    playback_separator_5.place(relheight=.0001, relwidth=.3505 - .0125, relx=.0125 + .35 - .0125 + .3, rely=.425)
    # Bottom part
    playback_separator_6.place(relheight=.0001, relwidth=.325, relx=.025, rely=.45)
    playback_separator_7.place(relheight=.0001, relwidth=.325, relx=.025 + .325 + .3, rely=.45)
    playback_separator_8.place(relheight=.315, relwidth=.0001, relx=.975, rely=.45)
    playback_separator_9.place(relheight=.315, relwidth=.0001, relx=.025, rely=.45)
    playback_separator_10.place(relheight=.0001, relwidth=.9505, relx=.025, rely=.765)


def display_sort_by_user_frame():
    """Displays the Sort By User Frame
    """
    # Constants
    relheight: float = .8
    relwidth: float = .3266666
    x_spacing: float = .005
    y_spacing: float = .025

    # Sort by user buttons label frame & elements
    sort_user_buttons_labelframe.place(relheight=.245, relwidth=.5, relx=.25, rely=.005)

    sort_user_any_user_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                         relx=x_spacing, rely=.1)
    sort_user_specific_user_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                              relx=relwidth + x_spacing * 2, rely=.1)
    sort_user_specific_users_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                               relx=relwidth * 2 + x_spacing * 3, rely=.1)

    # Choose any user frame & label
    sort_user_choose_any_frame.place(relheight=.175, relwidth=.5, relx=.25, rely=.275)
    sort_user_choose_any_label.place(relheight=1, relwidth=1)

    # Choose specific user frame & elements
    sort_user_choose_user_frame.place(relheight=.175, relwidth=.5, relx=.25, rely=.275)

    sort_user_choose_user_label.place(relheight=relheight, relwidth=.295, relx=.005, rely=.1)
    sort_user_choose_user_combobox.place(relheight=relheight, relwidth=.69, relx=.305, rely=.1)

    # Set new relheight constant value
    relheight: float = .3

    # Sort by users frame & elements
    sort_user_choose_users_container_frame.place(relheight=.5, relwidth=.99, relx=.005, rely=.475)

    sort_user_reserved_label.place(relwidth=1, relheight=1)

    # Invalid composer username label
    sort_user_invalid_composer_name_label.place(relwidth=1, relheight=1)

    sort_user_choose_users_content_frame.place(relwidth=1, relheight=1)

    sort_user_add_all_button.place(relheight=relheight, relwidth=.1825,
                                   relx=.005, rely=y_spacing)
    sort_user_remove_all_button.place(relheight=relheight, relwidth=.1825,
                                      relx=.005, rely=relheight + y_spacing * 2)

    sort_user_add_selected_button.place(relheight=relheight, relwidth=.1825,
                                        relx=.01 + .1825, rely=y_spacing)
    sort_user_remove_selected_button.place(relheight=relheight, relwidth=.1825,
                                           relx=.01 + .1825, rely=relheight + y_spacing * 2)

    sort_user_inclusive_radiobutton.place(relheight=relheight, relwidth=.1825,
                                          relx=.005, rely=relheight * 2 + y_spacing * 3)
    sort_user_exclusive_radiobutton.place(relheight=relheight, relwidth=.1825,
                                          relx=.01 + .1825, rely=relheight * 2 + y_spacing * 3)

    sort_user_separator.place(relheight=1.05, relwidth=.0001, relx=.38)

    sort_user_scrolled_list_box_frame.place(relheight=.99, relwidth=.614, relx=.385, rely=.005)

    sort_user_listbox.place(relheight=1, relwidth=.98)
    sort_user_listbox_scroll_bar.place(relheight=1, relwidth=.02, relx=.98)

    # Tips
    # Tip 1
    sort_user_tip_labelframe_1.place(relheight=.445, relwidth=.235, relx=.005, rely=.005)
    sort_user_tip_message_1.pack(padx=5, pady=5)
    # Tip 2
    sort_user_tip_labelframe_2.place(relheight=.445, relwidth=.235, relx=.76, rely=.005)
    sort_user_tip_message_2.pack(padx=5, pady=5)

    # Configure frame based on sort value
    # Needed both when going to the menu for the first time and when coming back to menu after changing values
    config_sort_by_user_frame()


def display_sort_by_composition_length():
    """Displays the Sort By Composition Length Frame
    """
    # Constants
    relheight: float = .8
    relwidth: float = .3266666
    x_spacing: float = .005
    y_spacing: float = .1

    # Sort by length buttons label frame & elements
    sort_length_buttons_labelframe.place(relheight=.245, relwidth=.6, relx=.2, rely=.005)

    sort_length_any_length_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                             relx=x_spacing, rely=y_spacing)
    sort_length_specific_length_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                                  relx=relwidth + x_spacing * 2, rely=y_spacing)
    sort_length_specific_lengths_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                                   relx=relwidth * 2 + x_spacing * 3, rely=y_spacing)

    # Set new relwidth constant value
    relwidth: float = .195

    # Choose any length frame & label
    sort_length_choose_any_frame.place(relheight=.225, relwidth=.8, relx=.1, rely=.275)
    sort_length_choose_any_label.place(relheight=1, relwidth=1)

    # Choose specific length frame & elements
    sort_length_choose_length_frame.place(relheight=.225, relwidth=.8, relx=.1, rely=.275)

    sort_length_choose_length_label.place(relheight=relheight, relwidth=relwidth * 2,
                                          relx=x_spacing, rely=y_spacing)

    sort_length_short_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                        relx=relwidth * 2 + x_spacing * 2, rely=y_spacing)
    sort_length_medium_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                         relx=relwidth * 3 + x_spacing * 3, rely=y_spacing)
    sort_length_long_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                       relx=relwidth * 4 + x_spacing * 4, rely=y_spacing)

    # Choose specific lengths frame & elements
    sort_length_choose_lengths_frame.place(relheight=.225, relwidth=.8, relx=.1, rely=.275)

    sort_length_choose_lengths_label.place(relheight=relheight, relwidth=relwidth * 2,
                                           relx=x_spacing, rely=y_spacing)

    sort_length_short_checkbutton.place(relheight=relheight, relwidth=relwidth,
                                        relx=relwidth * 2 + x_spacing * 2, rely=y_spacing)
    sort_length_medium_checkbutton.place(relheight=relheight, relwidth=relwidth,
                                         relx=relwidth * 3 + x_spacing * 3, rely=y_spacing)
    sort_length_long_checkbutton.place(relheight=relheight, relwidth=relwidth,
                                       relx=relwidth * 4 + x_spacing * 4, rely=y_spacing)

    # Info Tip (Useful Information)
    sort_length_tip_labelframe.place(relheight=.35, relwidth=.975, relx=.0125, rely=.525)
    sort_length_tip_message.pack(padx=5, pady=5)

    # Configure frame based on sort value
    # Needed both when going to the menu for the first time and when coming back to menu after changing values
    config_sort_by_length_frame()


def display_sort_by_date():
    """Displays the Sort By Date Frame
    """
    # Constants
    relheight: float = .8
    relwidth: float = .3266666
    x_spacing: float = .005

    # Sort by date label frame & elements
    sort_date_buttons_labelframe.place(relheight=.245, relwidth=.5, relx=.25, rely=.005)

    sort_date_any_date_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                         relx=x_spacing, rely=.1)
    sort_date_specific_date_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                              relx=relwidth + x_spacing * 2, rely=.1)
    sort_date_date_interval_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                              relx=relwidth * 2 + x_spacing * 3, rely=.1)

    # Choose specific date label frame & elements
    sort_date_specific_labelframe.place(relheight=.3, relwidth=.45, relx=.025, rely=.275)

    # Specific date comboboxes container frame
    sort_date_specific_date_combobox_frame.place(relheight=.8, relwidth=.8, relx=.1, rely=.1)

    # Set new relwidth constant value
    relwidth: float = .25
    # Define new constant; used to set month_combobox relwidth
    month_relwidth: float = relwidth * 2 - x_spacing * 2

    # Specific date comboboxes
    sort_date_specific_date_day_combobox.place(relheight=1, relwidth=relwidth)
    sort_date_specific_date_month_combobox.place(relheight=1, relwidth=month_relwidth,
                                                 relx=relwidth + x_spacing)
    sort_date_specific_date_year_combobox.place(relheight=1, relwidth=relwidth,
                                                relx=month_relwidth + relwidth + x_spacing * 2)

    # Choose date interval label frame & elements
    sort_date_interval_labelframe.place(relheight=.61, relwidth=.45, relx=.525, rely=.275)

    # Date interval content frame
    sort_date_interval_content_frame.place(relheight=.7, relwidth=.9, relx=.05, rely=.15)

    # From label
    sort_date_date_interval_from_label.place(relheight=.475, relwidth=.25)

    # From date combobox frame
    sort_date_from_date_combobox_frame.place(relheight=.475, relwidth=.75, relx=.25)

    # From date comboboxes
    sort_date_from_date_day_combobox.place(relheight=1, relwidth=relwidth)
    sort_date_from_date_month_combobox.place(relheight=1, relwidth=month_relwidth,
                                             relx=relwidth + x_spacing)
    sort_date_from_date_year_combobox.place(relheight=1, relwidth=relwidth,
                                            relx=month_relwidth + relwidth + x_spacing * 2)

    # To label
    sort_date_date_interval_to_label.place(relheight=.475, relwidth=.25, rely=.525)

    # To date combobox frame
    sort_date_to_date_combobox_frame.place(relheight=.475, relwidth=.75, relx=.25, rely=.525)

    # To date comboboxes
    sort_date_to_date_day_combobox.place(relheight=1, relwidth=relwidth)
    sort_date_to_date_month_combobox.place(relheight=1, relwidth=month_relwidth,
                                           relx=relwidth + x_spacing)
    sort_date_to_date_year_combobox.place(relheight=1, relwidth=relwidth,
                                          relx=month_relwidth + relwidth + x_spacing * 2)

    # Set new relwidth and x_spacing constant values
    relwidth: float = .475
    x_spacing: float = .0166666

    # Any date labelframe & label
    sort_date_any_date_labelframe.place(relheight=.285, relwidth=.45, relx=.025, rely=.6)
    sort_date_choose_any_date_label.place(relheight=1, relwidth=1)

    # Inclusive / Exclusive date interval radio buttons frame
    sort_date_specific_inclusive_exclusive_labelframe.place(relheight=.285, relwidth=.45, relx=.025, rely=.6)

    # Inclusive / Exclusive date interval radio buttons
    sort_date_specific_inclusive_radiobutton.place(relheight=.8, relwidth=relwidth,
                                                   relx=x_spacing, rely=.1)
    sort_date_specific_exclusive_radiobutton.place(relheight=.8, relwidth=relwidth,
                                                   relx=relwidth + x_spacing * 2, rely=.1)

    # Inclusive / Exclusive date interval radio buttons frame
    sort_date_interval_inclusive_exclusive_labelframe.place(relheight=.285, relwidth=.45, relx=.025, rely=.6)

    # Inclusive / Exclusive date interval radio buttons
    sort_date_interval_inclusive_radiobutton.place(relheight=.8, relwidth=relwidth,
                                                   relx=x_spacing, rely=.1)
    sort_date_interval_exclusive_radiobutton.place(relheight=.8, relwidth=relwidth,
                                                   relx=relwidth + x_spacing * 2, rely=.1)

    # Configure frame based on sort value
    # Needed both when going to the menu for the first time and when coming back to menu after changing values
    config_sort_by_date_frame()


def display_sort_by_rating():
    """Displays the Sort By Rating Frame
    """
    # Constants
    relheight: float = .8
    relwidth: float = .3266666
    x_spacing: float = .005
    y_spacing: float = .1

    # Sort by rating buttons label frame & elements
    sort_rating_buttons_labelframe.place(relheight=.245, relwidth=.6, relx=.2, rely=.005)

    sort_rating_any_rating_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                             relx=x_spacing, rely=y_spacing)
    sort_rating_specific_rating_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                                  relx=relwidth + x_spacing * 2, rely=y_spacing)
    sort_rating_specific_ratings_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                                   relx=relwidth * 2 + x_spacing * 3, rely=y_spacing)

    # Choose any rating frame & label
    sort_rating_choose_any_frame.place(relheight=.285, relwidth=.8, relx=.1, rely=.275)
    sort_rating_choose_any_label.place(relheight=1, relwidth=1)

    # Set new relwidth constant value
    relwidth: float = .160833333

    # Choose specific rating label frame & elements
    sort_rating_choose_rating_labelframe.place(relheight=.285, relwidth=.8, relx=.1, rely=.275)

    sort_rating_no_rating_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                            relx=x_spacing, rely=y_spacing)
    sort_rating_1_star_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                         relx=relwidth + x_spacing * 2, rely=y_spacing)
    sort_rating_2_star_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                         relx=relwidth * 2 + x_spacing * 3, rely=y_spacing)
    sort_rating_3_star_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                         relx=relwidth * 3 + x_spacing * 4, rely=y_spacing)
    sort_rating_4_star_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                         relx=relwidth * 4 + x_spacing * 5, rely=y_spacing)
    sort_rating_5_star_radiobutton.place(relheight=relheight, relwidth=relwidth,
                                         relx=relwidth * 5 + x_spacing * 6, rely=y_spacing)

    # Choose specific ratings label frame & elements
    sort_rating_choose_ratings_labelframe.place(relheight=.285, relwidth=.8, relx=.1, rely=.275)

    sort_rating_no_rating_checkbutton.place(relheight=relheight, relwidth=relwidth,
                                            relx=x_spacing, rely=y_spacing)
    sort_rating_1_star_checkbutton.place(relheight=relheight, relwidth=relwidth,
                                         relx=relwidth + x_spacing * 2, rely=y_spacing)
    sort_rating_2_star_checkbutton.place(relheight=relheight, relwidth=relwidth,
                                         relx=relwidth * 2 + x_spacing * 3, rely=y_spacing)
    sort_rating_3_star_checkbutton.place(relheight=relheight, relwidth=relwidth,
                                         relx=relwidth * 3 + x_spacing * 4, rely=y_spacing)
    sort_rating_4_star_checkbutton.place(relheight=relheight, relwidth=relwidth,
                                         relx=relwidth * 4 + x_spacing * 5, rely=y_spacing)
    sort_rating_5_star_checkbutton.place(relheight=relheight, relwidth=relwidth,
                                         relx=relwidth * 5 + x_spacing * 6, rely=y_spacing)

    # Info Tip (Useful Information)
    sort_rating_tip_labelframe.place(relheight=.25, relwidth=.8, relx=.1, rely=.6)
    sort_rating_tip_message.pack(padx=5, pady=5)

    # Configure frame based on sort value
    # Needed both when going to the menu for the first time and when coming back to menu after changing values
    config_sort_by_rating_frame()


def display_current_sorting_parameters():
    """Displays the Current Parameters Label, Separators & Frame (with children)
    """
    # Current Sorting Parameters    ;    Explanation:                 ↱ → → → → ↱ ⇉ ⇉ ⇉ ⇉ ⇉ ⇉ ⇉ ⇉ ⇉ ⇉ ⇉ ⇘
    current_sorting_parameters_label.place(relheight=.075, relwidth=.325, relx=.3375, rely=.7125)  # Down   ⇊
    # Place Separators              ;    Explanation:  ↳ → → → → → → → → → → → ⬐ ⇄⇄⇄ ↴ ← ← ↲              ⇊
    sorting_separator_1.place(relheight=.0001, relwidth=.349, relx=-.01, rely=.7125 + .075 / 2)  # Down     ⇊
    sorting_separator_2.place(relheight=.0001, relwidth=.3375, relx=.325 + .3375, rely=.7125 + .075 / 2)  # ⇊
    #                               ;    Explanation:                ⬑ ← ← ← ⬑ ⇇ ⇇ ⇇ ⇇ ⇇ ⇇ ⇇ ⇇ ⇇ ⇇ ⇇ ⇇ ⇙
    # Current Sorting By Container Frame
    current_sorting_by_container_frame.place(relheight=.2, relwidth=.975, relx=.0125, rely=.79)
    # Current Sorting By Parameter Frames
    current_sorting_by_user_frame.place(relheight=.5, relwidth=.5)
    current_sorting_by_length_frame.place(relheight=.5, relwidth=.5, relx=.5)
    current_sorting_by_date_frame.place(relheight=.5, relwidth=.5, rely=.5)
    current_sorting_by_rating_frame.place(relheight=.5, relwidth=.5, relx=.5, rely=.5)
    # Current Parameters User
    current_sorting_by_user_label.place(relheight=1, relwidth=.25)
    current_sorting_by_user_data_label.place(relheight=1, relwidth=.75, relx=.25)
    # Current Parameters Length
    current_sorting_by_length_label.place(relheight=1, relwidth=.25)
    current_sorting_by_length_data_label.place(relheight=1, relwidth=.75, relx=.25)
    # Current Parameters Date
    current_sorting_by_date_label.place(relheight=1, relwidth=.25)
    current_sorting_by_date_data_label.place(relheight=1, relwidth=.75, relx=.25)
    # Current Parameters Rating
    current_sorting_by_rating_label.place(relheight=1, relwidth=.25)
    current_sorting_by_rating_data_label.place(relheight=1, relwidth=.75, relx=.25)


def display_settings():
    """Displays the Settings Menu
    """
    Settings.is_in_settings_menu.set(True)

    forget_all_widgets(root)
    root.focus()

    if User.is_logged_in:
        user_settings_radiobutton.config(state=NORMAL)
    else:
        user_settings_radiobutton.config(state=DISABLED)

    quit_button.place(relheight=.05, relwidth=.05, relx=.925, rely=.05)

    settings_menu_label.place(relheight=.15, relwidth=.5, relx=.25, rely=.025)

    settings_menu_content_labelframe.place(relheight=.7, relwidth=.9, relx=.05, rely=.18)

    # Constant variables
    relheight: float = .11275
    relwidth_label: float = .225
    relwidth_menu: float = .325
    relwidth_button: float = .185
    relwidth_button_2: float = relwidth_menu * .5
    relwidth_button_3: float = relwidth_menu / 3
    relx: float = .01
    rely: float = .015
    x_spacing: float = .02
    y_spacing: float = .0275

    background_color_label.place(relheight=relheight, relwidth=relwidth_label,
                                 relx=relx,
                                 rely=rely)
    background_color_menu.place(relheight=relheight, relwidth=relwidth_menu,
                                relx=relx + relwidth_label + x_spacing,
                                rely=rely)
    default_background_color_button.place(relheight=relheight, relwidth=relwidth_button,
                                          relx=relx + relwidth_label + relwidth_menu + x_spacing * 2,
                                          rely=rely)
    custom_background_color_button.place(relheight=relheight, relwidth=relwidth_button,
                                         relx=relx + relwidth_label + relwidth_menu + relwidth_button + x_spacing * 3,
                                         rely=rely)

    text_color_label.place(relheight=relheight, relwidth=relwidth_label,
                           relx=relx,
                           rely=rely + relheight + y_spacing)
    text_color_menu.place(relheight=relheight, relwidth=relwidth_menu,
                          relx=relx + relwidth_label + x_spacing,
                          rely=rely + relheight + y_spacing)
    default_text_color_button.place(relheight=relheight, relwidth=relwidth_button,
                                    relx=relx + relwidth_label + relwidth_menu + x_spacing * 2,
                                    rely=rely + relheight + y_spacing)
    custom_text_color_button.place(relheight=relheight, relwidth=relwidth_button,
                                   relx=relx + relwidth_label + relwidth_menu + relwidth_button + x_spacing * 3,
                                   rely=rely + relheight + y_spacing)

    buttons_color_label.place(relheight=relheight, relwidth=relwidth_label,
                              relx=relx,
                              rely=rely + relheight * 2 + y_spacing * 2)
    buttons_color_menu.place(relheight=relheight, relwidth=relwidth_menu,
                             relx=relx + relwidth_label + x_spacing,
                             rely=rely + relheight * 2 + y_spacing * 2)
    default_button_color_button.place(relheight=relheight, relwidth=relwidth_button,
                                      relx=relx + relwidth_label + relwidth_menu + x_spacing * 2,
                                      rely=rely + relheight * 2 + y_spacing * 2)
    custom_button_color_button.place(relheight=relheight, relwidth=relwidth_button,
                                     relx=relx + relwidth_label + relwidth_menu + relwidth_button + x_spacing * 3,
                                     rely=rely + relheight * 2 + y_spacing * 2)

    buttons_text_color_label.place(relheight=relheight, relwidth=relwidth_label,
                                   relx=relx,
                                   rely=rely + relheight * 3 + y_spacing * 3)
    buttons_text_color_menu.place(relheight=relheight, relwidth=relwidth_menu,
                                  relx=relx + relwidth_label + x_spacing,
                                  rely=rely + relheight * 3 + y_spacing * 3)
    default_buttons_text_color_button.place(relheight=relheight, relwidth=relwidth_button,
                                            relx=relx + relwidth_label + relwidth_menu + x_spacing * 2,
                                            rely=rely + relheight * 3 + y_spacing * 3)
    custom_buttons_text_color_button.place(relheight=relheight, relwidth=relwidth_button,
                                           relx=relx + relwidth_label + relwidth_menu + relwidth_button + x_spacing * 3,
                                           rely=rely + relheight * 3 + y_spacing * 3)

    invalid_text_color_label.place(relheight=relheight, relwidth=relwidth_label,
                                   relx=relx,
                                   rely=rely + relheight * 4 + y_spacing * 4)
    invalid_text_color_menu.place(relheight=relheight, relwidth=relwidth_menu,
                                  relx=relx + relwidth_label + x_spacing,
                                  rely=rely + relheight * 4 + y_spacing * 4)
    default_invalid_text_color_button.place(relheight=relheight, relwidth=relwidth_button,
                                            relx=relx + relwidth_label + relwidth_menu + x_spacing * 2,
                                            rely=rely + relheight * 4 + y_spacing * 4)
    custom_invalid_text_color_button.place(relheight=relheight, relwidth=relwidth_button,
                                           relx=relx + relwidth_label + relwidth_menu + relwidth_button + x_spacing * 3,
                                           rely=rely + relheight * 4 + y_spacing * 4)

    gui_sound_label.place(relheight=relheight, relwidth=relwidth_label,
                          relx=relx,
                          rely=rely + relheight * 5 + y_spacing * 5)
    gui_sound_on_radiobutton.place(relheight=relheight, relwidth=relwidth_button_2,
                                   relx=relx + relwidth_label + x_spacing,
                                   rely=rely + relheight * 5 + y_spacing * 5)
    gui_sound_off_radiobutton.place(relheight=relheight, relwidth=relwidth_button_2,
                                    relx=relx + relwidth_label + relwidth_button_2 + x_spacing,
                                    rely=rely + relheight * 5 + y_spacing * 5)

    remember_settings_label.place(relheight=relheight, relwidth=relwidth_label,
                                  relx=relx,
                                  rely=rely + relheight * 6 + y_spacing * 6)
    preset_settings_radiobutton.place(relheight=relheight, relwidth=relwidth_button_3,
                                      relx=relx + relwidth_label + x_spacing,
                                      rely=rely + relheight * 6 + y_spacing * 6)
    user_settings_radiobutton.place(relheight=relheight, relwidth=relwidth_button_3,
                                    relx=relx + relwidth_label + relwidth_button_3 + x_spacing,
                                    rely=rely + relheight * 6 + y_spacing * 6)
    default_settings_radiobutton.place(relheight=relheight, relwidth=relwidth_button_3,
                                       relx=relx + relwidth_label + relwidth_button_3 * 2 + x_spacing,
                                       rely=rely + relheight * 6 + y_spacing * 6)

    settings_info_labelframe.place(relheight=relheight * 2 + y_spacing, relwidth=relwidth_button * 2 + x_spacing,
                                   relx=relx + relwidth_label + relwidth_menu + x_spacing * 2,
                                   rely=rely + relheight * 5 + y_spacing * 5)
    settings_info_scrolled_text.pack(padx=8, pady=5)

    settings_wrecked_label.place(relheight=.095, relwidth=.72, relx=.05, rely=.885)

    return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)


def display_stats():
    """Displays the Stats Menu
    """

    forget_all_widgets(root)
    root.focus()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    stats_menu_label.place(relheight=0.2, relwidth=0.5, relx=0.25)

    # Note-related

    Stats.notes_played_labelframe.place(relheight=0.32, relwidth=0.325, relx=0.1, rely=0.2)

    Stats.piano_notes_label.grid(row=0, column=0, sticky=W)
    Stats.stats_colon_label1.grid(row=0, column=1)
    Stats.piano_notes_number_label.grid(row=0, column=2, sticky=E)

    Stats.short_piano_notes_label.grid(row=1, column=0, sticky=W)
    Stats.stats_colon_label2.grid(row=1, column=1)
    Stats.short_piano_notes_number_label.grid(row=1, column=2, sticky=E)

    Stats.long_piano_notes_label.grid(row=2, column=0, sticky=W)
    Stats.stats_colon_label3.grid(row=2, column=1)
    Stats.long_piano_notes_number_label.grid(row=2, column=2, sticky=E)

    Stats.flute_notes_label.grid(row=3, column=0, sticky=W)
    Stats.stats_colon_label4.grid(row=3, column=1)
    Stats.flute_notes_number_label.grid(row=3, column=2, sticky=E)

    Stats.trumpet_notes_label.grid(row=4, column=0, sticky=W)
    Stats.stats_colon_label5.grid(row=4, column=1)
    Stats.trumpet_notes_number_label.grid(row=4, column=2, sticky=E)

    Stats.violin_notes_label.grid(row=5, column=0, sticky=W)
    Stats.stats_colon_label6.grid(row=5, column=1)
    Stats.violin_notes_number_label.grid(row=5, column=2, sticky=E)

    # Settings-related

    Stats.settings_changed_labelframe.place(relheight=0.32, relwidth=0.425, relx=0.45, rely=0.2)

    Stats.background_color_changed_label.grid(row=0, column=0, sticky=W)
    Stats.stats_colon_label10.grid(row=0, column=1)
    Stats.background_color_changed_number_label.grid(row=0, column=2, sticky=E)

    Stats.text_color_changed_label.grid(row=1, column=0, sticky=W)
    Stats.stats_colon_label11.grid(row=1, column=1)
    Stats.text_color_changed_number_label.grid(row=1, column=2, sticky=E)

    Stats.button_color_changed_label.grid(row=2, column=0, sticky=W)
    Stats.stats_colon_label12.grid(row=2, column=1)
    Stats.button_color_changed_number_label.grid(row=2, column=2, sticky=E)

    Stats.button_text_color_changed_label.grid(row=3, column=0, sticky=W)
    Stats.stats_colon_label13.grid(row=3, column=1)
    Stats.button_text_color_changed_number_label.grid(row=3, column=2, sticky=E)

    Stats.invalid_text_color_changed_label.grid(row=4, column=0, sticky=W)
    Stats.stats_colon_label14.grid(row=4, column=1)
    Stats.invalid_text_color_changed_number_label.grid(row=4, column=2, sticky=E)

    Stats.gui_sound_changed_label.grid(row=5, column=0, sticky=W)
    Stats.stats_colon_label15.grid(row=5, column=1)
    Stats.gui_sound_changed_number_label.grid(row=5, column=2, sticky=E)

    Stats.remember_settings_changed_label.grid(row=6, column=0, sticky=W)
    Stats.stats_colon_label16.grid(row=6, column=1)
    Stats.remember_settings_changed_number_label.grid(row=6, column=2, sticky=E)

    # Menu-related

    Stats.main_menu_labelframe.place(relheight=0.42, relwidth=0.425, relx=0.1, rely=0.525)

    Stats.played_freely_label.grid(row=0, column=0, sticky=W)
    Stats.stats_colon_label17.grid(row=0, column=1)
    Stats.played_freely_number_label.grid(row=0, column=2, sticky=E)

    Stats.recorded_compositions_label.grid(row=1, column=0, sticky=W)
    Stats.stats_colon_label18.grid(row=1, column=1)
    Stats.recorded_compositions_number_label.grid(row=1, column=2, sticky=E)

    Stats.played_back_compositions_label.grid(row=2, column=0, sticky=W)
    Stats.stats_colon_label19.grid(row=2, column=1)
    Stats.played_back_compositions_number_label.grid(row=2, column=2, sticky=E)

    Stats.managed_compositions_label.grid(row=3, column=0, sticky=W)
    Stats.stats_colon_label20.grid(row=3, column=1)
    Stats.managed_compositions_number_label.grid(row=3, column=2, sticky=E)

    Stats.entered_settings_label.grid(row=4, column=0, sticky=W)
    Stats.stats_colon_label21.grid(row=4, column=1)
    Stats.entered_settings_number_label.grid(row=4, column=2, sticky=E)

    Stats.viewed_stats_label.grid(row=5, column=0, sticky=W)
    Stats.stats_colon_label22.grid(row=5, column=1)
    Stats.viewed_stats_number_label.grid(row=5, column=2, sticky=E)

    Stats.separator.grid(row=6, column=0, columnspan=3, sticky=EW)

    Stats.viewed_more_stats_label.grid(row=7, column=0, sticky=W)
    Stats.stats_colon_label23.grid(row=7, column=1)
    Stats.viewed_more_stats_number_label.grid(row=7, column=2, sticky=E)

    Stats.logged_in_label.grid(row=8, column=0, sticky=W)
    Stats.stats_colon_label24.grid(row=8, column=1)
    Stats.logged_in_number_label.grid(row=8, column=2, sticky=E)

    Stats.logged_out_label.grid(row=9, column=0, sticky=W)
    Stats.stats_colon_label25.grid(row=9, column=1)
    Stats.logged_out_number_label.grid(row=9, column=2, sticky=E)

    Stats.registered_label.grid(row=10, column=0, sticky=W)
    Stats.stats_colon_label26.grid(row=10, column=1)
    Stats.registered_number_label.grid(row=10, column=2, sticky=E)

    # Account-related

    Stats.accounts_labelframe.place(relheight=0.195, relwidth=0.325, relx=0.55, rely=0.525)

    Stats.active_accounts_label.grid(row=0, column=0, sticky=W)
    Stats.stats_colon_label7.grid(row=0, column=1)
    Stats.active_accounts_number_label.grid(row=0, column=2, sticky=E)

    Stats.deleted_accounts_label.grid(row=1, column=0, sticky=W)
    Stats.stats_colon_label8.grid(row=1, column=1)
    Stats.deleted_accounts_number_label.grid(row=1, column=2, sticky=E)

    Stats.admin_accounts_label.grid(row=2, column=0, sticky=W)
    Stats.stats_colon_label9.grid(row=2, column=1)
    Stats.admin_accounts_number_label.grid(row=2, column=2, sticky=E)

    # Composition-related

    Stats.compositions_labelframe.place(relheight=0.15, relwidth=0.325, relx=0.55, rely=0.725)

    Stats.active_compositions_label.grid(row=0, column=0, sticky=W)
    Stats.stats_colon_label27.grid(row=0, column=1)
    Stats.active_compositions_number_label.grid(row=0, column=2, sticky=E)

    Stats.deleted_compositions_label.grid(row=1, column=0, sticky=W)
    Stats.stats_colon_label28.grid(row=1, column=1)
    Stats.deleted_compositions_number_label.grid(row=1, column=2, sticky=E)

    # Star label
    stats_star_label.place(relheight=0.05, relwidth=0.425, relx=0.1, rely=0.945)

    # Didn't have enough
    stats_more_stats_button.place(relheight=0.05, relwidth=0.2, relx=0.55, rely=0.9)

    return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)


def display_more_stats():
    """Displays the More Stats Menu
    """

    forget_all_widgets(root)
    root.focus()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    more_stats_menu_label.place(relheight=0.2, relwidth=0.5, relx=0.25)

    # Piano:
    Stats.piano_labelframe.place(relheight=0.41, relwidth=0.61, relx=0.05, rely=0.2)

    # Short Notes
    Stats.do_1_short_label.grid(row=0, column=0, sticky=W)
    Stats.more_stats_colon_label1.grid(row=0, column=1)
    Stats.do_1_short_number_label.grid(row=0, column=2, sticky=E)

    Stats.re_short_label.grid(row=1, column=0, sticky=W)
    Stats.more_stats_colon_label2.grid(row=1, column=1)
    Stats.re_short_number_label.grid(row=1, column=2, sticky=E)

    Stats.mi_short_label.grid(row=2, column=0, sticky=W)
    Stats.more_stats_colon_label3.grid(row=2, column=1)
    Stats.mi_short_number_label.grid(row=2, column=2, sticky=E)

    Stats.fa_short_label.grid(row=3, column=0, sticky=W)
    Stats.more_stats_colon_label4.grid(row=3, column=1)
    Stats.fa_short_number_label.grid(row=3, column=2, sticky=E)

    Stats.sol_short_label.grid(row=4, column=0, sticky=W)
    Stats.more_stats_colon_label5.grid(row=4, column=1)
    Stats.sol_short_number_label.grid(row=4, column=2, sticky=E)

    Stats.la_short_label.grid(row=5, column=0, sticky=W)
    Stats.more_stats_colon_label6.grid(row=5, column=1)
    Stats.la_short_number_label.grid(row=5, column=2, sticky=E)

    Stats.si_short_label.grid(row=6, column=0, sticky=W)
    Stats.more_stats_colon_label7.grid(row=6, column=1)
    Stats.si_short_number_label.grid(row=6, column=2, sticky=E)

    Stats.do_2_short_label.grid(row=7, column=0, sticky=W)
    Stats.more_stats_colon_label8.grid(row=7, column=1)
    Stats.do_2_short_number_label.grid(row=7, column=2, sticky=E)

    # Space Labels
    Stats.space_label1.grid(row=0, column=3)
    Stats.space_label2.grid(row=1, column=3)
    Stats.space_label3.grid(row=2, column=3)
    Stats.space_label4.grid(row=3, column=3)
    Stats.space_label5.grid(row=4, column=3)
    Stats.space_label6.grid(row=5, column=3)
    Stats.space_label7.grid(row=6, column=3)
    Stats.space_label8.grid(row=7, column=3)

    # Long Notes
    Stats.do_1_long_label.grid(row=0, column=4, sticky=W)
    Stats.more_stats_colon_label9.grid(row=0, column=5)
    Stats.do_1_long_number_label.grid(row=0, column=6, sticky=E)

    Stats.re_long_label.grid(row=1, column=4, sticky=W)
    Stats.more_stats_colon_label10.grid(row=1, column=5)
    Stats.re_long_number_label.grid(row=1, column=6, sticky=E)

    Stats.mi_long_label.grid(row=2, column=4, sticky=W)
    Stats.more_stats_colon_label11.grid(row=2, column=5)
    Stats.mi_long_number_label.grid(row=2, column=6, sticky=E)

    Stats.fa_long_label.grid(row=3, column=4, sticky=W)
    Stats.more_stats_colon_label12.grid(row=3, column=5)
    Stats.fa_long_number_label.grid(row=3, column=6, sticky=E)

    Stats.sol_long_label.grid(row=4, column=4, sticky=W)
    Stats.more_stats_colon_label13.grid(row=4, column=5)
    Stats.sol_long_number_label.grid(row=4, column=6, sticky=E)

    Stats.la_long_label.grid(row=5, column=4, sticky=W)
    Stats.more_stats_colon_label14.grid(row=5, column=5)
    Stats.la_long_number_label.grid(row=5, column=6, sticky=E)

    Stats.si_long_label.grid(row=6, column=4, sticky=W)
    Stats.more_stats_colon_label15.grid(row=6, column=5)
    Stats.si_long_number_label.grid(row=6, column=6, sticky=E)

    Stats.do_2_long_label.grid(row=7, column=4, sticky=W)
    Stats.more_stats_colon_label16.grid(row=7, column=5)
    Stats.do_2_long_number_label.grid(row=7, column=6, sticky=E)

    # Flute:
    Stats.flute_labelframe.place(relheight=0.41, relwidth=0.275, relx=0.675, rely=0.2)

    Stats.space_label0.grid(row=0, column=0)

    Stats.c4_flute_label.grid(row=1, column=0, sticky=W)
    Stats.more_stats_colon_label17.grid(row=1, column=1)
    Stats.c4_flute_number_label.grid(row=1, column=2, sticky=E)

    Stats.c5_flute_label.grid(row=2, column=0, sticky=W)
    Stats.more_stats_colon_label18.grid(row=2, column=1)
    Stats.c5_flute_number_label.grid(row=2, column=2, sticky=E)

    Stats.c6_flute_label.grid(row=3, column=0, sticky=W)
    Stats.more_stats_colon_label19.grid(row=3, column=1)
    Stats.c6_flute_number_label.grid(row=3, column=2, sticky=E)

    Stats.g4_flute_label.grid(row=4, column=0, sticky=W)
    Stats.more_stats_colon_label20.grid(row=4, column=1)
    Stats.g4_flute_number_label.grid(row=4, column=2, sticky=E)

    Stats.g5_flute_label.grid(row=5, column=0, sticky=W)
    Stats.more_stats_colon_label21.grid(row=5, column=1)
    Stats.g5_flute_number_label.grid(row=5, column=2, sticky=E)

    Stats.g6_flute_label.grid(row=6, column=0, sticky=W)
    Stats.more_stats_colon_label22.grid(row=6, column=1)
    Stats.g6_flute_number_label.grid(row=6, column=2, sticky=E)

    # Trumpet
    Stats.trumpet_labelframe.place(relheight=0.33, relwidth=0.24, relx=0.05, rely=0.62)

    Stats.c4_trumpet_label.grid(row=0, column=0, sticky=W)
    Stats.more_stats_colon_label23.grid(row=0, column=1)
    Stats.c4_trumpet_number_label.grid(row=0, column=2, sticky=E)

    Stats.c5_trumpet_label.grid(row=1, column=0, sticky=W)
    Stats.more_stats_colon_label24.grid(row=1, column=1)
    Stats.c5_trumpet_number_label.grid(row=1, column=2, sticky=E)

    Stats.c6_trumpet_label.grid(row=2, column=0, sticky=W)
    Stats.more_stats_colon_label25.grid(row=2, column=1)
    Stats.c6_trumpet_number_label.grid(row=2, column=2, sticky=E)

    Stats.g3_trumpet_label.grid(row=3, column=0, sticky=W)
    Stats.more_stats_colon_label26.grid(row=3, column=1)
    Stats.g3_trumpet_number_label.grid(row=3, column=2, sticky=E)

    Stats.g4_trumpet_label.grid(row=4, column=0, sticky=W)
    Stats.more_stats_colon_label27.grid(row=4, column=1)
    Stats.g4_trumpet_number_label.grid(row=4, column=2, sticky=E)

    Stats.g5_trumpet_label.grid(row=5, column=0, sticky=W)
    Stats.more_stats_colon_label28.grid(row=5, column=1)
    Stats.g5_trumpet_number_label.grid(row=5, column=2, sticky=E)

    # Violin
    Stats.violin_labelframe.place(relheight=0.33, relwidth=0.24, relx=0.3, rely=0.62)

    Stats.c4_violin_label.grid(row=0, column=0, sticky=W)
    Stats.more_stats_colon_label29.grid(row=0, column=1)
    Stats.c4_violin_number_label.grid(row=0, column=2, sticky=E)

    Stats.c5_violin_label.grid(row=1, column=0, sticky=W)
    Stats.more_stats_colon_label30.grid(row=1, column=1)
    Stats.c5_violin_number_label.grid(row=1, column=2, sticky=E)

    Stats.c6_violin_label.grid(row=2, column=0, sticky=W)
    Stats.more_stats_colon_label31.grid(row=2, column=1)
    Stats.c6_violin_number_label.grid(row=2, column=2, sticky=E)

    Stats.g4_violin_label.grid(row=3, column=0, sticky=W)
    Stats.more_stats_colon_label32.grid(row=3, column=1)
    Stats.g4_violin_number_label.grid(row=3, column=2, sticky=E)

    Stats.g5_violin_label.grid(row=4, column=0, sticky=W)
    Stats.more_stats_colon_label33.grid(row=4, column=1)
    Stats.g5_violin_number_label.grid(row=4, column=2, sticky=E)

    Stats.g6_violin_label.grid(row=5, column=0, sticky=W)
    Stats.more_stats_colon_label34.grid(row=5, column=1)
    Stats.g6_violin_number_label.grid(row=5, column=2, sticky=E)

    # Changed Instrument
    Stats.instrument_changed_labelframe.place(relheight=0.16, relwidth=0.4, relx=0.55, rely=0.62)

    Stats.instrument_changed_successfully_label.grid(row=0, column=0, sticky=W)
    Stats.more_stats_colon_label35.grid(row=0, column=1)
    Stats.instrument_changed_successfully_number_label.grid(row=0, column=2, sticky=E)

    Stats.instrument_changed_unsuccessfully_label.grid(row=1, column=0, sticky=W)
    Stats.more_stats_colon_label36.grid(row=1, column=1)
    Stats.instrument_changed_unsuccessfully_number_label.grid(row=1, column=2, sticky=E)

    # Returned to Main Menu
    Stats.returned_to_main_menu_labelframe.place(relheight=0.105, relwidth=0.4, relx=0.55, rely=0.79)
    Stats.returned_to_main_menu_number_label.place(relheight=0.05, relwidth=0.38, relx=0.56, rely=0.83)

    return_to_stats_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.55, rely=0.9)
    return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)


def display_login():
    """Displays the Login Menu
    """

    forget_all_widgets(root)
    root.focus()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    login_menu_label.place(relheight=0.15, relwidth=0.5, relx=0.25, rely=0.05)

    login_menu_labelframe.place(relheight=0.4, relwidth=0.7, relx=0.15, rely=0.25)

    login_menu_main_content_frame.place(relheight=.9, relwidth=.95, relx=.025, rely=.035)

    # Constant position variables
    relheight: float = .185
    label_relwidth: float = .3
    entry_relwidth: float = .575
    button_relwidth_1: float = .35
    button_relwidth_2: float = .2
    relx: float = .05625
    relx_2: float = .2
    rely: float = .1
    x_spacing: float = .0125
    y_spacing: float = .035

    name_label.place(relheight=relheight, relwidth=label_relwidth,
                     relx=relx, rely=rely)
    name_entry_field.place(relheight=relheight, relwidth=entry_relwidth,
                           relx=relx + label_relwidth + x_spacing, rely=rely)

    password_label.place(relheight=relheight, relwidth=label_relwidth,
                         relx=relx, rely=rely + relheight + y_spacing)
    password_entry_field.place(relheight=relheight, relwidth=entry_relwidth,
                               relx=relx + label_relwidth + x_spacing, rely=rely + relheight + y_spacing)

    show_password_checkbutton_login.place(relheight=relheight, relwidth=button_relwidth_1,
                                          relx=relx_2,
                                          rely=rely + relheight * 3 + y_spacing * 3)
    login_button.place(relheight=relheight, relwidth=button_relwidth_2,
                       relx=relx_2 + button_relwidth_1 + x_spacing * 4, rely=rely + relheight * 3 + y_spacing * 3)

    forgot_password_labelframe.place(relheight=0.125, relwidth=0.325, relx=0.15, rely=0.7)
    forgot_password_button.place(relheight=0.7, relwidth=0.9, relx=0.05, rely=0.1)

    no_account_labelframe.place(relheight=0.125, relwidth=0.325, relx=0.15 + .1 + .275, rely=0.7)
    register_button_2.place(relheight=0.7, relwidth=0.9, relx=0.05, rely=0.1)

    return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)


def display_sure_logout():
    """Displays the Sure Logout Menu
    """

    forget_all_widgets(root)
    root.focus()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    logout_menu_label.place(relheight=0.15, relwidth=0.8, relx=0.1, rely=0.05)

    whoa_label.place(relheight=0.1, relwidth=0.9, relx=0.05, rely=0.275)

    sure_logout_labelframe.place(relheight=0.225, relwidth=0.7, relx=0.15, rely=0.45)
    no_button.place(relheight=0.075, relwidth=0.3, relx=0.175, rely=0.55)
    yes_button.place(relheight=0.075, relwidth=0.3, relx=0.525, rely=0.55)


def display_forgot_password():
    """Displays the Recovery Key Menu
    """

    forget_all_widgets(root)
    root.focus()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    recover_password_label.place(relheight=0.15, relwidth=0.8, relx=0.1, rely=0.05)

    recover_key_labelframe.place(relheight=0.4, relwidth=0.6, relx=0.2, rely=0.2)

    recovery_key_username_label.place(relheight=0.05, relwidth=0.2, relx=0.3, rely=0.275)
    recovery_key_username_entry.place(relheight=0.05, relwidth=0.2, relx=0.5, rely=0.275)

    relx: float = 0.255
    rely: float = 0.35

    recovery_key_entry_field_1.place(relheight=0.085, relwidth=0.1, relx=relx, rely=rely)
    recovery_key_dash_label_1.place(relheight=0.085, relwidth=0.03, relx=relx + 0.1, rely=rely)
    recovery_key_entry_field_2.place(relheight=0.085, relwidth=0.1, relx=relx + 0.13, rely=rely)
    recovery_key_dash_label_2.place(relheight=0.085, relwidth=0.03, relx=relx + 0.23, rely=rely)
    recovery_key_entry_field_3.place(relheight=0.085, relwidth=0.1, relx=relx + 0.26, rely=rely)
    recovery_key_dash_label_3.place(relheight=0.085, relwidth=0.03, relx=relx + 0.36, rely=rely)
    recovery_key_entry_field_4.place(relheight=0.085, relwidth=0.1, relx=relx + 0.39, rely=rely)

    recover_password_button.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=0.45)

    recovered_password_labelframe.place(relheight=0.2, relwidth=0.6, relx=0.2, rely=0.61)

    recovered_password_text.place(relheight=.55, relwidth=.95, relx=.025, rely=.1)
    recovered_password_text_scrollbar.place(relheight=.2, relwidth=.95, relx=.025, rely=.65)

    show_password_checkbutton_recovery_key.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=0.825)
    create_recovered_password_file_button.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=0.9)

    return_to_login_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.825)
    return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)


def display_register_user_general_data():
    """Displays the Register Menu (general info)
    """

    User.is_in_register_user_menu_general_data.set(True)

    # Set date to current date
    if User.came_from_main_menu.get():
        User.chosen_birth_day.set(datetime.date.today().day)
        User.chosen_birth_month.set(datetime.date.today().strftime("%B"))
        User.chosen_birth_year.set(datetime.date.today().year)
        # Set User.came_from_main_menu to false if it was true
        User.came_from_main_menu.set(False)

    relx: float = .045

    forget_all_widgets(root)
    root.focus()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    register_menu_label.place(relheight=0.15, relwidth=0.5, relx=0.25, rely=0.05)

    welcome_label.place(relheight=0.125, relwidth=0.92, relx=0.04, rely=0.215)

    input_your_data_labelframe.place(relheight=0.47, relwidth=0.92, relx=0.04, rely=0.35)

    first_name_label.place(relheight=0.05, relwidth=0.11, relx=relx + 0.015, rely=0.425)
    first_name_entry_field.place(relheight=0.05, relwidth=0.285, relx=relx + 0.13, rely=0.425)

    last_name_label.place(relheight=0.05, relwidth=0.11, relx=relx + 0.015, rely=0.5)
    last_name_entry_field.place(relheight=0.05, relwidth=0.285, relx=relx + 0.13, rely=0.5)

    nickname_label.place(relheight=0.05, relwidth=0.11, relx=relx + 0.015, rely=0.575)
    nickname_entry_field.place(relheight=0.05, relwidth=0.285, relx=relx + 0.13, rely=0.575)
    nickname_help_label.place(relheight=0.02, relwidth=0.285, relx=relx + 0.13, rely=0.625)

    gender_label.place(relheight=0.05, relwidth=0.11, relx=relx + 0.015, rely=0.65)
    gender_option_menu.place(relheight=0.05, relwidth=0.285, relx=relx + 0.13, rely=0.65)

    birth_date_label.place(relheight=0.05, relwidth=0.11, relx=relx + 0.015, rely=0.725)
    birth_day_combobox.place(relheight=0.05, relwidth=0.05, relx=relx + 0.13, rely=0.725)
    birth_day_label.place(relheight=0.025, relwidth=0.05, relx=relx + 0.13, rely=0.775)
    slash_label1.place(relheight=0.05, relwidth=0.01, relx=relx + 0.185, rely=0.725)
    birth_month_combobox.place(relheight=0.05, relwidth=0.125, relx=relx + 0.2, rely=0.725)
    birth_month_label.place(relheight=0.025, relwidth=0.125, relx=relx + 0.2, rely=0.775)
    slash_label2.place(relheight=0.05, relwidth=0.01, relx=relx + 0.33, rely=0.725)
    birth_year_combobox.place(relheight=0.05, relwidth=0.07, relx=relx + 0.345, rely=0.725)
    birth_year_label.place(relheight=0.025, relwidth=0.07, relx=relx + 0.345, rely=0.775)

    relx = .48

    country_of_origin_label.place(relheight=0.05, relwidth=0.205, relx=relx, rely=0.425)
    country_of_origin_option_menu.place(relheight=0.05, relwidth=0.25, relx=relx + 0.21, rely=0.425)

    state_of_origin_label.place(relheight=0.05, relwidth=0.205, relx=relx, rely=0.5)
    state_of_origin_option_menu.place(relheight=0.05, relwidth=0.25, relx=relx + 0.21, rely=0.5)

    country_of_residence_label.place(relheight=0.05, relwidth=0.205, relx=relx, rely=0.575)
    country_of_residence_option_menu.place(relheight=0.05, relwidth=0.25, relx=relx + 0.21, rely=0.575)

    state_of_residence_label.place(relheight=0.05, relwidth=0.205, relx=relx, rely=0.65)
    state_of_residence_option_menu.place(relheight=0.05, relwidth=0.25, relx=relx + 0.21, rely=0.65)

    account_privacy_label.place(relheight=0.05, relwidth=0.205, relx=relx, rely=0.725)
    account_privacy_option_menu.place(relheight=0.05, relwidth=0.25, relx=relx + 0.21, rely=0.725)

    lookup_help_label.place(relheight=0.05, relwidth=0.7, relx=0.05, rely=0.825)

    help_button.place(relheight=0.05, relwidth=0.0975, relx=0.775, rely=0.825)

    next_button.place(relheight=0.05, relwidth=0.0975, relx=0.8775, rely=0.825)

    return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)


def display_register_user_username_password():
    """Displays the Register Menu (Username & Password)
    """

    User.is_in_register_user_menu_general_data.set(False)

    if User.chosen_gender.get() == "Male":
        hello_new_user_label["text"] = f"Hello, Mr. {User.chosen_last_name.get()}!\n" \
                                       f"Your account is almost ready, last step to go!"
    elif User.chosen_gender.get() == "Female":
        hello_new_user_label["text"] = f"Hello, Ms. {User.chosen_last_name.get()}!\n" \
                                       f"Your account is almost ready, last step to go!"
    else:
        hello_new_user_label["text"] = f"Hello, {User.chosen_last_name.get()}!\n" \
                                       f"Your account is almost ready, last step to go!"

    forget_all_widgets(root)
    root.focus()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    register_menu_label.place(relheight=0.15, relwidth=0.5, relx=0.25, rely=0.05)

    hello_new_user_label.place(relheight=0.1, relwidth=0.9, relx=0.05, rely=0.2)

    register_menu_labelframe.place(relheight=0.5, relwidth=0.7, relx=0.15, rely=0.3)

    choose_username_label.place(relheight=0.05, relwidth=0.2, relx=0.18, rely=0.375)
    choose_username_entry_field.place(relheight=0.05, relwidth=0.42, relx=0.4, rely=0.375)
    username_help_label.place(relheight=0.02, relwidth=0.42, relx=0.4, rely=0.425)

    choose_password_label.place(relheight=0.05, relwidth=0.2, relx=0.18, rely=0.475)
    choose_password_entry_field.place(relheight=0.05, relwidth=0.42, relx=0.4, rely=0.475)
    password_help_label.place(relheight=0.02, relwidth=0.42, relx=0.4, rely=0.525)

    confirm_password_label.place(relheight=0.05, relwidth=0.2, relx=0.18, rely=0.575)
    confirm_password_entry_field.place(relheight=0.05, relwidth=0.42, relx=0.4, rely=0.575)
    confirm_password_help_label.place(relheight=0.02, relwidth=0.42, relx=0.4, rely=0.625)

    create_account_button.place(relheight=0.05, relwidth=0.2, relx=0.29, rely=0.725)

    show_password_checkbutton_register.place(relheight=0.05, relwidth=0.2, relx=0.51, rely=0.725)

    lookup_help_label.place(relheight=0.05, relwidth=0.7, relx=0.05, rely=0.825)

    help_button.place(relheight=0.05, relwidth=0.0975, relx=0.775, rely=0.825)

    back_button.place(relheight=0.05, relwidth=0.0975, relx=0.8775, rely=0.825)

    return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)


def display_help():
    """Displays the help window when registering user
    """

    forget_all_widgets(root)
    root.focus()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    help_menu_label.place(relheight=0.15, relwidth=0.5, relx=0.25, rely=0.05)

    help_text_labelframe1.place(relheight=0.21, relwidth=0.95, relx=0.025, rely=0.2)
    help_text_label1.place(relheight=0.04, relwidth=0.945, relx=0.0275, rely=0.24)
    help_text_label2.place(relheight=0.04, relwidth=0.945, relx=0.0275, rely=0.28)
    help_text_label3.place(relheight=0.04, relwidth=0.945, relx=0.0275, rely=0.32)
    help_text_label4.place(relheight=0.04, relwidth=0.945, relx=0.0275, rely=0.36)

    help_text_labelframe2.place(relheight=0.13, relwidth=0.95, relx=0.025, rely=0.45)
    help_text_label6.place(relheight=0.04, relwidth=0.945, relx=0.0275, rely=0.49)
    help_text_label7.place(relheight=0.04, relwidth=0.945, relx=0.0275, rely=0.53)

    help_text_labelframe3.place(relheight=0.21, relwidth=0.95, relx=0.025, rely=0.62)
    help_text_label8.place(relheight=0.04, relwidth=0.945, relx=0.0275, rely=0.66)
    help_text_label9.place(relheight=0.04, relwidth=0.945, relx=0.0275, rely=0.7)
    help_text_label10.place(relheight=0.04, relwidth=0.945, relx=0.0275, rely=0.74)
    help_text_label11.place(relheight=0.04, relwidth=0.945, relx=0.0275, rely=0.78)

    help_wip_label.place(relheight=0.05, relwidth=0.7, relx=0.025, rely=0.9)

    back_to_previous_menu_button.place(relheight=0.05, relwidth=0.225, relx=0.75, rely=0.9)


def display_registration_successful():
    """Displays the registration successful window
    """

    User.is_in_registration_successful.set(True)

    if User.chosen_gender.get() == "Male":
        congratulations_label["text"] = f"Congratulations Mr. {User.chosen_username.get()}, your account " \
                                        f"registration is now complete!\n" \
                                        f"You are the {'{:,}'.format(User.user_count)}" \
                                        + Misc.get_suffix(User.user_count) + " user to join us!"
    elif User.chosen_gender.get() == "Female":
        congratulations_label["text"] = f"Congratulations Ms. {User.chosen_username.get()}, your account " \
                                        f"registration is now complete!\n" \
                                        f"You are the {'{:,}'.format(User.user_count)}" \
                                        + Misc.get_suffix(User.user_count) + " user to join us!"
    else:
        congratulations_label["text"] = f"Congratulations {User.chosen_username.get()}, your account " \
                                        f"registration is now complete!\n" \
                                        f"You are the {'{:,}'.format(User.user_count)}" \
                                        + Misc.get_suffix(User.user_count) + " user to join us!"

    given_recovery_key_label.config(text=User.logged_in_user["Credentials"]["Recovery Key"])

    forget_all_widgets(root)
    root.focus()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    registration_successful_menu_label.place(relheight=0.15, relwidth=0.8, relx=0.1, rely=0.05)

    congratulations_label.place(relheight=0.1, relwidth=0.95, relx=0.025, rely=0.2)

    recovery_key_labelframe.place(relheight=0.275, relwidth=0.7, relx=0.15, rely=0.325)
    given_recovery_key_label.place(relheight=0.1, relwidth=0.68, relx=0.16, rely=0.375)
    recovery_key_info_label.place(relheight=0.05, relwidth=0.68, relx=0.16, rely=0.475)
    create_recovery_key_txt_file_button.place(relheight=0.05, relwidth=0.3, relx=0.35, rely=0.535)

    gained_powers_labelframe.place(relheight=0.26, relwidth=0.7, relx=0.15, rely=0.6)
    gained_powers_label1.place(relheight=0.05, relwidth=0.68, relx=0.16, rely=0.65)
    gained_powers_label2.place(relheight=0.05, relwidth=0.68, relx=0.16, rely=0.7)
    gained_powers_label3.place(relheight=0.05, relwidth=0.68, relx=0.16, rely=0.75)
    gained_powers_label4.place(relheight=0.05, relwidth=0.68, relx=0.16, rely=0.8)

    return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)


def display_user_profile(user: dict):
    """Displays the given users' Profile Menu
    """

    forget_all_widgets(root)
    root.focus()

    # Set user profile user to current profile user (dict variable)
    User.user_profile_user = copy.deepcopy(user)

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    user_profile_menu_label.place(relheight=0.15, relwidth=0.8, relx=0.1, rely=0.025)

    # Config main labelframe text
    if user is User.logged_in_user:
        user_profile_labelframe.config(text="My Profile:")
    else:
        user_profile_labelframe.config(text=f"{user['Credentials']['Username']}"
                                            f"{Misc.get_possessive(user['Credentials']['Username'])} Profile:")

    # Place labelframes and separators
    user_profile_labelframe.place(relheight=.72, relwidth=.9, relx=.05, rely=.175)
    user_profile_separator_1.place(relheight=.0001, relwidth=.8995, relx=.05, rely=.375)
    user_profile_options_label.place(relheight=.05, relwidth=.075, relx=.4625, rely=.775)
    user_profile_separator_2.place(relheight=.0001, relwidth=.4125, relx=.05, rely=.8)
    user_profile_separator_3.place(relheight=.0001, relwidth=.412, relx=.5375, rely=.8)

    # Place options buttons
    # Country details relx when other buttons are available
    # relx=.0725
    # But now it's .3875 so it's centered
    view_country_details_button.place(relheight=.05, relwidth=.225, relx=.3875, rely=.825)

    # TODO: More User Profile Actions & Commands
    # send_message_button.place(relheight=0.05, relwidth=0.2, relx=0.295 + .0125, rely=0.825)
    # edit_account_button.place(relheight=0.05, relwidth=0.2, relx=0.505 + .0125, rely=0.825)
    # delete_account_button.place(relheight=0.05, relwidth=0.2, relx=0.715 + .0125, rely=0.825)

    # Display user data
    is_public: bool = user["Privacy"] in ("Public", "Private Compositions")
    if user["Credentials"]["Username"] == User.logged_in_user["Credentials"]["Username"] or is_public:
        # Nicely Format Birth Date
        user_birth_date: str = Misc.format_date(year=user['Birth Date']['Year'],
                                                month=user['Birth Date']['Month'],
                                                day=user['Birth Date']['Day'],
                                                with_day=True)
        # Config all data labels
        user_profile_first_name_data_label.config(text=user["Name"]["First Name"])
        user_profile_last_name_data_label.config(text=user["Name"]["Last Name"])
        user_profile_nickname_data_label.config(text=user["Name"]["Nickname"])
        user_profile_gender_data_label.config(text=user["Gender"])
        user_profile_country_origin_data_label.config(text=user['Location']['Country Of Origin'])
        user_profile_state_origin_data_label.config(text=user['Location']['State Of Origin'])
        user_profile_country_residence_data_label.config(text=user['Location']['Country Of Residence'])
        user_profile_state_residence_data_label.config(text=user['Location']['State Of Residence'])
        user_profile_birth_date_data_label.config(text=user_birth_date)

        user_age: int = User.get_user_age(year=user['Birth Date']['Year'],
                                          month=user['Birth Date']['Month'],
                                          day=user['Birth Date']['Day'])

        user_profile_current_age_data_label.config(text='{:,}'.format(user_age))

        # TODO: Enable Viewing Profiles of Other Users
        # if user['Credentials']['Username'] == User.logged_in_user['Credentials']['Username'] or user_age >= 18:
        #     user_profile_current_age_data_label.config(text='{:,}'.format(user_age))
        # elif user_age < 18:
        #     user_profile_current_age_data_label.config(text='{:,}'.format(user_age) + " - Warning: Minor user! "
        #                                                                               "Approach with caution!")

        # Constants
        relx: float = .051
        rely: float = .225
        relheight: float = .05

        user_profile_first_name_label.place(relheight=relheight, relwidth=0.125,
                                            relx=relx, rely=rely)
        user_profile_last_name_label.place(relheight=relheight, relwidth=0.125,
                                           relx=relx, rely=rely + relheight)
        user_profile_nickname_label.place(relheight=relheight, relwidth=0.125,
                                          relx=relx, rely=rely + relheight * 2)
        user_profile_gender_label.place(relheight=relheight, relwidth=0.215,
                                        relx=relx, rely=rely + relheight * 3)
        user_profile_country_origin_label.place(relheight=relheight, relwidth=0.215,
                                                relx=relx, rely=rely + relheight * 4)
        user_profile_state_origin_label.place(relheight=relheight, relwidth=0.215,
                                              relx=relx, rely=rely + relheight * 5)
        user_profile_country_residence_label.place(relheight=relheight, relwidth=0.215,
                                                   relx=relx, rely=rely + relheight * 6)
        user_profile_state_residence_label.place(relheight=relheight, relwidth=0.215,
                                                 relx=relx, rely=rely + relheight * 7)
        user_profile_birth_date_label.place(relheight=relheight, relwidth=0.215,
                                            relx=relx, rely=rely + relheight * 8)
        user_profile_current_age_label.place(relheight=relheight, relwidth=0.215,
                                             relx=relx, rely=rely + relheight * 9)

        user_profile_first_name_data_label.place(relheight=relheight, relwidth=0.7725,
                                                 relx=relx + .125, rely=rely)
        user_profile_last_name_data_label.place(relheight=relheight, relwidth=0.7725,
                                                relx=relx + .125, rely=rely + relheight)
        user_profile_nickname_data_label.place(relheight=relheight, relwidth=0.7725,
                                               relx=relx + .125, rely=rely + relheight * 2)
        user_profile_gender_data_label.place(relheight=relheight, relwidth=0.6825,
                                             relx=relx + .215, rely=rely + relheight * 3)
        user_profile_country_origin_data_label.place(relheight=relheight, relwidth=0.6825,
                                                     relx=relx + .215, rely=rely + relheight * 4)
        user_profile_state_origin_data_label.place(relheight=relheight, relwidth=0.6825,
                                                   relx=relx + .215, rely=rely + relheight * 5)
        user_profile_country_residence_data_label.place(relheight=relheight, relwidth=0.6825,
                                                        relx=relx + .215, rely=rely + relheight * 6)
        user_profile_state_residence_data_label.place(relheight=relheight, relwidth=0.6825,
                                                      relx=relx + .215, rely=rely + relheight * 7)
        user_profile_birth_date_data_label.place(relheight=relheight, relwidth=0.6825,
                                                 relx=relx + .215, rely=rely + relheight * 8)
        user_profile_current_age_data_label.place(relheight=relheight, relwidth=0.6825,
                                                  relx=relx + .215, rely=rely + relheight * 9)

        # TODO: Implement Hidden Words (Easter Eggs) System
        # # Only if at least 1 hidden word found
        # user_profile_hidden_word_found_label.place(relheight=relheight, relwidth=0.215,
        #                                            relx=relx, rely=rely + relheight * 10)
        # user_profile_hidden_word_found_data_label.place(relheight=relheight, relwidth=0.6825,
        #                                                 relx=relx + .215, rely=rely + relheight * 10)

        # Config country details labels
        config_country_details_labels(country_of_origin=user['Location']['Country Of Origin'],
                                      state_of_origin=user['Location']['State Of Origin'],
                                      country_of_residence=user['Location']['Country Of Residence'],
                                      state_of_residence=user['Location']['State Of Residence'])

    else:
        # TODO: Display Profiles of Private / Private Details Users
        # Display user private or something...
        raise NotImplementedError("Unsupported Operation.")

    return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)


def display_country_details():
    """Displays the given countries' Details Menu
    """

    forget_all_widgets(root)
    root.focus()

    quit_button.place(relheight=0.05, relwidth=0.05, relx=0.925, rely=0.05)

    country_details_menu_label.place(relheight=0.15, relwidth=0.8, relx=0.1, rely=0.025)

    # Constants
    relheight: float = .05

    country_origin: str = User.user_profile_user["Location"]["Country Of Origin"]
    country_residence: str = User.user_profile_user["Location"]["Country Of Residence"]

    state_origin: str = User.user_profile_user["Location"]["State Of Origin"]
    state_residence: str = User.user_profile_user["Location"]["State Of Residence"]

    is_same_location: bool = True if country_origin == country_residence and state_origin == state_residence else False

    if not is_same_location:
        # Constants for country of origin
        relx: float = .06
        rely: float = .215
        # Country of origin
        country_details_origin_labelframe.place(relheight=0.36, relwidth=0.9, relx=0.05, rely=0.175)
        # Country of origin title labels
        # Row 1
        country_details_origin_name_label.place(relheight=relheight, relwidth=0.13,
                                                relx=relx, rely=rely)
        country_details_origin_capital_label.place(relheight=relheight, relwidth=0.13,
                                                   relx=relx, rely=rely + relheight)
        country_details_origin_state_name_label.place(relheight=relheight, relwidth=0.13,
                                                      relx=relx, rely=rely + relheight * 2)
        country_details_origin_continent_label.place(relheight=relheight, relwidth=0.13,
                                                     relx=relx, rely=rely + relheight * 3)
        country_details_origin_currency_label.place(relheight=relheight, relwidth=0.13,
                                                    relx=relx, rely=rely + relheight * 4)
        country_details_origin_phone_prefix_label.place(relheight=relheight, relwidth=0.13,
                                                        relx=relx, rely=rely + relheight * 5)
        # Row 2
        country_details_origin_state_name_ISO2_label.place(relheight=relheight, relwidth=0.21,
                                                           relx=relx + .45, rely=rely + relheight * 2)
        country_details_origin_continent_ISO2_label.place(relheight=relheight, relwidth=0.21,
                                                          relx=relx + .45, rely=rely + relheight * 3)
        country_details_origin_name_ISO2_label.place(relheight=relheight, relwidth=0.25,
                                                     relx=relx + .41, rely=rely + relheight * 4)
        country_details_origin_name_ISO3_label.place(relheight=relheight, relwidth=0.25,
                                                     relx=relx + .41, rely=rely + relheight * 5)
        # Country of origin data labels
        # Row 1
        country_details_origin_name_data_label.place(relheight=relheight, relwidth=0.75,
                                                     relx=relx + .135, rely=rely)
        country_details_origin_capital_data_label.place(relheight=relheight, relwidth=0.75,
                                                        relx=relx + .135, rely=rely + relheight)
        country_details_origin_state_name_data_label.place(relheight=relheight, relwidth=0.315,
                                                           relx=relx + .135, rely=rely + relheight * 2)
        country_details_origin_continent_data_label.place(relheight=relheight, relwidth=0.315,
                                                          relx=relx + .135, rely=rely + relheight * 3)
        country_details_origin_currency_data_label.place(relheight=relheight, relwidth=0.275,
                                                         relx=relx + .135, rely=rely + relheight * 4)
        country_details_origin_phone_prefix_data_label.place(relheight=relheight, relwidth=0.275,
                                                             relx=relx + .135, rely=rely + relheight * 5)
        # Row 2
        country_details_origin_state_name_ISO2_data_label.place(relheight=relheight, relwidth=0.22,
                                                                relx=relx + .41 + .255, rely=rely + relheight * 2)
        country_details_origin_continent_ISO2_data_label.place(relheight=relheight, relwidth=0.22,
                                                               relx=relx + .41 + .255, rely=rely + relheight * 3)
        country_details_origin_name_ISO2_data_label.place(relheight=relheight, relwidth=0.22,
                                                          relx=relx + .45 + .215, rely=rely + relheight * 4)
        country_details_origin_name_ISO3_data_label.place(relheight=relheight, relwidth=0.22,
                                                          relx=relx + .45 + .215, rely=rely + relheight * 5)

        # Constants for country of residence
        rely: float = .215 + .36
        # Country of residence
        country_details_residence_labelframe.place(relheight=0.36, relwidth=0.9, relx=0.05, rely=0.535)
        # Country of residence title labels
        # Row 1
        country_details_residence_name_label.place(relheight=relheight, relwidth=0.13,
                                                   relx=relx, rely=rely)
        country_details_residence_capital_label.place(relheight=relheight, relwidth=0.13,
                                                      relx=relx, rely=rely + relheight)
        country_details_residence_state_name_label.place(relheight=relheight, relwidth=0.13,
                                                         relx=relx, rely=rely + relheight * 2)
        country_details_residence_continent_label.place(relheight=relheight, relwidth=0.13,
                                                        relx=relx, rely=rely + relheight * 3)
        country_details_residence_currency_label.place(relheight=relheight, relwidth=0.13,
                                                       relx=relx, rely=rely + relheight * 4)
        country_details_residence_phone_prefix_label.place(relheight=relheight, relwidth=0.13,
                                                           relx=relx, rely=rely + relheight * 5)
        # Row 2
        country_details_residence_state_name_ISO2_label.place(relheight=relheight, relwidth=0.21,
                                                              relx=relx + .45, rely=rely + relheight * 2)
        country_details_residence_continent_ISO2_label.place(relheight=relheight, relwidth=0.21,
                                                             relx=relx + .45, rely=rely + relheight * 3)
        country_details_residence_name_ISO2_label.place(relheight=relheight, relwidth=0.25,
                                                        relx=relx + .41, rely=rely + relheight * 4)
        country_details_residence_name_ISO3_label.place(relheight=relheight, relwidth=0.25,
                                                        relx=relx + .41, rely=rely + relheight * 5)
        # Country of residence data labels
        # Row 1
        country_details_residence_name_data_label.place(relheight=relheight, relwidth=0.75,
                                                        relx=relx + .135, rely=rely)
        country_details_residence_capital_data_label.place(relheight=relheight, relwidth=0.75,
                                                           relx=relx + .135, rely=rely + relheight)
        country_details_residence_state_name_data_label.place(relheight=relheight, relwidth=0.315,
                                                              relx=relx + .135, rely=rely + relheight * 2)
        country_details_residence_continent_data_label.place(relheight=relheight, relwidth=0.315,
                                                             relx=relx + .135, rely=rely + relheight * 3)
        country_details_residence_currency_data_label.place(relheight=relheight, relwidth=0.275,
                                                            relx=relx + .135, rely=rely + relheight * 4)
        country_details_residence_phone_prefix_data_label.place(relheight=relheight, relwidth=0.275,
                                                                relx=relx + .135, rely=rely + relheight * 5)
        # Row 2
        country_details_residence_state_name_ISO2_data_label.place(relheight=relheight, relwidth=0.22,
                                                                   relx=relx + .41 + .255, rely=rely + relheight * 2)
        country_details_residence_continent_ISO2_data_label.place(relheight=relheight, relwidth=0.22,
                                                                  relx=relx + .41 + .255, rely=rely + relheight * 3)
        country_details_residence_name_ISO2_data_label.place(relheight=relheight, relwidth=0.22,
                                                             relx=relx + .45 + .215, rely=rely + relheight * 4)
        country_details_residence_name_ISO3_data_label.place(relheight=relheight, relwidth=0.22,
                                                             relx=relx + .45 + .215, rely=rely + relheight * 5)

        return_to_profile_button.place(relheight=0.05, relwidth=0.2, relx=0.4, rely=0.9)
    else:  # is same location
        # Constants for same location
        relx: float = .0525
        rely: float = .215
        # Labelframe
        country_details_origin_labelframe.place(relheight=0.72, relwidth=0.9, relx=0.05, rely=0.175)
        # Same country label
        same_country_label.place(relheight=relheight, relwidth=.8, relx=.1, rely=rely)
        same_country_label.lift()
        # Title labels
        # Section 1
        country_details_origin_name_label.place(relheight=relheight, relwidth=0.15,
                                                relx=relx, rely=rely + relheight)
        country_details_origin_capital_label.place(relheight=relheight, relwidth=0.15,
                                                   relx=relx, rely=rely + relheight * 2)
        country_details_origin_state_name_label.place(relheight=relheight, relwidth=0.15,
                                                      relx=relx, rely=rely + relheight * 3)
        country_details_origin_continent_label.place(relheight=relheight, relwidth=0.15,
                                                     relx=relx, rely=rely + relheight * 4)
        country_details_origin_currency_label.place(relheight=relheight, relwidth=0.15,
                                                    relx=relx, rely=rely + relheight * 5)
        country_details_origin_phone_prefix_label.place(relheight=relheight, relwidth=0.15,
                                                        relx=relx, rely=rely + relheight * 6)
        # Section 2
        country_details_origin_state_name_ISO2_label.place(relheight=relheight, relwidth=0.25,
                                                           relx=relx, rely=rely + relheight * 7)
        country_details_origin_continent_ISO2_label.place(relheight=relheight, relwidth=0.25,
                                                          relx=relx, rely=rely + relheight * 8)
        country_details_origin_name_ISO2_label.place(relheight=relheight, relwidth=0.25,
                                                     relx=relx, rely=rely + relheight * 9)
        country_details_origin_name_ISO3_label.place(relheight=relheight, relwidth=0.25,
                                                     relx=relx, rely=rely + relheight * 10)
        # Data labels
        # Section 1
        country_details_origin_name_data_label.place(relheight=relheight, relwidth=0.741,
                                                     relx=relx + .155, rely=rely + relheight)
        country_details_origin_capital_data_label.place(relheight=relheight, relwidth=0.741,
                                                        relx=relx + .155, rely=rely + relheight * 2)
        country_details_origin_state_name_data_label.place(relheight=relheight, relwidth=0.741,
                                                           relx=relx + .155, rely=rely + relheight * 3)
        country_details_origin_continent_data_label.place(relheight=relheight, relwidth=0.741,
                                                          relx=relx + .155, rely=rely + relheight * 4)
        country_details_origin_currency_data_label.place(relheight=relheight, relwidth=0.741,
                                                         relx=relx + .155, rely=rely + relheight * 5)
        country_details_origin_phone_prefix_data_label.place(relheight=relheight, relwidth=0.741,
                                                             relx=relx + .155, rely=rely + relheight * 6)
        # Section 2
        country_details_origin_state_name_ISO2_data_label.place(relheight=relheight, relwidth=0.633,
                                                                relx=relx + .255, rely=rely + relheight * 7)
        country_details_origin_continent_ISO2_data_label.place(relheight=relheight, relwidth=0.633,
                                                               relx=relx + .255, rely=rely + relheight * 8)
        country_details_origin_name_ISO2_data_label.place(relheight=relheight, relwidth=0.633,
                                                          relx=relx + .255, rely=rely + relheight * 9)
        country_details_origin_name_ISO3_data_label.place(relheight=relheight, relwidth=0.633,
                                                          relx=relx + .255, rely=rely + relheight * 10)
        # Others Section
        user_profile_options_label.place(relheight=.05, relwidth=.075, relx=.4625, rely=.775)
        user_profile_separator_2.place(relheight=.0001, relwidth=.4125, relx=.05, rely=.8)
        user_profile_separator_3.place(relheight=.0001, relwidth=.412, relx=.5375, rely=.8)
        user_profile_options_label.lift()
        user_profile_separator_2.lift()
        user_profile_separator_3.lift()

        return_to_profile_button.place(relheight=.05, relwidth=.225, relx=.3875, rely=.825)

    return_to_main_menu_button.place(relheight=0.05, relwidth=0.2, relx=0.775, rely=0.9)
