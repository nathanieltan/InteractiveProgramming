import pygame
from pygame.locals import*
import os, sys
vec = pygame.math.Vector2

class Smiley(pygame.sprite.Sprite):
    """ make smiley """

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        name = os.path.join('smiley.png')
        image = pygame.image.load(name)
        self.image = image.convert()
        self.rect = image.get_rect()
        self.pos = vec(100,100)
        self.vel = vec(0,0)
        self.accel = vec(0,0)

    def update(self, dt):

        # arrow key input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.accel.x = -300
        elif keys[pygame.K_RIGHT]:
            self.accel.x = 300
        elif not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.accel.x = 0

        if keys[pygame.K_UP]:
            self.vel.y = -100

        # moves the player
        self.move(dt)

    def move(self, dt):
        # applying friction
        self.accel.x += self.vel.x * -2

        # Does gravity
        self.accel = vec(self.accel.x,10000*dt)

        # Movement Calculations
        self.pos += self.vel * dt + 0.5 * self.accel * (dt ** 2)
        self.vel += self.accel * dt

        # updates the position
        self.rect.midbottom = (self.pos)

