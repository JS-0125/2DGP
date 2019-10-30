from pico2d import *

class Enemy:
    def __init__(self):
        self. monsterDelX, self.monsterX = 0, 100
        self.monsterFrameX = 0
        self.image = load_image('monster1.png')

    def update(self):
        if (self.monsterX >= 200):
            self.monsterDelX = -2
        elif (self.monsterX <= 100):
            self.monsterDelX = 2
        self.monsterFrameX = (self.monsterFrameX + 1) % 28
        self.monsterX += self.monsterDelX

    def draw(self):
        self.image.clip_draw(self.monsterFrameX * 201 , 0 , 240 , 230, self.monsterX, 300, 100, 100)