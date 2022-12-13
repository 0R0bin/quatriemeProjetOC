import controllers.database as db


def check_tournament_to_reload():
    """Function to check if there's a tournament to reload and his state"""
    last_tournament = db.retrive_last_tournament()
    if last_tournament:
        nb_rounds = last_tournament['NombreRounds']  # Save nb_rounds to check state of game

        # Function return different value (int) :
        # 0 : If you need to reload the tournament from scratch
        # 1 : If you need to check state
        if nb_rounds == "ToReload":
            return 0
        else:
            return 1
    else:
        return 2


def retrieve_players_reload(tournament):
    """Function to know how many players we need to retrieve"""
    nb_players = len(tournament.players)
    nb_rounds = tournament.nb_rounds

    # If there's the right amount of players, we don't create new ones
    if nb_players == (nb_rounds * 2):
        return 0
    # If there's not the right amount, we create the remaining ones
    return (nb_rounds * 2) - nb_players


def retrieve_rounds_reload(tournament):
    """Function to know how many rounds we need to retrieve"""
    nb_players = len(tournament.players)
    nb_rounds = len(tournament.rounds)

    # If there's the right amount of rounds in the tournament
    if nb_rounds == (nb_players * 2):
        return 0
    # If there's not the right amout, we play the remaining ones
    return (nb_players * 2) - nb_rounds
