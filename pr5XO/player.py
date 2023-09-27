import math
import random


class player:
    def __init__(self, letter):
        self.letter=letter #letter=x,o
    
    #next move
    def getmove(self, game):
        pass
    
class cpu(player):
    def __init__(self, letter):
        super().__init__(letter)
        
    def getmove(self, game):
        square=random.choice(game.available_moves()) 
        return square 
    
class humanplayer(player):
    def __int__ (self, letter):
        super().__init__(letter)
    
    def getmove(self,game):
        valid_square=None
        val=None
        while not valid_square:
            square=input(self.letter + '\' s turn. Input move (0-9): ') #left 44:24