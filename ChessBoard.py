import pygame
import sys

from Piece import *


pygame.init()
clock = pygame.time.Clock()




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
        self.board_arr = [[Empty([y,x]) for x in range(self.rxc)] for y in range(self.rxc)]

        self.board_arr[0][0] = Rook([0,0], "bR", "black", self.board_arr)
        self.board_arr[0][1] = Knight([0,1], "bN", "black", self.board_arr)
        self.board_arr[0][2] = Bishop([0,2], "bB", "black", self.board_arr)
        self.board_arr[0][3] = Queen([0,3], "bQ", "black", self.board_arr)
        self.board_arr[0][4] = King([0,4], "bK", "black", self.board_arr)
        self.board_arr[0][5] = Bishop([0,5], "bB", "black", self.board_arr)
        self.board_arr[0][6] = Knight([0,6], "bN", "black", self.board_arr)
        self.board_arr[0][7] = Rook([0,7], "bR", "black", self.board_arr)

        self.board_arr[1][0] = Pawn([1,0], "bp", "black", self.board_arr)
        self.board_arr[1][1] = Pawn([1,1], "bp", "black", self.board_arr)
        self.board_arr[1][2] = Pawn([1,2], "bp", "black", self.board_arr)
        self.board_arr[1][3] = Pawn([1,3], "bp", "black", self.board_arr)
        self.board_arr[1][4] = Pawn([1,4], "bp", "black", self.board_arr)
        self.board_arr[1][5] = Pawn([1,5], "bp", "black", self.board_arr)
        self.board_arr[1][6] = Pawn([1,6], "bp", "black", self.board_arr)
        self.board_arr[1][7] = Pawn([1,7], "bp", "black", self.board_arr)
        
        self.board_arr[6][0] = Pawn([6,0], "wp", "white", self.board_arr)
        self.board_arr[6][1] = Pawn([6,1], "wp", "white", self.board_arr)
        self.board_arr[6][2] = Pawn([6,2], "wp", "white", self.board_arr)
        self.board_arr[6][3] = Pawn([6,3], "wp", "white", self.board_arr)
        self.board_arr[6][4] = Pawn([6,4], "wp", "white", self.board_arr)
        self.board_arr[6][5] = Pawn([6,5], "wp", "white", self.board_arr)
        self.board_arr[6][6] = Pawn([6,6], "wp", "white", self.board_arr)
        self.board_arr[6][7] = Pawn([6,7], "wp", "white", self.board_arr)

        
        self.board_arr[7][0] = Rook([7,0], "wR", "white", self.board_arr)
        self.board_arr[7][1] = Knight([7,1], "wN", "white", self.board_arr)
        self.board_arr[7][2] = Bishop([7,2], "wB", "white", self.board_arr)
        self.board_arr[7][3] = Queen([7,3], "wQ", "white", self.board_arr)
        self.board_arr[7][4] = King([7,4], "wK", "white", self.board_arr)
        self.board_arr[7][5] = Bishop([7,5], "wB", "white", self.board_arr)
        self.board_arr[7][6] = Knight([7,6], "wN", "white", self.board_arr)
        self.board_arr[7][7] = Rook([7,7], "wR", "white", self.board_arr)
     
        
    
    def draw_board(self):        
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

    def draw_pieces(self):
        for row in range(self.rxc):
            for col in range(self.rxc):
                piece = self.board_arr[row][col]
                '''blit piece.image'''
                if piece.name != '.':
                    self.screen.blit(self.Pieces[piece.name], pygame.Rect(col*self.squares, row*self.squares,
                                                       self.squares, self.squares))

    def move_piece(self): #ip_pos is a tuple (row, col)
                    
        row_current, col_current = self.clicks_stored[0]            
        row_next, col_next = self.clicks_stored[1]         
        selected_piece = self.board_arr[row_current][col_current]

        #highlight piece
    
        if self.board_arr[row_next][col_next] in self.avail_white:
            self.avail_white.remove(self.board_arr[row_next][col_next])
        if self.board_arr[row_next][col_next] in self.avail_black:
            self.avail_black.remove(self.board_arr[row_next][col_next])


        self.board_arr[row_next][col_next] = Empty([row_next, col_next])
        self.update()
        self.board_arr[row_next][col_next] = selected_piece
        selected_piece.pos = [row_next, col_next]
        self.board_arr[row_current][col_current] = Empty([row_current, col_current])
        
        self.undo_highlight((row_current, col_current))
        self.undo_highlight((row_next, col_next))

        self.clicks_clicked = ()
        self.clicks_stored.clear()


    
    def return_active_pieces(self, cs): #returns the two pieces that are interacting
                   
        row_c, col_c = cs[0]
        selected_piece = self.board_arr[row_c][col_c]
        row_n, col_n = cs[1] 
        next_piece = self.board_arr[row_n][col_n]
            
        return selected_piece, next_piece

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
                
                if piece.name != '.':
                    self.screen.blit(self.Pieces[piece.name], pygame.Rect(col*self.squares, row*self.squares,
                                                       self.squares, self.squares))  # draws pieces onto the board
                elif piece.name == '.':
                        color = colors[((row+col) % 2)]
                        pygame.draw.rect(self.screen, color, pygame.Rect(
                    col*self.squares, row*self.squares, self.squares, self.squares))


    def get_pos(self, pos):
        x, y = pos
        row = y // self.squares
        col = x // self.squares
        return row, col  # get position of piece

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
        
        self.draw_board()
        self.import_pieces()
        self.draw_pieces()

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
    
                        curr_piece, next_piece = self.return_active_pieces(self.clicks_stored)
                        if self.move_color[0] == curr_piece.color:
                            self.clicks_clicked = ()
                            self.clicks_stored.clear()  
                            self.undo_highlight(curr_piece.pos)                          
                            continue
                        
                        if self.move_color[0] != curr_piece.color:
                            
                            self.move_color.clear()
                            self.move_color.append(curr_piece.color)
                            #if move is legal, then check for checks 
                            if curr_piece.move_is_legal(next_piece.pos):
                                k = return_current_king(curr_piece, self.board_arr)
                                if does_not_put_self_in_check(k, curr_piece, self.board_arr):                                
                                    self.move_piece() 
                                    pygame.display.flip()
                                    # may need to modify to just taking in the two points
                                else:
                                    self.clicks_clicked = ()
                                    self.clicks_stored.clear() 
                            else: 
                                print("got here instead")
                                self.clicks_clicked = ()
                                self.clicks_stored.clear()
                    #undo_highlight
                self.update()
            
            clock.tick(60)  # clock running at 60 FPS
            pygame.display.flip()



if __name__ == "__main__":

    pass