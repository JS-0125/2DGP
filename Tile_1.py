import game_world
from pico2d import *
import title_state
import game_framework

class Tile:
    image = None

    def __init__(self):
        if Tile.image == None:
            Tile.image = load_image('tile_2.png')
        self.x, self.y = 0,0

    def draw(self):
        self.image.draw(self.x, self.y, 95, 95)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 42.5, self.y - 42.5, self.x + 42.5, self.y + 42.5

    def update(self):
        pass
