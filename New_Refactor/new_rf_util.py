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

def is_in_bounds(coordinate:tuple):
    if coordinate[0] >= 0 and coordinate[0] < 8 and coordinate[1] >= 0 and coordinate[1] < 8:
        return True
    else: return False


def is_clear_diag(c:tuple, g:tuple, board_arr:list[list]):   # positions (r,c) of the current and the goal
        # you can pass in the coordinates, do you need to pass in the board_arr
        if abs(c[0]-g[0])==1 and abs(c[1]-g[1])==1:
            return True  

        elif c[0]-g[0]>0 and c[1]-g[1]<0: # NE
            
            nr = c[0]-1
            nc = c[1]+1
            if board_arr[nr][nc].name != '.':                                 
                return False
            else:           
                return is_clear_diag((nr,nc),g, board_arr)            

        elif c[0]-g[0]<0 and c[1]-g[1]<0: # SE
            
            nr = c[0]+1
            nc = c[1]+1
            if board_arr[nr][nc].name != '.':
                return False
            else:
                return is_clear_diag((nr,nc),g, board_arr)

        elif c[0]-g[0]>0 and c[1]-g[1]>0: # NW
            
            nr = c[0]-1
            nc = c[1]-1
            if board_arr[nr][nc].name != '.':
                return False
            else:
                return is_clear_diag((nr,nc),g, board_arr)

        elif c[0]-g[0]<0 and c[1]-g[1]>0: # SW
            
            nr = c[0]+1
            nc = c[1]-1
            if board_arr[nr][nc].name != '.':
                return False
            else:
                return is_clear_diag((nr,nc),g, board_arr)

def is_clear_lin(c, g, board_arr): #if linear is clear, return true, if not...
    

    if (abs(c[0]-g[0])==1 or abs(c[1]-g[1])==1):
        return True
    
    elif c[0]-g[0]>0: #  N
        nr = c[0]-1
        if board_arr[nr][c[1]].name != '.':
            return False
        else:
            return is_clear_lin((nr,c[1]), g, board_arr)

    elif c[0]-g[0]<0: #  S
        nr = c[0]+1
        if board_arr[nr][c[1]].name != '.':
            return False
        else:
            return is_clear_lin((nr,c[1]), g, board_arr)

    elif c[1]-g[1]<0: #  E
        nc = c[1]+1
        if board_arr[c[0]][nc].name != '.':
            return False
        else:
            return is_clear_lin((c[0],nc), g, board_arr)
    elif c[1]-g[1]>0: #  W
        nc = c[1]-1
        if board_arr[c[0]][nc].name != '.':
            return False
        else:
            return is_clear_lin((c[0],nc), g, board_arr)


if __name__ == "__main__":
    pass