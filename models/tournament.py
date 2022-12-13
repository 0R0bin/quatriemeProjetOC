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
        # If a field is null
        if self.name is None:
            self.name = "ToReload"
        if self.place is None:
            self.place = "ToReload"
        if self.date is None:
            self.date = "ToReload"
        if self.timeplay is None:
            self.timeplay = "ToReload"
        if self.description is None:
            self.description = "ToReload"
        if self.nb_rounds is None:
            self.nb_rounds = "ToReload"

        # Transform our object to a dictionnary with null safety
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

    def modify_end_date_round(self, end_date):
        """Add players to the list for db"""
        self.rounds[-1]['DateFin'] = end_date

    def delete_last_round_save(self):
        """Function to delete last round so we don't save multiple times rounds"""
        if self.rounds:
            del self.rounds[-1]
