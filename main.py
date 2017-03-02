import pygame
from pygame.locals import *
import os, sys
from environment import *
from player import *
clock = pygame.time.Clock()
dt = None


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
        global dt
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
            self.draw()
            self.update()

    def update(self):
        # updates sprites
        global dt
        self.gameSprites.update(dt)

        # Sees if player hits a platform
        hits = pygame.sprite.spritecollide(self.smiley, self.platforms, False)
        if hits:
            self.smiley.applyGravity = False
            self.smiley.vel.y = 0
            self.smiley.pos.y = self.plat1.rect.top
        else:
            self.smiley.applyGravity = True

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.gameSprites.draw(self.screen)
        pygame.display.flip()

    def LoadSprites(self):
        self.smiley = Smiley()
        self.plat1 = platform()

        # puts all the spites into appropriate groups
        self.platforms = pygame.sprite.Group(self.plat1)
        self.gameSprites = pygame.sprite.Group(self.smiley, self.plat1)


if __name__ == "__main__":
    MainWindow = FunGameMain()
    MainWindow.MainLoop()
