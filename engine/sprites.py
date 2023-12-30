import os
import re
import pygame as pg
from globals import *


class AnimatedSprite(pg.sprite.Sprite):
    def __init__(self, size, state):
        super().__init__(Globals.anim_sprites)
        self.state = state
        self.size = size
        self.image = pg.Surface((size, size))
        self.rect = self.image.get_rect()
        self.progress = 0
        self.animations = {}

    def add_animation(self, folder, start, name):
        self.animations[name] = []
        for file in sorted(os.listdir(folder)):
            if file.startswith(start):
                self.animations[name].append(pg.transform.scale(
                    pg.image.load(os.path.join(folder, file)).convert_alpha(), (self.size, self.size))
                )

    def tick(self):
        self.progress = (self.progress + 1) % len(self.animations[self.state])
        self.image = self.animations[self.state][self.progress]


class AnimatedSpriteGroup(pg.sprite.Group):
    def __init__(self):
        super().__init__()

    def tick(self):
        for sprite in self.sprites():
            sprite.tick()
