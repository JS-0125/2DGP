import game_framework
from pico2d import *
import game_world
import title_state

name = "ShopState"
shop = None

def enter():
    global shop
    shop = load_image('resourse/shop.png')

def exit():
    global shop
    del(shop)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN,SDLK_ESCAPE) :
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(title_state)

def draw():
    clear_canvas()
    shop.draw(280, 450)

    update_canvas()

def update():
    pass

def pause():
    pass

def resume():
    pass