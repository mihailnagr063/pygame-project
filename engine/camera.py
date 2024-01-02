import pygame as pg


class Camera(pg.sprite.Group):
    def __init__(self, target, screen_size):
        super().__init__()
        self.offset = pg.Vector2(300, 100)
        self.target = target
        self.sw, self.sh = screen_size
        self.hw, self.hh = self.sw // 2, self.sh // 2
        self.background = []

    def center_at(self, target):
        self.offset.x = self.hw - target.rect.centerx
        self.offset.y = self.hh - target.rect.centery

    def add_background(self, *sprites):
        self.background.extend(sprites)

    def add_sprite(self, sprites):
        self.add(sprites)

    def resort(self):
        self.sprites().sort(key=lambda x: x.rect.centery)

    def draw_ysort(self, surface):
        self.center_at(self.target)
        for bg in self.background:
            surface.blit(bg.image, bg.rect.topleft + self.offset)
        for sprite in self.sprites():
            surface.blit(sprite.image, sprite.rect.topleft + self.offset)

    def blit(self, surface, image, rect):
        surface.blit(image, rect.topleft + self.offset)

    def screen_to_world(self, pos):
        return pos - self.offset

    def world_to_screen(self, pos):
        return pos + self.offset

    def rect_world_to_screen(self, rect):
        return rect.move(self.offset)
