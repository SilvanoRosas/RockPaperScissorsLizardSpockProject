from ai import AI
from person import Person

class Game:
    def __init__(self):
        self.players= ' '

    def start_game(self):
        print("Welcome to ROCK, PAPER, SCISSORS, LIZARD, SPOCK Game")
        print( "each match will be best of three")
        self.players= input("How many are playing? input 1 or 2:")

        while self.players != "1" and self.players != "2":
            self.players= input("How many are playing? input 1 or 2:")

        
        print("The rules of the game are:")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitates Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")





    def play_game(self):
        pass

    def display_winner(self):
        pass

    def run_game(self):
        pass


class Single_Player(Game):
        def __init__(self) -> None:
            super().__init__()


class Multiplayer(Game):
        def __init__(self) -> None:
            super().__init__()