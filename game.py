from ai import Ai
from human import Human
import random

class Game:
    def __init__(self):
        self.one = Human()
        self.two = Ai()

    def display_greeting(self):
        #Create a method/function that can display_greeting
        print('Welcome to Rock Paper Scissors Lizard Rock. ')
        print()

    def ask_user_input(self):
        #Create a method that will ask the user if they 
        # want to play a single or multiplayer game 
        # (ASK THE USER FOR INPUT) (REPLY IS A NUMBER HINT: INT)
        while True:
            game_mode = input("Choose a game mode: for Single Player enter 's', for Multiplayer enter 'm' ").lower()
            if game_mode not in ('s','m'):
                continue
            else:
                break
        if game_mode == 's':
                self.battle()
        elif game_mode == 'm':
            self.two = Human()
            self.battle()



    def battle(self):
        #Create a battle method that will LOOP the game 
        # under the condition of both player one AND player 
        # two wins being < 2
        while self.one.winning_score < 2 and self.two.winning_score < 2:
            self.user1 = self.one.choose_gesture()
            self.user2 = self.two.choose_gesture()
            print(f" Player two's choice is: {self.user2}")
            self.compare_gestures()
            if self.one.winning_score >= 2:
                self.display_winner("Player 1")
            elif self.two.winning_score >= 2:
                self.display_winner("Player 2")
            

    def run_game(self):
        #Create a run game method that should start the calling 
        # of all the functions. Should display welcome method 
        # and also call the CHOOSE A GAME TYPE method
        self.display_greeting()
        self.ask_user_input()
        

    def compare_gestures(self):
        #Create a method that will compare the gestures 
        # for player one and player two. Include the added 
        # win to the player wins for who ever won
        #[HINT under a condition...this player winning score += 1]
    
        # If rock wins beat 2 and 3 
        if self.user1 == self.one.gestures[0] and (self.user2 == self.two.gestures[2] or self.user2 == self.two.gestures[3]):
            print("Player one wins!")
            self.one.winning_score += 1 
        elif self.user2 == self.two.gestures[0] and (self.user1 == self.one.gestures[2] or self.user1 == self.one.gestures[3]):
            print("Player two wins!")
            self.two.winning_score += 1 

        # if paper wins beats 0 and 4
        if self.user1 == self.one.gestures[1] and (self.user2 == self.two.gestures[0] or self.user2 == self.two.gestures[4]):
            print("Player 1 wins!")
            self.one.winning_score += 1

        elif self.user2 == self.two.gestures[1] and (self.user1 == self.one.gestures[0] or self.user1 == self.one.gestures[4]):
            print("Player 2 wins!")
            self.two.winning_score += 1

        # if scissors wins beats 1 and 3
        if self.user1 == self.one.gestures[2] and (self.user2 == self.two.gestures[1] or self.user2 == self.two.gestures[3]):
            print("Player 1 wins!")
            self.one.winning_score += 1

        elif self.user2 == self.two.gestures[2] and (self.user1 == self.one.gestures[1] or self.user1 == self.one.gestures[3]):
            print("Player 2 wins!")
            self.two.winning_score += 1

        # if lizard wins beats 1 and 4
        if self.user1 == self.one.gestures[3] and (self.user2 == self.two.gestures[1] or self.user2 == self.two.gestures[4]):
            print("Player 1 wins!")
            self.one.winning_score += 1

        elif self.user2 == self.two.gestures[3] and (self.user1 == self.one.gestures[1] or self.user1 == self.one.gestures[4]):
            print("Player 2 wins!")
            self.two.winning_score += 1

        # if spock wins beats 0 and 2
        if self.user1 == self.one.gestures[4] and (self.user2 == self.two.gestures[0] or self.user2 == self.two.gestures[2]):
            print("Player 1 wins!")
            self.one.winning_score += 1

        elif self.user2 == self.two.gestures[4] and (self.user1 == self.one.gestures[0] or self.user1 == self.one.gestures[2]):
            print("Player 2 wins!")
            self.two.winning_score += 1
            
        # Tied 
        if self.user1 == self.user2:
            print("It's a tie! ")


    def display_winner(self,winner):
        print(f"{winner} is the winner! ")
        


