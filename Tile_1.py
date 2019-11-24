import game_world
from pico2d import *
import title_state
import game_framework
import grass
import main_state

class Tile:
    def __init__(self, x, y, mode):
        self.mode = mode
        if mode == 1:
            self.image = load_image('resourse/tile_2.png')
        else:
            self.image = load_image('resourse/tile_1.png')
        self.x, self.y = x, y
        self.delY = 0

    def draw(self):
        self.image.draw(self.x, self.y - main_state.grass.y, 95, 95)
        draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_bb_tile_side())

    def draw1(self, Real):
        self.image.draw(self.x, self.y - Real, 95, 95)

    def update(self):
        pass

    def update1(self, delY):
        self.y += delY

    def get_bb(self):
      return self.x - 47.5, self.y - main_state.grass.y + 30 , self.x + 47.5, self.y - main_state.grass.y + 47.5

    def get_bb_tile_side(self):
      return self.x - 47.5, self.y - main_state.grass.y - 10 , self.x + 47.5, self.y - main_state.grass.y