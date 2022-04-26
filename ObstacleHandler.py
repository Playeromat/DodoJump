import random

from Obstacle import Obstacle
from ObstacleFormation import ObstacleFormation


class ObstacleHandler:

    def __init__(self):
        self.obstacles = []
        self.obstacle_formations = ObstacleFormation.get_obstacle_formations()

    def tick(self):
        self.move()
        self.cleanup()

        if not self.obstacles:
            rand_formation = random.randint(0, len(self.obstacle_formations) - 1)
            self.create_obstacle_formation(self.obstacle_formations[rand_formation])

    def cleanup(self):
        for obstacle in self.obstacles:
            if obstacle.get_pos()[0] <= (0 - obstacle.width):
                self.obstacles.remove(obstacle)

    def create_obstacle_formation(self, _formation):
        obstacle_formation = ObstacleFormation(_formation)
        obstacle_types = obstacle_formation.get_obstacle_types()

        spacing = 0

        for obstacle_type in obstacle_types:
            obstacle_width, obstacle_height = obstacle_type.get_size()

            self.obstacles.insert(0, Obstacle(obstacle_height, obstacle_width, spacing))
            spacing += obstacle_width * 2

    def move(self):
        for obstacle in self.obstacles:
            obstacle.move()

    def get_obstacles(self):
        return self.obstacles
