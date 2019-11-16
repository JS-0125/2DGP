import game_framework
from pico2d import *
import game_world
import title_state
import shop_state
name = "IventoryState"
shop = None


def enter():
    global inventory
    inventory = load_image('resourse/inventory.png')
    shop_state.draw()

def exit():
    global inventory
    del(inventory)


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


def draw():

    inventory.draw(280, 400, 560, 800)

    update_canvas()


def update():
    pass


def pause():
    pass


def resume():
    pass