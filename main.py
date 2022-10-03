"""Entry point"""
from typing import List
from models import tournament

from models.player import Player
from models.match import Match
from models.tournament import Tournament
from models.round import Round
from controllers.body import Controller
from views.body import View

def main():
    """Main program"""
    view = View()

    game = Controller(view)
    game.run()

if __name__ == "__main__":
    main()
