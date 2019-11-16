from pico2d import *

class Inventory:
    def __init__(self):
        self.image = load_image('resourse/inventory.png')
        self.y = 1400
        self.bag = []
        self.money = 0
        self.got_crystal_count = 0

    def update(self):
        pass

    def draw(self):
        self.image.draw(280, 400, 560, 800)

    def click(self):
        
