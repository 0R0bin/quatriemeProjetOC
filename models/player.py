"""Define the player"""

class Player:
    """Player"""

    def __init__(self, name, nickname, dob, gender, ranking_world):
        "Some informations about the player"
        self.name = name
        self.nickname = nickname
        self.dob = dob
        self.gender = gender
        self.ranking_world = ranking_world
        self.ranking_tournament = 0
