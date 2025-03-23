"""
ISPPV1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Paddle.
"""

import pygame

import settings
from src.utilities.sprites import obtainImageSpriteSheet

class Paddle:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.width = 64
        self.height = 16

        # By default, the blue paddle
        self.skin = 0

        # By default, the 64-pixels-width paddle.
        self.size = 1

        self.texture = settings.TEXTURES["spritesheet"]
        self.frames = settings.FRAMES["paddles"]
        self.has_cannons = False
        
        self.cannonWidth = 20
        self.cannonHeigth = 40
        # The paddle only move horizontally
        self.vx = 0

    def resize(self, size: int) -> None:
        self.size = size
        self.width = (self.size + 1) * 32

    def dec_size(self):
        self.resize(max(0, self.size - 1))

    def inc_size(self):
        self.resize(min(3, self.size + 1))

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self, dt: float) -> None:
        next_x = self.x + self.vx * dt

        if self.has_cannons:
            if self.vx < 0:
                self.x = max(self.cannonWidth, next_x)
            else:
                self.x = min(settings.VIRTUAL_WIDTH - self.width - self.cannonWidth - 5, next_x)
        else:
            if self.vx < 0:
                self.x = max(0, next_x)
            else:
                self.x = min(settings.VIRTUAL_WIDTH - self.width, next_x)

    def render(self, surface: pygame.Surface) -> None:
        
        surface.blit(self.texture, (self.x , self.y), self.frames[self.skin][self.size])

        if self.has_cannons:
            cannonSprite = obtainImageSpriteSheet("cannons",self.cannonWidth,self.cannonHeigth,None)
            y_correction = self.y - self.height + self.cannonHeigth/20
            
            rigth_cannon_x= min(self.x + self.width - 5,settings.VIRTUAL_WIDTH - self.cannonWidth)
            # RIGTH CANNON
            surface.blit(
                cannonSprite,
                (rigth_cannon_x, y_correction)
            )
            left_cannon_x = max(0,self.x - self.cannonWidth + 2.5)
            # LEFT CANNON
            surface.blit(
                cannonSprite,
                (left_cannon_x , y_correction)
            )
                
        
