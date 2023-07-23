

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
        self.theoretical_moves = []

    def set_coordinate(self, row:int, col:int):
        self.row = row
        self.col = col
        self.coordinate = (row, col)
    # def move_is_legal
    def get_legal_moves(self): # will be a list of tuples, or maybe a set?
        ''' 1. to get legal moves for each piece, the piece needs to have a board to reference
            2. additionally, get_legal_moves will deal with the GEOMETRY'''
        return self.legal_moves
    
    def move_is_legal(self, destination_square:Square): # destination_square could have remained tuple ?
        # will return the legality, is there a same color piece blocking the selected piece?
        is_opp_color = is_opposite_color(self.color, destination_square)
        
        if destination_square.is_empty or is_opp_color:
            return True
        else: return False

    def get_moves_right(self):

        if self.col <=6:
            for i in range(self.col+1, 8):
                if self.move_is_legal(self.board[self.row][i]):
                    self.legal_moves.append((self.row,i))
                    if not self.board[self.row][i].is_empty: break

                else: break

    def get_moves_left(self):
    
        if self.col >=1:
            for i in range(self.col-1, -1, -1):
                
                if self.move_is_legal(self.board[self.row][i]):
                    self.legal_moves.append((self.row,i))
                    if not self.board[self.row][i].is_empty: break

                else: break

    def get_moves_forward(self):
        
        if self.row >= 1:
            for i in range(self.row-1, -1, -1):
                if self.move_is_legal(self.board[i][self.col]):
                    
                    self.legal_moves.append((i, self.col))
                    if not self.board[i][self.col].is_empty: break
                
                else: break

    def get_moves_backward(self):
        
        if self.row <= 6:
            for i in range(self.row+1, 8):
                if self.move_is_legal(self.board[i][self.col]):
                    self.legal_moves.append((i, self.col))
                    if not self.board[i][self.col].is_empty: break
                else: break # breaks for same color but not for opposite
    
    def get_moves_NE(self):
        row = self.row
        col = self.col

        if self.row >=1 and self.col <=6: #probably need to be modified granted that a piece should be able to move to 0,0
            while row > 0 and col < 7:
                row -= 1
                col += 1
                if self.move_is_legal(self.board[row][col]):
                    self.legal_moves.append((row, col))
                    if not self.board[row][col].is_empty: break
                else: break

    def get_moves_NW(self):
        row = self.row
        col = self.col

        if self.row >=1 and self.col <8:
            while row >=0 and col <8:
                row -= 1
                col -= 1
                if self.move_is_legal(self.board[row][col]):
                    self.legal_moves.append((row, col))
                    if not self.board[row][col].is_empty: break
                else: break

    def get_moves_SE(self):
        row = self.row
        col = self.col

        if self.row <=6 and self.col <=6: #probably need to be modified granted that a piece should be able to move to 0,0
            while row <7 and col <7:
                row += 1
                col += 1
                if self.move_is_legal(self.board[row][col]):
                    self.legal_moves.append((row, col))
                    if not self.board[row][col].is_empty: break
                else: break
                                            
    
    def get_moves_SW(self):
        row = self.row
        col = self.col

        if self.row <=6 and self.col >=1: #probably need to be modified granted that a piece should be able to move to 0,0
            while row <7 and col > 0:
                row += 1
                col -= 1
                if self.move_is_legal(self.board[row][col]):
                    self.legal_moves.append((row, col))
                    if not self.board[row][col].is_empty: break
                else: break
    def get_diagonal_moves(self):

        self.get_moves_NE()
        self.get_moves_NW()
        self.get_moves_SE()
        self.get_moves_SW()
        '''
        possible_moves = self.legal_moves
        print(self.legal_moves)
        self.legal_moves.clear()
        
        
        # now filter out what is legal move ie same not same colors
        for move in possible_moves:
            if self.move_is_legal(self.board[move[0]][move[1]]):
                self.legal_moves.append(move)'''
        return self.legal_moves
