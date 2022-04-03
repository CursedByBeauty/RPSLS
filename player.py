


class Player:
    def __init__(self):
        self.winning_score = 0
        self.gestures = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

    def choose_gesture(self):
    #ask user for input to pick from the list
        print("Type 0 for 'Rock'\nType 1 for 'Paper'\nType 2 for 'Scissors'\nType 3 for 'Lizard'\nType 4 for 'Spock'")
        while True:
            user_answer = input("Pick a gesture: ")
            if user_answer not in ['0','1','2','3','4']:
                continue 
            else:
                break

        return self.gestures[int(user_answer)]

    




        # REFERENCE
        # index = 0 
        # for gesture in self.gestures:
        #     print(f"Type {index} for {gesture}")
        #     index += 1 

        # user_answer = input("Choose a gesture: ")

