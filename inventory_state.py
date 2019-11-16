import game_framework
from pico2d import *
import game_world
import main_state
import shop_state
from inventory import Inventory

name = "IventoryState"


def enter():
    shop_state.draw()

def exit():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE) :
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
                game_framework.pop_state()
            elif event.type == SDL_MOUSEMOTION:
                x, y = event.x, 800 - 1 - event.y

def draw():

    main_state.inventory.draw(280, 400, 560, 800)
    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass