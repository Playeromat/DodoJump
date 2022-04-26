import pygame

from SETTINGS import SETTINGS


class WindowHandler:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("")
        self.WINDOW = pygame.display.set_mode((SETTINGS.GAME_WIDTH, SETTINGS.GAME_HEIGHT))

    def draw_window(self, player, obstacles):
        self.WINDOW.fill(SETTINGS.BG_COLOUR)

        player_pos = player.get_pos()
        player_rect = pygame.Rect(player_pos[0], player_pos[1], SETTINGS.PLAYER_WIDTH, SETTINGS.PLAYER_HEIGHT)
        pygame.draw.rect(self.WINDOW, SETTINGS.PLAYER_COLOUR, player_rect)

        for obstacle in obstacles:
            obstacle_pos = obstacle.get_pos()
            obstacle_rect = pygame.Rect(obstacle_pos[0], obstacle_pos[1], obstacle.width, obstacle.height)
            pygame.draw.rect(self.WINDOW, SETTINGS.PLAYER_COLOUR, obstacle_rect)

        pygame.display.update()

    def create_obstacle(self):
        pass
