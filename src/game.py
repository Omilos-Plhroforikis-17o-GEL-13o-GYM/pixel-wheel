"""
Gameplay scene class
"""
from .tleng2 import *
from .physics import Player

from pymunk import Vec2d
import pymunk
import pygame
import os

def flipy(p):
    """Convert chipmunk coordinates to pygame coordinates."""
    return Vec2d(p[0], -p[1]+RendererProperties._display.get_size()[1])


def image_load(*path) -> pygame.SurfaceType:
    return pygame.image.load(os.path.join(*path)).convert_alpha()

class FreeRoam(Scene):
    def __init__(self, scene_name) -> None:
        self.camera = Camera(default_camera = True)
        super().__init__(scene_name,'free_roam')
        assets_dir = os.path.join(get_parent_dir(__file__,2), 'assets')

        self.debug = True

        self.space = pymunk.Space()
        self.space.gravity = Vec2d(0.0, 0.0)
        self.space.damping = .01

        self.player_sprite = SpriteStackService()
        self.player_sprite.load_images(os.path.join(assets_dir,'formula'))

        self.player = Player((0,0), self.space, self.player_sprite.images[0].get_width(),self.player_sprite.images[0].get_height())

        


        self.city_streets_tileset = TileSet({
            'road_straight_up' : image_load(assets_dir,'city_tileset', 'road_straight_up.png'),
            'road_straight_down' : image_load(assets_dir,'city_tileset', 'road_straight_down.png'),
            'road_straight_right' : image_load(assets_dir,'city_tileset', 'road_straight_right.png'),
            'road_straight_left' : image_load(assets_dir,'city_tileset', 'road_straight_left.png'),
            'road_turn_ne' : image_load(assets_dir,'city_tileset','road_turn_ne.png'),
            'road_turn_se' : image_load(assets_dir,'city_tileset','road_turn_se.png'),
            'road_turn_sw' : image_load(assets_dir,'city_tileset','road_turn_sw.png'),
            'road_turn_nw' : image_load(assets_dir,'city_tileset','road_turn_nw.png'),
            'pavement' : image_load(assets_dir,'city_tileset', 'pavement.png'),
            'road' : image_load(assets_dir,'city_tileset', 'road.png'),
            'paved_road' : image_load(assets_dir,'city_tileset', 'paved_road.png')
        }, 35, 35)

        RU = 'road_straight_up'
        RD = 'road_straight_down'
        RR = 'road_straight_right'
        RL = 'road_straight_left'
        NE = 'road_turn_ne'
        SE = 'road_turn_se'
        SW = 'road_turn_sw'
        NW = 'road_turn_nw'
        PO = 'pavement'
        RO = 'road'
        PR = 'paved_road'

        tilemap = [
            [RO,RO,RO,RO,RO,RO,RO,RO,RO,RO,RO,RO,RO],
            [RO,SE,RD,RD,RD,SW,SE,RD,RD,RD,SW,RO,RO],
            [RO,RR,PO,PO,PO,RL,RR,PO,PO,PO,RL,RO,RO],
            [RO,RR,PO,PO,PO,RL,NE,RU,RU,RU,NW,RO,RO],
            [RO,RR,PO,PO,PO,RL,SE,RD,RD,RD,SW,RO,RO],
            [RO,NE,RU,RU,RU,NW,NE,RU,RU,RU,NW,RO,RO],
            [RO,RO,RO,RO,RO,RO,RO,RO,RO,RO,RO,RO,RO],
        ]


        ht = 35/2
        dc = 8 # distance from curb y px
        tile_hitboxes = {
            'road_straight_up' : [(-ht,ht),(-ht+dc,ht),(-ht+dc,-ht),(-ht,-ht)],
            'road_straight_down' : [(-ht,-ht),(-ht,-ht+dc),(ht,-ht+dc),(ht,-ht)],
            'road_straight_right' : [(ht,ht),(ht-dc,ht),(ht-dc,-ht),(ht,-ht)],
            'road_straight_left' : [(-ht,ht),(-ht+dc,ht),(-ht+dc,-ht),(-ht,-ht)],
            'road_turn_ne' : '',
            'road_turn_se' : '',
            'road_turn_sw' : '',
            'road_turn_nw' : '',
            'pavement' : '',
            'road' : '',
            'paved_road' : '',
        }

        self.free_roam_tilemap = TileMap()
        self.free_roam_tilemap.load_tilemap(tilemap)
        self.free_roam_tilemap.load_tileset(self.city_streets_tileset)


        self.rotonta = SpriteStackService()
        self.rotonta.load_images(os.path.join(assets_dir,'ROTONTA'))
        self.rotonta.update({'x':-17.5 + 35*5,'y':35*3})

        self.lefkos_pirgos = SpriteStackService()
        self.lefkos_pirgos.load_images(os.path.join(assets_dir,'LEFKOS'))
        self.lefkos_pirgos.update({'x':-17.5 + 35*10,'y':35*2 +5})


        self.polikatikia1 = SpriteStackService()
        self.polikatikia1.load_images(os.path.join(assets_dir,'building'))
        self.polikatikia1.update({'x':-17.5 + 35*4,'y':35*2})

        self.polikatikia2 = SpriteStackService()
        self.polikatikia2.load_images(os.path.join(assets_dir,'building'))
        self.polikatikia2.update({'x':-17.5 + 35*3,'y':35*3})

        self.polikatikia3 = SpriteStackService()
        self.polikatikia3.load_images(os.path.join(assets_dir,'building'))
        self.polikatikia3.update({'x':-17.5 + 35*8,'y':35*2})

        self.polikatikia4 = SpriteStackService()
        self.polikatikia4.load_images(os.path.join(assets_dir,'building'))
        self.polikatikia4.update({'x':-17.5 + 35*9,'y':35*2})

        self.polikatikia5 = SpriteStackService()
        self.polikatikia5.load_images(os.path.join(assets_dir,'building'))
        self.polikatikia5.update({'x':-17.5 + 35*3,'y':35*2})

        self.buildings = [
                     self.polikatikia5,
                     self.polikatikia1,
                     self.polikatikia2,
                     self.polikatikia3,
                     self.polikatikia4]

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        # self.space = pymunk.Space()

    def event_handling(self, keys_pressed) -> None:                    
        if keys_pressed[pygame.K_ESCAPE]:
            SceneManagerMethods.change_current_scene('Menu')
        for event in EngineProperties._events:
            self.player.handle_event(event)


    def update(self) -> None:
        self.space.step(1/60)

        self.player.update(EngineProperties._dt)
        pos = self.player.body._get_position()
        angl = convert_rad_to_deg(self.player.body._get_angle())
        self.player_sprite.update(params={
            'x':pos[0],
            'y':pos[1],
        })

        self.player_sprite.rotation = angl
        print(angl,self.player.body._get_angle())
        # self.rotonta.update({'x':35,'y':50})
        # self.lefkos_pirgos.update()
    

    def render(self) -> None:
        RendererMethods.fill_display(color=(34,32,52))
        self.free_roam_tilemap.render()

        if self.debug:
            for obj in self.all_sprites:
                shape = obj.shape
                ps = [flipy(pos.rotated(shape.body.angle) + shape.body.position)
                      for pos in shape.get_vertices()]
                ps.append(ps[0])
                pygame.draw.rect(RendererProperties._display, pygame.Color('blue'), obj.rect, 2)
                pygame.draw.lines(RendererProperties._display, (90, 200, 50), False, ps, 2)

        self.player_sprite.render()

        self.rotonta.render()
        self.lefkos_pirgos.render()

        for building in self.buildings:
            building.render()

        

        


        
        