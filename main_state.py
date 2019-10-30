import random
import json
import os

from pico2d import *

import game_framework
import title_state

name = "MainState"

character = None
grass = None
enemy1 = None

class Grass:
    def __init__(self):
        self.image = load_image('20180417022947-1-576x1024.jpg')

    def draw(self):
        self.image.draw(280, 512)

class Chatacter:
    def __init__(self):
        self.x, self.y = 0, 0
        self.frameX, self.frameY = 0, 4
        self.image = load_image('character.png')
        self.dir = 0

    def update(self):
        if (self.frameY == 4):
            self.frameX = (self.frameX + 1) % 4
            self.x += self.dir * 10
        elif(self.frameY == 6):
            self.frameX = (self.frameX - 1) % 4
            self.x += self.dir * 10
        elif (self.frameY == 0):
            self.frameX = (self.frameX + 1) % 19
            if (self.frameX == 0):
                self.frameY = 3
                self.frameX = 2
        elif(self.frameY == 7):
            self.frameX = (self.frameX - 1) % 19
            if (self.frameX == 0):
                self.frameY = 3
                self.frameX = 2

    def draw(self):
        if (self.frameY == 4 or self.frameY == 6 or self.frameY ==3):
            self.image.clip_draw(self.frameX * 360, self.frameY * 360, 360, 360, self.x, 500,200,200)
        elif (self.frameY == 0 or self.frameY == 7):
            self.image.clip_draw(self.frameX * 365, self.frameY * 360, 360, 360, self.x, 500,200,200)

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
    global character, grass, enemy1
    character = Chatacter()
    grass = Grass()
    enemy1 = Enemy()


def exit():
    global character, grass, enemy1
    del(character)
    del(grass)
    del(enemy1)


def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.change_state(title_state)
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                character.dir += 1
                character.frameX = 0
                character.frameY = 4
            elif event.key == SDLK_LEFT:
                character.dir -= 1
                character.frameX = 0
                character.frameY = 6
            elif event.key == SDLK_a:
                if(character.dir == 1):
                    character.frameY = 0
                elif(character.dir == -1):
                    character.frameY = 7
                    character.frameX = 19
            elif event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                character.dir -= 1
                character.frameX = 2
                character.frameY = 3
            elif event.key == SDLK_LEFT:
                character.dir += 1
                character.frameX = 2
                character.frameY = 3

def update():
    character.update()
    enemy1.update()


def draw():
    clear_canvas()
    grass.draw()
    character.draw()
    enemy1.draw()
    update_canvas()
    delay(0.02)





