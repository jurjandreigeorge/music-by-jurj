"""
Main Module; Consists of the main loop of the app and the other necessary operations to start the app properly
"""


def main():
    """Main Function; Does all the imports & all the required steps to gracefully start the app
    """
    import LoadingScreen
    LoadingScreen.display_loading_menu()
    # Check OS to be Windows; Create error box and quit app otherwise
    import ErrorChecking
    ErrorChecking.check_os()
    LoadingScreen.update_loading_menu()  # 1st call
    # Check for missing files
    LoadingScreen.update_loading_menu()  # 2nd call
    # Check for corrupt data
    LoadingScreen.update_loading_menu()  # 3rd call
    # Import Stats
    import Stats
    LoadingScreen.update_loading_menu()  # 4th call
    # Import GUI
    import GUI
    LoadingScreen.update_loading_menu()  # 5th call
    # Import User
    import User
    # Read users
    User.read_users_from_file()
    User.read_logged_user_from_file()
    # Import Composition
    import Composition  # Add to loading screen
    # Initiate composers list if any user logged in
    if User.is_logged_in:
        Composition.update_composer_list()
    # Login last user if necessary
    if User.is_logged_in:
        User.remember_me.set(True)
    LoadingScreen.update_loading_menu()  # 6th call
    # import Settings
    import Settings
    # Read & Set Settings
    Settings.read_remember_settings_value()
    Settings.read_preset_settings()
    Settings.set_initial_settings()
    LoadingScreen.update_loading_menu()  # 7th call
    # Config Stats
    Stats.initiate_stats()
    # Increment "App used" stat value
    Stats.app_used_counter.set(Stats.app_used_counter.get() + 1)
    LoadingScreen.update_loading_menu()  # 8th call
    # Mark last "Loading..." operation as "Done"

    # DEBUG ONLY
    # import MainWindow
    # MainWindow.sink_all_labels(MainWindow.root)

    # Start proper app
    GUI.display_main_menu()
    GUI.root.mainloop()


if __name__ == "__main__":
    main()
