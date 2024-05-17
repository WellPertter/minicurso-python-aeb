class Player:

    def __init__(self, name, club, nationality):
        self.name = name
        self.club = club
        self.nationality = nationality

    def get_nationality(self):
        return self.nationality