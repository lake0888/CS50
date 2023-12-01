from decimal import DivisionByZero

class Player:
    def __init__(self, id, full_name, birthday, position, club, nationality, appearance = 0, goals = 0, assists = 0, conceded = 0):
        self.id = id
        self.full_name = full_name
        self.birthday = birthday
        self.position = position
        self.club = club
        self.nationality = nationality
        self.appearance = appearance
        self.goals = goals
        self.assists = assists
        self.conceded = conceded

    #GET AND SET ID
    def get_ID(self):
        return self.id

    def set_ID(self, id):
        self.id = id

    # GET AND SET FULLNAME
    def get_full_name(self):
        return self.full_name

    def set_full_name(self, full_name):
        self.full_name = full_name

    # GET AND SET BIRTHDAY
    def get_birthday(self):
        return self.birthday

    def set_birthday(self, birthday):
        self.birthday = birthday

    # GET AND SET POSITION
    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    # GET AND SET CLUB
    def get_club(self):
        return self.club

    def set_club(self, club):
        self.club = club

    # GET AND SET NATIONALITY
    def get_nationality(self):
        return self.nationality

    def set_nationality(self, nationality):
        self.nationality = nationality

    # GET AND SET APPEARANCE
    def get_appearance(self):
        return self.appearance

    def set_appearance(self, appearance):
        self.appearance = appearance

    # GET AND SET GOAL
    def get_goals(self):
        return self.goals

    def set_goals(self, goals):
        self.goals = goals

    # GET AND SET ASSISTS
    def get_assists(self):
        return self.assists

    def set_assits(self, assits):
        self.assists = assits

    # GET AND SET CONCEDED
    def get_conceded(self):
        return self.conceded

    def set_conceded(self, conceded):
        self.conceded = conceded

    # AVERAGE GOL X MACTH
    def average_goal(self):
        if self.appearance == 0:
            raise DivisionByZero("APPEARANCE CANNOT BE 0")
        return self.goals/self.appearance

    # AVERAGE GOL CONCEDED X MATCH
    def average_conceded(self):
        if self.appearance == 0:
            raise DivisionByZero("APPEARANCE CANNOT BE 0")
        return self.conceded/self.appearance