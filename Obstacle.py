from SETTINGS import SETTINGS


class Obstacle:

    def __init__(self, _height, _width, _spacing):
        self.pos = [SETTINGS.GAME_WIDTH + _spacing, SETTINGS.GROUND - _height]
        self.height = _height
        self.width = _width

    def move(self):
        self.pos[0] -= SETTINGS.OBSTACLE_VEL

    def get_pos(self):
        return self.pos
