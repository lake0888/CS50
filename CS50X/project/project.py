import requests
import sys
from tabulate import tabulate
import team
import player
import match
import random

def main():
    params = {
        "key": "test85g57",
        "season_id": "1625",
    }

    is_simulated = False

    #SAVE TEAMS
    url = 'https://api.football-data-api.com/league-teams'
    teams = create_teams(url, params)

    #ADD PLAYERS
    url = 'https://api.football-data-api.com/league-players'
    add_players(teams, url, params)

    players = []

    title = "ENGLISH PREMIER LEAGUE 2018-2019"

    while True:
        option = main_menu(title)
        if option == 6:
            sys.exit("EXIT")
        elif option == 5:
            is_simulated = False
            title = "ENGLISH PREMIER LEAGUE 2018-2019"
        elif option == 1:
            header = ['Position', 'Name', 'Points', 'Wins', 'Draws', 'Losses', 'Goals', 'Conceded', 'Difference']
            if is_simulated == False:
                url = 'https://api.football-data-api.com/league-tables'
                show_table(url, params, header)
            else:
                show_table_simulated(teams, header)
        elif option == 2 or option == 3:
            header = ['Position', 'Name', 'Team', 'Matchs']
            if option == 2:
                header.append('Goals')
                if is_simulated == False:
                    url = 'https://api.football-data-api.com/league-season'
                    show_top_scorers(teams, url, params, header)
                else:
                    sort_scores(players)
                    show_top_scorers_simulated(players, header)
            else:
                header.append('Assists')
                if is_simulated == False:
                    url = 'https://api.football-data-api.com/league-season'
                    show_top_assists(teams, url, params, header)
                else:
                    sort_assists(players)
                    show_top_assists_simulated(players, header)
        else:
            header = ['Position', 'Name', 'Team', 'Matchs']
            title = input("ENTER THE SEASON ")
            matches = simulate_league(teams)
            players = get_players(teams)

            is_simulated = True
            sort_teams(teams)

def main_menu(title):
    while True:
        try:
            print("\nTITLE: " + title)
            print("1 - TABLE")
            print("2 - TOP TEN SCORERS")
            print("3 - TOP TEN ASSISTS")
            print("4 - SIMULATE NEW LEAGUE")
            print("5 - DEFAULT LEAGUE")
            print("6 - EXIT")

            option = int(input("\nSELECT OPTION FROM MENU "))

            if option < 1 or option > 6:
                continue
        except ValueError:
            pass
        except (KeyboardInterrupt, EOFError):
            return 6
        else:
            return option

def show_table(url, params, header):
    table = []
    response = requests.get(url, params=params)
    data = response.json()['data']['league_table']
    for team in data:
        c_team = [
            team['position'],
            team['name'],
            team['points'],
            team['seasonWins_overall'],
            team['seasonDraws_overall'],
            team['seasonLosses_overall'],
            team['seasonGoals'],
            team['seasonConceded_away'] + team['seasonConceded_home'],
            team['seasonGoalDifference']
        ]
        table.append(c_team)

    print(tabulate(table, header, tablefmt="grid"))

def show_top_scorers(teams, url, params, header):
    table = []
    response = requests.get(url, params=params)
    data = response.json()['data']['top_scorers']
    i = 0
    while i < 10:
        pos = get_team(teams, data[i]['club_team_id'])
        if pos != -1:
            c_scorer = [
                i + 1,
                data[i]['full_name'],
                teams[pos].get_name(),
                data[i]['appearances_overall'],
                data[i]['goals_overall']
            ]
            table.append(c_scorer)
        i += 1
    print(tabulate(table, header, tablefmt="grid"))


def show_top_assists(teams, url, params, header):
    table = []
    response = requests.get(url, params=params)
    data = response.json()['data']['top_assists']
    i = 0
    while i < 10:
        pos = get_team(teams, data[i]['club_team_id'])
        if pos != -1:
            c_assist = [
                i + 1,
                data[i]['full_name'],
                teams[pos].get_name(),
                data[i]['appearances_overall'],
                data[i]['assists_overall']
            ]
            table.append(c_assist)
        i += 1
    print(tabulate(table, header, tablefmt="grid"))

def create_teams(url, params):
    teams = []
    response = requests.get(url, params)
    data = response.json()['data']
    i = 0
    while i < len(data):
        id = data[i]['id']
        name = data[i]['name']

        c_team = team.Team(id, name)
        teams.append(c_team)
        i += 1
    return teams

def get_team(teams, id):
    i = 0
    while i < len(teams):
        c_team = teams[i]
        c_id = c_team.get_id()
        if c_id == id:
            return i
        i += 1
    return -1

def add_players(teams, url, params):
    response = requests.get(url, params=params)
    data = response.json()['data']

    i = 0
    while i < len(data):
        current_player = data[i]
        club_id = current_player['club_team_id']
        pos = get_team(teams, club_id)
        if pos != -1:
            add_player(teams[pos], current_player)
        i += 1

def add_player(c_team, current_player):
    id = current_player['id']
    name = current_player['full_name']
    birthday = current_player['birthday']
    position = current_player['position']
    nationality = current_player['nationality']

    new_player = player.Player(id, name, birthday, position, c_team.get_name(), nationality)
    players = list(c_team.get_players())
    players.append(new_player)
    c_team.set_players(players)

