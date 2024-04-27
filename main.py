import pygame

import config
from board import Board
from pieces import Pieces 
from cursor import Cursor 

def main():
    
    #pygame config
    pygame.init()
    window = pygame.display.set_mode(config.window_size)
    pygame.display.set_caption(config.title)

    #game objects
    board = Board(window) 
    cursor = Cursor(window) 
    pieces = Pieces(window)

    #game loop
    while True:

        events = pygame.event.get()
        mouse_pos = pygame.mouse.get_pos()

        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

        #draw
        board.update()
        cursor.update(events,mouse_pos,pieces)
        pieces.update()
        #update
        pygame.display.flip()

if __name__ == '__main__':
    main()
