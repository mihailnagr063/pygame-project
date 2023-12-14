import pygame as pg
import engine

pg.init()
size = w, h = 800, 600
half_size = hw, hh = w // 2, h // 2
win = pg.display.set_mode(size)
clk = pg.time.Clock()
font = pg.font.SysFont('Arial', 12)

tileset = engine.TileSet({
    ' ': 'data/map/empty.png',
    '#': 'data/map/wall.png',
}, 32)
tilemap = engine.TileMap('maps/map.txt', tileset)
player = engine.Player((10, 10), 4)
camera = engine.Camera(player, size)
camera.add_background(tilemap)
camera.add(player)

ANIM_TICK = pg.USEREVENT + 1
pg.time.set_timer(ANIM_TICK, 100)

running = True
while running:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            running = False
        elif ev.type == ANIM_TICK:
            player.tick()
    player.handle_input(pg.key.get_pressed())
    player.update()
    win.fill('black')
    camera.draw_ysort(win)
    pg.display.update()
    clk.tick(60)
