


def is_opposite_color(current: str, next_square):
    
    if current == "white" and next_square.get_Piece_color() == "black":
        return True

    elif current == "black" and next_square.get_Piece_color() == "white":
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



if __name__ == "__main__":
    pass