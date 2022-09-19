"""Main Controller"""
from typing import List

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
        self.tournament = Tournament

        # View
        self.view = view

    def menu(self):
        """Function creating tournament if choice is True"""
        choice = self.view.menu()

        if choice is True:

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
            tournament = Tournament(name_tournament, place_tournament, date_tournament, timeplay_tournament, description_tournament, nb_rounds)
            print(f"{tournament.name} / {tournament.place}")

        elif choice is False:
            print("Vous avez choisi de ne pas lancer de tournoi")
            return

    def get_players(self):
        """Ajout de joueurs"""
        while len(self.players) < 8:
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
# e            score = self.view.prompt_player_score()
#             if not score:
#                 return
            player = Player(name, nickname, dob, gender, ranking)
            self.players.append(player)

    def merge_players_ranking(self):
        """Merge players with their rankings"""
        self.players.sort(key=lambda players:players.ranking)

        for player in self.players:
            print(f"{player.name} / {player.ranking}")


    # Execution du programme
    def run(self):
        """Execution du tournoi"""
        self.menu()
        self.get_players()
        self.merge_players_ranking()
