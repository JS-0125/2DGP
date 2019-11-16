from pico2d import *
from crystal import Crystal

import random
import game_framework
import main_state

name = "CrystalState"

image_up = None
image_down = None
image_right = None
image_left = None
frameX = 0

keyboard_input_list = []
keyboard_check_list = []
keyboard_default_list = []


def enter():
    global image_up, image_down, image_right, image_left, keyboard_input_list, keyboard_default_list, frameX

    for i in range(5):
        keyboard_input_list.append(random.randrange(0,4))

    image_up = load_image('resourse/arrow_up.png')
    image_down = load_image('resourse/arrow_down.png')
    image_right = load_image('resourse/arrow_right.png')
    image_left = load_image('resourse/arrow_left.png')

    keyboard_default_list.append(image_up)
    keyboard_default_list.append(image_down)
    keyboard_default_list.append(image_right)
    keyboard_default_list.append(image_left)

    frameX = 0
    main_state.draw()


def exit():
    global image_up, image_down, image_right, image_left, frameX
    del(image_up)
    del(image_down)
    del(image_right)
    del(image_left)
    del(frameX)
    keyboard_input_list.clear()
    keyboard_check_list.clear()
    keyboard_default_list.clear()


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
    global frameX
    if keyboard_input_list == keyboard_check_list:
        main_state.inventory.my_bag.append(Crystal(0,0))
        frameX = 200
        draw()
        delay(0.5)
        game_framework.pop_state()
    else:
        pass


def draw():
    interval = 0
    for i in keyboard_input_list:
        keyboard_default_list[i].clip_draw(frameX, 0, 200, 200, 70 + interval, 600, 100, 100)
        interval += 105
    update_canvas()