import pygame
from pygame.locals import *
import os, sys
import math
clock = pygame.time.Clock()


class FunGameMain:
    """
    Main FunGame class
    """
    def __init__(self, width=640, height=480):
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

            self.smiley.decel()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if((event.key == K_RIGHT)
                       or (event.key == K_LEFT)
                       or (event.key == K_UP)
                       or (event.key == K_DOWN)):
                        self.smiley.keyPress(event.key)

            self.smiley.move(dt)
            # drawing

            self.screen.blit(self.background, (0, 0))
            self.smiley_sprites.draw(self.screen)
            pygame.display.flip()

    def LoadSprites(self):
        self.smiley = Smiley()
        self.smiley_sprites = pygame.sprite.RenderPlain((self.smiley))


class Smiley(pygame.sprite.Sprite):
    """ make smiley """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        name = os.path.join('smiley.png')
        image = pygame.image.load(name)
        self.image = image.convert()
        self.rect = image.get_rect()
        self.dx = 0
        self.dy = 0
        self.ddx = 0
        self.ddy = 0

    def move(self, dt):
        self.rect.move_ip(self.dx * dt, self.dy * dt)
        self.dx += self.ddx
        self.dy += self.ddy

    def decel(self):
        if self.dx != 0:
            self.ddx = -1 * self.dx * .01

    def keyPress(self, key):  # handles the efffects of a key press
        if (key == K_RIGHT):
            if self.dx < 10:
                self.ddx = 10
        elif (key == K_LEFT):
            if self.dx > -10:
                self.ddx = -10
        elif (key == K_UP):
            self.dy = 50
        elif (key == K_DOWN):
            pass

if __name__ == "__main__":
    MainWindow = FunGameMain()
    MainWindow.MainLoop()
