class Team:
    def __init__(self, club_id, name, players = [], cant_match = 0, points = 0, seasonWins = 0, seasonDraws = 0, seasonLosses = 0, seasonGoals = 0, seasonConceded = 0):
        self.club_id = club_id
        self.name = name
        self.players = players
        self.cant_match = cant_match
        self.points = points
        self.seasonWins = seasonWins
        self.seasonDraws = seasonDraws
        self.seasonLosses = seasonLosses
        self.seasonGoals = seasonGoals
        self.seasonConceded = seasonConceded

    def get_id(self):
        return self.club_id

    def set_id(self, id):
        self.club_id = id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_players(self):
        return self.players

    def set_players(self, players):
        self.players = players

    # MAX = 38
    def get_cant_match(self):
        return self.cant_match

    def set_cant_match(self, cant_match):
        self.cant_match = cant_match

    def get_Points(self):
        return self.points

    def set_Points(self, points):
        self.points = points

    def get_Wins(self):
        return self.seasonWins

    def set_Wins(self, wins):
        self.seasonWins = wins

    def get_Draws(self):
        return self.seasonDraws

    def set_Draws(self, draws):
        self.seasonDraws = draws

    def get_Losses(self):
        return self.seasonLosses

    def set_Losses(self, losses):
        self.seasonLosses = losses

    def get_Goals(self):
        return self.seasonGoals

    def set_Goals(self, goals):
        self.seasonGoals = goals

    def get_Conceded(self):
        return self.seasonConceded

    def set_Conceded(self, goals):
        self.seasonConceded = goals

    def get_player(self, id):
        i = 0
        while i < len(self.players):
            current = self.players[i]
            c_id = current.get_ID()
            if c_id == id:
                return i
            i += 1
        return -1

    def info(self):
        print(self.name + " has " + str(len(self.players)) + " players")