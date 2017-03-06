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

        # Sees if player hits a platform
        hits = pygame.sprite.spritecollideany(self.Hambo, self.platforms, False)
        self.Hambo.applyGravity = True
        if hits:
            if self.Hambo.vel.y > 0:
                self.Hambo.applyGravity = False
                self.Hambo.vel.y = 0
                self.Hambo.pos.y = hits.rect.top+1
            else:
                self.Hambo.vel.y = self.Hambo.vel.y * -1

        self.gameSprites.update(dt)

        if self.Hambo.pos.x >= 500:
            diff = self.Hambo.pos.x - 500
            self.Hambo.pos.x = 500
            self.lvl.shift_screen(-diff)

        if self.Hambo.pos.x <= 120:
            diff = 120 - self.Hambo.pos.x
            self.Hambo.pos.x = 120
            self.lvl.shift_screen(diff)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.gameSprites.draw(self.screen)
        pygame.display.flip()

    def LoadSprites(self):
        self.Hambo = Hambo()
        self.lvl = Level_1()

        # puts all the spites into appropriate groups
        self.platforms = self.lvl.platform_list
        self.gameSprites = pygame.sprite.Group(self.Hambo, self.lvl.platform_list)


if __name__ == "__main__":
    MainWindow = FunGameMain()
    MainWindow.MainLoop()
