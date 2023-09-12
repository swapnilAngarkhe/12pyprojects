import random

def computer_guess(x):
    low=1
    heigh=x
    feedback=''
    while feedback != 'c':
        if low != heigh:
            guess=random.randint(low,heigh)
        else:
            guess=low
        feedback=input(f"is {guess} is to heigh(H) too low(L) or correct(C)").lower()
        if feedback=='h':
            heigh= guess-1
        elif feedback=='l':
            low=guess+1
    print(f"The computer guessed the number {guess} correct")
    

computer_guess(10)
            
