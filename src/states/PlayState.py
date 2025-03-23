"""
ISPPV1 2023
Study Case: Breakout

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class to define the Play state.
"""





import random

import pygame

from gale.factory import AbstractFactory
from gale.state import BaseState
from gale.input_handler import InputData
from gale.text import render_text
from src.Shoots import Shoots

import settings
import src.powerups


class PlayState(BaseState):
    def enter(self, **params: dict):
        
        self.cannonBalls = params["cannonBalls"]
        self.cannon_active = params.get("cannon_active", False)
        self.cannon_ammo = params.get("cannon_ammo", 0)
        self.magnet_active = params.get("magnet_active", False)
        self.magnet_timer = 0  
        self.stuck_balls = []   
        self.slow_active = params.get("slow_active", False)
        self.slow_timer = 0  

        self.level = params["level"]
        self.score = params["score"]
        self.lives = params["lives"]
        self.paddle = params["paddle"]
        self.balls = params["balls"]
        self.brickset = params["brickset"]
        self.live_factor = params["live_factor"]
        self.points_to_next_live = params["points_to_next_live"]
        self.points_to_next_grow_up = (
            self.score
            + settings.PADDLE_GROW_UP_POINTS * (self.paddle.size + 1) * self.level
        )
        self.powerups = params.get("powerups", [])
        
        self.powerups_array = [
            "CannonBalls",
            "TwoMoreBall",
            "StickPower",
            "SlowMotion",
            
        ]

        if not params.get("resume", False):
            self.balls[0].vx = random.randint(-80, 80)
            self.balls[0].vy = random.randint(-170, -100)
            settings.SOUNDS["paddle_hit"].play()

        if self.cannon_active == True:
            self.paddle.has_cannons = True
            
        self.powerups_abstract_factory = AbstractFactory("src.powerups")

    def update(self, dt: float) -> None:
        self.paddle.update(dt)

        if self.cannon_active == False:
            self.paddle.has_cannons = False

        # Timer StickPower   
        if self.magnet_active:
            self.magnet_timer -= dt
            if self.magnet_timer <= 0:
                self.magnet_active = False
                self.magnet_timer = 0
                for ball, _ in self.stuck_balls:
                        ball.vx = random.randint(-80, 80)
                        ball.vy = -random.randint(120, 160)
                self.stuck_balls.clear()

        # Timer and activation SlowMotion 
        if self.slow_active: 
            for ball in self.balls:
                ball.speed_factor = 0.5            
            self.slow_timer -= dt          
            if self.slow_timer <= 0:
                self.slow_active = False
                self.slow_timer = 0
                for ball in self.balls:
                    ball.speed_factor = 1   


        for cannoball in self.cannonBalls:
            cannoball.update(dt)
            
            brick = self.brickset.get_colliding_brick(cannoball.get_collision_rect())

            if brick is None:
                continue
            
            brick.hit()
            self.score += brick.score()
    
            cannoball.in_play = False
            
        self.cannonBalls = [cannonBall for cannonBall in self.cannonBalls if cannonBall.in_play]
        
        for ball in self.balls:
            ball.update(dt)
            ball.solve_world_boundaries()

            # Check collision with the paddle
            if ball.collides(self.paddle):
                settings.SOUNDS["paddle_hit"].stop()
                settings.SOUNDS["paddle_hit"].play()
    
                if self.magnet_active and ball not in [b for b, _ in self.stuck_balls]:
                   ball.vx = 0
                   ball.vy = 0
                   ball.y = self.paddle.y - ball.height

                   offset_x = ball.x - self.paddle.x
                   self.stuck_balls.append((ball,offset_x))
                else:
                    ball.rebound(self.paddle)
                    ball.push(self.paddle)

            if ball not in [b for b, _ in self.stuck_balls]:
                if ball.collides(self.paddle):
                    brick = self.brickset.get_colliding_brick(ball.get_collision_rect())
                    if brick is None:
                        brick.hit()
                        self.score += brick.score()
                        ball.rebound(brick)


            # for ball, offset_x in self.stuck_balls:
            #     ball.x = self.paddle.x + offset_x
            #     ball.y = self.paddle.y - ball.height

            # Check collision with brickset
            if not ball.collides(self.brickset):
                continue

            brick = self.brickset.get_colliding_brick(ball.get_collision_rect())

            if brick is None:
                continue

            brick.hit()
            self.score += brick.score()
            ball.rebound(brick)

            # Check earn life
            if self.score >= self.points_to_next_live:
                settings.SOUNDS["life"].play()
                self.lives = min(3, self.lives + 1)
                self.live_factor += 0.5
                self.points_to_next_live += settings.LIVE_POINTS_BASE * self.live_factor

            # Check growing up of the paddle
            if self.score >= self.points_to_next_grow_up:
                settings.SOUNDS["grow_up"].play()
                self.points_to_next_grow_up += (
                    settings.PADDLE_GROW_UP_POINTS * (self.paddle.size + 1) * self.level
                )
                self.paddle.inc_size()

           
            if random.random() < 1:
                r = brick.get_collision_rect()
                
               
                power = random.choice(self.powerups_array)
                self.powerups.append(
                    self.powerups_abstract_factory.get_factory(power).create(
                        r.centerx - 8, r.centery - 8
                    )
                )

        for ball, offset_x in self.stuck_balls:
            ball.x = self.paddle.x + offset_x
            ball.y = self.paddle.y - ball.height
        # Removing all balls that are not in play
        self.balls = [ball for ball in self.balls if ball.active]

        self.brickset.update(dt)

        if not self.balls:
            self.lives -= 1
            if self.lives == 0:
                self.state_machine.change("game_over", score=self.score)
            else:
                self.paddle.dec_size()
                self.cannon_active = False
                self.cannon_ammo = 0
                self.paddle.has_cannons = False
                self.state_machine.change(
                    "serve",
                    level=self.level,
                    score=self.score,
                    lives=self.lives,
                    paddle=self.paddle,
                    brickset=self.brickset,
                    points_to_next_live=self.points_to_next_live,
                    live_factor=self.live_factor,
                )

        # Update powerups
        for powerup in self.powerups:
            powerup.update(dt)

            if powerup.collides(self.paddle):
                powerup.take(self)

        # Remove powerups that are not in play
        self.powerups = [p for p in self.powerups if p.active]

        # Check victory
        if self.brickset.size == 1 and next(
            (True for _, b in self.brickset.bricks.items() if b.broken), False
        ):
            self.cannon_active = False
            self.cannon_ammo = 0
            self.paddle.has_cannons = False
            
            self.state_machine.change(
                "victory",
                lives=self.lives,
                level=self.level,
                score=self.score,
                paddle=self.paddle,
                balls=self.balls,
                points_to_next_live=self.points_to_next_live,
                live_factor=self.live_factor,
            )

    def render(self, surface: pygame.Surface) -> None:
        heart_x = settings.VIRTUAL_WIDTH - 120

        i = 0
        # Draw filled hearts
        while i < self.lives:
            surface.blit(
                settings.TEXTURES["hearts"], (heart_x, 5), settings.FRAMES["hearts"][0]
            )
            heart_x += 11
            i += 1

        # Draw empty hearts
        while i < 3:
            surface.blit(
                settings.TEXTURES["hearts"], (heart_x, 5), settings.FRAMES["hearts"][1]
            )
            heart_x += 11
            i += 1

        render_text(
            surface,
            f"Shots: {self.cannon_ammo}  ",
            settings.FONTS["tiny"],
            settings.VIRTUAL_WIDTH - 190,
            5,
            (255, 255, 255),
        )
        
        render_text(
            surface,
            f"Score: {self.score}",
            settings.FONTS["tiny"],
            settings.VIRTUAL_WIDTH - 80,
            5,
            (255, 255, 255),
        )

        self.brickset.render(surface)

        self.paddle.render(surface)

        for ball in self.balls:
            ball.render(surface)

        for powerup in self.powerups:
            powerup.render(surface)
            
        for cannonBall in self.cannonBalls:
            cannonBall.render(surface)

    def on_input(self, input_id: str, input_data: InputData) -> None:

        if input_id == "move_left":
            if input_data.pressed:
                self.paddle.vx = -settings.PADDLE_SPEED
            elif input_data.released and self.paddle.vx < 0:
                self.paddle.vx = 0
        elif input_id == "move_right":
            if input_data.pressed:
                self.paddle.vx = settings.PADDLE_SPEED
            elif input_data.released and self.paddle.vx > 0:
                self.paddle.vx = 0
        elif input_id == "shoot" and input_data.pressed:
            Shoots.shoot_cannon(self)
        elif input_id == "pause" and input_data.pressed:
  
            if self.stuck_balls:
                for ball, _ in self.stuck_balls:
                        ball.vx = random.randint(-80, 80)
                        ball.vy = -random.randint(120, 160)
                self.stuck_balls.clear()
            else:
                self.state_machine.change(
                "pause",
                level=self.level,
                score=self.score,
                lives=self.lives,
                paddle=self.paddle,
                balls=self.balls,
                brickset=self.brickset,
                points_to_next_live=self.points_to_next_live,
                live_factor=self.live_factor,
                powerups=self.powerups,
                cannonBalls=self.cannonBalls,
                cannon_active=self.cannon_active,
                cannon_ammo=self.cannon_ammo,
                magnet_active=self.magnet_active,
                magnet_timer=self.magnet_timer,
                stuck_balls=self.stuck_balls 
            )
     
                    
