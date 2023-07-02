
import Square
import util
class Piece:
    def __init__(self, name, color, coordinate, board): # pos should NOT be tuple
        
        self.name = name
        self.color = color
        self.coordinate = coordinate
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
        else: return False# destination square color is opposite of the current color



class King(Piece):

    def __init__(self, name, color, coordinate):
        super().__init__(name, color, coordinate)

    def get_legal_moves(self): #king will have 8 moves, though it must fit in the constraints
        # so what's the easiest way to write the function? , pass in a next square?
        # but you have to iterate through each possible square to get a LIST
        for row in range(self.color[0] - 1, 2, )

    def move_is_legal(self, destination_square: Square):
        return super().move_is_legal(destination_square)

if __name__ == "__main__":
    pass