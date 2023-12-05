import pygame as pg
import engine

pg.init()
size = w, h = 800, 600
half_size = hw, hh = w // 2, h // 2
win = pg.display.set_mode(size)
clk = pg.time.Clock()
font = pg.font.SysFont('Arial', 12)
tileset = engine.TileSet({
    ' ': 'images/map/empty.png',
    '#': 'images/map/wall.png',
}, 32)
tilemap = engine.TileMap('maps/map.txt', tileset)
player = engine.Player((10, 10), 4)
camera = engine.Camera(player)
camera.add_background(tilemap)
camera.add(player)
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    player.handle_input(pg.key.get_pressed())
    win.fill('black')
    camera.draw_ysort(win)
    pg.display.update()
    clk.tick(60)
