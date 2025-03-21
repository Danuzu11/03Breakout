"""
ISPPV1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains some util functions to generate frames for the game textures.
"""

from typing import List

import pygame

from gale.frames import generate_frames


def generate_paddle_frames() -> List[List[pygame.Rect]]:
    paddle_base_width = 32
    paddle_height = 16

    x = 0
    y = paddle_height * 4

    frames = []

    for _ in range(4):
        frames.append(
            [
                # The smallest paddle is in (0, y) and its dimensions are 32x16.
                pygame.Rect(x, y, paddle_base_width, paddle_height),
                # The next paddle is in (32, y) and its dimensions are 64x16.
                pygame.Rect(
                    x + paddle_base_width, y, paddle_base_width * 2, paddle_height
                ),
                # The next paddle is in (96, y) and its dimensions are 96x16.
                pygame.Rect(
                    x + paddle_base_width * 3, y, paddle_base_width * 3, paddle_height
                ),
                # The largest paddle is in (0, y + 16) # and its dimensions are
                # 128x16.
                pygame.Rect(x, y + paddle_height, paddle_base_width * 4, paddle_height),
            ]
        )

        y += paddle_height * 2

    return frames


def generate_ball_frames() -> List[pygame.Rect]:
    ball_size = 8
    x = 96
    y = 48

    frames = []

    for _ in range(4):
        frames.append(pygame.Rect(x, y, ball_size, ball_size))
        x += ball_size

    x = 96
    y += ball_size

    for _ in range(3):
        frames.append(pygame.Rect(x, y, ball_size, ball_size))
        x += ball_size

    return frames


def generate_brick_frames(spritesheet: pygame.Surface) -> List[pygame.Rect]:
    all_frames = generate_frames(spritesheet, 32, 16)
    return all_frames[:20]


def generate_powerups_frames() -> List[pygame.Rect]:
    y = 12 * 16  # 4 brick rows + 8 paddle rows

    frames = []

    for j in range(10):
        frames.append(pygame.Rect(j * 16, y, 16, 16))

    return frames

def generate_shoot_frames() -> List[pygame.Rect]:
    
    #frame 0
    x = 241
    cannon_width = 150
    y = 176
    cannon_heigth = 99
    
    #frame 1
    x2 = 436
    cannon_width2 = 150
    y2 = 57
    cannon_heigth2 = 55
    
    #frame 2
    x3 = 240
    cannon_width3 = 150
    y3 = 57
    cannon_heigth3 = 55
    
    frames = []
    
    for _ in range (1):
        frames.append(
            [
                pygame.Rect(x, y, cannon_width, cannon_heigth),
                pygame.Rect(x2, y2, cannon_width2, cannon_heigth2),
                pygame.Rect(x3, y3, cannon_width3, cannon_heigth3)
            ]                 
        )
        
    return frames

def generate_cannons_frames() -> List[pygame.Rect]:
    
    #frame CANNON frame
    x = 192
    cannon_width = 47
    y = 391
    cannon_heigth = 99
    
    frames = []
    
    for _ in range (1):
        frames.append(
            [
                pygame.Rect(x, y, cannon_width, cannon_heigth),
            ]                 
        )
        
    return frames