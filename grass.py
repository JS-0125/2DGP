from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('background.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(280, -100)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 0, 0, 90, 1800