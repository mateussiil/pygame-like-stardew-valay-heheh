import pygame
from player import Player
from settings import *

class Card(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.sprint_type = 'card'

        self.rect = pygame.Rect(WIDTH-30, HEIGTH-30, 30, 30)
    
    def show_bar(self, current, max_amount, bg_rect, color):
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, 'gray', current_rect, 3)

    def onClick(self, leftButton, middleButton, rightButton ):
        print(leftButton)
    
    def display(self):
        self.show_bar(300, 300, self.rect, HEALTH_COLOR)

