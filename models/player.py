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

    def serialized(self):
        """Transform Player object into JSON readable dictionnary"""
        serialized_player = {
            "Name": self.name,
            "Nickname": self.nickname,
            "Dob": self.dob,
            "Gender": self.gender,
            "Ranking": self.ranking_world,
            "Ranking_Tournament": int(self.ranking_tournament)
        }
        return serialized_player

    def deserialized(self, object_json):
        """Transfom player from db into player object"""
        self.name = object_json['Name']
        self.nickname = object_json['Nickname']
        self.dob = object_json['Dob']
        self.gender = object_json['Gender']
        self.ranking_world = object_json['Ranking']
        self.ranking_tournament = object_json["Ranking_Tournament"]
        return "Joueur crée"

    def get_name(self):
        """Get name of the player"""
        return self.name

    def __str__(self):
        return "Nom : " + self.name + "Prénom : " + self.nickname + "Ranking : " + self.ranking_world
