"""Main Controller"""
from typing import List

from models.match import Match
from models.player import Player
from models.tournament import Tournament
from models.tours import Tours

class Controller:
    """Main controller."""

    def __init__(self, match: Match, tournament: Tournament, tours: Tours, view):
        """Has a list of players, a match, a tournament, and tours and a view."""
        # Models
        self.players: List[Player] = []
        self.match = match
        self.tournament = tournament
        self.tours = tours

        # View
        self.view = view

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
            score = self.view.prompt_player_score()
            if not score:
                return
            player = Player(name, nickname, dob, gender, ranking, score)
            self.players.append(player)

    def run(self):
        """Execution du tournoi"""
        self.get_players()