class King(Piece):

    def __init__(self, name, color, coordinate, board):
        super().__init__(name, color, coordinate, board)

    def set_coordinate(self, row: int, col: int):
        super().set_coordinate(row, col)
    
    def get_legal_moves(self): #king will have 8 moves, though it must fit in the constraints
        # so what's the easiest way to write the function? , pass in a next square?
        # but you have to iterate through each possible square to get a LIST
        self.legal_moves.clear()
        possible_moves = [(self.row+1, self.col), (self.row+1, self.col-1), (self.row+1, self.col+1), 
                          (self.row, self.col+1), (self.row, self.col-1), 
                          (self.row-1, self.col+1), (self.row-1, self.col), (self.row-1, self.col-1)]
                          

        for move in possible_moves:
            
            if is_in_bounds(move) and self.move_is_legal(self.board[move[0]][move[1]]):
                self.legal_moves.append(move)
            else: continue
        
        return self.legal_moves
    
    def move_is_legal(self, destination_square: Square):
        return super().move_is_legal(destination_square)
    
class Queen(Piece):
    def __init__(self, name, color, coordinate, board):
        super().__init__(name, color, coordinate, board)
    def set_coordinate(self, row: int, col: int):
        return super().set_coordinate(row, col)
    
    def get_legal_moves(self):
        self.legal_moves.clear()
        self.get_moves_backward()
        self.get_moves_forward()
        self.get_moves_left()
        self.get_moves_right()

        
        self.get_diagonal_moves()
        return self.legal_moves

class Pawn(Piece):

    def __init__(self, name, color, coordinate, board):
        super().__init__(name, color, coordinate, board)
    def set_coordinate(self, row: int, col: int):
        super().set_coordinate(row, col)
    
    def get_legal_moves(self):
        self.legal_moves.clear()
        #assert self.col != 7
        if self.color == "black":
            self.get_pawn_captures()
            if self.row == 1: 
                self.legal_moves.append((self.row+1, self.col))
                self.legal_moves.append((self.row+2, self.col))
                
            else: self.legal_moves.append((self.row+1, self.col))
                

        if self.color == "white":
            self.get_pawn_captures()
            if self.row == 6: 
                self.legal_moves.append((self.row-1, self.col) )
                self.legal_moves.append((self.row-2, self.col))
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

    def set_coordinate(self, row: int, col: int):
        return super().set_coordinate(row, col)
        
    def get_legal_moves(self): # this is NOT the most efficient way to get the SMALLEST LIST
        self.legal_moves.clear()
        self.get_moves_backward()
        self.get_moves_forward()
        self.get_moves_left()
        self.get_moves_right()

        return self.legal_moves
    
    def get_moves_right(self):
        return super().get_moves_right()
    
    def get_moves_left(self):
        return super().get_moves_left()
    
    def get_moves_forward(self):
        return super().get_moves_forward()
    
    def get_moves_backward(self):
        return super().get_moves_backward()

class Bishop(Piece):
    def __init__(self, name, color, coordinate, board):
        super().__init__(name, color, coordinate, board)

    def set_coordinate(self, row: int, col: int):
        return super().set_coordinate(row, col)
    
    def get_legal_moves(self):
        self.legal_moves.clear()
        self.get_diagonal_moves()
        return self.legal_moves

class Knight(Piece):
    def __init__(self, name, color, coordinate, board):
        super().__init__(name, color, coordinate, board)

    def set_coordinate(self, row: int, col: int):
        return super().set_coordinate(row, col)
           
    def get_legal_moves(self):
        self.legal_moves.clear()
        possible_moves = [(self.row+1,self.col+2,), (self.row+1,self.col-2,),
                          (self.row-1,self.col+2,), (self.row-1,self.col-2,),
                          (self.row+2,self.col-1,), (self.row+2,self.col+1,),
                          (self.row-2,self.col+1,), (self.row-2,self.col-1)]
        
        possible_moves = list(filter(is_in_bounds, possible_moves))

        # now filter out what is legal move ie same not same colors
        for move in possible_moves:
            if self.move_is_legal(self.board[move[0]][move[1]]):
                self.legal_moves.append(move)

        return self.legal_moves
class Empty():
    def __init__(self, pos):
        self.pos = pos
        self.name = "."
        self.color = "."
    
    

if __name__ == "__main__":
    pass