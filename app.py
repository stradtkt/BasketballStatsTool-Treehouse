from constants import TEAMS, PLAYERS

option = input("Enter an option > ")


def menu():
    print("""\nBasketball Team Stats Tool\n""")
    print("""---- MENU ----\n""")
    print("""-- Here are your choices --\n
    1) Display Team Stats
    2) Help
    3) Quit
    """)


def help():
    pass


def user_input():
    """Take the user input and navigate the menu"""
    try:
        if option == 1:
            for key, value in TEAMS.items():
                print(int(key), ")", str(value))

    except ValueError as err:
        print("That is not a valid entry: {}".format(err))


def clear_screen():
    """Clear the unwanted items from the screen"""
    pass


def separate_based_on_experience():
    """Separate the teams so there is an even amount of experienced and inexperienced players on the team"""
    pass


def average_height():
    """Calculate the average height of a team"""
    pass


def guardian_names():
    """Make the guardian names look neat"""
    pass


if __name__ == '__main__':
    menu()
    user_input()
