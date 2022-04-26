from SETTINGS import SETTINGS


class ObstacleType:
    # OBSTACLE TYPES
    OBSTACLE_LOW_THIN = 0
    OBSTACLE_LOW_WIDE = 1
    OBSTACLE_HIGH_THIN = 2
    OBSTACLE_HIGH_WIDE = 3

    @staticmethod
    def get_obstacle_types():
        return ObstacleType.OBSTACLE_LOW_THIN, \
               ObstacleType.OBSTACLE_LOW_WIDE, \
               ObstacleType.OBSTACLE_HIGH_THIN, \
               ObstacleType.OBSTACLE_HIGH_WIDE

    def __init__(self, _type):
        self.width = 0
        self.height = 0

        if _type == ObstacleType.OBSTACLE_LOW_THIN:
            self.width = SETTINGS.OBSTACLE_THIN
            self.height = SETTINGS.OBSTACLE_LOW
        if _type == ObstacleType.OBSTACLE_LOW_WIDE:
            self.width = SETTINGS.OBSTACLE_WIDE
            self.height = SETTINGS.OBSTACLE_LOW
        if _type == ObstacleType.OBSTACLE_HIGH_THIN:
            self.width = SETTINGS.OBSTACLE_THIN
            self.height = SETTINGS.OBSTACLE_HIGH
        if _type == ObstacleType.OBSTACLE_HIGH_WIDE:
            self.width = SETTINGS.OBSTACLE_WIDE
            self.height = SETTINGS.OBSTACLE_HIGH

    def get_size(self):
        return self.width, self.height
