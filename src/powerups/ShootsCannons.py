# """
# ISPPV1 2023
# Study Case: Breakout

# Author: Alejandro Mujica
# alejandro.j.mujic4@gmail.com

# This file contains the specialization of PowerUp to add two more ball to the game.
# """

# import random
# from typing import TypeVar

# from gale.factory import Factory

# import settings
# from src.Ball import Ball
# from src.powerups.PowerUp import PowerUp
# from src.Shoots import Shoots


# class ShootsCannons():
#     """
#     Power-up that shoot cannons, this is a apart power.
#     """ 

#     def __init__(self, x: int, y: int) -> None:
#         super().__init__(x, y, 3)
#         self.shoots_factory = Factory(Shoots)
#         self.active = False
        
#     def take(self, play_state: TypeVar("PlayState")) -> None:

            # if play_state.cannon_active == True:
            #     if play_state.cannon_ammo > 0:
            #         y_correction = play_state.paddle.y - play_state.paddle.height + 8
                    
            #         shootRight = self.shoots_factory.create(play_state.paddle.x + play_state.paddle.width - 5 , y_correction )
            #         shootLeft = self.shoots_factory.create(play_state.paddle.x - 20 + 2.5 , y_correction )
                    
            #         shootRight.vy = -170
            #         shootLeft.vy = -170
                    
            #         play_state.cannon_ammo -= 1
                    
            #         if play_state.cannon_ammo <= 0 :
            #             play_state.cannon_active = False
            #             play_state.cannon_ammo = 0
            #             play_state.paddle.has_cannons = False
                    
            #         play_state.cannonBalls.append(shootLeft)
            #         play_state.cannonBalls.append(shootRight)
            #     else:
            #         print("eje cuidadito perro, deja la maña ")