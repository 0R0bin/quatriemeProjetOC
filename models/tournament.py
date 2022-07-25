"""Define the tournament"""

class Tournament:
    """Tournament"""

    def __init__(self, name, place, date, rounds, players, timeplay, description, nb_rounds=4):
        "Some informations about the tournament"
        self.name = name
        self.place = place
        self.date = date
        self.rounds = rounds
        self.players = players
        self.timeplay = timeplay
        self.description = description
        self.nb_rounds = nb_rounds