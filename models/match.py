"""Define the match"""


class Match:
    """Match"""

    def __init__(self, player1, score1, player2, score2):
        "Some informations about the Match"
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2
        self.tuple_match = ([self.player1, self.score1], [self.player2, self.score2])

    def __str__(self):
        return "Joueur 1 : " + self.player1.name + " Joueur 2 : " + self.player2.name
