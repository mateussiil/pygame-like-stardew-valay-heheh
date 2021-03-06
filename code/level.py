import pygame
import pygame.freetype
from components import Card
from ui import UI, MenuDown
from settings import *
from support import import_csv_layout, import_folder 
from tile import Tile
from debug import debug
from player import Player

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = YSortCamerGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.mouseable_sprites = pygame.sprite.Group()

        self.create_map()

        self.ui = UI(self.mouseable_sprites)
        self.menu_bottom = MenuDown([], self.mouseable_sprites)

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('../map/map_FloorBlocks.csv'),
            'entities': import_csv_layout('../map/map_Entities.csv')
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y), [self.obstacle_sprites], 'invisible')
                        if style == 'entities':
                            if col == '0':
                                self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)
        
    def mouse_logic(self):
        if self.mouseable_sprites:
            for mouse_sprite in self.mouseable_sprites:
                click = pygame.mouse.get_pressed()
                collision_sprites = mouse_sprite.rect.collidepoint(pygame.mouse.get_pos()) 
                if collision_sprites and mouse_sprite.sprint_type == 'card' and click[0]:
                    mouse_sprite.onClick(click[0], click[1], click[2])

    def run(self):
        #update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        self.mouse_logic()
        self.ui.display(self.player)
        self.menu_bottom.display()

class YSortCamerGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        #creating the floor
        self.floor_surf = pygame.image.load('../graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0, 0))

    def custom_draw(self, player: Player):

        #getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y =  player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery): # type: ignore #O bloco nao fica em cima do player
            assert sprite.rect is not None
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
