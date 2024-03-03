from os import environ, path, getcwd
import json
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'


# core_engine Directory
from .core_engine.scene_manager import SceneManager

# utils Directory
from .utils.colors import *
from .utils.settings import GlobalSettings, LocalSettings
from .utils.properties import GlobalProperties, LocalProperties
from .utils.debug import debug_print
from .utils.subpixel import SubPixelSurface


# engine Directory
from .engine.area import Area
from .engine.entity import Entity
from .engine.scene import Scene, SceneCatcher, SceneManager
from .engine.camera import Camera
from .engine.game import Game


# ui_elemetns Directory
from .ui_elements.label import Label
# from .ui_manager import 


# physics Directory
from .physics.object import Object
from .physics.projectile import Projectile, Particles


# services Directory
from .services.animation import LazyAnimationService
from .services.image import ImageService
from .services.sound import SoundService
from .services.font import FontService
from .services.tilemap import TileMap, TileSet



__all__ = [
'Area', 
'Entity', 
'Scene', 
'Camera', 
'Scene', 'SceneCatcher',
"Game",
'Label', 
'Object', 
'Projectile', 'Particles', 
'LazyAnimationService', 
'SoundService',
'ImageService', 
'FontService', 
'TileMap', 'TileSet', 
'GlobalSettings', 'LocalSettings',
'GlobalProperties', 'LocalProperties',
'debug_print',
'SubPixelSurface'
]


__author__ = "TheooKing/Theolaos"
__version__ = "v2.2.05-exp"

__name__ = "tleng2"
__doc__ = f'''TLeng2.py is a python 2d game engine

Current version is {__version__}

Current License:
MIT License

Copyright (c) 2023 Theofilos Nikolaos Savvidis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

# Engine Report:
# TODO: Settings Json support.
# TODO: Animation Json Support.
# TODO: Redo the Label system in update 2.2 and add:
#       capitilize / lower
#       striketrough, underlined
#       left|Center|Right
#       find
#       join
#       change_{smt}
#       __len__, __str__