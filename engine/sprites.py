import os
import re
import pygame as pg
from globals import *


class AnimatedSprite(pg.sprite.Sprite):
    def __init__(self, size, state):
        super().__init__(Globals.anim_sprites)
        self.state = state
        self.size = size
        self.image = pg.Surface(size)
        self.rect = self.image.get_rect()
        self.progress = 0
        self.animations = {}

    def add_animation(self, sheet, name, size):
        self.animations[name] = []
        sheet = pg.image.load(sheet).convert_alpha()
        for y in range(sheet.get_height() // size[1]):
            for x in range(sheet.get_width() // size[0]):
                self.animations[name].append(
                    pg.transform.scale(sheet.subsurface((x * size[0], y * size[1], size[0], size[1])), self.size))

    def tick(self):
        try:
            self.progress = (self.progress + 1) % len(self.animations[self.state])
            self.image = self.animations[self.state][self.progress]
        except:
            pass


class AnimatedSpriteGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()

    def tick(self):
        for sprite in self.sprites():
            sprite.tick()
