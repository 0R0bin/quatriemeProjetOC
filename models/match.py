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

    def serialized(self):
        """Transform Match object into JSON readable dictionnary"""
        player1_serialized = self.player1.serialized()
        player2_serialized = self.player1.serialized()
        tuple_serialized = ([player1_serialized, self.score1], [player2_serialized, self.score2])
        serialized_match = {
            "Player1": player1_serialized,
            "Player2": player2_serialized,
            "Score1": self.score1,
            "Score2": self.score2,
            "Tuple": tuple_serialized
        }
        return serialized_match

    def deserialized(self, object_json):
        """Transfom match from db into match object"""
        self.player1 = object_json['Player1']
        self.player2 = object_json['Player2']
        self.score1 = object_json['Score1']
        self.score2 = object_json['Score2']
        self.tuple_match = object_json['Tuple']
        return "Round crée"

    def __str__(self):
        return "Joueur 1 : " + self.player1.name + " Joueur 2 : " + self.player2.name
