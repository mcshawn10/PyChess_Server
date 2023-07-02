import Piece
import Square

def is_opposite_color(current: str, next_square:Square):
    
    if current == "white" and next_square.get_Piece_color() == "black":
        return True

    elif current == "black" and next_square.get_Piece_color() == "white":
        return True

    else: return False
    
# def recursive_linear()
# def recursive_diagonal

if __name__ == "__main__":
    pass