"""Base view"""

class View:
    """Chess Tournament View"""

    #   =====================
    #       Global Views
    #   =====================
    def error(self):
        """Display if an error is encountered"""
        print("Désolé, une erreur a été rencontrée, fermeture du programme")
        quit()


    #   =======================
    #   Tournament view section
    #   =======================

    def menu(self):
        """Display information for the menu"""
        # Affichage des choix
        print("Que souhaitez-vous faire ?\n")
        print("1 - Créer un tournoi\n")
        print("2 - Création d'un ou plusieurs joueur(s)\n")

        # Choix de lancer ou non le tournoi
        choice = input("Merci d'indiquer le numéro de votre choix : ")
        if choice == "1" or choice == "un" or choice == "Un":
            print("Vous avez choisi de créer un tournoi\n")
            return 1

        elif choice == "2" or choice == "deux" or choice == "Deux":
            print("Vous avez choisi la création de joueur\n")
            return 2

        else:
            print("Désolé votre réponse n'est pas reconnue, fermeture du programme\n")
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
        """Prompt for tournament nb of round"""
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
        print("Choissisez votre contrôle du temps")
        timeplay_tournament = input("Bullet ou Blitz ou Coup rapide : ")
        if timeplay_tournament == "Bullet" or timeplay_tournament == "bullet":
            return timeplay_tournament
        elif timeplay_tournament == "Blitz" or timeplay_tournament == "blitz":
            return timeplay_tournament
        elif timeplay_tournament == "Coup rapide" or timeplay_tournament == "coup rapide":
            return timeplay_tournament
        else:
            timeplay_tournament = "Non défini"
            return timeplay_tournament

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
        name_player = input("\nEntrez le nom du joueur : ")
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
        """Prompt for player gender"""
        gender_player = input("Entrez genre du joueur : ")
        if not gender_player:
            return None
        return gender_player

    def prompt_player_ranking(self):
        """Prompt for player ranking"""
        ranking_player = input("Entrez le classement du joueur : ")
        if not ranking_player:
            return None
        return ranking_player

    def nb_player_to_create(self):
        """Display for the player creation screen"""
        nb_player_to_create = input("Combien voulez-vous en créer ? ")
        return nb_player_to_create

    def display_nb_player_created(self, number):
        """Display for informations"""
        if number < 2:
            print(f"Merci, vous avez créé {number} joueur")
        elif number >= 2:
            print(f"Merci, vous avez créé {number} joueurs")

    #   =======================
    #          Round Views
    #   =======================
    def prompt_round_name(self):
        """Prompt for round name"""
        name_round = input("\nEntrez le nom du round : ")
        if not name_round:
            return None
        return name_round

    def prompt_round_begin_date(self):
        """Prompt for round date_debut"""
        date_begin_round = input("Entrez la date de début du round : ")
        if not date_begin_round:
            return None
        return date_begin_round

    def prompt_round_end_date(self):
        """Prompt for round date_fin"""
        date_end_round = input("Entrez la date de fin du round : ")
        if not date_end_round:
            return None
        return date_end_round

    def winner_of_the_match(self, match, numero_match):
        """Prompt for the winner of the round"""
        string_joueur_1 = f"\nLe match {numero_match} opposait {match.player1.name}, le joueur n°1 "
        string_joueur_2 = f"à {match.player2.name}, le joueur n°2"
        print(string_joueur_1 + string_joueur_2 +"\n")
        print("Indiquer 1, si le joueur 1 a gagné")
        print("Indiquer 2, si le joueur 2 a gagné")
        print("Indiquer 3, si il y a eu égalité\n")
        winner = input("Merci d'indiquer le vainqueur du match : ")
        return winner

    #   =======================
    #         Test Views
    #   =======================
    def show_pair_player(self, player, player2):
        """Affiche une paire de joueur"""
        print(f"Première paire de joueur : {player} et {player2}")