import pygame as pg
from engine import sprites, map
from game.enemies import Enemy
from engine import utils
from globals import *


class Player(sprites.AnimatedSprite):
    def __init__(self, pos, speed):
        super().__init__((32, 64), 'idle')
        self.health = 100
        self.speed = speed
        self.damage = 25
        last_pos = ''
        self.killed = 0
        self.score = 0
        self.check_attack = False
        self.flag = False
        self.cool_down = 5
        self.add_animation('data/player/down1.png', 'down', (16, 32))
        self.add_animation('data/player/up1.png', 'up', (16, 32))
        self.add_animation('data/player/left1.png', 'left', (16, 32))
        self.add_animation('data/player/right1.png', 'right', (16, 32))
        self.add_animation('data/player/idle.png', 'idle', (16, 32))
        self.add_animation('data/player/attack1.png', 'attack', (16, 32))
        self.rect = self.image.get_rect(center=pos)
        self.collider = pg.Rect(self.rect)
        self.collider.size = (self.rect.width - 12, 2)
        self.collider.y += 48
        self.collider.x += 6
        self.collider_sprite = pg.sprite.Sprite()
        self.collider_sprite.rect = self.collider
        self.movement_bounds = (1000, 1000)

    def update(self):
        pass

    def get_health(self):
        return self.health

    def move(self, vector):
        self.rect.x += vector[0]
        self.collider.x += vector[0]
        if pg.sprite.spritecollideany(self.collider_sprite, Globals.objects)\
                or self.rect.x < 32 or self.rect.x + 64 > self.movement_bounds[0]:
            self.rect.x -= vector[0]
            self.collider.x -= vector[0]
        self.rect.y += vector[1]
        self.collider.y += vector[1]
        if pg.sprite.spritecollideany(self.collider_sprite, Globals.objects)\
                or self.rect.y < 32 or self.rect.y + 96 > self.movement_bounds[1]:
            self.rect.y -= vector[1]
            self.collider.y -= vector[1]

    def cooldown(self):
        if self.cool_down >= 4:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1

    def handle_input(self, keys):
        self.flag = False
        self.cooldown()
        if keys[pg.K_w]:
            self.move((0, -self.speed))
            self.state = 'up'
            self.last_pos = 'up'
        elif keys[pg.K_s]:
            self.move((0, self.speed))
            self.state = 'down'
            self.last_pos = 'down'
        if keys[pg.K_a]:
            self.move((-self.speed, 0))
            self.state = 'left'
            self.last_pos = 'left'
        elif keys[pg.K_d]:
            self.move((self.speed, 0))
            self.state = 'right'
            self.last_pos = 'right'
        elif not keys[pg.K_w] and not keys[pg.K_s]:
            self.state = 'idle'
        if keys[pg.K_SPACE] and self.cool_down == 0:
            self.cool_down = 1
            self.flag = True

    def attack(self):
        return self.flag

    def print_text(self, message, x, y, screen, font_color=(0, 0, 0), type='font.ttf', font_size=30):
        font_type = pg.font.Font(type, font_size)
        text = font_type.render(message, True, font_color)
        screen.blit(text, (x, y))