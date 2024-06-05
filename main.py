from game import Game
from colorama import init
from configuration import configuration

def main():
    init(autoreset=True)
    name, bot_name, chips = configuration()
    player_names = [name, bot_name]
    game = Game(player_names, chips)
    game.play_game()

if __name__ == "__main__":
    main()