def simulate_league(teams):
    # there are 20 teams so to know how many matches needs the league is factorial(20 - 1) * 2
    # cant_matches = factorial(20 - 1) * 2
    matches = []
    i = 0
    while i < len(teams):
        home = teams[i]
        j = 0
        while j < len(teams):
            visitor = teams[j]

            if home.get_id() != visitor.get_id():
                goals_home = random.randint(0, 4)
                goals_visitor = random.randint(0, 3)

                assits_home = random.randint(0, goals_home)
                assits_visitor = random.randint(0, goals_visitor)

                # SET GOALS TO THE PLAYERS
                # HOME
                set_GoaltoPlayers(home.get_players(), goals_home)
                set_AssisttoPlayers(home.get_players(), assits_home)
                set_Appearance(home.get_players())
                # VISITOR
                set_GoaltoPlayers(visitor.get_players(), goals_visitor)
                set_AssisttoPlayers(home.get_players(), assits_visitor)
                set_Appearance(visitor.get_players())

                # SET POINTS TO THE TEAM
                if goals_home > goals_visitor:
                    home.set_Points(home.get_Points() + 3)

                    home.set_Wins(home.get_Wins() + 1)
                    visitor.set_Losses(visitor.get_Losses() + 1)
                elif goals_home < goals_visitor:
                    visitor.set_Points(visitor.get_Points() + 3)

                    visitor.set_Wins(visitor.get_Wins() + 1)
                    home.set_Losses(home.get_Losses() + 1)
                else:
                    home.set_Points(home.get_Points() + 1)
                    visitor.set_Points(visitor.get_Points() + 1)

                    home.set_Draws(home.get_Draws() + 1)
                    visitor.set_Draws(visitor.get_Draws() + 1)


                home.set_cant_match(home.get_cant_match() + 1)
                visitor.set_cant_match(visitor.get_cant_match() + 1)

                home.set_Goals(home.get_Goals() + goals_home)
                home.set_Conceded(home.get_Conceded() + goals_visitor)

                visitor.set_Goals(visitor.get_Goals() + goals_visitor)
                visitor.set_Conceded(visitor.get_Conceded() + goals_home)

                new_match = match.Match(home, visitor, goals_home, goals_visitor)
                matches.append(new_match)

            j += 1
        i += 1
    return matches

def exists_match(matches, home, visitor):
    i = 0
    while i < len(matches):
        c_home = matches[i].get_Home()
        c_visitor = matches[i].get_Visitor()
        cant_match = matches[i].get_Cant_match()

        if (c_home == home or c_home == visitor) and (c_visitor == home or c_visitor == visitor) and cant_match == 2:
            return True
        i += 1
    return False

def set_Appearance(players):
    i = 0
    while i < len(players):
        player = players[i]
        player.set_appearance(player.get_appearance() + 1)
        i += 1

def set_GoaltoPlayers(players, goals):
    val = len(players)
    i = 0
    while i < goals:
        if val != 0:
            pos = random.randint(0, val - 1)
            player = players[pos]
            player.set_goals(player.get_goals() + 1)
        i += 1

def set_AssisttoPlayers(players, goals):
    val = len(players)
    i = 0
    while i < goals:
        if val != 0:
            pos = random.randint(0, val - 1)
            player = players[pos]
            player.set_assits(player.get_assists() + 1)
        i += 1

def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)

def get_players(teams):
    players = []
    i = 0
    while i < len(teams):
        c_players = list(teams[i].get_players())
        players.extend(c_players)
        i += 1
    return players

def show_table_simulated(teams, header):
    table = []
    i = 0
    while i < len(teams):
        team = teams[i]
        c_team = [
            i + 1,
            team.get_name(),
            team.get_Points(),
            team.get_Wins(),
            team.get_Draws(),
            team.get_Losses(),
            team.get_Goals(),
            team.get_Conceded(),
            team.get_Goals() - team.get_Conceded()
        ]
        table.append(c_team)
        i += 1

    print(tabulate(table, header, tablefmt="grid"))

def show_top_scorers_simulated(players, header):
    table = []
    i = 0
    while i < 10:
        player = players[i]
        c_player = [
            i + 1,
            player.get_full_name(),
            player.get_club(),
            player.get_appearance(),
            player.get_goals()
        ]
        table.append(c_player)
        i += 1
    print(tabulate(table, header, tablefmt="grid"))


def show_top_assists_simulated(players, header):
    table = []
    i = 0
    while i < 10:
        player = players[i]
        c_player = [
            i + 1,
            player.get_full_name(),
            player.get_club(),
            player.get_appearance(),
            player.get_assists()
        ]
        table.append(c_player)
        i += 1
    print(tabulate(table, header, tablefmt="grid"))

# SORT BY POINT
def sort_teams(teams):
    i = 0
    while i < len(teams):
        j = i + 1
        while j < len(teams):
            x = teams[i].get_Points()
            y = teams[j].get_Points()
            if x < y:
                temp = teams[i]
                teams[i] = teams[j]
                teams[j] = temp
            j += 1
        i += 1

def sort_scores(players):
    i = 0
    while i < len(players):
        j = i + 1
        while j < len(players):
            x = players[i].get_goals()
            y = players[j].get_goals()
            if x < y:
                temp = players[i]
                players[i] = players[j]
                players[j] = temp
            j += 1
        i += 1

def sort_assists(players):
    i = 0
    while i < len(players):
        j = i + 1
        while j < len(players):
            x = players[i].get_assists()
            y = players[j].get_assists()
            if x < y:
                temp = players[i]
                players[i] = players[j]
                players[j] = temp
            j += 1
        i += 1

if __name__ == "__main__":
    main()