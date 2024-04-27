import pygame

class Board:
    def __init__(self,window:pygame.Surface):
        self.size = 600*600
        self.image = pygame.image.load('./assets/images/reversi_board.png')
        self.window = window
    
    def update(self)->None:
        self.window.blit(self.image,(0,0))

