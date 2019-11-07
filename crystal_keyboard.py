from pico2d import *

import random
import game_framework

image = None
keyboard_input_list = []
keyboard_check_list = []

for i in range(5):
    keyboard_input_list.append(random(4))

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_UP:
            keyboard_check_list.append(0)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_DOWN:
            keyboard_check_list.append(1)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            keyboard_check_list.append(2)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            keyboard_check_list.append(3)

def update():
    if keyboard_input_list == keyboard_check_list:
        pass
    else:
        pass

def draw():
    for i in keyboard_input_list:
        if i == 0:
            pass
        elif i == 1:
            pass
        elif i == 2:
            pass
        elif i == 3:
            pass
