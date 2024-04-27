import config
import pygame

class Board:
    def __init__(self,window:pygame.Surface):

        self.window = window
        self.image_board = pygame.image.load('./assets/images/reversi_board.png')

    def __render(self)->None:
        self.window.blit(self.image_board,(0,0))

    def update(self)->None:
        self.__render()

