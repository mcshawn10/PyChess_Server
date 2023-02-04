
from util import *


class Piece:
    def __init__(self, pos, name, color):
        self.pos = pos # should be a tuple
        self.name = name
        self.color = color
        
class Empty(Piece):
    def __init__(self, pos, name, color):
        self.pos = pos
        self.name = "."
        self.color = "empty"


class Pawn(Piece):

    def __init__(self, pos, name, color):
        super.__init__(pos, name, color)

    def move_is_legal(self, next_pos):
        if (self.pos[0] == 6) and (next_pos[0] == 4) and (self.pos[1]==next_pos[1]):
                    return True
        elif next_pos[0] == self.pos[0]-1:
            return True
        elif (next_pos[1] == self.pos[1]+1 or next_pos[1] == self.pos[1]-1) and (next_pos[0] == self.pos[0]-1):
            return True
        else: return False

    def get_legal_moves(self):
        pass


class Rook(Piece):
    
    def __init__(self, pos, name, color):
        super.__init__(pos, name, color)


    def move_is_legal(self, next_pos) -> bool:
        if (self.pos[0] == next_pos[0]) or (self.pos[1] == next_pos[1]):
                if is_clear_lin(self.pos, next_pos, board_arr):
                    return True
        else: return False
    
    def get_legal_moves(self) -> list:
        pass

class Bishop(Piece):
    
    def __init__(self, pos, name, color):
        super.__init__(pos, name, color)

    def move_is_legal(self, next_pos) -> bool:
        if abs(self.pos[0]-next_pos[0])>=1 and abs(self.pos[1]-next_pos[1])>=1:
            
            if self.is_clear_diag(self.pos, next_pos, board_arr):
                return True
        else: return False

    def get_legal_moves(self) -> list:
        pass

class Knight(Piece):
    
    def __init__(self, pos, name, color):
        super.__init__(pos, name, color)

    def move_is_legal(self, next_pos) -> bool:
        col_diff = abs(self.pos[1]-next_pos[1])
        row_diff = abs(self.pos[0]-next_pos[0])
        if col_diff == 1 and row_diff == 2:
            return True
        if col_diff == 2 and row_diff == 1:
            return True
        else: return False

    def get_legal_moves(self) -> list:
        pass

class King(Piece):
    
    def __init__(self, pos, name, color):
        super.__init__(pos, name, color)
    
    def move_is_legal(self, next_pos):
        if abs(self.pos[0]-next_pos[0])==1 or abs(self.pos[1]-next_pos[1])==1:
                return True
        else: return False
        
    def get_legal_moves(self):
        pass
            

class Queen(Piece):
    
    def __init__(self, pos, name, color):
        super.__init__(pos, name, color)
    
    def move_is_legal(self, next_pos):
        if abs(self.pos[0]-next_pos[0])>=1 or abs(self.pos[1]-next_pos[1])>=1:
                if (self.pos[0] == next_pos[0]) or (self.pos[1] == next_pos[1]):
                    if self.is_clear_lin(self.pos, next_pos, board_arr):
                        return True

                elif abs(self.pos[0]-next_pos[0])>=1 and abs(self.pos[1]-next_pos[1])>=1:        
                    if self.is_clear_diag(self.pos, next_pos, board_arr):
                        return True   
        else: return False

    def get_legal_moves(self):
        pass


        
if __name__ == "__main__":

    pass