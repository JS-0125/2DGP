from pico2d import *

class Enemy:
    def __init__(self, x,  y):
        self. monsterDelX, self.x = 0, x
        self.monsterFrameX = 0
        self.y = y
        self.image = load_image('resourse/monster1.png')

    def update(self):
        if (self.x >= 400):
            self.monsterDelX = -2
        elif (self.x <= 200):
            self.monsterDelX = 2
        self.monsterFrameX = (self.monsterFrameX + 1) % 6
        self.x += self.monsterDelX


    def draw(self):
        self.image.clip_draw(self.monsterFrameX * 360 , 0 , 360, 360, self.x, 300, 100, 100)

    def get_bb(self):
        return self.x - 35 , 250, self.x + 35, 300