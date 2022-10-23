"""Define the tournament"""


class Tournament:
    """Tournament"""

    def __init__(self, name, place, date, timeplay, description, nb_rounds=4):
        "Some informations about the tournament"
        self.name = name
        self.place = place
        self.date = date
        self.timeplay = timeplay
        self.description = description
        self.nb_rounds = nb_rounds
        self.rounds = []
        self.players = []

    def serialized(self):
        """Transform Tournament object into JSON readable dictionnary"""
        serialized_tournament = {
            "Name": self.name,
            "Place": self.place,
            "Date": self.date,
            "Mode": self.timeplay,
            "Description": self.description,
            "NombreRounds": self.nb_rounds,
            "ListeRounds": self.rounds,
            "ListeJoueurs": self.players
        }
        return serialized_tournament

    def deserialized(self, object_json):
        """Transfom tournament from db into tournament object"""
        self.name = object_json['Name']
        self.place = object_json['Place']
        self.date = object_json['Date']
        self.timeplay = object_json['Mode']
        self.description = object_json['Description']
        self.nb_rounds = object_json['NombreRounds']
        self.rounds = object_json['ListeRounds']
        self.players = object_json['ListeJoueurs']
        return "Tournoi crée"

    def add_rounds(self, round_to_add):
        """Add round to the list for db"""
        self.rounds.append(round_to_add)

    def add_players(self, player_to_add):
        """Add players to the list for db"""
        self.players.append(player_to_add)
