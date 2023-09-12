import random

def play():
    user=input(f" choose rock paper or scissors by entering r, p or s respectively: ")
    computer=random.choice(['r', 'p', 's'])
    if user==computer:
        return f"your choice: {user} =  computer choice: {computer} tie"

    if win(user, computer):
        return f" your choice: {user}, computer choice: {computer} you won"
    
    return f"your choice: {user},  computer choice: {computer} you lost"

def win(player, opponent):
    #when player wins
    if (player == 'r' and opponent == 's') or (player=='s' and opponent=='p') \
        or (player=='p' and opponent=='r'): 
        return True

print(play())