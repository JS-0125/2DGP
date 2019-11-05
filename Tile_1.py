import game_world
from pico2d import *
import title_state
import game_framework

class Tile:
    def __init__(self, x, y, mode):
        if mode == 1:
            self.image = load_image('resourse/tile_2.png')
        else:
            self.image = load_image('resourse/tile_1.png')
        self.x, self.y = x, y
        self.delY = 0

    def draw(self):
        self.image.draw(self.x, self.y, 95, 95)

    def update(self):
        self.y += self.delY

    def get_bb(self):
        return self.x - 42.5, self.y - 42.5, self.x + 42.5, self.y + 42.5