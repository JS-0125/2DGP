from pico2d import *
import main_state


class Crystal:
    def __init__(self, x, y):
        self.frame = 0
        self.image = load_image('resourse/crystal.png')
        self.x = x
        self.y = y
        self.get_crystal = load_wav('resourse/get_crystal.wav')
        self.get_crystal.set_volume(64)
        self.fail_get_crystal = load_wav('resourse/fail_get_crystal.wav')
        self.fail_get_crystal.set_volume(64)

    def update(self):
        self.frame = (self.frame + 1) % 6

    def update1(self, DelY):
        self.frame = (self.frame + 1) % 6

    def draw1(self, DelY):
        self.image.clip_draw(self.frame * 66, 0, 66, 100, self.x, self.y - DelY)

    def draw(self):
        self.image.clip_draw(self.frame * 66, 0, 66, 100, self.x, self.y - main_state.grass.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 33 , self.y - main_state.grass.y - 50, self.x + 33, self.y - main_state.grass.y + 50