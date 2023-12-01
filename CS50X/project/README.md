# ENGLISH PREMIER LEAGUE SOCCER SIMULATOR
#### Video Demo:  https://youtu.be/VPVIobyEQnM
#### Description:
This is a simulator of the English football league based on the teams formed in the 2018-2019 season. the teams have been uploaded from the web https://docs.footystats.org/.
A profile must be created on said website to obtain the data from its API. You have this football league, this season as an example because it is a free league, to obtain more you have to pay for that information. The id for this league is 1625, and the api key will be according to the created user, these data are necessary to download the information.

The system has a menu to view, the standings, the scoring leaders, the assist leaders, simulating a new league, and being able to see how that new information looks.

Files used

project.py . Our controller and main file.
team.py . Contains the Team class, where the team data is located
player.py . Contains the Player class, where the player data is located
match.py . Contains the Match class, where the data of the matches that are simulated are stored
test_project.py . Our test file, of three functions in particular

Modules used
request .Used to download information from the web.
tabulate. To display the information in table form
random .To simulate the matches
