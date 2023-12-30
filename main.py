import pygame as pg
import engine
import game
from globals import *


pg.init()
size = w, h = 800, 600
half_size = hw, hh = w // 2, h // 2
win = pg.display.set_mode(size)
pg.display.set_caption('Pygame Project')
clk = pg.time.Clock()
Globals.anim_sprites = engine.sprites.AnimatedSpriteGroup()

tilemap_pos = (-200, -150)
tileset = engine.TileSet({
    ' ': 'data/map/empty.png',
    '#': 'data/map/wall.png',
    'C': 'data/objects/chest.png'
}, 32)
tilemap = engine.TileMap('maps/map.txt', tileset)
player = game.player.Player((10, 10), 4)
objects = engine.Objects('maps/map.txt', tilemap_pos, tileset, game.objects.object_map)
camera = engine.Camera(player, size)
camera.add_background(tilemap)
camera.add_sprite(objects)
camera.add_sprite(player)

Globals.font_small = pg.font.Font('data/font.ttf', 16)
Globals.font_big = pg.font.Font('data/font.ttf', 32)
Globals.player = player
Globals.world = tilemap
Globals.objects = objects
Globals.camera = camera

enemy = game.enemies.Enemy((0, 0))
camera.add_sprite(enemy)

ANIM_TICK = pg.USEREVENT + 1
pg.time.set_timer(ANIM_TICK, 100)

dbg_mode = False
running = True
while running:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            running = False
        elif ev.type == ANIM_TICK:
            Globals.anim_sprites.tick()
            enemy.enemy_tick()
        elif ev.type == pg.MOUSEBUTTONDOWN:
            objects.handle_click(camera.screen_to_world(ev.pos))
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_F1:
                dbg_mode = not dbg_mode
    Globals.sprites.update()
    Globals.anim_sprites.update()
    player.handle_input(pg.key.get_pressed())
    player.update()
    win.fill('black')
    camera.draw_ysort(win)
    Globals.sprites.draw(win)
    if dbg_mode:
        for s in camera.sprites():
            pg.draw.rect(win, 'red', camera.rect_world_to_screen(s.rect), 1)
            if hasattr(s, 'collider'):
                pg.draw.rect(win, 'green', camera.rect_world_to_screen(s.collider), 1)
        win.blit(Globals.font_small.render(f'FPS: {clk.get_fps():.2f}', True, 'white'), (10, 10))
    pg.display.update()
    clk.tick(60)
