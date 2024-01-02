import pygame as pg
from globals import *


class Popup(pg.sprite.Sprite):
    def __init__(self, pos, text):
        super().__init__(Globals.sprites)
        self.image = Globals.font_big.render(text, False, 'white')
        self.rect = self.image.get_rect(center=pos)
        self.frames_passed = 0

    def update(self):
        self.frames_passed += 1
        self.rect.y -= 0.1
        if self.frames_passed > 120:
            self.kill()


class Button(pg.sprite.Sprite):
    ST_NORMAL: pg.Surface
    ST_HOVER: pg.Surface

    def __init__(self, pos, width, text, group=None, icon: str = None, sound=True):
        super().__init__(group)
        self.margin = 8
        self.hovered = 0
        self.sound = pg.mixer.Sound('data/sound/menu-hover.wav') if sound else None
        if sound:
            self.sound.set_volume(0.25)
        rend_text = Globals.font_big.render(text, False, 'white')
        self.image = pg.Surface((width, rend_text.get_height() + self.margin * 2))
        self.rect = self.image.get_rect(center=pos)
        self.icon = None
        self.icon_rect = None
        if icon:
            self.icon = pg.transform.scale(pg.image.load(f'data/icons/{icon}.png').convert_alpha(), (32, 32))
            self.icon_rect = self.icon.get_rect(bottomleft=(self.margin, self.rect.height - self.margin))
        self.text = text
        self.render_all()
        self.image = self.ST_NORMAL

    def update(self, event):
        if event.type == pg.MOUSEMOTION:
            if self.rect.collidepoint(event.pos):
                self.image = self.ST_HOVER
                if self.hovered == 0 and self.sound:
                    self.sound.play()
                self.hovered = 1
            else:
                self.image = self.ST_NORMAL
                self.hovered = 0

    def render_all(self):
        text = Globals.font_big.render(self.text, False, 'white')
        self.ST_NORMAL = pg.Surface((self.rect.width, self.rect.height))
        self.ST_NORMAL.fill('#625565')
        if not self.icon:
            self.ST_NORMAL.blit(text, (self.margin, self.margin))
        else:
            self.ST_NORMAL.blit(self.icon, self.icon_rect)
            self.ST_NORMAL.blit(text, (self.margin + self.icon.get_width() + 4, self.margin))
        pg.draw.rect(self.ST_NORMAL, '#7f708a', (0, 0, self.rect.width, self.rect.height), 2)
        self.ST_HOVER = pg.Surface((self.rect.width, self.rect.height))
        self.ST_HOVER.fill('#7f708a')
        if not self.icon:
            self.ST_HOVER.blit(text, (self.margin, self.margin))
        else:
            self.ST_HOVER.blit(self.icon, self.icon_rect)
            self.ST_HOVER.blit(text, (self.margin + self.icon.get_width() + 4, self.margin))
        pg.draw.rect(self.ST_HOVER, '#625565', (0, 0, self.rect.width, self.rect.height), 2)


class CallbackButton(Button):
    def __init__(self, pos, width, text, callback):
        super().__init__(pos, width, text)
        self.callback = callback

    def update(self, event):
        super().update(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()


class Label(pg.sprite.Sprite):
    def __init__(self, pos, size, text, group=None):
        super().__init__(group)
        self.image = pg.font.Font(Globals.font_path, size).render(text, False, 'white')
        self.rect = self.image.get_rect(center=pos)

