import pygame as pg
from engine import sprites, utils
from globals import *


class Enemy(sprites.AnimatedSprite):
    speed: int
    damage: int
    health: int
    reload: int

    def __init__(self, pos):
        super().__init__((32, 64), 'walk')
        self.speed = 4
        self.rect = self.image.get_rect(center=pos)
        self.direction = pg.Vector2(0, 0)
        self.add_animation('data/player/down.png', 'walk', (16, 32))
        self.collider = pg.Rect(self.rect)
        self.collider.size = (self.rect.width - 12, 8)
        self.collider.y += 24
        self.collider.x += 6
        self.collider_sprite = pg.sprite.Sprite()
        self.collider_sprite.rect = self.collider
        self.reloading_status = 0
        self.is_reloading = False
        Globals.enemies.append(self)

    def update(self):
        self.rect.x += self.direction.x
        self.collider_sprite.rect.x += self.direction.x
        if pg.sprite.spritecollideany(self.collider_sprite, Globals.objects):
            self.rect.x -= self.direction.x
            self.collider_sprite.rect.x -= self.direction.x
        self.rect.y += self.direction.y
        self.collider_sprite.rect.y += self.direction.y
        if pg.sprite.spritecollideany(self.collider_sprite, Globals.objects):
            self.rect.y -= self.direction.y
            self.collider_sprite.rect.y -= self.direction.y

    def enemy_tick(self):
        if self.is_reloading:
            self.reloading_status += 1
            if self.reloading_status > self.reload:
                self.is_reloading = False
        dist = utils.distance(pg.Vector2(self.rect.center), pg.Vector2(Globals.player.rect.center))
        if 250 > dist > 32:
            self.direction = (pg.Vector2(Globals.player.rect.center) -
                              pg.Vector2(self.rect.center)).normalize() * self.speed
            self.direction.x = round(self.direction.x)
            self.direction.y = round(self.direction.y)
        else:
            self.direction = pg.Vector2(0, 0)
        self.attack(dist)

    def start_reloading(self):
        self.is_reloading = True
        self.reloading_status = 0

    def attack(self, dist):
        pass
