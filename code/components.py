import random
import pygame
from player import Player
from settings import *

class Card(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.sprint_type = 'card'
        self.random = random.randint(0,9)

        self.rect = pygame.Rect(pos[0], pos[1], TILESIZE, TILESIZE)

        self.click_press_cooldown = 200
        self.click_pressable = True
        self.click_press_time = None

        self.display()
    
    def onClick(self, leftButton, middleButton, rightButton ):
        if self.click_pressable:
            self.click_pressable = False
            self.click_press_time = pygame.time.get_ticks()
    
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if not self.click_pressable:
            if current_time - self.click_press_time >= self.click_press_cooldown:
                self.click_pressable = True

    def display(self):
        pygame.draw.rect(self.display_surface, 'black', self.rect)
        pygame.draw.rect(self.display_surface, 'white', self.rect, 1)
        self.cooldowns()

