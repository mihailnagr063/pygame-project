import pygame as pg
import engine
import globals


def start_screen(win: pg.Surface, clk: pg.time.Clock):
    size = w, h = win.get_size()
    ui = pg.sprite.Group()
    start_btn = engine.gui.Button((w // 2, h // 2), 200, 'Начать игру', ui, 'play')
    exit_btn = engine.gui.Button((w // 2, h // 2 + 50), 200, 'Выйти', ui, 'exit')
    engine.gui.Label((w // 2, h // 2 - 100), 96, 'zelda', ui)
    running = True
    while running:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                return False
            elif ev.type == pg.MOUSEBUTTONDOWN:
                if start_btn.rect.collidepoint(ev.pos):
                    return True
                elif exit_btn.rect.collidepoint(ev.pos):
                    return False
            ui.update(ev)
        win.fill('#2e222f')
        ui.draw(win)
        pg.display.update()
        clk.tick(60)


def pause_screen(win: pg.Surface, clk: pg.time.Clock):
    size = w, h = win.get_size()
    ui = pg.sprite.Group()
    dark_bg = win.copy()
    dark_bg.fill((96, 96, 96), special_flags=pg.BLEND_MULT)
    engine.gui.Label((w // 2, h // 2 - 100), 96, 'пауза', ui)
    resume_btn = engine.gui.Button((w // 2, h // 2), 200, 'Продолжить', ui, 'play')
    exit_btn = engine.gui.Button((w // 2, h // 2 + 50), 200, 'Выйти', ui, 'exit')
    running = True
    while running:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                return False
            elif ev.type == pg.MOUSEBUTTONDOWN:
                if resume_btn.rect.collidepoint(ev.pos):
                    return True
                elif exit_btn.rect.collidepoint(ev.pos):
                    return False
            elif ev.type == pg.KEYDOWN:
                if ev.key == pg.K_ESCAPE:
                    return True
            ui.update(ev)
        win.blit(dark_bg, (0, 0))
        ui.draw(win)
        pg.display.update()
        clk.tick(60)
    del ui


def gameover_screen(win: pg.Surface, clk: pg.time.Clock):
    size = w, h = win.get_size()
    ui = pg.sprite.Group()
    dark_bg = win.copy()
    dark_bg.fill((96, 96, 96), special_flags=pg.BLEND_MULT)
    engine.gui.Label((w // 2, h // 2 - 100), 96, 'вы проиграли', ui)
    exit_btn = engine.gui.Button((w // 2, h // 2 + 50), 200, 'Выйти', ui, 'exit')
    running = True
    while running:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                return
            elif ev.type == pg.MOUSEBUTTONDOWN:
                if exit_btn.rect.collidepoint(ev.pos):
                    return
            ui.update(ev)
        win.blit(dark_bg, (0, 0))
        ui.draw(win)
        pg.display.update()
        clk.tick(60)

def winer_screen(win: pg.Surface, clk: pg.time.Clock):
    size = w, h = win.get_size()
    ui = pg.sprite.Group()
    dark_bg = win.copy()
    dark_bg.fill((96, 96, 96), special_flags=pg.BLEND_MULT)
    engine.gui.Label((w // 2, h // 2 - 100), 96, 'Вы победили', ui)
    engine.gui.Label((w // 2, h // 2 - 30), 96, f'Вы набрали {globals.Globals.player.score + globals.Globals.player.health}', ui)
    exit_btn = engine.gui.Button((w // 2, h // 2 + 50), 200, 'Выйти', ui, 'exit')
    running = True
    while running:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                return
            elif ev.type == pg.MOUSEBUTTONDOWN:
                if exit_btn.rect.collidepoint(ev.pos):
                    return
            ui.update(ev)
        win.blit(dark_bg, (0, 0))
        ui.draw(win)
        pg.display.update()
        clk.tick(60)