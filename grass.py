from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('resourse/background.png')
        self.y = 1700
        self.delY = 0
        self.bgm = load_music('resourse/dodadag_main_bgm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def update(self):
        self.y += self.delY

    def update1(self, delY):
        self.y -= delY

    def draw(self):
        self.image.clip_draw(0, int(self.y), 575 , 800, 280, 400)