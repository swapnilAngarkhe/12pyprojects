

class tictactoe:
    def __init__(self):
        self.board= [' ' for _ in range(9)]
        self.CurrentWinner=None
        
        
    def printboard(self):
        for row in [self.board [i *3:(i+1)*3] for i in range(3)]:
            print(' | ' + ' | ' .join(row) + ' | ')
            
    @staticmethod
    def print_borad_num():
        #number for boxes
        numboard=[[str (i) for i in range(j*3, (j+1)*3)] for j in range (3)]
        for row in numboard:
            print(' | ' + ' | ' .join(row) + ' | ')
            