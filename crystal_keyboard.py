from pico2d import *

import random
import game_framework

image_up = load_image('resourse/arrow_up.png')
image_down = load_image('resourse/arrow_down.png')
image_right = load_image('resourse/arrow_right.png')
image_left = load_image('resourse/arrow_left.png')

keyboard_input_list = []
keyboard_check_list = []
keyboard_default_list = {0: image_up, 1: image_down, 2: image_right, 3: image_left}

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
        for i in keyboard_input_list:
            tmp = keyboard_default_list[i]
            tmp.clip_draw(200, 0, 200, 200, 280, 600)
    else:
        pass

def draw():
    for i in keyboard_input_list:
        tmp = keyboard_default_list[i]
        tmp.clip_draw(0,0,200,200,280,600)
