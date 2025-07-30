import random

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def difficulty():
    diff=input("Choose a dificulty level 'easy' or 'hard':? ").lower()
    if diff=="easy":
         return EASY_LEVEL_TURNS
    elif diff=="hard":
         return HARD_LEVEL_TURNS
    else:
         print("Invalid Choice. ")

def check_ans(user,cpu,turns):
    """""Check answere agains against guess,reutrn the number of turns remaining"""
    if user>cpu:   
            print("Too High.")
            return turns-1
    elif user==cpu:
            print("You win.")
    elif user<cpu:
        print("too Low")
        return turns-1
        
    
        

def game():
    print("Welcome to the NUmber Guessing Game! ")
    
    numbers = list(range(1, 301))
    cpu=random.choice(numbers)

    print("I am thinking of a number between 1 and 301 ")
    print(cpu)

    turns=difficulty()
    guess=0

    while guess!=cpu:
        print(f"You have {turns} attempts remaining to Guess the number. ")
        user=int(input("Make a Guess: "))
        turns=check_ans(user,cpu,turns)
        if turns==0:
            print("you ran out of guess ")
            return



game()


        
        

