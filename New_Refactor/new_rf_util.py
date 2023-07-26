

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

def GetKingCannotGetOutOfCheck(checkingPiece, kingInCheck): 
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

    return isSubset
def createListOfBlockingPieces(checkingPiece, pieceList, b):
    retList = []
    attackingMoves = set(checkingPiece.get_legal_moves())
    for blockingPiece in pieceList:
        p = b[blockingPiece[0]][blockingPiece[1]].get_Piece()
        blockingMoves = set(p.get_legal_moves())
        sharedMoves = attackingMoves.intersection(blockingMoves)
        if sharedMoves: retList.append((blockingPiece))
    

    return retList

    # return whether the piece can block check, but in the scheme of iterating all pieces, how would we call this?
    return sharedMoves is True
def PieceCanBlockCheck(checkingPiece, blockingPiece):
    attackingMoves = set(checkingPiece.get_legal_moves())
    blockingMoves = set(blockingPiece.get_legal_moves())

    sharedMoves = attackingMoves.intersection(blockingMoves)

    # return whether the piece can block check, but in the scheme of iterating all pieces, how would we call this?
    return sharedMoves is True


def IterateForBlockingPieces():
    pass
    '''the issue at the moment is that we need a way to save all the pieces -> a list
       then iterate through this list;
       this list assumes that you remove captured pieces'''

def GetCheckmate():
    pass

    #king has to be in check first, if the king has no moves, and if none of its other pieces have moves that can block, then checkmate
    # if the king has no moves, and neither do any of its other pieces, then its a stalemate

def RemoveCapturedPiece(pieceList:list, newPos:tuple, oldPos:tuple):
    # if you move to square that is inhabited, then you need a way to remove/modify those coordinates
    # so the old position would be removed, and that new position would remain
    pieceList.remove(oldPos)
    pieceList.append(newPos)


if __name__ == "__main__":
    pass