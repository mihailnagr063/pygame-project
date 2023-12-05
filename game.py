import pygame
import sys
from settings import *
from world_map import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Map()

    def run(self):
        self.level.creat_map()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.level.run()
            pygame.display.update()
            self.clock.tick(60)



if __name__ == '__main__':
    game = Game()
    game.run()