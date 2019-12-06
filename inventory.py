from pico2d import *
from crystal import Crystal
import character

class Inventory:
    def __init__(self):
        self.image = load_image('resourse/inventory.png')
        self.my_bag = []
        self.money = 0
        self.buy_sound = load_wav('resourse/buy.wav')
        self.buy_sound.set_volume(64)
        self.sell_sound = load_wav('resourse/sell.wav')
        self.sell_sound.set_volume(64)
        self.speed = 1

    def update(self):
        pass

    def draw(self):
        count_tmp = 0
        self.image.draw(280, 400, 560, 800)
        for i in self.my_bag:
            if i == 'crystal':
                if count_tmp < 3:
                    Crystal(0, 0).image.clip_draw(0, 0, 66, 100, 120 + 155 * count_tmp, 310)
                else:
                    Crystal(0, 0).image.clip_draw(0, 0, 66, 100, 120 + 155 * (count_tmp - 3), 310 - 200)
                count_tmp += 1

    def click(self, x, y):
        # buy
        if 40 < x < 200 and 590 < y < 615:
            self.buy_sound.play()
            if self.money >= 1000:
                self.buy(1000)
                self.speed += 0.1
        elif 200 < x < 360 and 590 < y < 615:
            self.buy_sound.play()
            if self.money >= 1000:
                self.buy(1000)
        elif 360 < x < 515 and 590 < y < 615:
            self.buy_sound.play()
            pass

        # sell
        if 40 < x < 200 and 235 < y < 260:
            self.sell_sound.play()
            if len(self.my_bag) >= 1:
                self.sell(0)
                self.my_bag.remove(self.my_bag[0])
        elif 200 < x < 360 and 235 < y < 260:
            self.sell_sound.play()
            if len(self.my_bag) >= 2:
                self.sell(1)
                self.my_bag.remove(self.my_bag[1])
        elif 360 < x < 515 and 235 < y < 260:
            self.sell_sound.play()
            if len(self.my_bag) >= 3:
                self.sell(2)
                self.my_bag.remove(self.my_bag[2])
        elif 40 < x < 200 and 35 < y < 60:
            self.sell_sound.play()
            if len(self.my_bag) >= 4:
                self.sell(3)
                self.my_bag.remove(self.my_bag[3])
        elif 200 < x < 360 and 35 < y < 60:
            self.sell_sound.play()
            if len(self.my_bag) >= 5:
                self.sell(4)
                self.my_bag.remove(self.my_bag[4])
        elif 360 < x < 515 and 35 < y < 60:
            self.sell_sound.play()
            if len(self.my_bag) >= 6:
                self.sell(5)
                self.my_bag.remove(self.my_bag[5])

    def sell(self, i):
        if self.my_bag[i] == 'crystal':
            self.money += 10000

    def buy(self, item_price):
        self.money -= item_price