import math
import time

import pygame
import pygameFpsCounter.FpsCounterSlim

from ObstacleFormation import ObstacleFormation
from ObstacleHandler import ObstacleHandler
from Player import Player
from SETTINGS import SETTINGS
from WindowHandler import WindowHandler


class Game:
    PLAYERTICKEVENT = pygame.USEREVENT + 1
    OBSTACLETICKEVENT = pygame.USEREVENT + 2

    def __init__(self):
        self.window_handler = WindowHandler()
        self.player = Player()
        self.obstacle_handler = ObstacleHandler()

        self.game_loop()

    def game_loop(self):
        keep_running = True

        self.obstacle_handler.create_obstacle_formation(ObstacleFormation.SINGLE_LOW)

        fps = SETTINGS.FPS
        fps_clock = pygame.time.Clock()

        self.set_timers()

        jump_time = 0
        jump_pressed = False

        fps_counter = pygameFpsCounter.FpsCounterSlim.FpsCounterSlim(self.window_handler.WINDOW)

        while keep_running:
            fps_clock.tick(fps)

            self.window_handler.draw_window(self.player, self.obstacle_handler.get_obstacles())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keep_running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jump_pressed = True  # time.time()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        jump_released = time.time()
                        jump_time = jump_released - jump_pressed

                if event.type == Game.PLAYERTICKEVENT:
                    self.player_tick(jump_pressed)
                    jump_pressed = False

                if event.type == Game.OBSTACLETICKEVENT:
                    self.obstacle_tick()

            fps_counter.render_fps()
            pygame.display.flip()

        pygame.quit()

    def set_timers(self):
        player_tick_s = SETTINGS.PLAYER_TICK
        obstacle_tick_s = SETTINGS.OBSTACLE_TICK
        player_tick_ms = math.ceil(1000 / player_tick_s)
        obstacle_tick_ms = math.ceil(1000 / obstacle_tick_s)

        pygame.time.set_timer(Game.PLAYERTICKEVENT, player_tick_ms)
        pygame.time.set_timer(Game.OBSTACLETICKEVENT, obstacle_tick_ms)

    def player_tick(self, _jump_time):
        self.player.set_vel(self.player.get_vel() + SETTINGS.GRAVITY)

        if _jump_time:
            self.player.set_vel(-SETTINGS.JUMP_VEL)

        self.player.move()

    def obstacle_tick(self):
        self.obstacle_handler.tick()


