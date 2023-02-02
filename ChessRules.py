
import pygame
from Piece import *
class ChessRules():
    def __init__(self, curr, nxt): # where you pass in two Piece objects
        self.curr = curr
        self.nxt = nxt
        self.all_pieces = ['bR', 'bN', 'bB', 'bQ', 'bK','bp','wR', 'wN', 'wB', 'wQ', 'wK', 'wp']
        self.white = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wp']
        self.black = ['bR', 'bN', 'bB', 'bQ', 'bK','bp']
    
    def is_legal(self, board_arr): #  where n is the next coordinate (row,col)
        
        name = self.curr.name

        if self.curr.color == self.nxt.color:
            return False
            
        if name == "pawn": # INCLUDE THE COLOR IF STATEMENT
            if self.curr.color == "white":

                if (self.curr.pos[0] == 6) and (self.nxt.pos[0] == 4) and (self.curr.pos[1]==self.nxt.pos[1]):
                    return True
                elif self.nxt.pos[0] == self.curr.pos[0]-1:
                    return True
                elif (self.nxt.pos[1] == self.curr.pos[1]+1 or self.nxt.pos[1] == self.curr.pos[1]-1) and (self.nxt.pos[0] == self.curr.pos[0]-1):
                    return True
                else: return False
            else:
                if (self.curr.pos[0] == 1) and (self.nxt.pos[0] == 3) and (self.curr.pos[1]==self.nxt.pos[1]):
                    return True
                elif self.nxt.pos[0] == self.curr.pos[0]+1:
                    return True
                elif (self.nxt.pos[1] == self.curr.pos[1]-1 or self.nxt.pos[1] == self.curr.pos[1]+1) and (self.nxt.pos[0] == self.curr.pos[0]+1):
                    return True
                else: return False        

        elif name == "king":
            if abs(self.curr.pos[0]-self.nxt.pos[0])==1 or abs(self.curr.pos[1]-self.nxt.pos[1])==1:
                return True
            else: return False

        elif name == "queen":
            if abs(self.curr.pos[0]-self.nxt.pos[0])>=1 or abs(self.curr.pos[1]-self.nxt.pos[1])>=1:
                if (self.curr.pos[0] == self.nxt.pos[0]) or (self.curr.pos[1] == self.nxt.pos[1]):
                    if self.is_clear_lin(self.curr.pos, self.nxt.pos, board_arr):
                        return True

                elif abs(self.curr.pos[0]-self.nxt.pos[0])>=1 and abs(self.curr.pos[1]-self.nxt.pos[1])>=1:        
                    if self.is_clear_diag(self.curr.pos, self.nxt.pos, board_arr):
                        return True   
            else: return False

        elif name == "knight":
            col_diff = abs(self.curr.pos[1]-self.nxt.pos[1])
            row_diff = abs(self.curr.pos[0]-self.nxt.pos[0])
            if col_diff == 1 and row_diff == 2:
                return True
            if col_diff == 2 and row_diff == 1:
                return True
            else: return False

        elif name == "bishop":
            
            if abs(self.curr.pos[0]-self.nxt.pos[0])>=1 and abs(self.curr.pos[1]-self.nxt.pos[1])>=1:
                
                if self.is_clear_diag(self.curr.pos, self.nxt.pos, board_arr):
                    return True
            else: return False   
                    
        elif name == "rook":
            if (self.curr.pos[0] == self.nxt.pos[0]) or (self.curr.pos[1] == self.nxt.pos[1]):
                if self.is_clear_lin(self.curr.pos, self.nxt.pos, board_arr):
                    return True
            else: return False
    
    def clear_path(self, p, goal): #goal is a tuple
        if abs(self.curr.pos[0]-goal[0])==1 or abs(self.curr.pos[1]-self.goal[1])==1:
            return True
        else: return False

    def is_clear_diag(self, c, g, board_arr):  # positions (r,c) of the current and the goal
        
        if abs(c[0]-g[0])==1 and abs(c[1]-g[1])==1:
            return True  

        elif c[0]-g[0]>0 and c[1]-g[1]<0: # NE
            
            nr = c[0]-1
            nc = c[1]+1
            if board_arr[nr][nc] != '.':                                 
                return False
            else:           
                return self.is_clear_diag((nr,nc),g, board_arr)            

        elif c[0]-g[0]<0 and c[1]-g[1]<0: # SE
            
            nr = c[0]+1
            nc = c[1]+1
            if board_arr[nr][nc] != '.':
                return False
            else:
                return self.is_clear_diag((nr,nc),g, board_arr)

        elif c[0]-g[0]>0 and c[1]-g[1]>0: # NW
            
            nr = c[0]-1
            nc = c[1]-1
            if board_arr[nr][nc] != '.':
                return False
            else:
                return self.is_clear_diag((nr,nc),g)

        elif c[0]-g[0]<0 and c[1]-g[1]>0: # SW
            
            nr = c[0]+1
            nc = c[1]-1
            if board_arr[nr][nc] != '.':
                return False
            else:
                return self.is_clear_diag((nr,nc),g)

    def is_clear_lin(self,c , g, board_arr):
        

        if (abs(c[0]-g[0])==1 or abs(c[1]-g[1])==1):
            return True
        
        elif c[0]-g[0]>0: #  N
            nr = c[0]-1
            if board_arr[nr][c[1]] != '.':
                return False
            else:
                return self.is_clear_lin((nr,c[1]), g, board_arr)

        elif c[0]-g[0]<0: #  S
            nr = c[0]+1
            if board_arr[nr][c[1]] != '.':
                return False
            else:
                return self.is_clear_lin((nr,c[1]), g, board_arr)

        elif c[1]-g[1]<0: #  E
            nc = c[1]+1
            if board_arr[c[0]][nc] != '.':
                return False
            else:
                return self.is_clear_lin((c[0],nc), g, board_arr)
        elif c[1]-g[1]>0: #  W
            nc = c[1]-1
            if board_arr[c[0]][nc] != '.':
                return False
            else:
                return self.is_clear_lin((c[0],nc), g, board_arr)

    def in_check(self, board_arr):
        k = self.get_kings(board_arr)

        if self.curr.name == "rook" or self.curr.name == "queen":
            if k.pos[0] == self.nxt.pos[0] or k.pos[1] == self.nxt.pos[1]:
                print("in check")

        if self.curr.name == "bishop" or self.curr.name == "queen":
            if abs(k.pos[0]-k.pos[1]) == abs(self.nxt.pos[0]-self.nxt.pos[1]) or (k.pos[0]+k.pos[1]) == self.nxt.pos[0]+self.nxt.pos[1]:
                if self.is_clear_diag(self.nxt.pos,k.pos, board_arr)==True:
                
                    print("in check")

        if self.curr.name == "pawn":
            if abs(k.pos[0]-self.nxt.pos[0])==1 and abs(k.pos[1]-self.nxt.pos[1])==1:
                print("in check") 

    def checkmate(self, c, k):
        pass 
         
    def get_kings(self, board_arr):
        
        
        if self.curr.color == "white":

            for i in board_arr:
                for j in i:
                    if j == 'bK':
                        coord = (board_arr.index(i),i.index(j))
                        return Piece(coord, "king","black")
        if self.curr.color == "black":
    
            for i in board_arr:
                for j in i:
                    if j == 'wK':
                        coord = (board_arr.index(i),i.index(j))
                        return Piece(coord, "king", "white")

    def same_king(self, board_arr):
        
        
        if self.curr.color == "white":

            for i in board_arr:
                for j in i:
                    if j == 'wK':
                        coord = (board_arr.index(i),i.index(j))
                        return Piece(coord, "king","white")
        if self.curr.color == "black":
    
            for i in board_arr:
                for j in i:
                    if j == 'bK':
                        coord = (board_arr.index(i),i.index(j))
                        return Piece(coord, "king", "black")
    def lin_atk(self,p):
        
        w_lin = ['wR', 'wQ']
        b_lin = ['bR', 'bQ']
        
        if p in self.white:
            if p in w_lin:
                return True
            else: return False
        elif p in self.black:
            if p in b_lin:
                
                return True
            else: return False

    def diag_atk(self,p):
        w_diag = ['wB', 'wQ']
        b_diag = ['bB', 'bQ']
        

        if p in self.white:
            if p in w_diag:
                return True
            else: return False
        elif p in self.black:
            if p in b_diag:
                
                return True
            else: return False

    def check_color(self, k, p):
        
        color = "-"
        if p in self.white:
            color = "white"
            if k.color == color:
                return True
            else: 
                return False 
        elif p in self.black:
            color = "black"
            if k.color == color:
                return True
            else: 
                return False
        
        
    def self_check(self,r,c, board_arr): # function will determine if the current piece to be moved will put own king in check, RC of curr
        white = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wp']
        black = ['bR', 'bN', 'bB', 'bQ', 'bK','bp']
        k = self.same_king(board_arr)

        #check left
        if k.pos[0] == self.curr.pos[0] and k.pos[1]-self.curr.pos[1]>0:
            nc = c-1
            if board_arr[r][nc] != '.':
                if self.check_color(k, board_arr[r][nc]):
                    return True
                else:  # if not same color, check what piece it is and is it attacking
                    if self.lin_atk(board_arr[r][nc]):
                        return False
                    elif not self.lin_atk(board_arr[r][nc]):
                        return True
            else:
                return self.self_check(r, nc, board_arr)
        #check right
        elif k.pos[0] == self.curr.pos[0] and k.pos[1]-self.curr.pos[1]<0:
            nc = c+1
            if board_arr[r][nc] != '.':
                if self.check_color(k, board_arr[r][nc]):
                    return True
                else:
                    if self.lin_atk(board_arr[r][nc]):
                        return False
                    elif not self.lin_atk(board_arr[r][nc]):
                        return True
            else:
                return self.self_check(r, nc, board_arr)
        #NE
        elif k.pos[0]-self.curr.pos[0]>0 and k.pos[1]-self.curr.pos[1]<0:
            nc = c+1
            nr = r-1
            if board_arr[nr][nc] != '.':
                if self.check_color(k, board_arr[nr][nc]):
                    return True
                else:
                    if self.diag_atk(board_arr[nr][nc]):
                        return False
                    elif not self.diag_atk(board_arr[nr][nc]):
                        return True
            else:
                return self.self_check(nr, nc, board_arr)
        #SE
        elif k.pos[0]-self.curr.pos[0]<0 and k.pos[1]-self.curr.pos[1]<0:
            nc = c+1
            nr = r+1
            if board_arr[nr][nc] != '.':
                if self.check_color(k, board_arr[nr][nc]):
                    return True
                else:
                    if self.diag_atk(board_arr[nr][nc]):
                        return False
                    elif not self.diag_atk(board_arr[nr][nc]):
                        return True
            else:
                return self.self_check(nr, nc, board_arr)

        #SW
        elif k.pos[0]-self.curr.pos[0]<0 and k.pos[1]-self.curr.pos[1]>0:
            nc = c-1
            nr = r+1
            if board_arr[nr][nc] != '.':
                if self.check_color(k, board_arr[nr][nc]):
                    return True
                else:
                    if self.diag_atk(board_arr[nr][nc]):
                        return False
                    elif not self.diag_atk(board_arr[nr][nc]):
                        return True
            else:
                return self.self_check(nr, nc, board_arr)
        #NW
        elif k.pos[0]-self.curr.pos[0]>0 and k.pos[1]-self.curr.pos[1]>0:
            nc = c-1
            nr = r-1
            if board_arr[nr][nc] != '.':
                if self.check_color(k, board_arr[nr][nc]):
                    return True
                else:
                    if self.diag_atk(board_arr[nr][nc]):
                        return False
                    elif not self.diag_atk(board_arr[nr][nc]):
                        print("not working")
                        return True
            else:
                return self.self_check(nr, nc, board_arr)
        #front
        elif k.pos[1]==self.curr.pos[1] and k.pos[0]-self.curr.pos[0]>0:
            nr = r-1
            if board_arr[nr][c] != '.':
                if self.check_color(k, board_arr[nr][c]): #if same color then all good
                    return True
                else:  # if not same color, check what piece it is and is it attacking
                    if self.lin_atk(board_arr[nr][c]):
                        return False
                    elif not self.lin_atk(board_arr[nr][c]):
                        return True
            else:
                return self.self_check(nr, c, board_arr)
        #back
        elif k.pos[1]==self.curr.pos[1] and k.pos[0]-self.curr.pos[0]<0:
            nr= r+1
            if board_arr[nr][c] != '.':
                if self.check_color(k, board_arr[nr][c]):
                    return True
                else:
                    if self.lin_atk(board_arr[nr][c]):
                        return False
                    elif not self.lin_atk(board_arr[nr][c]):
                        return True
            else:
                return self.self_check(nr,c, board_arr)

    
    def safe_square(self):
        pass




if __name__ == "__main__":

    pass