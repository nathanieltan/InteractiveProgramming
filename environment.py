import pygame
from pygame.locals import*
import os, sys


class Level():
    """
    Generic Level Class
    """
    def __init__(self):
        self.platform_list = pygame.sprite.Group()
        self.carrot_list = pygame.sprite.Group()
        self.screen_shift = 0

    def shift_screen(self, shift_x):
        """
        controls scrolling of screen
        """

        for platform in self.platform_list:
            platform.rect.x += shift_x
        for carrot in self.carrot_list:
            carrot.rect.x += shift_x


class Platform(pygame.sprite.Sprite):
    """Simple Platform"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        name = os.path.join('platform.png')
        image = pygame.image.load(name)
        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()

    def update(self, dt):
        self.checkBounds()

    def checkBounds(self):
        """ wrap around screen """

        if self.rect.centerx - (self.rect.width / 2) > 1000:
            self.rect.centerx = 0
        if self.rect.centerx + (self.rect.width / 2) < 0:
            self.rect.centerx = 1000


class Carrot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        name = os.path.join('carrot.png')
        image = pygame.image.load(name)
        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()

    def update(self, dt):
        self.checkBounds()

    def checkBounds(self):
        """ wrap around screen """

        if self.rect.centerx - (178 / 2) > 1000:
            self.rect.centerx = 0
        if self.rect.centerx + (178 / 2) < 0:
            self.rect.centerx = 1000


class Level_1(Level):
    def __init__(self):
        Level.__init__(self)

        level = [[100, 600],
                 [200, 500],
                 [300, 700],
                 [400, 500],
                 [700, 400],
                 [600, 700],
                 [750, 800],
                 [1000, 800],
                 [1100, 700]]

        for platform in level:
            block = Platform()
            block.rect.x = platform[0]
            block.rect.y = platform[1]
            self.platform_list.add(block)

            carrot = Carrot()
            carrot.rect.x = platform[0] + (block.rect.width / 2)
            carrot.rect.y = platform[1] - block.rect.height
            self.carrot_list.add(carrot)
