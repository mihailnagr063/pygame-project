import pygame as pg


class Player(pg.sprite.Sprite):
    def __init__(self, pos, speed):
        super().__init__()
        self.speed = speed
        self.image = pg.transform.scale(pg.image.load('images/player.png').convert_alpha(), (32, 32))
        self.rect = self.image.get_rect(center=pos)

    def handle_input(self, keys):
        if keys[pg.K_w]:
            self.rect.y -= self.speed
        elif keys[pg.K_s]:
            self.rect.y += self.speed
        if keys[pg.K_a]:
            self.rect.x -= self.speed
        elif keys[pg.K_d]:
            self.rect.x += self.speed
