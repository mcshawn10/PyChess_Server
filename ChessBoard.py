import pygame
import sys

from ChessRules import ChessRules
from Piece import *




pygame.init()
clock = pygame.time.Clock()




w_lin = ['wR', 'wQ']
w_diag = ['wB', 'wQ']

b_lin = ['bR', 'bQ']
b_diag = ['bB', 'bQ']






#screen = pygame.display.set_mode((512, 512))  # Setting the screen size






class ChessBoard:
    
    def __init__(self):
        #self.b = b  #  b = board_arr
        self.TAN = (255, 228, 181)  # RGB color combination
        self.BROWN = (139, 101, 8)
        self.rxc = 8  # dimensions of row and columns (9)
        self.height = 512  # dimensions of the board (constants)
        self.width = 512
        self.squares = 512//8  # size of our board squares
        self.colors = [pygame.Color(self.TAN), pygame.Color(self.BROWN)]
        self.PATH = r"C:\\Python\\WORTHY PROJECTS\\PyChess_Server\\chess_pieces\\"
        self.Pieces = {}
        self.white = ['wR', 'wN', 'wB', 'wQ', 'wK', 'wp']
        self.black = ['bR', 'bN', 'bB', 'bQ', 'bK','bp']
        self.avail_white = ['wR', 'wN', 'wB', 'wQ', 'wK','wR', 'wN', 'wB','wp','wp','wp','wp','wp','wp','wp','wp']
        self.avail_black = ['bR', 'bN', 'bB', 'bQ', 'bK','bR', 'bN', 'bB','bp','bp','bp','bp','bp','bp','bp','bp']

        self.clicks_stored = []
        self.clicks_clicked = ()
        self.move_color = ["-"]


        self.screen = pygame.display.set_mode((512, 512))  # Setting the screen size
        self.screen.fill(pygame.Color((255, 228, 181)))  # intitally fills screen to be all tan color
        pygame.display.set_caption("A.I. HW #2")  # title of the pygame window

