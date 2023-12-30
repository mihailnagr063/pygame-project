import pygame as pg
from globals import *


class Popup(pg.sprite.Sprite):
    def __init__(self, pos, text):
        super().__init__(Globals.sprites)
        self.image = Globals.font_big.render(text, False, 'white')
        self.rect = self.image.get_rect(center=pos)
        self.frames_passed = 0

    def update(self):
        self.frames_passed += 1
        self.rect.y -= 0.1
        if self.frames_passed > 120:
            self.kill()
