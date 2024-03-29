from pico2d import *
from crystal import Crystal

import random
import game_framework
import main_state
import start_state

name = "CrystalState"

image_up = None
image_down = None
image_right = None
image_left = None
frameX = 0
time = 0
max_time = None

keyboard_input_list = []
keyboard_check_list = []
keyboard_default_list = []

count = 0

def enter():
    global image_up, image_down, image_right, image_left, keyboard_input_list, keyboard_default_list, frameX, max_time

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
    max_time = main_state.inventory.mining_time

    main_state.draw()

def exit():
    global image_up, image_down, image_right, image_left, frameX, time
    del(image_up)
    del(image_down)
    del(image_right)
    del(image_left)
    del(frameX)
    time = 0
    keyboard_input_list.clear()
    keyboard_check_list.clear()
    keyboard_default_list.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            start_state.bgm.stop()
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
    global frameX, count, time
    time += game_framework.frame_time
    print(time)

    if(time > max_time):
        main_state.crystal[0].fail_get_crystal.play()
        main_state.life.count -= 1
        game_framework.pop_state()
    elif keyboard_input_list == keyboard_check_list:
        main_state.crystal[0].get_crystal.play()
        main_state.inventory.my_bag.append('crystal')
        frameX = 200
        draw()
        delay(0.1)
        game_framework.pop_state()

    for i in range(len(keyboard_check_list)):
        if keyboard_input_list[i] != keyboard_check_list[i]:
            main_state.crystal[0].fail_get_crystal.play()
            main_state.life.count -= 1
            game_framework.pop_state()


def draw():
    interval = 0
    for i in keyboard_input_list:
        keyboard_default_list[i].clip_draw(frameX, 0, 200, 200, 70 + interval, 600, 100, 100)
        interval += 105
    update_canvas()