# needed arrays/tuples

        self.board_arr = [
            ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
             ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
             ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR']]
    
    def board(self):        
        for row in range(self.rxc):
            for col in range(self.rxc):
                color = self.colors[((row+col) % 2)]
                pygame.draw.rect(self.screen, color, pygame.Rect(
                    col*self.squares, row*self.squares, self.squares, self.squares))

    def import_pieces(self):        
        pieces = ['bB', 'bK', 'bN', 'bp', 'bQ', 'bR','wB', 'wK', 'wN', 'wp', 'wQ', 'wR']
        for piece in pieces:
            self.Pieces[piece] = pygame.transform.scale(pygame.image.load(
                self.PATH + piece + ".png"), (self.squares, self.squares))

    def draw_piece(self):
        for row in range(self.rxc):
            for col in range(self.rxc):
                piece = self.board_arr[row][col]
                if piece != '.':
                    self.screen.blit(self.Pieces[piece], pygame.Rect(col*self.squares, row*self.squares,
                                                       self.squares, self.squares))

    def move_piece(self): #ip_pos is a tuple (row, col)
                    
        row_current, col_current = self.clicks_stored[0]            
        row_next, col_next = self.clicks_stored[1]         
        selected_piece = self.board_arr[row_current][col_current]

        #highlight piece
        
        

        if self.board_arr[row_next][col_next] in self.avail_white:
            self.avail_white.remove(self.board_arr[row_next][col_next])
        if self.board_arr[row_next][col_next] in self.avail_black:
            self.avail_black.remove(self.b[row_next][col_next])
        self.board_arr[row_next][col_next] = '.'
        #self.update()
        self.board_arr[row_next][col_next] = selected_piece
        self.board_arr[row_current][col_current] = '.'

        self.undo_highlight((row_current, col_current))
        self.undo_highlight((row_next, col_next))

        self.clicks_clicked = ()
        self.clicks_stored.clear()
            
    def what_color(self,p):
        
        if p == '.':
            return "blank"
        elif p in self.white:
            return "white"
        elif p in self.black:
            return "black"
          
    def get_name(self, p):
        name = "_"
        if p == '.':
            name = "blank"
        if p == 'bp' or p == 'wp':
            name = "pawn"            
        if p == 'wK' or p == 'bK':
            name = "king"            
        if p == 'wQ' or p == 'bQ':
            name = "queen"            
        if p == 'bR' or p == 'wR':
            name = "rook"            
        if p == 'bN' or p == 'wN':
            name = "knight"            
        if p == 'bB' or p == 'wB':
            name = "bishop"
        return name   

    def two_pieces(self, cs, cc): #returns the two pieces that are interacting
                   
        row_c, col_c = cs[0]
        selected_piece = self.board_arr[row_c][col_c]
        name1 = self.get_name(selected_piece)  
        curr_color = self.what_color(selected_piece)
        cp = Piece(cs[0], name1, curr_color)

        row_n, col_n = cs[1] 
        next_piece = self.board_arr[row_n][col_n]
        name2 = self.get_name(next_piece)
        next_color = self.what_color(next_piece)
        np = Piece(cs[1], name2, next_color)
        
        return cp, np

    def get_clicks(self, ip_pos, cs, cc):   
        if cc == ip_pos:
            cc = ()
            cs.clear()
        else:
            cc = ip_pos
            cs.append(cc)
        return cc, cs           
      
    def update(self):
        
        colors = [pygame.Color(self.TAN), pygame.Color(self.BROWN)]
        for row in range(self.rxc):
            for col in range(self.rxc):
                piece = self.board_arr[row][col]
                if piece != '.':
                    self.screen.blit(self.Pieces[piece], pygame.Rect(col*self.squares, row*self.squares,
                                                       self.squares, self.squares))  # draws pieces onto the board
                elif piece == '.':
                        color = colors[((row+col) % 2)]
                        pygame.draw.rect(self.screen, color, pygame.Rect(
                    col*self.squares, row*self.squares, self.squares, self.squares))

    def get_pos(self,pos):
        x, y = pos
        row = y // self.squares
        col = x // self.squares
        return row, col  # get position of piece

    def inst_piece(self, pos):
        r,c = pos[0],pos[1]
        piece = self.board_arr[r][c]
        name = self.get_name(piece)
        clr = self.what_color(piece)
        return self.Piece(pos,name,clr)

    def highlight_square(self, pos):
        r,c = pos[0],pos[1]

        pygame.draw.rect(self.screen, (255,255,51), (c*self.squares, r*self.squares, self.squares, self.squares), 3)
        pygame.display.flip()
        
        #get the position, and draw an empty square given to coordinates
    def undo_highlight(self, pos):
        r,c = pos[0],pos[1]
        color = self.colors[((r+c) % 2)]
        pygame.draw.rect(self.screen, color, (c*self.squares, r*self.squares, self.squares, self.squares), 3)
        pygame.display.flip()

    def RUN_ALL(self):
        
        self.board()
        self.import_pieces()
        self.draw_piece()

        while True:
        # game loop
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # command that makes the game quit
                    pygame.quit()
                    sys.exit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()                    
                    x, y = self.get_pos(mouse_pos)
                    self.highlight_square((x, y))
                    
                    self.clicks_clicked, self.clicks_stored = self.get_clicks((x,y), self.clicks_stored, self.clicks_clicked)
                   
                    if len(self.clicks_stored) == 2:
                         
                        curr_piece, nxt_piece = self.two_pieces(self.clicks_stored, self.clicks_clicked)

                         
                        if self.move_color[0] == curr_piece.color:
                            self.clicks_clicked = ()
                            self.clicks_stored.clear()                            
                            continue

                        elif self.move_color[0] != curr_piece.color:
                            self.move_color.clear()
                            self.move_color.append(curr_piece.color)
                            rlz = ChessRules(curr_piece, nxt_piece)

                            if rlz.is_legal(self.board_arr) == True:
                                rlz.in_check(self.board_arr)
                                if rlz.self_check(curr_piece.pos[0],curr_piece.pos[1], self.board_arr):                                
                                    self.move_piece() # may need to modify to just taking in the two points
                                if not rlz.self_check(curr_piece.pos[0],curr_piece.pos[1], self.board_arr):
                                    self.clicks_clicked = ()
                                    self.clicks_stored.clear()
                            else: 
                                self.clicks_clicked = ()
                                self.clicks_stored.clear()
                    #undo_highlight
                    self.update()
                    

                
                    

            
            clock.tick(60)  # clock running at 60 FPS
            pygame.display.flip()



if __name__ == "__main__":

    pass