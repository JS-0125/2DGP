from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('resourse/background.png')
        self.y = 1400
        self.delY = -8

    def update(self):
        self.y += self.delY

    def update1(self, delY):
        self.y += delY

    def draw(self):
        self.image.clip_draw(0, self.y, 575 , 800, 280, 400)


