import pygame

import config
from board import Board

def main():
    
    #pygame config
    pygame.init()
    window = pygame.display.set_mode(config.window_size)
    pygame.display.set_caption(config.title)

    #game objects
    board = Board(window) 

    #game loop
    while True:

        events = pygame.event.get()

        for e in events:
            if e.type == pygame.QUIT:
                pygame.quit()
                quit()

        #draw
        board.update()
        #update
        pygame.display.flip()

if __name__ == '__main__':
    main()
