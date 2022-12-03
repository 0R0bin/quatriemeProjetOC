"""Main Controller"""
from typing import List

import controllers.database as db
from models.match import Match
from models.player import Player
from models.tournament import Tournament
from models.round import Round


class Controller:
    """Main controller."""

    def __init__(self, view):
        """Has a list of players, a match, a tournament, and rounds and a view."""
        # Models
        self.players: List[Player] = []
        self.match: List[Match] = []
        self.rounds: List[Round] = []
        self.actual_round = Round
        self.compteur_round = 0

        # View
        self.view = view

    def create_tournament(self):
        """Creation of a tournament"""
        name_tournament = self.view.prompt_tournament_name()
        if not name_tournament:
            return
        place_tournament = self.view.prompt_tournament_place()
        if not place_tournament:
            return
        date_tournament = self.view.prompt_tournament_date()
        if not date_tournament:
            return
        nb_rounds = self.view.prompt_tournament_round()
        if not nb_rounds:
            return
        timeplay_tournament = self.view.prompt_tournament_timeplay()
        if not timeplay_tournament:
            return
        description_tournament = self.view.prompt_tournament_description()
        if not description_tournament:
            return

        # Creation du tournoi
        return Tournament(name_tournament, place_tournament, date_tournament,
        timeplay_tournament, description_tournament, nb_rounds)

    def create_player(self):
        """Création d'un joueur"""
        name = self.view.prompt_player_name()
        if not name:
            return
        nickname = self.view.prompt_player_nickname()
        if not nickname:
            return
        dob = self.view.prompt_player_dob()
        if not dob:
            return
        gender = self.view.prompt_player_gender()
        if not gender:
            return
        ranking = self.view.prompt_player_ranking()
        if not ranking:
            return

        player = Player(name, nickname, dob, gender, ranking)
        # self.save_player_to_db(player.serialized())
        self.players.append(player)
        return player

    def merge_players_ranking_world(self):
        """Merge players with their world rankings"""
        self.players.sort(key=lambda players: players.ranking_world)

    def reset_tournament_score(self):
        """Reset the ranking tournament of all players"""
        for player in self.players:
            player.ranking_tournament = 0

    def merge_players_ranking_tournament(self):
        """Merge players with their tournament rankings"""
        self.players.sort(key=lambda players: players.ranking_tournament)
        for i in range(0, int(len(self.players)), 2):
            player1 = self.players[i]
            player2 = self.players[i + 1]
            if player1.ranking_tournament == player2.ranking_tournament:
                if player1.ranking_world > player2.ranking_world:
                    return
                else:
                    self.players[i], self.players[i + 1] = self.players[i + 1], self.players[i]

    def create_round_and_matchs(self):
        """Create round & match with the ranked list of players"""
        # name = self.view.prompt_round_name()
        self.compteur_round += 1
        name = "Round " + str(self.compteur_round)
        begin_date = self.view.prompt_round_begin_date()
        if not begin_date:
            return
        # end_date = self.view.prompt_round_end_date()
        end_date = "Undefined"

        actual_round = Round(name, begin_date, end_date)
        self.rounds.append(actual_round)

        for i in range(0, int(len(self.players)), 2):
            actual_match = Match(self.players[i], 0, self.players[i + 1], 0)
            actual_round.matchs.append(actual_match)

            match_to_save = actual_match.serialized()
            actual_round.matchs_serialized.append(match_to_save)

        return actual_round

    def choosing_a_winner_for_all_matchs_in_round(self, actual_round):
        """Function to choose a winner for a match"""
        numero_match = 0
        for match in actual_round.matchs:
            numero_match += 1
            winner = int(self.view.winner_of_the_match(match, numero_match))
            if winner == 1:
                match.player1.ranking_tournament += 1
            elif winner == 2:
                match.player2.ranking_tournament += 1
            elif winner == 3:
                match.player1.ranking_tournament += 0.5
                match.player2.ranking_tournament += 0.5
            else:
                self.view.error()

    def winner_and_score_tournament(self):
        """Merge players in reverse so you can display the winner"""
        self.compteur_round = 0
        self.players.sort(key=lambda players: players.ranking_tournament, reverse=True)
        self.view.tournament_ranking_and_winner(self.players)

    #   ======================
    #   Execution du programme
    #   ======================

    def run(self):
        """Execution du programme pour le tournoi"""
        # Menu pour choisir ce que va exectuer le programme
        choice = self.view.menu()

        #   ===============================
        #       1 : Création de tournoi
        #   ===============================
        if choice == 1:
            tournament = self.create_tournament()
            nb_players_in_tournament = int(self.view.number_player_in_tournament(tournament.nb_rounds))
            # Récupération des joueurs
            i = 0
            while i < nb_players_in_tournament:
                i += 1
                name = self.view.searching_players()
                player_to_add = db.retrieve_player(name)
                self.view.player_added(name)
                if player_to_add is False:
                    self.view.error_add_player()
                    i -= 1
                else:
                    self.players.append(player_to_add)
                    player_to_save = player_to_add.serialized()
                    tournament.add_players(player_to_save)

            self.reset_tournament_score()
            self.merge_players_ranking_world()

            # Jouer les rounds
            j = 0
            while j < int(tournament.nb_rounds):
                j += 1
                actual_round = self.create_round_and_matchs()
                self.choosing_a_winner_for_all_matchs_in_round(actual_round)
                date_fin = input("Entrez la date de fin du round : ")
                actual_round.change_date_fin(date_fin)
                round_to_save = actual_round.serialized()
                tournament.add_rounds(round_to_save)
                self.merge_players_ranking_tournament()

            self.winner_and_score_tournament()
            choice_save = self.view.save_tournament()

            if choice_save is True:
                db.save_to_db_tournament(tournament.serialized())

            reload_choice = self.view.reload_tournament()
            if reload_choice is True:
                self.run()
            else:
                quit()

        #   =================================
        #       2 : Création de joueur(s)
        #   =================================
        elif choice == 2:
            nb_player_to_create = self.view.nb_player_to_create()
            nb_player_to_create = int(nb_player_to_create)
            i = 0
            while i < nb_player_to_create:
                i += 1
                player_created = self.create_player()
                # Sauvegarde dans la base de données joueurs
                save_to_db = self.view.save_to_db_player()
                if save_to_db is True:
                    serialized_player = player_created.serialized()
                    db.save_to_db(serialized_player)

            self.view.display_nb_player_created(nb_player_to_create)
            self.run()

        #   ===================
        #       3 : Rapports
        #   ===================
        elif choice == 3:
            # Afficher tous les rapports possible
            report_choice = self.view.menu_reports()
            # Choix d'affichage des joueurs
            if report_choice == 1:
                # Choix du tri
                merge_choice = self.view.merge_player_db()
                if merge_choice is False:
                    quit()
                # Affichage des joueurs + demande de retour ?
                choice_back = db.retrieve_all_players(merge_choice)
                if choice_back is True:
                    self.run()
                else:
                    quit()
            # Rapport sur tous les tournois dans la base
            elif report_choice == 2:
                choice_back = db.retrieve_all_tournament()
                if choice_back is True:
                    self.run()
                else:
                    quit()
            # Affichage des joueurs d'un tournoi
            elif report_choice == 3:
                name_tournament = input("Merci d'indiquer le nom du tournoi recherché : ")
                choice_back = db.retrieve_x_in_tournament(name_tournament, 1)
                if choice_back is True:
                    self.run()
                else:
                    quit()
            # Affichage des rounds d'un tournoi
            elif report_choice == 4:
                name_tournament = input("Merci d'indiquer le nom du tournoi recherché : ")
                choice_back = db.retrieve_x_in_tournament(name_tournament, 2)
                if choice_back is True:
                    self.run()
                else:
                    quit()
            # Affichage des matchs d'un tournoi
            elif report_choice == 5:
                name_tournament = input("Merci d'indiquer le nom du tournoi recherché : ")
                choice_back = db.retrieve_x_in_tournament(name_tournament, 3)
                if choice_back is True:
                    self.run()
                else:
                    quit()
            # Retour
            elif report_choice == 6:
                self.run()
            # Inconnu
            else:
                self.run()
        # Error
        elif choice is False:
            self.run()
