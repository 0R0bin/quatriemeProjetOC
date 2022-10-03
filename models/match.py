"""Define the match"""

class Match:
    """Match"""

    def __init__(self, player1, player2):
        "Some informations about the Match"
        self.player1 = player1
        self.player2 = player2
    
    def __str__(self):
        return "Joueur 1 : " + self.player1.name + " Joueur 2 : " + self.player2.name
