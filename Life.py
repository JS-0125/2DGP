from pico2d import *

class Life:
    def __init__(self):
        self.image = load_image('resourse/life.png')
        self.count = 3

    def update(self):
        for i in range(self.count):
            self.image.draw(210 + i * 70, 750, 50, 50)

    def draw(self):
        for i in range(self.count):
            self.image.draw(210 + i * 70, 750, 50, 50)