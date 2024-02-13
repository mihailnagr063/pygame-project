import pygame as pg
import pytmx
import engine
import game
from globals import *

pg.init()
pg.mixer.init()
size = w, h = 1280, 720
half_size = hw, hh = w // 2, h // 2
win = pg.display.set_mode(size)
pg.display.set_caption('Pygame Project')
clk = pg.time.Clock()

lbl = engine.gui.Label((0, 0), 48, 'loading...', pg.sprite.Group())
lbl.rect.bottomleft = (16, h - 16)
win.blit(lbl.image, lbl.rect)
pg.display.update()
del lbl

Globals.anim_sprites = engine.sprites.AnimatedSpriteGroup()

pg.mixer.music.load('music/start_screen.mp3')
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.1)

tiled_map = pytmx.load_pygame('data/map.tmx')

tilemap = engine.TileMap(tiled_map, 32)
player = game.player.Player((0, 0), 4)
objects = engine.Objects(tiled_map, game.objects.object_map)
camera = engine.Camera(player, size)
camera.add_background(tilemap)
camera.add_sprite(objects)
camera.add_sprite(player)

Globals.font_small = pg.font.Font(Globals.font_path, 16)
Globals.font_big = pg.font.Font(Globals.font_path, 32)
Globals.player = player
Globals.world = tilemap
Globals.objects = objects
Globals.camera = camera
player.movement_bounds = (tilemap.image.get_width(), tilemap.image.get_height())

layer: pytmx.TiledObjectGroup = [l for l in tiled_map.layers if l.name == 'objects'][0]
for obj in layer:
    obj: pytmx.TiledObject
    if obj.name == 'player':
        player.rect.center = (obj.x * 2, obj.y * 2)
        player.collider.move_ip(obj.x * 2, obj.y * 2)
    elif obj.type == 'enemy':
        camera.add(game.enemies.Enemy((obj.x * 2, obj.y * 2)))

health_bar = engine.gui.ProgressBar((10, 10), (128, 24), group=Globals.sprites, watch_func=player.get_health)
if not game.screens.start_screen(win, clk):
    pg.quit()
    exit()

ANIM_TICK = pg.USEREVENT + 1
pg.time.set_timer(ANIM_TICK, 100)

dbg_mode = False
running = True
pg.mixer.music.stop()
while running:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            running = False
        elif ev.type == ANIM_TICK:
            Globals.anim_sprites.tick()
            for en in Globals.enemies:
                en.enemy_tick()
        elif ev.type == pg.MOUSEBUTTONDOWN:
            objects.handle_click(camera.screen_to_world(ev.pos))
        elif ev.type == pg.KEYDOWN:
            if ev.key == pg.K_F1:
                dbg_mode = not dbg_mode
            elif ev.key == pg.K_ESCAPE:
                if not game.pause_screen(win, clk):
                    running = False
            elif ev.key == pg.K_p:
                game.screens.gameover_screen(win, clk)
                running = False
    Globals.sprites.update()
    Globals.anim_sprites.update()
    player.handle_input(pg.key.get_pressed())
    if player.health <= 0:
        game.screens.gameover_screen(win, clk)
        running = False
    win.fill((58, 190, 65))
    camera.draw_ysort(win)
    Globals.sprites.draw(win)
    Globals.player.print_text(f'score: {Globals.player.health + Globals.player.score}', 10, 40, win)
    if dbg_mode:
        for s in camera.sprites():
            pg.draw.rect(win, 'red', camera.rect_world_to_screen(s.rect), 1)
            if hasattr(s, 'collider'):
                pg.draw.rect(win, 'green', camera.rect_world_to_screen(s.collider), 1)
        win.blit(Globals.font_small.render(f'FPS: {clk.get_fps():.2f}', True, 'white'), (10, 10))
    pg.display.update()
    clk.tick(60)

pg.quit()
