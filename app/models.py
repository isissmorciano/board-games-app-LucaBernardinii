class Game:
    def __init__(self, title, genre, year, players, id=None):
        self.id = id
        self.title = title
        self.genre = genre
        self.year = year
        self.players = players