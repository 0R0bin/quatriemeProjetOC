"""Define the tours"""

class Tours:
    """Tours"""

    def __init__(self, name, date_debut, date_fin):
        "Some informations about the tours"
        self.name = name
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.matchs = []
        