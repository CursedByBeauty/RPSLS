from game import Game

game = Game()
game.run_game

# You want to create 4 classes Player, Human, Ai and Game 

# Player class:
# - This will be the PARENT class for the Human and the Ai
# - Create an instance variable to hold the winnning score
# - Create an instance variable that holds all the GESTURES that will be used in the form of a LIST in string format
#     ["Rock, "Paper", "Scissors", "Lizard", "Spock"]
# - Create a method in this class that allows a player to CHOOSE A GESTURE 


# Human class: 
# - From player import Player
# - This will be one of the CHILD classes for the PLAYER class, whcih means Human will need to INHERIT Player class


# Ai class: 
# - From player import Player
# - This will be one of the CHILD classes for the PLAYER class, which means Ai will need to INHERIT Player class
# - IMPORT RANDOM IN THIS MODULE 
# - INHERIT the CHOOSE A GESTURE method from the player class and make the choose gesture method to be a random choice that will be RETURNED

# Game class:
# - import random
# - from ai import Ai 
# - from human import Human
# - Create two instance variables: One will store the player_one which will call Human() and the other will store player_two which will call Ai()
# - Create a method/function that can display_greeting
# - Create a method that will ask the user if they want to play a single or multiplayer game (ASK THE USER FOR INPUT) (REPLY IS A NUMBER HINT: INT)
# - Create a battle method that will LOOP the game under the condition of both player one AND player two wins being < 2
# - Create a run game method that should start the calling of all the functions. Should display welcome method and also call the CHOOSE A GAME TYPE method
# - Create a method that will compare the gestures for player one and player two. Include the added win to the player wins for who ever won
# [HINT under a condition...this player wins += 1]
# - Create a method that displays a winner 

# Main. py 
# - import game from Game 
# - create a variable to call Game()
# - dot notate to call the run_game method

# DON'T FORGET TO TEST EACH FUNCTION AS YOU GO. DO NOT CONTINUE UNDER THE METHOD YOU ARE WORKING ON HAS NO BUGS!!!


