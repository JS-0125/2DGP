from pico2d import *
import main_state

class Enemy:
    def __init__(self, x,  y):
        self. monsterDelX, self.x = 2, x
        self.monsterFrameX = 0
        self.y = y
        self.image = load_image('resourse/monster1.png')

    def update(self):
        if (self.x >= 400):
            self.monsterDelX = -2
        elif (self.x <= 150):
            self.monsterDelX = 2
        self.monsterFrameX = (self.monsterFrameX + 1) % 6
        self.x += self.monsterDelX

    def draw(self):
        self.image.clip_draw(self.monsterFrameX * 360 , 0 , 360, 360, self.x, int(self.y - main_state.grass.y), 100, 100)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 35 , self.y - main_state.grass.y - 50, self.x + 35, int(self.y - main_state.grass.y) + 10