import pygame
import config

class Cursor:

    def __init__(self,window):
        self.window = window
        self.pos = (0,0) 
        self.cursor_green_image = pygame.image.load('./assets/images/reversi_cursor_green.png')
        self.cursor_red_image = pygame.image.load('./assets/images/reversi_cursor_red.png')

        self.my_chance = config.black_plays_first #my chance = black
        self.is_current_move_legal = False

    def __render(self,mouse_pos)->None:
        self.pos = (int(mouse_pos[0]/75)*75,(int(mouse_pos[1]/75)*75))

        if self.is_current_move_legal:
            self.window.blit(self.cursor_green_image,self.pos)
        else:
            self.window.blit(self.cursor_red_image,self.pos)

    def __check_legal_move(self,pieces)->bool: #determine if the move you are making is legal or not
        cursor_x_cell = int(self.pos[0]/75)
        cursor_y_cell = int(self.pos[1]/75)

        if pieces.pieces[cursor_y_cell][cursor_x_cell] != 0: #if no free space
            return False,[]

        for y in range(8):
            for x in range(8):
                if (x == y or x == cursor_x_cell or y == cursor_y_cell or x+y == 8) and (x != cursor_x_cell and y != cursor_y_cell):
                    if self.my_chance and pieces.pieces[y][x] == 1:
                        return True
                    elif not self.my_chance and pieces.pieces[y][x] == 2:
                        return True
        return False,[]


    def __place_piece(self,events,mouse_pos,pieces)->None:
        x = int(self.pos[0]/75)
        y = int(self.pos[1]/75)
        for e in events:
            if e.type == pygame.MOUSEBUTTONDOWN:
                if not self.is_current_move_legal:
                    return
                if self.my_chance:
                    pieces.pieces[y][x] = 1
                else:
                    pieces.pieces[y][x] = 2

    def update(self,events,mouse_pos,pieces)->None:
        if self.__check_legal_move(pieces):
            self.is_current_move_legal = True
        else:
            self.is_current_move_legal = False

        self.__render(mouse_pos)
        self.__place_piece(events,mouse_pos,pieces)
