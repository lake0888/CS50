class Match:
    def __init__(self, home, visitor, goals_home = 0, goals_visitor = 0, cant_match = 0):
        self.home = home
        self.visitor = visitor
        self.goals_home = goals_home
        self.goals_visitor = goals_visitor
        self.cant_match = cant_match

    #GET AND SET
    def get_Home(self):
        return self.home

    def set_Home(self, home):
        self.home = home

    def get_Visitor(self):
        return self.visitor

    def set_Visitor(self, visitor):
        self.visitor = visitor

    def get_Goals_home(self):
        return self.goals_home

    def set_Goals_home(self, goals):
        self.goals_home = goals

    def get_Goals_visitor(self):
        return self.goals_visitor

    def set_Goals_visitor(self, goals):
        self.goals_visitor = goals

    # MAX = 2
    def get_Cant_match(self):
        return self.cant_match

    def set_Cant_match(self, cant_match):
        self.cant_match = cant_match