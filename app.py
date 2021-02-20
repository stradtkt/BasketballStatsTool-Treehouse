import copy
from os import system, name
from constants import TEAMS, PLAYERS


def clear_screen():
    """Clear the unwanted items from the screen"""
    system("cls" if name == "nt" else "clear")


def clean_data(player_data):
    """Cleans the data for experience and guardians"""
    for player in player_data:
        player['height'] = int(player['height'][:2])
        player['inches'] = player['height'][3:]
        player['guardians'] = player['guardians'].split(' and ')

        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
    return player_data


def menu():
    print("""
    \nBasketball Team Stats Tool
    \r---- Menu ----
    \rHere are your choices
    \r1) Display Team Stats
    \r2) Quit
    \rType 'cls' for Windows or 'clear' for Mac or Linux to clear your screen
    """)


def submenu():
    """Show the team options to choose from"""
    for i, team in enumerate(TEAMS, start=1):
        print(f"{i}) {team}")


def user_input():
    """Take the user input and navigate the menu"""
    pass


def split_teams(player_list):
    """Splits the teams when you want to set up a team to have different players"""
    pass


def separate_based_on_experience(player_data):
    """Separate the teams so there is an even amount of experienced and inexperienced players on the team"""
    experienced = [player for player in player_data if player['experienced']]
    not_experienced = [player for player in player_data if not player['experienced']]


def team_roster(team, players):
    players_on_team = []
    for player in players:
        if player['name'] in team['roster']:
            players_on_team.append(player)
    return players_on_team


def average_height(team, players):
    """Calculate the average height of a team"""
    heights_of_players = []
    for player in team_roster(team, players):
        heights_of_players.append(player['height'])
    return sum(heights_of_players) / len(heights_of_players)


def guardian_names():
    """Make the guardian names look neat"""
    pass


if __name__ == '__main__':
    menu()
    user_input()
