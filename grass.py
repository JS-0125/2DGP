from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('resourse/background.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(280, -100)