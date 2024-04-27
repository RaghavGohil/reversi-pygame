import config
import pygame

class Pieces:
    def __init__(self,window:pygame.Surface):

        self.window = window

        self.image_black_piece = pygame.image.load('./assets/images/reversi_black_piece.png').convert_alpha()
        self.image_white_piece = pygame.image.load('./assets/images/reversi_white_piece.png').convert_alpha()

        self.pieces = [[0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,2,1,0,0,0],
                       [0,0,0,1,2,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0],
                       [0,0,0,0,0,0,0,0]] #free space = 0, black = 1, white = 2

    def __render(self)->None:
        for y in range(8):
            for x in range(8):
                if self.pieces[y][x] == 1:
                    self.window.blit(self.image_black_piece,(x*config.cell_size,y*config.cell_size))
                elif self.pieces[y][x] == 2:
                    self.window.blit(self.image_white_piece,(x*config.cell_size,y*config.cell_size))

    def update(self)->None:
        self.__render()

