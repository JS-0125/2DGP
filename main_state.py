import random
import json
import os

from pico2d import *

import game_world
import game_framework

from character import Chatacter
from grass import Grass
from Tile_1 import Tile


import title_state

name = "MainState"

character = None
grass = None
enemy1 = None
tile1 = None

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

def enter():
    global character, grass, enemy1, tile1
    character = Chatacter()
    grass = Grass()
    enemy1 = Enemy()
    tile1 = Tile()
    game_world.add_object(grass, 0)
    game_world.add_object(character, 1)
    game_world.add_object(tile1, 2)


def exit():
    game_world.clear()


def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            character.handle_event(event)

def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    delay(0.02)





