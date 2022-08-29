"""Base view"""

class View:
    """Chess Tournament View"""

    #   =======================
    #   Tournament view section
    #   =======================

    def create_tournament(self):
        """Create tournament"""
        print("Souhaitez-vous créer un tournoi ?")
        # Choix de lancer ou non le tournoi
        choice = input("Oui ou non ? : ")
        if choice == "Oui" or choice == "oui" or choice == "yes" or choice == "y":
            return True
        elif choice == "Non" or choice == "non" or choice == "no" or choice == "n":
            return False
        else:
            print("Désolé votre réponse n'est pas reconnue")
            return False

    def prompt_tournament_name(self):
        """Prompt for tournament name"""
        name_tournament = input("Entrez le nom du tournoi : ")
        if not name_tournament:
            return None
        return name_tournament

    def prompt_tournament_place(self):
        """Prompt for tournament place"""
        place_tournament = input("Entrez le lieu du tournoi : ")
        if not place_tournament:
            return None
        return place_tournament

    def prompt_tournament_date(self):
        """Prompt for tournament date"""
        date_tournament = input("Entrez la date du tournoi : ")
        if not date_tournament:
            return None
        return date_tournament

    def prompt_tournament_round(self):
        """Prompt for tournament date"""
        round_tournament = input("Entrez le nombre de tour du tournoi : ")
        if not round_tournament:
            return None
        return round_tournament

    def prompt_tournament_timeplay(self):
        """Prompt for timeplay
        Possibility :
        Bullet
        Blitz
        Fast play
        """
        print("Choissisez votre contrôle du temps : \n")
        timeplay_tournament = input("Bullet ou Blitz ou Coup rapide")
        if timeplay_tournament == "Bullet" or timeplay_tournament == "bullet":
            return timeplay_tournament
        elif timeplay_tournament == "Blitz" or timeplay_tournament == "blitz":
            return timeplay_tournament
        elif timeplay_tournament == "Coup rapide" or timeplay_tournament == "coup rapide":
            return timeplay_tournament
        else:
            return None

    def prompt_tournament_description(self):
        """Prompt for description"""
        description_tournament = input("Entrez la description du tournoi : ")
        if not description_tournament:
            return None
        return description_tournament

    #   ===================
    #   Player view section
    #   ===================

    def prompt_player_name(self):
        """Prompt for player name"""
        name_player = input("Entrez le nom du joueur : ")
        if not name_player:
            return None
        return name_player

    def prompt_player_nickname(self):
        """Prompt for player nickname"""
        nickname_player = input("Entrez le prénom du joueur : ")
        if not nickname_player:
            return None
        return nickname_player

    def prompt_player_dob(self):
        """Prompt for player date of birth (dob)"""
        dob_player = input("Entrez la date de naissance du joueur : ")
        if not dob_player:
            return None
        return dob_player

    def prompt_player_gender(self):
        """Prompt for player date of birth (dob)"""
        gender_player = input("Entrez la date de naissance du joueur : ")
        if not gender_player:
            return None
        return gender_player

    def prompt_player_ranking(self):
        """Prompt for player ranking"""
        ranking_player = input("Entrez le classement du joueur : ")
        if not ranking_player:
            return None
        return ranking_player
    
    def prompt_player_score(self):
        """Prompt for player score"""
        score_player = input("Entrez le score du joueur : ")
        if not score_player:
            return None
        return score_player
    
    #   =======================
    #         Test Views
    #   =======================
    def show_pair_player(self, player, player2):
        """Affiche une paire de joueur"""
        print(f"Première paire de joueur : {player} et {player2}")