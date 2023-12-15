import pygame as pg


class Camera(pg.sprite.Group):
    def __init__(self, target, screen_size):
        super().__init__()
        self.offset = pg.Vector2(300, 100)
        self.target = target
        self.sw, self.sh = screen_size
        self.hw, self.hh = self.sw // 2, self.sh // 2
        self.background = []
        self.no_ysort = pg.sprite.Group()

    def add_noysort(self, group):
        self.no_ysort.add(group)

    def center_at(self, target):
        self.offset.x = self.hw - target.rect.centerx
        self.offset.y = self.hh - target.rect.centery

    def add_background(self, *sprites):
        self.background.extend(sprites)

    def draw_ysort(self, surface):
        self.center_at(self.target)
        for bg in self.background:
            surface.blit(bg.image, bg.rect.topleft + self.offset)
        for sprite in self.no_ysort:
            surface.blit(sprite.image, sprite.rect.topleft + self.offset)
        for sprite in sorted(self.sprites(), key=lambda x: x.rect.centery):
            surface.blit(sprite.image, sprite.rect.topleft + self.offset)

    def blit(self, surface, image, rect):
        surface.blit(image, rect.topleft + self.offset)
