from pico2d import *
import main_state

class Enemy:
    def __init__(self, x,  y):
        self. monsterDelX, self.x = 2, x
        self.monsterFrameX = 0
        self.y = y
        self.delY = 0
        self.image = load_image('resourse/monster1.png')

    def update(self):
        self.x += self.monsterDelX
        self.y += self.delY

        if (self.x >= 450):
            self.monsterDelX = -2
        elif (self.x <= 120):
            self.monsterDelX = 2
        self.monsterFrameX = (self.monsterFrameX + 1) % 6

    def draw(self):
        self.image.clip_draw(self.monsterFrameX * 360 , 0 , 360, 360, self.x, int(self.y - main_state.grass.y), 100, 100)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30 , int(self.y - main_state.grass.y) - 50, self.x + 30, int(self.y - main_state.grass.y) + 10