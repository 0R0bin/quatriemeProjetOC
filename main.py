"""Entry point"""
from controllers.body import Controller
from views.body import View

def main():
    """Main program"""
    view = View()

    game = Controller(view)
    game.run()

if __name__ == "__main__":
    main()
