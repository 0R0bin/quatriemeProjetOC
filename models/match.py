"""Define the match"""

import random

class Match:
    """Match"""

    def __init__(self, player1, score1, player2, score2):
        "Some informations about the Match"
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2
    
    def __str__(self):
        return "Joueur 1 : " + self.player1.name + " Joueur 2 : " + self.player2.name

    def randomn_winner(self):
        "Chose a random winner between the two players"
        result_possibilities = [1, 0.5, 0]
        self.score1 = random.choice(result_possibilities)
        if self.score1 == 1:
            self.score2 = 0
        elif self.score1 == 0.5:
            self.score2 = 0.5
        else:
            self.score2 = 1
        return ([self.player1.name, self.score1], [self.player2.name, self.score2])
