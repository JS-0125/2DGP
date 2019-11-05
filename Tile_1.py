import game_world
from pico2d import *
import title_state
import game_framework

class Tile:
    image = None

    def __init__(self, x, y):
        if Tile.image == None:
            Tile.image = load_image('resourse/tile_2.png')
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y, 95, 95)

    def get_bb(self):
        return self.x - 42.5, self.y - 42.5, self.x + 42.5, self.y + 42.5

    def update(self):
        pass
