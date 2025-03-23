"""
ISPPV1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the PowerUp specialization to make balls move slower.
"""

import random
from typing import TypeVar

from gale.factory import Factory

import settings
from src.Ball import Ball
from src.powerups.PowerUp import PowerUp


class SlowMotion(PowerUp):
    """
    Power to make the balls move slower
    """ 

    def __init__(self, x: int, y: int) -> None:
        super().__init__(x, y, 6)

    def take(self, play_state: TypeVar("PlayState")) -> None:
        play_state.slow_active = True
        play_state.slow_timer = 5
        self.active = False 