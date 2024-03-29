from ..components.renderable import Renderable
from ..engine.properties import EngineProperties

import pygame


class TileSet:
    def __init__(self, 
            tset,
            width, 
            height
        ) -> None:
        """
        Tile set, 
        {"grass": grass_tile.png,
         "concrete" : concrete_tile.png
         ...}
        """
        
        self.set = tset
        self.width = width
        self.height = height


class TileMap:
    def __init__(self, name):
        self.tiles = []
        self.tileset = {}
        self.renderable = Renderable()


    def load_tilemap(self, 
            tilemap: list
        ) -> None:
        """
        Matrix list, if not created in a json file.
        """
        self.tiles = tilemap
    

    def load_tileset(self,
            tileset: TileSet
        ) -> None:
        self.tileset = tileset


    #TODO
    def load_tilemap_json(self,
            tilemap: list
        ) -> None: ...


    def load_tileset_json(self,
            tileset: TileSet
        ) -> None: ...


    def render(self) -> None:
        # Renderer.render_tiles()
        for y, y_tiles in enumerate(self.tiles):
            for x, tile_name in enumerate(y_tiles):
                self.renderable.update(x*self.width, y*self.height, self.tileset[tile_name])
                self.renderable.render()

    def update(self) -> None:
        pass