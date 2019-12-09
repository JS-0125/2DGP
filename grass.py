from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('resourse/background.png')
        self.y = 3000
        self.delY = 0


    def update(self):
        self.y += self.delY

    def update1(self, delY):
        self.y -= delY

    def draw(self):
        print(self.y)
        self.image.draw(280, 2600 - int(self.y))
