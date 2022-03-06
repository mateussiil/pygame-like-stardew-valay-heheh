import json
import random
import pygame
from support import read_save
from player import Player
from settings import *

class Card(pygame.sprite.Sprite):
    def __init__(self, pos, index, render, groups):
        super().__init__(groups)
        self.index = index
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)
        self.render = render
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
            self.render += 1
            self.save()
    
    def save(self):
        data = read_save('../saves/menu.txt')
        with open('../saves/menu.txt', 'w') as file:
            data[self.index] = self.render
            json.dump(data, file)
    
    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if not self.click_pressable:
            if current_time - self.click_press_time >= self.click_press_cooldown:
                self.click_pressable = True
    
    def show(self):
        text_surf = self.font.render(str(int(self.render)), False, TEXT_COLOR)
        x = self.rect.centerx
        y = self.rect.centery
        text_rect = text_surf.get_rect(bottomright = (x, y))
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect) #inflate is padding
        self.display_surface.blit(text_surf, text_rect)

    def display(self):
        pygame.draw.rect(self.display_surface, 'black', self.rect)
        pygame.draw.rect(self.display_surface, 'white', self.rect, 1)
        self.show()
        self.cooldowns()

