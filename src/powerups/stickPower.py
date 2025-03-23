import random
from typing import TypeVar

from gale.factory import Factory

import settings
from src.Ball import Ball
from src.powerups.PowerUp import PowerUp


class StickPower(PowerUp):
    """
    Power-up to add sticky power in the paddle.
    """ 

    def __init__(self, x: int, y: int) -> None:
          super().__init__(x, y, 4)

    def take(self, play_state: TypeVar("PlayState")) -> None:
        paddle = play_state.paddle
        play_state.magnet_active = True
        play_state.magnet_timer = 10
        self.active = False