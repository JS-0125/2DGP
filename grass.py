from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('20180417022947-1-576x1024.jpg')
    def update(self):
        pass
    def draw(self):
        self.image.draw(280, 512)