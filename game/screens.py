import pygame as pg
import engine
import globals


def start_screen(win: pg.Surface, clk: pg.time.Clock):
    size = w, h = win.get_size()
    ui = pg.sprite.Group()
    start_btn = engine.gui.Button((w // 2, h // 2), 200, 'Начать игру', ui, 'play')
    exit_btn = engine.gui.Button((w // 2, h // 2 + 50), 200, 'Выйти', ui, 'exit')
    about_btn = engine.gui.Button((w // 2, h // 2 + 100), 200, 'Об игре', ui, 'about')
    engine.gui.Label((w // 2, h // 2 - 100), 96, 'zelda', ui)
    with open('high_scores.txt', 'r') as f:
        hs = f.readlines()
        hs = [line.strip() for line in hs]
    if not hs:
        hs = ['- не сохранено -']
    for i, line in enumerate(['лучшие результаты'] + hs):
        if i:
            lbl = engine.gui.Label((0, 0), 48, f'{i}. {line}', ui)
        else:
            lbl = engine.gui.Label((0, 0), 48, line, ui)
        lbl.rect.topleft = (50, h // 2 - 100 + i * 50)
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
                elif about_btn.rect.collidepoint(ev.pos):
                    if not about_screen(win, clk):
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
    engine.gui.Label((w // 2, h // 2 - 30), 96, f'Результат: {globals.Globals.player.score + globals.Globals.player.health}', ui)
    exit_btn = engine.gui.Button((w // 2, h // 2 + 50), 200, 'Выйти', ui, 'exit')
    hs = []
    with open('high_scores.txt', 'r') as f:
        for line in f:
            hs.append(int(line))
    if len(hs) and max(hs) < globals.Globals.player.score + globals.Globals.player.health:
        engine.gui.Label((w // 2, h // 2 - 200), 48, 'Новый рекорд!', ui)
    hs.append(globals.Globals.player.score + globals.Globals.player.health)
    hs = list(set(hs))
    hs.sort(reverse=True)
    hs = hs[:3]
    with open('high_scores.txt', 'w') as f:
        for score in hs:
            f.write(str(score) + '\n')
    for i, line in enumerate(['лучшие результаты'] + hs):
        if i:
            lbl = engine.gui.Label((0, 0), 48, f'{i}. {line}', ui)
        else:
            lbl = engine.gui.Label((0, 0), 48, line, ui)
        lbl.rect.topleft = (50, h // 2 - 100 + i * 50)
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


def about_screen(win: pg.Surface, clk: pg.time.Clock):
    size = w, h = win.get_size()
    ui = pg.sprite.Group()
    engine.gui.Label((w // 2, 48), 96, 'об игре', ui)
    back_btn = engine.gui.Button((100, 0), 200, 'Назад', ui, 'exit')
    back_btn.rect.topleft = (0, 0)
    line1 = engine.gui.Label((0, 0), 48, 'управление: ходьба - WASD, атака - пробел, пауза - esc', ui)
    line1.rect.topleft = (100, 150)
    line2 = engine.gui.Label((0, 0), 48, 'цель игры: уничтожить всех врагов', ui)
    line2.rect.topleft = (100, 220)
    line3 = engine.gui.Label((0, 0), 48, 'игра сделана с помощью pygame и pytmx', ui)
    line3.rect.topleft = (100, 290)
    running = True
    while running:
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                return 0
            elif ev.type == pg.MOUSEBUTTONDOWN:
                if back_btn.rect.collidepoint(ev.pos):
                    return 1
            ui.update(ev)
        win.fill('#2e222f')
        ui.draw(win)
        pg.display.update()
        clk.tick(60)
