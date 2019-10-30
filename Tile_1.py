import game_world
from pico2d import *
import title_state
import game_framework

class Tile:
    image = None

    def __init__(self):
        if Tile.image == None:
            Tile.image = load_image('tile_2.png')
        self.x, self.y = 300, 100

    def draw(self):
        self.image.draw(self.x, self.y,100,100)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
