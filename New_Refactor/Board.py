
import pygame
import sys
from Piece import *
from Square import *
from new_rf_util import *

pygame.init()
clock = pygame.time.Clock()
class Board:

    def __init__(self):
        self.TAN = (255, 228, 181)  # RGB color combination
        self.BROWN = (139, 101, 8)
        self.BLUE = (192,192,192)
        self.GREEN = (102,204,0)
        self.RED = (255,0,0)
        self.rxc = 8  # dimensions of row and columns (9)
        self.height = 640  # dimensions of the board (constants) 512
        self.width = 900
        self.squares = 640//8  # size of our board squares
        self.colors = [pygame.Color(self.TAN), pygame.Color(self.BROWN)]
        
        self.colors = [pygame.Color(self.TAN), pygame.Color(self.BROWN)]
        self.PATH = r"C:\\Python\\WORTHY PROJECTS\\PyChess_Server\\chess_pieces\\"
        self.screen = pygame.display.set_mode((self.width, self.height))  # Setting the screen size
        self.screen.fill(pygame.Color((255, 228, 181)))  # intitally fills screen to be all tan color
        pygame.display.set_caption("PyChess")

        self.color_to_move = "white"
        self.Pieces = {}

        self.board_arr = [[Square(True, (y,x)) for x in range(self.rxc)] for y in range(self.rxc)]
        self.clicks = []
        self.current_move_list = []

        self.BlackKing = (0,4)
        self.WhiteKing = (7,4)
        self.checkmate = False
        self.WhiteInCheck = False
        self.BlackInCheck = False
        self.blackBlockingPieces = None
        self.whiteBlockingPieces = None
        

    def import_pieces(self):        
        pieces = ['bB', 'bK', 'bN', 'bp', 'bQ', 'bR','wB', 'wK', 'wN', 'wp', 'wQ', 'wR']
        for piece in pieces:
            self.Pieces[piece] = pygame.transform.scale(pygame.image.load(
                self.PATH + piece + ".png"), (self.squares, self.squares))
            
    def draw_board(self):        
        for row in range(self.rxc):
            for col in range(self.rxc):
                color = self.colors[((row+col) % 2)]
                pygame.draw.rect(self.screen, color, 
                                 pygame.Rect(col*self.squares, row*self.squares, self.squares, self.squares))
        pygame.draw.line(self.screen, (0,0,0), (self.height, 0), (self.height,self.height), width=4)     

    def draw_player_turn(self):
        pygame.draw.rect(self.screen, self.TAN, pygame.Rect((self.height, 0, self.width-self.height, (self.height//2) )))
        text_font = pygame.font.SysFont("Arial", 30)
        text = text_font.render(f"{self.color_to_move} to play", True, (0,0,0)) 
        self.screen.blit(text, (700, 200))
        
    def set_pieces(self):
        
        for j in range(self.rxc):  
            
            square = self.board_arr[1][j]
            square.is_empty = False
            square.piece = Pawn('bp',"black", (1,j), self.board_arr)
            square.piece.set_coordinate(1,j)

        
        for j in range(self.rxc):   
            square = self.board_arr[6][j]
            square.is_empty = False
            square.piece = Pawn('wp',"white", (6,j), self.board_arr)
            square.piece.set_coordinate(6,j)
            
        
        for square in self.board_arr[7]: square.is_empty = False
        for square in self.board_arr[0]: square.is_empty = False

        self.board_arr[0][0].piece = Rook('bR', "black", (0,0), self.board_arr)
        self.board_arr[0][7].piece = Rook('bR', "black", (0,7), self.board_arr)
        self.board_arr[0][1].piece = Knight('bN', "black", (0,1), self.board_arr)
        self.board_arr[0][6].piece = Knight('bN', "black", (0,6), self.board_arr)
        self.board_arr[0][2].piece = Bishop('bB', "black", (0,2), self.board_arr)
        self.board_arr[0][5].piece = Bishop('bB', "black", (0,5), self.board_arr)
        self.board_arr[0][3].piece = Queen('bQ', "black", (0,3), self.board_arr)
        self.board_arr[0][4].piece = King('bK', "black", (0,4), self.board_arr)

        self.board_arr[7][0].piece = Rook('wR', "white", (7,0), self.board_arr)
        self.board_arr[7][7].piece = Rook('wR', "white", (7,7), self.board_arr)
        self.board_arr[7][1].piece = Knight('wN', "white", (7,1), self.board_arr)
        self.board_arr[7][6].piece = Knight('wN', "white", (7,6), self.board_arr)
        self.board_arr[7][2].piece = Bishop('wB', "white", (7,2), self.board_arr)
        self.board_arr[7][5].piece = Bishop('wB', "white", (7,5), self.board_arr)
        self.board_arr[7][3].piece = Queen('wQ', "white", (7,3), self.board_arr)
        self.board_arr[7][4].piece = King('wK', "white", (7,4), self.board_arr)

        self.availableBlackPieces = [(i,j) for j in range(8) for i in range(2)]

        self.availableWhitePieces = [(i,j) for j in range(8) for i in range(6,8)]

    def draw_king_check(self):
        pass    

    def draw_pieces(self):
        for row in range(self.rxc):
            for col in range(self.rxc):
                piece = self.board_arr[row][col].get_Piece()
                
                if piece == None: continue
                elif piece.name != '.':
                    self.screen.blit(self.Pieces[piece.name], pygame.Rect(col*self.squares, row*self.squares,
                                                      self.squares, self.squares))
    def undo_highlight(self, pos):
        r,c = pos[0],pos[1]
        color = self.colors[((r+c) % 2)]
        pygame.draw.rect(self.screen, color, (c*self.squares, r*self.squares, self.squares, self.squares), 3)
        pygame.display.flip()

    def GetColorClicked(self, row, col):
        
        p = self.board_arr[row][col]
        if p.is_empty:
            return "empty"
        else:
            return p.get_Piece_color()

    def get_pos(self, pos):
        x, y = pos
        row = y // self.squares
        col = x // self.squares
        return row, col  # get position of piece
    
    def highlight_square(self, pos:tuple):
        r,c = pos[0],pos[1]

        pygame.draw.rect(self.screen, self.GREEN, (c*self.squares, r*self.squares, self.squares, self.squares), 3)
        pygame.display.flip()

    def draw_moves(self, moves:list):
        for move in moves:

            pygame.draw.circle(self.screen, self.GREEN, ((move[1]*self.squares)+40, (move[0]*self.squares)+40), 15)
            
    def move_piece(self, old_pos:tuple, next_pos:tuple, piece_selected:Piece):
        piece_selected.set_coordinate(next_pos[0], next_pos[1])
        if not self.board_arr[next_pos[0]][next_pos[1]].is_empty:
            if self.color_to_move == "white":
                self.availableBlackPieces.remove(next_pos)
            else: self.availableWhitePieces.remove(next_pos)
            
        # you want to stop blitting on the current square
        # blit to the new square
        # old square is empty
        # new square is not empty
        self.board_arr[next_pos[0]][next_pos[1]].piece = self.board_arr[old_pos[0]][old_pos[1]].piece
        self.board_arr[old_pos[0]][old_pos[1]].is_empty = True
        self.board_arr[old_pos[0]][old_pos[1]].piece = None
        self.board_arr[next_pos[0]][next_pos[1]].is_empty = False
        self.board_arr[next_pos[0]][next_pos[1]].piece.set_coordinate(next_pos[0], next_pos[1])

        if self.color_to_move == "white":
            self.availableWhitePieces.remove(old_pos)
            self.availableWhitePieces.append(next_pos)
        else: 
            self.availableBlackPieces.remove(old_pos)
            self.availableBlackPieces.append(next_pos) # how to handle if a piece gets captured?

    def get_piece_clicked(self, row, col ):
        self.draw_board()
        piece_clicked = self.board_arr[row][col].get_Piece()
                        
        move_list = piece_clicked.get_legal_moves()
        self.clicks.append((row,col)) 
        self.highlight_square((row, col))
        self.draw_moves(move_list) 

    def undo_move_dots(self):
        for s in self.current_move_list:
            color = self.colors[((s[0]+s[1]) % 2)]
            pygame.draw.rect(self.screen, color, 
                                pygame.Rect(s[1]*self.squares, s[0]*self.squares, self.squares, self.squares))

    
    def redraw_piece(self, piece:Piece, old_pos:tuple):
        old_row,old_col = old_pos[0], old_pos[1]
        color = self.colors[((old_row+old_col) % 2)]

        pygame.draw.rect(self.screen, color, 
                                 pygame.Rect(old_col*self.squares, old_row*self.squares, self.squares, self.squares))

        self.screen.blit(self.Pieces[piece.name], pygame.Rect(piece.col*self.squares, piece.row*self.squares,
                                                      self.squares, self.squares))

        pygame.display.flip()

    def display_king_check(self, pos:tuple):
        r,c = pos[0],pos[1]

        pygame.draw.rect(self.screen, self.RED, (c*self.squares, r*self.squares, self.squares, self.squares), 3)

        text_font = pygame.font.SysFont("Arial", 30)
        text = text_font.render(f"{self.color_to_move} King in check!!", True, (0,0,0)) 
        self.screen.blit(text, (650, 400))

        pygame.display.flip()

    def determine_white_king_check(self, attackingPiece:Piece):
        moves = attackingPiece.get_legal_moves()
        # if king in moves, then king in check
        for move in moves:
            if type(self.board_arr[move[0]][move[1]].get_Piece()) == King:
                self.display_king_check(move)
        

    def DetermineKingCheck(self, attackingPiece:Piece):
        moves = attackingPiece.get_legal_moves()
        # if king in moves, then king in check
        for move in moves:
            if type(self.board_arr[move[0]][move[1]].get_Piece()) == King:
                self.display_king_check(move)
                return True
        return False
        
        

    def RUN(self):

        self.draw_board()
        
        self.import_pieces()
        self.set_pieces()
        # self.draw_pieces()



        while True:
            # game loop
            if self.checkmate: break
            self.draw_pieces()
            self.draw_player_turn() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # command that makes the game quit
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()                    
                    row,col = self.get_pos(mouse_pos)
                    
                    color_clicked = self.GetColorClicked(row,col)

                    #piece_clicked = self.board_arr[row][col].get_Piece()
                    
                    if len(self.clicks) == 0 and color_clicked == self.color_to_move:
                        
                        if self.color_to_move == "black" and self.BlackInCheck:
                            
                            
                            if (row,col) not in self.blackBlockingPieces:
                                continue # need to modify what piece clicked in blockingPieces look like

                            else:
                                piece_clicked = self.board_arr[row][col].get_Piece()
                            
                                move_list = piece_clicked.get_legal_moves()
                                self.current_move_list = move_list
                                self.clicks.append((row,col)) 
                                self.highlight_square((row, col))
                                self.draw_moves(move_list)
                        elif self.color_to_move == "white" and self.WhiteInCheck:
                            if (row,col) not in self.whiteBlockingPieces:
                                continue
                            else:
                                piece_clicked = self.board_arr[row][col].get_Piece()
                            
                                move_list = piece_clicked.get_legal_moves()
                                self.current_move_list = move_list
                                self.clicks.append((row,col)) 
                                self.highlight_square((row, col))
                                self.draw_moves(move_list)
                        else:
                            piece_clicked = self.board_arr[row][col].get_Piece()
                            
                            move_list = piece_clicked.get_legal_moves()
                            self.current_move_list = move_list
                            self.clicks.append((row,col)) 
                            self.highlight_square((row, col))
                            self.draw_moves(move_list)
                        
                        

                    elif len(self.clicks) == 1: # need to rewrite all of this, starting with a base case
                        # you have to determine if white or black in check first before you hit the control flow
                        
                        if self.color_to_move == "black" and self.BlackInCheck:
                            
                            if (row,col) not in self.blackBlockingPieces:
                                
                                continue 
                            elif (row,col) in self.blackBlockingPieces:
                                
                                if (row, col) in self.clicks: # if you clicked the same guy
                                    self.draw_board()
                                
                                else:
                                    
                                    #self.draw_board()
                                    self.undo_highlight((self.clicks[0]))
                                    self.undo_move_dots()
                                    self.clicks.clear()
                                    piece_clicked = self.board_arr[row][col].get_Piece()
                            
                                    move_list = piece_clicked.get_legal_moves()
                                    self.current_move_list = move_list
                                    self.clicks.append((row,col)) 
                                    self.highlight_square((row, col))
                                    self.draw_moves(move_list)
                                    self.undo_highlight(self.BlackKing)
                                    self.BlackInCheck = False
                                    print("reaches")
                            
                        elif self.color_to_move == "black" and not self.BlackInCheck:
                            if color_clicked == self.color_to_move:
                                self.undo_highlight(self.clicks[0]) # did you click the same piece or a new piece
                                if (row, col) in self.clicks: # if you clicked the same guy
                                    self.draw_board()
                                    
                                else:
                                    #self.draw_board()
                                    self.undo_move_dots()
                                    self.clicks.clear()
                                    piece_clicked = self.board_arr[row][col].get_Piece()
                            
                                    move_list = piece_clicked.get_legal_moves()
                                    self.current_move_list = move_list
                                    self.clicks.append((row,col)) 
                                    self.highlight_square((row, col))
                                    self.draw_moves(move_list)
                                    # highlight the new piece
                                    # draw the new moves
                            else:
                                # crashes when you try to select a new piece to move
                                self.move_piece(self.clicks[0], (row,col), piece_clicked)
                                self.undo_move_dots()
                                self.redraw_piece(piece_clicked, self.clicks[0])
                                check = self.DetermineKingCheck(piece_clicked)
                                if check:
                                    self.WhiteInCheck = True
                                    whiteKingCannotGetOutOfCheck = GetKingCannotGetOutOfCheck(piece_clicked, self.board_arr[self.WhiteKing[0]][self.WhiteKing[1]].get_Piece())
                                    if whiteKingCannotGetOutOfCheck:
                                        self.whiteBlockingPieces = createListOfBlockingPieces(piece_clicked, self.availableWhitePieces)
                                        if not self.whiteBlockingPieces: self.checkmate = True
                                self.clicks.clear()
                                self.color_to_move = get_opposite_color(self.color_to_move)
                                self.board_arr[row][col].color = piece_clicked.color
                                self.current_move_list.clear()

                        elif self.color_to_move == "white" and not self.WhiteInCheck:

                            if color_clicked == self.color_to_move:
                                self.undo_highlight(self.clicks[0]) # did you click the same piece or a new piece
                                if (row, col) in self.clicks: # if you clicked the same guy
                                    self.draw_board()
                                    
                                else:
                                    #self.draw_board()
                                    self.undo_move_dots()
                                    self.clicks.clear()
                                    piece_clicked = self.board_arr[row][col].get_Piece()
                            
                                    move_list = piece_clicked.get_legal_moves()
                                    self.current_move_list = move_list
                                    self.clicks.append((row,col)) 
                                    self.highlight_square((row, col))
                                    self.draw_moves(move_list)
                                    # highlight the new piece
                                    # draw the new moves
                            else:
                                self.move_piece(self.clicks[0], (row,col), piece_clicked)
                                self.undo_move_dots()
                                self.redraw_piece(piece_clicked, self.clicks[0])
                                self.clicks.clear()
                                check = self.DetermineKingCheck(piece_clicked)
                                if check:
                                    self.BlackInCheck = True
                                    blackKingCannotGetOutOfCheck = GetKingCannotGetOutOfCheck(piece_clicked, self.board_arr[self.BlackKing[0]][self.BlackKing[1]].get_Piece())
                                    if blackKingCannotGetOutOfCheck:
                                        self.blackBlockingPieces = createListOfBlockingPieces(piece_clicked, self.availableBlackPieces, self.board_arr)
                                        if not self.blackBlockingPieces: self.checkmate = True
                                self.color_to_move = get_opposite_color(self.color_to_move)
                                self.board_arr[row][col].color = piece_clicked.color
                                self.current_move_list.clear()

                        elif self.color_to_move == "white" and self.WhiteInCheck:
                            
                            
                            if (row,col) not in self.whiteBlockingPieces:
                                continue
                            elif (row,col) in self.whiteBlockingPieces:
                                if (row, col) in self.clicks: # if you clicked the same guy
                                    self.draw_board()
                                
                                else:
                                    #self.draw_board()
                                    self.undo_highlight((self.clicks[0]))
                                    self.undo_move_dots()
                                    self.clicks.clear()
                                    piece_clicked = self.board_arr[row][col].get_Piece()
                            
                                    move_list = piece_clicked.get_legal_moves()
                                    self.current_move_list = move_list
                                    self.clicks.append((row,col)) 
                                    self.highlight_square((row, col))
                                    self.draw_moves(move_list)
                                    self.undo_highlight(self.WhiteKing)
                                    self.WhiteInCheck = False

                        
                        

                    else: 
                        #print("continued")
                        continue
                        
                    
            
            clock.tick(60)  # clock running at 60 FPS
            pygame.display.flip()

if __name__ == "__main__":
    pass    