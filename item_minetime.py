from pico2d import *


class ItemMineTime:
    def __init__(self):
        self.image = load_image('resourse/background.png')
        self.y = 1400

    def update(self):
        pass

    def draw(self):
        self.image.draw(0, self.y, 575, 800)