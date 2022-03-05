from os import walk
from csv import reader
from typing import List
from settings import *

import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter = ',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map

def import_folder(path: str) -> List[pygame.surface.Surface]:
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list


def load_tile_table(filename):
    image = pygame.image.load(filename).convert_alpha()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, int(image_width/TILESIZE)):
        line = []
        tile_table.append(line)
        for tile_y in range(0, int(image_height/TILESIZE)):
            rect = (tile_x*TILESIZE, tile_y*TILESIZE, TILESIZE, TILESIZE)
            line.append(image.subsurface(rect))
    return tile_table