import pygame
from pygame.locals import*
import os, sys


class Level():
    """
    Generic Level Class
    """
    def __init__(self):
        self.platform_list = pygame.sprite.Group()
        self.screen_shift = 0

    def shift_screen(self, shift_x):
        """
        controls scrolling of screen
        """

        for platform in self.platform_list:
            platform.rect.x += shift_x


class Platform(pygame.sprite.Sprite):
    """Simple Platform"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        name = os.path.join('platform.png')
        image = pygame.image.load(name)
        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()


class Level_1(Level):
    def __init__(self):
        Level.__init__(self)

        level = [[100, 650],
                 [300, 500],
                 [700, 350],
                 [1000, 800],
                 [-400, 500]]

        for platform in level:
            block = Platform()
            block.rect.x = platform[0]
            block.rect.y = platform[1]
            self.platform_list.add(block)
