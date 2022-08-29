"""Define the player"""

class Player:
    """Player"""

    def __init__(self, name, nickname, dob, gender, ranking, score):
        "Some informations about the player"
        self.name = name
        self.nickname = nickname
        self.dob = dob
        self.gender = gender
        self.ranking = ranking
        self.score = score

    def getRanking(self):
        """Return ranking & ranking_temp of a player"""
        if self.score == 0:
            return self.ranking
        else:
            return self.score, self.ranking