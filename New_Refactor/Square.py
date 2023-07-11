class Square:

    def __init__(self, is_empty, coordinate):
        self.is_empty = is_empty 
        self.piece = None
        self.coordinate = coordinate
        self.color = None
        
    def get_Piece(self):
        if not self.is_empty:
            return self.piece
        else: return None
    
    def get_Piece_color(self):
        if not self.is_empty:
            return self.piece.color
        else: return None

    def draw_piece(self):
        pass




if __name__ == "__main__":
    pass