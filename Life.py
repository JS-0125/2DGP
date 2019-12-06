from pico2d import *
from character import Chatacter
import main_state

class Life:
    def __init__(self):
        self.image = load_image('resourse/life.png')
        self.count = 3
        self.timer = 0

    def update(self):
        for i in range(self.count):
            self.image.draw(210 + i * 70, 750, 50, 50)
        self.timer -= 1
        if self.timer < 0:
            main_state.character.size = 160


    def draw(self):
        for i in range(self.count):
            self.image.draw(210 + i * 70, 750, 50, 50)

    def stop(self):
        print(self.timer)
        if self. timer <= 0:
            self.count -= 1
            self.timer = 120
            main_state.character.size = 190