from pico2d import *

class Crystal:
    def __init__(self):
        self.frame = 0
        self.image = load_image('resourse/crystal.png')
        self.x = 139.5
        self.y = 300

    def update(self):
        self.frame = (self.frame + 1) % 6

    def draw(self):
        self.image.clip_draw(self.frame * 66, 0, 66, 100, self.x, self.y)

    def get_bb(self):
        return self.x - 33 , self.y - 50, self.x + 33, self.y + 50