
import pygame
import sys
from Piece import *
from Square import Square


pygame.init()
clock = pygame.time.Clock()
class Board:

    def __init__(self):
        self.TAN = (255, 228, 181)  # RGB color combination
        self.BROWN = (139, 101, 8)
        self.rxc = 8  # dimensions of row and columns (9)
        self.height = 512  # dimensions of the board (constants)
        self.width = 800
        self.squares = 512//8  # size of our board squares
        self.colors = [pygame.Color(self.TAN), pygame.Color(self.BROWN)]
        self.rxc = 8
        self.colors = [pygame.Color(self.TAN), pygame.Color(self.BROWN)]
        self.PATH = r"C:\\Python\\WORTHY PROJECTS\\PyChess_Server\\chess_pieces\\"
        self.screen = pygame.display.set_mode((self.width, self.height))  # Setting the screen size
        self.screen.fill(pygame.Color((255, 228, 181)))  # intitally fills screen to be all tan color
        pygame.display.set_caption("PyChess")

        self.color_to_move = "white"
        self.Pieces = {}

        self.board_arr = [[Square(True, (y,x)) for x in range(self.rxc)] for y in range(self.rxc)]

        for square in self.board_arr[1]:
            for j in range(self.rxc):   
                square.is_empty = False
                square.piece = Pawn('bp',"black", (1,j), self.board_arr)
        for square in self.board_arr[6]:
            for j in range(self.rxc):   
                square.is_empty = False
                square.piece = Pawn('wp',"black", (6,j), self.board_arr)
        #self.board_arr[1] = [i.Piece = Pawn("bp", "black",(1, i), self.board_arr ) for i in range(self.rxc)]

    def import_pieces(self):        
        pieces = ['bB', 'bK', 'bN', 'bp', 'bQ', 'bR','wB', 'wK', 'wN', 'wp', 'wQ', 'wR']
        for piece in pieces:
            self.Pieces[piece] = pygame.transform.scale(pygame.image.load(
                self.PATH + piece + ".png"), (self.squares, self.squares))
            
    def draw_board(self):        
        for row in range(self.rxc):
            for col in range(self.rxc):
                color = self.colors[((row+col) % 2)]
                pygame.draw.rect(self.screen, color, pygame.Rect(
                    col*self.squares, row*self.squares, self.squares, self.squares))
        pygame.draw.line(self.screen, (0,0,0), (512, 0), (512,512), width=4)     

    def draw_player_turn(self):
        text_font = pygame.font.SysFont("Arial", 30)
        text = text_font.render("Player", True, (0,0,0)) 
        self.screen.blit(text, (600, 200))

    def draw_pieces(self):
        for row in range(self.rxc):
            for col in range(self.rxc):
                piece = self.board_arr[row][col].get_Piece()
                
                if piece == None: continue
                elif piece.name != '.':
                    self.screen.blit(self.Pieces[piece.name], pygame.Rect(col*self.squares, row*self.squares,
                                                       self.squares, self.squares))
    def RUN(self):

        self.draw_board()
        self.draw_player_turn()
        self.import_pieces()
        self.draw_pieces()


        while True:
            # game loop
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # command that makes the game quit
                    pygame.quit()
                    sys.exit()

            clock.tick(60)  # clock running at 60 FPS
            pygame.display.flip()

if __name__ == "__main__":
    pass