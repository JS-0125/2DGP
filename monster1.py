from pico2d import *
import main_state
import game_framework

# Boy Run Speed
# fill expressions correctly
PIXEL_PER_METER = (10.0 / 0.2)
RUN_SPEED_KMPH = 8.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
# fill expressions correctly
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6

class Enemy:
    def __init__(self, x,  y):
        self. monsterDelX, self.x = 2, x
        self.monsterFrameX = 0
        self.y = y
        self.delY = 0
        self.image = load_image('resourse/monster1.png')

    def update(self):
        self.x += self.monsterDelX * RUN_SPEED_PPS * game_framework.frame_time
        self.y += self.delY

        if (self.x >= 450):
            self.monsterDelX = -1
        elif (self.x <= 120):
            self.monsterDelX = 1
        self.monsterFrameX = (self.monsterFrameX + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6

    def draw(self):
        self.image.clip_draw(int(self.monsterFrameX) * 360 , 0 , 360, 360, int(self.x), int(self.y - main_state.grass.y), 100, 100)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return int(self.x) - 30 , int(self.y - main_state.grass.y) - 50, int(self.x) + 30, int(self.y - main_state.grass.y) + 10