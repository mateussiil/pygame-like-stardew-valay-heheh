import pygame, sys
import pygame.freetype  # Import the freetype module.
from settings import * 
from debug import debug
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Fazendinha')
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(True)
        self.level = Level()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                    pygame.quit()
                    sys.exit()
            
            self.screen.fill('#001010')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()