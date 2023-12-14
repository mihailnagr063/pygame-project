import pygame as pg


class TileSet:
    def __init__(self, mapping, tile_size):
        self.mapping = mapping
        self.tiles = {}
        self.tile_size = tile_size
        self.load_tiles()

    def load_tiles(self):
        for key, value in self.mapping.items():
            self.tiles[key] = pg.transform.scale(pg.image.load(value).convert_alpha(), (self.tile_size, self.tile_size))


class TileMap(pg.sprite.Sprite):
    def __init__(self, file, tileset):
        super().__init__()
        self.tileset = tileset
        self.tile_size = self.tileset.tile_size
        self.map = []
        self.tileset = tileset
        with open(file, encoding='utf-8') as f:
            self.map = f.read().splitlines()
        self.image = pg.Surface((self.tile_size * max([len(i) for i in self.map]), self.tile_size * len(self.map)))
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.rerender()

    def rerender(self):
        for i, row in enumerate(self.map):
            for j, col in enumerate(row):
                self.image.blit(self.tileset.tiles[col], (j * self.tile_size, i * self.tile_size))


class Objects(pg.sprite.Group):
    def __init__(self, file, topleft, tileset):
        super().__init__()
        self.tileset = tileset
        self.tile_size = self.tileset.tile_size
        self.map = []
        self.tileset = tileset
        with open(file, encoding='utf-8') as f:
            self.map = f.read().splitlines()
        for i, row in enumerate(self.map):
            for j, col in enumerate(row):
                if col == ' ' or col == '#':
                    continue
                self.add(Object(pg.Vector2(topleft) + pg.Vector2(i * self.tile_size, j * self.tile_size), self.tileset.tiles[col]))


class Object(pg.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

    def on_clicked(self):
        pass
