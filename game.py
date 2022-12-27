from ai import AI
from person import Person
import time

class Game:
    def __init__(self):
        self.players= ' '
        self.winner = ''

    def start_game(self):
        print("Welcome to ROCK, PAPER, SCISSORS, LIZARD, SPOCK Game!")
        print(" ")
        print("each match will be best of three!")
        time.sleep(1)
        self.players= input("How many players? input 1 or 2:")

        while self.players != "1" and self.players != "2":
            self.players= input("How many are playing? input 1 or 2:")

        print (" ")
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
        time.sleep(1)





    def play_game(self):
        pass

    def display_winner(self):
        print(self.winner)

    def run_game(self):
       self.start_game()
       if self.players == '1':
            Singles = Single_Player()
            self.winner = Singles.play_game()
            self.display_winner()
       else:
            Doubles = Multiplayer()
            self.winner = Doubles.play_game()
            self.display_winner()




class Single_Player(Game):
        def __init__(self) -> None:
            super().__init__()

        def play_game(self):
            win_1=0
            win_2=0

            player_1=Person()
            player_2=AI()

            while win_1 <2 and win_2 <2:
                hand_1=player_1.display_choice()
                hand_2= player_2.display_choice()
                if hand_1 == "ROCK" and (hand_2 == "SCISSORS" or hand_2 == "LIZARD"):
                    win_1 += 1 
                    print("Player 1 wins!")
                elif hand_1 == "PAPER" and (hand_2 == "ROCK" or hand_2 == "SPOCK"):
                    win_1 += 1
                    print("Player 1 wins!")
                elif hand_1 == "SCISSORS" and (hand_2 == "PAPER" or hand_2 == "LIZARD"):
                    win_1 += 1
                    print("Player 1 wins!")
                elif hand_1 == "LIZARD" and (hand_2 == "PAPER" or hand_2 == "SPOCK"):
                    win_1 += 1
                    print("Player 1 wins!")
                elif hand_1 == "SPOCK" and (hand_2 == "ROCK" or hand_2 == "SCISSORS"):
                    win_1 += 1
                    print("Player 1 wins!")
                elif hand_2 == "ROCK" and (hand_1 == "SCISSORS" or hand_1 == "LIZARD"):
                    win_2 += 1 
                    print("Player 2 wins!")
                elif hand_2 == "PAPER" and (hand_1 == "ROCK" or hand_1 == "SPOCK"):
                    win_2 += 1
                    print("Player 2 wins!")
                elif hand_2 == "SCISSORS" and (hand_1 == "PAPER" or hand_1 == "LIZARD"):
                    win_2 += 1
                    print("Player 2 wins!")
                elif hand_2 == "LIZARD" and (hand_1 == "PAPER" or hand_1 == "SPOCK"):
                    win_2 += 1
                    print("Player 2 wins!")
                elif hand_2 == "SPOCK" and (hand_1 == "ROCK" or hand_1 == "SCISSORS"):
                    win_2 += 1
                    print("Player 2 wins!")
                else:
                    print("tie tie!")
            
                print(f'Player 1 has {win_1} wins. Player 2/AI has {win_2} wins.')
            
            if win_1 == 2:
                return "Player 1 is the winner, Chicken Dinner!"
            else:
                return "Player 2 is the winner, Player 1 is a sore loser!"
                
                


class Multiplayer(Game):
        def __init__(self) -> None:
            super().__init__()
        def play_game(self):
            win_1=0
            win_2=0

            player_1=Person()
            player_2=Person()

            while win_1 <2 and win_2 <2:
                hand_1=player_1.display_choice()
                hand_2=player_2.display_choice()
                if hand_1 == "ROCK" and (hand_2 == "SCISSORS" or hand_2 == "LIZARD"):
                    win_1 += 1 
                    print("Player 1 wins!")
                elif hand_1 == "PAPER" and (hand_2 == "ROCK" or hand_2 == "SPOCK"):
                    win_1 += 1
                    print("Player 1 wins!")
                elif hand_1 == "SCISSORS" and (hand_2 == "PAPER" or hand_2 == "LIZARD"):
                    win_1 += 1
                    print("Player 1 wins!")
                elif hand_1 == "LIZARD" and (hand_2 == "PAPER" or hand_2 == "SPOCK"):
                    win_1 += 1
                    print("Player 1 wins!")
                elif hand_1 == "SPOCK" and (hand_2 == "ROCK" or hand_2 == "SCISSORS"):
                    win_1 += 1
                    print("Player 1 wins!")
                elif hand_2 == "ROCK" and (hand_1 == "SCISSORS" or hand_1 == "LIZARD"):
                    win_2 += 1 
                    print("Player 2 wins!")
                elif hand_2 == "PAPER" and (hand_1 == "ROCK" or hand_1 == "SPOCK"):
                    win_2 += 1
                    print("Player 2 wins!")
                elif hand_2 == "SCISSORS" and (hand_1 == "PAPER" or hand_1 == "LIZARD"):
                    win_2 += 1
                    print("Player 2 wins!")
                elif hand_2 == "LIZARD" and (hand_1 == "PAPER" or hand_1 == "SPOCK"):
                    win_2 += 1
                    print("Player 2 wins!")
                elif hand_2 == "SPOCK" and (hand_1 == "ROCK" or hand_1 == "SCISSORS"):
                    win_2 += 1
                    print("Player 2 wins!")
                else:
                    print("tie tie!")

                print(f'Player 1 has {win_1} wins. Player 2 has {win_2} wins.')
            
            if win_1 == 2:
                return "Player 1 is the winner, Chicken Dinner!"
            else:
                return "Player 2 is the winner, Player 1 is a sore loser!"