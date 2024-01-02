import pygame as pg


class Globals:
    sprites = pg.sprite.Group()
    anim_sprites: None
    enemies = []
    font_path = 'data/font.ttf'
    font_small: pg.Font
    font_big: pg.Font
    player: None
    world: None
    objects: None
    camera: None
