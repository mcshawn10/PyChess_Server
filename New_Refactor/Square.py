

class Square:

    def __init__(self, is_empty, P, coordinate, color):
        self.is_empty = is_empty 
        self.piece = P
        self.coordinate = coordinate
        self.color = color
        
    def get_Piece(self):
        if not self.is_empty:
            return self.piece
        else: return None
    
    def get_Piece_color(self):
        if not self.is_empty:
            return self.piece.color
        else: return None





if __name__ == "__main__":
    pass