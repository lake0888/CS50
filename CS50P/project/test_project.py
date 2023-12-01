from project import get_team
import team
from project import create_teams
from project import simulate_league
from project import factorial

params = {
        "key": "test85g57",
        "season_id": "1625",
    }

url = 'https://api.football-data-api.com/league-teams'

team1 = team.Team( 1, "Argentina")
team2 = team.Team(2, "Brazil")
team3 = team.Team(3, "France")

teams = [team1, team2, team3]

def test_get_team():
    assert get_team(teams, 3) == 2
    assert get_team(teams, 1) == 0

def test_create_teams():
    assert len(create_teams(url, params)) == 20
    assert len(create_teams(url, params)) != 12

def test_simulate_leagues():
    assert len(simulate_league(teams)) == factorial(len(teams))

