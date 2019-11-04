from pico2d import *

class Crystal:
    def __init__(self):
        self.image = load_image('resourse/crystal.png')

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 30 , 17, 30, 280,100)