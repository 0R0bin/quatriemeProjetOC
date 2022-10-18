import os
from tinydb import TinyDB, Query
from models.player import Player


# Global variables
body_path = os.getcwd()
PATH_DB_PLAYER = r'\DataBase\db_players.json'
db_player = TinyDB(body_path + PATH_DB_PLAYER)


def save_to_db(serialized_player):
    """Save a player into the database"""
    db_player.insert(serialized_player)
    print(f"Le joueur {serialized_player['name']} a été sauvegardé")


def retrieve_player(name):
    """Display all players in Db according to the given name"""
    list_players = db_player.search(Query().Name == name)

    if len(list_players) == 1:
        player = Player('Name', 'nickname', 'dob', 'm', 45)
        player.deserialized(list_players[0])
        return player

    else:
        i = 0
        for player in list_players:
            i += 1
            print(f"{i} - {player['Name']}, {player['Nickname']}, {player['Dob']}\n")

        player_chose = input("Quel joueur choisissez-vous (indiquer le numéro) : ")
        player_chose = int(player_chose)

        if isinstance(player_chose, int):
            player = Player('Name', 'nickname', 'dob', 'm', 45)
            player.deserialized(list_players[player_chose - 1])
            return player

        else:
            print("Merci d'indiquer un numéro")
            return
