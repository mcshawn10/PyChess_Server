
def same_color(current, other):
    return current.color == other.color


def is_lin_atk(p): #if linear is clear, return true, if not...
        
    w_lin = ['wR', 'wQ']
    b_lin = ['bR', 'bQ']
    
    if p.name == '.': return False
    elif p.color == "white" and p.name in w_lin:
        return True
        
    elif p.color == "black" and p.name in b_lin:
        return True

    else: return False

def is_diag_atk(p):
    w_diag = ['wB', 'wQ']
    b_diag = ['bB', 'bQ']
    
    if p.name == '.': return False

    elif p.color == "white" and p.name in w_diag:
        return True
            
    elif p.color == "black" and p.name in b_diag:
        return True

    else: return False

def is_clear_diag(c, g, board_arr):  # positions (r,c) of the current and the goal
        
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


def is_legal(current_piece, next_piece):

    if current_piece.color == next_piece.color: return False

    else: return current_piece.move_is_legal(next_piece.pos)

def return_current_king(current_piece, board_arr):

    if current_piece.color == "white":
    
        for r in range(8):
            for c in range(8):
                if board_arr[r][c].name == '.': continue

                elif board_arr[r][c].name == 'wK': return board_arr[r][c]
                        

    if current_piece.color == "black":

        for r in range(8):
            for c in range(8):
                if board_arr[r][c].name == '.': continue

                elif board_arr[r][c].name == 'bK': return board_arr[r][c]

def does_not_put_self_in_check(k, current_piece, board_arr, next_pos):
    
    
    r = current_piece.pos[0]
    c = current_piece.pos[1]
    
    #check left
    if k.pos[0] == current_piece.pos[0] and k.pos[1]-current_piece.pos[1]>0:
        nc = c-1
        if board_arr[r][nc].name != '.':
            if same_color(k, board_arr[r][nc]):
                return True
            else:  # if not same color, check what piece it is and is it attacking
                if is_lin_atk(board_arr[r][nc]): # if 
                    return captures_next_pos([r,nc], next_pos)
                elif not is_lin_atk(board_arr[r][nc]):
                    return True
        else:
            return does_not_put_self_in_check(k, board_arr[r][nc], board_arr, next_pos)
    #check right/ linear
    elif k.pos[0] == current_piece.pos[0] and k.pos[1]-current_piece.pos[1]<0:
        nc = c+1
        if nc > 7: return True
        if board_arr[r][nc].name != '.':
            if same_color(k, board_arr[r][nc]):
                return True
            else:
                if is_lin_atk(board_arr[r][nc]):
                    captures_next_pos([r,nc], next_pos)
                elif not is_lin_atk(board_arr[r][nc]):
                    return True
        else:
            return does_not_put_self_in_check(k, board_arr[r][nc], board_arr, next_pos)
    #NE
    elif k.pos[0]-current_piece.pos[0]>0 and k.pos[1]-current_piece.pos[1]<0:
        nc = c+1
        nr = r-1
        if nc > 7 or nr < 0: return True
        if board_arr[nr][nc].name != '.':
            if same_color(k, board_arr[nr][nc]):
                return True
            else:
                if is_diag_atk(board_arr[nr][nc]):
                    return captures_next_pos([nr,nc], next_pos)
                elif not is_diag_atk(board_arr[nr][nc]):
                    return True
        else:
            return does_not_put_self_in_check(k, board_arr[nr][nc], board_arr, next_pos)
    #SE
    elif k.pos[0]-current_piece.pos[0]<0 and k.pos[1]-current_piece.pos[1]<0:
        nc = c+1
        nr = r+1
        if nc > 7 or nr > 7: return True
        if board_arr[nr][nc].name != '.':
            if same_color(k, board_arr[nr][nc]):
                return True
            else:
                if is_diag_atk(board_arr[nr][nc]):
                    return captures_next_pos([nr,nc], next_pos)
                elif not is_diag_atk(board_arr[nr][nc]):
                    return True
        else:
            return does_not_put_self_in_check(k, board_arr[nr][nc], board_arr, next_pos)

    #SW
    elif k.pos[0]-current_piece.pos[0]<0 and k.pos[1]-current_piece.pos[1]>0:
        nc = c-1
        nr = r+1
        if nc < 0 or nr > 7: return True
        if board_arr[nr][nc].name != '.':
            if same_color(k, board_arr[nr][nc]):
                return True
            else:
                if is_diag_atk(board_arr[nr][nc]):
                    return captures_next_pos([nr,nc], next_pos)
                elif not is_diag_atk(board_arr[nr][nc]):
                    return True
        else:
            return does_not_put_self_in_check(k, board_arr[nr][nc], board_arr, next_pos)
    #NW
    elif k.pos[0]-current_piece.pos[0]>0 and k.pos[1]-current_piece.pos[1]>0: # have to adjust this so that an empty square doesnt cause bugs
        nc = c-1
        nr = r-1
        if nc < 0 or nr < 0: return True
        if board_arr[nr][nc].name != '.':
            if same_color(k, board_arr[nr][nc]):
                return True
            else:
                if is_diag_atk(board_arr[nr][nc]):
                    return captures_next_pos([nr,nc], next_pos)
                elif not is_diag_atk(board_arr[nr][nc]):
                    
                    return True
        else:
            return does_not_put_self_in_check(k, board_arr[nr][nc], board_arr, next_pos)
    #front
    elif k.pos[1]==current_piece.pos[1] and k.pos[0]-current_piece.pos[0]>0:
        nr = r-1
        if nr < 0: return True
        if board_arr[nr][c].name != '.':
            if same_color(k, board_arr[nr][c]): #if same color then all good
                return True
            else:  # if not same color, check what piece it is and is it attacking
                if is_lin_atk(board_arr[nr][c]):
                    return captures_next_pos([nr,c], next_pos)
                elif not is_lin_atk(board_arr[nr][c]):
                    return True
        else:
            return does_not_put_self_in_check(k, board_arr[nr][c], board_arr, next_pos)
    #back
    elif k.pos[1]==current_piece.pos[1] and k.pos[0]-current_piece.pos[0]<0:
        nr= r+1
        if nr > 7: return True
        if board_arr[nr][c].name != '.':
            if same_color(k, board_arr[nr][c]):
                return True
            else:
                if is_lin_atk(board_arr[nr][c]):
                    return captures_next_pos([nr,c], next_pos)
                elif not is_lin_atk(board_arr[nr][c]):
                    return True
        else:
            return does_not_put_self_in_check(k, board_arr[nr][c], board_arr, next_pos)


def new_does_not_put_self_in_check(k, current_piece, board_arr):
    white = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wp']
    black = ['bR', 'bN', 'bB', 'bQ', 'bK','bp']
    #k = return_current_king(current_piece, board_arr)
    r = current_piece.pos[0]
    c = current_piece.pos[1]
    
    '''
    take the kings position and the next position of the piece
    check is clear linearly and diagnolly for king
    if not clear, check if it is an attack '''
    #check linear
    if not is_clear_lin(k.pos, current_piece.pos, board_arr):
        return is_lin_atk()
def in_check(current_piece):

    pass

def captures_next_pos(p, np):
    '''this function is more like, check where the current piece is moving to, if it's capturing the checker, then move is safe'''
    return p == np

if __name__ == "__main__":
    pass