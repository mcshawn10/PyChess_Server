

def is_opposite_color(current: str, next_square):
    
    next_color = next_square.get_Piece_color()
    if current == "white" and next_color == "black":
        return True

    elif current == "black" and next_color == "white":
        return True

    else: return False
def get_opposite_color(color:str):
    if color == "white":
        return "black"
    else: return "white"

# def recursive_linear()
# def recursive_diagonal

def is_in_bounds(coordinate:tuple):
    if coordinate[0] >= 0 and coordinate[0] < 8 and coordinate[1] >= 0 and coordinate[1] < 8:
        
        return True
    else: return False

def GetKingCanGetOutOfCheck(checkingPiece, kingInCheck): 
    # you could iterate all pieces and get all their legal moves, if any of the kings theoretical moves is in, then chekcmate
    # you can try to make a move, and see if king is in anyone's list of legal moves
    # get all kings moves, find if any of the opposition moves has that same one, if so, then mark that off of kings possible moves
    # is there a computationally less expensive way than just iterating through all the pieces to see who can block?
    # note to self: in c++ this would probably be a good time to have a thread
    '''you can get all of kings legal moves, 
        if king has no legal moves, then start looking at its other pieces moves
        if those pieces have an intersection with the attacking piece, then not checkmate, but ones of those pieces has to move'''
    kingMoves = set(kingInCheck.get_legal_moves())
    attackingMoves = set(checkingPiece.get_legal_moves())

    isSubset = kingMoves <= attackingMoves

    if isSubset: return True
    else:
        # here is where you start iterating to see what piece has an intersection with the checking piece's moves
        pass





def GetCheckmate():
    pass

    #king has to be in check first, if the king has no moves, and if none of its other pieces have moves that can block, then checkmate
    # if the king has no moves, and neither do any of its other pieces, then its a stalemate




if __name__ == "__main__":
    pass