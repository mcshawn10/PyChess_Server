
import Square

class Piece:
    def __init__(self, name, color, coordinate): # pos should NOT be tuple
        
        self.name = name
        self.color = color
        self.coordinate = coordinate
        self.is_turn = False
        self.is_selected = False
        self.is_movable = False # if not the player's turn, then not movable, but also deals with checks
        self.has_moves = False

    # def move_is_legal
    def get_legal_moves(): # will be a list of tuples, or maybe a set?

        return []
    ''' to get legal moves for each piece, the piece needs to have a board to reference
        additionally, get_legal_moves will deal with the GEOMETRY'''
    def move_is_legal(destination_square:Square): # will return the legality, is there a same color piece blocking the selected piece?
        
        if destination_square.is_empty:
            return True
        else # destination square color is opposite of the current color



class King(Piece):

    def __init__(self, name, color, coordinate):
        super().__init__(name, color, coordinate)


