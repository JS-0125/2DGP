from pico2d import *
import crystal

class Inventory:
    def __init__(self):
        self.image = load_image('resourse/inventory.png')
        self.y = 1400
        self.my_bag = []
        self.money = 0
        self.got_crystal_count = 0

    def update(self):
        pass

    def draw(self):
        self.image.draw(280, 400, 560, 800)

    def click(self, x, y):
        # buy
        if 40 < x < 200 and 590 < y < 615:
            if self.money >= 1000:
                self.money -= 1000
        elif 200 < x < 360 and 590 < y < 615:
            if self.money >= 1000:
                self.money -= 1000
        elif 360 < x < 515 and 590 < y < 615:
            pass

        # sell
        if 40 < x < 200 and 235 < y < 260:
            if len(self.my_bag) >= 1:
                self.sell(0)
        elif 200 < x < 360 and 235 < y < 260:
            if len(self.my_bag) >= 2:
                self.sell(1)
        elif 360 < x < 515 and 235 < y < 260:
            if len(self.my_bag) >= 3:
                self.sell(2)
        elif 40 < x < 200 and 35 < y < 60:
            if len(self.my_bag) >= 4:
                self.sell(3)
        elif 200 < x < 360 and 35 < y < 60:
            if len(self.my_bag) >= 5:
                self.sell(4)
        elif 360 < x < 515 and 35 < y < 60:
            if len(self.my_bag) >= 6:
                self.sell(5)

    def sell(self, i):
        if self.my_bag[i] == crystal:
            self.money += 10000