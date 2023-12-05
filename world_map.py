import pygame
from settings import *
from tile import Tile

class Map():
    def __init__(self):
        self.display = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        self.creat_map()

    def creat_map(self):
        for row_index, row in enumerate(WOLD_MAP):
            for elem_index, elem in enumerate(row):
                x = row_index * 64
                y = elem_index * 64
                if elem == 'x':
                    Tile((x, y), self.visible_sprites)
                elif elem == '.':
                    pass

    def run(self):
        self.visible_sprites.draw(self.display)