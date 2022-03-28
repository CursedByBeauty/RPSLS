from ai import Ai
from human import Human
import random

class Game:
    def __init__(self):
        self.player_one = Human
        self.player_two = Ai

    def display_greeting(self):
        #Create a method/function that can display_greeting
        pass

    def ask_user_input(self):
        #Create a method that will ask the user if they 
        # want to play a single or multiplayer game 
        # (ASK THE USER FOR INPUT) (REPLY IS A NUMBER HINT: INT)
        pass

    def battle(self):
        #Create a battle method that will LOOP the game 
        # under the condition of both player one AND player 
        # two wins being < 2
        pass

    def run_game(self):
        #Create a run game method that should start the calling 
        # of all the functions. Should display welcome method 
        # and also call the CHOOSE A GAME TYPE method
        pass

    def compare_gestures(self):
        #Create a method that will compare the gestures 
        # for player one and player two. Include the added 
        # win to the player wins for who ever won
        #[HINT under a condition...this player wins += 1]
        pass

    def display_winner(self):
        pass
