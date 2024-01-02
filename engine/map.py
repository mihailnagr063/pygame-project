import pygame as pg
import pytmx

BG_TILES = [' ']


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
    def __init__(self, tiled_map: pytmx.TiledMap, tile_size):
        super().__init__()
        self.tile_size = tile_size
        self.map = tiled_map
        self.layer = [l for l in tiled_map.layers if l.name == 'background'][0]
        self.image = pg.Surface((self.tile_size * self.map.width, self.tile_size * self.map.height))
        self.rect = self.image.get_rect(topleft=(0, 0))
        self.rerender()

    def rerender(self):
        for x, y, gid in self.layer:
            tile = pg.transform.scale(self.map.get_tile_image_by_gid(gid).convert_alpha(), (32, 32))
            if not tile:
                continue
            self.image.blit(tile, (x * self.tile_size, y * self.tile_size))


class Objects(pg.sprite.Group):
    def __init__(self, tiled_map: pytmx.TiledMap, objmap):
        super().__init__()
        self.tile_size = 32
        self.map = tiled_map
        self.layer = [l for l in tiled_map.layers if l.name == 'colliding'][0]
        self.objmap = objmap
        for x, y, gid in self.layer:
            if gid == 0:
                continue
            self.add(self.objmap.get(gid, Object)((x * self.tile_size, y * self.tile_size),
                                                  pg.transform.scale(self.map.get_tile_image_by_gid(gid).convert_alpha(), (32, 32))))

    def handle_click(self, pos):
        for sprite in self.sprites():
            if sprite.rect.collidepoint(pos):
                sprite.on_clicked()


class Object(pg.sprite.Sprite):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

    def on_clicked(self):
        pass

    def update(self):
        pass
