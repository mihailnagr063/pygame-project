import pygame as pg
from engine import sprites


class Player(sprites.AnimatedSprite):
    def __init__(self, pos, speed):
        super().__init__(32, 'idle')
        self.speed = speed
        self.add_animation('data/player', r'player1.png', 'idle')
        self.add_animation('data/player', r'player.\.png', 'walk')
        self.rect = self.image.get_rect(center=pos)

    def update(self):
        pass

    def move(self, vector):
        self.rect.move_ip(vector)

    def handle_input(self, keys):
        if keys[pg.K_w]:
            self.move((0, -self.speed))
        elif keys[pg.K_s]:
            self.move((0, self.speed))
        if keys[pg.K_a]:
            self.move((-self.speed, 0))
        elif keys[pg.K_d]:
            self.move((self.speed, 0))
        if keys[pg.K_w] or keys[pg.K_s] or keys[pg.K_a] or keys[pg.K_d]:
            self.state = 'walk'
        else:
            self.state = 'idle'
