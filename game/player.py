import pygame as pg
from engine import sprites, map


class Player(sprites.AnimatedSprite):
    def __init__(self, pos, speed, objects: map.Objects):
        super().__init__(32, 'idle')
        self.speed = speed
        self.add_animation('data/player', r'player1.png', 'idle')
        self.add_animation('data/player', r'player.\.png', 'walk')
        self.rect = self.image.get_rect(center=pos)
        self.objects = objects
        self.collider = pg.Rect(self.rect)
        self.collider.size = (self.rect.width - 12, 2)
        self.collider.y += 30
        self.collider.x += 6
        self.collider_sprite = pg.sprite.Sprite()
        self.collider_sprite.rect = self.collider

    def update(self):
        pass

    def move(self, vector):
        self.rect.x += vector[0]
        self.collider.x += vector[0]
        if self.objects.is_colliding(self.collider):
            self.rect.x -= vector[0]
            self.collider.x -= vector[0]
        self.rect.y += vector[1]
        self.collider.y += vector[1]
        if self.objects.is_colliding(self.collider):
            self.rect.y -= vector[1]
            self.collider.y -= vector[1]

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
