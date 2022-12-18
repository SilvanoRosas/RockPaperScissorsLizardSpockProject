import random


class AI:

    def __init__(self):
        self.choice_list= ['ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK']


    def display_choice(self):
        ai_choice= random.choice(self.choice_list)
        print(f" AI has chosen {ai_choice}")