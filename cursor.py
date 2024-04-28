import pygame
from pygame import mixer
import config
from move import Move

class Cursor:

    def __init__(self,window):
        mixer.init()
        mixer.music.load('./assets/audio/coin.wav')
        self.window = window
        self.pos = (0,0) 
        self.cursor_green_image = pygame.image.load('./assets/images/reversi_cursor_green.png')
        self.cursor_red_image = pygame.image.load('./assets/images/reversi_cursor_red.png')

        self.move = Move()
        self.is_valid = False
        self.sequences = [] 

    def __render(self,mouse_pos,pieces)->None:
        self.pos = (int(mouse_pos[0]/75)*75,(int(mouse_pos[1]/75)*75))
        self.is_valid, self.sequences =  self.move.check_current_move_validity(int(self.pos[0]/75),int(self.pos[1]/75),pieces)

        if self.is_valid:
            self.window.blit(self.cursor_green_image,self.pos)
        else:
            self.window.blit(self.cursor_red_image,self.pos)
        print(self.sequences)

    def __flip_coins(self,pieces):
        mixer.music.play()
        for seq in self.sequences:
            mixer.music.play()
            if self.move.current_chance_is_black:
                pieces.pieces[seq[1]][seq[0]] = 1
            else:
                pieces.pieces[seq[1]][seq[0]] = 2

    def __place_piece(self,events,mouse_pos,pieces)->None:
        x = int(self.pos[0]/75)
        y = int(self.pos[1]/75)
        if not self.move.can_move(pieces):
            self.move.current_chance_is_black = not self.move.current_chance_is_black 
            return
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if self.is_valid:
                    if self.move.current_chance_is_black:
                        pieces.pieces[y][x] = 1
                    else:
                        pieces.pieces[y][x] = 2
                    self.__flip_coins(pieces)
                    self.move.current_chance_is_black = not self.move.current_chance_is_black 

    def update(self,events,mouse_pos,pieces)->None:
        self.__render(mouse_pos,pieces)
        self.__place_piece(events,mouse_pos,pieces)
