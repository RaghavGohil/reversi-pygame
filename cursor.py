import pygame
import config

class Cursor:

    def __init__(self,window):
        self.window = window
        self.pos = (0,0) 
        self.cursor_image = pygame.image.load('./assets/images/reversi_cursor.png')

        self.my_chance = config.black_plays_first

    def __render(self,mouse_pos)->None:
        self.pos = (int(mouse_pos[0]/75)*75,(int(mouse_pos[1]/75)*75))
        self.window.blit(self.cursor_image,self.pos)

    def __place_piece(self,events,mouse_pos,pieces):
        x = int(mouse_pos[0]/75)
        y = int(mouse_pos[1]/75)
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if pieces.pieces[y][x] == 0:
                    if self.my_chance:
                        pieces.pieces[y][x] = 1
                    else:
                        pieces.pieces[y][x] = 2

    def update(self,events,mouse_pos,pieces)->None:
        self.__render(mouse_pos)
        self.__place_piece(events,mouse_pos,pieces)
