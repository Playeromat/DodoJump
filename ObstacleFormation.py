from ObstacleType import ObstacleType


class ObstacleFormation:
    # OBSTACLE FORMATIONS
    SINGLE_LOW = 0
    SINGLE_HIGH = 1
    SNAKE = 10
    CAMEL = 11
    DUMB = 99

    @staticmethod
    def get_obstacle_formations():
        return ObstacleFormation.SINGLE_LOW, \
               ObstacleFormation.SINGLE_HIGH, \
               ObstacleFormation.SNAKE, \
               ObstacleFormation.CAMEL, \
               ObstacleFormation.DUMB

    def __init__(self, _formation):
        self.obstacle_types = []
        # self.OBSTACLE_LOW_THIN = ObstacleType(ObstacleType.OBSTACLE_LOW_THIN)
        # self.OBSTACLE_LOW_WIDE = ObstacleType(ObstacleType.OBSTACLE_LOW_WIDE)
        # self.OBSTACLE_HIGH_THIN = ObstacleType(ObstacleType.OBSTACLE_HIGH_THIN)
        # self.OBSTACLE_HIGH_WIDE = ObstacleType(ObstacleType.OBSTACLE_HIGH_WIDE)

        if _formation == ObstacleFormation.SINGLE_LOW:
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_LOW_THIN))
        if _formation == ObstacleFormation.SINGLE_HIGH:
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_HIGH_THIN))
        if _formation == ObstacleFormation.SNAKE:
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_HIGH_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_LOW_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_HIGH_THIN))
        if _formation == ObstacleFormation.CAMEL:
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_LOW_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_HIGH_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_LOW_THIN))
        if _formation == ObstacleFormation.DUMB:
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_LOW_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_HIGH_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_LOW_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_HIGH_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_LOW_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_HIGH_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_LOW_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_HIGH_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_LOW_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_HIGH_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_LOW_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_HIGH_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_LOW_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_HIGH_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_LOW_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_HIGH_THIN))
            self.obstacle_types.append(ObstacleType(ObstacleType.OBSTACLE_LOW_THIN))

    def get_obstacle_types(self):
        return self.obstacle_types
