
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
        self.rxc = 8  # dimensions of row and columns (9)
        self.height = 512  # dimensions of the board (constants)
        self.width = 800
        self.squares = 512//8  # size of our board squares
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
        pygame.draw.line(self.screen, (0,0,0), (512, 0), (512,512), width=4)     

    def draw_player_turn(self):
        pygame.draw.rect(self.screen, self.TAN, pygame.Rect((512, 0, self.width-512, self.height )))
        text_font = pygame.font.SysFont("Arial", 30)
        text = text_font.render(f"{self.color_to_move} to play", True, (0,0,0)) 
        self.screen.blit(text, (600, 200))
        
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
        self.board_arr[0][4].piece = Queen('bK', "black", (0,4), self.board_arr)

        self.board_arr[7][0].piece = Rook('wR', "white", (7,0), self.board_arr)
        self.board_arr[7][7].piece = Rook('wR', "white", (7,7), self.board_arr)
        self.board_arr[7][1].piece = Knight('wN', "white", (7,1), self.board_arr)
        self.board_arr[7][6].piece = Knight('wN', "white", (7,6), self.board_arr)
        self.board_arr[7][2].piece = Bishop('wB', "white", (7,2), self.board_arr)
        self.board_arr[7][5].piece = Bishop('wB', "white", (7,5), self.board_arr)
        self.board_arr[7][3].piece = Queen('wQ', "white", (7,3), self.board_arr)
        self.board_arr[7][4].piece = Queen('wK', "white", (7,4), self.board_arr)
    

        

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

    def what_was_clicked(self, row, col):
        
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

            pygame.draw.circle(self.screen, self.GREEN, ((move[1]*64)+32, (move[0]*64)+32), 10)
            
    def move_piece(self, old_pos:tuple, next_pos:tuple, piece_selected:Piece):
        piece_selected.set_coordinate(next_pos[0], next_pos[1])
        # you want to stop blitting on the current square
        # blit to the new square
        # old square is empty
        # new square is not empty
        self.board_arr[next_pos[0]][next_pos[1]].piece = self.board_arr[old_pos[0]][old_pos[1]].piece
        self.board_arr[old_pos[0]][old_pos[1]].is_empty = True
        self.board_arr[old_pos[0]][old_pos[1]].piece = None
        self.board_arr[next_pos[0]][next_pos[1]].is_empty = False
        self.board_arr[next_pos[0]][next_pos[1]].piece.set_coordinate(next_pos[0], next_pos[1])

    def get_piece_clicked(self, row, col ):
        self.draw_board()
        piece_clicked = self.board_arr[row][col].get_Piece()
                        
        move_list = piece_clicked.get_legal_moves()
        self.clicks.append((row,col)) 
        self.highlight_square((row, col))
        self.draw_moves(move_list) 
    
                        
    def RUN(self):

        self.draw_board()
        
        self.import_pieces()
        self.set_pieces()
        # self.draw_pieces()



        while True:
            # game loop
            self.draw_pieces()
            self.draw_player_turn() 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # command that makes the game quit
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()                    
                    row,col = self.get_pos(mouse_pos)
                    
                    color_clicked = self.what_was_clicked(row,col)


                    if len(self.clicks)==0 and color_clicked == self.color_to_move:
                        
                        piece_clicked = self.board_arr[row][col].get_Piece()
                        
                        move_list = piece_clicked.get_legal_moves()
                        self.clicks.append((row,col)) 
                        self.highlight_square((row, col))
                        self.draw_moves(move_list)
                        
                        

                    elif len(self.clicks) == 1:

                        if color_clicked == self.color_to_move:
                            self.undo_highlight(self.clicks[0]) # did you click the same piece or a new piece
                            if (row, col) in self.clicks: # if you clicked the same guy
                                self.draw_board()

                            else:
                                self.draw_board()
                                self.clicks.clear()
                                piece_clicked = self.board_arr[row][col].get_Piece()
                        
                                move_list = piece_clicked.get_legal_moves()
                                self.clicks.append((row,col)) 
                                self.highlight_square((row, col))
                                self.draw_moves(move_list)
                                # highlight the new piece
                                # draw the new moves
                        elif (row,col) in move_list:
                            
                            self.move_piece(self.clicks[0], (row,col), piece_clicked)
                            self.draw_board()
                            self.clicks.clear()
                            self.color_to_move = get_opposite_color(self.color_to_move)
                            self.board_arr[row][col].color = piece_clicked.color

                    else: continue
                    

            clock.tick(60)  # clock running at 60 FPS
            pygame.display.flip()

if __name__ == "__main__":
    pass