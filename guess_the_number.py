import random
easy_chance = 10
hard_chance = 5

def game(number, user_input,turns):
    if user_input > number:
        print("too high")
        return turns -1
    elif user_input < number:
        print("too low")
        return turns -1
    else:
        print("win")

def chances():
    level= input("Choose a difficulty. Type 'easy' or 'hard':")
    if level == "easy":
        return easy_chance
    else:
        return hard_chance
    
def games():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(0,100)
    print(number)
    turns = chances()
    user_input = 0
    while user_input != number:
        print(f"you had {turns} sttempots reaming to guess the number")
        user_input = int(input("enter a number"))
        turns = game(number,user_input,turns)
        if turns == 0:
            print("your out no guess left")
            return
        elif user_input != number:
            print("guess again")    

games()