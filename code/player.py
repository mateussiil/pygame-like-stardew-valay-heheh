import pygame
from settings import *
from support import *
from debug import debug


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstacle_sprites):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

        self.animations = load_tile_table('../graphics/player/idle/idle.png')
        self.status = 'idle'
        self.image = self.animations[0][0]
        self.rect: pygame.rect.Rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0, -5)
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        # movement
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = 'up'
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = 'down'
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = 'right'
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = 'left'
        else:
            self.direction.x = 0

    def move(self, speed: int):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += int(self.direction.x * speed)
        self.collision('horizontal')
        self.hitbox.y += int(self.direction.y * speed)
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0: # Moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0: # Moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0: # Moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0: # Moving top  
                        self.hitbox.top = sprite.hitbox.bottom

    def animate(self):
        animation = self.animations
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)][0]
        self.rect = self.image.get_rect(center = self.hitbox.center)

    def update(self):
        self.input()
        # self.animate()
        self.move(self.speed)