



class Piece:
    def __init__(self, pos, name, color):
        self.pos = pos # should be a tuple
        self.name = name
        self.color = color
        

class Pawn(Piece):

    def __init__(self, pos, name, color):
        super.__init__(pos, name, color)


class Rook(Piece):
    
    def __init__(self, pos, name, color):
        super.__init__(pos, name, color)


class Bishop(Piece):
    
    def __init__(self, pos, name, color):
        super.__init__(pos, name, color)

class Knight(Piece):
    
    def __init__(self, pos, name, color):
        super.__init__(pos, name, color)

class King(Piece):
    
    def __init__(self, pos, name, color):
        super.__init__(pos, name, color)

class Queen(Piece):
    
    def __init__(self, pos, name, color):
        super.__init__(pos, name, color)


        
if __name__ == "__main__":

    pass