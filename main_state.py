import random
import json
import os

from pico2d import *

import game_world
import game_framework

from character import Chatacter
from grass import Grass
from Tile_1 import Tile
from Tile_2 import Tile_2

import title_state

name = "MainState"

character = None
grass = None
enemy1 = None
tile1 = None
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
    global character, grass, enemy1, tile1, tile2
    xpos = [139.5, 139.5, 139.5, 234.5, 234.5, 234.5, 234.5, 234.5, 329.5, 329.5, 329.5, 329.5, 424, 424, 424, 424]
    ypos = [1500, 1000, 900, 1500, 1000, 1000, 500, 1000, 1500 ,900, 500, 200, 1200, 900, 500, 200]

    character = Chatacter()
    grass = Grass()
    enemy1 = Enemy()
    game_world.add_object(grass, 0)
    game_world.add_object(character, 1)

    tile1 = [Tile() for i in range(16)]
    for i in range(16):
        tile1[i].x = xpos[i]
        tile1[i].y = ypos[i]
    game_world.add_objects(tile1, 1)

    xpos = [139.5, 139.5, 139.5,234.5,0,0,0,0,0,0,0,0,0,0,0,0]
    ypos = [200, 500,400,200,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000,1000]
    tile2 = [Tile_2() for i in range(16)]
    for i in range(16):
        tile2[i].x = xpos[i]
        tile2[i].y = ypos[i]
    game_world.add_objects(tile2, 2)


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

    for tile in tile1:
        if collide(tile, character):
            character.stop()
            break
        else:
            character.dirY = -5

    for tile in tile2:
        if collide(tile, character):
            character.stop()



def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    delay(0.01)

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True



