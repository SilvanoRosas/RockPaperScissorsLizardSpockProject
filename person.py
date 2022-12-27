import time
class Person:

    def __init__(self):
        self.choice_list= ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']


    def display_choice(self):
        print(" ")
        print("Choose 0 for ROCK")
        print("Choose 1 for PAPER")
        print("Choose 2 for SCISSORS")
        print("Choose 3 for LIZARD")
        print("Choose 4 for SPOCK")

        self.person_choice= input("Choose your Gesture.")

        while self.person_choice not in ('0','1','2','3','4'):
         self.person_choice= input("Choose your Gesture.")   

        

        print(f"Player has chosen {self.choice_list[int(self.person_choice)]}")
        return self.choice_list[int(self.person_choice)]