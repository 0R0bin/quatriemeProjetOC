"""Entry point"""
from controllers.body import Controller
from views.body import View
import controllers.database as db

def main():
    """Main program"""
    view = View()

    player = db.retrieve_player("Senechal")
    print(player)

    game = Controller(view)
    game.run()

if __name__ == "__main__":
    main()
