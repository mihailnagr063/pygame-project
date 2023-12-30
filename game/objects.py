import pygame as pg
import engine
from globals import Globals


class Chest(engine.Object):
    def __init__(self, pos, image):
        super().__init__(pos, image)
        self.items = []

    def on_clicked(self):
        engine.gui.Popup(Globals.camera.world_to_screen(self.rect.center), 'Сундук открыт')
        self.kill()
        # добавить игроку предметы в инвентарь


object_map = {
    'C': Chest,
    '#': engine.Object
}
