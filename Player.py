from SETTINGS import SETTINGS


class Player:
    vel = 0
    pos = SETTINGS.PLAYER_POS[:]

    def __init__(self):
        self.vel = 0
        self.pos = SETTINGS.PLAYER_POS
        self.width = SETTINGS.PLAYER_WIDTH
        self.height = SETTINGS.PLAYER_HEIGHT

    def move(self):
        if self.pos[1] + self.vel > SETTINGS.GROUND - self.height:
            self.pos[1] = SETTINGS.GROUND - self.height
        else:
            self.pos[1] += self.vel

    def get_pos(self):
        return self.pos

    def get_vel(self):
        return self.vel

    def set_vel(self, _vel):
        self.vel = _vel
