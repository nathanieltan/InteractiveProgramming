import pygame
from pygame.locals import*
import os, sys


class platform(pygame.sprite.Sprite):
    """Simple Platform"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        name = os.path.join('platform.png')
        image = pygame.image.load(name)
        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()
        self.rect.x = 300
        self.rect.y = 500
