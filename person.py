class Person:

    def __init__(self):
        self.choice_list= ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']


    def display_choice(self):
        print("Choose 0 for Rock")
        print("Choose 1 for Paper")
        print("Choose 2 for Scissors")
        print("Choose 3 for Lizard")
        print("Choose 4 for Spock")

        self.person_choice= input("Choose your Gesture")