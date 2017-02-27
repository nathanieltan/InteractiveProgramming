import pygame
from pygame.locals import *
import os, sys
from euclid import *

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if((event.key == K_RIGHT)
                       or (event.key == K_LEFT)
                       or (event.key == K_UP)
                       or (event.key == K_DOWN)):
                        self.smiley.move(event.key)

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
        image = pygame.image.load('smiley.png')
        self.image = image.convert()
        self.rect = image.get_rect()
        self.x_dist = 64
        self.y_dist = 64
        self.dx = 0
        self.dy = 0
        self.ddx = 0
        self.ddy = 0

    def move(self, key):
        x_move = 0
        y_move = 0

        if (key == K_RIGHT):
            x_move = self.x_dist
        elif (key == K_LEFT):
            x_move = -self.x_dist
        elif (key == K_UP):
            y_move = -self.y_dist
        elif (key == K_DOWN):
            y_move = self.y_dist

        self.rect.move_ip(x_move, y_move)


if __name__ == "__main__":
    MainWindow = FunGameMain()
    MainWindow.MainLoop()
