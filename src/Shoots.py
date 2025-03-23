"""
ISPPV1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Shoot.
"""

import random
from typing import Any, Tuple, Optional , TypeVar

import pygame

import settings
from src.Paddle import Paddle
from src.utilities.sprites import obtainImageSpriteSheet

class Shoots:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.width = 40
        self.height = 20

        self.vx = 0
        self.vy = 0

        self.in_play = True
        self.texture = settings.TEXTURES["spritesheet"]
        self.frames_image = 3
        self.animation_timer = 0
        self.animation_interval = 0.01
        self.current_frame = 0
        self.colission_max = 5
        # self.active = True

    def get_collision_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x - self.colission_max, self.y, self.width, self.height)

    def solve_world_boundaries(self) -> None:
        r = self.get_collision_rect()
        
        if r.bottom < 0:
            self.in_play = False
        elif r.top > settings.VIRTUAL_HEIGHT:
            self.in_play = False

    def collides(self, another: Any) -> bool:
        return self.get_collision_rect().colliderect(another.get_collision_rect())

    def update(self, dt: float) -> None:
        self.x += self.vx * dt
        self.y += self.vy * dt

        self.animation_timer += dt
        
        if self.animation_timer >= self.animation_interval :
            self.animation_timer = 0
            self.current_frame = (self.current_frame + 1) % self.frames_image
            
    def render(self, surface):
        
        cannonSprite = obtainImageSpriteSheet("shoots",self.width,self.height,"Up",self.current_frame)
        surface.blit(
           cannonSprite,
           (self.x,self.y)
        )
        #pygame.draw.rect(surface, (255, 0, 0), self.get_collision_rect(), 1)
        self.solve_world_boundaries()

    @staticmethod
    def get_intersection(r1: pygame.Rect, r2: pygame.Rect) -> Optional[Tuple[int, int]]:
        """
        Compute, if exists, the intersection between two
        rectangles.
        """
        if r1.x > r2.right or r1.right < r2.x or r1.bottom < r2.y or r1.y > r2.bottom:
            # There is no intersection
            return None

        # Compute x shift
        if r1.centerx < r2.centerx:
            x_shift = r2.x - r1.right
        else:
            x_shift = r2.right - r1.x

        # Compute y shift
        if r1.centery < r2.centery:
            y_shift = r2.y - r1.bottom
        else:
            y_shift = r2.bottom - r1.y

        return (x_shift, y_shift)

    @staticmethod
    def shoot_cannon(play_state: TypeVar("PlayState")) -> None:
        if play_state.cannonBalls:
            return
        if play_state.cannon_active == True:
            if play_state.cannon_ammo > 0:
                y_correction = play_state.paddle.y - play_state.paddle.height + 8
                    
                shootRight = Shoots(play_state.paddle.x + play_state.paddle.width - 5 , y_correction )
                shootLeft = Shoots(play_state.paddle.x - 20 + 2.5 , y_correction )
                    
                shootRight.vy = -170
                shootLeft.vy = -170
                    
                play_state.cannon_ammo -= 1
                    
                if play_state.cannon_ammo <= 0 :
                    play_state.cannon_active = False
                    play_state.cannon_ammo = 0
                    play_state.paddle.has_cannons = False
                    
                play_state.cannonBalls.append(shootLeft)
                play_state.cannonBalls.append(shootRight)
            else:
                play_state.cannon_active = False
                play_state.cannon_ammo = 0
                play_state.paddle.has_cannons = False
        else:
            print("No cannon")
        