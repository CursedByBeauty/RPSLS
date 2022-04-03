from player import Player
import random

class Ai(Player):
    def __init__(self):
        super().__init__()
    
    def choose_gesture(self):
        random_gesture = random.randint(0,4)
        return self.gestures[random_gesture]
        # need to refer to self.gestures list
        # need to return the answer from a random choice
        
