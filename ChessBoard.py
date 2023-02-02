import pygame
import sys

print("hello world")


class ChessBoard:
    
    def __init__(self, b):
        self.b = b  #  b = board_arr
        self.TAN = (255, 228, 181)  # RGB color combination
        self.BROWN = (139, 101, 8)
        self.rxc = 8  # dimensions of row and columns (9)
        self.height = 512  # dimensions of the board (constants)
        self.width = 512
        self.squares = 512//8  # size of our board squares
        self.colors = [pygame.Color(self.TAN), pygame.Color(self.BROWN)]
        self.PATH = r"C:\\Python\\WORTHY PROJECTS\\AI_hw\\chess_pieces\\"
    
    def board(self):        
        for row in range(self.rxc):
            for col in range(self.rxc):
                color = self.colors[((row+col) % 2)]
                pygame.draw.rect(screen, color, pygame.Rect(
                    col*self.squares, row*self.squares, self.squares, self.squares))

    def import_pieces(self):        
        pieces = ['bB', 'bK', 'bN', 'bp', 'bQ', 'bR','wB', 'wK', 'wN', 'wp', 'wQ', 'wR']
        for piece in pieces:
            Pieces[piece] = pygame.transform.scale(pygame.image.load(
                self.PATH + piece + ".png"), (self.squares, self.squares))

    def draw_piece(self):
        for row in range(self.rxc):
            for col in range(self.rxc):
                piece = self.b[row][col]
                if piece != '.':
                    screen.blit(Pieces[piece], pygame.Rect(col*self.squares, row*self.squares,
                                                       self.squares, self.squares))

    def move_piece(self): #ip_pos is a tuple (row, col)
        global clicks_clicked, clicks_stored, avail_black, avail_white              
        row_current, col_current = clicks_stored[0]            
        row_next, col_next = clicks_stored[1]         
        selected_piece = self.b[row_current][col_current]

        #highlight piece
        
        

        if self.b[row_next][col_next] in avail_white:
            avail_white.remove(self.b[row_next][col_next])
        if self.b[row_next][col_next] in avail_black:
            avail_black.remove(self.b[row_next][col_next])
        self.b[row_next][col_next] = '.'
        #self.update()
        self.b[row_next][col_next] = selected_piece
        self.b[row_current][col_current] = '.'

        self.undo_highlight((row_current, col_current))
        self.undo_highlight((row_next, col_next))

        clicks_clicked = ()
        clicks_stored.clear()
            
    def what_color(self,p):
        global white, black
        if p == '.':
            return "blank"
        elif p in white:
            return "white"
        elif p in black:
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
        selected_piece = self.b[row_c][col_c]
        name1 = self.get_name(selected_piece)  
        curr_color = self.what_color(selected_piece)
        cp = Piece(cs[0], name1, curr_color)

        row_n, col_n = cs[1] 
        next_piece = self.b[row_n][col_n]
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
        global screen 
        colors = [pygame.Color(self.TAN), pygame.Color(self.BROWN)]
        for row in range(self.rxc):
            for col in range(self.rxc):
                piece = self.b[row][col]
                if piece != '.':
                    screen.blit(Pieces[piece], pygame.Rect(col*self.squares, row*self.squares,
                                                       self.squares, self.squares))  # draws pieces onto the board
                elif piece == '.':
                        color = colors[((row+col) % 2)]
                        pygame.draw.rect(screen, color, pygame.Rect(
                    col*self.squares, row*self.squares, self.squares, self.squares))

    def get_pos(self,pos):
        x, y = pos
        row = y // self.squares
        col = x // self.squares
        return row, col  # get position of piece

    def inst_piece(self, pos):
        r,c = pos[0],pos[1]
        piece = self.b[r][c]
        name = self.get_name(piece)
        clr = self.what_color(piece)
        return Piece(pos,name,clr)

    def highlight_square(self, pos):
        r,c = pos[0],pos[1]

        pygame.draw.rect(screen, (255,255,51), (c*self.squares, r*self.squares, self.squares, self.squares), 3)
        pygame.display.flip()
        
        #get the position, and draw an empty square given to coordinates
    def undo_highlight(self, pos):
        r,c = pos[0],pos[1]
        color = self.colors[((r+c) % 2)]
        pygame.draw.rect(screen, color, (c*self.squares, r*self.squares, self.squares, self.squares), 3)
        pygame.display.flip()

    def RUN_ALL(self):
        global clicks_stored, clicks_clicked, move_color
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
                    
                    clicks_clicked, clicks_stored = self.get_clicks((x,y), clicks_stored, clicks_clicked)
                   
                    if len(clicks_stored) == 2:
                         
                        curr_piece, nxt_piece = self.two_pieces(clicks_stored, clicks_clicked)

                         
                        if move_color[0] == curr_piece.color:
                            clicks_clicked = ()
                            clicks_stored.clear()                            
                            continue

                        elif move_color[0] != curr_piece.color:
                            move_color.clear()
                            move_color.append(curr_piece.color)
                            rlz = ChessRules(curr_piece, nxt_piece)

                            if rlz.is_legal() == True:
                                rlz.in_check()
                                if rlz.self_check(curr_piece.pos[0],curr_piece.pos[1]):                                
                                    self.move_piece() # may need to modify to just taking in the two points
                                if not rlz.self_check(curr_piece.pos[0],curr_piece.pos[1]):
                                    clicks_clicked = ()
                                    clicks_stored.clear()
                            else: 
                                clicks_clicked = ()
                                clicks_stored.clear()
                    #undo_highlight
                    self.update()
                    

                
                    

            
            clock.tick(60)  # clock running at 60 FPS
            pygame.display.flip()
