import pygame
from pygame.locals import*
import os, sys
import math


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
    def update(self, dt):
        self.ddx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.dx = -100
        if keys[pygame.K_RIGHT]:
            self.dx = 100
        self.move(dt)
    def move(self, dt):
        self.rect.move_ip(self.dx * dt, self.dy*dt)
        self.dx += self.ddx * dt
        self.dy += self.ddy * dt

    def decel(self):
        self.ddx=0
        if self.dx != 0:
            pass



