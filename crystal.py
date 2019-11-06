from pico2d import *
import main_state

class Crystal:
    def __init__(self, x, y):
        self.frame = 0
        self.image = load_image('resourse/crystal.png')
        self.x = x
        self.y = y

    def update(self):
        self.frame = (self.frame + 1) % 6

    def update1(self, DelY):
        self.frame = (self.frame + 1) % 6
        self. y += DelY

    def draw1(self, DelY):
        self.image.clip_draw(self.frame * 66, 0, 66, 100, self.x, self.y - DelY)

    def draw(self):
        self.image.clip_draw(self.frame * 66, 0, 66, 100, self.x, self.y - main_state.grass.y)

    def get_bb(self):
        return self.x - 33 , self.y - 50, self.x + 33, self.y + 50