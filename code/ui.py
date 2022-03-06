import pygame
from components import Card
from player import Player
from settings import *

class UI(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        self.sprint_type = 'ui'

        self.rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        
        self.stamina_bar_rect = pygame.Rect(10, 30, HEALTH_BAR_WIDTH, BAR_HEIGHT)

    def show_bar(self, current, max_amount, bg_rect, color):
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, current_rect, 3)
    
    def display(self, player: Player):
        self.show_bar(300, 300, self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(300, 300, self.stamina_bar_rect, 'green')

class MenuDown(pygame.sprite.Sprite):
    def __init__(self, groups, group_clickable):
        self.groups = groups
       
        self.group_clickable = group_clickable
        
        self.storage_limit = 10
        self.display_surface = pygame.display.get_surface()
        self.rect = pygame.Rect(WIDTH // 2, HEIGTH - 30, self.storage_limit*TILESIZE + 2, TILESIZE + 4)
        self.rect.center = (WIDTH // 2, HEIGTH - 30)
        self.items = [x for x in range(self.storage_limit)]

        self.draw()

    def draw(self):
        for i in range(self.storage_limit):
            x = self.rect.left + i*TILESIZE + 1
            y = self.rect.top
            self.items[i] = Card((x,y), self.group_clickable)

    def display(self):
        pygame.draw.rect(self.display_surface, HEALTH_COLOR, self.rect)
        for sprites in self.items:
            sprites.rect.center =  (sprites.rect.center[0], self.rect.center[1])
            sprites.display()
        