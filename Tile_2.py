from pico2d import *

class Tile_2:
    image = None

    def __init__(self):
        if Tile_2.image == None:
            Tile_2.image = load_image('resourse/tile_1.png')
        self.x, self.y = 0, 0

    def draw(self):
        self.image.draw(self.x, self.y, 95, 95)

    def get_bb(self):
        return self.x - 42.5, self.y - 42.5, self.x + 42.5, self.y + 42.5

    def update(self):
        pass
