

import Square
from new_rf_util import *
class Piece:
    def __init__(self, name, color, coordinate, board): # pos should NOT be tuple
        
        self.name = name
        self.color = color
        self.coordinate = coordinate
        self.row = coordinate[0]
        self.col = coordinate[1]
        self.board = board
        self.is_turn = False
        self.is_selected = False
        self.is_movable = False # if not the player's turn, then not movable, but also deals with checks
        self.has_moves = False
        self.legal_moves = [] # list of coordinates

    # def move_is_legal
    def get_legal_moves(self): # will be a list of tuples, or maybe a set?
        ''' 1. to get legal moves for each piece, the piece needs to have a board to reference
            2. additionally, get_legal_moves will deal with the GEOMETRY'''
        return self.legal_moves
    
    def move_is_legal(self, destination_square:Square): 
        # will return the legality, is there a same color piece blocking the selected piece?
        is_opposite_color = is_opposite_color(self.color, destination_square.get_Piece_color())
        
        if destination_square.is_empty or is_opposite_color:
            return True
        else: return False



class King(Piece):

    def __init__(self, name, color, coordinate):
        super().__init__(name, color, coordinate)

    def get_legal_moves(self): #king will have 8 moves, though it must fit in the constraints
        # so what's the easiest way to write the function? , pass in a next square?
        # but you have to iterate through each possible square to get a LIST
        possible_moves = [(self.row+1, self.col), (self.row+1, self.col-1), (self.row+1, self.col+1), 
                          (self.row, self.col+1), (self.row, self.col-1), 
                          (self.row-1, self.col+1), (self.row-1, self.col), (self.row-1, self.col-1)]
                          

        for move in possible_moves:
            
            if is_in_bounds(move): self.legal_moves.append(move)
            else: continue
        
        return self.legal_moves
    
    def move_is_legal(self, destination_square: Square):
        return super().move_is_legal(destination_square)
    
class Queen(Piece):
    def __init__(self, name, color, coordinate, board):
        super().__init__(name, color, coordinate, board)

    def get_legal_moves(self):
        
        ''' queen moves linearly and diagonally
            so in order for the move to be legal, it cant move through anyone -> recursive function '''

class Pawn(Piece):

    def __init__(self, name, color, coordinate, board):
        super().__init__(name, color, coordinate, board)

    def get_legal_moves(self):
        self.legal_moves.clear()
        
        if self.color == "white":
            self.get_pawn_captures()
            if self.row == 6: self.legal_moves.append((self.row+1, self.col), (self.row+2, self.col))
                
            else: self.legal_moves.append((self.row+1, self.col))
                

        if self.color == "black":
            self.get_pawn_captures()
            if self.row == 1: self.legal_moves.append((self.row-1, self.col), (self.row-2, self.col))

            else: self.legal_moves.append((self.row-1, self.col))

        return self.legal_moves


    def get_pawn_captures(self):

        if self.color == "white":
            capture_squares = [(self.row-1, self.col-1), (self.row-1, self.col+1)]

            for square in capture_squares:
                if is_in_bounds(square) and is_opposite_color(self.color, self.board[square[0]][square[1]]):
                    self.legal_moves.append(square)
                else: continue

        if self.color == "black":
            capture_squares = [(self.row+1, self.col-1), (self.row+1, self.col+1)]

            for square in capture_squares:
                if is_in_bounds(square) and is_opposite_color(self.color, self.board[square[0]][square[1]]):
                    self.legal_moves.append(square)
                else: continue


class Rook(Piece):

    def __init__(self, name, color, coordinate, board):
        super().__init__(name, color, coordinate, board)
        
    def get_legal_moves(self): # this is NOT the most efficient way to get the SMALLEST LIST
        self.legal_moves.clear()
        for i in range(8):
            self.legal_moves.append((i, self.col))
        for i in range(8):
            self.legal_moves.append((self.row, i))
        return self.legal_moves

class Bishop(Piece):
    def __init__(self, name, color, coordinate, board):
        super().__init__(name, color, coordinate, board)


class Knight(Piece):
    def __init__(self, name, color, coordinate, board):
        super().__init__(name, color, coordinate, board)
        
           

if __name__ == "__main__":
    pass