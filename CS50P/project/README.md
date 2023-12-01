# ENGLISH PREMIER LEAGUE SOCCER SIMULATOR
#### Video Demo:  https://youtu.be/VPVIobyEQnM
#### Description:
This is a simulator of the English football league based on the teams formed in the 2018-2019 season. the teams have been uploaded from the web https://docs.footystats.org/.
A profile must be created on said website to obtain the data from its API. You have this football league, this season as an example because it is a free league, to obtain more you have to pay for that information. The id for this league is 1625, and the api key will be according to the created user, these data are necessary to download the information.

The system has a menu to view, the standings, the scoring leaders, the assist leaders, simulating a new league, and being able to see how that new information looks.

The project shows a main menu with 6 options

1. Table (Shows the football league position table)
2. Top Ten Scores (Shows the top 10 scorers)
3. Top Ten Assists (Shows the first 10 attendees)
4. Simulate New League (Simulates a new league, in which the user has to create it, and the system does the rest)
5. Default League (Loads the initial league, the one obtained from the API)
6. Exit (Closes the system)

Files used
- project.py . This file is the main one, since it manages all the business logic of the system.
- team.py . Contains the Team class, where the Team data is located
- player.py . Contains the Player class, where the player data is located
- match.py . Contains the Match class, where the data of the matches that are simulated are stored
- test_project.py . Our test file, of three functions in particular

To run the simulation, the first thing that was done was to download all the teams and all the players of each team, since the league is made up of 20 teams and each team has several players. To save all this data, the team.py and player.py files have been used.

Later, to do the simulation, we have the match.py file, in which we will have the results of the matches. With these data, the final position table, the goalscoring leaders and assists leaders will be obtained.

Modules used
- request .Used to download information from the web.
- tabulate. To display the information in table form
- random .To simulate the matches
