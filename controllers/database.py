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


def retrieve_all_players(merge_choice):
    """Retrieve & Display all Players in the DataBase"""
    all_players = db_player.all()
    print(all_players[0]["Name"])
    # Choix du tri
    if merge_choice == 1:
        print("Sort by alphabetical")
        all_players.sort(key=lambda x: x["Name"])
    else:
        print("Sort by classement")
        all_players.sort(key=lambda x: x["Ranking"])

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
    # S'il n'y a qu'un joueur à afficher
    if len(list_players) == 1:
        player = Player('Name', 'nickname', 'dob', 'm', 45)
        player.deserialized(list_players[0])
        return player
    # Si aucun joueur n'est trouvé
    elif len(list_players) == 0:
        return False
    # S'il y a une liste de joueurs à afficher
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
    db_tournament.insert(serialized_tournament)
    print(f"Le tournoi {serialized_tournament['Name']} a été sauvegardé")


def retrieve_all_tournament():
    """Retrieve all tournaments in the database"""
    all_tournament = db_tournament.all()
    for tournament in all_tournament:
        string1 = f"{tournament['Name']} qui a eu lieu à {tournament['Place']} le {tournament['Date']}, "
        string2 = f"ayant pour mode de jeu le {tournament['Mode']} et pour description {tournament['Description']}."
        string3 = f"Il comporte {tournament['NombreRounds']} rounds, en voici la liste :\n"
        string4 = "Voici la liste des joueurs ayant participé : \n"
        print("\n==============================================================================\n")
        print("- " + string1 + string2)
        print("\n==============================================================================\n")

        # Affichage des rounds du tournoi
        print(string3)
        i = 0
        for round in tournament['ListeRounds']:
            i += 1
            print(f"{i} - Round {round['Name']} commençant le {round['DateDebut']} finissant le {round['DateFin']}\n")
            print(f"Un total de {len(round['Match'])} macth a été joué, voici la liste : \n")
            for match in round["Match"]:
                string1 = f"Match opposant {match['Player1']['Name']} à {match['Player2']['Name']} : "
                string2 = f"{match['Player1']['Name']} à obtenu {match['Score1']} points / "
                string3 = f"{match['Player2']['Name']} à obtenu {match['Score2']} points"
                print(string1 + string2 + string3)
            print("\n")

        # Affichage des joueurs ayant participé au tournoi
        print(string4)
        i = 0
        for player in tournament["ListeJoueurs"]:
            i += 1
            string_too_long = f"né le {player['Dob']} avec un classement de {player['Ranking']}"
            f_string_too_long = f"née le {player['Dob']} avec un classement de {player['Ranking']}"

            if player["Gender"] == "f" or player['Gender'] == "F":
                print(f"{i} - {player['Name']} {player['Nickname']}, " + f_string_too_long)
            else:
                print(f"{i} - {player['Name']} {player['Nickname']}, " + string_too_long)

    # Affichage pour utilisateur
    print(f"\nUn total de {len(all_tournament)} tournois est enregistré dans la base !")
    choice = input("Retour au menu principal ? ")
    if choice in ("Oui", "oui", "y", "yes"):
        return True
    print("Fermeture du programme...")


def retrieve_x_in_tournament(name_tournament, x):
    """
    Retrieve all Players of a tournament
    If x == 1 : Retrieve All Players
    If x == 2 : Retrieve All Rounds
    If x == 3 : Retrieve All Matchs
    """
    list_tournament = db_tournament.search(Query().Name == name_tournament)
    # S'il n'y a qu'un tournoi à afficher
    if len(list_tournament) == 1:
        tournament_here = list_tournament[0]
        print(f"{tournament_here['Name']}, le {tournament_here['Date']}, à {tournament_here['Place']}\n")
    # Si aucun tournoi n'est trouvé
    elif len(list_tournament) == 0:
        return False
    # S'il y a une liste de tournoi à afficher
    else:
        i = 0
        for tournament in list_tournament:
            i += 1
            print(f"{i} - {tournament['Name']}, le {tournament['Date']}, à {tournament['Place']}\n")
        tournament_here = input("Quel tournoi choisissez-vous (indiquer le numéro) : ")
        tournament_here = int(tournament_here)
        if isinstance(tournament_here, int):
            tournament_here = list_tournament[tournament_here - 1]
            string_too_long = "le {tournament_here['Date']}, à {tournament_here['Place']} a été séléctionné\n"
            print(f"Le tournoi {tournament_here['Name']}, " + string_too_long)
        else:
            print("Merci d'indiquer un numéro : ")
            return

    # Si on veut afficher la liste des joueurs
    if x == 1:
        i = 0
        list_players = tournament_here['ListeJoueurs']
        print("Voici la liste des joueurs de ce tournoi : \n")
        for player in list_players:
            i += 1
            string_too_long = f"né le {player['Dob']} avec un classement de {player['Ranking']}"
            f_string_too_long = f"née le {player['Dob']} avec un classement de {player['Ranking']}"

            if player["Gender"] == "f" or player['Gender'] == "F":
                print(f"{i} - {player['Name']} {player['Nickname']}, " + f_string_too_long)
            else:
                print(f"{i} - {player['Name']} {player['Nickname']}, " + string_too_long)

        choice = input("\nRetour au menu principal ? ")
        if choice in ("Oui", "oui", "y", "yes"):
            return True
        print("Fermeture du programme...")

    # Si on veut afficher la liste des rounds
    elif x == 2:
        i = 0
        list_rounds = tournament_here['ListeRounds']
        print("Voici la liste des rounds de ce tournoi : \n")
        for round in list_rounds:
            i += 1
            print(f"{i} - Round {round['Name']}, commençant le {round['DateDebut']}, finissant le {round['DateFin']}")
        choice = input("\nRetour au menu principal ? ")
        if choice in ("Oui", "oui", "y", "yes"):
            return True
        print("Fermeture du programme...")

    # Si on veut afficher la liste des matchs
    elif x == 3:
        i = 0
        list_rounds = tournament_here['ListeRounds']
        print("Voici la liste des matchs de ce tournoi : \n")
        for round in list_rounds:
            matchs = round["Match"]
            for match in matchs:
                string1 = f"Match opposant {match['Player1']['Name']} à {match['Player2']['Name']} : "
                string2 = f"{match['Player1']['Name']} à obtenu {match['Score1']} points / "
                string3 = f"{match['Player2']['Name']} à obtenu {match['Score2']} points"
                print(string1 + string2 + string3)
        choice = input("\nRetour au menu principal ? ")
        if choice in ("Oui", "oui", "y", "yes"):
            return True
        print("Fermeture du programme...")
