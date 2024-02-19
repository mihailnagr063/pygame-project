import pygame as pg
from random import choice
import game
from engine import sprites, utils
from globals import *


class Enemy(sprites.AnimatedSprite):
    speed: int
    damage: int
    health: int
    reload: int

    def __init__(self, pos):
        super().__init__((32, 32), f'anim')
        self.speed = 4
        self.hp = 50
        self.damage = 10
        self.cool_down = 5
        self.time_check = 0
        self.rect = self.image.get_rect(center=pos)
        self.direction = pg.Vector2(0, 0)
        anim_path = f'data/enemies/{choice(["lynel", "lynel2", "moblin2", "octorok-red", "moblin", "octorok"])}.png'
        self.add_animation(anim_path, 'anim', (16, 16))
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

    def cooldown(self):
        if self.cool_down >= 15:
            self.cool_down = 0
        elif self.cool_down > 0:
            self.cool_down += 1

    def check_enemy(self):
        delyte = []
        for i in range(len(Globals.enemies)):
            if '2' not in f'{Globals.enemies[i]}':
                delyte.append(i)
        [Globals.enemies.pop(n) for n in delyte]
        Globals.player.score += (len(delyte)) * 10
        Globals.player.killed += (len(delyte))

    def enemy_update_pos(self):
        last = Globals.player.last_pos
        if last == 'up':
            self.direction.y -= 8
        elif last == 'down':
            self.direction.y += 8
        elif last == 'right':
            self.direction.x += 8
        elif last == 'left':
            self.direction.x += 8

    def attack(self, dist):
        self.check_enemy()
        self.cooldown()
        if dist <= 32 and self.cool_down == 0:
            Globals.player.health -= self.damage
            self.cool_down = 1
        if dist <= 64 and Globals.player.attack():
            if self.hp - Globals.player.damage == 0 and Globals.player.health < 100:
                if Globals.player.health + 10 > 100:
                    Globals.player.health = 100
                else:
                    Globals.player.health += 10
            self.hp -= Globals.player.damage
            self.enemy_update_pos()
        elif Globals.player.attack():
            Globals.player.score -= 2
        if self.hp <= 0:
            self.kill()
