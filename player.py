import pygame
from pygame.locals import*
import os, sys
vec = pygame.math.Vector2

facingRight = True
gravity = 30000
friction = -3

class Hambo(pygame.sprite.Sprite):
    """ make Hambo """

    def __init__(self, carrots=0):
        pygame.sprite.Sprite.__init__(self)
        self.imageNames = ['hambo_walk_1.png','hambo_stand.png','hambo_walk_2.png']
        image = pygame.image.load(self.imageNames[1])
        self.image = image.convert()
        self.image = image.convert_alpha()
        self.rect = image.get_rect()
        self.pos = vec(400, 100)
        self.vel = vec(0, 0)
        self.accel = vec(0, 0)
        self.applyGravity = False
        self.animationFrames = 0  # counts the amount of frames a sprite has been displayed
        self.animationState = 0

        self.carrots = 0     # counts how many carrots eaten

    def update(self, dt):
        global facingRight
        # arrow key input
        self.updateAnimation()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.accel.x = -500
            if facingRight:
                facingRight = False
                self.image = pygame.transform.flip(self.image,True,False)

        elif keys[pygame.K_RIGHT]:
            self.accel.x = 500
            if not facingRight:
                facingRight = True
                self.image = pygame.transform.flip(self.image,True,False)
        elif not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.accel.x = 0

        if keys[pygame.K_UP]:
            if not self.applyGravity:
                self.vel.y = -350

        # moves the player
        self.move(dt)
        # calls walking animation

    def updateAnimation(self):
        self.animationFrames = (self.animationFrames+1) % 30

        if self.animationFrames == 29:
            if int(self.vel.x) != 0:
                self.animationState = (self.animationState+1) % len(self.imageNames)
                image = pygame.image.load(self.imageNames[self.animationState])
                self.image = image.convert()
                self.image = image.convert_alpha()
            else:
                self.animationState = 0
                image = pygame.image.load(self.imageNames[self.animationState])
                self.image = image.convert()
                self.image = image.convert_alpha()
            if not facingRight:
                self.image = pygame.transform.flip(self.image, True, False)

    def move(self, dt):
        # applying friction
        self.accel.x += self.vel.x * friction

        # Does gravity
        if self.applyGravity:
            self.accel = vec(self.accel.x, gravity*dt)
        else:
            self.accel = vec(self.accel.x, 0)
        # Movement Calculations
        self.pos += self.vel * dt + 0.5 * self.accel * (dt ** 2)
        self.vel += self.accel * dt

        # updates the position
        self.rect.midbottom = (self.pos)
