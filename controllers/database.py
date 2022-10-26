import os
from tinydb import TinyDB, Query
from models.player import Player


# Global variables
body_path = os.getcwd()

PATH_DB_PLAYER = r'\DataBase\db_players.json'
PATH_DB_TOURNAMENT = r'\DataBase\db_tournament.json'

db_player = TinyDB(body_path + PATH_DB_PLAYER)
db_tournament = TinyDB(body_path + PATH_DB_TOURNAMENT)

#   ====================
#       Players Save
#   ====================


def save_to_db(serialized_player):
    """Save a player into the database"""
    db_player.insert(serialized_player)
    print(f"Le joueur {serialized_player['Name']} a été sauvegardé")


def retrieve_all_players():
    """Retrieve & Display all Players in the DataBase"""
    all_players = db_player.all()
    for player in all_players:
        # String pour Homme ou Femme ou inconnu
        string_m = f'{player["Name"]} {player["Nickname"]}, né le {player["Dob"]}, '
        string_f = f'{player["Name"]} {player["Nickname"]}, née le {player["Dob"]}, '
        string_f_m = f'{player["Name"]} {player["Nickname"]}, né(e) le {player["Dob"]}, '
        string2 = f'avec un classement de {player["Ranking"]}'
        # En fonction du genre, changer l'affichage
        gender = player['Gender']
        if gender in ("Homme", "M", "m", "homme"):
            print("- " + string_m + string2)
        elif gender in ("Femme", "femme", "f", "F"):
            print("- " + string_f + string2)
        else:
            print("- " + string_f_m + string2)
    # Affichage pour utilisateur
    print(f"\nUn total de {len(all_players)} joueurs est enregistré dans la base !")
    choice = input("Retour au menu principal ? ")
    if choice in ("Oui", "oui", "y", "yes"):
        return True
    print("Fermeture du programme...")


def retrieve_player(name):
    """Display all players in Db according to the given name"""
    list_players = db_player.search(Query().Name == name)

    if len(list_players) == 1:
        player = Player('Name', 'nickname', 'dob', 'm', 45)
        player.deserialized(list_players[0])
        return player

    elif len(list_players) == 0:
        return False

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
            print("Merci d'indiquer un numéro : ")
            return

#   =======================
#       Tournament Save
#   =======================


def save_to_db_tournament(serialized_tournament):
    """Save a player into the database"""
    print(serialized_tournament)
    db_tournament.insert(serialized_tournament)
    print(f"Le tournoi {serialized_tournament['Name']} a été sauvegardé")


def retrieve_all_tournament():
    """Retrieve all tournaments in the database"""
    all_tournament = db_tournament.all()
    for tournament in all_tournament:
        string1 = f"{tournament['Name']} qui a eu lieu à {tournament['Place']} le {tournament['Date']}, "
        string2 = f"ayant pour mode de jeu le {tournament['Mode']} et pour description {tournament['Description']}."
        string3 = f"Il comporte {tournament['NombreRounds']} rounds, en voici la liste : {tournament['ListeRounds']}"
        string4 = f"Voici la liste des joueurs ayant participé : {tournament['ListeJoueurs']}"
        print("- " + string1 + string2 + "\n")
        print(string3 + "\n")
        print(string4 + "\n")

    # Affichage pour utilisateur
    print(f"\nUn total de {len(all_tournament)} tournois est enregistré dans la base !")
    choice = input("Retour au menu principal ? ")
    if choice in ("Oui", "oui", "y", "yes"):
        return True
    print("Fermeture du programme...")
