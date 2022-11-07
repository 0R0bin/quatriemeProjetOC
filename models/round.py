"""Define the rounds"""


class Round:
    """Round"""

    def __init__(self, name, date_debut, date_fin):
        "Some informations about the tours"
        self.name = name
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.matchs = []
        self.matchs_serialized = []

    def change_date_fin(self, date_fin):
        """Change the end date of a round"""
        self.date_fin = date_fin

    def serialized(self):
        """Transform Round object into JSON readable dictionnary"""
        serialized_round = {
            "Name": self.name,
            "DateDebut": self.date_debut,
            "DateFin": self.date_fin,
            "Match": self.matchs_serialized,
        }
        return serialized_round

    def deserialized(self, object_json):
        """Transfom round from db into round object"""
        self.name = object_json['Name']
        self.date_debut = object_json['DateDebut']
        self.date_fin = object_json['DateFin']
        self.matchs_serialized = object_json['Match']
        return "Round crée"
