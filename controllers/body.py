"""Main Controller"""
from typing import List

import controllers.database as db
import controllers.reload_and_save as reload
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
        self.round_to_complete = Round

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
        self.compteur_round += 1
        name = "Round " + str(self.compteur_round)
        begin_date = self.view.prompt_round_begin_date()
        if not begin_date:
            return
        end_date = "Undefined"

        actual_round = Round(name, begin_date, end_date)
        self.rounds.append(actual_round)

        for i in range(0, int(len(self.players)), 2):
            actual_match = Match(self.players[i], 0, self.players[i + 1], 0)
            actual_round.matchs.append(actual_match)

        return actual_round

    def choosing_a_winner_for_all_matchs_in_round(self, actual_round, tournament):
        """Function to choose a winner for a match"""
        numero_match = 0
        for match in actual_round.matchs:
            numero_match += 1
            winner = int(self.view.winner_of_the_match(match, numero_match))
            if winner == 1:
                match.player1.ranking_tournament += 1
                match.score1 += 1
            elif winner == 2:
                match.player2.ranking_tournament += 1
                match.score2 += 1
            elif winner == 3:
                match.player1.ranking_tournament += 0.5
                match.player2.ranking_tournament += 0.5
                match.score1 += 0.5
                match.score2 += 0.5
            else:
                self.view.error()
            actual_round.add_match(match.serialized())
            round_to_save = actual_round.serialized()
            if numero_match != 1:
                tournament.delete_last_round_save()
            tournament.add_rounds(round_to_save)

    def winner_and_score_tournament(self):
        """Merge players in reverse so you can display the winner"""
        self.compteur_round = 0
        self.players.sort(key=lambda players: players.ranking_tournament, reverse=True)
        self.view.tournament_ranking_and_winner(self.players)

    def reinit(self):
        """Function to reset state if you keep looping and creating tournaments"""
        self.players: List[Player] = []
        self.match: List[Match] = []
        self.rounds: List[Round] = []
        self.actual_round = Round
        self.compteur_round = 0
        self.round_to_complete = Round

    def recup_players_for_tournament(self, nb_players_in_tournament, tournament):
        """Get the players for the tournament"""
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

    def play_tournament(self, tournament, j, diff_match):
        """Execute rounds and display winner"""
        # If a round doesn't have all his matchs
        if diff_match != 0:
            for i in range(diff_match * 2, int(len(self.players)), 2):
                actual_match = Match(self.players[i], 0, self.players[i + 1], 0)
                self.round_to_complete.matchs.append(actual_match)
            self.choosing_a_winner_for_all_matchs_in_round(self.round_to_complete, tournament)
            date_fin = input("Entrez la date de fin du round : ")
            tournament.modify_end_date_round(date_fin)
            self.merge_players_ranking_tournament()

        while j < int(tournament.nb_rounds):
            j += 1
            actual_round = self.create_round_and_matchs()
            self.choosing_a_winner_for_all_matchs_in_round(actual_round, tournament)
            date_fin = input("Entrez la date de fin du round : ")
            tournament.modify_end_date_round(date_fin)
            self.merge_players_ranking_tournament()

        self.winner_and_score_tournament()
        choice_save = self.view.save_tournament()

        if choice_save is True:
            db.save_to_db_tournament(tournament.serialized())

        reload_choice = self.view.reload_tournament()
        if reload_choice is True:
            self.reinit()
            self.run()
        else:
            quit()

    def add_rounds_or_not(self, tournament):
        """We add rounds or not if the game as been reloaded"""
        retrieve_rounds = reload.retrieve_rounds_reload(tournament)
        # If the good amount of rounds is saved in the tournament, we play the end the normal way
        if retrieve_rounds == 0:
            for round_to_add in tournament.rounds:
                # We get back the rounds into our game
                default_round = Round("Name", "DB", "DF")
                default_round.deserialized(round_to_add)
                self.rounds.append(default_round)
                # For every match
                for match in default_round.matchs_serialized:
                    # For every player, we check if player exist to give him RankingTournament back
                    for player in self.players:
                        if player.get_name() == match["Player1"]['Name']:
                            player.ranking_tournament += match["Score1"]
                        elif player.get_name() == match["Player2"]['Name']:
                            player.ranking_tournament += match["Score2"]

            self.merge_players_ranking_tournament()
            self.winner_and_score_tournament()
            choice_save = self.view.save_tournament()

            if choice_save is True:
                db.save_to_db_tournament(tournament.serialized())

            reload_choice = self.view.reload_tournament()
            if reload_choice is True:
                self.reinit()
                self.run()
            else:
                quit()
        # If Rounds are missings
        else:
            diff_match = 0
            # We add the ones alreay played
            if tournament.rounds:
                for round_to_add in tournament.rounds:
                    # We get back the rounds into our game
                    default_round = Round("Name", "DB", "DF")
                    default_round.deserialized(round_to_add)
                    self.rounds.append(default_round)
                    # For every match
                    for match in default_round.matchs_serialized:
                        # For every player, we check if player exist to give him RankingTournament back
                        for player in self.players:
                            if player.get_name() == match["Player1"]['Name']:
                                player.ranking_tournament += match["Score1"]
                            elif player.get_name() == match["Player2"]['Name']:
                                player.ranking_tournament += match["Score2"]
                    if default_round.matchs_serialized != tournament.nb_rounds:
                        diff_match = tournament.nb_rounds - len(default_round.matchs_serialized)
                        self.round_to_complete = self.rounds[-1]
            # We sort the list in good order
            self.merge_players_ranking_tournament()
            # We play as usual, beginning rounds after the last one saved
            self.play_tournament(tournament, len(self.rounds), diff_match)

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
            try:
                tournament = self.create_tournament()
                nb_players_in_tournament = int(self.view.number_player_in_tournament(tournament.nb_rounds))
                # Récupération des joueurs
                self.recup_players_for_tournament(nb_players_in_tournament, tournament)
                # Jouer les rounds
                self.play_tournament(tournament, 0, 0)
            except KeyboardInterrupt:
                print("Vous avez coupé l'application, enregistrement du tournoi en cours")
                try:
                    db.save_to_db_temp_tournament(tournament.serialized())
                except UnboundLocalError:
                    print("Rien n'a été enregistré par manque d'informations")

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

        #   =====================================
        #       4 : Chargement ancien tournoi
        #   =====================================
        elif choice == 4:
            try:
                state_tournament = reload.check_tournament_to_reload()
                # If there's a tournament to retrieve
                if state_tournament != 2:
                    # ===============================
                    # Need to recreate all tournament
                    # ===============================
                    if state_tournament == 0:
                        tournament = self.create_tournament()
                        nb_players_in_tournament = int(self.view.number_player_in_tournament(tournament.nb_rounds))
                        # Get Players
                        self.recup_players_for_tournament(nb_players_in_tournament, tournament)
                        # Play rounds
                        self.play_tournament(tournament, 0, 0)

                    # =======================================
                    # Need to re-insert players in tournament
                    # =======================================
                    elif state_tournament == 1:
                        tournament = Tournament("TEMP", "TEMP", "TEMP", "TEMP", "TEMP", 4)
                        tournament.deserialized(db.retrive_last_tournament())
                        db.remove_saved_tournament()

                        retrieve_players = reload.retrieve_players_reload(tournament)

                        # If the good amount of players is saved in the tournament
                        if retrieve_players == 0:
                            for player_to_add in tournament.players:
                                player = Player("Name", "Nickname", "Dob", "Gender", 0)
                                player.deserialized(player_to_add)
                                self.players.append(player)
                            # We check if rounds are missings and play the game the normal way
                            self.add_rounds_or_not(tournament)

                        # If we need to create players
                        else:
                            if tournament.players:
                                for player_to_add in tournament.players:
                                    player = Player("Name", "Nickname", "Dob", "Gender", 0)
                                    player.deserialized(player_to_add)
                                    self.players.append(player)
                            # Get Players
                            self.recup_players_for_tournament(retrieve_players, tournament)
                            # We check if rounds are missings and play the game the normal way
                            self.add_rounds_or_not(tournament)
                # If there's no tournament to retrieve
                else:
                    print("\nDésolé, il n'y a pas de tournoi à récupérer, retour au menu principal")
                    self.run()
            except KeyboardInterrupt:
                print("Vous avez coupé l'application, enregistrement du tournoi en cours")
                db.save_to_db_temp_tournament(tournament.serialized())

        # Error
        elif choice is False:
            self.run()
