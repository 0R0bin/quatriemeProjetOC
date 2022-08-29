"""Entry point"""
from typing import List

from models.player import Player
from models.match import Match
from models.tournament import Tournament
from models.tours import Tours
from controllers.body import Controller
from views.body import View

def main():
    # Define the players
    players : List[Player] = []
    players.append(Player("Joueur 1", "Test 1", "01", "M", 2, 0))
    players.append(Player("Joueur 2", "Test 2", "02", "F", 89, 0))
    players.append(Player("Joueur 3", "Test 3", "03", "M", 9, 0))
    players.append(Player("Joueur 4", "Test 4", "04", "F", 21, 0))
    players.append(Player("Joueur 5", "Test 5", "05", "M", 45, 0))
    players.append(Player("Joueur 6", "Test 6", "06", "F", 77, 0))
    players.append(Player("Joueur 7", "Test 7", "07", "M", 86, 0))
    players.append(Player("Joueur 8", "Test 8", "08", "F", 226, 0))

    # Add it to a list so we can sort rankings
    players.sort(key=lambda players:players.ranking)

    for player in players:
        print(f"{player.name} / {player.ranking}")


    # Do 4 matchs and update scores
    match1 = Match(players[0], 0, players[1], 0)
    result_match1 = match1.randomn_winner()
    players[0].rankingTemp = result_match1[0][1]
    players[1].rankingTemp = result_match1[1][1]
    print(f"Après le match 1, {players[0].name} à un score de {players[0].rankingTemp}")
    print(f"Après le match 1, {players[1].name} à un score de {players[1].rankingTemp}")

    match2 = Match(players[2], 0, players[3], 0)
    result_match2 = match2.randomn_winner()
    players[2].rankingTemp = result_match2[0][1]
    players[3].rankingTemp = result_match2[1][1]
    print(f"Après le match 2, {players[2].name} à un score de {players[2].rankingTemp}")
    print(f"Après le match 2, {players[3].name} à un score de {players[3].rankingTemp}")

    match3 = Match(players[4], 0, players[5], 0)
    result_match3 = match3.randomn_winner()
    players[4].rankingTemp = result_match3[0][1]
    players[5].rankingTemp = result_match3[1][1]
    print(f"Après le match 3, {players[4].name} à un score de {players[4].rankingTemp}")
    print(f"Après le match 3, {players[5].name} à un score de {players[5].rankingTemp}")
    
    match4 = Match(players[6], 0, players[7], 0)
    result_match4 = match4.randomn_winner()
    players[6].rankingTemp = result_match4[0][1]
    players[7].rankingTemp = result_match4[1][1]
    print(f"Après le match 4, {players[6].name} à un score de {players[6].rankingTemp}")
    print(f"Après le match 4, {players[7].name} à un score de {players[7].rankingTemp}")


if __name__ == "__main__":
    main()
