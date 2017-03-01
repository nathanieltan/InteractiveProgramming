import pygame
from pygame.locals import *
import os, sys
import math
from player import *
clock = pygame.time.Clock()


class FunGameMain:
    """
    Main FunGame class
    """
    def __init__(self, width=1000, height=1000):
        self.width = width
        self.height = height
        pygame.init()
        # Create the screen
        self.screen = pygame.display.set_mode((self.width, self.height))

    def MainLoop(self):
        """main loop of game"""
        self.LoadSprites()

        # makes it so user can hold down keys
        pygame.key.set_repeat(50, 100)

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

        while 1:
            dtime_ms = clock.tick(60)  # gets the tick time in milliseconds
            dt = dtime_ms/1000  # converting the tick time to seconds


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()

            self.smiley.update(dt)

            # drawing

            self.screen.blit(self.background, (0, 0))
            self.smiley_sprites.draw(self.screen)
            pygame.display.flip()

    def LoadSprites(self):
        self.smiley = Smiley()
        self.smiley_sprites = pygame.sprite.RenderPlain((self.smiley))


if __name__ == "__main__":
    MainWindow = FunGameMain()
    MainWindow.MainLoop()
